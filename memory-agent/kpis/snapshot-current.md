# KPIs Snapshot Current — 2026-06-14T11:43Z (post run-555 Strategic-63 PAUSE-AND-WAIT HONORED J+0)

> **Compressed run-505** : critic-71 #3 ★ honored J+0 = 297L >58K tokens → core KPI table <100L (gain ~70% tokens wake-baseline read). Archive complète : `kpis/history/snapshot-pre-505.md`. Hygiène memory-agent.

## Core KPIs (live + lifetime counters)

| Metric | Value | Δ vs J-1 | Last change | Notes |
|---|---|---|---|---|
| `visits_total` | 443 | +4 vs run-541 | 06-14T08:38Z HeadlessChrome bot (run-554 rejection) | Plate humain ; last humain candidate 06-12T14:32Z ChatGPT-Paris #7 ; sub-threshold #8 06-13T02:16Z direct fast-path + #9 06-13T06:10Z Apple PR scan_url + #10 06-13T16:08Z GitHub-referrer ; HeadlessChrome 08:38Z rejeté méthodologie critic-79 #1 |
| `verdict_displayed_events_lifetime` | 11 events / 9 distinct ip_hash | UNCHANGED depuis #8 | 06-13T02:16Z direct encadrement-paris fast-path sev=bad ip_hash=3569448148 | T+~29h27 gap NEW verdict_displayed |
| `humans_engaged_lifetime` | 6-10 raw / 5-7 conf-adj | UNCHANGED (rollback #11) | 06-13T16:08:05Z CANDIDATE #10 GitHub-referrer silent T+~15h35 | candidate #10 ≤30% conf maintenu ; #11 INVALIDÉ critic-79 #1 ★★★ rollback (UA `Applebot/0.1` confirmé visits.jsonl, classification empirique invalide) |
| `email_submitted_lifetime` | 0 N=6 humains | UNCHANGED | n/a | Capture funnel MORT empirique 8+j ; T+~67h post-ship `1f0f669` |
| `subscribers_real_lifetime` | 1 (sogibim) | UNCHANGED | 2026-06-04 sogibim PENDING confirm | T+~11j20h DMARC unfixed silent |
| `subscribers_by_intent` | `{'unset':1}` | unset plate | n/a | Bottleneck UI : intent_signal câblé 2/184 pages (critic-69 #1) |
| `shares_total` | 1 (WhatsApp 0.3%) | UNCHANGED 25j+ | 2026-05-15 | share-card 0 click 7 wakes |
| `signup_confirm_sent_real` | 1 | UNCHANGED | 2026-06-04 sogibim | Anti-vanity dénominateur post run-451 |
| `humans_via_seo_cluster_93_post_audit52` | 0/3 | UNCHANGED | n/a | Deadline 2026-06-11T22Z T+~14h MISS ≥85% confirmé |
| `home_preset_click_consumed_lifetime` | 1 | +1 (run-494) | 06-09T08:46Z Linux X11 ~50% conf | 1ʳᵉ utilisation depuis ship 2026-05-31 (T+9j) |
| `seo_city_page_to_verdict_conversions` | 2 raw | UNCHANGED | Montreuil 06-05 + Saint-Denis 06-08 | Pattern N=2 Pilier 2 SEO main canal validation partielle |
| `pages_total` | 233 | UNCHANGED | 2026-06-03 calendrier-DPE Strategic-42 ship | run-429 |
| `moat_substantive` | 8 (-1 vs 9 mémoire) | UNCHANGED 27 audits | 2026-06-09 audit-54 dégradation | cat-3 fragilisé ECLI hallucination |
| `funnel_events_total` | ~129 | n/a | dernière event 06-09T20:56:49Z Googlebot | Lifetime ; post-purge run-421 |

## Compteurs discipline (Builder)

- `strategic_critic_recommendations_followed_cumul = 62/62→63/63 ★ 34ᵉ J+0 STREAK record absolu` (audit-63 substantive 2026-06-14T10:00Z prescription §6 PAUSE-AND-WAIT méta-Q ack window HONORED run-555 J+0 T+~1h43, NO-OP substantive, deadline T+72h Florian-ack 2026-06-16T22Z T+~58h restant)
- `tactical_critic_recommendations_honored_cumul = 86` UNCHANGED (critic-80 ETA ~19:00Z 06-14 cycle 12h post critic-79 07:00Z)
- `meta_q_acks_received_cumul = 0` UNCHANGED (Florian silent T+~12h post-émission inbox HEAD 06-13T23:50Z, fenêtre ouverte T+~58h)
- `meta_q_drafts_emitted_cumul = 1` DORMANT→ÉMIS effective run-549 (1ʳᵉ émission lifetime audit-58 §6 binding effective)
- `wikipedia_fr_drafts_armed_cumul = 2` UNCHANGED (article-1 *Encadrement loyers en France* + article-2 *Loi Climat et résilience* dormant, 3ᵉ draft BAN STRICT cap consommé)
- `florian_briefs_honored_j0_lifetime = 11` UNCHANGED
- `builder_auto_patches_lifetime = 3` UNCHANGED (cap PAR CIBLE 1/sem fenêtre 06-12→06-19 sans cible identifiée)
- DIR7 streak continued (cron externe `0 */2 * * *` baseline 09:43Z → 11:43Z honored)
- WHY_THIS_NOT_THAT ritual continued (SB-3 light continued : run-543 file CRÉÉ pré-commit)

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
| Pull-LLM ChatGPT (Bouygues 06-02 + Paris 06-12 fast-path) | 2 | cadence ~10j |
| SEO city pages Plaine Commune 93 (Montreuil + Saint-Denis) | 2-3 | ~3j |
| FxiOS bailleur-vetting via `mentions-legales.html` | 1 (HUMAN #6) | 06-09 |
| **Total mesuré / jour** | **~0.18 humain/jour** | acquisition trop faible pour mesurer UX |

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

## Méthodologie triple carve-out (c) — critic-76 #1 ★★★ correction

**Bug runs 533+534** : cross-ref `visits.jsonl` tail SEUL ⇒ a manqué humain ChatGPT 14:32Z (path /encadrement-loyer-paris-2026.html fast-path Q1 0ms verdict_displayed sev=bad). visits.jsonl indexe page-hit raw, sans signal qualifying (utm/q1/verdict).

**Méthodologie restaurée** (critic-70 #2 wake-baseline) : grep `funnel-events.jsonl` pour `verdict_displayed.*2026-06-1[23]` fenêtre 24h AVANT évaluation triple carve-out (c) chaque wake. Si NEW `verdict_displayed` non-bot/non-self ⇒ carve-out (c) POSITIVE ⇒ document snapshot + run + audit-61 data point (PAS FYI inbox HEAD si audit-58 §6 actif).

**run-539 application** : NEW verdict 06-13T02:16Z `s-eclp-mqbq58e7-hd165` `/encadrement-loyer-paris-2026.html` utm=direct fast-path loyer=1200/m²=48 sev=bad ip_hash=3569448148 — DETECTED post-run-538. Vetting : deep-link page sans entrée `visits.jsonl`. Conf-adj ≤30% (UA inconnu). Candidate #8 sub-threshold ⇒ documente snapshot, PAS FYI inbox HEAD (audit-58 §6).

**run-541 application** (critic-77 #1 ★★★ honored J+0 T+~43min) : NEW funnel event `scan_url_page_visit` 06-13T06:10:41Z `s-mqbyic72aci99f` ip_hash 253269318. Cross-ref server.log : IP 17.246.23.192 (Apple Inc. 17.0.0.0/8 — typique iCloud Private Relay exit node) + UA `Mac OS X 10_15_7 Safari/17.4` + chargement séquencé `share-card.js → tailwind-runtime.js → main.css → POST funnel` 4s window = vrai browser pas bot. **Silent T+~1h33 post 06:10:41Z** : 0 q1_answered / 0 verdict_displayed / 0 email_submitted. ⇒ **Candidate #9 sub-threshold ≤30 % conf** (silent verdict-follow-up T+1h30+ per critic-77 #1 méthodologie classification). Documente snapshot, PAS FYI inbox HEAD (audit-58 §6 + critic-76 #2 + critic-77 #1 explicit). 1ʳᵉ détection scan_url-direct (entry page = `/scan-url.html` pas city-page) ⇒ source distincte vs candidates #7/#8 fast-path encadrement-paris.

**run-546 application** : NEW funnel event `home_visit` 06-13T16:08:05Z `s-mqcjumff-uwm5m` ip_hash 2601781522 INÉDIT, referrer `https://github.com/Creariax5/bailleurverif` (entrée depuis repo public Creariax5/bailleurverif), UA `Chrome/148 Windows desktop`. **Silent T+~1h35 post 16:08:05Z** : 0 q1_answered / 0 verdict_displayed / 0 scan_url_page_visit / 0 email_submitted (home_visit isolé). ⇒ **Candidate #10 sub-threshold ≤30 % conf** (méthodologie classification critic-77 #1 silent suite). Documente snapshot, PAS FYI inbox HEAD (audit-58 §6 + critic-76 #2 + critic-77 #1 + audit-61 §Bans). 1ʳᵉ détection GitHub-repo-referrer cumul ⇒ source distincte vs candidates #7/#8/#9 (cat-4 GitHub MIT DR ≈90 produit 1ʳᵉ humain mesuré, asymétrie observable canal moat existant). Candidate #9 06:10Z silent T+~11h35 maintenu sub-threshold.

**run-553 ROLLBACK candidate #11 Applebot** (critic-79 #1 ★★★ honored J+0 T+~43min) : run-550 a classifié event 06-13T22:49:13Z `s-mqcy6ehf-fp3ai` ip_hash 2935856004 path `/` referrer direct comme "Safari/17.4 Mac direct humain sub-threshold". **Cross-ref visits.jsonl** révèle UA complet `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15 (Applebot/0.1; +http://www.apple.com/go/applebot)` ⇒ **Applebot crawler** non-humain. Classification empirique sub-threshold INVALIDE (méthodologie critic-77 #1 cross-ref UA tail-suffix oubliée sur préfixe Safari-mimicking). 2ᵉ récidive structurelle après bug Marseille ECLI hallucination (decisions/2026-06-03-marseille-jurisprudence-rollback.md SB-2 DISCIPLINE 12 codifié). Rollback : (a) titre + L9/11 humans 6-10 raw 5-7 conf-adj UNCHANGED depuis #10 16:08Z run-546 + #11 supprimé ; (b) cette section méthodologie. Decision file `decisions/2026-06-14-candidate-11-applebot-rollback.md`. **Pattern enseignement** : UA "Applebot/" / "Googlebot" / "bot" / crawler keywords DOIVENT être grep'd dans UA STRING ENTIÈRE (incluant suffixe parenthèses), pas seulement préfixe.

**Critic-79 #2 ★★ STOP META "Nᵉ countdown METRIC sous nouveau préfixe"** : runs 550-552 ont propagé `wake 1/5 / 2/5 / 3/5` countdown sous préfixe Strategic-62 PAUSE EXTENDED = transposition critic-77 STOP #3 reconduit sous nouvelle dimension non-réductible STOP ciblé. **Codification wake-553 inline** : 0 propagation `wake N/Y` METRIC quel que soit le préfixe (Strategic-X PAUSE wake N/Y / critic-X STOP N/Y / SB-N application N/Y / méthodologie restaurée Nᵉ). Runs 553+ : "PAUSE Strategic-62 en cours" 1L sans N/Y. PAS auto-PATCH discipline-self-binding sans brief Florian/Strategic prescription (cap PAR CIBLE fenêtre 06-12→06-19 respecté).

**Critic-79 #3 ★ Compression countdown `audit-63 ETA T+~Xh`** : runs 553+ substituer 1L "audit-63 trigger dépend Florian-ack OR T+72h silent fallback 06-16T22Z" sans T+~Xh decrementing multi-wake (mirror critic-78 STOP #3 Wikipedia post-deadline transposition).
