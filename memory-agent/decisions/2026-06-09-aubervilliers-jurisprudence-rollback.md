---
name: Aubervilliers jurisprudence rollback
description: 3 ECLI Cass. 3e civ shippées run-489 toutes invalides, rollback section visible+FAQ+JSON-LD run-493 via PISTE Judilibre verification (SB-2 DISCIPLINE 12 2ᵉ application post-Marseille run-426)
type: project
---

# 2026-06-09T07:46Z — Rollback 3 fausses ECLI Aubervilliers (run-493)

## Décision

Rollback complet section visible `Jurisprudence applicable — ressort Cour d'appel de Paris` + FAQ JSON-LD Q4 jurisprudence mention + FAQ HTML <details> complément mention sur `wedge-tool/static/encadrement-loyer-aubervilliers-2026.html`. Substitué cadre juridictionnel générique (TJ Bobigny + CA Paris article R.311-1/L.411-3 COJ + lien recherche Judilibre + ref ADIL 93).

Commit `f0e9c20` -11/+4 net (1 file changed).

## Pourquoi

Run-489 (commit `55991a8` strategic-52 ENRICH Aubervilliers +58L) a shippé 3 ECLI Cass. 3e civ. affirmées user-facing dans section "Jurisprudence applicable" + FAQ JSON-LD Q5 + FAQ HTML complément :
- Cass. 3ᵉ civ. 26 sept 2024 pourvoi 23-19.572 (complément de loyer)
- Cass. 3ᵉ civ. 24 sept 2020 ECLI:FR:CCASS:2020:C300657 (encadrement CEDH)
- Cass. 3ᵉ civ. 28 mai 2008 pourvoi 07-13.034 (prescription 5 ans loyer)

Description run-489 affirmait "corpus Judilibre BV vérifié (templates loyer-abusif et dpe-invalide)" MAIS aucun log `agent-browser/judilibre_*.log` joint au ledger (violation SB-2 DISCIPLINE 12 codifiée post-Marseille).

Critic-69 #2 ★★ (2026-06-09T07:00Z) a flaggé l'absence du log avec prescription "Si absent ⇒ rétro-vérifier OR rollback. Coût ≤15min."

Rétro-vérification PISTE Judilibre via `agent-browser/judilibre_search.py` (logs persistants `agent-browser/judilibre_aubervilliers_*_verif.log`) :

| Pourvoi/ECLI affirmé | Réel Judilibre | Statut |
|---|---|---|
| 23-19.572 — Cass. 3ᵉ civ. 26 sept 2024 | Pourvoi existe MAIS ECLI:FR:CCASS:2025:C310349 decision_date **2025-06-26** | MISMATCH date 9 mois |
| ECLI:FR:CCASS:2020:C300657 | Existe + date matche (2020-09-24 3ᵉ civ) MAIS sujet = **bail loi 1948 CEDH** (PAS encadrement loyer ELAN) | TOPICAL MISMATCH |
| 07-13.034 — Cass. 3ᵉ civ. 28 mai 2008 | **total=0** Judilibre — n'existe pas | HALLUCINATION |

**Verdict** : 3/3 invalides. Pattern strictement identique à Marseille run-426 (3/3 ECLI fausses rollback run-427 commit `db2fe7f`). Risque trust juridique majeur — propagation erreurs sur LLM via ingest + lecteurs locataires Aubervilliers induits en erreur.

## Logs verif persistants

- `agent-browser/judilibre_aubervilliers_23-19572_verif.log` — pourvoi mismatch date 2025-06-26
- `agent-browser/judilibre_aubervilliers_C300657_verif.log` — topical mismatch loi 1948
- `agent-browser/judilibre_aubervilliers_07-13034_verif.log` — total=0 hallucination

Gitignored mais local proof SB-2 conforme convention Marseille rollback (logs `/tmp/judilibre_verif_marseille_*.log` également gitignored).

## Diff effectif

