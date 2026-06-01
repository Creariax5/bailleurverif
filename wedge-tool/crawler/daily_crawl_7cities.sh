#!/usr/bin/env bash
# Daily passive moat-builder : crawl 7 villes Locservice, append JSONL date-stampé.
# Pace 30s/detail (intra-ville) + 60s entre villes. Total ~110-130min.
# Compliance robots.txt Locservice (User-agent:*) + UA identifié.

set -u
cd "$(dirname "$0")"
LOG_DIR=/home/deploy/saas-florian/wedge-tool/crawler/logs
mkdir -p "$LOG_DIR"
TODAY=$(date -u +%F)
LOG="$LOG_DIR/daily-$TODAY.log"

LIMIT=${LIMIT:-100}

declare -a CITIES=(
  "paris|https://www.locservice.fr/paris-75/location.html"
  "lyon|https://www.locservice.fr/rhone-69/location.html"
  "lille|https://www.locservice.fr/nord-59/location.html"
  "marseille|https://www.locservice.fr/bouches-du-rhone-13/location.html"
  "nantes|https://www.locservice.fr/loire-atlantique-44/location.html"
  "toulouse|https://www.locservice.fr/haute-garonne-31/location.html"
  "bordeaux|https://www.locservice.fr/gironde-33/location.html"
)

echo "[daily_crawl] START $(date -u +%FT%TZ) LIMIT=$LIMIT cities=${#CITIES[@]}" >> "$LOG"

for entry in "${CITIES[@]}"; do
  slug="${entry%%|*}"
  url="${entry##*|}"
  echo "[daily_crawl] --- ville=$slug url=$url ---" >> "$LOG"
  /usr/bin/python3 locservice_v0.py "$LIMIT" --index-url "$url" --city-slug "$slug" >> "$LOG" 2>&1
  echo "[daily_crawl] inter-city pause 60s" >> "$LOG"
  sleep 60
done

echo "[daily_crawl] DONE $(date -u +%FT%TZ)" >> "$LOG"

# Best-effort post-run dedupe (silencieux si fail)
/usr/bin/python3 /home/deploy/saas-florian/wedge-tool/scoring/dedupe_listings.py \
  /home/deploy/saas-florian/wedge-tool/data/listings/locservice-*.jsonl \
  -o /home/deploy/saas-florian/wedge-tool/data/listings/all-cities-latest.dedup.jsonl \
  >> "$LOG" 2>&1 || true

# Pipeline dedupe+score+CSV (générates fresh observatoire-annonces-loyer-DATE.csv)
# Added 2026-06-01 — sub-observatoire-publisher was stale because cities_queue=all-done
# meant ingest_orchestrator skipped pipeline.sh. Daily_crawl now triggers pipeline directly.
DATE_TODAY="$(date -u +%F)"
echo "[daily_crawl] pipeline.sh $DATE_TODAY" >> "$LOG"
/bin/bash /home/deploy/saas-florian/crawler/pipeline.sh "$DATE_TODAY" >> "$LOG" 2>&1 || \
  echo "[daily_crawl] pipeline.sh FAILED for $DATE_TODAY" >> "$LOG"
