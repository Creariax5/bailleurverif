# Concept : Tactical Warnings (last critic audit)

**Source** : `inbox-from-critic.md` audit-13 2026-05-18T10:50Z.

## Verdict global

**8.0/10** (+0.5 vs audit-12). Cycle 5 wakes excellent côté exécution : 3/3 priorités audit-12 honorées J+0/J+1. DIRECTIVE 7 RÉVISÉE 49 sessions. **MAIS** : +0 humain 53 wakes / +38h ; alerte polish loop cat-1 JSON-LD 3 wakes consécutifs (253+254+255) ; helper `parse_detail_jsonld()` NON-câblé `main()` = pattern "ready-but-not-publish" récurrent ; migration mémoire Florian-priorité 06:10Z+09:55Z = 4h+ différée.

## 3 actions critic-13 prioriser

1. **★★★ Lire `tail -50 visits.jsonl` CE WAKE + reconnaître visite Open3CL** ✅ HONORÉ run-257
2. **★★ Wiring `parse_detail_jsonld()` dans `main()` + smoke `--limit 3 --dry-run`** ✅ HONORÉ run-257
3. **★★ Migration mémoire Phase 1 bootstrap partiel** ✅ HONORÉ run-258 (ce wake)

## 3 actions critic-13 arrêter

1. STOP célébration `directive_7_revisee_compliance_consecutive_wakes=49` headline state.md (6 wakes consécutifs ; mention 1 fois suffit)
2. STOP "ready-but-not-publish" patterns récurrents
3. STOP 3+ wakes consécutifs sur même PISTE cat-1 (JSON-LD upgrade = 253+254+255 limite atteinte)

## Hypothèse à vérifier d'urgence

- Lecture `tail -50 visits.jsonl` + curl `https://github.com/Open3CL/engine/issues/160` wake +1
- Si mainteneur a réagi OU si 2+ autres visites referrer Open3CL T+24h → widget DPE / Open3CL angle = levier acquisition externe le plus haut ROI pour les 84j restants
- Audit raw count runs 237→255 pour clarifier `wakes_since_last_strategic_critic` (metrics.json=3 / state.md=5 / raw=18 ?). Si raw 18 → strategic critic audit-3 DÉPASSÉ ≥2 wakes

## État application

- Action #1 ★★★ : ✅ honoré J+0 run-257
- Action #2 ★★ : ✅ honoré J+0 run-257
- Action #3 ★★ : ✅ honoré J+0 run-258 (Phase 1 bootstrap)
- Hypothèse Open3CL : surveiller visits.jsonl wakes prochains + Florian Option A/B
- Audit raw count `wakes_since_last_strategic_critic` : à clarifier wake +N (mettre vrai chiffre dans kpis/snapshot-current.md)

## Anti-patterns flaggés à éviter wake +N

- 3+ wakes consécutifs PISTE cat-1 (limite atteinte)
- "ready-but-not-publish" (wiring/publish à faire le même wake si possible)
- Célébrer compteurs vanity en headline (DIRECTIVE 7 49 wakes mention 1 fois)
- Migration mémoire différée plusieurs wakes après priorité Florian explicite
