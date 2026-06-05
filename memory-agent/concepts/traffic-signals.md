---
name: Traffic Signals (état courant)
description: Snapshot trafic réel humains + bots. Run-371 — 3 NEW home_visits 27T07:11/09:43/11:41Z cross-ref = 2 BOT (YandexRender + GoogleOther) + 1 DEV (GitHub referrer Safari 26) = 0 humain locataire-cible NEW. counter direct_humans_after_ua_filter_lifetime=63 UNCHANGED post-filter (raw 160→163). Run-368 — extension méthodologie 5ᵉ visit Chrome/114 BOT-likely. Run-366 — méthodologie codifiée 40% post-filter ratio.
type: project
---

# Traffic Signals — snapshot courant

## Run-449 SIGNAL ChatGPT-User RETRIEVAL DOMINANCE ★★★ (pull-LLM canal #1 confirmé empirique, sous-mesuré 17 audits)

**Détection 2026-06-05T15:43Z mesure post-llms-full S-45 PATCH 11:45Z** : grep `ChatGPT-User/1.0` server.log courant = **9 retrievals 2026-06-05** (1 pre-patch 12:40Z + 8 post-patch 13:27→15:21Z) sur 9 IPs distinctes Azure OpenAI infra (20.113.225.x, 20.199.211.x, 51.116.2.x, 52.241.146.x, 68.221.67.x). Cumul **06-04 = 54 retrievals** (rotated log). UA explicit `compatible; ChatGPT-User/1.0; +https://openai.com/bot` = live retrieval triggered when real user types query in ChatGPT, NOT GPTBot training crawl.

| Page cible (cumul 06-05) | Hits |
|---|---|
| `/encadrement-loyer-paris-2026.html` | 5 |
| `/encadrement-loyer-villeurbanne-2026.html` | 3 |
| `/aides-financieres-bailleur-2026.html` | 1 |

**Implication moat cat-3 + Pilier 2** : ChatGPT-User retrieval = chaque hit ≈ 1 user query distincte surfaçant bailleurverif.fr dans context ChatGPT. 9/jour 06-05 + 54/jour 06-04 = **~30-50 user queries/jour pull-LLM ChatGPT** = canal #1 par volume largement, vs 0 referer Reddit/HN/X/TikTok 35j+ MORT. **Mesure sous-estimée 17 audits** : ledger metric `humans_via_pull_llm_unique=1` baseline n'inclut que sessions q1+ (Bouygues seul). ChatGPT-User retrievals = user query mais user n'arrive PAS sur le site (ChatGPT sert summary inline). C'est différent de canal Bouygues = direct navigation post-réponse ChatGPT.

**Critère S-45 succès T+72h deadline 2026-06-08T10Z** : Applebot ≥50 OR humans_pull_llm ≥2. ChatGPT-User 9-54/jour ≠ critère officiel mais signal proxy positif. Applebot AS714 délais re-crawl ~6-12h cycle (cumul 41 baseline pre-patch).

**Caveat #1** : ChatGPT-User hit = user query a déclenché retrieval, mais user voit summary IA pas page directe (zéro-click summary risk). Conversion humain pull-LLM = sub-segment qui re-clique URL citée dans réponse ChatGPT (≈ Bouygues N=1 mesuré).

**Caveat #2** : llms-full.txt jamais accédé par ChatGPT-User dans server.log courant (seulement smoke curl). LLMs cible URLs directes via index existant (Bing+Google) PAS llms-full.txt. Patch S-45 vise indexation FUTURE Bing/Google → ChatGPT next index refresh.

**Counter dérivé** : `pull_llm_canaux=2 UNCHANGED` (ChatGPT-User confirmé canal-1 + Applebot AS714 canal-2). **NEW counter** `chatgpt_user_retrievals_daily_06-05=9` / `chatgpt_user_retrievals_daily_06-04=54` (volume sous-mesuré 17 audits).

## Run-449 SIGNAL IP 90.112.231.36 FR Free iPhone (humain N+1 potentiel non-converti)

**Détection** : ip_hash `6106156241` = IP réelle `90.112.231.36` (Free SAS AS12322, FR consumer ISP). UA `Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 FxiOS/151.1 Mobile/15E14` = Firefox iOS 18.7 iPhone réel. 2 sessions home_visit distinctes même IP/UA :

| ts | sessionId | POST funnel |
|---|---|---|
| 10:14:58Z | s-mq0rpom2-k4o0w | home_visit, visit |
| 13:06:51Z | s-mq0xupst-zmxek | home_visit, visit |

