---
name: TODO-24 reuse data.gouv.fr publié
description: data.gouv.fr reuse 6a0c30a2a24bbe3d7c2e69d4 créé run-287 (cat-4 backlink DR 90 LIVE)
type: decision
---

# Decision — TODO-24 reuse data.gouv.fr publié (run-287 2026-05-19T09:42:58Z)

**Décision** : Soumettre `data-gouv-fr-reuse-payload.json` (4815 octets) via `bash submit-data-gouv-fr-reuse.sh` après dépôt `DGVFR_API_KEY` par Florian dans `.env` (inbox directive 2026-05-19T07:25Z).

**Résultat** : reuse `6a0c30a2a24bbe3d7c2e69d4` créé à 09:42:58.701Z UTC, owner Florian Demartini, 4 datasets cités (DPE ADEME / BAN / Encadrement Paris / JORF).

## Pourquoi (motivation)

- TODO-24 OPEN depuis run-156 (2026-05-17T02:08Z) = 131 wakes blocage Florian-action.
- Asymétrie : 0€ + 0 PII + 1 backlink dofollow gov.fr DR ≈90 + visibilité data analysts/journalistes FR.
- Strategic critic-6 audit-6 a flaggué "cat-4 institutionnel = 0 composant substantif depuis 70+ wakes" → reuse data.gouv.fr = composant substantif unique distinct des mails outbound (qui restent silent 4 press + 3 SMTP + 1 ANIL).
- Florian directive 07:25Z ★★★ explicit override toute alternative NEXT.

## Anomalie observée

`POST /api/1/reuses/` a retourné `HTTP 400 BODY="No connection adapters were found for '!BXPYRqoCVCDSaVpYfV:agent.dinum.tchap.gouv.fr'"` = bug backend data.gouv.fr (URL Matrix/Tchap mal-formée traitée comme HTTP). **Mais la ressource a été créée malgré l'erreur réponse** : `GET /api/1/reuses/?q=bailleurverif` immédiat retourne `total=1` avec le bon `id`. Pattern à mémoriser pour futurs POST.

## URL publique canonique

`https://www.data.gouv.fr/fr/reuses/bailleurverif-observatoire-annonces-loyer-non-conformes-encadrement-dpe-f-g/`
(HEAD 308 redirect normal → 200 sur slug)

## Alternatives rejetées

- **Alt 1 — Attendre ack Florian sur 400 false-positive avant valider** : prudent mais inutile vu vérif GET immédiate retourne ressource existante. Florian peut désavouer wake +N s'il veut suppression.
- **Alt 2 — Re-POST identique** : risque doublon (data.gouv.fr peut accepter ou rejeter selon dedupe règles). Vérif GET avant retry évite ce risque.
- **Alt 3 — Pas exécuter avant strategic critic** : aurait laissé directive Florian ★★★ J+1 stale. Discipline post critic-18 STOP #3 "outreach N+1 J+1 stérile" NE s'applique PAS aux directives Florian explicit.

## Effets observables KPIs

- `data_gouv_fr_reuse_published=true` ★★★ NEW
- `cat_4_dofollow_gov_fr_backlinks_count=0→1` ★★
- `cat_4_institutionnel_outreach_substantive_components=2→3` ★★ (+ reuse distinct des mails)
- `moat_components_live_honest=3/4 maintained` (cat-4 partiel renforcé concrètement)
- `todo_24_status=DONE`

## Rollback

Si Florian veut suppression : `DELETE https://www.data.gouv.fr/api/1/reuses/6a0c30a2a24bbe3d7c2e69d4/` avec `X-API-KEY` Florian (env-only). Pas de side-effects locaux.

## Liens

- Payload : `data-gouv-fr-reuse-payload.json`
- Script : `submit-data-gouv-fr-reuse.sh`
- URL publique : data.gouv.fr/fr/reuses/bailleurverif-observatoire-annonces-loyer-non-conformes-encadrement-dpe-f-g/
- Florian directive : `inbox.md` 2026-05-19T07:25Z
