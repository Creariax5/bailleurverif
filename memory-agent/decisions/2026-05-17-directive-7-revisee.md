# Décision : DIRECTIVE 7 RÉVISÉE — Cron-driven pacing

**Date** : 2026-05-17T15:00Z (verbatim Florian 14:58Z)
**Status** : ACTIVE (jusqu'à `humans_engaged_lifetime ≥ 5000`)

## Décision verbatim Florian

> "pas besoin que l'agent fasse un schedule wakeup, car j'ai un cron qui le lance toutes les 15 minutes, donc il travaille à peu près 10 minutes et 5 plus tard il est re-réveillé."

## Règle dure

- **L'agent N'APPELLE PAS `ScheduleWakeup`** en fin de session. **JAMAIS.**
- Fin de session = commit éventuel + ledger NEXT (description plan) + stop.
- Le cron externe `*/15 * * * *` côté agents-control relance.
- **Builder interval** : `3600s` (1h) depuis run-248ter 2026-05-18T06:00Z (budget-tight).
- **Pas de boucle d'auto-relance**.

## Pourquoi (correction architecturale)

Version précédente disait "ScheduleWakeup ≤ 60s". **C'était faux.** Si agent appelle ScheduleWakeup 60s, il se relance avant le tick cron suivant → wakes parallèles + sessions concurrentes + doublement coûts API + race conditions sur fichiers partagés (inbox.md/ledger.md/state.md).

## Anti-patterns

- ❌ `ScheduleWakeup 60s/270s/300s/3600s` en fin session (relance avant cron tick = doublons)
- ❌ Convention textuelle ledger `"ScheduleWakeup 60s. Cible run-X ≈ HH:MMZ"` qui se transforme en vrai appel runtime
- ✅ Fin session = ledger NEXT description plan + stop. Cron prend relais.
- ✅ Pendant les ~10 min session = action substantive (ship / research / fix / brief Florian).

## Exception unique

Signal externe précis avec horizon < 5 min (justifier explicitement dans ledger pourquoi malgré cron 15 min).

## KPIs

- `directive_7_revisee_compliance_consecutive_wakes` : 50 wakes consécutifs au 2026-05-18T11:08Z (50ᵉ session conforme, milestone)
- `schedulewakeup_calls_this_wake` : 0 cible permanente
