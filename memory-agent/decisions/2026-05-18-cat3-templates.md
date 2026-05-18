# Décision : Cat-3 templates v0 (recours locataire)

**Date** : 2026-05-18T~05Z (run-243)
**Status** : 1/4 templates live, 3 candidats wake +N

## Décision

Shipper `loyer-abusif.v0.json` inline (sans Claude API externe) comme 1ʳᵉ amorce cat-3 intelligence interprétative. Anti-blocage DIRECTIVE 9 : Claude Code génère identique à un API call.

## Template v0 `loyer-abusif.json`

- Format JSON 15.4 KB
- Sourcé corpus Service-Public.fr + ANIL
- Structure : `{tag, title, sources, conditions, references_legales, jurisprudence_refs: [], generated_letter_template, contact_authority}`
- `jurisprudence_refs: []` = vide (bloqueur RAG Cassation/CA, pending ANTHROPIC_API_KEY TODO-26)

## Endpoint live

`/api/recourse/<tag>` GET (run-244)
- Sitemap.xml entry ajoutée
- CC-BY-4.0 licence (replicable mais antériorité timestampée)

## 3 templates candidats wake +N

1. `dpe-invalide.v0.json` (DPE F/G interdit 2025 + recours commission départementale)
2. `depot-non-rendu.v0.json` (caution dépôt restitué J+1 état des lieux conforme + recours)
3. `charges-injustifiees.v0.json` (charges récup non-conformes art. 23 loi 89-462 + recours)

## Pourquoi cat-3 amorce mais pas composant moat

- Templates inline = work-to-do copyable <1j par dev solo
- Vrai moat cat-3 = RAG jurisprudence vectorisé (Cassation+CA) + génération courrier case-by-case
- Stade actuel = squelette éditorial sourcé, pas intelligence interprétative

## Plan upgrade

Une fois TODO-26 ANTHROPIC_API_KEY .env :
- Pipeline batch scrape judilibre.fr (Cassation+CA bail FR ~5000 décisions)
- Embeddings + retrieval API Anthropic (Claude Haiku 4.5 cost-efficient)
- Génération courriers personnalisés par cas (pas par template)

## Files

- `wedge-tool/static/api/recourse/loyer-abusif.v0.json`
- `wedge-tool/server.py` endpoint
- `wedge-tool/static/sitemap.xml`
- `wedge-tool/static/llms.txt` mention recourse endpoints
