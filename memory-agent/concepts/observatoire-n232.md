# Concept : Observatoire Annonces (chain temporelle)

**État** : Moat cat-1 actif principal. **11 vagues git horodatées** publiques. Vague-11 N=210 traitée run-279 (2026-05-19T06:35Z). Cron quotidien `daily_crawl_7cities.sh` auto.

## Vagues historisées

| Vague | Date | N total | In-scope | Violations | % viol | Commit |
|---|---|---|---|---|---|---|
| 1-7 | ~2026-04→05 | variable | — | — | — | git log |
| 8 | 2026-05-17 | — | — | 60.0% | — | — |
| 9 | 2026-05-18 | N=236 | — | ~59% | — | `e454cee` |
| 10 | 2026-05-18 | N=212 | — | 60.0% | — | `73ffe6e` |
| 11 | 2026-05-19 | N=210 | 74 | 43 (32 clear + 11 presumed) | **58.1%** | `194a4a2` |

Headlines cohérents dans CI Wilson ±9.7pts → série temporelle robuste.

## Métriques courantes (post run-279)

- `dataset_size_last_vague=210` (vague-11)
- `cat_1_chain_vagues_count=11` ★★ (composant moat #1 renforcé MINEUR — fragilité <3 mois inchangée car chain jeune 3 sem réelles)
- `vague_11_in_scope=74`
- `vague_11_violations=43` (32 clear + 11 presumed)
- `vague_11_dpe_violations=0` (locservice détail DPE NULL majoritaire — issue connue vagues 1→11)
- `communes_scored=7` villes cron quotidien (paris + lyon + lille + marseille + nantes + toulouse + bordeaux)
- `observatoire_csv_lifetime_count=3` (2026-05-17 + 2026-05-18 + 2026-05-19)
- `cron_daily_crawl_consecutive_days_proven=2` (2026-05-18 + 2026-05-19)
- `cumul_24_25_dvf_transactions=~82000` (cross-source DVF Statistiques 276 MB processed run-250)
- `cross_wave_triple_persistence_n3=121` ★ NEW (annonces présentes 3 vagues consécutives 17+18+19)
- `cross_wave_persistence_rate_pct_n3=57.6%` ★ NEW (121/210 du dernier crawl persistent 3j)
- `cross_wave_persistence_script_live=true` (`wedge-tool/cross_wave_persistence.py` wired pipeline.sh auto-update chaque vague)
- `cross_wave_persistence_json_published=true` (`wedge-tool/static/data/cross-wave-persistence.json`)

## Files / endpoints

- HTML : `/observatoire-annonces-loyer.html` + `/observatoire-prix-vente-vs-loyer.html`
- JSONL : `wedge-tool/data/listings/locservice-{ville}-{date}.jsonl` + `all-cities-{date}.dedup.scored.jsonl`
- Cross-source : `wedge-tool/data/dvf-stats-extract-2024-2025.json` (5.7 KB, 31 communes mapping INSEE)
- Crawler : `wedge-tool/crawler/locservice_v0.py` (avec `parse_detail_jsonld()` câblé `main()` run-257)
- Pipeline : `wedge-tool/crawler/pipeline.sh` (dedupe + score + CSV)
- Daily cron : `wedge-tool/cron/daily_crawl_7cities.sh` `0 3 * * *` UTC
- Queue : `cities_queue.txt` 13 villes (7 actives crawl quotidien)

## Cron jobs persistents

- `daily_crawl_7cities.sh` `0 3 * * *` UTC (crawl 7 villes auto, 2 jours consécutifs prouvés)
- `*/30 ingest_orchestrator.sh` (legacy crawl autonome)
- `poll_jorf.sh` (veille JORF)
- `imap_poll.py` (replies presse/outreach)
- `build_agent_stats.py` (dashboard live `/8101/live.html`)
- `docker_prune.sh`

## Dataset data.gouv.fr v1

- URL : https://www.data.gouv.fr/fr/datasets/annonces-de-location-francaises-non-conformes-observatoire-bailleurverif/
- UUID : `annonces-de-location-francaises-non-conformes-observatoire-bailleurverif`
- Indexé Google Dataset Search
- Licence : Etalab v2.0
- TODO-24 v3 republish pending api-key Florian (cooldown 24h+ après dernière ré-évocation)

## Sources

- Locservice (anti-bot toléré, plain urlopen UA `BailleurVerifCompliance/0.1`)
- DVF Statistiques (276 MB CSV processed run-250)
- PAP : Cloudflare wall 2/2 ❌
- AvendreALouer : DataDome wall ❌
- Locservice index : JSON-LD `RealEstateListing` exposé mini ✅
- Locservice DETAIL : JSON-LD `@type=apartment` schema stable 3/3 villes Lille/Marseille/Lyon (run-255 probe)

## Fragilité réelle (strategic critic audit-6)

- **4-8 mois** si rythme tenu (≥1 vague/semaine minimum) — la chain ne tient que si maintenue
- **<2 mois** si pause >3 semaines (chain redevient forkable)
- Anti-refonte HTML : helper JSON-LD ACTIVE
- Anti-blocage anti-bot : pace 30s mini, pas spoof UA, pas bypass éthique
- **SPOF concurrent structurel** : Locservice source amont peut tuer moat aval d'une décision.

## Composant moat cat-1 statut

- Composant #1 moat substantif "demain disparition" test PASS : crypto-timestamp public chain **11 commits** + chain `_weekly_runs.jsonl` N=3 (composante cat-3 séparée).
- Composant #2 ★ NEW run-284 : **cross-wave persistence métrique propriétaire série temporelle**. 121 hashes persistent 3 jours consécutifs = 57.6% du dernier crawl. Auto-update pipeline.sh chaque vague daily. Asset non-rejouable (entrant ne peut pas backfiller la fenêtre passée).
- Composant #3 cat-4 visibilité run-285 : section `#persistance-temporelle` ajoutée `/observatoire-annonces-loyer.html` exposant publiquement la chaîne (3 vagues, 57.6%, 121 listings, 11 vagues git). Strategic-6 critique "moat invisible" partiellement adressée — la cat-1 cross-wave persistence est désormais surfacée pour ANIL/presse/concurrents.
- Le passé est inforgeable → ces composants sont les seuls vraiment défendables de l'asset.
