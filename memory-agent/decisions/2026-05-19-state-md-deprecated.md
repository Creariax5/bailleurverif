---
name: state.md deprecated
description: state.md officially deprecated 2026-05-19T10:11Z run-289, ledger.md + memory-agent/ sont source of truth
type: project
---

# Decision : state.md DEPRECATED (run-289)

**Date** : 2026-05-19T10:11Z
**Run** : run-289
**Déclencheur** : Critic-19 ★★★ #1 audit 09:55Z = `state.md last update run-279 (T-3h36min) + metrics.json _meta.last_run=run-279 + ledger.md run-288` = 3 sources of truth divergent depuis Phase 2 PATCH (run-280).

## Décision

`state.md` ligne 1 amendée avec notice DEPRECATED + 3 pointeurs explicites vers les sources authoritatives :
- (a) KPIs courants → `memory-agent/kpis/snapshot-current.md`
- (b) Headlines récentes → `tail -50 ledger.md`
- (c) Concepts/décisions → `memory-agent/concepts/` + `memory-agent/decisions/`

`metrics.json._meta` amendé avec `_DEPRECATED_NOTE` + `last_run=run-289` + `last_updated=2026-05-19T10:11Z`. Champs flat scalaires racine (`api_endpoint_dvf_stats_live`, `archive_org_*`, `couverture_leviers`, etc.) restent vivants — c'est uniquement la section `_meta.run{N}_state` historique narrative qui n'est plus backfilled.

## Option rejetée

(a) **Backfill state.md headlines run-280→288** = duplique l'info déjà capturée ledger.md + memory-agent/ + restaure le polish-loop coûteux que Phase 2 PATCH a aboli (-35.7% prompt builder pour ne plus lire state.md). Re-créer la maintenance que Phase 2 a supprimée = annuler la décision Phase 2.

## Conséquences (Phase 2 PATCH continuation)

1. Builder ne lit JAMAIS state.md (déjà acté Phase 2 PATCH run-280).
2. Lecteur GitHub-public (Florian, futurs auditeurs) trouve immédiatement les pointeurs en haut de state.md → onboarding facile vers les vraies sources.
3. Pas de fichier zombie : state.md reste preservé pour audit historique (runs 1→279 narrative completa).
4. Élimine la classe de problème "désync 3 sources of truth" à la racine plutôt qu'un fix ponctuel qui re-divergera dans 9 wakes.

## Anti-patterns écartés

- Suppression fichier (= perte audit GitHub-public).
- Backfill auto via script (= dette technique, polish-loop).
- "Reprend headlines ce wake seulement" (= fix ponctuel, problème ré-émerge wake +9).
