# Sub-agents actifs (état courant)

> Capability shippée par Florian 2026-05-19T11:55Z (champ `model` sur `/api/agents` agents-control, connector test bout-en-bout 12:00Z). Builder Opus seul peut POST/PATCH/DELETE. Naming convention : prefix `sub-`. Max 6 actifs simultanés. Budget €20/mois total.

## Actifs

| Name | Model | ID | Interval | Status | Use-case | Created |
|---|---|---|---|---|---|---|
| `sub-judilibre-enrich` | Haiku 4.5 | `2bbb1dc8-1336-4b64-890b-063c486de4aa` | 1h | enabled, cycle 1+2 outcome=ok (dpe 0→3 + depot 0→3, 2/3 saturés). Cycle 3 outcome=api_fail token cache 50min < interval 60min + env vars absents → **fix run-301** auto-load `.env`. Cycle 4 (15:29:38Z) outcome=**drift_avoided** ★ : 60k Judilibre hits mais focalisés baux ruraux/HLM/résiliation pas zone tendue post-ALUR 2014, Haiku a choisi **ne pas dégrader** template loyer-abusif (qualité > quantité). Loyer-abusif reste N=1. Cycle 5 ~16:29Z. | Enrichit `jurisprudence_refs[]` cat-3 templates | run-297 2026-05-19T12:28Z |
| `sub-seo-monitor` | Haiku 4.5 | `d47a1a87-b317-488c-a449-c7326567f341` | 24h | enabled (stopped pre-tick) | Audit SEO/GEO quotidien (PageSpeed Insights + crawler sitemap + LLM-bot diff + diff vs hier), alert inbox HEAD si régression sinon silent | run-299 2026-05-19T13:29Z |

## Garde-fous appliqués

- **Prompt strict** : 10 étapes loop + 7 hard bans (no .env edit, no push, no API agents-control, no spawn, no Claude external, no ScheduleWakeup, no improvise) + exit clauses (saturated_3 / api_fail / drift_avoided / error).
- **Log dédié** : `data/sub-agents/<name>.jsonl` 1 ligne/wake (ts, template, added, total_now, outcome).
- **Backup payload** : `agent-browser/prompts-backup/sub-<name>-create-<ISO>.json` append-only.
- **Registry** : `agent-browser/sub-agents-registry.json` source-of-truth append-only.
- **Auto-rollback** : Builder PATCH `enabled=0` si outcome="error" 2× consécutif.

## Use-cases prescrits Florian (non encore spawnés)

> Brief Florian 2026-05-19T13:30Z autorise spawn `sub-seo-monitor` immédiat (run-299) — override discipline « 1 sous-agent 2-3 cycles » sur cas explicite. Pour les 4 autres en attente, conserver discipline incremental après cycle observé `sub-seo-monitor`.

1. `sub-imap-summarizer` (interval 30 min) — résume IMAP inbound tail.
2. `sub-crawler-postprocess` (interval 3h post-vague) — scoring/dedup nouveaux listings.
3. `sub-linkedin-drafter` (interval 24h) — drafte 3-5 posts LinkedIn.
4. `sub-observatoire-publisher` (interval 12h) — republie HTML observatoire post-crawl.

## Convention update

- Ajout/retrait sous-agent → update ce concept + registry.json + ledger.md.
- Builder vérifie chaque wake : `data/sub-agents/<name>.jsonl` tail 3 lignes pour status courant.
