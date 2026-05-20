# Concept : Signaux trafic réel (visiteurs non-Florian)

**État** : Émergent. Très peu de signal exploitable. 0 conversion observée.

## Source

`wedge-tool/data/visits.jsonl` (213 lignes au run-286). Champs : `ts`, `sessionId`, `referrer`, `path`, `source`, `ip_hash`, `ua`.

## Signaux notables (post run-286)

### Visiteur récurrent ip_hash `6994446044`

| # | ts UTC | referrer | path |
|---|---|---|---|
| 1 | 2026-05-18T08:04:59Z | https://www.google.com/ | `/` |
| 2 | 2026-05-18T11:24:22Z | direct | `/` |
| 3 | 2026-05-19T07:20:24Z | direct | `/` |

**Pattern** : 3 visites en ~23h, **toutes sur homepage `/` uniquement**. UA stable (Chrome 147 Linux X11). Premier hit post-GSC verify 2026-05-17.

**Interprétation possible** :
- Hypothèse A : utilisateur réel curieux, mais homepage ne convertit pas en clic profond (bounce répété → CTA homepage faible).
- Hypothèse B : Florian lui-même testant (mais Chrome 147 dev + ip_hash isolé du pattern usuel = à confirmer).
- Hypothèse C : Bot disguisé en Linux X11 (peu probable, 3 visites espacées sans burst).

**Implication mission 5000 users** : si A, signal que homepage doit pousser observatoire/loyer-abusif directement. Si B, faux signal.

### Référents externes captés

- `https://github.com/dapphub/dapptools/issues/160` (run-282 mention) : Open3CL issue #160 → session 94s 3 pages (utilisateur distinct du récurrent, single visit).
- `https://www.google.com/` (ip_hash 6994446044, 1ʳᵉ visite) : 1ʳᵉ visite organique Google post-GSC verify 2026-05-17.

## Métriques courantes (run-286)

- `visits_jsonl_lines=213`
- `recurring_visitors_count=1` (ip_hash 6994446044, 3 hits ≥2 jours distincts)
- `recurring_visitor_pages_per_session_avg=1.0` (homepage-only)
- `recurring_visitor_deep_navigation=false` (0 clic vers /observatoire ou /loyer-abusif)
- `google_organic_referrer_first_hit_at=2026-05-18T08:04:59Z`
- `open3cl_referrer_first_hit_at=2026-05-18T10:21Z` (run-282)

### Signal — ip_hash `2124423717` (investigué run-290)

**Critic-19 ★★ #2** (audit 09:55Z post run-287) : `ip_hash 2124423717` 09:47Z deep-nav OBS→HOME T+4h12min post-ANIL outbound (run-278 SMTP 05:35Z). Hypothèse écho ANIL ou bot crawler.

**Résultat investigation run-290** : `grep "2124423717" visits.jsonl` → **1 seule occurrence** (09:47:31Z), UA `Firefox 150 Windows 10 x64` (récent navigateur réel), referrer `https://bailleurverif.fr/observatoire-annonces-loyer.html` → path `/`. **Single-shot non-récurrent ≥24h** sur fenêtre check.

**Verdict** : curieux ponctuel, **PAS écho ANIL substantif** (ANIL répondrait probablement par mail SMTP plutôt que browser direct depuis IP propre). Navigation OBS→HOME = utilisateur qui découvre l'observatoire par lien externe et remonte vers home pour comprendre le site (pattern reverse-funnel intéressant mais isolé). **PAS de cat-4 substantif candidate** sans 2ᵉ visite ≥24h.

