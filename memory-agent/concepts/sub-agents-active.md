# Sub-agents actifs (état courant)

> Capability shippée par Florian 2026-05-19T11:55Z (champ `model` sur `/api/agents` agents-control, connector test bout-en-bout 12:00Z). Builder Opus seul peut POST/PATCH/DELETE. Naming convention : prefix `sub-`. Max 8 actifs simultanés (cap relevé run-304 brief Florian 16:XXZ). Budget €20/mois total.

## Actifs

| Name | Model | ID | Interval | Status | Use-case | Created |
|---|---|---|---|---|---|---|
| `sub-judilibre-enrich` | Haiku 4.5 | `2bbb1dc8-1336-4b64-890b-063c486de4aa` | 1h | **stopped/enabled=0** auto-disabled cycle 5 saturated_3 (16:29:42Z loyer 1→3 ok, 3/3 templates SATURÉS, exit-clause prompt). Cumul cat-3 `jurisprudence_refs` = **9 ECLI Cass.** (3 dpe + 3 depot + 3 loyer). Total cost lifetime ≈ €0.72 (5 cycles). | Enrichit `jurisprudence_refs[]` cat-3 templates — **MISSION COMPLÈTE run-305** | run-297 2026-05-19T12:28Z |
| `sub-seo-monitor` | Haiku 4.5 | `d47a1a87-b317-488c-a449-c7326567f341` | 24h | enabled (1ʳᵉ tick ~2026-05-20T13:29Z) | Audit SEO/GEO quotidien (PageSpeed Insights + crawler sitemap + LLM-bot diff + diff vs hier), alert inbox HEAD si régression sinon silent | run-299 2026-05-19T13:29Z |
| `sub-linkedin-drafter` | Sonnet 4.6 | `d1a89a62-26ab-4223-8f21-0eae41ca7e97` | 24h | enabled — **1ʳᵉ tick EARLY 2026-05-19T16:45Z** (T+14min post-spawn vs T+24h prévu) outcome=ok signal=judilibre_cycle, draft 1184 chars high confidence #Immobilier #EncadrementLoyer + 3 autres, CTA `loyer-abusif.html`. Append `social-drafts.md` LINKEDIN-AUTO 16:45Z. Florian validation pending (TODO-32). | Drafte 1 post LinkedIn/jour basé sur signaux frais ledger/judilibre/observatoire/snapshot, append `social-drafts.md` section LINKEDIN-AUTO, Florian valide 30s + poste perso 8000 followers | run-304 2026-05-19T16:31Z |
| `sub-observatoire-publisher` | Haiku 4.5 | `576fb185-9c51-4ca9-9453-ac9088a223ac` | 7j (604800s) | enabled (1ʳᵉ tick ~2026-05-27T06:31Z) | Republie 1 ressource CSV observatoire/cycle sur dataset data.gouv.fr `6a09ca8088345193c180e0b5` (frequency weekly). Évite warning `quality.update_fulfilled_in_time: False` + maintient signal "actively maintained" Google Dataset Search. Exit clause 3 cycles `no_fresh_data` → log `pipeline_dead`. Coût ≈€0.12/mois. | run-317 2026-05-20T06:31Z |

## Garde-fous appliqués

- **Prompt strict** : 10 étapes loop + 7+ hard bans (no .env edit, no push, no API agents-control, no spawn, no Claude external, no ScheduleWakeup, no improvise) + exit clauses (saturated_3 / api_fail / drift_avoided / error).
- **Log dédié** : `data/sub-agents/<name>.jsonl` 1 ligne/wake (ts, outcome, signal_source, post_chars, confidence, hashtags_count, cta_url).
- **Backup payload** : `agent-browser/prompts-backup/sub-<name>-create-<ISO>.json` append-only.
- **Registry** : `agent-browser/sub-agents-registry.json` source-of-truth append-only.
- **Auto-rollback** : Builder PATCH `enabled=0` si outcome="error" 2× consécutif OU no-op 2× consécutif (cf. brief Florian 16:XXZ §"Garde-fous").

## Use-cases prescrits Florian (encore en attente de spawn)

> Brief Florian 2026-05-19T16:XXZ autorise spawn explicite plus de sous-agents Haiku/Sonnet (cap 8). Discipline anti-bloat : E2E systématique post-spawn (vérifier delta réel, pas heartbeat).

1. `sub-imap-summarizer` (Haiku, interval 6h) — poll IMAP `contact@bailleurverif.fr` + classify spam/legit + summarize → inbox.md `📧` section. Évite à Builder de lire 50 emails/wake.
2. `sub-crawler-postprocess` (Haiku, interval 12h) — nettoie + normalise crawls observatoire annonces, calcule % violations DPE/loyer par ville, écrit `data/observatoire-stats.json` daily.
3. ~~`sub-observatoire-publisher`~~ — **SHIPPED run-317 2026-05-20T06:31Z** (interval 7j, brief Florian 05:40Z).
4. `sub-press-monitor` (Haiku, interval 12h) — Google News + Mention.com-style scrape via search HTML "bailleurverif" OR "encadrement loyer 2026" + flag mentions presse FR dans inbox.md. Détecte trigger pour TODO-23.

## Convention update

- Ajout/retrait sous-agent → update ce concept + registry.json + ledger.md.
- Builder vérifie chaque wake : `data/sub-agents/<name>.jsonl` tail 3 lignes pour status courant.
