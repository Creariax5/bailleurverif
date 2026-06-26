# Decision — Thin DPE city-page pruning (301 → hub) — P0-3 brief Florian 2026-06-26

**Run** : run-672 (2026-06-26T~15:50Z) · **Brief** : Florian 06-26T08:00Z action P0-3 ★★ · **Status** : SHIPPED + verified live.

## Contexte
Brief GSC indexation : 177 pages « Détectée non-indexée » (1.1 % indexé). Hypothèse #3 = pages programmatiques templates similaires perçues thin → Google déduplique avant crawl. P0-3 = auditer les 50 DPE-ville templates, garder celles à data unique, 301-rediriger les thin vers hub.

## Audit empirique (déterministe, `agent-browser/audit_thin_dpe.py`)
50 pages `<ville>-dpe-f-g-interdit-location.html`. Mesure de contenu unique = nombre de `<td>` (table calendrier partagée = **15 cellules byte-identiques** sur 47 pages = baseline).

- Diff direct metz vs caen : identiques sauf nom ville + département + **estimation F+G formulaire** (même base 65 000 résidences × ratio 16-18 % « ajusté » — PAS de la vraie donnée observatoire ; présentée en `Dataset` JSON-LD licence Etalab = léger risque intégrité en plus du thin).
- **3 pages seulement** ont une table data unique (>15 td) : **Paris (95), Toulouse (36), Nantes (33)**.
- 47 autres = template pur (15 td baseline + estimation formulaire).

## Écart vs brief (surface honnête, pas d'escalade)
Le brief estimait 10-15 pages à data unique et nommait Paris/**Lyon/Lille/Bordeaux** comme ayant des tables per-arrondissement. **Empiriquement faux** : Lyon/Lille/Bordeaux DPE = baseline 15 td (templates), seul Paris a une vraie table ; Toulouse/Nantes (non cités) en ont une aussi. La vraie séparation est 3 unique / 47 template, pas 10-15 / 35-40.

## Décision (KEEP 6 / PRUNE 44)
- **KEEP (200)** : Paris, Toulouse, Nantes (table unique) **+ Lyon, Lille, Bordeaux** (keep-list explicite Florian honorée malgré templating = marge de sécurité low-risk, respect instruction).
- **PRUNE → 301 `/calendrier-interdiction-dpe-2025-2028-2034.html`** : 44 templates (hub le plus topique pour « DPE F/G interdit location »).

## Réversibilité (garde-fou brief : rollback si delta T+14j négatif)
- **Fichiers HTML NON supprimés** — restent sur disque. Le 301 est servi via map `wedge-tool/redirects-301.json` chargée au boot par server.py. Retirer une entrée = un-redirige la page. Rollback = vider/restaurer le JSON + restart.
- Régénération idempotente : `python3 agent-browser/audit_thin_dpe.py`.
- Sitemap segmenté (P0-1) conserve volontairement les 44 URLs court-terme (aide Google à crawler → découvrir le 301). Retrait sitemap = follow-up post-confirmation re-crawl (~2-4 sem).

## Mécanique server.py
`REDIRECTS_301` (dict chargé de `redirects-301.json`) + check 301 dans `do_GET` juste après le bloc `/index.html`. Symétrie avec le 301 existant index.html→/.

## Smoke (8/8 PASS)
- 5 pruned (metz/marseille/strasbourg/villeurbanne/saint-denis) → 301 + Location calendrier (interne :8102 ET prod https).
- 6 kept (paris/lyon/lille/bordeaux/toulouse/nantes) → 200.
- Hub calendrier → 200.

## Mesure (brief T+14j, deadline 2026-07-10)
`gsc_detected_not_indexed` 177 → cible 130-150 (-15-25 %) ; `gsc_indexed_pages` 2 → 30-50. Si delta négatif → rollback redirects (procédure ci-dessus).
