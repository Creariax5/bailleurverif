---
name: Wikidata entity Q139857638 intégrée site
description: Brief Florian 07:35Z = item Wikidata Q139857638 créé via bot API, intégration site J+0 run-319 (sameAs + footer + moat-categories cat-4 +1)
type: project
---

# Decision : Wikidata entity Q139857638 intégrée — cat-4 distribution institutionnelle +1 substantif net

**Date** : 2026-05-20T08:30Z (run-319 J+0, ack brief Florian 07:35Z T+55min)
**Type** : Action — intégration entité institutionnelle dans site + memory agent

## Contexte

Florian a créé l'item Wikidata `Q139857638` ce wake (~07:30Z) via API bot password (`agent-browser/wikidata_create_item.py` one-shot). Action 100 % Florian-charge (zéro charge agent). Item public : https://www.wikidata.org/wiki/Q139857638

**Métadonnées item** :
- Label FR : `BailleurVérif`
- Description FR : `outil web français d'analyse de conformité des annonces de location`
- 4 aliases : Bailleur Vérif / BailleurVerif / bailleurverif.fr / bailleurverif
- 6 statements : P31 (website Q35127) / P856 (URL bailleurverif.fr) / P17 (France Q142) / P407 (French Q150) / P571 (inception 2026) / P275 (MIT Q334661)

**Asymétrie cat-4 distribution institutionnelle** :
- DR 100 dofollow Wikidata.org (autorité maximale)
- Source du Knowledge Graph Google = candidat panel droite Google search
- Scrapée par LLMs (ChatGPT/Claude/Perplexity) = signal entité officielle
- Persistante perpétuel (Wikidata ne supprime pas, juste tag deprecated possible)
- Pré-existe à concurrents — non-rejouable 1 weekend (création bot pass + 6 statements + Knowledge Graph candidate requiert notabilité)

## Actions exécutées run-319 (3/3 brief)

### Étape 1 — JSON-LD `sameAs` étendu (priorité)

Fichier : `wedge-tool/static/index.html` L74

Avant :
```json
"sameAs": ["https://github.com/Creariax5/bailleurverif"]
```

Après :
```json
"sameAs": [
  "https://www.wikidata.org/wiki/Q139857638",
  "https://github.com/Creariax5/bailleurverif",
  "https://www.data.gouv.fr/datasets/annonces-de-location-francaises-non-conformes-observatoire-bailleurverif",
  "https://www.data.gouv.fr/reuses/bailleurverif-observatoire-annonces-loyer-non-conformes-encadrement-dpe-f-g/"
]
```

**Why 4 URLs cumulées NOT juste Wikidata** : `sameAs` est consulté par Google Knowledge Graph pour cross-référencer entité. Plus d'URLs canoniques = signal entité officielle renforcé. Les 2 data.gouv URLs étaient absentes du JSON-LD jusqu'ici (présentes uniquement comme texte dans page).

### Étape 2 — Footer link Wikidata + GitHub visible

Fichier : `wedge-tool/static/index.html` L680-687

Ajout dans `<nav class="flex flex-wrap gap-x-4 gap-y-1 text-xs">` (footer nav) :
```html
<a href="https://www.wikidata.org/wiki/Q139857638" rel="noopener" title="BailleurVérif sur Wikidata">Wikidata</a>
<a href="https://github.com/Creariax5/bailleurverif" rel="noopener" title="Code source MIT">GitHub</a>
```

**Why GitHub aussi visible** : Le lien GitHub était `hidden` dans h-card (microformat invisible). Le rendre visible améliore signal dofollow + cohérence narrative (Wikidata + GitHub = 2 backlinks haute autorité côte-à-côte = transparence open-source/data).

### Étape 3 — `concepts/moat-categories.md` cat-4 update

Cat-4 réécrit avec section dédiée Wikidata + nouvelle ligne "Composants substantifs cat-4 cumul" :
1. data.gouv.fr reuse `6a0c30a` dofollow gov.fr DR 90
2. **Wikidata entity `Q139857638` DR 100 + Knowledge Graph candidate ★ NEW run-319**
3. Repo GitHub MIT DR 90 + 11 vagues git horodatées

**Total ligne mise à jour** : `Total : 3/4 substantifs (cat-1 + cat-3 + cat-4 renforcé Wikidata). cat-2 = morte (ban).` (avant : 2/4 substantifs cat-1 + cat-4 partiel).

### Étape 4 (non-faite) — pas de Wikipedia article ni `.env` touch

Florian explicite : « Pas de spawn sous-agent dédié. Pas de touche aux credentials .env WIKIDATA_BOT_* (Florian va probablement les révoquer post-intégration, c'est OK — l'item est créé définitivement). »

## Implications audit-10 strategic critic

**Audit-10 verdict (2026-05-20T03:53Z)** : `moat_components_live=3/4 substantifs UNCHANGED. +0 net vs audit-9. Stagnation 18 wakes consécutifs.`

**Post run-319** : `cat_4_substantif_count=2→3` (Wikidata ajouté). Si Knowledge Graph indexation Google cadence ~14j (typique) confirme propagation entité, audit-11 ~run-340 pourrait noter `moat_components_live=4/4 substantifs` (verdict "stagnation" cassée).

**Test "Demain disparition" renforcé** : Wikidata `Q139857638` = composant non-rejouable 1 weekend (pré-existence + statements P31/P275 = signal entité officielle).

## Smoke tests prod

```bash
$ curl -s https://bailleurverif.fr/ | grep wikidata
    "https://www.wikidata.org/wiki/Q139857638",
        <a href="https://www.wikidata.org/wiki/Q139857638" rel="noopener" title="BailleurVérif sur Wikidata">Wikidata</a>
```

= 2 hits ✅ (JSON-LD sameAs + footer link). 0 server restart nécessaire (HTML statique servi directement).

## KPIs delta

- `cat_4_substantif_count = 2 → 3` ★ NEW
- `moat_components_live = 3/4 → 3/4 UNCHANGED audit-10` mais `cat_4_substantif_count=3` interne
- `json_ld_sameas_urls_count = 1 → 4` ★ NEW KPI
- `footer_dofollow_external_links_count = 0 → 2` ★ NEW (Wikidata + GitHub désormais visibles)
- `wikidata_entity_qid = NA → Q139857638` ★ NEW KPI
- `memory_agent_decisions_count = 27 → 28`
- `wakes_total_lifetime = 318 → 319`
- `directive_7_revisee_compliance_consecutive_wakes = 98 → 99` trophy

## Anti-patterns évités

- Ne PAS spawn sous-agent dédié Wikidata maintenance (anti-spawn-bomb, item statique post-création).
- Ne PAS toucher `.env` ni `WIKIDATA_BOT_*` credentials (Florian va les révoquer probablement, hors-scope agent).
- Ne PAS créer Wikipedia FR/EN article (notabilité Wikipedia ≠ Wikidata, hors brief + risque flag-déletion notabilité insuffisante).
- Ne PAS toucher Paris page A/B (fenêtre 7j mesure ouverte deadline 2026-05-26T22:30Z).
- Ne PAS ré-IndexNow round (anti-théâtre, Googlebot WRS découvre liens internes naturellement run-318).

## Liens

- Wikidata item : https://www.wikidata.org/wiki/Q139857638
- Brief Florian 07:35Z : `inbox.md` HEAD
- Concept moat-categories cat-4 : `memory-agent/concepts/moat-categories.md`
- JSON-LD live : https://bailleurverif.fr/ (search `application/ld+json`)
- Footer live : https://bailleurverif.fr/ (search `Wikidata`)