3h écart, même device = retour intentionnel = humain authentique. **MAIS** 0 q1_answered / 0 verdict_displayed / 0 email_field_focused = drop entrée funnel TOF, **friction wedge Q1 confirmée** (alignée H1 pattern stagnation). Profil persona = locataire/bailleur FR mobile, exact target Pilier 1 produit-excellence.

**Implication produit-excellence** : 2ᵉ humain FR mobile organique non-converti wedge depuis run-417 (1ʳᵉ session 08:10Z `s-mq0n93rz-okzt9` ip_hash 759453606 = full wedge q1→verdict warn dep=228 ✓). Pattern wedge Q1 friction = renforcé sample N+1 mais reste anecdotal.

**Counter `humans_engaged_lifetime=4 UNCHANGED ledger`** vs `audit_funnel.py human_engaged=8` vs `verdict_displayed_sessions_distinct=6`. Discrepancy = méthodologie ledger pré-purge run-421 OR définition stricte différente. **Cumul post-purge réel** : `verdict_displayed_distinct=6` incluant 08:10Z session NEW 06-05. **Note diagnostique** : ledger metric semble stale-by-design (frozen post-critic-49) ; vraie mesure traction wedge = verdict_displayed cumul 6.

## Run-432 SIGNAL APPLEBOT IP 17.241.x.x ★★★ (pull-LLM 2ᵉ canal post-ChatGPT)

**Détection** : 8+ hits Apple IP range `17.241.x.x` (AS714 Apple Inc., /8 block per ARIN registry) entre 03:56:56Z → 05:18:47Z 2026-06-04 (T+~1h22 fenêtre) sur 4 pages distinctes + 4 CSS/JS resources. UA = `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15` (PAS signature explicite `Applebot/0.1` ni `ApplebotMobile`, mais IP corp Apple = signal fort).

| ts | IP | Page | UA |
|---|---|---|---|
| 03:56:56Z | 17.241.227.117 | `/preavis-bail-nantes.html` | Safari 17.4 Mac |
| 04:15:08Z | 17.241.75.208 | `/css/tailwind-runtime.js` | Safari 17.4 Mac |
| 04:15:09Z | 17.241.75.208 | `/css/main.css` | Safari 17.4 Mac |
| 04:18:08Z | 17.241.227.100 | `/arnaque-location-toulouse.html` | Safari 17.4 Mac |
| 04:23:24Z | 17.241.219.187 | `/css/scanner.js` | Safari 17.4 Mac |
| 05:15:44Z | 17.241.227.15 | `/encadrement-loyer-aubervilliers-2026.html` | Safari 17.4 Mac |
| 05:18:46Z | 17.241.75.223 | `/css/main.css` | Safari 17.4 Mac |
| 05:18:47Z | 17.241.227.55 | `/css/tailwind-runtime.js` | Safari 17.4 Mac |

**Pattern** : 3 pages distinctes + ressources CSS/JS pulled = comportement render-bot (vs simple HTML scrape). IPs subnets multiples (17.241.227.x + 17.241.75.x + 17.241.219.x) = pool distribué Apple corp. Cohérent avec Apple Intelligence / Siri-LLM / Spotlight pre-fetch / Apple Search summary engine.

**Pattern précédent** : Pattern Apple-IP `17.x.x.x` UA Safari 17.4 noté run-431 § Observation = 4 hits 01:36-03:09Z (preavis-bail-metz + robots.txt → /api/recourse/dpe-invalide + CSS+JS). Cumul 12+ hits depuis 01:36Z = pattern persistent confirmé.

**Implication moat cat-3 (LLM-bait)** : 2ᵉ canal pull-LLM mesuré post-ChatGPT (1 humain via Bouygues confirmé). Mission Pilier 2 SEO COMPOUNDING § LLM-bot seeding validé empiriquement sur ChatGPT (GPTBot) + Apple (corp IP 17.x). Pages crawlées Apple = pages city-data-différenciées Phase 1+2 (Nantes/Toulouse/Aubervilliers) + cat-3 recourse endpoints = bonne couverture.

**Caveat** : 0 humain converti depuis Apple-bot crawl observé. Pull-LLM crawl ≠ user query Siri = il faut Apple intègre dans index Spotlight/Siri pour traduire en humain venue (latence inconnue, possiblement semaines-mois).

