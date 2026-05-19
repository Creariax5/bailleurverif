# Décision — Sub-agents capability activée + 1er sous-agent spawné

**Date** : 2026-05-19T12:28Z
**Run** : run-297
**Type** : Architecture / Cost-optimization
**Statut** : Immutable post-decision

## Context

Florian a shippé 2026-05-19T11:55Z (brief TOP inbox) un champ `model` sur `/api/agents` agents-control + connector test bout-en-bout 12:00Z (`--model claude-haiku-4-5-20251001` correctement passé au CLI, vérifié `/proc/PID/cmdline`). Coût Haiku ≈ 1/7-1/10 d'Opus sur inférence comparable, qualité OK pour tasks déterministes.

## Décision

1. **Activer capability** sub-agents pour routines déterministes (parsing, enrichment, dedup, scoring).
2. **Builder Opus = seule entité** autorisée à POST/PATCH/DELETE sous-agents (anti-spawn-bomb).
3. **Naming convention obligatoire** : prefix `sub-` (= subordonné Builder).
4. **Garde-fous obligatoires** :
   - Time-box ≤5 min/wake.
   - Exit clauses explicites (saturated / api_fail / drift_avoided / error).
   - Log dédié `data/sub-agents/<name>.jsonl` 1 ligne/wake.
   - Hard bans : no .env edit, no git push, no Claude API external, no spawn, no PATCH/DELETE autres agents, no ScheduleWakeup.
   - Backup payload pré-création `agent-browser/prompts-backup/`.
   - Registry tracking `agent-browser/sub-agents-registry.json` append-only.
5. **Limits** : ≤6 sous-agents simultanés, budget €20/mois total.
6. **1er spawn** : `sub-judilibre-enrich` (Haiku 4.5, interval 1h, id `2bbb1dc8-1336-4b64-890b-063c486de4aa`).
7. **Anti-spawn-bomb** : ≥2 cycles observés OK avant spawn 2ᵉ sous-agent (discipline Florian explicite).

## Rationale

- Sous-agent Haiku libère ~70% budget Builder Opus pour décisions stratégiques (Florian).
- Routines déterministes = pattern match + API + JSON merge → Haiku saturant.
- 5 use-cases prescrits Florian (judilibre / imap / crawler / linkedin / observatoire publisher) couvrent ~80% wakes Builder routiniers actuels.
- Risque spawn-bomb mitigé par : Builder = seul créateur, prompt strict 7 hard bans, registry + log + budget cap.

## Conséquences

- Wakes Builder Opus dégagés pour : stratégie, décisions, audits critic, pivot product.
- Capacité d'exécution parallèle (sub-agents 1h vs Builder 15 min) = compound moat plus rapide.
- Surveillance Builder requise chaque wake : check `data/sub-agents/<name>.jsonl` tail 3 lignes.

## Source-of-truth

- Registry : `agent-browser/sub-agents-registry.json`.
- Concept courant : `memory-agent/concepts/sub-agents-active.md`.
- Florian visibility : `florian-todos.md` section `## SOUS-AGENTS ACTIFS`.
