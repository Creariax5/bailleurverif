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
- `_index_bail_loyer.jsonl` — persistent dedup index of LEGIARTI IDs
  seen by the weekly run, with `first_seen_run_ts`. Bounded growth.

## Why

The DILA bulk dump is itself public. The non-rejouable moat is the
**timestamped history of ingestion + curation** : commit N at week N
proves we crawled and parsed delta T before anyone else. Combined with
`legal_basis[]` population in `data/interpretation-library-v0/*.json`,
this builds a defensible audit-trail for the legal-grounding layer of
BailleurVérif's recourse templates.

First run : run-266 (2026-05-18, agent autonome).
