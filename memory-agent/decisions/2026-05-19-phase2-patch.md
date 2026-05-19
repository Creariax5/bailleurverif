# Décision : Phase 2 PATCH agent prompt (compaction memory-agent)

**Date** : 2026-05-19T07:24Z (run-280).
**Source** : ORDRE FLORIAN 06:45Z + Tactical Critic audit-18 ★★★ #1.

## Décision

Patcher le prompt système de l'agent Builder (`Saas 2` ID `42f2c562-927a-45ea-b6ee-ecfadad0d4d6`) via API agents-control pour supprimer les sections devenues redondantes avec `memory-agent/` (Loop d'exécution monolithique state.md/ledger.md/inbox.md → bloc compact memory-agent Obsidian-style depuis run-258).

## Action exécutée

1. **Backup** : `curl GET /api/agents` → `agent-browser/prompts-backup/all-agents-2026-05-19T0645Z.json` 26185 bytes HTTP 200 (5 agents).
2. **Regex substitution** : Python `re.compile(r"## Loop d'exécution chaque wake.*?(?=## Conditions d'arrêt)", re.DOTALL)` 1 match exact + bloc compact memory-agent (PRIMARY READ MEMORY.md + SELECTIVE READ 3-5 concepts + TARGETED READ inbox tail 80 / critic / strategic head 60 + NO READ COMPLET state/ledger + ritual DIRECTIVE 10 + stop SANS ScheduleWakeup).
3. **Diff visuel** `/tmp/old_prompt_saas2.txt` vs `/tmp/new_prompt_saas2.txt` chirurgical lines 56-121 only.
4. **PATCH** : `curl -X PATCH /api/agents/42f2c562-927a-45ea-b6ee-ecfadad0d4d6` JSON payload 5951 bytes HTTP 200.
5. **Verify** : re-fetch `curl GET /api/agents` → builder length=5349 ✓ + 8 checks PASS (memory-agent present / Obsidian / PRIMARY READ / old loop gone / 8 leviers gone / Conditions arret kept / Mission unique kept / DIRECTIVE 7 cron-driven kept).

## Métriques

- `agent_prompt_chars_before=8326`
- `agent_prompt_chars_after=5349`
- `agent_prompt_compaction_pct=35.7%` ★★ NEW
- `tokens_saved_per_wake_estimate=~750` ★ (1 token ≈ 4 chars × N wakes/jour × 90j cible)
- `agent_prompt_patches_executed_lifetime=0→1` ★★★ NEW (capability agents-control activée J+1 24h post discovery)
- `phase_2_memory_migration_status=shipped`

## Observation post-PATCH

- **run-281 (J+0 first wake post-PATCH)** : loop compliance OBSERVÉE (PRIMARY READ MEMORY.md → SELECTIVE READ concepts → TARGETED READ inbox tail 80 + critic + strategic head 60 → NO READ COMPLET state/ledger → WHY_THIS_NOT_THAT ritual).
- `phase_2_patch_observed_first_wake_post_patch=run-281-2026-05-19T07:33Z`
- `phase_2_patch_loop_compliance_observed=true`
- `phase_2_patch_tokens_saved_estimate_per_wake=750`

## Rollback

- Backup intact `agent-browser/prompts-backup/all-agents-2026-05-19T0645Z.json` → rollback manuel possible si critic-19 ou critic-20 flagge dérive comportementale.
- Sections supprimées du prompt (8 leviers / DIRECTIVE 9 / KPIs / Garde-fous légaux) **continuent à vivre** dans `HUMAN_DIRECTIVE.md` + `memory-agent/decisions/`.
