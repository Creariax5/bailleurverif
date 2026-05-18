#!/usr/bin/env bash
# ingest_orchestrator.sh — Mission 1 §1.1 / DIRECTIVE AUTOMATION-FIRST 2026-05-17T21:14Z
#
# Picks ONE city flagged "pending" in cities_queue.txt, scrapes it via
# locservice_v0.py, then runs pipeline.sh, then marks the city "done <utc-ts>".
# Designed for cron */30 * * * * (one pending city per tick; scrape pace 30s
# × ~30 listings = ~15-25min wall, fits inside the tick).
#
# Concurrency-safe via flock on a single global lockfile (skip if previous run
# still going). Idempotent: 0 pending => exit 0 silently.
#
# Queue format (one line per city):
#   <slug>|<index-url>|<status>|<timestamp>
#   status ∈ {pending, done}.  Timestamp set when status becomes done.
#
# Usage:
#   bash ingest_orchestrator.sh            # normal: scrape first pending
#   bash ingest_orchestrator.sh --dry-run  # skip scrape, still rotate queue + log
#
# Exit codes:
#   0 = clean (whether something was processed or nothing pending)
#   1 = queue parse / scrape / pipeline failure (cron will see it)

set -euo pipefail
shopt -s nullglob

ROOT="/home/deploy/saas-florian"
CRAWLER="$ROOT/crawler"
QUEUE="$CRAWLER/cities_queue.txt"
LOCK="/tmp/ingest_orchestrator.lock"
LOG="$CRAWLER/orchestrator.log"
PIPELINE="$CRAWLER/pipeline.sh"
SCRAPER="$ROOT/wedge-tool/crawler/locservice_v0.py"
LIMIT="${LIMIT:-30}"

DRY_RUN=0
if [ "${1:-}" = "--dry-run" ]; then
  DRY_RUN=1
fi

ts() { date -u +%FT%TZ; }
log() { echo "[$(ts)] $*" >> "$LOG"; }

mkdir -p "$(dirname "$LOG")"

# Single global lock: skip silently if previous run still busy.
exec 9>"$LOCK"
if ! flock -n 9; then
  log "skip: previous orchestrator still running"
  exit 0
fi

if [ ! -f "$QUEUE" ]; then
  log "abort: queue file missing ($QUEUE)"
  exit 1
fi

# Find first pending line. Format: slug|url|status|ts
PENDING_LINE=""
PENDING_LINENO=0
LINENO_=0
while IFS= read -r line || [ -n "$line" ]; do
  LINENO_=$((LINENO_ + 1))
  case "$line" in
    ""|"#"*) continue ;;
  esac
  status="$(printf '%s\n' "$line" | awk -F'|' '{print $3}')"
  if [ "$status" = "pending" ]; then
    PENDING_LINE="$line"
    PENDING_LINENO=$LINENO_
    break
  fi
done < "$QUEUE"

if [ -z "$PENDING_LINE" ]; then
  log "noop: 0 pending in queue (dry_run=$DRY_RUN)"
  exit 0
fi

SLUG="$(printf '%s\n' "$PENDING_LINE" | awk -F'|' '{print $1}')"
URL="$(printf '%s\n' "$PENDING_LINE" | awk -F'|' '{print $2}')"

if [ -z "$SLUG" ] || [ -z "$URL" ]; then
  log "abort: malformed pending line ($PENDING_LINE)"
  exit 1
fi

log "start slug=$SLUG limit=$LIMIT dry_run=$DRY_RUN"

# Per-city lock to make doubly sure two ticks never both scrape the same city.
CITY_LOCK="/tmp/ingest_${SLUG}.lock"
exec 8>"$CITY_LOCK"
if ! flock -n 8; then
  log "skip: city lock busy slug=$SLUG"
  exit 0
fi

# Scrape (or skip in dry-run).
if [ "$DRY_RUN" -eq 0 ]; then
  CRAWLER_LOG="$ROOT/wedge-tool/crawler/logs/orchestrator-$SLUG-$(date -u +%FT%H%MZ).log"
  mkdir -p "$(dirname "$CRAWLER_LOG")"
  log "scrape slug=$SLUG url=$URL log=$CRAWLER_LOG"
  if ! /usr/bin/python3 "$SCRAPER" "$LIMIT" --index-url "$URL" --city-slug "$SLUG" \
        > "$CRAWLER_LOG" 2>&1; then
    log "fail: scrape slug=$SLUG (see $CRAWLER_LOG)"
    exit 1
  fi
  log "scrape ok slug=$SLUG records=$(grep -cE 'DONE wrote [0-9]+ records' "$CRAWLER_LOG" >/dev/null && grep -oE 'DONE wrote [0-9]+ records' "$CRAWLER_LOG" | grep -oE '[0-9]+' || echo 0)"

  log "pipeline trigger date=$(date -u +%F)"
  if ! /bin/bash "$PIPELINE" >> "$LOG" 2>&1; then
    log "fail: pipeline slug=$SLUG"
    exit 1
  fi
  log "pipeline ok slug=$SLUG"
else
  log "dry-run: skip scrape + skip pipeline slug=$SLUG"
fi

# Mark done atomically (rewrite queue via tmp + mv).
NEW_TS="$(ts)"
TMP="$QUEUE.tmp.$$"
awk -F'|' -v OFS='|' -v ln="$PENDING_LINENO" -v ts="$NEW_TS" '
  NR == ln { $3 = "done"; $4 = ts }
  { print }
' "$QUEUE" > "$TMP"
mv "$TMP" "$QUEUE"
log "done slug=$SLUG marked_at=$NEW_TS"
