# Légifrance DILA — cadence ingest hebdo (cat-3 moat)

Public proof of weekly ingestion cadence for the BailleurVérif cat-3 moat
(intelligence interprétative coûteuse, DIRECTIVE 9 §3).

## Source

- DILA Open Data, bulk LEGI archive : <https://echanges.dila.gouv.fr/OPENDATA/LEGI/>
- License : Licence Ouverte Etalab v2.0
- Tooling : `crawler/legifrance_dila_fetch.py` (stdlib only, no OAuth)
- Wrapper : `crawler/legifrance_dila_weekly.sh` (intended cron Sunday 04:17 UTC)

## Files

- `_weekly_runs.jsonl` — one JSON line per weekly run. Each line carries
  `run_ts`, `articles_extracted`, `new_legiarti_ids`, `archive_used`,
  `index_total_after`. The git commit history of this file is the
  crypto-timestamp chain that proves cadence — a concurrent cannot
  retroactively rebuild week N–10 commits.
- `_index_bail_loyer.jsonl` — enriched corpus of LEGIARTI articles
  matching the bail/loyer scope. Each entry carries `id`, `num`,
  `titre_loi`, `texte_num`, `nor`, `date_publi_jorf`, `etat`,
  `date_debut_article`, `date_fin_article`, `verbatim_excerpt` (up to
  2000 chars BLOC_TEXTUEL extracted from DILA bulk archives under
  Licence Ouverte Etalab v2.0), `dila_archive_provenance` (archive name
  + URL + member path + first_seen_run_ts + enriched_run_ts), and
  `legifrance_canonical_url`. Bounded growth, deduplicated by id.

## Scope filter

Strict bail/loyer keyword set applied on titre + contenu (run-267
enrichment pass) :
`loi n° 89-462 | bail d'habitation | résidence principale | encadrement des loyers | loyer de référence | dépôt de garantie | passoire énergétique | performance énergétique | décence | logement décent | location nue | location meublée | préavis du locataire | renouvellement du bail`.

Code général des impôts (CGI) entries that match "résidence principale"
are excluded from the index — tax-context relevance, not bail-core moat.

## Why

The DILA bulk dump is itself public. The non-rejouable moat is the
**timestamped history of ingestion + curation** : commit N at week N
proves we crawled and parsed delta T before anyone else. Combined with
`legal_basis[]` population in `data/interpretation-library-v0/*.json`,
this builds a defensible audit-trail for the legal-grounding layer of
BailleurVérif's recourse templates.

## Run history

- **run-266** (2026-05-18T17:35Z) — bootstrap, 25 LEGIARTI stub entries
  from latest delta (`LEGI_20260517-204556.tar.gz`), single-keyword
  filter (over-broad : matched Code action sociale L314-4 noise).
- **run-267** (2026-05-18T18:45Z) — enrichment pass : strict keyword
  re-scan over 58 DILA deltas (Loi Jeanbrun window Feb-Mar 2026 + April
  + May), verbatim BLOC_TEXTUEL extraction (≤2000c per article), CGI
  tax-context exclusion. 874 articles indexed (vs 25 stubs run-266).
