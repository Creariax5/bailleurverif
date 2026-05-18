#!/usr/bin/env bash
# legifrance_dila_weekly.sh — cat-3 ingest cadence wrapper (run-266 ship)
#
# Runs the DILA LEGI bulk fetcher with bail/loyer keywords, deduplicates
# against a persistent index of LEGIARTI IDs already seen, and appends a
# timestamped run entry to data/legifrance/_weekly_runs.jsonl.
#
# Compounding evidence: each git commit of _weekly_runs.jsonl + delta JSONL
# crypto-timestamps the ingestion server-side (GitHub) at week N — a chain
# a concurrent cannot retroactively reproduce.
#
# Intended cron (weekly Sunday 04:17 UTC, low VPS load + post-DILA daily push):
#   17 4 * * 0  cd /home/deploy/saas-florian && bash crawler/legifrance_dila_weekly.sh >> crawler/weekly.log 2>&1
#
# Manual run:
#   bash crawler/legifrance_dila_weekly.sh
set -euo pipefail

cd "$(dirname "$0")/.."

KEYWORDS="bail,loyer,encadrement,locatif,location,baux,habitation,logement"
MAX_ARTICLES=200
STAMP="$(date -u +%Y%m%d-%H%M%SZ)"
OUT_DIR="data/legifrance"
PUBLIC_DIR="wedge-tool/static/data/legifrance"
INDEX_FILE="${PUBLIC_DIR}/_index_bail_loyer.jsonl"
RUNS_LOG="${PUBLIC_DIR}/_weekly_runs.jsonl"

mkdir -p "${OUT_DIR}" "${PUBLIC_DIR}"
touch "${INDEX_FILE}" "${RUNS_LOG}"

echo "[weekly $STAMP] fetch latest-delta keywords=${KEYWORDS} max=${MAX_ARTICLES}"
RAW_OUT="${OUT_DIR}/legi-weekly-${STAMP}.jsonl"
FETCH_STDERR="${OUT_DIR}/legi-weekly-${STAMP}.stderr"
python3 crawler/legifrance_dila_fetch.py \
  --latest-delta \
  --keywords "${KEYWORDS}" \
  --max-articles "${MAX_ARTICLES}" \
  --out "${RAW_OUT}" 2> >(tee "${FETCH_STDERR}" >&2)

# Articles scanned/extracted in this run
SCANNED=$(wc -l < "${RAW_OUT}" 2>/dev/null || echo 0)

# Deduplicate against persistent index; append only LEGIARTI IDs not seen.
# Index stores one {"id":..., "first_seen_run_ts":..., "num":...} per article.
NEW_COUNT=$(python3 - <<PY
import json, sys
from pathlib import Path

index_file = Path("${INDEX_FILE}")
raw_file = Path("${RAW_OUT}")
stamp = "${STAMP}"

seen = set()
if index_file.exists():
    for line in index_file.read_text().splitlines():
        if not line.strip():
            continue
        try:
            seen.add(json.loads(line)["id"])
        except Exception:
            pass

new = []
if raw_file.exists():
    for line in raw_file.read_text().splitlines():
        if not line.strip():
            continue
        try:
            art = json.loads(line)
        except Exception:
            continue
        aid = art.get("id")
        if not aid or aid in seen:
            continue
        seen.add(aid)
        new.append({
            "id": aid,
            "num": art.get("num", ""),
            "texte_num": art.get("texte_num", ""),
            "etat": art.get("etat", ""),
            "date_debut": art.get("date_debut", ""),
            "first_seen_run_ts": stamp,
        })

with index_file.open("a") as f:
    for entry in new:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

print(len(new))
PY
)

# Append weekly run summary (one JSON line)
# Archive name is announced by the fetcher on stderr: "[latest] picked LEGI_YYYYMMDD-HHMMSS.tar.gz"
ARCHIVE_USED=$(grep -oE 'LEGI_[0-9]{8}-[0-9]{6}\.tar\.gz' "${FETCH_STDERR}" 2>/dev/null | head -1 || echo "")
rm -f "${FETCH_STDERR}"
SUMMARY=$(python3 -c "
import json
print(json.dumps({
  'run_ts': '${STAMP}',
  'kind': 'weekly_cadence_run',
  'keywords': '${KEYWORDS}'.split(','),
  'max_articles': ${MAX_ARTICLES},
  'articles_extracted': ${SCANNED},
  'new_legiarti_ids': ${NEW_COUNT},
  'raw_jsonl': '${RAW_OUT}',
  'archive_used': '${ARCHIVE_USED}',
  'index_total_after': sum(1 for _ in open('${INDEX_FILE}')),
}, ensure_ascii=False))
")
echo "${SUMMARY}" >> "${RUNS_LOG}"

echo "[weekly $STAMP] extracted=${SCANNED} new=${NEW_COUNT}"
echo "[weekly $STAMP] summary: ${SUMMARY}"
echo "[weekly $STAMP] OK — review ${RAW_OUT}, then 'git add ${RUNS_LOG} ${INDEX_FILE} ${RAW_OUT} && git commit -m \"legifrance weekly ${STAMP}\" && git push'"
