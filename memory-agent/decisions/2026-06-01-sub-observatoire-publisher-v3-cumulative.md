# 2026-06-01T17:45Z — sub-observatoire-publisher v3 cumulative

**Run** : run-402
**Trigger** : Brief Florian inbox HEAD 2026-06-01T14:30Z « OBSERVATOIRE SCALE : N=210→843 (×4) + LIMIT 30→100 + CSV cumulative » — section "Action agent — push cumulative sur data.gouv au prochain cycle", option (a) recommandée (NEW resource permanente cumulative en plus du single-wave).

**État entrée** :
- Cumulative CSV existe : `wedge-tool/static/data/observatoire-annonces-loyer-cumulative.csv` (N=843 cumulatif 12 vagues, généré par `crawler/pipeline.sh` section "Cumulative CSV" 2026-06-01T14:27Z).
- Resource cumulative déjà publiée par Florian manuellement à 14:30Z : ID `9a8426d7-e5ef-4acd-adfa-d2041251e054` sur dataset `6a09ca8088345193c180e0b5`. Titre : "Observatoire annonces non-conformes — CUMULATIVE (toutes vagues, dédupliqué)".
- Sub-observatoire-publisher v2 (8634 chars) ne le maintient pas → restera stale dès qu'une nouvelle vague crawl arrive.

**Décision** :
PATCH v3 sub-observatoire-publisher pour qu'il maintienne automatiquement la cumulative à chaque cycle (1×/7j).

**Implémentation** :
1. Étape **6.25** ajoutée entre 6 (PATCH metadata single-wave) et 6.5 (HF) :
   - Cible figée resource_id `9a8426d7-e5ef-4acd-adfa-d2041251e054` (jamais re-créer)
   - POST `/datasets/<id>/resources/<resource_id>/upload/` remplace fichier
   - PUT metadata rafraîchit titre + description avec N_cum + date
   - Fail-soft (cumulative fail n'affecte ni single-wave step 5 ni HF step 6.5)
2. Schéma log jsonl étendu v3 : `cumulative_outcome` / `N_cum` / `villes_count_cum` / `cumulative_error`.
3. Hard bans ajoutés : ❌ NE PAS créer 2ᵉ ressource cumulative / ❌ NE PAS toucher resources autres (b64c8670 Plafonds JSON, 98b56f97 Plafonds barème, 7c20a3c3 Méthodologie).
4. Compactage step 1 (env loader Python remplacé par 1 ligne référence "helper standard") + step 3 (metadata compute one-liner) + step 6.5 (HF section condensée) pour rester sous limite API (10000 chars enforced HTTP 400 "prompt too long").

**Métriques** :
- Prompt : 8634 → 9605 chars (+971 chars net, ajout contenu cumulative ≈1400 chars compensé par 430 chars compactés env/metadata/HF).
- Hash : `6e432483f1eca7f8` → `f62bfeb5bcdbaea0`.
- Backup : `agent-browser/prompts-backup/sub-observatoire-publisher-patch-v3-cumulative-2026-06-01T1745Z.json`.
- PATCH HTTP 200 confirmé via agents-control `/api/agents/576fb185...` enabled=1.

**Carve-out gouvernance** :
- DIRECTIVE 10 §c-bis (Brief Florian > Strategic Critic) authorize override ban audit-36 "0 patch sub-agents" (Florian explicit "À implémenter dans `sub-observatoire-publisher` next iteration").
- Précédent run-401 même wake : KILL sub-seo-monitor + PATCH sub-content-syndicator déjà overriden ban audit-36 sous brief Florian 15:00Z audit hebdo (checklist `ROI=0 4+ cycles → enabled=0`).
- 2 patches sub-agent même wake = exceptionnel, justifié par 2 briefs Florian directs distincts (14:30Z observatoire scale + 15:00Z audit hebdo).
- Bans audit-36 13/14 toujours respectés strict (0 ship code prod / 0 NEW FILE user-facing / 0 city-page / 0 touch 6 surfaces / 0 monétisation / 0 Telegram / 0 ScheduleWakeup / 0 méta-Q / 0 spawn 7ᵉ / 0 SMTP / 0 IndexNow / 0 Indexing API ping / 0 inbox.md HEAD write).

**Critère succès T+7j (next cycle ≈ 2026-06-03T06:31Z) si CSV fresh ≤7j présent** :
- `cumulative_outcome=ok` dans jsonl post-cycle 2
- last_modified ressource `9a8426d7-...054` > 2026-06-01T14:30Z (proof MAJ effective sub-agent vs manuel Florian)
- Titre resource rafraîchi avec date du jour cycle
- Si fail → root cause investigation : (a) endpoint API data.gouv accept-il `/resources/<id>/upload/` ? (b) format payload PUT JSON OK ?

**Critère échec** :
- Si `cumulative_outcome=fail` 2 cycles consécutifs (≥2026-06-10) → patch debug ou refactor.
- Si jamais cumulative-resource créée doublon (anti-hardrule violé) → urgent rollback + delete doublon manuel Florian.

**Asset cumul gouvernance** :
- 3ᵉ patch sub-observatoire-publisher (v1 create→v2 HF→v3 cumulative)
- 7ᵉ patch sub-agent global cumul lifetime (`sub_agents_patched_lifetime` 7→8).
- Brief Florian honored J+0 T+~3h15 substantive (brief 14:30Z → patch 17:45Z, dans 1ʳᵉ session post-brief).
- `florian_briefs_honored_j0_lifetime` 8→9 ★.
