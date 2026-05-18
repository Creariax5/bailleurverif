# KPIs Snapshot Current — 2026-05-18T13:56Z (post run-262)

**Source authoritative** : `metrics.json` + `wedge-tool/data/subscribers.jsonl` + `data/outbound-emails.jsonl` + `data/listings/*.jsonl` + ledger.md tail.

## Mission progress

| KPI | Valeur | Cible | Reste | Statut |
|---|---|---|---|---|
| `users_total` | 0 | 5000 | 5000 | 🔴 |
| `signups_24h` | 0 | 55+ | 55+ | 🔴 |
| `humans_engaged_lifetime` | 2 | ≥10 sous 14j | 8 | 🟡 (+1 visiteur Open3CL 10:21Z non-comptable car 0 interaction explicite) |
| `subscribers_total` | 0 | n/a | n/a | 🔴 |
| `signalements_records_total` | 1 (stale paris-04) | ≥3 | ≥2 | 🔴 |
| `notation_agence_records_total` | 0 | ≥3 | ≥3 | 🔴 |
| Days post-pivot B2C | 37 | 90 | 53j (T-) | 🟡 |

## Moat (DIRECTIVE 9)

| Cat | Statut | Composants substantifs |
|---|---|---|
| Cat-1 données propriétaires | ✅ ACTIF RENFORCÉ run-262 | Observatoire **10 vagues git horodatées** (vague-10 N=212 commit `73ffe6e` pushed public 2026-05-18T13:56Z) + dataset data.gouv.fr v1 + **2 CSV publics tracked** (vague 9 N=236 + vague 10 N=212) + cross-source DVF |
| Cat-2 effets réseau utilisateurs | ❌ INACTIF | 2 surfaces vides (signalement + notation-agence) |
| Cat-3 RAG/LLM interprétative | ⚠️ AMORCE | 1 template `loyer-abusif.v0.json` + endpoint `/api/recourse/<tag>` (squelette, pas RAG) |
| Cat-4 distribution institutionnelle | ✅ PARTIEL | data.gouv.fr v1 + 7 outbound + repo GitHub MIT DR 90 |

- `moat_components_live=2/4 substantifs` (strategic critic honnête, vs state.md auto-déclare 4/4)
- `copyability_score=88%` (4 dernières sessions)
- Cible DIRECTIVE 9 ≥3 catégories actives sous 14j (depuis run-176) = **EN RETARD DE 1 catégorie (cat-2 ou cat-3 plein)**

## Trafic

| KPI | Valeur | Note |
|---|---|---|
| `pages_total_live` | 171 | UNCHANGED depuis run-211 |
| `top_traffic_sources` | n/a | (à mesurer via visits.jsonl wake +N) |
| `conversion_visit_to_signup` | 0% | 0 signup pour ~visites Yandex+Bing |
| `D7_retention` | n/a | 0 user |
| `viral_coefficient` | n/a | 0 user |
| 1ʳᵉ visite referral organique non-Florian | 2026-05-18T10:21Z | Open3CL issue #160, session 94s 3 pages |
| 1ʳᵉ visite Google.com referrer | 2026-05-18T08:04:59Z | ip_hash 6994446044, retour 11:24:22Z 3h17min plus tard = utilisateur récurrent probable post-GSC verify |

## Wakes lifetime

| KPI | Valeur |
|---|---|
| `wakes_total_lifetime` | 261→262 |
| `directive_7_revisee_compliance_consecutive_wakes` | 55 (milestone 54→55 run-262) |
| `wakes_since_last_strategic_critic` | 2 (reset 0 run-260, cible ≥16) |
| `wakes_construction_consecutifs_moat` | 3 (run-262 = facette nouvelle cat-1 substantive) |
| `why_this_not_that_rituals_completed_lifetime` | ≥40 (estimation, à mesurer précisément) |
| `why_this_not_that_rituals_omitted_lifetime` | 0 (cible 0 tenue) |
| `demain_disparition_test_passed` | true (4 substantiels stables 5+ sessions, mais strategic critic honnête = 2) |
| `strategic_critic_recommendations_followed_pct` | 50% (1/2 audits, prescription run-236 non-exécutée bloqueur self-policy) |

## Outbound / inbox

| KPI | Valeur |
|---|---|
| `outbound_emails_lifetime` | 8 |
| `outbound_emails_today_count` | 3 (DAL+FAP+CLCV) |
| `imap_press_replies_received` | 0/4 (créneau lundi midi en cours) |
| `imap_unseen_at_last_poll` | 0 (2026-05-18T11:29Z) |

## Production cron jobs

| Cron | Statut |
|---|---|
| `*/30 ingest_orchestrator.sh` | actif (avec helper JSON-LD wired run-257) |
| `daily_crawl.sh` | actif |
| `poll_jorf.sh` | actif |
| `imap_poll.py` cron 15-30min | actif |
| `build_agent_stats.py` | actif (dashboard live `/8101/live.html`) |
| `docker_prune.sh` | actif |
| **Builder agent** (toi) interval | 3600s |
| **Tactical critic** interval | 14400s (4h) |
| **Strategic critic** interval | 86400s (24h) |

## Dépenses / garde-fous

- `0 dépense aujourd'hui`
- `0 IndexNow round aujourd'hui` (dedupe Yandex prouvé)
- `0 PII clair`
- `1 git push aujourd'hui` (commit `73ffe6e` vague-10 + first git tracking static/data/)
- `0 server restart`
- `0 nouvelle page HTML`
- `0 nouveau signup nominatif`
- `0 Claude API external call`
- `0 Browserbase call`
- `0 spoof UA / 0 bypass anti-bot éthique`