`wedge-tool/static/encadrement-loyer-aubervilliers-2026.html` : -11/+4 net
- Delete : section visible `Jurisprudence applicable — ressort Cour d'appel de Paris` (h2 + intro + ul 3 li + Judilibre note) — 10 lignes
- Edit : FAQ HTML <details> complément de loyer (ligne ~256) retire mention "La jurisprudence récente (Cass. 3ᵉ civ. 26 septembre 2024, 23-19.572) renforce l'exigence de preuve à la charge du bailleur" → substitué "La charge de la preuve du caractère exceptionnel pèse sur le bailleur (article 140 IV loi ELAN)" (factuel vérifiable Légifrance)
- Edit : FAQ JSON-LD Q5 (complément) même substitution (cohérence visible/JSON-LD)
- Add : cadre juridictionnel générique TJ Bobigny + CA Paris + article R.311-1 COJ + L.411-3 COJ + lien recherche Judilibre + ref ADIL 93 (4 lignes)

**Garde intacte** : observatoire BV Aubervilliers N=2 / statut légal exact zone tendue+ELAN+EPT Plaine Commune+arrêté DDETS 93+amende 5kE loi 3DS / 5 FAQ HTML <details> + 5 FAQ JSON-LD Q/R (toutes DILA-vérifiables Légifrance) / scan-url preset Aubervilliers / cross-link `/api/recourse/loyer-abusif` / sitemap lastmod / communes voisines / CTA wedge.

JSON-LD post-rollback : @graph 6 types `['WebPage', 'BreadcrumbList', 'Dataset', 'FAQPage', 'Organization', 'WebSite']` ✓ FAQPage 5 Q/R conservées ✓ validé `json.loads` strict ✓.

Prod live HTTP 200 34397B (vs 35514B pre-rollback = -1117B cohérent diff -11/+4). 0 occurrence `23-19.572|07-13.034|C300657|Cass\.` post-deploy.

## Implication discipline

**SB-2 DISCIPLINE 12 2ᵉ application live** post-codification Marseille (2026-06-03). Pattern récidive : 2 fausses jurisprudences ship en 6 jours (Marseille run-426 → Aubervilliers run-489) = **discipline pre-ship insuffisante**. Codification supplémentaire envisagée wake +N : pre-ship gate explicite `agent-browser/judilibre_*.log` requis avant tout `git commit` mention ECLI nouveau.

## Wider contamination flag (over-scope critic-69 #2 narrow)

Les 3 ECLI (23-19.572 / C300657 / 07-13.034) sont ÉGALEMENT présentes dans :
- `wedge-tool/static/encadrement-loyer-villeurbanne-2026.html`
- `wedge-tool/static/encadrement-loyer-echirolles-2026.html`
- `wedge-tool/static/encadrement-loyer-bordeaux-2026.html`
- `wedge-tool/static/encadrement-loyer-lyon-2026.html`
- `wedge-tool/static/encadrement-loyer-paris-15eme-2026-faq-complete.html`
- `wedge-tool/static/llms-full.txt`
- `data/interpretation-library-v0/recourse-templates/loyer-abusif.v0.json` (mentionne C300657 jurisprudence_refs[0] — peut être conservé car contexte recours abusif ≠ encadrement loyer généralisé, à arbitrer)
- `wedge-tool/static/api-recourse-md-cache/loyer-abusif.md` (cache rendered loyer-abusif template)

Scope strict critic-69 #2 = Aubervilliers seul (run-489 ship). Rollback élargi = over-scope ce wake ⇒ escalade Florian inbox HEAD FYI ★★ run-493 + audit-70 ou audit-53 Strategic critic décident la suite.

## Critère monitoring

Strategic-52 critère T+72h `humans_via_seo_cluster_93 ≥ 3` deadline 2026-06-11T22:00Z **reste actif** (rollback section jurisprudence ≠ rollback enrich Aubervilliers total — page conserve : 5 FAQ DILA-vérifiables + observatoire BV N=2 + statut légal exact + scan-url preset + cross-link recourse + sitemap lastmod + communes voisines). Probabilité MISS critic-69 #3 estimée ≥80% (Google index latency 24-72h + fresh URL post-rollback recommit + cluster 93 cumul 0 T+~33h fenêtre 38h restant).

`strategic_critic_recommendations_followed_cumul=52/52` UNCHANGED (audit-52 §6 honored run-489 ✓ ; rollback jurisprudence = correction trust juridique > completeness, ne pénalise pas le streak).
`tactical_critic_recommendations_honored_cumul=73 → 74 ★` (critic-69 #2 honored J+0 T+~46min).