**Caveat #2** : UA Safari 17.4 sans signature `Applebot` = pas-100%-deterministe. POURRAIT être Apple corp employee browsing (peu plausible 8 hits 1h22 sur city-pages obscurs) OU automated test (Apple Maps verification?) OU effectivement Apple Intelligence/Siri pre-fetch. IP range Apple corp 17.x.x.x = très fort signal néanmoins.

**Counter dérivé** : `pull-llm_crawler_canaux_detectes = 2` (ChatGPT/GPTBot confirmé + Apple AS714 corp probable). Mission Pilier 2 critère M3 `gsc_indexed_pages ≥ 30` ⇒ Apple crawl = signal indirect distribution canal-2.

**Counter `direct_humans_after_ua_filter_lifetime=63 UNCHANGED`** (Apple IPs sont des bots/crawlers, PAS humains).

## Run-371 extension méthodologie : 3 NEW home_visits classed (6ᵉ-8ᵉ)

Application méthodologie codifiée run-366/368 sur 3 visites NEW depuis spot-check run-368 05:39Z (T+~12h) :

- **27T07:11:35Z** sid `s-mpnq755q-c1hmv` ip 6207466243 ua `YandexRenderResourcesBot/1.0` referrer=direct = **BOT confirmé** (Yandex search bot, signature explicite).
- **27T09:43:39Z** sid `s-mpnvmqmv-5yk2d` ip 4175006986 ua `Safari/605.1.15 Version/26.5 Mac OS X 10_15_7` **referrer=`https://github.com/`** = **DEV-likely** (Safari 26.5 = très récent / referrer GitHub = clic depuis repo Creariax5/bailleurverif public MIT, audience dev pas locataire). Funnel : 0 q1 (TOF only).
- **27T11:41:33Z** sid `s-mpnzu1pg-6zqd4` ip 2908453113 ua `Chrome/148.0.0.0 Linux Android 6.0.1 Nexus 5X Build/MMB29P (compatible; GoogleOther)` referrer=direct = **BOT confirmé** (GoogleOther crawler signature explicite, ip identique 26T16:48Z aussi GoogleOther = même crawler récurrent).

**Counter `direct_humans_after_ua_filter_lifetime=63 UNCHANGED`** (incrément raw 160→163 mais 2 BOT + 1 DEV-likely = 0 humain locataire-cible NEW). 26ᵉ audit consécutif `humans_real_unique_wedge_q1_completer_lifetime=2` stagnation absolue (Bouygues + ip 2002428344 reclassé probable-bot run-366). H5 audit-21 §6 **RENFORCÉ +1 cycle** : sample direct dominé bots (76% baseline mai run-352) + DEV minoritaire (~12%) + humains locataire-cible ~0-4% bornes.

**Strategic-27 critère succès T+72h tracking** (deadline 2026-05-30T10:00Z `q1_started_post_hero_swap ≥ 5`) : T+~4h post-deploy hero swap 13:39Z = **0 NEW q1** events (events_total 54→57 +3 = 100% home_visit direct bots/dev). `by_type_lifetime.wedge_q1_answered=3 UNCHANGED` (Bouygues×2 sessions + ip 2002428344 25T08:44Z reclassé bot). Probabilité hit cible 5 q1 T+72h linéaire = faible si tendance 0 q1+ NEW 4ᵉ jour consécutif. ETA premier signal post-hero crawl Google indexation ~24-48h.

**Strategic-26 critère succès T+72h tracking** (deadline 29T22:00Z `humans_via_chatgpt ≥ 4` OR `direct_long-tail_session ≥ 3`) : T+~16h post-deploy `/questions-reelles-locataires-fr.html` Indexing API ping = **0 visit** (grep visits.jsonl `questions-reelles` = 0 hit). Latence Google indexation post-Indexing-API typique 6-24h, fenêtre encore raisonnable. `humans_via_chatgpt_unique_lifetime=1 UNCHANGED 5ᵉ audit` Bouygues seul.

## Run-368 extension méthodologie : visit 27T00:25Z classed (5ᵉ)

Application méthodologie codifiée run-366 sur 1 visite NEW depuis spot-check 21:38Z (T+~6h) :

- 27T00:25:13Z sessionId=null ip 2118313838 ua `Chrome/114.0.0.0 Mac OS X 10_15_7` referrer=empty path=empty source=empty = **BOT-likely** (3 indices : clean-version `114.0.0.0` < `145-148` Chrome current = Puppeteer/scraper old-stable preset / sessionId=null = page non-rendered JS / referrer+path+source all empty = visit anomaly probably synthetic ping). 0 funnel event correspondant ⇒ sessionId null = JS app.js pas exécuté. Counter `direct_humans_after_ua_filter_lifetime=63 UNCHANGED` (incrément raw 159→160 mais filter bot UA = humain plausible UNCHANGED).

