---
name: SEO discipline — no orphan pages + BreadcrumbList template rule
description: Règles immuables shipping pages HTML : (1) linkées depuis ≥1 page indexée AVANT "shipped" (run-318) ; (2) BreadcrumbList JSON-LD doit avoir champ `item` sur tous les ListItem (codified 2026-05-20T10:30Z run-321 brief Florian post-GSC URL Inspection 81 pages cassées).
type: feedback
---

# SEO Discipline — no orphan pages (codified 2026-05-20T07:30Z run-318, brief Florian 06:35Z)

## Règle (immuable)

Toute nouvelle page HTML shippée (programmatique ville/arrondissement, blog, recours, observatoire) DOIT être linkée depuis ≥1 page déjà indexée Google AVANT d'être considérée "shipped".

**Why** : Sandbox Google < 90j sites = sitemap.xml seul = signal faible. Sans backlink interne depuis page indexée, Google déprioritise massivement l'indexation. Internal link from indexed page = signal fort propagation. **Preuve empirique observée run-318 brief Florian 06:35Z** : `/lille-dpe-f-g-interdit-location.html` (linkée homepage L542) → 1 visiteur organic 2026-05-20T05:18Z. `/loyer-legal-paris.html` (orpheline) → 0 visiteur 9h post-ship + GSC URL Inspection "Cette URL n'a pas été indexée par Google + Aucune page d'origine détectée".

**How to apply** :

## Pages sources-of-juice (indexées Google, confirmées)

- `/` (homepage) — verified GSC verify 2026-05-17 + Googlebot WRS render 2026-05-20T06:40Z (run-318)
- `/observatoire-annonces-loyer.html` — verified visits.jsonl + dataset data.gouv.fr backlink
- `/lille-dpe-f-g-interdit-location.html` — 1 visiteur organic 2026-05-20T05:18Z (preuve juice)

## Pages encore-orphelines (à monitorer)

- Pages DPE F/G autres villes (Paris, Marseille, Lyon, etc.) : linkées section `#dpe-cities` homepage L535-546 ✅
- Pages encadrement loyer Paris : **FIXED run-318** ajout section `#outils-paris` homepage + section "Voir aussi" observatoire
- Pages recours `/recourse/<tag>` : statut inconnu, vérifier batch séparé

## Workflow obligatoire à chaque ship page X

1. Identifier la page parent sémantiquement pertinente :
   - ville X = homepage section dédiée (ex: `#dpe-cities` ou `#outils-paris`) + observatoire si pertinent
   - recours X = page recourse-index ou observatoire footer
   - blog X = `/blog/` index (déjà fait naturellement par template blog)
2. Ajouter ≥1 `<a href="/X.html">` depuis cette page parent **dans la même PR/commit que le ship**
3. Vérifier post-ship : `grep "/X.html" wedge-tool/static/index.html wedge-tool/static/observatoire-annonces-loyer.html` = ≥1 match
4. Ledger ACTION mention "internal-link added from parent: /parent.html"
5. Sub-seo-monitor Haiku peut audit nightly (grep orphans dans sitemap vs homepage links) — optionnel, à intégrer cycle suivant

## Conséquence violation (mesurée)

Page orpheline indexée 30-90j (vs 24-48h linked). Pendant sandbox <90j = quasiment jamais. Page Paris run-309 ship → 9h+ post-ship + 0 indexation GSC = preuve empirique sans linking on est dans le second cas.

## Anti-pattern à éviter

- ❌ Ship page sans audit linking parent
- ❌ "Sitemap suffit" mental model (faux pendant sandbox <90j)
- ❌ Bulk-generate 200 pages ville sans plan d'internal linking entre elles (toute la stratégie Pilier 2 SEO compounding sabotée silencieusement)
- ❌ Ajouter lien dans page non-indexée (perd 90% effet propagation)
- ❌ Linking entre 2 orphelins = chaîne suspendue, pas de juice qui descend

## Override / fallback

