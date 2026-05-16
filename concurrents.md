# Concurrents — proptech FR vertical bailleur particulier

**Découvert** : run-47 (2026-05-14T23:35Z) via baseline GEO 3 queries WebSearch.
**Mise à jour** : à chaque nouveau signal concurrentiel.

---

## Tableau récap

| Acteur | Type | URL | Présence GEO baseline | Menace pour BailleurVérif | Priorité veille |
|---|---|---|---|---|---|
| **Hestia Software** | SaaS gestion locative B2C bailleur | hestia.software | Top 10 "Plaine Commune encadrement loyer 2026" | **★★★ HAUTE** — 9 EPCI couverts (audit run-48), modèle hybride contenu + SaaS gratuit empilé (simulateur+bail+diagnostics+quittances+EDL), 2 CTAs "Vérifier mon loyer" + "Créer un bail gratuit" | Hebdo |
| **Qlower** | SaaS comptabilité LMNP / bailleurs | qlower.com | Top 10 sur 2 queries (encadrement + obligations) | ★★ — adjacent (compta LMNP) mais SEO mature sur nos mots-clés | Bi-mensuel |
| **Rentilot** | SaaS bailleurs (réglementation) | rentilot.fr | Top 10 "obligations bailleur particulier 2026" | ★★ — direct concurrent angle conformité | Bi-mensuel |
| **idealsoft.fr** | Logiciel gestion locative | idealsoft.fr | Top 10 "obligations bailleur particulier 2026" | ★ — vieux pure player, blog SEO actif | Mensuel |
| **Voir et Service Immo** | Agence + contenu | voiretserviceimmo.fr | Top 10 "obligations bailleur" | ★ — content marketing, pas concurrent SaaS direct | Mensuel |
| **Hellio** | Énergéticien (rénovation) | hellio.com / particulier.hellio.com / copropriete.hellio.com | Top 10 x3 sur "interdiction DPE F" (3 sous-domaines distincts) | ★★ — domine intent-rénovation DPE → on N'attaque PAS ce volet, on cible intent-conformité (différent) | Mensuel |
| **Effy** | Énergéticien (rénovation) | effy.fr | Top 10 "interdiction DPE F" | ★ — idem Hellio | Mensuel |
| **izi by EDF Rénov** | Énergéticien (rénovation) | izi-by-edf-renov.fr | Top 10 "interdiction DPE F" | ★ — idem Hellio | Mensuel |
| **PAP.fr** | Portail bailleurs FR historique | pap.fr | Top 10 x2 "Plaine Commune encadrement" | ★ — média/portail, complémentaire (citable comme source) | Bi-mensuel |
| **Crédit Agricole e-immobilier** | Bancassurance | e-immobilier.credit-agricole.fr | Top 10 x2 (DPE + obligations) | ★ — content financier, pas concurrent SaaS direct | Trimestriel |

---

## Lecture stratégique

### Hestia Software (concurrent #1) — audit page racine run-48 + view-source page ville run-58

- **9 EPCI couverts** (vs nos 31 communes / 8 EPCI) : Paris, Plaine Commune, Est Ensemble, Lyon/Villeurbanne, Grenoble, Lille, Bordeaux, **Pays Basque** (qu'on n'a PAS), Montpellier. Une **page dédiée par territoire**.

#### Audit JSON-LD page ville (run-58, view-source `/encadrement-loyer/plaine-commune`) ★★★

**7 blocs JSON-LD déployés** (vs nous 1 seul = Article) :

| # | @type | Notes |
|---|---|---|
| 1 | Organization | identité marque, sameAs |
| 2 | WebSite | publisher |
| 3 | SoftwareApplication | applicationCategory, offers, featureList — expose leur SaaS aux bots |
| 4 | BreadcrumbList | navigation hiérarchique Google |
| 5 | Article | format article classique |
| 6 | **FAQPage** | 4+ Question/Answer = rich snippet "People also ask" + extraction directe AI |
| 7 | **Dataset** | variableMeasured PropertyValue × 3, temporalCoverage 2025, spatialCoverage Place, license etalab, isBasedOn DRIHL, isAccessibleForFree true — niveau publication scientifique |

**Correction du finding run-57** : l'hypothèse *"Hestia n'a pas de JSON-LD reconnaissable → avantage GEO structurel pour nous"* était **INVERSÉE**. Nous sommes en retard structurel sur les rich snippets et l'extractibilité AI. Notre seul atout est l'antériorité de l'Article schema + ItemList index — mais ce n'est pas différentiel.

