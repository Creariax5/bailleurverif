#!/usr/bin/env bash
# pipeline.sh — Mission 1 / DIRECTIVE AUTOMATION-FIRST (2026-05-17T21:14Z brief Florian)
#
# Idempotent ingest pipeline run AFTER a scrape has appended a new
# locservice-<city>-YYYY-MM-DD.jsonl in wedge-tool/data/listings/.
# Re-deduplicates ALL locservice-*-<date>.jsonl, re-scores, regen CSV.
# Safe to call repeatedly: same input set => same output (dedupe by accommodation_id).
#
# Does NOT touch observatoire-annonces-loyer.html / llms.txt / llms-full.txt
# (those publish steps require judgment per Critic-9 §"max 1×/24h, Δ≥50 OR new IN-SCOPE city"
#  and stay manual / Builder-driven for now).
#
# Usage: bash pipeline.sh [YYYY-MM-DD]   (default: today UTC)
# Exit code 0 = clean, non-zero = something failed (cron will see it).

set -euo pipefail

DATE="${1:-$(date -u +%F)}"
ROOT="/home/deploy/saas-florian/wedge-tool"
LISTINGS="$ROOT/data/listings"
SCORING="$ROOT/scoring"
EXPORTER="$ROOT/export_observatoire_csv.py"

DEDUP="$LISTINGS/all-cities-$DATE.dedup.jsonl"
SCORED="$LISTINGS/all-cities-$DATE.dedup.scored.jsonl"
REPORT="/home/deploy/saas-florian/crawler/last_ingest_report.txt"

shopt -s nullglob
INPUTS=( "$LISTINGS"/locservice-*-"$DATE".jsonl )
if [ ${#INPUTS[@]} -eq 0 ]; then
  echo "[pipeline] no locservice-*-$DATE.jsonl inputs found, abort" >&2
  exit 1
fi

# Skip .scored.jsonl artefacts that share the locservice- prefix (e.g. paris .scored).
INPUTS_FILTERED=()
for f in "${INPUTS[@]}"; do
  case "$f" in
    *.scored.jsonl) ;;
    *) INPUTS_FILTERED+=( "$f" ) ;;
  esac
done

echo "[pipeline] date=$DATE inputs=${#INPUTS_FILTERED[@]}"

python3 "$SCORING/dedupe_listings.py" -o "$DEDUP" "${INPUTS_FILTERED[@]}"
python3 "$SCORING/conformity_score.py" -o "$SCORED" "$DEDUP"
python3 "$EXPORTER"
python3 "$ROOT/cross_wave_persistence.py" || true

# Derive headline stats from the scored file for the report line.
STATS=$(python3 - <<PY
import json
from collections import Counter
in_scope = vio = clear = presumed = 0
communes = Counter(); villes = Counter()
n_total = 0
with open("$SCORED") as f:
    for line in f:
        r = json.loads(line); n_total += 1
        if r.get("commune_slug"):
            in_scope += 1
            communes[r["commune_slug"]] += 1
            villes[r.get("ville_label")] += 1
            v = r.get("encadrement_violation", "none")
            if v != "none": vio += 1
            if v == "clear": clear += 1
            elif v == "presumed": presumed += 1
pct = (100.0 * vio / in_scope) if in_scope else 0.0
print(f"N={n_total} in_scope={in_scope} vio={vio} clear={clear} presumed={presumed} "
      f"headline={pct:.1f}% communes={len(communes)} villes={len(villes)}")
PY
)

mkdir -p "$(dirname "$REPORT")"
TS=$(date -u +%FT%TZ)
echo "$TS | $STATS" >> "$REPORT"
echo "[pipeline] $TS | $STATS"

# ===== Cumulative CSV (all waves merged, dedupe by accommodation_id, keep latest)
# Added 2026-06-01 — single-wave CSV stuck at N≈210, this exposes the 800+ accumulated.
DEDUP_CUM="$LISTINGS/all-cities-cumulative.dedup.jsonl"
SCORED_CUM="$LISTINGS/all-cities-cumulative.dedup.scored.jsonl"
ALL_INPUTS=( "$LISTINGS"/locservice-*-*.jsonl )
ALL_FILTERED=()
for f in "${ALL_INPUTS[@]}"; do
  case "$f" in
    *.scored.jsonl) ;;
    *) ALL_FILTERED+=( "$f" ) ;;
  esac
done
echo "[pipeline cumulative] inputs=${#ALL_FILTERED[@]}"
python3 "$SCORING/dedupe_listings.py" -o "$DEDUP_CUM" "${ALL_FILTERED[@]}"
python3 "$SCORING/conformity_score.py" -o "$SCORED_CUM" "$DEDUP_CUM"
python3 "$EXPORTER" cumulative

CUM_STATS=$(python3 - <<PY
import json
from collections import Counter
in_scope = vio = clear = presumed = 0
communes = Counter(); villes = Counter()
n_total = 0
with open("$SCORED_CUM") as f:
    for line in f:
        r = json.loads(line); n_total += 1
        if r.get("commune_slug"):
            in_scope += 1
            communes[r["commune_slug"]] += 1
            villes[r.get("ville_label")] += 1
            v = r.get("encadrement_violation", "none")
            if v != "none": vio += 1
            if v == "clear": clear += 1
            elif v == "presumed": presumed += 1
pct = (100.0 * vio / in_scope) if in_scope else 0.0
print(f"N={n_total} in_scope={in_scope} vio={vio} clear={clear} presumed={presumed} "
      f"headline={pct:.1f}% communes={len(communes)} villes={len(villes)}")
PY
)
echo "$TS | CUMULATIVE $CUM_STATS" >> "$REPORT"
echo "[pipeline cumulative] $TS | $CUM_STATS"