- Si urgence ship sans parent indexé immédiatement → ledger flag `[ORPHAN-FLAG]` + TODO follow-up dans concept + audit sub-seo-monitor cycle suivant.
- Si page programmatique batch (ex: 50 villes d'un coup) → 1 section homepage dédiée OBLIGATOIRE (cf. `#dpe-cities` pattern) + cross-link entre pages du batch (Paris → Marseille → Lyon, ring topology).

## Action retroactive run-318 (fix initial)

- Homepage `index.html` : ajout section `#outils-paris` avec 2 liens (`/loyer-legal-paris.html` + `/encadrement-loyer-paris-2026.html`) après `#outil-hub-encadrement`.
- Observatoire `observatoire-annonces-loyer.html` : ajout section `#voir-aussi` bas de page avec 4 liens (paris-calc + paris-encadrement + france-hub + Lille DPE).
- Commit + push GitHub same wake.
- Florian-side : GSC re-soumission sitemap + URL Inspection forced indexation 4 pages stratégiques (zéro charge agent).

## Lien avec Googlebot WRS run-318

Googlebot WRS Mobile rendant homepage avec JS confirmé 2026-05-20T06:40Z = Google découvre les nouveaux liens internes à chaque crawl WRS (24-48h cadence post-sandbox). Donc ce fix orphan = **propagation rapide attendue** sur les 4 pages stratégiques d'ici 2-7j. Re-check GSC index status due ≥2026-05-22.

---

# BreadcrumbList JSON-LD template rule (codified 2026-05-20T10:30Z run-321, brief Florian 09:45Z)

## Règle (immuable)

Tout `BreadcrumbList` JSON-LD généré par template DOIT avoir un champ `item` (URL absolue HTTPS) sur **tous** les `ListItem`, sans exception. Le champ `item` est techniquement optionnel pour le dernier item selon schema.org mais **Google le préfère partout** pour Rich Results breadcrumb.

**Why** : 81 pages prod ont été invalidées silencieusement par Google pour Rich Results breadcrumb (mais restaient indexées). Découverte via GSC URL Inspection manuelle Florian sur `/encadrement-loyer-paris-2026.html` 2026-05-20T~09:30Z. Pattern incident :
- 31 pages `encadrement-loyer-*.html` : position #2 `"name": "Encadrement des loyers"` SANS `item`
- 50 pages `*-dpe-f-g-interdit-location.html` : position #2 `"name": "DPE & passoires thermiques"` SANS `item`

Fix Florian via Python `str.replace()` propagé aux 81 + ~9 pages connexes (guide-*, scanner, IRL, preavis, deficit-foncier, locataire-loyer-legal, loyer-legal-paris). Commit `3ee81da` run-321 J+0 (90 fichiers HTML).

**How to apply** :

## Pattern correct (template à respecter pour toutes pages futures)

```json
{
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Accueil",
     "item": "https://bailleurverif.fr"},
    {"@type": "ListItem", "position": 2, "name": "<Catégorie>",
     "item": "https://bailleurverif.fr/<hub-categorie>.html"},
    {"@type": "ListItem", "position": 3, "name": "<Page courante>",
     "item": "https://bailleurverif.fr/<page-courante>.html"}
  ]
}
```

## Hubs de catégorie canoniques (à utiliser comme `item` URL pour position #2)

| Nom catégorie | URL hub `item` |
|---|---|
| `Encadrement des loyers` | `/encadrement-loyer-france-2026.html` |
| `Loyer légal` | `/encadrement-loyer-france-2026.html` |
| `DPE & passoires thermiques` | `/dpe-fiabilite.html` |
| `Guides` | `/` (homepage, fallback) |
| `Outils gratuits` | `/` (homepage, fallback) |
| `Observatoire` | `/observatoire-annonces-loyer.html` |

Si nouvelle catégorie introduite (ex: `Notation agences`, `Recours locataire`) → créer le hub AVANT la 1ʳᵉ page enfant, OU choisir un hub existant proche sémantiquement.

## Anti-pattern à éviter

- ❌ Générer `BreadcrumbList` avec position #2 sans `item` ("optionnel" ≠ "à omettre")
- ❌ Mettre `item` uniquement sur position #1 et #3
- ❌ URL relative dans `item` (Google exige absolue HTTPS)
- ❌ Introduire nouvelle catégorie sans hub correspondant

## Détection automatisée (sub-seo-monitor cycle suivant)

Audit quotidien Haiku : `grep -L '"item":"https://bailleurverif.fr/' wedge-tool/static/*-*.html` pour détecter toute page avec BreadcrumbList où `item` manque. Alert dans `inbox.md` HEAD si trouvé. Patch sub-seo-monitor prompt run-321 J+0.

## Pourquoi cette discipline matters

1. **Rich Results breadcrumb visible dans SERP Google** = 5-15% CTR boost mesuré (doc Google)
2. **JSON-LD = signal sémantique fort** Knowledge Graph + LLM scrapers (GPTBot/OAI-SearchBot/ClaudeBot crawlent déjà)
3. **81 pages affectées** = invalidité massive non-flaggée jusqu'à URL Inspection manuelle Florian = angle mort historique sub-seo-monitor

## Canary indexation post-fix (zéro charge agent)

Florian à demander indexation GSC J+0 sur 2 pages canary :
- `https://bailleurverif.fr/encadrement-loyer-paris-2026.html`
- `https://bailleurverif.fr/aix-en-provence-dpe-f-g-interdit-location.html`

Si breadcrumb redevient "valid" J+1/J+2 → fix systémique confirmé sur 90 pages.

---

# Indexing API Google rule (codified 2026-05-21T09:55Z run-333, brief Florian 09:30Z)

## Règle (immuable)

Toute nouvelle page user-facing HTML shippée DOIT être pingée Indexing API Google dans le même wake post-commit. Sitemap.xml passif ne suffit PAS (latence 2-4 semaines vs API 15min-48h).

**Why** : Florian a setup 2026-05-21T09:30Z un service account Google Cloud `bailleurverif-indexing@bailleurverif-indexing.iam.gserviceaccount.com` auto-vérifié owner `https://bailleurverif.fr/`, avec quota 200 URLs/jour. Tool live `agent-browser/indexing_api_ping.py`. Asymétrie : 24h vs 2-4 sem propagation = ROI immédiat SEO compounding Pilier 2 (mission RECALIBRÉE 2026-05-21T07:35Z reste valide structurellement même si "vanity SEO" non-prio absolue — pages nouvelles ne sont PAS vanity SEO).

**How to apply** :

## Workflow obligatoire post-ship NEW page HTML

1. Ship page X.html + internal link parent (cf règle anti-orphan ci-dessus)
2. Commit + push GitHub same wake
3. **NEW** : `python3 agent-browser/indexing_api_ping.py https://bailleurverif.fr/X.html`
4. Log auto-append `wedge-tool/data/indexing-api.jsonl`
5. Ledger ACTION mention "indexing-api ping ok|error"

## Anti-patterns à éviter

- ❌ Ship page sans ping Indexing API (Sitemap suffit mental model = faux)
- ❌ Re-pinger même URL <72h (Google rate-limits backend)
- ❌ Batch >200 URLs/jour (quota cap 200 partagé global projet GCP)
- ❌ Pinger MAJ contenu page existante (Indexing API = `URL_UPDATED` valable mais discrétionnaire ; cible primaire = nouvelles URLs)
- ❌ Supprimer fichier `wedge-tool/static/google69a01ab508377433.html` (casserait vérification SA owner)

## Batch initial sitemap (run-334+ 02:30Z UTC quotidien)

Florian a déjà soumis 8 URLs prioritaires 2026-05-21T09:30Z (quota restant=192/200 jusqu'à 02:00 Paris reset minuit UTC). Action agent demain ≥02:30Z UTC : `python3 agent-browser/indexing_api_ping.py --all` pour batch les ~170 URLs sitemap restantes. Si HTTP 429 mid-batch → script stoppe propre, relance jour suivant.

## Monitoring (sub-seo-monitor cycle suivant + spot-checks Builder)

- Logs JSONL : `wedge-tool/data/indexing-api.jsonl` (append-only)
- Si error rate >10% sur 24h → flag `inbox.md` HEAD priorité ★★
- Spot-check possible : `grep -c '"status":"error"' wedge-tool/data/indexing-api.jsonl` vs `wc -l indexing-api.jsonl`

## Credentials .env (déjà set Florian)

- `GOOGLE_INDEXING_API_KEYFILE` (path keyfile JSON)
- `GOOGLE_INDEXING_API_SA_EMAIL` (service account email)

## Pourquoi cette discipline matters (mission RECALIBRÉE check)

Mission 2026-05-21T07:35Z dit NON-PRIO "vanity SEO (pages_total brut, IndexNow rounds, JSON-LD coverage)". **Distinction clé** : Indexing API ping new page ≠ vanity. Vanity = ship 50 pages programmatiques bookkeeping. Indexing API = optimiser la propagation des pages déjà décidées comme priorité (proof-of-pattern Paris, Lille DPE, futurs). Pillar 2 acquisition compounding bénéficie directement. Donc OK avec mission. Mais NE PAS générer des nouvelles pages JUSTE pour pinger l'API (anti-vanity).

# Règle "≥4 sections data locale unique" — pages programmatiques (codifiée 2026-06-02T14:30Z run-412, pattern Lille run-411 + Villeurbanne run-412)

## Règle (immuable)

Toute page programmatique (encadrement-loyer-`<ville>`, `<ville>`-dpe-f-g, arnaque-location-`<ville>`) DOIT comporter **au moins 4 sections de data locale unique** au-dessus du template-substitution standard, sinon Google déduplique → 1-2 pages indexées sur N, le reste invisible.

**Why** : Brief Florian 2026-06-01T15:45Z verbatim *"Pages programmatiques pas différenciées faut fix ça"* après mesure sur 93 pages programmatiques avec ~95 lignes différentes sur ~800-1500 = template-substitution pur. Conséquence GSC mesurée : Paris écrase (104 imp), Villeurbanne 11, Echirolles 10, le reste = 0. Strategic-39 a confirmé le pattern (run-411 Lille +150L, run-412 Villeurbanne +54L denses).

**How to apply** : à chaque ship OU enrichissement de page programmatique, vérifier la présence des 4 sections minimum.

## Les 4 sections obligatoires

1. **Observatoire BV local** (cat-1 réutilisé) : N annonces locales scrapées + taux violation clear/presumed + dépassement moyen €/m² + DPE risk count + comparaison nationale (mean 18 communes N=843). Source : `wedge-tool/static/data/observatoire-annonces-loyer-cumulative.csv` filtré sur `ville_label`.
2. **Statut légal local exact** : citations directes décrets/arrêtés + liens Légifrance stables (.gouv.fr) + dates de prise d'effet + particularités locales vérifiables (zone tendue / permis de louer si applicable / encadrement expérimental / DPE national). Ne JAMAIS inventer un arrêté préfectoral DPE — le calendrier DPE F/G/E est strictement national, aucune dérogation préfectorale possible (anti-fake-data DIRECTIVE 9 §3).
3. **FAQ locale 8+ Q/R DILA-verified** : adresses ADIL locale + TJ ressort + CDC départementale + jurisprudence Cass. récente + recours administratifs locaux. Format JSON-LD FAQPage `mainEntity` synchronisé pour Rich Results.
4. **Jurisprudence ressort CA local** : 2-3 ECLI Cass. civ. 3 issues du corpus `data/interpretation-library-v0/recourse-templates/<tag>.v0.json` (Judilibre-verified production). Précision juridique : ces arrêts Cass. civ. 3 lient toutes les CA du ressort (art. L.411-3 COJ) — pas besoin d'ECLI CA-spécifiques fabriqués.

## Pattern de référence (à reproduire)

- **Lille** run-411 : `/lille-dpe-f-g-interdit-location.html` 367→516L (+150L) — 4 sections shippées strategic-39 J+0.
- **Villeurbanne** run-412 : `/encadrement-loyer-villeurbanne-2026.html` 277→331L (+54L denses) — 4 sections shippées Phase 1 brief Florian J+1 continuation.

## Anti-pattern à éviter

- ❌ Section "Observatoire" sans N réel (calcul depuis CSV obligatoire, pas placeholder)
- ❌ Section "Jurisprudence" avec ECLI fabriqués CA locales (uniquement Cass. civ. 3 + précision "lie CA du ressort")
- ❌ FAQ locale ≤5 Q/R (insuffisant Rich Results SERP density)
- ❌ Section "Arrêté préfectoral DPE" littérale — DPE national zéro dérogation locale, reframe honnête sur zone tendue / encadrement expérimental
- ❌ Regen 93 pages d'un coup — cadence 1 page/wake substantif (qualité > quantité, brief Florian)
- ❌ Copy-paste sections entre villes — chaque ville doit avoir chiffres + adresses + jurisprudence (si applicable) propres

## Cadence Phase 1 brief Florian

Priorité absolue = pages avec impressions GSC déjà acquises (juice indexée éprouvée > sandbox 90j NEW) :

1. ✅ Paris-2026 (104 imp) — title rewrite run-409
2. ✅ Lille DPE (21 imp) — enrich strategic-39 run-411
3. ✅ Villeurbanne (11 imp) — enrich Phase 1 run-412
4. ⏳ Echirolles (10 imp) — prochain wake substantif candidat

Au-delà : top observatoire (Lyon Paris-arr Marseille Bordeaux Toulouse Nantes) puis long-tail opportuniste.

---

# Discipline 11 — Build the verification tool BEFORE escalating fact-check doubts (codifiée 2026-06-03T11:00Z run-422+, brief Florian inbox HEAD)

## Règle (immuable)

Quand tu rencontres un doute factuel — typiquement régime juridique, date d'effet, périmètre administratif — et SI ce doute est :

1. **Re-occurring** (le cas n'est pas isolé : ≥2 autres pages probables avec même type de question)
2. **Automatisable** (sources publiques structurées dispo : Légifrance API, Wikipedia FR, Service-Public.fr, gov.fr datasets, ANIL)
3. **Aligné mission** (P1 produit-excellence accuracy / P2 SEO E-E-A-T)

ALORS : **construire l'outil de vérification autonome AVANT d'escalader Florian**. Escalade légitime uniquement si :

- Sources publiques contradictoires (vrai gap d'interprétation juridique)
- Action a impact externe ≥50€ (validation Florian explicit budget)
- Pas de source publique exploitable (Légifrance/Service-Public/Wikipedia/ANIL vides)

**Why** : Florian time = ressource la plus chère du système (HUMAN_DIRECTIVE.md DIRECTIVE PRINCIPALE). Chaque escalade évitable = ~quart d'heure Florian perdu. Un script 30-60 min de dev autonome règle structurellement le doute pour N pages à la fois — pas seulement la page courante. Anti-pattern observable : run-414 Échirolles a flaggé honest doute régime ELAN art 140 Grenoble Métropole + escaladé inbox HEAD au lieu de construire `check_legal_regime.py` autonome. Florian l'a fait à sa place (seed run-422 trail) en flaggant explicitement *"il aurait d'ailleurs dû prendre cette décision par lui-même"*. La grappe Grenoble (5 pages) + 28+ autres cross-claim potentielles = 28+ escalades évitables si on reste en mode "flag + escalade".

**How to apply** :

## Workflow obligatoire face à un doute fact-check

1. Identifier la classe du doute : `(re-occurring? automatisable? aligné mission?)`
2. Si 3/3 OUI → **STOP escalade, BUILD tool**. Si <3/3 OUI → escalade OK avec justification ledger.
3. Construire le tool dans `agent-browser/` (Python stdlib + urllib, pas de deps tierces).
4. Sources de vérité par ordre d'autorité :
   1. **Légifrance API** (PISTE_CLIENT_ID/SECRET déjà en `.env`, utilisé par `piste_oauth.py`)
   2. **Service-Public.fr** (crawl + parse)
   3. **Wikipedia FR** (cross-check confiance)
   4. **ANIL FAQ / DRIHL / DDETS** (secondaires)
5. Output JSON structuré minimal : `regime`, `date_effet`, `confidence_score` 0-1, `sources` array, `note_juridique`, `epci_membre` si applicable.
6. Re-run sur **toutes** pages concernées (pas seulement la déclencheuse).
7. Backfill correction immédiate des pages affectées (disclaimer banner visible + JSON-LD `note` honnête).
8. Régénération hebdo cron OR sub-agent pour capter nouveaux arrêtés.

## Tool de référence (canonical)

- **`agent-browser/check_legal_regime.py` v2 (2026-06-03)** : authoritative table + cross-check Wikipedia FR + Service-Public.fr + confidence_score + EPCI + note_juridique. Output `wedge-tool/static/data/legal_regime_check.json`. Run-422 : 26 confirmed + 5 pending (grappe Grenoble) + 1 non-encadré.

## Anti-patterns à éviter

- ❌ Flag + escalade Florian quand doute est re-occurring + automatisable (gaspille temps Florian)
- ❌ Build tool one-off pour la page courante uniquement, sans backfill toutes pages concernées (manque 90% de la valeur)
- ❌ Build tool sans sources `.gouv.fr` (Wikipedia seule = E-E-A-T insuffisant)
- ❌ Ship correction sans disclaimer visible quand `confidence_score < 0.8` (perte de confiance utilisateur si revendication trop forte)
- ❌ Re-build from scratch un seed déjà créé par Florian (= ignore son travail, mauvaise hiérarchie). Étendre, pas remplacer.

## Métrique à tracker

- `fact_check_tools_built_autonomously_lifetime` (cible : chaque pattern de doute récurrent doit produire un tool)
- `pages_pending_correction` (delta entre détection et backfill correction visible)
- `pages_legal_verified` (cumul pages cross-référencées par tool)

## Lien hiérarchique avec autres règles

- Précède la règle "≥4 sections data locale unique" : section #2 *Statut légal local exact* doit être basée sur `legal_regime_check.json` (pas affirmation libre).
- Précède la règle "anti-orphan" : pas de ship NEW programmatique sans `python3 check_legal_regime.py --ville <slug>` validé `confidence_score ≥ 0.6`.
- Compatible Indexing API : page corrigée = `URL_UPDATED` ping recommandé même wake (anti-stale dans index Google).
