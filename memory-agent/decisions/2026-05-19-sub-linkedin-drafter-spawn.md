# 2026-05-19 — Sub-linkedin-drafter Sonnet 4.6 spawn (3ᵉ sous-agent)

**Run** : run-304 (2026-05-19T16:35Z)
**Décideur** : Builder Opus 4.7 sur ordre explicite Florian (inbox.md 16:XXZ brief priorité #1).

## Décision

Spawn 3ᵉ sous-agent `sub-linkedin-drafter` :
- **Model** : `claude-sonnet-4-6`
- **Interval** : 86400s (24h)
- **ID agents-control** : `d1a89a62-26ab-4223-8f21-0eae41ca7e97`
- **Status** : enabled (stopped pre-1er tick)
- **Use-case** : drafte 1 post LinkedIn/jour basé sur dernier signal data frais (ledger METRIC ★ NEW / sub-judilibre cycle / observatoire wave / KPI snapshot). Output append-only `social-drafts.md` section LINKEDIN-AUTO + log jsonl. Florian valide en 30s + poste à son rythme sur compte perso (8000 followers FR immo/tech).

## Justification

1. **Brief Florian explicite TOP inbox.md 16:XXZ** : sous-agent `sub-linkedin-drafter` (Sonnet 4.6, interval 24h) déclaré "prioritaire #1" suite à TODO-23 partial done (post LinkedIn organique 2026-05-18T15:45Z → +10 visites/17h P10 = canal externe humain validé).
2. **Sonnet 4.6 nécessaire** (vs Haiku 4.5) : drafting LinkedIn FR-immo nuancé (tone, narrative arc, CTA), pas déterministe. Haiku produirait flat copy. Coût marginal ≈$0.04-0.08/cycle Sonnet.
3. **Asymétrie ROI** : 1 wake Builder Opus €0.10 spawné → ~€2-3/mois opex Sonnet pour cadence 1 post/sem qualité validée par Florian → ~40 visites/sem additionnelles vs baseline ~5/jour humains réels filtrés. Compound moat cat-4 distribution.
4. **Cap 6 → 8** sous-agents : brief Florian autorise scaling horizontal pour absorber shortfall cron `0 * * * *` (1 wake/h Builder, -75% vélocité brute).

## Garde-fous

- Time-box dur 8 min/cycle.
- Hard bans (.env, *.html, git push, agents-control API, spawn, ScheduleWakeup, LinkedIn post direct, fabriquer chiffres).
- Exit clause `drift_avoided` si aucun signal frais 24h (pas de post fabriqué).
- Anti-duplication : lire 3 derniers drafts pour varier angle.
- Auto-rollback Builder : PATCH `enabled=0` si 2 cycles consécutifs error OU no-op.

## Effet attendu

- T+24h : 1er draft généré (cycle 1 ~2026-05-20T16:31Z).
- T+7j : 7 drafts proposés (théorique). Florian valide les meilleurs (~1-3 prévisibles selon qualité signal frais journalier).
- Cible KPI : +40 visites/sem incrementales si 1 post/sem validé moyenne.

## Liens

- Backup payload : `agent-browser/prompts-backup/sub-linkedin-drafter-create-2026-05-19T1635Z.json`
- Registry : `agent-browser/sub-agents-registry.json` (3 entrées totales)
- Output : `social-drafts.md` (section LINKEDIN-AUTO append-only)
- Log : `data/sub-agents/sub-linkedin-drafter.jsonl`
- Concept : `memory-agent/concepts/sub-agents-active.md` (3 actifs)
