# KPIs Snapshot Current — 2026-06-10T07:42Z (post run-505)

> **Compressed run-505** : critic-71 #3 ★ honored J+0 = 297L >58K tokens → core KPI table <100L (gain ~70% tokens wake-baseline read). Archive complète : `kpis/history/snapshot-pre-505.md`. Hygiène memory-agent.

## Core KPIs (live + lifetime counters)

| Metric | Value | Δ vs J-1 | Last change | Notes |
|---|---|---|---|---|
| `visits_total` | 421 | +0 | 06-10T01:51Z probe Mac/Chrome sub-threshold | Plate 22h consécutives 06-09T20:56Z → 06-10T07:42Z |
| `humans_engaged_lifetime` | 5-6 raw / 4-6 conf-adj | UNCHANGED 53ᵉ wake | 06-09T07:19Z HUMAN #6 FxiOS vetting | Stagnation post HUMAN #6 |
| `email_submitted_lifetime` | 0 N=6 humains | UNCHANGED | n/a | Capture funnel MORT empirique 7+j ; T+~23h post-ship `1f0f669` |
| `verdict_displayed_events_lifetime` | 9 events / 7 distinct ip_hash | UNCHANGED | 06-09T07:19Z FxiOS sev=ok | dont 2 bot/probe |
| `subscribers_real_lifetime` | 1 (sogibim) | UNCHANGED | 2026-06-04 sogibim PENDING confirm | T+~6j23h DMARC unfixed silent |
| `subscribers_by_intent` | `{'unset':1}` | UNCHANGED 41ᵉ plate | n/a | Bottleneck UI : intent_signal câblé 2/184 pages (critic-69 #1) |
| `shares_total` | 1 (WhatsApp 0.3%) | UNCHANGED 25j+ | 2026-05-15 | share-card 0 click 7 wakes |
| `signup_confirm_sent_real` | 1 | UNCHANGED | 2026-06-04 sogibim | Anti-vanity dénominateur post run-451 |
| `humans_via_seo_cluster_93_post_audit52` | 0/3 | UNCHANGED | n/a | Deadline 2026-06-11T22Z T+~14h MISS ≥85% confirmé |
| `home_preset_click_consumed_lifetime` | 1 | +1 (run-494) | 06-09T08:46Z Linux X11 ~50% conf | 1ʳᵉ utilisation depuis ship 2026-05-31 (T+9j) |
| `seo_city_page_to_verdict_conversions` | 2 raw | UNCHANGED | Montreuil 06-05 + Saint-Denis 06-08 | Pattern N=2 Pilier 2 SEO main canal validation partielle |
| `pages_total` | 233 | UNCHANGED | 2026-06-03 calendrier-DPE Strategic-42 ship | run-429 |
| `moat_substantive` | 8 (-1 vs 9 mémoire) | UNCHANGED 27 audits | 2026-06-09 audit-54 dégradation | cat-3 fragilisé ECLI hallucination |
| `funnel_events_total` | ~129 | n/a | dernière event 06-09T20:56:49Z Googlebot | Lifetime ; post-purge run-421 |

## Compteurs discipline (Builder)

- `strategic_critic_recommendations_followed_cumul = 58/58 ★` (audit-61 ETA 06-13T10:00Z arbitrage triple convergence MISS)
- `tactical_critic_recommendations_honored_cumul = 80 → 81 ★` (critic-75 3/3 honored J+0 T+~43min run-529)
- `florian_briefs_honored_j0_lifetime = 11` UNCHANGED
- `builder_auto_patches_lifetime = 3` UNCHANGED (cap PAR CIBLE 1/sem, Builder consommé `decisions/2026-06-05`)
- DIR7 streak continued (cron externe `0 */2 * * *` baseline 05:42Z → 07:42Z honored)
- WHY_THIS_NOT_THAT ritual continued (SB-3 light 6ᵉ application self : run-505 file CRÉÉ pré-commit)

## Sub-agents actifs (6/8 cap, marge 2)

| Sous-agent | Modèle | Interval | Statut |
|---|---|---|---|
| `sub-judilibre-enrich` | Haiku 4.5 | 1h | DISABLED saturated_3 (`decisions/2026-05-19-cat3-jurisprudence-saturated-3-3.md`) |
| `sub-seo-monitor` | Haiku 4.5 | 24h | ACTIF PATCHED v2 run-321 |
| `sub-linkedin-drafter` | Sonnet 4.6 | 24h | ACTIF (drafts queue Florian validate) |
| `sub-observatoire-publisher` | Haiku 4.5 | 7j | ACTIF PATCHED v2 run-325 +HF dataset |
| `sub-bluesky-poster` | Haiku 4.5 | 24h | ACTIF |
| `sub-content-syndicator` | Sonnet 4.6 | 7j | ACTIF (dev.to 0/2 referer T+~22j mort empirique) |

## Sources d'humains validées (32+ derniers jours, N=5-6 cumul)

| Canal | Volume | Cadence empirique |
|---|---|---|
| Pull-LLM ChatGPT (Bouygues 06-02) | 1 | unique |
| SEO city pages Plaine Commune 93 (Montreuil + Saint-Denis) | 2-3 | ~3j |
| FxiOS bailleur-vetting via `mentions-legales.html` | 1 (HUMAN #6) | 06-09 |
| **Total mesuré / jour** | **~0.16 humain/jour** | acquisition trop faible pour mesurer UX |

## Canaux push 0 referer 31j+ MORT structurel

dev.to×2 / awesome-list PRs ×2 (0 merge) / Bluesky / content-syndicator / Telegram bot (E2E pending Florian).

## Critic-71 actions honored J+0 T+~42min (run-505)

- ✅ #1 ★★★ FYI inbox HEAD Florian "Trafic FLAT 22h + sample T+24h=2-3 au lieu ≥30, MISS ≥80% conf, hypothèse acquisition-trafic" (decisions/cross-ref inbox.md HEAD)
- ✅ #2 ★★ Decision file BATCH PURGE ECLI pré-armé `2026-06-10-batch-purge-ecli-template-ready.md` (PAS auto-execute, cap silence holds T-4min)
- ✅ #3 ★ Compression snapshot-current.md 297L → <100L (archive `kpis/history/snapshot-pre-505.md`)
- ✅ STOPs respectés : 0 "critic-72 ETA Xh" / 0 "M0 baseline strict (post-ship surveillance fenêtre N%)" / 0 `why_streak=N→N+1 ★★★` / 0 `pause_measure_cumul=N→N+1` METRIC formel

## Strategic-54 PAUSE-AND-MEASURE statut

- Carve-out (a) BATCH PURGE Florian-ack : silent T+~22h, cap expire 06-10T07:46Z T+4min, default SKIP confirmable wake 09:42Z
- Carve-out (b) NEW signal humain ≥90% conf : 0 NEW depuis 06-09T08:46Z 22h+
- Carve-out (c) critic émis : **critic-71 émis 06-09T19:09Z mtime confirmé 06-10T07:05Z** ⇒ 3/3 actions honored ce wake J+0

## Archive

- Historique complet ante-run-505 : `memory-agent/kpis/history/snapshot-pre-505.md`
- Historique ante-run-306 : `memory-agent/kpis/history/snapshot-pre-306.md`

## Convention update

Wake-baseline lit cette table puis update inline (pas d'append historique). Append `ledger.md` reste source of truth event-log. Si table change > +50L : nouvelle compression + archive `snapshot-pre-NNN.md`.
