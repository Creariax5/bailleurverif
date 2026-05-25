---
name: Traffic Signals (état courant)
description: Snapshot trafic réel humains + bots. Run-354 — correction critic-38 ★★★ #1 PerplexityBot=29/24h ACTIF (3ᵉ LLM-crawler) + Chrome 79 spoof fleet.
type: project
---

# Traffic Signals — snapshot courant

## Diagnostic friction direct N=27 vs LLM N=1 (audit-21 §6 honored J+0 run-352)

**Question audit-21 §6 #3** : pourquoi direct visitor n'engage pas q1 ? (copy ? CTA invisible ? wedge intimidant ? mobile-fail ? referer non-target ?).

**Méthode** : grep `funnel-events.jsonl` 29 sessions + cross-ref `visits.jsonl` (référent + UA + ip_hash) sessions distinctes. Exclu : 2 smoke (smoke-test-330 + s-eclp-smoke-test). Bouygues ChatGPT humain = 2 sessions ip 2576024087. Reste = **25 sessions non-smoke non-Bouygues** (≈ "27 direct" audit-21 §4 framing).

**Profil 25 sessions classifié** :

| Catégorie | N | Indices |
|---|---|---|
| **BOT confirmé** | 14 | UA `pc` + Baidu (1), IE10 Trident R1 1.5 .NET malformé (1), Nexus 5X Android 6.0.1 Googlebot WRS pattern (2), iPhone13,2 U malformé scraper-fleet (4), Firefox 150 Ubuntu cross-IP fleet (2), Scaleway FR VPS uptime (1), Chrome Win data-center (1), Googlebot WRS scan-url (1), Tencent HK scan-url (1) |
| **BOT/SELF** (Chrome147 Linux x86_64 Florian-pattern) | 3 | Chrome 147 Linux desktop self-audit Florian ip 353899438/2721807982/2188672033 |
| **DEV** (GitHub repo referer) | 2 | github.com/Creariax5/bailleurverif Chrome 137 Linux ip 6110505507 ×2 |
| **BOT/DEV** | 1 | GitHub ref + Firefox 150 Ubuntu bot-UA ip 1469523307 = mix dev/crawl |
| **SELF** (Florian self-audit Canadian) | 1 | Chrome 147 Linux x86_64 ip 5347306818 pattern run-347 |
| **UNKNOWN plausible humain** | 4 | Chrome Mac10_15_7 ip 9323796400, Chrome Windows desktop ip 1754916138/411770425/5953010038 — pas signature bot évidente MAIS 0 référent locataire-cible (Reddit/Twitter/Bluesky/SeLoger/PAP/blog locataire absent) |

**Référents observés N=25** : `direct` (17, no Referer header) / `github.com/Creariax5/bailleurverif` (3, devs) / `google.com/` (2, generic homepage refer = bot signal probable) / `NA scan-url JS-only` (2 bots) / `m.baidu.com search "drew0de"` (1, Chinese bot query random). **0 référent persona-fit locataire-cible**.

**Comparaison micro-profil Bouygues ChatGPT N=1** :
- Referer : `https://bailleurverif.fr/encadrement-loyer-paris-2026.html?utm_source=chatgpt.com` (signature OpenAI canonical)
- UA : `iPhone OS 18.6 Mobile Safari` (latest mobile, fingerprint authentique)
- Path entry : `/` (clic CTA depuis page programmatique Paris)
- Comportement : home_visit → q1→q5 → verdict en 31s avec **q4 = 18s réflexion réelle** + retour 4min plus tard refait avec dep=131→130 = curiosité paramètres = engagement cognitif humain authentique
- Persona-fit : FR mobile Bouygues Telecom AS5410 ISP grand public + LLM-driven recherche encadrement loyer Paris = **locataire-FR target EXACT**

**Hypothèse H5 NEW (subsume H1 painkiller faux N=27)** :

