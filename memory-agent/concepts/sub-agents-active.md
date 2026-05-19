# Sub-agents actifs (état courant)

> Capability shippée par Florian 2026-05-19T11:55Z (champ `model` sur `/api/agents` agents-control, connector test bout-en-bout 12:00Z). Builder Opus seul peut POST/PATCH/DELETE. Naming convention : prefix `sub-`. Max 6 actifs simultanés. Budget €20/mois total.

## Actifs

| Name | Model | ID | Interval | Status | Use-case | Created |
|---|---|---|---|---|---|---|
| `sub-judilibre-enrich` | Haiku 4.5 | `2bbb1dc8-1336-4b64-890b-063c486de4aa` | 1h | enabled (stopped pre-tick) | Enrichit `jurisprudence_refs[]` cat-3 templates (état entrée N=0/0/1 dpe/depot/loyer) | run-297 2026-05-19T12:28Z |

## Garde-fous appliqués

- **Prompt strict** : 10 étapes loop + 7 hard bans (no .env edit, no push, no API agents-control, no spawn, no Claude external, no ScheduleWakeup, no improvise) + exit clauses (saturated_3 / api_fail / drift_avoided / error).
- **Log dédié** : `data/sub-agents/<name>.jsonl` 1 ligne/wake (ts, template, added, total_now, outcome).
- **Backup payload** : `agent-browser/prompts-backup/sub-<name>-create-<ISO>.json` append-only.
- **Registry** : `agent-browser/sub-agents-registry.json` source-of-truth append-only.
- **Auto-rollback** : Builder PATCH `enabled=0` si outcome="error" 2× consécutif.

## Use-cases prescrits Florian (non encore spawnés)

> Spawn UNIQUEMENT après ≥2 cycles `sub-judilibre-enrich` observés OK (discipline incremental).

1. `sub-imap-summarizer` (interval 30 min) — résume IMAP inbound tail.
2. `sub-crawler-postprocess` (interval 3h post-vague) — scoring/dedup nouveaux listings.
3. `sub-linkedin-drafter` (interval 24h) — drafte 3-5 posts LinkedIn.
4. `sub-observatoire-publisher` (interval 12h) — republie HTML observatoire post-crawl.

## Convention update

- Ajout/retrait sous-agent → update ce concept + registry.json + ledger.md.
- Builder vérifie chaque wake : `data/sub-agents/<name>.jsonl` tail 3 lignes pour status courant.
