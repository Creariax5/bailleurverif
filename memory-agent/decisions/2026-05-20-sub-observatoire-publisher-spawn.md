---
name: Sub-observatoire-publisher spawn
description: 4ᵉ sous-agent Haiku 4.5 interval 7j spawné run-317 (brief Florian 2026-05-20T05:40Z "Oui go") republie ressource CSV observatoire hebdo dataset data.gouv.fr 6a09ca8088345193c180e0b5
type: project
---

# Sub-observatoire-publisher — spawn run-317 2026-05-20T06:31Z

**Trigger** : Brief Florian inbox.md HEAD 2026-05-20T05:40Z (verbatim "Oui go"). Découverte 05:30Z page dataset data.gouv.fr : 17 vues + 1 téléchargement 2j (signal positif) MAIS warning "fréquence non respectée" (déclaré `daily` initialement, last update 2026-05-17 +3j). Florian a PATCH frequency `daily→weekly` (warning supprimé). Prochain trigger auto = 2026-05-24 (+7j post 2026-05-17). Sans nouvelle ressource d'ici là, warning revient.

**Décision** : spawn 4ᵉ sous-agent dédié automation perpétuelle.

## Payload spawn

- **ID** : `576fb185-9c51-4ca9-9453-ac9088a223ac`
- **Model** : `claude-haiku-4-5-20251001`
- **Schedule** : `interval` 604800s (7j)
- **Enabled** : 1
- **Prompt** : 6396 chars (hash `8ecbb525d87e22c5`) — source `agent-browser/sub_observatoire_publisher_prompt.md`
- **Backup** : `agent-browser/prompts-backup/sub-observatoire-publisher-create-2026-05-20T0631Z.json`
- **Log path** : `data/sub-agents/sub-observatoire-publisher.jsonl`

## Tâches (séquentielles)

1. Charger env (`_load_env_if_missing(['DGVFR_API_KEY'])`)
2. Détecter dernière vague CSV `observatoire-annonces-loyer-YYYY-MM-DD.csv` fresh ≤7j (sinon `no_fresh_data` + STOP)
3. Compute metadata (N, villes_count)
4. Dédup : GET dataset resources, skip si titre date déjà présent
5. POST `/upload/` multipart sur dataset `6a09ca8088345193c180e0b5`
6. PUT metadata ressource (titre + description + format csv + type main)
7. Log jsonl 1 ligne (outcome, resource_id, csv_date, N, villes_count, http_status)
8. Commit jsonl (PAS push, Builder agglomère, cap 2 fichiers)

## Hard bans

- ❌ Re-publier MÊME CSV (date identique) — dédup step 4 obligatoire
- ❌ Modifier dataset metadata global (frequency/description/license/title)
- ❌ Toucher reuse `6a0c30a2a24bbe3d7c2e69d4`
- ❌ Modif `.env`, `*.html`, `*.py`, `wedge-tool/server.py`
- ❌ Spawn autres sous-agents / ScheduleWakeup / git push / commit >2 fichiers

## Exit clause

3 cycles `no_fresh_data` consécutifs → log `pipeline_dead` + Builder PATCH `enabled=0` au wake suivant.

## WHY spawn NOT Builder direct chaque 7j

- (a) Florian explicit verbatim "Oui go" — autorisation maximum
- (b) Asymétrie : 1 wake Builder Opus (~€0.10 capex) = data.gouv.fr DR 90 reste fresh perpétuel sans charge Builder récurrente (cycle Haiku ~€0.03 × 4/mois = €0.12/mois)
- (c) Cap budget €20/mois 8 sous-agents = €0.12 négligeable, 4ᵉ slot (drafter 3ᵉ, judilibre 1ᵉʳ disabled saturated_3, seo-monitor 2ᵉ)
- (d) Tâche déterministe (multipart upload + log jsonl) = Haiku 4.5 suffisant, pas besoin nuance Sonnet
- (e) Test diagnostic Builder discipline : si Builder oublie 7j manual = warning revient, fail visible

## WHY Haiku NOT Sonnet/Opus

Tâche purement mécanique (curl multipart + JSON parse) sans créativité. Haiku 4.5 livre 95% capability à 5% du coût Opus. Sonnet réservé tasks nuancées (sub-linkedin-drafter).

## Coût attendu

- Capex spawn run-317 : ~€0.10 (1 wake Opus)
- Opex récurrent : ~€0.03/cycle × 52 cycles/an = ~€1.56/an (€0.13/mois)
- Asymétrie : ROI = signal Google Dataset Search "actively maintained" + zéro warning data.gouv.fr + cat-1 visibility perpétuel

## Update artifacts

- `agent-browser/sub-agents-registry.json` : +1 entry (4ᵉ agent)
- `memory-agent/concepts/sub-agents-active.md` : table refresh + use-case #3 marked SHIPPED
- `MEMORY.md` : ligne sub-agents passe 3→4
- `florian-todos.md` : § SOUS-AGENTS ACTIFS +1 ligne (sera fait next wake si rotation déjà différée)
- `ledger.md` : 1 entry ACTION + 1 entry METRIC