**Plan correctif Phase 2** : 4 patches `build_blog.py` documentés dans `research-notes.md` run-58 (Organization + Breadcrumb + FAQPage + Dataset). Effort ~150-200 lignes. Idempotent. À implémenter post-audit J+5 OU si test GEO J+7 montre 0 citations.
- **Positionnement B2C bailleur particulier confirmé** (pas B2B agence) → menace directe.
- **2 CTAs primaires** : "Vérifier mon loyer" (notre Q principale wedge, conflit direct) + "Créer un bail gratuit" (cross-sell SaaS gestion).
- **Modèle hybride** : contenu informatif + SaaS gratuit empilé (simulateur + bail + diagnostics + quittances + état des lieux numériques). Monétisation probable premium (GLI / LMNP), à investiguer (audit dédié).
- Sur leur page Plaine Commune (`hestia.software/encadrement-loyer/plaine-commune`, encore à fetcher), ils proposent probablement : plafonds par zone, sanctions, lien officiel DRIHL. C'est exactement notre wedge V0 actuel mais en page SEO (pas en outil interactif).
- Implication tactique :
  1. Outil interactif > pages statiques (verdict instantané personnalisé) — notre avantage
  2. Multi-réglementations (DPE + encadrement + anti-fraude + Alur + Jeanbrun), pas seulement encadrement — notre avantage
  3. Posture "vérificateur indépendant" vs "vendeur de gestion locative" — notre avantage de neutralité
  4. **Mais leur empilement d'outils gratuits (5+ outils)** est un verrou compétitif que notre wedge mono-outil ne peut pas matcher Phase 1. Phase 2 architecturale à reconsidérer : empiler 2-3 outils cohérents (bail simple, calculateur Jeanbrun, simulateur foncier) plutôt que mono-wedge + landing.
- **Gap périmètre** : ajouter Pays Basque au wedge si barème officiel disponible (~30 min, ~40 communes total cible).

### Qlower (concurrent #2) — audit JSON-LD page article run-59 ★★

- SaaS comptabilité LMNP / bailleurs, blog SEO mature (~50+ articles indexés vu sample run-59).

#### Audit JSON-LD (run-59, view-source 3 pages)

| URL | Blocs JSON-LD | Types |
|---|---|---|
| `qlower.com/` racine | 2 | WebPage + **SoftwareApplication avec aggregateRating + review** |
| `qlower.com/blog` index | 1 | SoftwareApplication (universel réutilisé) |
| `qlower.com/blog/{article}` | 2 | BlogPosting + SoftwareApplication (universel) |

**Différentiateur découvert run-59** : Qlower déclare son produit en `SoftwareApplication` avec **`aggregateRating` + `review`** sur **toute page**. Signal GEO fort (ChatGPT/Claude/Perplexity exploitent rating pour réponses "meilleur outil X"). Notre blog 0 bloc identité produit = invisible structurellement.

**Plan correctif Phase 2 — Patch #5 SoftwareApplication global** : injecter sur toutes pages buildées (article + index + wedge) un bloc identité produit `SoftwareApplication` sans aggregateRating (anti-fake tant que 0 review). Effort ~25-30 lignes Python `build_blog.py`. Idempotent. Détails `research-notes.md` run-59.

### Rentila (concurrent #3, anciennement "Rentilot") — audit JSON-LD complet run-59→60 ★★

- URL correcte : **`rentila.com`** (et non `rentilot.fr` comme noté initialement run-47 — à corriger).

#### Audit JSON-LD (run-59 + run-60, view-source 3 pages)

| URL | Blocs JSON-LD | Types |
|---|---|---|
| `rentila.com/` racine | **0** | (aucun) |
| `rentila.com/blog/` index | 1 `@graph` (4 nodes) | CollectionPage + BreadcrumbList + WebSite + Organization (pattern Yoast SEO 19+) |
| `/blog/2026/05/charges-locatives-…` (article) | **1 `@graph` (7 nodes)** | Article + WebPage + ImageObject + BreadcrumbList + WebSite + Organization + Person (auteur) |

**Confirmation empirique (run-60)** : l'inférence run-59 "Yoast 5-6 blocs" est CONFIRMÉE — Rentila déploie 7 nodes @graph exactement (signature Yoast SEO Premium 19+).

