#!/usr/bin/env bash
# Auto-submit du payload data-gouv-fr-reuse-payload.json sur data.gouv.fr/api/1/reuses/
#
# Usage :
#   export DGVFR_API_KEY="<la clé que Florian colle dans inbox.md ligne TODO-24 api-key:>"
#   bash submit-data-gouv-fr-reuse.sh
#
# La clé est lue depuis l'env, jamais persistée disque. Discipline post-incident.
# Sortie : reuse_id + URL canonique du reuse publié, à archiver dans ledger.md.
set -euo pipefail

PAYLOAD="$(dirname "$0")/data-gouv-fr-reuse-payload.json"

if [[ -z "${DGVFR_API_KEY:-}" ]]; then
  echo "ERR: export DGVFR_API_KEY avant d'exécuter ce script."
  echo "     Florian colle la clé dans inbox.md ligne 'TODO-24 api-key: xxxx',"
  echo "     l'agent l'export ici, run le script, puis instruit Florian de révoquer."
  exit 2
fi

if [[ ! -f "$PAYLOAD" ]]; then
  echo "ERR: payload introuvable: $PAYLOAD"
  exit 2
fi

echo "→ POST https://www.data.gouv.fr/api/1/reuses/  ($(wc -c <"$PAYLOAD") octets)"

RESP="$(curl -sS -w '\n__HTTP_CODE__=%{http_code}\n' \
  -X POST "https://www.data.gouv.fr/api/1/reuses/" \
  -H "X-API-KEY: ${DGVFR_API_KEY}" \
  -H "Content-Type: application/json" \
  -H "User-Agent: BailleurVerifCompliance/0.1 (+https://bailleurverif.fr; contact@bailleurverif.fr) reuse-submission" \
  --data @"$PAYLOAD")"

HTTP="$(printf '%s\n' "$RESP" | sed -n 's/^__HTTP_CODE__=\(.*\)$/\1/p')"
BODY="$(printf '%s\n' "$RESP" | sed '/^__HTTP_CODE__=/d')"

echo "HTTP=$HTTP"
echo "BODY:"
echo "$BODY"

if [[ "$HTTP" == "201" ]]; then
  REUSE_ID="$(printf '%s' "$BODY" | python3 -c 'import sys,json; print(json.load(sys.stdin).get("id",""))')"
  REUSE_URL="https://www.data.gouv.fr/fr/reuses/$REUSE_ID/"
  echo
  echo "✅ Reuse publié : $REUSE_URL"
  echo "→ Backlink dofollow gov.fr DR 90 actif."
  echo "→ Rappel : Florian doit révoquer la clé dans https://www.data.gouv.fr/fr/admin/me/ → API Key"
  exit 0
else
  echo "❌ Échec submission (HTTP $HTTP)."
  exit 1
fi
