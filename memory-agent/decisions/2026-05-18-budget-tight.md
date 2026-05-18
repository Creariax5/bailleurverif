# Décision : Budget-tight Florian + memory compact

**Date** : 2026-05-18T06:00Z (run-248ter)
**Status** : ACTIVE

## Décision verbatim Florian

Mode budget-tight : ~$1-1.5/wake juste contexte lecture monolithique 1.6 MB. Diagnostic agent : ~$115/jour Builder à interval 900s.

Mission compact :
1. **Builder interval 900s → 3600s** (1h, -75% sessions/jour)
2. **Lectures sélectives** head/tail patterns 50-100 lignes max
3. **Skip wakes vides** via tools/check_wake_useful.sh (à coder wake +N)
4. **Ledger entries max 200 chars** (anti-bloat)
5. **State.md format compact <300 lignes** (section État courant unique + métriques tableau + décisions actives)
6. **Prompt caching** si support agents-control

## Cible compactage

- ledger 692 KB → <50 KB
- state 556 KB → <30 KB
- inbox 416 KB → <30 KB
- **total <100 KB/wake** (-94%)
- coût/wake $1.20 → $0.15 (-87%)

## Combiné wake 1h + compact

~$3.6/jour Builder vs ~$115/jour actuel (**-97%**)

## Migration mémoire Phase 1 (run-258 ce wake)

Architecture cible `memory-agent/` Obsidian-style :
- MEMORY.md index (~5 KB)
- 9 concepts atomiques (~10 KB total)
- 10 décisions datées (~5 KB total)
- 1 kpis snapshot (~2 KB)
- **TOTAL ~22 KB** vs 1600 KB monolithique (**-98% lecture/wake**)

Économie cible **~$270/mois** (-95% Builder).

## Phase 2 (wake +N)

Patch prompt Builder via agents-control API → pointer `memory-agent/MEMORY.md` au lieu de "Fichiers vivants" complets. Gain ~1 KB/wake supplémentaire.

## Phase 3 (wake +N+M)

Patch Tactical + Strategic Critic prompts (sources à lire changent).

## Anti-drift

- ZERO-POSE compliant (cron driven, no ScheduleWakeup)
- TODO-25 + DPE ADEME ingest restent priorité
- Garder ledger/state/inbox/runs comme archives append-only (transparence GitHub + rollback safe)

## Anti-patterns

- Copier ledger.md complet dans memory-agent (= no gain)
- Créer 100 micro-concepts (over-engineering)
- Skip ritual WHY_THIS_NOT_THAT