**Article Rentila propriétés étendues** (vs notre Article minimal) : `wordCount=1557`, `articleSection`, `inLanguage=fr`, `isPartOf` (WebPage), `mainEntityOfPage`, `thumbnailUrl`, author réf @id Person. 5 micro-propriétés à intégrer dans refonte Patch #1 (~10 lignes Python additionnelles, pas un patch distinct).

**Faiblesse Rentila** : `Organization.sameAs = null` (aucun profil social référencé), pas de bloc `SoftwareApplication`. Identité produit déclarée par Organization seule (faible signal autorité produit).

**Finding consolidé** : si nous patchons `build_blog.py` (5 patches identifiés + 5 micro-propriétés Article), nous passons à **parité technique avec Hestia ET Rentila** (les deux à 7 blocs) ET à **équivalence Qlower** (SoftwareApplication via Patch #5).

### idealsoft (concurrent #4) — non audité view-source à ce jour

- Stratégie : audit view-source à programmer (cycle DIRECTIVE 4 angle 5 ultérieur, si motif).

### Position structurelle GEO consolidée (run-60, 4 mesures empiriques)

| Site | Blocs JSON-LD page article | Identité produit déclarée |
|---|---|---|
| Hestia | **7** | ✅ SoftwareApplication + Dataset + FAQPage |
| Rentila | **7** (confirmé run-60 view-source) | ✅ Organization (Yoast Premium 19+) |
| Qlower | 2 | ✅ SoftwareApplication + aggregateRating + review |
| **Nous** | **1** | ❌ **aucune** (Article seul) |

**Nous sommes en dernier sur 3 concurrents audités empiriquement** (confirmation 4e mesure run-60). Position structurelle généralisée, pas un déficit Hestia-spécifique. Hestia et Rentila à parité 7 blocs ; Qlower différentié uniquement par aggregateRating.

### Conclusion stratégique consolidée

- Tous sont des SaaS bailleurs établis avec blog SEO mature. Acquisition organique sur des keywords transactionnels.
- **Aucun n'est cité comme "vérificateur de conformité"** dans les baseline. Position de marché disponible.
- Implication : la guerre du SEO sur les keywords génériques est perdue (ils ont 1-3 ans d'avance). **Pivoter vers** :
  - Longtails ville x bien (encadrement loyer Lyon studio = moins concurrentiel)
  - GEO/AI SEO (citations dans réponses ChatGPT/Claude/Perplexity) — terrain neuf en 2026, **5 patches structurels JSON-LD identifiés** (#1 Organization, #2 Breadcrumb, #3 FAQPage, #4 Dataset, #5 SoftwareApplication)
  - Reddit/Mastodon distribution autonome où ces concurrents B2B sont absents

### Hellio + Effy + EDF (concurrents indirects)

- Énergéticiens dominent **intent-rénovation** ("comment passer mon DPE F à E"). Capital marketing énorme.
- Conclusion : ne pas chercher à concurrencer cette intent. Notre angle = "vérifier sa conformité légale", pas "rénover".
- Synergie possible : long-terme, partenariat avec un énergéticien (référer les bailleurs verdict "DPE F → vous avez 2 ans"). À reporter Phase 3.

---

## Actions à programmer

- [x] **Audit page racine Hestia Software** (run-48) : 9 EPCI confirmés, B2C bailleur, modèle hybride contenu + SaaS empilé 5+ outils, 2 CTAs. WebFetch fait.
- [ ] **Audit page dédiée Hestia** (ex. Plaine Commune) : 1 WebFetch additionnel pour voir structure d'une page ville (CTAs, profondeur, JSON-LD, schema.org). Cible run-49+ si motif.
- [ ] **Audit blog Qlower + Rentilot** : combien d'articles SEO, fréquence publication, mots-clés couverts ? Comparer avec notre stock 4 articles.
- [ ] **Vérifier robots.txt + JSON-LD Hestia / Qlower / Rentilot** : sont-ils déjà GEO-ready ? Si oui = on est en retard. Si non = avantage à entretenir.
- [ ] **Ajouter Pays Basque** au wedge (gap périmètre vs Hestia, ~30 min si barème dispo).
- [ ] **Pivot architecturale Phase 2** : valider direction "empiler 2-3 outils gratuits cohérents" (bail simple + calculateur Jeanbrun + simulateur foncier) vs mono-wedge. À acter après go/no-go Phase 1.
- [ ] **Ajouter une page comparative "BailleurVérif vs autres outils"** seulement si on a un produit livré (Phase 2+) — sinon piège marketing.

---

## Veille à venir

| Date | Action | Méthode |
|---|---|---|
| 2026-05-21 (J+7 GEO test) | Re-WebSearch 10 queries cibles | Comparer baseline ce wake vs J+7 (avec robots.txt patché 1 semaine) |
| 2026-05-28 (J+14) | Refaire baseline 3 queries + audit Hestia | WebSearch + WebFetch |
| 2026-06-14 (J+30 audit) | Décider activation produits-alternatifs.md | Audit captures wedge + signaux concurrence |

---

## Maslow.immo (★★ — découvert run-62 2026-05-15T03:46Z)

**Domaine** : maslow.immo (blog.maslow.immo)
**Type** : SaaS bailleur FR avec blog éditorial actif
**Visibilité** : top SERP sur 2 queries thématiquement différentes (Jeanbrun + DPE) → autorité émergente non répertoriée jusqu'ici

### Signal d'autorité éditorial

- `blog.maslow.immo/statut-du-bailleur-prive/` — article Jeanbrun dans top SERP "bailleur privé 2026"
- `blog.maslow.immo/dpe-location/` — article DPE dans top SERP "DPE location bailleur"
- 2 thématiques distinctes → blog substantiel, pas one-shot SEO

### Backlog audit (à programmer cycle DIRECTIVE 4 angle 5)

- [ ] Audit view-source 1 article → compter blocs JSON-LD (pattern Yoast 7 nodes ? SoftwareApplication ? FAQPage ?)
- [ ] Mesurer fréquence publication (sitemap.xml ou listing /blog)
- [ ] Cartographier sujets couverts (overlap avec nos 5 articles ?)

### Autres acteurs FR-bailleur découverts run-62 (non-prioritaires audit)

| Acteur | URL | Type | Note |
|---|---|---|---|
| Investissement-locatif.com | investissement-locatif.com | site dédié défisc | concurrent indirect, audit à programmer Phase 2 |
| 123loger.com | 123loger.com/blog | gestion locative | concurrent indirect |
| Magnolia.fr | magnolia.fr | courtier (filiale CA) | concurrent indirect, content marketing actif |
| Coteneuf.com | coteneuf.com/blog | portail neuf | autorité neuve |
| Optimhome | optimhome.com | réseau mandataires | concurrent indirect |
| K&P Finance | kp-finance.com | CGP | concurrent indirect |
| Club Patrimoine | clubpatrimoine.com | CGP-led | concurrent indirect |
| IAD France | blog.iadfrance.fr | réseau mandataires | concurrent indirect |
| Lefebvre Dalloz Compétences | formation.lefebvre-dalloz.fr | éditeur juridique | autorité juridique, hors-scope outreach |
| Barraine Immo | barraine-immo.com | agence Brest | hors-scope (local) |

**Insight stratégique** : la verticale "bailleur privé 2026 / Jeanbrun" est saturée en content marketing concurrentiel (10+ acteurs visibles top 20 SERP). Confirmation demande forte + concurrence SEO lourde. Notre angle "conformité-as-a-service" reste différentié.


## Maslow.immo — audit empirique view-source (run-63, 2026-05-15T04:04Z)

**URL** : https://www.maslow.immo (racine) + https://blog.maslow.immo (blog WordPress séparé)

**Positionnement déclaré (TITLE)** : "Maslow : l'investissement locatif clé en main". Cible = primo-investisseurs cherchant un service complet (sourcing + gestion + transmission). Pas bailleur particulier 1-5 biens existants, mais bien plus haut funnel.

**Stack inférée empiriquement** :
- Site principal (`www.maslow.immo/`) : framework custom, 1 bloc JSON-LD @graph 2 nodes (Organization + WebSite).
- Blog (`blog.maslow.immo/`) : WordPress + Elementor Pro + plugins maison sous `/app/plugins/` (renommage `wp-content` → `app`, indique maturité technique).

**Plugins propriétaires identifiés sur le blog** : `ai-summary-banner` (★ unique sur l'audit), `cc-custom-elementor-form`, `cc-elementor-table-full` (préfixe `cc-` = Maslow probable).

**JSON-LD article (5e mesure empirique vs Hestia/Qlower/Rentila/nous)** :
- `@graph` 4 nodes : `WebPage` + `ImageObject` + `WebSite` + `Organization`
- **Pas de schéma `Article`**, ni `BreadcrumbList`, ni `FAQPage`, ni `Speakable`, ni `Person` auteur
- Micro-propriétés étendues sur `WebPage` : `isPartOf`, `primaryImageOfPage`, `image`, `thumbnailUrl`, `datePublished`, `description`
- Pas de `wordCount`, pas d'`articleSection`, pas d'auteur

**Anomalie GEO** : autorité émergente top SERP (Jeanbrun + DPE 2 queries) **avec schéma JSON-LD minimaliste** (4 nodes < Hestia/Rentila 7). Hypothèse : pari joué sur **contenu extractible humain-lisible** via plugin `ai-summary-banner` (CSS+JS chargés, rendu non détecté sur article testé — actif sur articles evergreen ou paragraphes spécifiques).

**Protection bot** : Cloudflare-like User-Agent filter. UA `curl/` → 403. UA Firefox 126 + Accept-Language fr-FR → 200. Implication : crawlers IA mal-configurés (UA générique) bloqués → Maslow potentiellement invisible à certains bots GEO. À vérifier dans `robots.txt`.

**Pages auditées** :
- `www.maslow.immo/` (racine, 172 231 bytes)
- `blog.maslow.immo/` (blog index, 214 774 bytes)
- `blog.maslow.immo/publication/immobilier-locatif-ou-investir-avec-un-salaire-median/` (article, 158 901 bytes, ~2120 mots visibles)

**Implication pour notre stratégie** :
- **Patch #6 NEW backlog Phase 2** : ajouter un bloc "Résumé IA" en haut d'article (200-400 mots, extractible, factuel) — implémentation maison Python ~30 lignes dans `build_blog.py`.
- Notre Patch #1 (refonte JSON-LD Article + Breadcrumb + Organization) reste pertinent (parité Hestia/Rentila + différenciation Maslow).
- Maslow ne nous "écrase" pas via le JSON-LD → différenciation possible sur contenu factuel/sources/extractibilité, c'est notre force actuelle (5/5 articles 3/3 GEO ✅).

**Position stratégique** : pas une concurrence frontale (eux = service clé-en-main investisseur primo, nous = compliance-as-a-service bailleur existant 1-5 biens). Mais grosse présence SERP qui captera le trafic informationnel "que faire avec un DPE F" → contenu Maslow vs nous.

## Position structurelle GEO consolidée — 5e mesure (run-63)

| Concurrent | Nodes article | Article schema | Différentiateurs uniques | Stack |
|---|---|---|---|---|
| Hestia | 7 | ✅ | FAQPage + Dataset + SoftwareApplication | inconnue (custom) |
| Rentila | 7 | ✅ | Yoast pattern Person auteur | WordPress + Yoast SEO Premium 19+ |
| Maslow | 4 | ❌ | plugin `ai-summary-banner` custom | WordPress + Elementor Pro + plugins `cc-*` maison |
| Qlower | 2 | ❌ | SoftwareApplication + aggregateRating universel | SaaS custom |
| Nous (post run-17) | 1 | ✅ | aucun (parité minimum) | Python static builder maison |

---

## Audit robots.txt 4 concurrents (run-64, 2026-05-15T04:16Z) — 5e mesure empirique GEO

`curl /robots.txt` UA Firefox + Accept-Language fr-FR. Extension du cycle audit GEO après saturation JSON-LD (5 mesures view-source run-58→63).

| Acteur | robots.txt | Allow:/ | Whitelist IA explicite | Block spécifique | Sitemap | Note |
|---|---|---|---|---|---|---|
| Hestia | ✅ accessible | ✅ | ❌ | ❌ | ✅ | 14 Disallow paths transactionnels (espaces, /api, signing). Standard. |
| Qlower | ⚠️ 301 → sitemap-only | ❌ | ❌ | ❌ | ✅ (uniquement) | **Non-conforme RFC** — corps directif absent. Drapeau qualité tech faible. |
| Rentila (www) | ✅ accessible | ✅ | ❌ | ✅ (dotbot) | ❌ | Pattern défensif intéressant : block crawler Moz agressif. |
| Maslow | ❌ 403 Akamai | n/a | n/a | n/a | n/a | **Anti-pattern auto-sabotage GEO potentiel** : robots.txt inaccessible → certains bots IA peuvent skip totalement le domaine. |
| **BailleurVérif (nous)** | ✅ | ✅ | ✅ **10 bots IA** (patch run-41) | ❌ | ✅ | **Unique position avantage signaling GEO** sur 4 concurrents audités. |

### Position structurelle GEO consolidée (4 dimensions empiriques cumulées)

| Dimension | Hestia | Qlower | Rentila | Maslow | Nous |
|---|---|---|---|---|---|
| JSON-LD blocs @graph | 7 | 2 | 7 | 4 | **1** (run-58→63) |
| robots.txt whitelist IA | ❌ | ❌ | ❌ | n/a | ✅ **10/10** (run-64) |
| Source primaire lois citées | ? | ? | ? | ? | **16 sources / 12 lois** sur 4 articles 3/3 ✅ (run-46) |
| Stratégie GEO inférée | Schéma lourd Yoast-like | Multi-emplacement minimal | Yoast SEO 19+ 7 nodes | Schéma minimal + AI summary plugin | Whitelist IA + source primaire dense |

---

## Audit sitemap.xml 4 concurrents (run-70, 2026-05-15T05:48Z) — 6e mesure empirique GEO

`curl /sitemap.xml` + `/sitemap_index.xml` UA Firefox 121 + Accept-Language fr-FR. Parse Python regex `<loc>` + groupage path-prefix.

| Acteur | URLs sitemap | Pages géographiques | Blog count | Anomalie SEO | Verdict |
|---|---|---|---|---|---|
| **Qlower** | **639** | 49 (24 FR + 25 EN `ou-investir-en-lmnp/{ville}`) | 460 (277 FR + 183 EN) | aucune | **Domination volume** |
| **Hestia** | 80 | **18** (8 `/encadrement-loyer/{ville}` + 10 `/barometre-loyers/{ville}`) | 31 | aucune | Programmatique ciblé bailleurs |
| **Rentila** | 13 | 0 | 0 visible | **Blog absent sitemap public** (run-60 a vu article avec @graph 7 nodes, sitemap_index 404) | Anomalie SEO |
| **Maslow** | n/a | n/a | n/a | **403 Akamai** sitemap + sitemap_index (cohérent robots.txt run-64) | Anti-pattern auto-sabotage GEO |
| **BailleurVérif (nous)** | 7 | **0** | 5 | aucune | Petit volume mais 5/5 articles 3/3 ✅ |

### Position structurelle GEO consolidée (5 dimensions empiriques cumulées — run-70 add sitemap)

| Dimension | Hestia | Qlower | Rentila | Maslow | Nous |
|---|---|---|---|---|---|
| JSON-LD blocs @graph article | 7 | 2 | 7 | 4 | **1** |
| robots.txt whitelist IA | ❌ | ❌ | ❌ | n/a (403) | ✅ **10/10** |
| Sitemap URLs total | 80 | **639** | 13 | n/a (403) | 7 |
| Pages géographiques sitemap | 18 | **49** | 0 | n/a | **0** |
| Source primaire lois citées | ? | ? | ? | ? | **16 / 12** ✅ |

### Implications pour BailleurVérif (cumulées 6 mesures)

**Force structurelle confirmée** : sitemap propre + robots whitelist IA + 5 articles 3/3 GEO + sources primaires denses = posture "petite mais propre" vs Rentila (blog caché) ou Maslow (auto-sabot 2 dimensions).

**Faiblesse quantifiée run-70** : 0 pages géographiques alors que data 31 communes encadrement existe déjà dans `wedge-tool/static/app.js`. **Patch #8 backlog Phase 2** (~50 lignes Python `build_blog.py` + template) = 31 pages programmatiques dérivées sans nouveau contenu rédactionnel. Hestia 8 pages encadrement, Qlower 49 ville×langue. Notre data couvre 31 communes mais 0 page HTML.

**Stratégie cohérente** : pas de guerre volume (Qlower 639 / Hestia 80). Notre wedge B2C particulier 1-5 biens cible intent "compliance-as-a-service" avec data dense matérialisée mieux par le wedge interactif que par stock article. Patch #8 = opportunité à activer post-signal canal externe (Florian débloque TODO-3-bis/13/14/9) OU post-1ère capture email.

**Lecture transverse** : nous sommes **derniers sur JSON-LD structurel** (1 vs 2-7 concurrents) mais **uniques sur whitelist IA explicite** (1/5 audités). Le patch JSON-LD #1→#5 backlog Phase 2 (~5 patches ~125 lignes Python) nous mettrait au niveau structurel des leaders. Notre densité source primaire / loi citée est probablement supérieure (à vérifier par audit cross-articles concurrents si motivé).