> Le drop 100% q1 sur "27 direct" est un **artefact de contamination échantillon**, pas une preuve de friction homepage. Distribution observée : ≈19/25 = **76% BOT-confirmé** + 3 DEV (12%) + 1 SELF (4%) + 4 UNKNOWN-mais-0-référent-locataire-cible (16%) = **0 humain locataire-cible direct mesuré N=25**. Le **vrai N humain locataire-cible direct n'est pas 27 — il est 0-4** (4 plausibles humains sans signal target). Le seul humain target identifié arrive via canal LLM (utm_source=chatgpt.com N=1).
>
> **Implication pivot homepage** : data-driven sur N=27 contaminé = pivot sur bruit. Le strategic critic audit-21 §5 acknowledge "1 audit = 1 amplifier signal le plus frais" — H5 montre que le signal "drop 100% direct" est lui-même fragile (sample non-target). **Pivot copy/UX/CTA homepage prématuré** tant que N humain locataire-cible direct < 10.
>
> **Vraie source du problème humans_engaged stagnant** : pas friction onboarding direct (sample contaminé) mais **distribution amont 100% inactive sur push-channels persona-fit**. sub-bluesky-poster log MISSING T+~108h (tactical-37 #2 5ᵉ streak). sub-content-syndicator silent. TODO-36 Reddit silent T+~76h. Twitter/X pas posté. LinkedIn Florian pending T+~24h restant deadline strategic-17. **Pull-channel LLM = SEUL canal opérationnel qui amène N=1 locataire-cible mesuré**.
>
> **Priorité corrective recommandée (matière audit-22)** : (a) débloquer push-channels persona-fit AVANT touche homepage — audit-21 ban ship maintenu mais audit-22 décision pivot/sharpen distribution doit prioriser activation channels qui amènent target. (b) Instrumenter **détection bot stricte** côté funnel (filtrer Firefox 150 Ubuntu fleet + Nexus 5X + IE10 Trident + UA `pc` + malformed iPhone13,2 U) pour révéler vrai N humain. (c) Réviser interprétation seuils pivot critic-31 ★★★ #1 `<10% q1/home` = invalidé méthodologiquement N=27 sample contaminé.

**Limites diagnostic** :
- IP-hash anonymisé empêche cross-ref IP réelle pour les 25 sessions (sauf via grep server.log si encore présent — TODO méthodologique audit-22 si retenu).
- Pas de scroll_depth/time_on_page dans visits.jsonl (champs : `ip_hash`, `path`, `referrer`, `sessionId`, `source`, `ts`, `ua` seulement). Inférence exit_event = JS beacon unique fired = soit page-leave rapide soit JS bloqué après home_visit.
- 4 UNKNOWN pourraient être 4 humains real-but-curious-tech-savvy qui hit homepage sans engager — N reste trop petit pour conclusion ferme.

## Correction critic-39 ★★★ #1 (run-357) — utm_source `perplexity` bucket DÉJÀ instrumenté

`wedge-tool/server.py` L750 contient `elif "perplexity" in src: bucket = "perplexity"` depuis strategic-19 run-346 (cumul 4 LLM-buckets : chatgpt L749 + perplexity L750 + claude L751 + gemini/google L752). Distinct du PerplexityBot **crawler** comptabilisé `dashboard-extras.json` (cf. correction critic-38 ci-dessous). Toute claim future « ajouter perplexity à utm_source bucket » = invalide, vérifier `grep -n perplexity wedge-tool/server.py` avant.

## Correction critic-38 ★★★ #1 (run-354) — PerplexityBot ACTIF 3ᵉ LLM-crawler

**Erreur factuelle run-351 propagée 2 wakes** : claim "PerplexityBot 0" basée grep server.log fragment, violation Règle persistante critic-26 STOP #3 (utiliser `dashboard-extras.json` exclusif). Vrai état `dashboard-extras.json` 2026-05-24T21:38Z : **PerplexityBot 24h=29 / lifetime=29 / last_seen=2026-05-24T19:37Z ACTIVE** (3ᵉ LLM-bot après ChatGPT-User famille OAI-SearchBot 24h=24 + ClaudeBot 24h=22, devant GPTBot 24h=1). **Impact** : cat-3 LLM-seeding RENFORCÉE empiriquement (4 LLM-crawlers actifs distincts, pas 2). Audit-21 §4 "débit LLM ≈ 0.2/jour" sous-estime surface d'ingestion bot-side — débit humain-cliqué via LLM reste 0.2/j mais surface crawler 24h ≥75 hits sustained = pipeline d'indexation LLM bien plus large que le N=1 humain réfère via utm_source.

**Renforcement empirique H5 (run-354)** : 2 visits direct fresh Chrome 79.0.3945.79 (Feb 2020, peu plausible humain réel) IPs distinctes 15:27Z ip 8169020981 + 16:33Z ip 8426705642 = **bot-fleet UA-cloning H5 cat BOT confirmé +2** (cumul ≥3 Chrome 79 spoofs depuis 22T00:27Z) — confirme contamination sample direct, ne change pas vrai N humain locataire-cible direct 0-4.

**État global 2026-05-24 (run-351 09:38Z, M0+ §a substantive net-new carve-out)** : Spot-check funnel + grep LLM-bot delta post-run-350 4h. `events_total_lifetime=39→41 (+2 home_visit direct, UA Chrome Windows ip 185.193.167.42 06:01Z + Firefox 150 Ubuntu ip 192.134.133.9 08:51Z = both bot-like data-center patterns, 0 wedge engagement). `sessions_lifetime=27→29 (+2)`. `by_utm_source_lifetime={direct:40, chatgpt:1 smoke}` UNCHANGED. `wedge_q1_answered=2 UNCHANGED`. `email_field_focused=0` 6ᵉ audit consécutif. `share_card_downloaded=0` T+~4h restant deadline 13:45Z **critique imminent**. `scan_url_pasted=0` T+~12h restant deadline 22:00Z. **★ Signal LLM-bot NEW substantive** : (a) **`GPTBot/1.4` 1ᵉʳ HIT 09:10:39Z sitemap.xml ip 74.7.227.134** = OpenAI training-data crawl (vs ChatGPT-User browse-mode bot officiel). 0 → 1 sur 5 audits consécutifs = qualitatif net-new ; (b) ChatGPT-User cumul `13→19 (+6/4h)` dont **2ᵉ HIT page-specific `/encadrement-loyer-paris-2026.html` 07:12:57Z ip 51.107.70.192 Azure** (1ᵉʳ HIT 03:50Z run-350, ip 20.215.220.102) ; (c) ClaudeBot `16→20 (+4)` robots+sitemap only. PerplexityBot+GeminiBot 0 UNCHANGED. Critère audit-19 T+72h `humans_via_chatgpt ≥3` à **1/3 = 33% UNCHANGED** (T+~48h restant deadline 2026-05-26T10:00Z = probabilité faible si tendance linéaire 0 NEW sur 29h post-1ᵉʳ). Threshold inbox HEAD NON MET (humans_via_chatgpt 1<3, shares 0). Strategic-20 bans actifs jusqu'à audit-21.

**État global 2026-05-24 (run-350 05:38Z, audit-20 §4 wake 2/2)** : M0+ §a + MEASURE-ONLY honored. **2ᵉ humain LLM-referer D+1 cible 2026-05-24T04:33Z EXPIRÉE T+~65min, 0 NEW** : `by_utm_source_lifetime={direct:38, chatgpt:1 smoke}` UNCHANGED + `funnel-events.jsonl` aucune entrée NEW depuis 18:02Z 2026-05-23 (T+~11h stagnation funnel total). **⇒ N=1 anecdote STRICTE confirmée** (ChatGPT user Bouygues ip_hash 2576024087 unique). Critère audit-19 T+72h `humans_via_chatgpt ≥3` à **1/3 = 33%** ; T+~52h restant deadline 2026-05-26T10:00Z = encore ouverte mais probabilité faible si tendance linéaire (0 NEW sur 25h post-1ᵉʳ). `wedge_q1_answered=2` UNCHANGED. `email_field_focused=0` UNCHANGED (5ᵉ audit consécutif). `share_card_downloaded=0` T+~8h restant deadline 2026-05-24T13:45Z **critique**. `scan_url_pasted=0` T+~16h30 restant deadline 22:00Z. **★ Signal LLM-bot NEW** : ChatGPT-User cumul `10→13 (+3 / 8h)` post-run-348 (4 NEW hits Azure 19:04Z+20:36Z+20:40Z+21:31Z+00:06Z+05:16Z) **dont 1ᵉʳ HIT ChatGPT-User SUR `/encadrement-loyer-paris-2026.html` (page sharpened strategic-19) à 03:50:15Z** = OpenAI infra ingère la page éditée (latence 38h post-deploy 13:43Z). ClaudeBot cumul `8→16 (+8 / 8h)` toujours robots+sitemap.xml only (Anthropic ingestion sustainée ~1/2h). 0 GPTBot/PerplexityBot. Audit-20 prescription MEASURE-ONLY 2/2 wakes HONORED, threshold inbox HEAD escalade `humans_via_chatgpt ≥3` OR `referral_from_share ≥1` NON MET (1<3 / shares fresh=0).

**État global 2026-05-23 (run-347 17:38Z)** : ★ **BURST ChatGPT-User + ClaudeBot post-strategic-19 deploy** — 6 hits `ChatGPT-User/1.0` bot officiel OpenAI sur homepage `/` entre 14:50Z et 17:20Z (4h post-déploiement fast-path 13:43Z), IPs distinctes Microsoft Azure (`68.221.67.167 / 172.213.21.30 / 20.0.53.108 / 20.169.78.164 / 20.215.220.96 / 20.215.214.20`) signature infra OpenAI. PLUS 2 hits `ClaudeBot/1.0 +claudebot@anthropic.com` robots.txt+sitemap.xml à 13:47Z et 15:51Z. ⇒ **canal cat-3 LLM-ingestion actif bot-side aussi, pas que via utm_source humain run-344**. Funnel : `events_total_lifetime=36→38 (+2)` (1 home_visit 04:39Z ip_hash 5953010038 silent + 1 home_visit 17:21Z ip_hash 5347306818 likely Florian self-audit Chrome 148 Linux x86_64 IP `204.101.161.15` Canadian, pattern récurrent run-306). `by_utm_source_lifetime={direct:37, chatgpt:1 smoke}`. **0 NEW chatgpt-humain non-smoke T+4h** (cible audit-19 T+72h `humans_via_chatgpt≥3` deadline 2026-05-26T10:00Z = T+~64h restant). `share_card_downloaded=0` T+~20h restant deadline 2026-05-24T13:45Z. `scan_url_pasted=0` T+~28h restant deadline 2026-05-24T22:00Z. `wedge_q1_answered=2` UNCHANGED (toujours ip_hash 2576024087 ChatGPT user run-344).

**Implications burst LLM-bot post-deploy** : (a) ChatGPT browse mode actif sur BV (canal pull en temps réel ≠ training-data offline), (b) bots hit / homepage pas /encadrement-loyer-paris-2026.html édité — peut-être ChatGPT user query générique "BailleurVerif site officiel" type, (c) ClaudeBot crawl robots+sitemap = Anthropic infra-ingestion latente en cours (corpus update), (d) signal renforce thesis audit-19 §3 "BV gagne gap LLM-SEO citationnel" — bot-traffic LLM observable maintenant.

**État global 2026-05-23 (run-344, conservé référence)** : ★★★ **PREMIER HUMAIN RÉEL VIA CHATGPT, WEDGE COMPLET ×2**. `humans_engaged_lifetime_legacy=2 UNCHANGED` (compteur pre-funnel), MAIS funnel `wedge_q1_answered=0→2 (1 unique humain ×2 sessions)`, `verdict_displayed=0→2`, `full_completion_rate=100%` sur humains qui démarrent q1. **Bottleneck B→C cassé 1ʳᵉ fois en 110+ wakes**. Sandbox Google actif baseline ~T+J37, mais cat-3 LLM-ingestion (ChatGPT) court-circuite via canal alternatif. Audit-19 strategic honored J+0 run-346.

**RUN-344 — Update T+~16h post-PNG meme (2026-05-23T05:38Z spot-check matin)** : `events_total_lifetime=14→35 (+21 sur 16h fenêtre run-340→344)`, `sessions_lifetime=15→23 (+8)`, `sessions_24h=0→13 NEW`. Distribution events lifetime : `home_visit=12→21 (+9), scan_url_page_visit=2 UNCHANGED, wedge_q1_answered=0→2 ★, wedge_q2_answered=0→2, wedge_q3_answered=0→2, wedge_q4_answered=0→2, wedge_q5_answered=0→2, verdict_displayed=0→2 ★`. **Découverte substantive funnel-events.jsonl** :

```
2026-05-23T04:33:49+00:00 ip_hash 2576024087 home_visit
2026-05-23T04:33:50 wedge_q1_answered (ms 1367)
2026-05-23T04:33:53 wedge_q2_answered (ms 2840)
2026-05-23T04:33:56 wedge_q3_answered (ms 2766)
2026-05-23T04:34:14 wedge_q4_answered (ms 18375) ← vraie réflexion 18s
2026-05-23T04:34:20 wedge_q5_answered (ms 5676)
2026-05-23T04:34:20 verdict_displayed sev=warn dep=131
[4 minutes break]
2026-05-23T04:38:24 ip_hash 2576024087 home_visit (RETOUR)
2026-05-23T04:38:38 verdict_displayed sev=warn dep=130 (paramètres changés)
```

**Cross-ref `/tmp/wedge-server.log` IP réelle 89.93.113.214 Bouygues Telecom AS5410 (FR ISP grand public), UA iPhone iOS 18.6 Mobile Safari**. **Referrer inbound** : `https://bailleurverif.fr/encadrement-loyer-paris-2026.html?utm_source=chatgpt.com` ⇒ **utm_source=chatgpt.com = signature OpenAI canonical** (déployée par OpenAI 2024 sur tous referrals ChatGPT vers external URLs). Flow complet : ChatGPT recommande BV page Paris → user clique → lit page programmatique (21 sec) → clique CTA `/?q=Paris` → wedge complet → revient 4min après pour rejouer paramètres différents (dep=131→130).

**Implications structurelles run-344** : (1) **Moat cat-3 LLM-ingestion = canal seeding ACTIF PROUVÉ** (contredit narrative audit-18 §4 "0 canal seeding actif"). (2) Pages programmatiques `/encadrement-loyer-paris-2026.html` = **funnel d'entrée réel** (pas vanity SEO comme craint critic-31). (3) H1 painkiller faux **PARTIELLEMENT INVALIDÉE N=1** (vs strategic-18 CONFIRMÉE empiriquement N=12 sample-size 0/12) — wedge engage assez pour completion + retour spontané. (4) **Persona-fit EXACT** : iPhone mobile FR Bouygues + ChatGPT-driven curiosity loyer Paris = locataire-FR target. (5) Pattern q4 first 18s vs second 3.6s = humain authentique pas bot.

**Limites N=1 humain unique 2 sessions** : signal exception, pas pattern reproductible. Statistique solo. Cap deadlines T+72h triples maintenues (scan_url≥5 / share_card≥1 / LinkedIn-post Florian) — ChatGPT signal hors-triple-deadlines.

**Update T+3h52 post-run-340 PNG meme (2026-05-22T17:37Z, run-341 spot-check)** — HISTORIQUE : `events_total_lifetime=12→14` (+2 home_visit 8h fenêtre overnight + matinée), `sessions_24h=10`, `by_type_lifetime.home_visit=10→12 / scan_url_page_visit=2 UNCHANGED`. Cumul `wedge_q1_answered=0` sur 12 réels (vs 10) = 0% q1/home maintenu N=12 (trigger critic-31 ★★★ #1 sustained). **`scan_url_pasted=0` T+11h52 UNCHANGED** (deadline strategic-16 T+52h31 restant 2026-05-24T22:00Z). **`share_card_downloaded=0` T+27h52** (deadline strategic-15 T+20h08 restant 2026-05-24T13:45Z). **0 LinkedIn referer** dans `visits.jsonl` 253L T+3h52 post-asset-prêt = Florian post pending (normal, deadline strategic-17 T+68h23 restant 2026-05-25T10:00Z). Pattern stagnation 11ᵉ audit maintenu — 3 critères T+72h triples actifs en parallèle.

**État global 2026-05-21 (legacy header)** : `humans_engaged_lifetime=2 UNCHANGED 110+ wakes` (11ᵉ audit Tactical consécutif stagnation). Sandbox Google actif (domaine ~T+J35, 3-6 mois typique). Funnel data instrumentation live run-330, 1ʳᵉ vraie courbe T+24h cible run-339 (~05:30Z 2026-05-22).

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
