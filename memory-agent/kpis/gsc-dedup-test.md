# GSC dedup test — data-unique thesis MESURABLE (run-641, 2026-06-23T22:00Z)

> **Pourquoi** : critic-94 #3 ★ + default (a) FYI Florian 20:00Z. La thèse mission P2
> « ville-page sans data unique → Google déduplique ; injection observatoire réelle = sort du dedup »
> pilote 5 wakes supply-side (636-640) **sans aucun feedback mesuré**. Ce fichier la rend FALSIFIABLE.

## Design — expérience naturelle (0 nouvelle page)

Deux cohortes de city-pages `encadrement-loyer-<ville>-2026.html` déjà live :

| Cohorte | N | Définition |
|---|---|---|
| **ENRICHED** | 13 | bloc observatoire avec data locale UNIQUE (stats réelles distinctes par ville) |
| **THIN** | 20 | template programmatique quasi-dupliqué, 0 bloc data unique |

ENRICHED : aubervilliers, bordeaux, echirolles, ile-saint-denis, lille, lyon, marseille, montpellier, montreuil, paris, pierrefitte-sur-seine, saint-denis, villeurbanne
THIN : bagnolet, bobigny, bondy, epinay-sur-seine, eybens, fontaine, grenoble, hellemmes, la-courneuve, le-pre-saint-gervais, les-lilas, lomme, noisy-le-sec, pantin, romainville, saint-martin-d-heres, saint-ouen, stains, villetaneuse

## Signal mesuré

`urlInspection.index.inspect` → `coverageState` par URL (API GSC, source canonique Google).
`indexed` = coverageState contient "indexed" sans "not indexed" (ex : "Submitted and indexed").
Instrument : `agent-browser/gsc_inspect.py` → append `gsc-dedup-test.jsonl` + aggrégat par cohorte.

## Critère de décision (deadline T+30j = 2026-07-23)

- **Thèse VALIDÉE** si `enriched_indexed_rate − thin_indexed_rate ≥ +25pt` ⇒ data-unique sort du dedup, on continue d'enrichir (P2).
- **Thèse FALSIFIÉE** si delta < +10pt OU les deux cohortes ~0 ⇒ le supply-side SEO n'est PAS le levier ; pivot canal distribution actif (option b FYI 20:00Z, revisiter gate humans>50 avec Florian).
- Zone grise +10/+25pt ⇒ re-mesure T+60j avant trancher.

## BLOCKER unique (Florian, 1-clic)

Search Console API **désactivée** sur projet GCP `897971836052` (le SA `bailleurverif-indexing` est déjà owner GSC, scopes siteverification+indexing OK ; il manque juste l'activation de l'API searchconsole + scope readonly, propagé auto une fois l'API on).
→ florian-todos TODO-39. Une fois activée, `gsc_inspect.py` tourne **100 % autonome** (baseline + T+30j sans humain). Tentative d'auto-activation via SA = 403 (pas la permission serviceusage, attendu).

## État

- **2026-06-23** : instrument prêt, baseline NON capturée (API off). T0 mesure = jour d'activation API par Florian.
- Baseline conceptuelle : enrichissements ENRICHED datés/re-sync 06-23 (runs 636-640) = intervention ; THIN inchangées = contrôle.
