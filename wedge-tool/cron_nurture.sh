#!/bin/bash
# Brief Florian P0 2026-06-05T08:15Z run-446 — nurture poll hourly.
# Reads CRON_SECRET from .env, POST /api/cron/nurture, logs result.
set -eo pipefail
ENV_FILE="/home/deploy/saas-florian/.env"
LOG="/home/deploy/saas-florian/wedge-tool/cron_nurture.log"
SECRET=$(grep '^BAILLEURVERIF_CRON_SECRET=' "$ENV_FILE" | cut -d= -f2)
if [ -z "$SECRET" ]; then
    echo "[$(date -u +%FT%TZ)] no CRON_SECRET in .env" >> "$LOG"
    exit 0
fi
RESP=$(curl -s -X POST http://127.0.0.1:8102/api/cron/nurture \
    -H "X-Cron-Secret: $SECRET" \
    -H 'Content-Type: application/json' \
    -d '{}' --max-time 300 || echo '{"error":"curl_failed"}')
echo "[$(date -u +%FT%TZ)] $RESP" >> "$LOG"
