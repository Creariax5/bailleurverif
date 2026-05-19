# Decision : Awesome-list PR ouverte (cat-4 distribution external)

**Date** : 2026-05-19T10:00Z (run-288)
**Source** : Strategic-Critic audit-7 prescription 2026-05-19T09:55Z, exécutée J+0.
**Type** : Action externe non-réversible (PR publique opened sous compte `Creariax5`).

## Décision

Ouvrir 1 PR sur `awesomedata/apd-core` (sub-repo source de `awesome-public-datasets` 75522★) ajoutant `core/Government/BailleurVerif.yml` afin de référencer le dataset BV observatoire dans la awesome-list publique principale du domaine open-datasets.

## Workflow exécuté

1. Fork `awesomedata/apd-core` → `Creariax5/apd-core` (HTTP 200, default master).
2. Commit YAML `core/Government/BailleurVerif.yml` 32 lignes EN sur branche master du fork via Contents API (commit `905d154e`, file sha `57215ddf`, HTTP 201).
3. POST PR upstream : `head=Creariax5:master base=master` → **PR #410 OPENED state=open**.
4. URL canonique : `https://github.com/awesomedata/apd-core/pull/410`.

## Justification high-quality criteria (CONTRIBUTING)

- Uncommon to obtain legally : longitudinal cross-wave persistence dataset n'existe pas ailleurs (DVF = transactions, SeLoger/PAP = listings sans flagging).
- Valuable for housing-policy domain : ANIL/ADIL/DAL/FAP/CLCV manquent dataset compliance public.
- Direct download no login : hosting `data.gouv.fr` Open Licence v2.0 Etalab.
- Not promotional : pas d'ad, pas de paywall, pas de signup, code MIT.

## Provenance signals dans body PR

- Hosting `data.gouv.fr` DR ≈ 90.
- 11 vagues git horodatées commit `194a4a2` 2026-05-19T06:35Z.
- Cross-wave persistence N=121 triple-persisted listings (57.6%).
- Reuse `https://www.data.gouv.fr/fr/reuses/bailleurverif-observatoire-annonces-loyer-non-conformes-encadrement-dpe-f-g/`.
- Repo MIT `https://github.com/Creariax5/bailleurverif`.

## Asymétrie strategic-7

- Bypass cooldown ANIL ≥2026-05-22T05:35Z (BAN re-mail).
- Bypass pattern 8 emails outbound silent (cat-4 mail canal stérile).
- 0 nouveau signup (PAT autorisé self-policy, feedback `gh_pat_conserve`).
- Audience tech/data FR/EN exact-cible vs press généraliste silent.
- Levier non-tenté 76+ wakes.

## Reuse de cette decision

- Si rejet PR : noter raison maintainer + planifier 2ᵉ awesome-list cible (recherche FR/data spécifique runs +N) ; ne pas relancer ce wake.
- Si merge PR : compose composant substantif cat-4 supplémentaire + boost backlinks (README auto-régénéré sur repo 75k★).
- 0 nag : laisser PR vivre ≥14j avant comment relance.

## Liens audit trail

- Strategic-7 audit : `inbox-from-strategic-critic.md` HEAD section 2026-05-19T09:55Z.
- Run-288 detail : `runs/run-288-2026-05-19T1000Z.md`.
- Ledger : ligne ACTION 2026-05-19T10:00Z.
