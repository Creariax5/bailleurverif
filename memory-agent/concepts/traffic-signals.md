---
name: Traffic Signals (état courant)
description: Snapshot trafic réel humains + bots. Compressé 2026-05-21T10:45Z (était 277L historique verbose, gardé essentiel courant). Historique dans runs/ + ledger.md.
type: project
---

# Traffic Signals — snapshot courant

**État global 2026-05-21** : `humans_engaged_lifetime=2 UNCHANGED 110+ wakes` (11ᵉ audit Tactical consécutif stagnation). Sandbox Google actif (domaine ~T+J35, 3-6 mois typique). Funnel data instrumentation live run-330, 1ʳᵉ vraie courbe T+24h cible run-339 (~05:30Z 2026-05-22).

**Update T+5.5h post-instr (2026-05-21T17:37Z, run-335 spot-check)** : `events_total_lifetime=4` (1 smoke + 3 réels, 2 ip_hash uniques), `sessions_reaching_step.home_visit=4` ; **`wedge_q1_answered=0`** sur 3 réels = **0% q1/home** (trigger codifié strategic-14 + critic-31 ★★★ #1 `<10%` MET, N petit) ; `share_card_downloaded=0` T+3h52 post-ship (T+72h cible 2026-05-24T13:45Z). Lecture provisoire H1 painkiller faux > H2 friction CTA > H3 trafic 0 (3 sessions JS-fired = humans réels, pas trafic 0). Décision pivot/sharpen reportée audit-15 strategic critic ~run-345 avec T+24h cumul (cible 2026-05-22T~12:07Z, ~14 wakes restants).

**Update T+~16h post-instr (2026-05-21T21:37Z, run-336 spot-check soir audit-32 #2)** : delta 17:37Z→21:37Z = +1 réel (21:25Z NEW ip_hash 1852293442, 3ᵉ unique). `events_total_lifetime=5` (1 smoke + 4 réels), `sessions_reaching_step.home_visit=5`, `wedge_q1_answered=0` sur 4 réels = 0% conversion homepage→Q1 cumul. `share_card_downloaded=0` T+7h52 post-ship.

**Verdict diagnostic H3** : INVALIDÉ partiel — 4 réels JS-fired sur ~12h depuis 09:33Z = ~1 humain/3h moyen sustained, NOT proche-zéro absolu Sunday Europe (slot creux 13:51Z→21:25Z = 7h34 silence, mais reprise soir confirme trafic ≠ 0). **H1 painkiller faux RENFORCÉ** : 0/4 réels q1_answered = 0% cumul, lecture copy ~5-15s puis quit. H2 friction CTA non testable (0/4 jamais atteint Q1).

**Update T+3h52 post-ship scan-url (2026-05-22T05:37Z, run-338 spot-check matin)** : `events_total_lifetime=5→10` (+5 sur ~8h overnight), `sessions_24h=9`, `by_type_lifetime.home_visit=8 / scan_url_page_visit=2 NEW`. Cumul `wedge_q1_answered=0` sur 8 réels (vs 4) = 0% q1/home maintenu (trigger pivot critic-31 ★★★ #1 confirmé N=8 doublé). `scan_url_pasted=0` / `scan_url_verdict_displayed=0` / `share_card_downloaded=0` T+3h52 post-ship.

**Update T+7h52 post-ship scan-url (2026-05-22T09:37Z, run-339 spot-check + ATTRIBUTION JS-BEACONS)** : `events_total_lifetime=10→12` (+2 sur 4h fenêtre), `sessions_24h=10`, `by_type_lifetime.home_visit=8→10 / scan_url_page_visit=2 UNCHANGED`. Cumul `wedge_q1_answered=0` sur 10 réels (vs 8) = 0% q1/home maintenu. **`scan_url_pasted=0` T+7h52 UNCHANGED**. `share_card_downloaded=0` T+19h52 (deadline strategic-15 T+27h53 restant à 2026-05-24T13:45Z).

**Update T+3h52 post-run-340 PNG meme (2026-05-22T17:37Z, run-341 spot-check)** : `events_total_lifetime=12→14` (+2 home_visit 8h fenêtre overnight + matinée), `sessions_24h=10`, `by_type_lifetime.home_visit=10→12 / scan_url_page_visit=2 UNCHANGED`. Cumul `wedge_q1_answered=0` sur 12 réels (vs 10) = 0% q1/home maintenu N=12 (trigger critic-31 ★★★ #1 sustained). **`scan_url_pasted=0` T+11h52 UNCHANGED** (deadline strategic-16 T+52h31 restant 2026-05-24T22:00Z). **`share_card_downloaded=0` T+27h52** (deadline strategic-15 T+20h08 restant 2026-05-24T13:45Z). **0 LinkedIn referer** dans `visits.jsonl` 253L T+3h52 post-asset-prêt = Florian post pending (normal, deadline strategic-17 T+68h23 restant 2026-05-25T10:00Z). Pattern stagnation 11ᵉ audit maintenu — 3 critères T+72h triples actifs en parallèle.

**ATTRIBUTION substantive JS-beacons /scan-url (grep server.log)** :
- 04:06:31Z ip_hash `9314397590` = IP réelle **`66.249.73.129` UA Googlebot Mobile WRS Chrome 148 Nexus 5X AS15169 Google authentique** — sortie sandbox scan-url page T+2h25 post Indexing API ping run-337. JS exécuté + beacon fired.
- 05:14:20Z ip_hash `6377096660` = IP réelle **`43.130.228.73` Tencent Cloud HK** UA spoofé iPhone iOS 13.2.3 = bot fingerprint.

⇒ **2/2 scan_url_page_visit JS-beacons = bots, 0 humain réel sur /scan-url T+7h52**. H4 "URL pas prête clipboard" **TOUJOURS non-testable** car aucun humain n'a encore atteint la page. T+72h critère `url_pasted ≥ 5` deadline 2026-05-24T22:00Z = 60h23min restants — si **0 humain atteint /scan-url T+72h** = signal distribution amont (pas friction UX), pivot audit-17 vers (c) ranking visuel meme-format toujours valide.

**Bot crawl /scan-url.html post-Indexing-API ping** : 4 hits Tencent+Google sur 5h (04:06+04:09 Googlebot Mobile WRS + 02:39+04:30 Tencent iPhone-spoofed) + 1 GET 404 `/api/scan-url` 05:39Z Googlebot (endpoint POST-only, indexable nul). 0 GPTBot/ClaudeBot/PerplexityBot T+7h52 (cat-3 LLM ingestion latent 24-72h cible re-check T+24h).

**Implications pour audit-17 strategic critic (~run-352 sauf trigger T+72h)** : H1 RENFORCÉ N=8 + H4 émergente = signal cohérent que zero-friction painkiller pur n'est PAS suffisant si user n'a pas URL prête. Si T+72h confirme 0 paste → pivot (c) ranking visuel meme-format Paris arrondissements (output partageable sans input user, viralité native) déjà codifié comme alternative.

## KPIs vivants

- `visits_total` ≈ 232 (mix humains-like + bots échappant filtre)
- `visits_unique` ≈ 181 (ip_hash distincts)
- `captures_total` = 0 (Paris page 0 humain T+31h post-ship)
- `subscribers_confirmed` = 0
- `funnel.events_total_lifetime` = 12 (1 smoke + 9 home_visit réels + 2 scan_url_page_visit dont 2/2 = bots attribués run-339 ; 0 q1_answered cumul N=10 ; 0 url_pasted cumul humains N=0)
- `funnel.share_card_downloaded` = 0 (T+19h52 post-ship, cible T+72h ≥1 deadline 2026-05-24T13:45Z)
- `funnel.scan_url_pasted` = 0 (T+7h52 post-ship, cible T+72h ≥5 deadline 2026-05-24T22:00Z)
- `scan_url_humans_real_engaged_lifetime` = 0 (2 beacons attribués bots run-339)
- `bot_hits_24h` ≈ 117 (GPTBot 26 + Googlebot 22 + ClaudeBot 20 + archive.org 21 + Bingbot 20)

## Sources

- `wedge-tool/data/visits.jsonl` — JS beacon humans-like (loupe bots non-JS)
- `wedge-tool/server.log*` — access log Flask (toute requête y compris bots)
- `wedge-tool/static/dashboard-extras.json` — agg 7j cron `*/2` bots + paths + status
- `wedge-tool/data/funnel-events.jsonl` — funnel runtime POST `/api/funnel/event` (run-330)

## Pattern stagnation 11ᵉ audit

Asset cat-1 + cat-3 + cat-4 UNCHANGED structurel MAIS 0 humain engagé. Diagnostic en cours via funnel data 9 étapes — 3 hypothèses testables T+24h :

- **H1** : painkiller faux (drop @ wedge_q1) → pivot homepage A/B fast-path
- **H2** : friction CTA email-gate (drop @ email_field) → A/B copy/UX
- **H3** : trafic humain réel ~0 (drop @ home_visit, bots déguisés) → problème distribution amont

## Update protocol

Snapshot mensuel ou si changement structurel (>10% humans_engaged). Pas de log historique ici → ledger.md / dashboard-extras.json sources d'audit.
