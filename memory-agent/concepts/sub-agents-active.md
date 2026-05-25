# Sub-agents actifs (état courant)

> Capability shippée par Florian 2026-05-19T11:55Z (champ `model` sur `/api/agents` agents-control, connector test bout-en-bout 12:00Z). Builder Opus seul peut POST/PATCH/DELETE. Naming convention : prefix `sub-`. Max 8 actifs simultanés (cap relevé run-304 brief Florian 16:XXZ). Budget €20/mois total.

## Actifs

| Name | Model | ID | Interval | Status | Use-case | Created |
|---|---|---|---|---|---|---|
| `sub-judilibre-enrich` | Haiku 4.5 | `2bbb1dc8-1336-4b64-890b-063c486de4aa` | 1h | **stopped/enabled=0** auto-disabled cycle 5 saturated_3 (16:29:42Z loyer 1→3 ok, 3/3 templates SATURÉS, exit-clause prompt). Cumul cat-3 `jurisprudence_refs` = **9 ECLI Cass.** (3 dpe + 3 depot + 3 loyer). Total cost lifetime ≈ €0.72 (5 cycles). | Enrichit `jurisprudence_refs[]` cat-3 templates — **MISSION COMPLÈTE run-305** | run-297 2026-05-19T12:28Z |
| `sub-seo-monitor` | Haiku 4.5 | `d47a1a87-b317-488c-a449-c7326567f341` | 24h | **enabled mais LOG MISSING T+~76h post-PATCH-v2 run-341 spot-check** (cycle 1 cible ~2026-05-20T13:29Z = T+52h silent, cycles 2 + 3 cibles 21+22 13:29Z = silent cumul). Pas de patch/respawn autonome (tactical-33 #3 explicit ban). Flag tactical-34 audit ~run-341+. Backup `prompts-backup/sub-seo-monitor-patch-v2-2026-05-20T1031Z.json` hash `81a0184d8f687290`. | Audit SEO/GEO quotidien (PageSpeed Insights + crawler sitemap + **BreadcrumbList JSON-LD audit v2** + LLM-bot diff + diff vs hier), alert inbox HEAD si régression OU breadcrumb missing item sinon silent | run-299 2026-05-19T13:29Z (v2 PATCH run-321) |
| `sub-linkedin-drafter` | Sonnet 4.6 | `d1a89a62-26ab-4223-8f21-0eae41ca7e97` | 24h | enabled — **cycle 4 fired 2026-05-22T14:10Z** (signal=snapshot_kpi `run-340 top10 Paris arr: 1er/5e/6e 100% viol N=45 3vagues 17-19mai`, post_chars=1039, high confidence, 5 hashtags, CTA `loyer-legal-paris.html`). Cycle 1 EARLY 19T16:45Z (judilibre/loyer-abusif) + cycle 2 20T16:34Z (Paris vague-11) + cycle 3 21T10:30Z (cross-wave 121/57.6%) + cycle 4 22T14:10Z (top10 Paris run-340 data, autonomy cascade ★). Florian TODO-32-bis pending. | Drafte 1 post LinkedIn/jour basé sur signaux frais ledger/judilibre/observatoire/snapshot, append `social-drafts.md` section LINKEDIN-AUTO, Florian valide 30s + poste perso 8000 followers | run-304 2026-05-19T16:31Z |
| `sub-observatoire-publisher` | Haiku 4.5 | `576fb185-9c51-4ca9-9453-ac9088a223ac` | 7j (604800s) | enabled (1ʳᵉ tick ~2026-05-27T06:31Z) — **PATCHED v2 run-325 2026-05-20T14:32Z** : prompt 6396→8634 chars (+step 6.5 HF dataset upload, schema log étendu `datagouv_outcome` + `hf_outcome` séparés, fail HF soft jamais bloque data.gouv.fr). Backup `sub-observatoire-publisher-patch-hf-2026-05-20T1432Z.json` hash `6e432483f1eca7f8`. | Republie 1 ressource CSV observatoire/cycle sur dataset data.gouv.fr `6a09ca8088345193c180e0b5` (frequency weekly) **+ HuggingFace dataset secondary** (1er cycle créera dataset HF `<HF_USERNAME>/bailleurverif-observatoire`). Évite warning + maintient signal Google Dataset Search. Exit clause 3 cycles `no_fresh_data` → log `pipeline_dead`. Coût ≈€0.12/mois. | run-317 2026-05-20T06:31Z (v2 run-325) |
| `sub-bluesky-poster` | Haiku 4.5 | `1a6b2a20-fe71-417c-adc7-7a561985366b` | 24h (86400s) | **enabled — ACTIF 1 cycle posted 2026-05-24T14:32:46Z** (correction critic-39 ★★★ #1 run-357 — claims antérieurs « LOG MISSING streak » erronés, `data/sub-agents/sub-bluesky-poster.jsonl` existe 502b 1 ligne `outcome=posted`, post_uri `at://did:plc:kbsz5jfik4z64aha5jtbtlff/app.bsky.feed.post/3mmm6lgqxsw2x`, signal `run-344-1ere-capture-chatgpt-humain-reel`, 1ʳᵉ capture FR Bouygues ChatGPT). Audit Bluesky API public engagement T+36h cible ~2026-05-26T02:32Z. | Poste 1×/jour sur Bluesky (`@BLUESKY_HANDLE`) via AT Protocol (script `bluesky_post_atproto.py` shippé run-274). 280 chars FR + 1 URL canonique bailleurverif.fr + ≤3 hashtags + 0 tagging. Drive trafic fediverse. Exit clause 3 cycles fail → `action_required:builder_review`. Coût ≈€0.60/mois. | run-325 2026-05-20T14:30Z |
| `sub-content-syndicator` | Sonnet 4.6 | `cc0f6fb3-c226-4574-a74c-a35355621c47` | 7j (604800s) | enabled (1ʳᵉ tick ~2026-05-27T14:31Z) | Publie 1 article 800-1500 mots/sem sur dev.to via API (skip Hashnode Pro-only + Medium no-API). Audience devs/tech opendata immo FR. Structure obligatoire : hook + story + stack + code snippet + takeaway + footer github/site/Wikidata. 1ère personne (agent narrateur), pas marketing copy. Tags max 4. Exit clause 2 cycles fail OU 3 skip_no_angle → builder_review. Coût ≈€0.60/mois. | run-325 2026-05-20T14:31Z |

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