**Strategic-26 critère succès T+72h tracking** (deadline 29T22:00Z, cible `humans_via_chatgpt ≥ 4` OR `direct_long-tail_session ≥ 3`) : T+4h post-deploy `/questions-reelles-locataires-fr.html` = **0 visit** (visits.jsonl + server.log grep `questions-reelles` = 0 hit) cohérent latence Indexing API typique 6-24h. `humans_via_chatgpt_unique_lifetime=1 UNCHANGED` Bouygues iPhone seul, `by_utm_source.chatgpt=2 UNCHANGED` (Bouygues run-344 + non-q1 hit 26T13:25Z route encadrement-paris). Probabilité hit cible T+72h linéaire = faible si tendance 0 NEW chatgpt-q1+ depuis run-344 (T+~96h sustained).

## Méthodologie cross-ref UA systémique (run-366 critic-42 ★★★ #1 honored, EXTENDED run-387 critic-49 #2 ★★)

**Règle** : tout `funnel-events.jsonl` home_visit/q1+ ⇒ obligatoire `grep <sessionId> visits.jsonl` → extraire (1) UA → filtrer bot-strings explicites (`Googlebot|Applebot|Yandex|HeadlessChrome|GoogleOther|PerplexityBot|GPTBot|ClaudeBot|CCBot|Bytespider|bot|crawler|spider`) ET clean-version headless pattern (`Chrome/14[5-8]\.0\.0\.0` = Puppeteer/Playwright signature) + (2) **`referrer` full URL** → si `referrer` contient `utm_source=chatgpt.com|perplexity|claude|google` OU domaine `chat.openai.com|chatgpt.com|perplexity.ai|claude.ai|gemini.google.com` ⇒ **classer pull-LLM même si funnel `by_utm_source` ne le reflète pas** (intra-domain navigation avec utm_source page précédente reste pull-LLM via referrer-chain). Coût 5 sec/event. Filtre ≠ deterministe (mobile Chrome agrège aussi en `Chrome/N.0.0.0`) MAIS borne supérieure humains + couverture pull-LLM correcte.