**Hypothèses secondaires** :
- Crawler bot disguisé Firefox 150 (peu probable, single-hit + referrer OBS interne suggère click humain).
- Visiteur Reddit/HN/Twitter ayant croisé une mention obs (mais 0 referrer captable = direct OR strip referrer).
- Florian lui-même testant depuis Windows VM (à confirmer si reconnaît l'UA).

**Action retenue** : pas de structurel ce wake. Re-check ip_hash `2124423717` runs +N — si 2ᵉ visite ≥24h, reclasser cat-4 substantif candidate.

## Bots indexers — inventaire (run-294)

Source `wedge-tool/data/visits.jsonl` (~220 lignes). Période 2026-05-16 → 2026-05-19 (~3.5 jours post-GSC verify).

| Crawler | Hits | Première visite | Dernière visite | Paths indexés observés |
|---|---|---|---|---|
| **Applebot** | **7** | 2026-05-16T11:18Z | 2026-05-19T10:43Z | `/`, `/preavis-bail.html` |
| Googlebot (desktop+mobile) | 5 | 2026-05-16T16:55Z | 2026-05-18T07:01Z | `/` |
| YandexRenderResourcesBot | 3 | 2026-05-16T13:01Z | 2026-05-17T07:52Z | `/` (resources render) |
| Bingbot | 1 | 2026-05-17T17:35Z | 2026-05-17T17:35Z | `/` |
| GPTBot / OAI-SearchBot | 0 | — | — | — |
| ClaudeBot / Anthropic | 0 | — | — | — |
| PerplexityBot | 0 | — | — | — |

**Signal cat-4 substantif** : Applebot **plus actif que Googlebot** (7 vs 5 hits, ratio inversé). Crawler Apple = ingestion Siri / Spotlight Search / Apple Intelligence / Maps. Pattern multi-jour (3 visites distinctes) + 2 paths indexés = re-crawl planifié, pas one-shot.

**Implication mission 5000 users** : Apple ecosystem FR a iPhones ~22-25% part de marché (audience captive iOS). Si Siri/Apple Intelligence ingère "encadrement loyer Paris" → exposition zéro-coût audience cible (B2C locataire). Aucun LLM crawler majeur n'est encore venu — ni GPTBot, ni ClaudeBot, ni PerplexityBot. Opportunité asymmetrique : optimiser `llms.txt` / `robots.txt` / meta tags pour LLM training crawlers.

**Action différée** : pas de nouvelle action externe ce wake (run-294, anti-spam-burst, critic-20 ~14:00Z). Documentation suffit. Re-check Applebot hits runs +N pour confirmer cadence régulière.

### Signal — Google referrer→deep-nav ip_hash `3790475865` (run-298, critic-20 ★★ #2) + cross-IP `6269819028` (run-306, critic-22 STOP #2 closure)

Critic-20 (audit 12:55Z) a flaggé deep-nav non-Florian via Google.com referrer 12:53Z **APRÈS** run-297, donc non-traité ce wake. Investigation run-298 :

| # | ts UTC | referrer | path | UA | ip_hash |
|---|---|---|---|---|---|
| 1 | 2026-05-19T12:53:19Z | `https://www.google.com/` | `/` | Chrome 147 Linux X11 | `3790475865` |
| 2 | 2026-05-19T12:53:32Z | (none, internal click) | `/preavis-bail.html` | Chrome 147 Linux X11 | `3790475865` |
| 3 | 2026-05-19T13:18-13:29Z | (5 hits deep-nav) | `/` + multi pages | Chrome 147 Linux X11 | `6269819028` |

**Pattern** : 2 IP hashes distincts (`3790475865` 12:53 + `6269819028` 13:18-13:29) **même UA Chrome 147 Linux X11** sur fenêtre ~30 min couvrant brief writing Florian 13:15-13:30Z (4 briefs TOP inbox 16:XXZ effectivement écrits ~13:15-13:30Z d'après timestamps).

**Hypothèses (critic-22 closure 24h max)** :

- **Hypothèse PRIMARY (preferred)** : **Florian self-audit during brief writing 13:15-13:30Z**. Probabilité : haute. Indices : (a) même UA Chrome 147 Linux X11 sur 2 IPs (NAT/VPN switch typique testing), (b) timing strict aligné brief writing window, (c) deep-nav `/preavis-bail.html` cohérent test path conversion mentionné brief, (d) cross-IP+same-UA = pattern self-test pas user organique. **Verdict probable : Florian-confirmed**.
- **Hypothèse SECONDARY (à invalider via recurrence check)** : utilisateur réel via Google "préavis bail" + utilisateur distinct deep-nav 25 min plus tard = 2 utilisateurs Chrome 147 Linux distincts. Probabilité : faible (coincidence UA + timing + path conversion brief = ~1% bruit).
- **Hypothèse TERTIARY** : bot crawler self-test (peu probable, 13s entre 2 hits + UA browser réel cohérent).

**Closure proactive 24h max** : reclasser Florian-confirmed si pas de récurrence 2ᵉ visite ≥24h depuis 2026-05-19T12:53Z (check due 2026-05-21T12:53Z). Si récurrence ≥24h détectée → reclasser utilisateur réel deep-nav substantif. Si null → Florian-confirmed locked.

**Action retenue run-306** : closure hypothèse documentée (PRIMARY Florian self-audit). Pas de modif `/preavis-bail.html` ni homepage. Cooldown re-check ip_hash `3790475865` + `6269819028` due 2026-05-21T12:53Z (48h depuis 1ʳᵉ visite).

## IndexNow round-69 verdict — théâtre confirmé puis CORRIGÉ "partial-functional" (run-317 2026-05-20T06:31Z)

### Verdict initial (run-315 04:30Z) — INVALIDÉ

`grep -c loyer-legal-paris visits.jsonl = 0` T+6h → "théâtre confirmé". **MAIS source `visits.jsonl` est JS-beacon-only**, sous-compte les bots par 22× (la plupart des crawlers ne rendent pas le JS).

### Verdict corrigé (run-317 06:31Z post-Florian inbox 06:00Z + `dashboard-extras.json` 06:28Z)

Source autoritative bot-crawl désormais = `wedge-tool/static/dashboard-extras.json` (parse `server.log*` filtré IPs internes, cron `*/2`). Spot-check `grep loyer-legal-paris wedge-tool/server.log.run-308-restart.log` :

- **9 hits IP `217.182.171.135` (VPS self-IP)** UA `curl/8.5.0` ou `Python-urllib/3.12` = auto-checks Builder/critic = internal noise.
- **1 hit IP externe `23.23.253.54` (AWS EC2)** à 2026-05-20T05:19:15Z UA `Mozilla/5.0 (compatible)` = **bot externe non-identifié** (probable IndexNow crawler Bing/Microsoft ack ou AWS-hosted scraper).

`dashboard-extras.json` confirme par ailleurs :
- `last_googlebot=2026-05-20T02:05:58Z` (Googlebot crawle quotidien — domaine indexé)
- `bot_hits_24h=32` (Googlebot 4, Bingbot 4, GPTBot 6, OAI-SearchBot 1, AhrefsBot 4, YandexBot 6, archive.org 3, FacebookExt 3, curl/wget 1)
- `chart_7days[2026-05-20].total=4` (Googlebot 2 + AhrefsBot 1 + curl/wget 1) — fenêtre encore tôt 06:30Z UTC

**Verdict corrigé** : IndexNow round-69 = **partial-functional**. ≥1 bot externe a crawlé Paris page T+7h post-ping. Googlebot crawle quotidien le site (vu hier 2026-05-19 ET aujourd'hui 02:05Z) MAIS ne s'est pas vu sur Paris page spécifiquement dans logs disponibles (server.log.run-308-restart.log ne couvre que post-22:30Z 2026-05-19). Latency réelle indexation Google = **toujours 24-72h hypothèse PRIMARY survivante**.

**Implications corrections aval** :

1. **Critic ledger** : critic-25 hypothèse "0 bot hit → théâtre" rebated par data source plus fiable. Pas erreur critic (basé sur source qui était officielle au moment audit), juste data-quality upgrade rétroactive.
2. **Source of truth bot crawl** : désormais `dashboard-extras.json` (lifetime + 24h + 1h + chart 7j + last_seen par bot). `visits.jsonl` reste source humains-approx (JS-enabled browsers).
3. **GPTBot 6 + OAI-SearchBot 1 lifetime** = présence dans index OpenAI/ChatGPT search **déjà acquise** (pas besoin chercher attirer plus, ils sont là).
4. **AhrefsBot 6 lifetime** = DR/backlinks vont apparaître dans index industrie SEO 2-4 sem (cat-4 moat compound).
5. **Googlebot ne crawle QUE `/robots.txt` + `/sitemap.xml` semble-t-il en 7j** (jamais pages contenu observable dans dashboard-extras) = **sandbox Google confirmé** typique nouveau site <30j. Patience 30-60j + signaux externes (backlinks autorité, mentions sociales). **★ MIS À JOUR run-318 2026-05-20T07:30Z : ce point #5 PARTIELLEMENT INVALIDÉ par Googlebot WRS Mobile sortant de sandbox, voir section dédiée plus bas.**

**Implication mission revenu passif (maintenue depuis run-315)** : reconnecter discussion canal humain (drafter cycle 2 + post Florian validation TODO-32-bis) reste pertinent. Pas de pivot stratégique sur cette correction — moat compound se construit ailleurs (mail Que Choisir T+2h, ANIL T+25h, presse 0/4 T+60h).

## Signal — NEW visitor ip_hash `2925209098` mobile Android via Lille DPE F/G (run-316 2026-05-20T05:18Z)

**Premier signal organic-looking depuis 15h+ silence** (last 13:29:30Z 2026-05-19 ip_hash 6269819028 Florian self-audit closure run-306).

| # | ts UTC | referrer | path | UA | ip_hash |
|---|---|---|---|---|---|
| 1 | 2026-05-20T05:18:03Z | `https://bailleurverif.fr/lille-dpe-f-g-interdit-location.html` | (empty) | Chrome 148 **Mobile Android 10** | `2925209098` |
| 2 | 2026-05-20T05:18:04Z | `https://bailleurverif.fr/lille-dpe-f-g-interdit-location.html` | `/` | Chrome 148 Mobile Android 10 | `2925209098` |

**Pattern** : 2 hits 1s apart, **UA mobile Android Chrome 148** (DIFFÉRENT du pattern Florian Chrome 147 Linux X11 sur ip_hash `6994446044`/`6269819028`/`3790475865`). Path 1 empty = beacon JS initial, path 2 = `/` navigation tracking complète. Referrer LILLE DPE F/G ON BOTH = visiteur d'abord sur page programmatique DPE F/G Lille (page tracking-less ou cache), puis clic vers homepage.

**Hypothèses** :

- **Hypothèse PRIMARY (preferred)** : Visiteur réel mobile, arrivée organique sur `/lille-dpe-f-g-interdit-location.html` (Google/social/direct), navigation programmatique SEO city-page → homepage. Probabilité : haute. Indices : (a) UA Mobile Android distinct des patterns Florian X11 Linux, (b) timing T-12min avant run-316 = pas aligné brief writing Florian observable, (c) path empty + path `/` 1s apart = double beacon JS pattern d'un browser réel pas pattern bot scriptable, (d) 0 deep-nav Paris page = visiteur n'a pas vu URL `/loyer-legal-paris` (page non-cross-linkée depuis Lille DPE F/G).
- **Hypothèse SECONDARY (à invalider via recurrence check)** : Bot maquillé Mobile Android Chrome 148 single-shot non-récurrent. Probabilité : faible (UA très récent + 2 hits structure beacon humain + Lille→home navigation pattern humain).
- **Hypothèse TERTIARY** : Florian on mobile testing. Probabilité : très faible (Florian usually X11 Linux Chrome 147 desktop, jamais vu Mobile Android dans patterns historiques).

**Implication mission revenu passif** :

1. **Pilier 2 SEO compounding validé partiellement** : page programmatique `lille-dpe-f-g-interdit-location.html` (générée vague 1ʳᵉ batch DPE F/G N=7 villes run-XXX) **GÉNÈRE TRAFIC**. Donc le modèle "1 page programmatique → 1+ visiteurs organic-like" tient. Pas Paris page mais cousine.
2. **Page Lille tracking-less** : les visites sur `/lille-dpe-f-g-interdit-location.html` elle-même ne sont PAS dans visits.jsonl (pas d'instrument client tracking). Seule la navigation OUT (vers `/`) est captée via referrer. **Coût bookkeeping** : visits.jsonl undercount programmatique pages by 100%. Pas urgent mais à noter.
3. **0 deep-nav Paris page** : visiteur Mobile Android n'a pas vu URL Paris. Donc fenêtre mesure Paris J+7 (deadline 2026-05-26T22:30Z) intacte, ce visiteur n'est pas un candidat capture (focused sur DPE pas loyer).
4. **NE PAS scaler Paris→Lyon avant signal Paris 7j** (BAN strategic-9+10 maintenu). Le signal vient page DPE F/G PAS page Paris — donc signal de validation modèle programmatique général, pas signal capture iter-1 Pilier 1.

**Action retenue run-316** : documentation only. Pas de tracking instrument page Lille (anti-touch programmatique iter-1 mesure ouverte) + pas de cross-link Lille→Paris hardcoded (anti-touch Paris page A/B). Re-check ip_hash `2925209098` recurrence ≥24h cible 2026-05-21T05:18Z — si 2ᵉ visite récurrence → reclasser cat-4 substantif candidate ; si null → single-shot organic-like documenté.

## Action retenue (run-286, maintenue)

**Documentation only**. Pas de refonte homepage sans validation Florian/strategic-critic. Ce concept sert d'intel pour le prochain audit strategic (critic-20 attendu ~14:00Z).

## Action différée (post critic input)

- Si critic-19 recommande optim homepage CTA → ajouter bandeau « Voir l'observatoire (43 violations N=210 dernière vague) » au-dessus du fold.
- Sinon : continuer baseline, surveiller si `recurring_visitors_count` augmente sur ≥3 visiteurs distincts (seuil signal vs bruit).

## ★ Signal — Googlebot WRS Mobile RENDERED HOMEPAGE WITH JS (run-318 2026-05-20T07:30Z)

**Découverte ce wake** : 1ʳᵉ trace concrète Googlebot **WRS (Web Rendering Service) Mobile-First Indexing** rendant la homepage avec exécution JavaScript complète.

### Séquence chronologique (server.log.run-308-restart.log)

| ts UTC | IP | requête | UA |
|---|---|---|---|
| 2026-05-20T05:46:50Z | 217.182.171.135 | HEAD / | Googlebot/2.1 (basic) — self-IP self-check |
| 2026-05-20T06:39:59Z | 66.249.73.129 | GET /robots.txt | Googlebot/2.1 (basic, AS15169 Google) |
| 2026-05-20T06:40:00Z | 66.249.73.129 | GET / | **Googlebot Mobile WRS Chrome 148** (Nexus 5X) |
| 2026-05-20T06:40:02Z | 66.249.73.129 | GET /api/changelog?limit=5 | Googlebot Mobile WRS Chrome 148 |
| 2026-05-20T06:40:03Z | 66.249.73.129 | POST /api/visit | Googlebot Mobile WRS Chrome 148 |

**Diagnostic** : Googlebot Mobile WRS UA = `Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.7778.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)`. C'est le bot **rendering** Google (distinct du basic crawler) qui exécute JavaScript pour Mobile-First Indexing.

**Preuve rendering JS** : POST `/api/visit` à T+3s post-GET `/` = beacon JavaScript déclenché par `app.js` (notre instrument client). GET `/api/changelog?limit=5` à T+2s = appel JS dynamic interne homepage (composant changelog). Ces 2 endpoints **ne peuvent être appelés QUE si JS s'exécute**.

### Implications stratégiques

1. **Sandbox Google sortie partielle (≥1 page rendered)** : verdict précédent "Googlebot ne crawle QUE robots.txt + sitemap.xml" est PARTIELLEMENT FAUX au moins pour homepage. WRS est entré. Pages programmatiques (Paris, Lille DPE, etc.) PAS encore vues dans logs WRS, mais infrastructure crawling activée.
2. **Mobile-First Indexing actif** : Google indexe la version mobile = nos optims mobile (responsive viewport, touch CTAs) **comptent**. Notre layout mobile-first est OK (vérifié pré-ship). Pas d'action structurelle nécessaire.
3. **Dynamic content visible Google** : JSON-LD injected via JS (FAQPage, Dataset) + verdict €/mois calculator output + observatoire stats sont **probablement vus Google** car JS s'exécute. C'est le scénario optimiste qu'on espérait sans en avoir preuve.
4. **Sitemap effectiveness** : Googlebot lit `/robots.txt` 4× en 24h + `/sitemap.xml` régulièrement. Ship indexNow + sitemap path = bonne décision.
5. **Round-69 verdict révisé +1** : "partial-functional" (1 bot externe AWS run-317) + maintenant "Googlebot WRS confirmé" → upgrade à **functional Mobile-First**.

### Nouvelle hypothèse à valider

- **Indexation Google homepage dans SERP** : checker `site:bailleurverif.fr` next 7-14j sur compte Florian GSC (Florian-side, TODO existant). Si pages programmatiques apparaissent en SERP = sandbox levée pour ces pages aussi.
- **Pas de structural change ce wake** : laisser fenêtre mesure Paris ouverte (deadline 2026-05-26T22:30Z), ne pas toucher A/B baseline.

**ip_hash `2872988250`** = Googlebot Mobile WRS Nexus 5X (NEW). Stable IP range 66.249.73.x AS15169 Google.

**Action retenue run-318** : documentation only (concept update + inbox.md HEAD signal Florian). Pas de touch HTML, pas de spawn agent dédié, pas d'IndexNow re-ping (anti-théâtre).
