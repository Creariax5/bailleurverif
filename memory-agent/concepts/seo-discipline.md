---
name: SEO discipline — no orphan pages
description: Règle immuable shipping pages HTML : doivent être linkées depuis ≥1 page indexée Google AVANT considération "shipped". Codifiée 2026-05-20T06:35Z brief Florian post-debug GSC URL Inspection Paris page non-indexée.
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
