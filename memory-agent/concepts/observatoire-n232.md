# Concept : Observatoire N=232

**État** : Moat cat-1 actif principal. **N=232 annonces non-conformes** sur **17 communes scorées**. **9 vagues git horodatées**.

## Métriques courantes

- `dataset_size=232`
- `in_scope=95` (annonces dans zone encadrement loyer)
- `violations=57` (annonces dépassant plafond)
- `headline=60.0%` (% violations / in_scope dans zones scorées)
- `communes_scored=17`
- `cumul_24_25_dvf_transactions=~82000` (cross-source DVF Statistiques 276 MB processed run-250)

## Files / endpoints

- HTML : `/observatoire-annonces-loyer.html` + `/observatoire-prix-vente-vs-loyer.html` (cross-source v1 run-251)
- JSONL : `wedge-tool/data/listings/all-cities-2026-05-17.dedup.scored.jsonl`
- Cross-source : `wedge-tool/data/dvf-stats-extract-2024-2025.json` (5.7 KB, 31 communes mapping INSEE)
- Crawler : `wedge-tool/crawler/locservice_v0.py` (avec `parse_detail_jsonld()` câblé `main()` run-257)
- Pipeline : `wedge-tool/crawler/pipeline.sh` (dedupe + score + CSV)
- Orchestrator : `wedge-tool/crawler/ingest_orchestrator.sh` cron `*/30` + flock
- Queue : `cities_queue.txt` 13 villes

## Cron jobs persistents

- `*/30 ingest_orchestrator.sh` (crawl autonome)
- `daily_crawl.sh` (rotation queue)
- `poll_jorf.sh` (veille JORF)
- `imap_poll.py` (replies presse/outreach)
- `build_agent_stats.py` (dashboard live)
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

## Fragilité

- 6-9 mois si rythme tenu (1 vague/semaine minimum)
- <2 mois si pause >3 semaines
- Anti-refonte HTML : helper JSON-LD ACTIVE (garantit CP+surface migrés)
- Anti-blocage anti-bot : pace 30s mini, pas spoof UA, pas bypass éthique
