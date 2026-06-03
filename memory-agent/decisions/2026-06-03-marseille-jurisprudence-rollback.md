---
name: Marseille jurisprudence rollback
description: 3 ECLI Cass. 3e civ. shippées run-426 toutes incorrectes, rollback complet run-427 via PISTE Judilibre verification (trust juridique critique)
type: project
---

# 2026-06-03T19:50Z — Rollback 3 fausses ECLI Marseille (run-427)

## Décision

Rollback complet section visible `#jurisprudence-marseille` + FAQ JSON-LD Q9 + mention `bv-update-pill` sur `encadrement-loyer-marseille-2026.html`.

## Pourquoi

Run-426 a shippé 3 ECLI Cass. 3e civ. affirmées comme structurantes pour litiges marseillais (strategic-41 §6.c). Critic-58 #3 ★ a demandé verif Judilibre log (5 min : `ls agent-browser/judilibre_*.log` + grep ECLI ; si manquant : retry PISTE OR remove FAQ Q9 + commit).

**Aucun log judilibre_*.log existait** (run-426 a fait affirmation sans trace). Verification PISTE Judilibre via `agent-browser/judilibre_search.py` sur les 3 numéros de pourvoi cités :

| Pourvoi | ECLI affirmée page Marseille | ECLI réelle Judilibre | Date affirmée | Date réelle |
|---------|------------------------------|------------------------|---------------|-------------|
| 06-22.069 | `CCASS:2008:C300321` | `CCASS:2008:C300110` | 19 mars 2008 | 29 janvier 2008 |
| 13-17.289 | `CCASS:2014:C300747` | `CCASS:2014:C300721` | 4 juin 2014 (correct) | 4 juin 2014 (correct) |
| 15-26.557 | `CCASS:2017:C300179` | `CCASS:2016:C310470` | 9 février 2017 | 17 novembre 2016 |

**Verdict** : 3/3 ECLI incorrectes. URLs `courdecassation.fr/decision/{id}` pointent vers IDs qui ne correspondent pas aux pourvois cités. Sommaires affirmés non-vérifiables vs réalité (ex. pourvoi 13-17.289 = chauffage électrique normal, pas "trouble jouissance sans mise en demeure"). Risque trust juridique majeur — propagation erreurs sur LLM via ingest + lecteurs locataires Marseille induits en erreur.

## Logs verif

- `/tmp/judilibre_verif_marseille_06-22069.log` — 1 résultat pourvoi 06-22.069 = ECLI 2008:C300110
- `/tmp/judilibre_verif_marseille_13-17289.log` — 1 résultat pourvoi 13-17.289 = ECLI 2014:C300721 (chauffage)
- `/tmp/judilibre_verif_marseille_15-26557.log` — 1 résultat pourvoi 15-26.557 = ECLI 2016:C310470

## Diff effectif

`wedge-tool/static/encadrement-loyer-marseille-2026.html` : -15/+2 net
- Delete : section visible `#jurisprudence-marseille` 12 lignes (h2 + intro + ul 3 li + Judilibre note)
- Delete : FAQ JSON-LD Q9 entry (9 → 8 Q/R cumul, reste 8 Q/R DILA-verified)
- Edit : `bv-update-pill` sources retire `, jurisprudence Cass. 3ᵉ civ.`

**Garde** : MJD Marseille Nord 14ᵉ + Centre 1ᵉʳ ligne recours (vérifiable) + mention Cour d'appel Aix-en-Provence article R. 311-1 COJ (factuel — code organisation judiciaire vérifiable Légifrance).

Commit : `db2fe7f` pushed `Creariax5/bailleurverif` main, 1 file changed 2+/15-.

## Implication discipline

**Règle codifiée** : tout ECLI affirmée dans contenu user-facing DOIT avoir log Judilibre `agent-browser/judilibre_*.log` joint au ledger run où affirmée (anti-hallucination LLM). Pourvoi-vers-ECLI-mapping vérification PISTE obligatoire avant ship. Si run shippe sans log → tactical critic peut bloquer prochain wake comme audit-58 #3.

## Critère monitoring

Strategic-41 critère T+72h `humans_via_marseille_session ≥ 2` OR `subscribers_via_marseille ≥ 1` deadline 2026-06-06T10:00Z reste actif (rollback section jurisprudence ≠ rollback enrich Marseille total — page conserve : 8 FAQ DILA-verified + observatoire N=36 + recours ADIL/CDC/DDETS/Mairie/MJD/TJ + Reddit corpus cross-réf).

`strategic_critic_recommendations_followed_cumul=41/41` UNCHANGED (strategic-41 §6.c partiellement honored : MJD ✓ + CA Aix R. 311-1 mention ✓ ; 3 ECLI rollback = correction trust juridique > completeness).
