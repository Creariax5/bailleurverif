---
name: Tactical Warnings (last critic audit)
description: État vivant du dernier audit Tactical Critic, prescriptions ★★★/★★, statut suivi
type: project
---

# Concept : Tactical Warnings (last critic audit)

**Source** : `inbox-from-critic.md` **audit-19 2026-05-19T09:55Z** (post run-287).

## Verdict global

**8.7/10** (+0.1 vs audit-18). 2 directives Florian ★★★ honored J+0 run-287 + Phase 2 PATCH J+0 run-280 + 8 commits + 0 ScheduleWakeup 8/8 + cyclage 4/4.

**MAIS** :
1. **state.md/metrics.json stale 3h+** — désync 3 sources of truth depuis Phase 2 PATCH.
2. **Ritual §b omis 3/8** runs 285-287 (Copyability check + Moat category fields manquants).
3. **ip 2124423717 09:47Z non-investigué** (deep-nav OBS→HOME T+4h12min post-ANIL).
4. **82 wakes 0 humain newly engaged**.

## 3 actions critic-19 prioriser

1. **★★★ FIXER désync state.md + metrics.json** — choisir explicit (a) reprendre headlines 280-287 OU (b) deprecate state.md ligne 1 + amend HUMAN_DIRECTIVE. ✅ HONORÉ run-289 J+0 (option b choisie : déprécation explicite + pointeurs vers ledger.md + memory-agent/. Decision file `decisions/2026-05-19-state-md-deprecated.md`).
2. **★★ Investiguer ip 2124423717** 09:47Z deep-nav OBS→HOME T+4h12min post-ANIL = écho potentiel. UPDATE `concepts/traffic-signals.md`. ⏳ PENDING run-290 (DIRECTIVE 7 ZERO-POSE = 1 ★★★ ce wake, ★★ wake +1).
3. **★★ Ritual §b strict** runs 288+ : fields "Copyability check : X%" + "Moat category : <N>" obligatoires. ✅ HONORÉ run-289 (Copyability ≈95%, Moat N/A — méthode/hygiène pas composant).

## 3 actions critic-19 arrêter

1. **STOP grossissement `kpis/snapshot-current.md`** append-only. Rotation history/ ≤200 lignes. ⏳ PENDING — rotation prochaine wake.
2. **STOP "déficit TODO-24/28 rattrapé glorieusement"** : agent a tardé 2h15+ self-noticing creds. ✅ HONORED run-289 (PLAN-NEXT n'invoque pas "rattrapage glorieux", language neutre).
3. **STOP "wait cron J+1" cat-1** : 4/8 wakes memory-agent = polish-méta risque. ✅ HONORED run-289 (action déprécation = élimine source polish-méta, pas en ajoute).

## Hypothèse à vérifier d'urgence

**ip 2124423717 09:47Z = écho ANIL ou bot ?** Si récurrence 24h → cat-4 substantif candidat. À investiguer run-290 ★★ #2.

## Anti-patterns flaggés à éviter wake +N

- Backfill state.md (déprécation actée).
- Grossissement snapshot-current.md sans rotation history/.
- "Rattrapage glorieux" rhétorique self-congratulatoire.
- Investigation IP reportée 2 wakes consécutifs (faire run-290 strictement).
- Polish-méta memory-agent > 1/4 wakes (cap audit-19).
