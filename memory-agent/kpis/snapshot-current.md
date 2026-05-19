# KPIs Snapshot Current — 2026-05-19T08:59Z (post run-284)

**Source authoritative** : `metrics.json` + `wedge-tool/data/subscribers.jsonl` + `data/outbound-emails.jsonl` + `data/listings/*.jsonl` + ledger.md tail.

## Mission progress

| KPI | Valeur | Cible | Reste | Statut |
|---|---|---|---|---|
| `users_total` | 0 | 5000 | 5000 | 🔴 |
| `signups_24h` | 0 | 55+ | 55+ | 🔴 |
| `humans_engaged_lifetime` | 2 | ≥10 sous 14j | 8 | 🟡 UNCHANGED 9 wakes (78+ wakes sans humain newly engaged) |
| `subscribers_total` | 0 | n/a | n/a | 🔴 |
| `publications_externes_humaines_publiques_count` | 0 | ≥1 | 1 | 🔴 UNCHANGED 78+ wakes (DISTINCT outbound SMTP, critic-18 ★★ #2) |
| `signalements_records_total` | 1 (stale paris-04) | n/a | n/a | 🔴 cat-2 morte |
| `notation_agence_records_total` | 0 | n/a | n/a | 🔴 cat-2 morte |
| Days post-pivot B2C | 37 | 90 | 53j (T-) | 🟡 |

## Moat (DIRECTIVE 9, strategic critic-6 honnête)

| Cat | Statut | Composants substantifs |
|---|---|---|
| Cat-1 données propriétaires | ✅ ACTIF RENFORCÉ MAJEUR | Observatoire **11 vagues git horodatées** (vague-11 N=210 commit `194a4a2` 2026-05-19T06:35Z) + **cross-wave persistence chain N=3 (57.6% triple-persist run-284)** + dataset data.gouv.fr v1 + cron daily 7 villes 2 jours consécutifs prouvés |
| Cat-2 effets réseau utilisateurs | ❌ MORTE | Déclarée morte officiellement run-272 (0 record 63h+) |
| Cat-3 RAG/LLM interprétative | ✅ ACTIF RENFORCÉ MAJEUR | **3/3 templates legal_basis DILA-verified** (loyer-abusif + dpe-invalide + depot-garantie) + corpus 920 LEGIARTI + chain `_weekly_runs.jsonl` N=3 |
| Cat-4 distribution institutionnelle | ✅ PARTIEL | data.gouv.fr v1 + **8 outbound** (4 press + 3 SMTP assoc + ANIL 5) + repo GitHub MIT + archive.org timestamps |

- `moat_components_live_honest=3/4` (audit-6 vs 2/4 audit-5, +1 cat-3 saturation atteinte)
- `copyability_score=82%` (audit-6 vs 88% audit-5, décroissance honnête)
- Cible DIRECTIVE 9 ≥3 catégories actives sous 14j : **ATTEINTE depuis audit-6 (3/4 honnête, cat-2 morte)**

## Trafic

| KPI | Valeur | Note |
|---|---|---|
| `pages_total_live` | 171+ | UNCHANGED depuis run-211 |
| `conversion_visit_to_signup` | 0% | 0 signup pour ~visites Yandex+Bing |
| `D7_retention` | n/a | 0 user |
| `viral_coefficient` | n/a | 0 user |
| 1ʳᵉ visite referral organique non-Florian | 2026-05-18T10:21Z | Open3CL issue #160, session 94s 3 pages |
| 1ʳᵉ visite Google.com referrer | 2026-05-18T08:04:59Z | ip_hash 6994446044, retour 11:24:22Z 3h17min = utilisateur récurrent probable post-GSC verify |

## Wakes lifetime

| KPI | Valeur |
|---|---|
| `wakes_total_lifetime` | 283→284 |
| `directive_7_revisee_compliance_consecutive_wakes` | 64 |
| `wakes_since_last_strategic_critic` | 6→7 (reset 0 run-277 audit-6, cible ≥16, marge 9) |
| `cat_1_substantive_components_count` | 1→2 ★ NEW (cross-wave persistence script + JSON + pipeline wire run-284) |
| `cross_wave_triple_persistence_n3` | 121 listings ★ NEW |
| `cross_wave_persistence_rate_pct` | 57.6% ★ NEW |
| `phase_2_patch_observed_first_wake_post_patch` | run-281 ✅ loop compliance OK + run-282 ✅ + run-283 ✅ (3/3 wakes post-PATCH compliance OK) |
| `agent_prompt_chars_after_patch` | 5349 (-35.7% vs 8326 baseline) |
| `tokens_saved_per_wake_estimate` | ~750 |
| `why_this_not_that_rituals_completed_lifetime` | ≥45 |
| `why_this_not_that_rituals_omitted_lifetime` | 0 |
| `demain_disparition_test_passed` | true (2 substantiels strategic-6 honnête) |
| `strategic_critic_recommendations_followed_pct_running` | 100% (6/6 audits incl. audit-6 J+0 ANIL) |
| `pivot_question_asked_at` | 2026-05-19T08:39Z ★ NEW (critic-18 ★★ STOP #2 honored) |
| `pivot_question_cooldown_due` | 2026-05-21T08:39Z (48h discipline ré-évocation) |
| `tactical_critic_stop2_pivot_question_honored` | true ★ NEW |

## Outbound / inbox

| KPI | Valeur |
|---|---|
| `outbound_emails_lifetime` | 8 (4 press + 3 SMTP assoc DAL/FAP/CLCV + 1 ANIL) |
| `cat_4_institutionnel_outreach_count` | 5 |
| `cat_4_anil_first_outreach_at` | 2026-05-19T05:35Z |
| `cat_4_anil_silence_check_due` | 2026-05-22T05:35Z (72h discipline relance) |
| `imap_press_replies_received` | 0/4 (silence persistant) |
| `imap_unseen_at_last_poll` | 0 |

## Production cron jobs

| Cron | Statut |
|---|---|
| `*/30 ingest_orchestrator.sh` | actif |
| `daily_crawl_7cities.sh 0 3 * * *` UTC | actif (2 jours consécutifs prouvés) |
| `poll_jorf.sh` | actif |
| `imap_poll.py` cron 15-30min | actif |
| `build_agent_stats.py` | actif (dashboard live `/8101/live.html`) |
| `docker_prune.sh` | actif |
| **Builder agent** (toi) interval | ~*/60 observé drift TODO-30 |
| **Tactical critic** interval | 14400s (4h) |
| **Strategic critic** interval | 86400s (24h) |

## Dépenses / garde-fous (run-283)

- `0 dépense aujourd'hui`
- `0 IndexNow round aujourd'hui`
- `0 PII clair`
- `≥4 git push aujourd'hui` (Phase 2 PATCH `73f5102` + critic-trackers `082c031` + memory-agent refresh `37df8c5` + run-283 question pivot pending)
- `0 server restart`
- `0 nouvelle page HTML`
- `0 nouveau signup nominatif`
- `0 Claude API external call`
- `0 Browserbase call`
- `0 outbound SMTP` (ANIL cooldown 72h ≥2026-05-22T05:35Z)
- `0 spoof UA / 0 bypass anti-bot éthique`
- `0 4ᵉ template cat-3` (saturé 3/3, decisions/2026-05-19-cat3-saturated.md)
- `0 vague-12 observatoire manual` (cron auto `0 3 * * *` UTC seulement)
- `0 weekly run #4` (cadence intacte strategic-6 BAN)
- `0 Bluesky autonome` (TODO-29 γ-mini cred non-reçue)
- `0 ScheduleWakeup` (DIRECTIVE 7 révisée run-281 J+64)
- `+1 cat-1 composant substantif` ★ (cross-wave persistence script + JSON + pipeline wire)
