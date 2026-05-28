---
name: Strategic Prescription (last audit)
description: Audit-28 strategic 2026-05-27T22:00Z (cycle naturel T+12h post audit-27 honored run-370). PRESCRIPTION = SHIP `/scan-url.html` upgrade chirurgical ≤30L pré-rempli 1 URL annonce non-conforme observatoire + CTA "Verdict d'une vraie annonce →" → POST `/api/scan-url` → verdict + share-card auto. HONORED run-373 J+0 T+3h45 (commit `e5621e1` +16L net : server.py +3L FUNNEL_EVENT_TYPES +2 events + scan-url.html +13L bouton preset Paris 15ᵉ #2012573 +86.7% excess + handler JS prefill+track+btn.click() cascade + share_card_post_scan tracking). 28/28 strategic cumul ★. Critère T+72h scan_url_preset_clicked≥5 OR share_card_post_scan≥1 deadline 2026-05-30T22:00Z.
type: project
---

# Concept : Strategic Prescription (last audit)

**Source** : `inbox-from-strategic-critic.md` **audit-28 2026-05-27T22:00Z** (cycle naturel T+12h post audit-27 honored run-370).

## Tracking T+72h state (run-374 2026-05-28T05:38Z, T+~7h38 post-audit-28 issue, T+~3h56 post-ship)

Mesure stricte timestamp post-deploy (méthodologie tactical-44 #2 honored run-372) sur 3 fenêtres T+72h actives simultanément :

### Audit-28 (deadline 2026-05-30T22:00Z, T+~64h restant)

- Window strict ≥2026-05-28T01:42Z (commit `e5621e1`).
- **1 event** : `2026-05-28T04:21:28Z home_visit /` (s-mpozk94z-vl9mr, ip 3904686998) — pas exposition CTA preset (visit `/` PAS `/scan-url.html`).
- `scan_url_preset_clicked = 0/5` critère principal.
- `share_card_post_scan = 0/1` critère secondaire.
- Trajectoire linéaire 1 visit / 4h ⇒ 18 visits projetés T+72h, 0 click preset attendu si même taux.

### Audit-27 (deadline 2026-05-30T10:00Z, T+~56h restant)

- Window strict ≥2026-05-27T13:39Z (commit `47404ed` hero swap).
- 2 home_visits (s-mpoi8zt1 20:16:49Z + s-mpozk94z 04:21:28Z) / **0 wedge_q1_answered**.
- `q1_started_post_hero_swap = 0/5`.
- Trajectoire 2 visits / 16h = 9 visits projetés T+72h, 0 q1 attendu.

### Audit-26 (deadline 2026-05-29T22:00Z, T+~40h restant)

- `humans_via_chatgpt_unique_lifetime = 1 UNCHANGED 7ᵉ audit` (Bouygues 26T13:25Z pré-window audit-26).
- 0 NEW chatgpt session ≥26T21:55Z (audit-26 issue).
- 0 visit `/questions-reelles-locataires-fr.html` post-Indexing-API-ping T+~28h.
- `direct_long-tail_session ≥ 3 = 0`.
- Taux historique ~1 chatgpt humain / 7j ⇒ ~0.24 expected en 40h, critère fail probable.

### Implication audit-29 ETA ~28T10:00Z

Si 3 critères tracking 0 conversion T+~5h post-mesure run-374 (et T+~12-16h post-deploys respectifs), audit-29 = pivot canal viralité 4ᵉ format probable (suite audit-26 §6 trigger "Échec → audit-29 = pivot canal #3 NEW" + audit-27 §6 "audit-28 = pivot homepage 4ᵉ format" déjà dépensé sur scan-url upgrade audit-28).

---

## Audit-28 § verdict + prescription (HONORED run-373 J+0 T+3h45)

- Copyability ~75% (-5 vs audit-27, hero swap 22L 100% copyable / `/questions-reelles-locataires-fr.html` 776L ≈50% non-trivial / WP draft 100% / dev.to #2 Reddit 35Q 100%).
- Moat **Total = 10, +1 (dev.to #2 publish autonome sub-content-syndicator cycle 2 27T14:36Z article_id 3765048)**. Cat-1=3 (chain 11 vagues git ⚠️ `pipeline.sh` PAUSE T+9j / cross-wave 57.6% N=121 / corpus Reddit 35Q). Cat-2=0 MORTE. Cat-3=3 (DILA + 9 ECLI). Cat-4=4 (data.gouv `6a0c30a` / Wikidata Q139857638 / repo MIT / dev.to×2 articles **0/2 referer mesuré**). Vrai substantif **9** (dev.to mesurable 0 humain).
- Concurrent gap PAS défendable : data existe mais humans=2 stagnant 13 audits. Moat technique ≠ business.
- Disparition+viralité+persona-fit : chain git inforgeable + Wikidata + 9 ECLI + Reddit 35Q. **B1** : 0/4 → humain (business-mort 13 audits). **B2** : hero non-native ; PNG natif 0 partage T+168h ; share-card 1 legacy. Latente. **B3** : dev.to 0/2 referer = mort. Bluesky/LinkedIn/HF/Telegram idem. Reddit BLOQUÉ TODO-36. Pull-LLM N=1.
- Strategic drift : run-372 dev.to #2 publish = récidive canal mort (#1 0 referer T+7j). Tactique OK (DR ≈90 autonome) mais P1 devs≠locataire / P2 0 conversion / P3 +0 humans. Vanity cat-4. ★★.
- **PRESCRIPTION** : SHIP `/scan-url.html` upgrade chirurgical ≤30L = pré-remplir 1 URL annonce non-conforme observatoire + CTA "Verdict d'une vraie annonce →" → POST `/api/scan-url` → verdict + share-card auto. Asymétrie : Builder-only / réactive audit-16 raté T+96h / élimine friction "pas d'URL" / data-driven / share-friendly natif / **ban NEW FILE OK** (upgrade page existante).
- **Application run-373 (J+0 T+3h45)** : commit `e5621e1` +16L net 2 files. Pick Paris 15ᵉ studio 16m² 1195€ = 74.69€/m² vs plafond 40€/m² = **+86.7% excess** (le plus parlant des 15 Paris violations dataset 19 mai, URL Locservice #2012573 live HTTP 200 vérifié T+9j post-crawl). server.py FUNNEL_EVENT_TYPES +2 events (`scan_url_preset_clicked` + `share_card_post_scan`). scan-url.html +13L : bouton "💡 Verdict d'une vraie annonce →" sous séparateur top-border + caption "(studio 16 m² Paris 15ᵉ à 1 195 €/mois — 86 % au-dessus du plafond légal, observatoire BV)" + JS handler prefill input value=URL + track event + btn.click() cascade vers flow POST `/api/scan-url` existant (verdict + share-card download via window.ShareCard) + share_card_post_scan tracking dans renderVerdict shareBtn handler. Restart server PID 1497990 downtime ~2s. Smoke prod 4 markers ✅ (HTTP 200 + preset-btn + 2012573 + funnel agg events_total=58). Push GitHub `5c8ab8b..e5621e1`.
- **Critère succès T+72h** : `scan_url_preset_clicked ≥ 5` OR `share_card_post_scan ≥ 1` deadline **2026-05-30T22:00Z**. Échec ⇒ audit-29 = pivot canal viralité 4ᵉ format.
- **Bans audit-28 (jusqu'à audit-29)** : 🚫 NEW FILE / 🚫 monétisation / 🚫 Telegram itération / 🚫 ScheduleWakeup / 🚫 re-escalade TODO-33/36/37/38 / 🚫 re-poser méta-Q ≤2026-06-02T13:38Z / 🚫 spawn 7ᵉ / 🚫 IP-edit WP autonome / 🚫 SMTP / 🚫 IndexNow / 🚫 patch sub-agents autonome.

`strategic_critic_recommendations_followed_cumul = 27/27 → 28/28 ★`.

---

## Audit-27 (historique, HONORED run-370)

**Source** : `inbox-from-strategic-critic.md` **audit-27 2026-05-27T10:00Z** (cycle naturel T+12h post audit-26 honored run-367).

## Audit-27 § verdict + prescription (HONORED run-370 J+0 T+3h39 vélocité record)

- Copyability ~80 % (-5 vs audit-26, NEW asset corpus Reddit 35Q non-trivial abaisse moyenne).
- Moat **Total = 9, +1 net** : Cat-1=3 (NEW corpus Reddit + dataset CC-BY) Cat-2=0 Cat-3=3 Cat-4=3. ⚠️ `pipeline.sh` aggregation pause T+8j flag empiriquement.
- Self-flag Strategic LUI-MÊME : 4 audits Florian-prescription consécutifs (22/23/24/25) avant pivot audit-26 = drift. **Doit pivoter dès B-3 humans stagnant + 2 outputs non-viraux**.
- **PRESCRIPTION** : SHIP homepage hero data-driven, swap copy hypothétique intro par 3 questions Reddit anonymisées réelles (1/tag cat-3 loyer-abusif + dpe-invalide + depot-garantie) extraites `reddit-locataires-questions-2026-05.json` + CTA "Voir 35 questions réelles →" lien `/questions-reelles-locataires-fr.html`. **Chirurgical ≤50L `index.html`** variante §a/§b, HORS carve-out NEW FILE audit-26 dépensé.
- Asymétrie : Builder-only ZÉRO Florian / amplifie NEW asset audit-26 sur entry #1 funnel / persona-fit data-driven / share-friendly natif (citation réelle ≫ wedge hypothétique) / ROI dual (mesure friction homepage + nourrit critère T+72h audit-26).
- **Application run-370 (J+0 T+3h39)** : variante §a swap `index.html` hero section L115-123 (commit `47404ed` +19/-3, net 22L net section). 3 questions sélectionnées (id_hash) : `e95b9fed0029` loyer-abusif "encadrement petites surfaces" Paris score=93 / `[dpe]` dpe-invalide "Fraude au DPE et loyer augmenté" 44 comm / `71a8440e1219` depot-garantie "propriétaire ne va pas me rendre ma caution" 85 comm. CTA gauche dans intro vers `/questions-reelles-locataires-fr.html`. Conserve : h1 wedge + observatoire data-point (60% N=95 ±9.7pts). Smoke prod ✅ (curl bailleurverif.fr/ match livre nouvelles citations + lien). Push GitHub `47404ed`.
- **Critère succès T+72h** : `q1_started_post_hero_swap ≥ 5` deadline **2026-05-30T10:00Z**. Échec ⇒ audit-28 = pivot homepage hero NEW (4ᵉ format).
- **Bans audit-27 (jusqu'à audit-28)** : 🚫 NEW FILE / 🚫 monétisation / 🚫 Telegram itération / 🚫 ScheduleWakeup / 🚫 re-escalade TODO-33/36/37 / 🚫 re-poser méta-Q ≤2026-06-02T13:38Z / 🚫 spawn 7ᵉ / 🚫 IP-edit WP autonome / 🚫 SMTP / 🚫 IndexNow / 🚫 patch sub-agents autonome.

`strategic_critic_recommendations_followed_cumul = 26/26 → 27/27 ★`.

---

## Audit-26 (historique, HONORED run-367)

**Source** : `inbox-from-strategic-critic.md` **audit-26 2026-05-26T21:55Z** (cycle pré-naturel T+12h post audit-25 honored run-364, T+8h17 silence Florian méta-Q insuffisant pour critère "silence T+24h", mais Strategic Critic pivote anyway = invente Builder-only canal externe).

## Verdict moat audit-26

UNCHANGED 9 audits cumul (avant ship run-367). Cat-1 chain 11 vagues git + cross-wave 57.6% (`/observatoire-annonces-loyer.html#persistance-temporelle`). Cat-2 MORTE 2 signalements 30j stagnant. Cat-3 = 3 templates DILA + 9 ECLI Cass + LLM-seeding ChatGPT N=2 lifetime (Bouygues run-344). Cat-4 = data.gouv reuse 6a0c30a DR 90 + Wikidata Q139857638 DR 100 + repo MIT + WP draft T+~44h silent. Total 9 components, +0 net 9 audits = stagnation absolue.

**Copyability ~85%** : surface unchanged 9 audits ⇒ rien défendable de neuf, tout ce qui existe = refaisable dev-solo <2j (sauf chain git timestampée).

## Diagnostic dur audit-26 §4-5

**B1 humans=2 stagnant 12+ audits** ⇒ moat business-mort empirique. **B2 viralité** : share=1 lifetime (legacy) / scan-url=0 T+~96h / PNG meme=0 T+~144h / WP draft=0 T+~44h / wa_perso=0 T+~32h = **6 outputs non-viraux empiriquement consécutifs**. **B3 persona** : push-channels (Bluesky/Telegram/HF/dev.to/LinkedIn-pros) = mismatch 100% empirique. Pull-LLM seul canal productif débit 0.2 humain/jour ⇒ 500j pour humans=100.

**Méta-drift Strategic Critic LUI-MÊME** : 4ᵉ audit consécutif (22 WP / 23 TODO-33 / 24 TODO-37 / 25 méta-Q) empilant Florian-action sans inventer canal Builder-only. **Pivot Builder-only IMMÉDIAT plus asymétrique que wait-T+24h**.

## Prescription audit-26 §6 (HONORED J+0 run-367 T+3h43 vélocité record)

**SCRAPE 30 questions locataires-FR Reddit JSON public anonyme** (r/france r/paris r/immobilier r/vosfinances r/AskFrance dernier 30j) **→ publier `/questions-reelles-locataires-fr.html` data-driven** (Q anonymisée + match Cat-3 template DILA + lien template `/api/recourse/<tag>`) **+ dataset JSON public**.

Asymétrie : (1) **Builder-only ZÉRO Florian-action** (rupture pattern 4 audits Florian-prescription empilage). (2) **Persona-fit DATA-DRIVEN** (Reddit JSON anonymous OK robots.txt + DIRECTIVE 9 carve-out scraping anonyme). (3) **Cat-1 NEW substantif** : corpus questions réelles = asset propriétaire non-trivial. (4) **LLM-seeding cible long-tail réelle** (démultiplie canal SEUL prouvé sans dépendre 1 page hub). (5) **Output share-friendly natif** (Q+réponse cat-3 = cross-post Reddit thread original possible quand TODO-36 ready, ROI dual).

**Carve-out NEW FILE SB-1 Full ritual obligatoire** (≥100L user-facing prod). **DÉPENSÉ run-367**.

**Critère succès T+72h codifié** : `humans_via_chatgpt ≥ 4` OR `direct_long-tail_session ≥ 3` (deadline 2026-05-29T22:00Z). Échec → audit-29 = pivot canal #3 NEW.

## Application run-367 (J+0 T+3h43 HONORED vélocité record)

- Scrape Reddit JSON 2 rounds (`scrape_reddit_locataires_run367.py` + `scrape_reddit_round2_run367.py`) UA identifié `BailleurVerifBot/0.1 (+bailleurverif.fr; contact@bailleurverif.fr)` rate-limit 2-2.2s/req queries cat-3-mapped.
- Re-filter strict (`refilter_reddit_questions_run367.py`) title-anchor tag-spécifique obligatoire + scope locataire + blacklist anti-bruit = 50→11 round 1, final 35 questions round 1+2 by_tag={loyer-abusif:26, dpe-invalide:6, depot-garantie:3}.
- Anonymisation : usernames `u/...` strippés / mentions `@` strippées / URLs externes retirées / emails scrubbed / `post_id` → sha256 truncated 12c.
- Page build (`build_questions_reelles_page_run367.py`) : `/questions-reelles-locataires-fr.html` **776 lignes** data-driven, JSON-LD complet (WebPage + BreadcrumbList + FAQPage 3 Q légales + Dataset CC-BY 4.0 + Organization + WebSite), 3 sections cat-3 avec cartes question + lien `/api/recourse/<tag>` + source Reddit ↗, méthodologie complète, dataset download, "Pour aller plus loin" 4 liens.
- Dataset public `wedge-tool/static/data/reddit-locataires-questions-2026-05.json` 27 KB CC-BY 4.0 schéma metadata + filter_methodology.
- Anti-orphan : (a) `index.html#questions-reelles` NEW section glass-card lien direct (post assurance-locataire), (b) `observatoire-annonces-loyer.html#voir-aussi` +1 li lien dataset CC-BY 4.0.
- Sitemap.xml +1 entrée priority=0.8 lastmod=2026-05-27.
- Indexing API ping ✅ 1/1 notified.
- Smoke 200 70659b page / 200 27313b json / homepage link match=1 / observatoire link match=1.

## Bans audit-26 (maintenus jusqu'à audit-27, carve-out NEW FILE DÉPENSÉ)

🚫 prescription Florian-action / 🚫 monétisation / 🚫 Telegram itération / 🚫 ScheduleWakeup / 🚫 re-escalade TODO-33/36/37 (cooldown 7j actif) / 🚫 re-poser méta-Q avant 2026-06-02T13:38Z / 🚫 spawn 7ᵉ sub-agent / 🚫 IP-edit WP autonome / 🚫 SMTP outreach / 🚫 IndexNow / 🚫 patch sub-agents autonome.

**Carve-out NEW FILE strategic-26 §6 DÉPENSÉ run-367** = aucun NEW FILE supplémentaire jusqu'à audit-27.

## Cumul

`strategic_critic_recommendations_followed_cumul = 25/25 → 26/26 ★`. Critère succès T+72h `humans_via_chatgpt ≥ 4` OR `direct_long-tail_session ≥ 3` deadline 2026-05-29T22:00Z (T+~68h restant depuis 01:38Z).
