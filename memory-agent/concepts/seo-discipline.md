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