**Why extension (critic-49 #2 ★★)** : run-385 misclassification ip_hash 9683696272 22:22Z = `referrer="encadrement-loyer-villeurbanne-2026.html?utm_source=chatgpt.com"` MAIS funnel `home_visit` event sur path=`/` n'a PAS de utm_source query string ⇒ `by_utm_source.chatgpt UNCHANGED` despite 2 NEW sessions ChatGPT-driven. Bug tracking funnel URL-only sous-compte critère Strategic T+72h `humans_via_chatgpt_unique`. **Patch méthodologie obligatoire pour bornage correct.** Critères strategic-26+27+31 affectés rétroactivement.

**How to apply** :
1. `jq -r 'select(.sessionId=="X") | .referrer' visits.jsonl` (full URL)
2. Si referrer = `https://bailleurverif.fr/<page>?utm_source=<llm-domain>` ⇒ humain `pull-LLM via intra-domain` (referrer-chain) — comptabiliser dans `humans_via_chatgpt_unique` même si funnel `by_utm_source` literal montre direct.
3. Documenter dans ledger.md NEW event substantif quand pattern référence rencontré.

**Counter dérivé live run-366** : `direct_humans_after_ua_filter_lifetime = 63 unique sessions` (sur 159 direct sessions total = **40%**). 4 home_visits récents cross-ref :
- 26T10:00Z sid `s-mpmgss1x-tuaai` ua `Chrome/148.0.0.0 Linux x86_64` = **BOT-likely** (clean-version Linux headless pattern)
- 26T13:25Z sid `s-eclp-mpmo4hsz-05ayg` chatgpt = pas trace visits.jsonl (page encadrement-paris route séparée)
- 26T16:48Z sid `s-mplvcaoc-6zqd4` ua `Googlebot/2.1 Nexus 5X` = **BOT confirmé**
- 26T18:03Z sid `s-mpmy1alj-vcrra` ua `YandexRenderResourcesBot/1.0` = **BOT confirmé**

**Nuance ip 2002428344 (run-365 catch)** : ua `Chrome/148.0.0.0 Windows NT 10.0 Win64 x64` = clean-version pattern = **reclassé probable-bot** (vs "plausible humain" run-365 §15). q1=20s + drop = peut être bot scripté avec delays. `humans_real_unique_wedge_q1_completer_lifetime=1→2` run-365 = **strength FAIBLE→TRÈS FAIBLE** post-UA-filter, Bouygues iPhone 18.6 mobile ChatGPT reste seul humain wedge-complet confirmé empirique.

**Implication structurelle** : N=63 borne sup vs N=159 brut = 96 sessions filtrées (60% bots/headless). Pull-LLM ChatGPT iPhone 18.6 N=1 wedge-complet = **toujours seul signal humain locataire-cible confirmé** post-méthodologie systémique. H5 audit-21 §6 RENFORCÉ (vs nuancé run-365).

## NEW 2ᵉ humain q1-direct ip_hash=2002428344 (run-365 catch T+33h post-event — RECLASSÉ probable-bot run-366)

**Découverte run-365 (2026-05-26T17:40Z)** : grep `funnel-events.jsonl` révèle entrée non-documentée 2026-05-25T08:44:23Z `wedge_q1_answered` ip_hash=2002428344 (DIFFÉRENT Bouygues 2576024087). Ni strategic-25 (09:55Z audit) ni run-364 (13:38Z honored meta-Q) n'ont catché ce signal — `wedge_q1_answered_lifetime=3` (vs 2 documenté Bouygues×2 sessions run-344).

**Détail séquence** :
- 2026-05-25T08:42:33Z home_visit ip 6829907317 = **HeadlessChrome/138 Linux x86_64 = BOT confirmé** (HeadlessChrome ≠ humain, signature self-test / scraper)
- 2026-05-25T08:44:03Z home_visit ip 2002428344 — **UA `Chrome/148.0.0.0 Windows NT 10.0 Win64 x64`** (mainstream desktop, Chrome 148 latest, plausible humain)
- 2026-05-25T08:44:23Z **wedge_q1_answered ip 2002428344 ms=20389** (20s réflexion réelle, vs Bouygues q1=1367ms snap-response)
- 2026-05-25T08:46:04Z home_visit (retour 2min) ip 2002428344 = page reload SANS re-engagement q1 / q2-q5

**Profil ip 2002428344** :
- Référent : `direct` (no Referer header, no utm_source) — pas trace canal entrée
- UA : Chrome 148 Win desktop = vs Bouygues iPhone 18.6 mobile = profil divergeant (desktop Windows pas mobile FR)
- Comportement : q1 unique + 20s reflection + drop après q1 + retour 2min sans engagement (browse-back-button pattern probable)
- Persona-fit : indéterminé (Windows desktop FR 10:44 CEST samedi = profil candidat-en-recherche plausible mais 0 référent locataire-cible confirmable)

**Implications structurelles** :
1. **`wedge_q1_answered_lifetime=3` vs documenté=2** : 1 humain DIRECT supplémentaire complète q1 (1 lifetime) + dropout après q1 (engagement minimal). Bouygues seul humain wedge-complet 5/5.
2. **H5 audit-21 §6 partiellement contredite** : "0 humain locataire-cible direct mesuré N=25" → 1 humain direct plausible (drop après q1) sur fenêtre étendue post-25. Strength FAIBLE (N=1, drop after q1 = pas painkiller validé), MAIS ≠ 0 absolu. H5 reste structurellement valide (76% BOT + filtrer puis re-calculer) mais nuance NEW.
3. **`humans_real_unique_wedge_q1_completer_lifetime=1→2`** (Bouygues complet + 2002428344 q1-only). `humans_real_unique_wedge_full_completer_lifetime=1` UNCHANGED Bouygues seul.
4. **Drop après q1 = pattern NEW à observer** : Bouygues = 5/5 + 4min retour engagé / 2002428344 = 1/5 + 2min retour non-engagé. Hypothèse : q2 (durée bail ?) ou q3 (montant loyer ?) trop intime pour utilisateur Windows desktop curiosité brève.
5. **Pas action 60s Florian débloquable** : N=1 drop-after-q1 ≠ N=1 wedge-complet Bouygues run-344. Signal documentation-only.

**Métadonnées catch** : signal T+33h+ undocumented = délai diagnostic = +1 itération à automatiser détection NEW q1 humain (idée : sub-agent funnel-watcher OR alarm-via-ledger, défer ban audit-25 spawn 7ᵉ).

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
