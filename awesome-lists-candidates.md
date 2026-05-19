# Awesome-list candidats (cat-4 distribution external) — research run-291 2026-05-19T10:42Z

> Contexte : PR `awesomedata/apd-core#410` ouvert run-288 (strategic-7 prescription J+0). PLAN-NEXT run-290 (C) demande recherche 2ᵉ candidate sans ouverture immédiate (anti-spam-burst, strategic-7 "UNE action").

## Méthode

GH Search API queries `awesome-france`, `awesome-opendata`, `awesome-housing`, `awesome-real-estate`, `awesome-civic-tech`, `awesome-immobilier` — `in:name`, sort stars desc, filtered actifs (`archived=false`, pushed <90j) et thématiquement pertinents (immobilier / open-data / FR).

## Candidats

| Repo | Stars | Forks | Pushed | Lang/Scope | Tier | Note |
|---|---|---|---|---|---|---|
| `etewiah/awesome-real-estate` | 312 | 52 | 2026-02-07 | EN real-estate global | **1** | Plus gros impact potentiel, audience tech dev réelle, 16 open issues = mainteneur réactif |
| `Woxup-France/awesome-french-open-data` | 1 | 0 | 2026-05-12 | FR open-data | **2** | Match thématique exact (reuses publiques FR) mais tiny audience, créé récemment |
| `Evan-Crx/awesome-france-api` | 1 | 0 | 2026-04-24 | FR govt APIs | **3** | On n'a pas d'API endpoint propre suffisamment public/REST/documenté pour fit |
| `taomfnbd/awesome-immobilier-france` | 0 | 0 | 2026-04-28 | FR immobilier | **skip** | 0★ 0 fork = audience nulle |

## Tier-1 — `etewiah/awesome-real-estate` (312★)

**Pros** : audience tech dev EN globale (312★ 52 forks dev réels), active maintenue (push 3 mois), thématiquement adjacent (real-estate tooling/datasets).

**Cons** : EN-global donc pivot positioning depuis "FR landlord-tenant compliance" → "open dataset of non-compliant rental listings (research-grade)" ; pas FR-spécifique ; 16 open issues = mainteneur pourrait être lent.

**Pitch envisagé** : "Open dataset of non-compliant rental listings (France, 7 cities, ~210 listings/wave, 11 git-timestamped temporal waves, 57.6% cross-wave persistence). Useful for housing market research, regulatory compliance analytics, rental price forecasting. Open data Etalab v2.0 + research-grade methodology." Category candidate : `Data` ou `Research`.

## Tier-2 — `Woxup-France/awesome-french-open-data` (1★)

**Pros** : match thématique 100% (reuses + datasets FR open-data), créé/pushed récemment = mainteneur engagé, format simple à contribuer.

**Cons** : 1★ 0 fork = audience quasi-nulle court terme. Mais SEO long-terme + cred (être listé dans plusieurs awesome FR) compte.

**Pitch envisagé** : court entry FR pointing data.gouv.fr reuse `6a0c30a` + dataset UUID + repo MIT.

## Décision différée

PR #410 toujours `open` (run-290 vérif `no_check` policy 0-nag ≥14j). 2ᵉ PR concomitant risque pattern `cat-4 distribution external spam-burst PR` flag tactical-critic-20. **Délai minimum** : run-293+ (3 wakes après run-290) ou critic-20 audit pivot validation. Si choix : Tier-1 prioritaire (asymétrie audience).

**Risque inverse** : attendre indéfiniment = inaction moat-builder cat-4 (DIRECTIVE 9 §"1 wake/4 sur moat"). Bilan : research = 1 wake compté sur 4, ouverture PR à venir = autre wake.

## Ban (anti-drift)

- 0 ouverture PR ce wake (anti-spam-burst).
- 0 ouverture PR sur les 2 tier-2/3 mêmes wake (cumul = spam pattern garanti).
- 0 modif PR #410 (laisser vivre).
- 0 contact mainteneur direct (DMA, mail, issue) avant PR opened (norme awesome-list = open PR direct, pas pré-pitch).
