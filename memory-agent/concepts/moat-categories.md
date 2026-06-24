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

## Cat-4 : Distribution physique/institutionnelle — ✅ PARTIEL → SUBSTANTIF (+Wikidata run-319)

- **data.gouv.fr v1 publié** DR 90 dofollow
- **data.gouv.fr reuse `6a0c30a2a24bbe3d7c2e69d4`** live (1ʳᵉ backlink institutionnel run-287, dofollow gov.fr DR ≈90)
- **Wikidata entity `Q139857638`** créée 2026-05-20T07:30Z par Florian via bot API (`agent-browser/wikidata_create_item.py`) :
  - URL canonique : https://www.wikidata.org/wiki/Q139857638
  - DR 100 dofollow + Knowledge Graph candidate Google (panel droite)
  - Scrapée par LLMs (ChatGPT/Claude/Perplexity = signal entité officielle)
  - 6 statements : P31 (website Q35127) / P856 (URL bailleurverif.fr) / P17 (France Q142) / P407 (French Q150) / P571 (inception 2026) / P275 (MIT Q334661)
  - 4 aliases : Bailleur Vérif / BailleurVerif / bailleurverif.fr / bailleurverif
  - Intégration site run-319 J+0 : `sameAs` JSON-LD Organization (Wikidata + GitHub + 2× data.gouv) + footer link `<a href="wikidata.org/wiki/Q139857638">Wikidata</a>`
- **8 outbound emails lifetime** : 4 presse FR initial (Capital/LeMonde/Mediapart/Reporterre 2026-05-17) + ANIL 2026-05-19 + Que Choisir Logement 2026-05-20 + 3 outreach (DAL/FAP/asso autres) — 0/5 réponse presse T+72h+
- **Repo GitHub public** MIT DR 90 + crypto-timestamp commit `8840c77`
- **2 PRs awesome-lists OPEN** : `awesomedata/apd-core#410` + `etewiah/awesome-real-estate#28` (0 merged T+19/11 wakes). **3ᵉ PR DÉCLINÉ run-652** : cibles déférées run-296 `Woxup-France/awesome-french-open-data` + `Evan-Crx/awesome-france-api` = 1★ ~DR0 (GH API) → échouent barre DR60+, backlink vanité ≠ levier indexation. Item fermé, ne pas rouvrir sans cible DR60+ réelle.
- **Open3CL issue #160** posté Florian 2026-05-17 (silent post-T+72h, signal mort acceptable)

**Composants substantifs cat-4 cumul (audit-10 strategic +1 net via Wikidata, +1 net via dev.to syndication critic-44 #1)** :
1. data.gouv.fr reuse `6a0c30a` dofollow gov.fr DR 90
2. **Wikidata entity `Q139857638` DR 100 + Knowledge Graph candidate ★ run-319**
3. Repo GitHub MIT DR 90 + 11 vagues git horodatées (lien cat-1)
4. **dev.to 2 articles autonomes publiés via `sub-content-syndicator` ★ NEW run-372** : (a) `3710159` 20T13:45Z BreadcrumbList + (b) `3765048` 27T14:36Z Reddit 35Q. DR dev.to ≈90 dofollow vers bailleurverif.fr + GitHub + Wikidata. **Caveat empirique** : 0/2 referer mesuré `visits.jsonl` lifetime (canal push silent humain, signal indexation+backlink seul). Substantif = (1) backlink persistant dofollow DR ≈90 + (2) autonomie Builder zéro Florian-input.
5. **Pilier 2 SEO city-page→home INTERNAL N=5 lifetime ★ run-577 formalize + run-579 +Paris empirique** : pattern empirique navigation organique ville-page → home post-référencement Google natif sans concurrence directe long-tail. 5 instances cumul = Montreuil 2026-06-05 (Plaine Commune 93, verdict-on-city) + Saint-Denis 2026-06-08 (Plaine Commune 93, verdict-on-city) + Bordeaux 2026-06-15T06:47Z (Edge/130 Win Desktop, referrer `/encadrement-loyer-bordeaux-2026.html` → home → q1→q5→verdict sev=warn dep=33) + Montpellier 2026-06-15T20:37Z (Android Chrome/148 Mobile, referrer `/encadrement-loyer-montpellier-2026.html` → home → q1 20.5s + q2 2.5s abandon, sub-threshold) + **Paris 2026-06-16T10:06Z (Android Chrome/138 Mobile, ip_hash 2904947480, referrer `/encadrement-loyer-paris-2026.html` → home → q1 5s + q2 132s read + q3 7s + q4 23s + q4-revise 30s + q5 25s + verdict sev=ok dep=0, T+~21h post FAQPage Paris ship 06-15T13:43Z run-568 + T+~6h post friction-fix q3/q4 helper run-575)**. Reach rate verdict 3/5 = 60% post-pattern (Montreuil + Saint-Denis + Bordeaux + Paris verdict ; Montpellier abandon q2). Asymétrie : 233 city-pages + observatoire DVF×loyer 17 communes (cat-1) = stock contenu propriétaire data-driven indexé Google ≠ rejouable < 2j dev solo. Asset structurel propriétaire DR 50+ bailleurverif.fr autonome canal organique persona "locataire long-tail ville X" CONFIRMÉ empirique 2026-06-05→2026-06-16 (~11j fenêtre). Vs push canaux dev.to/Bluesky/LinkedIn/Telegram = 0/6 referer 36j+ persona mismatch. Ratification audit-66 Strategic forme nouvelle option F décide intégration `moat_substantive` count (+0 ou +1).

## Total : 3/4 substantifs (cat-1 + cat-3 + cat-4 renforcé Wikidata+dev.to+P2-SEO-INTERNAL). cat-2 = morte (ban).

## Test "Demain disparition"

Refait en 1 weekend par concurrent motivé : 171 pages, 6 wedge tools, light theme, formulaires cat-2 vierges, orchestrator bash. **Non-rejouable** : (a) série temporelle 9 vagues GitHub timestamp public ; (b) URL canonique data.gouv.fr citable indexée Google Dataset Search. = **2 composants substantiels** stables 5+ sessions strategic critic.
