# Concept : Moat Categories (DIRECTIVE 9)

**État** : 2 catégories actives / 4. Cible DIRECTIVE 9 ≥3 sous 14j (J+1 = 2026-05-18, deadline ~2026-05-31). **En retard de 1.**

## Cat-1 : Données propriétaires accumulées — ✅ ACTIF

- **Observatoire N=232 annonces non-conformes** sur 17 communes scorées
- **9 vagues git horodatées** commit history publique (`cf51c00→075b344`)
- **Dataset data.gouv.fr v1** UUID `annonces-de-location-francaises-non-conformes-observatoire-bailleurverif`
- **Anti-fragilité** : helper `parse_detail_jsonld()` câblé dans `main()` `wedge-tool/crawler/locservice_v0.py` (run-257) → résiste refonte HTML Locservice future
- **Fragilité** : 6-9 mois si rythme tenu, <2 mois si pause >3 semaines
- **Cross-source** : page `/observatoire-prix-vente-vs-loyer.html` DVF×loyer 17 communes publiée run-251

## Cat-2 : Effets de réseau utilisateurs — ❌ INACTIF (2 surfaces vides)

- `/api/signalement` (run-196) : 1 record dormant paris-04, 0 nouveau en 60+ wakes
- `/api/notation-agence` (run-236) : 0 record
- **Diagnostic strategic critic run-236** : surfaces sans flux ≠ effet réseau
- **Prescription** : poster sur 1 canal humain réel (LinuxFr / Que-Choisir / fil X organique)
- **Self-policy bloque** : 0 signup nominatif sans Florian-validation = bloquant

## Cat-3 : Intelligence interprétative coûteuse — ⚠️ AMORCE

- **`loyer-abusif.v0.json`** template inline 15.4 KB JSON sourcé corpus SP.fr+ANIL (run-243)
- **Endpoint `/api/recourse/<tag>`** live + sitemap (run-244)
- **MAIS** : pas de LLM fine-tuné, pas de RAG jurisprudence Cassation/CA, `jurisprudence_refs: []` vide
- **Bloqueur** : ANTHROPIC_API_KEY .env TODO-26 silent T+~10h (pour batch jobs scrape→résumé→template + embeddings)
- **Templates additionnels** : `dpe-invalide` / `depot-non-rendu` / `charges-injustifiees` candidates wake +N

## Cat-4 : Distribution physique/institutionnelle — ✅ PARTIEL

- **data.gouv.fr v1 publié** DR 90 dofollow
- **7 outbound emails** : 4 presse FR (Capital/LeMonde/Mediapart/Reporterre 2026-05-17) + 3 outreach (DAL/FAP/asso autres)
- **Repo GitHub public** MIT DR 90 + crypto-timestamp commit `8840c77`
- **0 réponse presse à T+17h** (créneau lundi midi en cours)
- **Open3CL issue #160** posté Florian 2026-05-17T14:49Z + visiteur ~10:21Z 2026-05-18 = piste cat-4 potentielle (1 PR merged = composant)

## Total : 2/4 substantifs (cat-1 + cat-4 partiel). cat-2 + cat-3 = ouverture priorité.

## Test "Demain disparition"

Refait en 1 weekend par concurrent motivé : 171 pages, 6 wedge tools, light theme, formulaires cat-2 vierges, orchestrator bash. **Non-rejouable** : (a) série temporelle 9 vagues GitHub timestamp public ; (b) URL canonique data.gouv.fr citable indexée Google Dataset Search. = **2 composants substantiels** stables 5+ sessions strategic critic.
