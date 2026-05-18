# Décision : Pivot Moat-builder (DIRECTIVE 9)

**Date** : 2026-05-17T08:05Z (HUMAN_DIRECTIVE.md)
**Status** : ACTIVE (jusqu'à `moat_components_live ≥ 3` substantiels)

## Décision verbatim Florian

> "j'ai dit qu'il fallait jamais se bloquer" (2026-05-17T07:55Z, en réaction au constat que les 37 wakes nuit n'avaient produit que des features copyables).

DIRECTIVE 9 codifie :
1. **Copyability check obligatoire** avant 1 ligne de code feature : *"dev solo refait <2j ?"*
2. **Au moins 1 wake/4 sessions sur composant moat-builder**
3. **4 catégories moat** à cycler activement (cat-1 données / cat-2 réseau / cat-3 RAG-LLM / cat-4 distribution)
4. **Self-policy "0 signup automatisé"** ne s'applique qu'aux signups nominatifs PAS au scraping anonyme
5. **Anti-blocage** : TODO bloqué humain → list 1 fois → pivot voie alternative → pas ré-évoquer 24h+
6. **Polish loop critic-flag** → pivot IMMÉDIAT obligatoire vers moat-builder

## KPIs introduits

- `copyability_score` (cible décroissante)
- `moat_components_live` (cible ≥3 sous 14j depuis run-176)
- `auto_blocks_dropped_lifetime` (cible croissante)
- `scraping_continuous_data_rows_lifetime` (cible croissante)

## Anti-patterns

- ❌ "TODO-21 SMTP bloqué humain donc 4 outreach drafts polish en attendant"
- ❌ "Ce wake j'ajoute encore une page hub / un outil grand public déjà couvert"
- ❌ "Cette feature est copyable 5 min mais utile" → utile oui, moat non, ne remplace PAS wake moat-builder
- ✅ "Ce wake je scrape 100 annonces LeBonCoin Paris, je match conformité, publie stat"
- ✅ "Ce wake je drafte pipeline fine-tuning LLM jurisprudence bail FR"

## État application (run-258 2026-05-18T11:29Z)

- `moat_components_live=2/4 substantifs` (strategic critic last audit) — **toujours en retard de 1**
- `copyability_score=88%` (4 dernières sessions, en hausse vs 92% audit précédent — pas d'amélioration)
- `auto_blocks_dropped_lifetime` croissant (scraping Locservice continu, helper JSON-LD wired, cat-3 inline)
- `wakes_construction_consecutifs_moat=2`
