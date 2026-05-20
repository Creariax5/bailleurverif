---
name: Orphan fix + SEO discipline codified
description: Brief Florian 2026-05-20T06:35Z post-debug GSC URL Inspection (Paris page non-indexée car orpheline) HONORED run-318 J+0. 2 liens internes ajoutés homepage + obs + concept seo-discipline.md codifié + TODO-35 ★ Indexing API Google ajouté florian-todos.
type: decision
---

# Décision — Fix orphan pages + SEO discipline codified (run-318 2026-05-20T07:30Z)

## Contexte

Brief Florian 2026-05-20T06:35Z (4 minutes après mon wake run-317 06:31Z, lecture initiale spot-check head 3 lignes raté ce brief) : diagnostic empirique GSC URL Inspection sur `/loyer-legal-paris.html` = "Cette URL n'a pas été indexée par Google + Aucune page d'origine détectée + Aucun sitemap référent détecté".

Diagnostic empirique :
- ✅ Paris page DANS sitemap.xml
- ❌ Paris page PAS linkée homepage
- ❌ encadrement-loyer-paris-2026 PAS linkée homepage non plus
- ✅ Lille DPE page linkée homepage L542 → 1 visiteur organic 2026-05-20T05:18Z (preuve juice)

Verdict Florian : sandbox Google < 90j sites, sitemap.xml seul insuffisant, internal linking from indexed page = signal critique propagation.

## Décision honorée J+0

1. **Étape 1 fix homepage** : nouvelle section `#outils-paris` (`wedge-tool/static/index.html` après L344 `#outil-hub-encadrement`) avec 2 liens `<a>` vers `/loyer-legal-paris.html` + `/encadrement-loyer-paris-2026.html`. Smoke `curl https://bailleurverif.fr/ | grep` = 1 hit chacun live.
2. **Étape 2 fix observatoire** : nouvelle section `#voir-aussi` (`wedge-tool/static/observatoire-annonces-loyer.html` avant `</main>` L495) avec 4 liens `<li>` (paris-calc + paris-encadrement + france-hub + Lille DPE). Smoke 1 hit chacun live.
3. **Étape 3 codify** : `memory-agent/concepts/seo-discipline.md` créé 78 lignes (règle immuable + 3 sources-of-juice + workflow 5 steps + 5 anti-patterns + override/fallback + lien Googlebot WRS).
4. **Étape 4 sub-seo-monitor PATCH** : DIFFÉRÉ sur confirmation Florian explicite. Brief dit "optionnel". Cycle sub-seo-monitor 24h next ≥17:30Z. Si Florian confirme "patch step 4 yes" → PATCH prompt cycle suivant. Sinon naturel.
5. **TODO-35 ★ NEW** : `florian-todos.md` ajout Indexing API Google (faible priorité, optionnel, 15-20 min setup service account).
6. **MEMORY.md index L22** : ajout seo-discipline.md concept.

## Why empirique (preuve mesurée)

Page Lille DPE (linkée homepage L542) → 1 visiteur organic 2026-05-20T05:18Z = preuve juice transmis. Page Paris (orpheline) → 0 indexation GSC 9h+ post-ship + 0 visiteur. **Différence A/B observée**.

## Synergie avec Googlebot WRS run-318

Googlebot WRS Mobile-First Indexing rendant homepage avec JS confirmé 2026-05-20T06:40:00Z = Google découvre les NEW liens internes au prochain crawl WRS (24-48h cadence post-sandbox typique) = propagation rapide attendue 2026-05-22 ≈ T+48h sur les 4 pages stratégiques (Paris calc + Paris encadrement + observatoire + Lille déjà fait).

## Anti-pattern évité

- ❌ Differer brief Florian au run-319 (priorité #1 absolue verbatim)
- ❌ Touch Paris page A/B (mesure 7j ouverte deadline 2026-05-26T22:30Z préservée — fix linking est upstream pages parent, pas Paris page elle-même)
- ❌ IndexNow round-70 forcing crawl (laisse Googlebot WRS découvrir naturellement, anti-théâtre)
- ❌ Spawn sous-agent dédié monitoring orphans (cap 8 mais 4 actifs OK, sub-seo-monitor pattern existant suffit)

## Conséquences mesurables

- `orphan_pages_fixed_count = 0 → 2` (paris-calc + paris-encadrement)
- `seo_discipline_codified = true`
- `florian_todos_open = 6 → 7` (TODO-35 ★ ajouté)
- Re-check GSC URL Inspection 4 pages stratégiques due ≥2026-05-22 (cible T+48h propagation)
- Re-check captures Paris page T+10h next wake (cible 2026-05-20T08:30Z = futur next)
