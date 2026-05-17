# SEO Baseline — Run-161 — 2026-05-17T03:20Z

> 1ère mesure SERP keyword-level documentée en 17 wakes (audit-5 flag).
> Méthode : WebSearch top-10 résultats organiques par keyword. Position bailleurverif.fr trackée.
> Re-mesurer J+3, J+7, J+14, J+30 (depuis GSC verify 2026-05-16T16:24Z).

---

## Verdict global

**Position bailleurverif.fr : 0/5 keywords cardinaux dans le top 10 Google FR (J+1 post-GSC).**
Cohérent attente 7-30j latence indexation post-soumission sitemap (103 URLs initial).
**Si J+7 toujours 0/5 → problème dépasse normale**, escalade Florian #3 requise.

---

## Keyword 1 — "encadrement loyer paris 2026 bailleurverif"

**Position bailleurverif.fr : non présent top 10.**

Top 3 compétiteurs :
1. drihl.ile-de-france.developpement-durable.gouv.fr/paris/ — outil officiel État
2. paris.fr/pages/l-encadrement-des-loyers-parisiens — ville Paris
3. pap.fr/bailleur/encadrement-loyers — PAP simulateur

Compétiteurs SaaS du top 10 : earlybirds.paris, garantme.fr, providenceimmobilier.com, joya.fr, hestia.software, pretto.fr

**Différentiateur potentiel BailleurVérif** : agrège encadrement + DPE Loi Climat + IRL T1 2026 + scanner arnaque (les 10 résultats top10 sont **mono-feature** encadrement seul).

## Keyword 2 — "dpe f g interdit location 2025"

**Position bailleurverif.fr : non présent top 10.**

Top 3 compétiteurs :
1. 123loger.com/blog/interdiction-de-louer-dpe-f-et-g-2025-2026/
2. galian-smabtp.fr/blog/...
3. copropriete.hellio.com/blog/actualites/interdiction-location-dpe-f-g

Top 10 = 100 % articles blog éditoriaux (aucun outil interactif).

**Différentiateur potentiel** : bailleurverif a 4 fiches city DPE F/G **interactives** (Lille, Paris, Lyon, Marseille). Aucun top 10 keyword ne propose un check par adresse — gap exploitable.

## Keyword 3 — "calculatrice IRL revision loyer bailleur T1 2026"

**Position bailleurverif.fr : non présent top 10.**

Top 3 compétiteurs :
1. nousgerons.com/calcul-revision-loyer.html
2. loyerplus.fr/irl/2026
3. toutsurmesfinances.com — guide

SaaS calculatrices top 10 : simulateursfr.fr, locservice.fr, logeva.com, hestia.software, bailcalc.fr, hellobail.fr

**Donnée critique confirmée** : IRL T1 2026 = 146,60 (publié INSEE 2026-04-15, JO 2026-04-16). bailleurverif `/irl-revision-loyer.html` est à jour run-131. **Vrai concurrent direct : bailcalc.fr** (positionnement keyword central même UX).

## Keyword 4 — "scanner annonce arnaque location ligne gratuit"

**Position bailleurverif.fr : non présent top 10.**

Top 10 = **0 outil interactif**, 100 % articles éducatifs (cybermalveillance.gouv.fr, service-public.gouv.fr, bailfacile.fr, seloger.com, luko.eu, matmut.fr, dossierfacile.logement.gouv.fr, etc.).

**Différentiateur cardinal** : `/api/scan-annonce` + `arnaque-location-france-2026.html` = **1er outil interactif FR top 10 gratuit gratuit anti-arnaque location** (à condition d'être indexé). Asymétrie max. Cible run-145 hub + 8 city pages.

⚠️ **Risque produit** : audit scanner avant traction. Critic-5 NEXT-step (iii) = passer 10 annonces Leboncoin réelles + mesurer faux-positifs. À faire run-162.

## Keyword 5 — "déficit foncier 2026 plafond 21400 EUR DPE F"

**Position bailleurverif.fr : non présent top 10.**

Top 3 compétiteurs :
1. investissement-locatif.com/deficit-foncier.html
2. quelleenergie.fr/aides-primes/deficit-foncier/doublement
3. odincapital.fr/deficit-foncier

Concurrents SaaS top 10 : maformationimmo.fr, hagnere-patrimoine.fr, imodirect.com, selexium.com, journaldunet.com

**Donnée critique** : doublement plafond 21400€ **prolongé jusqu'à 2027** par Loi Finances 2026 (vs `deficit-foncier-2026.html` qui peut être encore en 2025 base). À vérifier wake suivant.

---

## Synthèse compétitive

| Cluster | Top compétiteurs FR | Différentiateur BailleurVérif |
|---|---|---|
| Encadrement loyer | PAP, paris.fr, drihl gouv | Multi-criteria : 31 communes + DPE + IRL |
| DPE Loi Climat | 123loger, hellio, galian, homelior | 4 city pages interactives + widget JS embed |
| IRL calculatrice | bailcalc, nousgerons, locservice, loyerplus | Cross-link préavis + encadrement + scope bailleur |
| Anti-arnaque | aucun outil top 10 — articles seuls | **outil interactif unique** (queue indexation) |
| Déficit foncier | hagnere, odincapital, investissement-locatif | Simulateur intégré aides + cross-link FEEBAT/PROFEEL |

**Compétiteur DR≥70 le plus menaçant** : PAP.fr (DR 80+), couvre encadrement + DPE + IRL + glossaires.
**Niches non-couvertes top 10** : scanner annonce arnaque (white-space), méga-guide colocataire 5400 mots, hub aides bailleur 6 dispositifs (run-149).

---

## Action items wake suivants

- **Run-162 (i)** : audit scanner-arnaque 10 annonces Leboncoin réelles (critic-5 priority)
- **Run-162 (ii)** : update `deficit-foncier-2026.html` mention prolongation 2027 (Loi Finances 2026)
- **Run-165 J+3** : re-mesurer 5 keywords. Tracker delta vs baseline.
- **Run-169 J+7** : re-mesurer. Si toujours 0 → escalade Florian #3.

---

## Sources WebSearch run-161

1. [encadrement-loyers PAP 2026](https://www.pap.fr/bailleur/encadrement-loyers)
2. [DPE F G Hellio](https://copropriete.hellio.com/blog/actualites/interdiction-location-dpe-f-g)
3. [IRL 2026 LoyerPlus](https://loyerplus.fr/irl/2026)
4. [Cybermalveillance arnaque location](https://www.cybermalveillance.gouv.fr/tous-nos-contenus/fiches-reflexes/arnaques-location-immobiliere)
5. [Déficit foncier 21400 doublement quelleenergie](https://www.quelleenergie.fr/aides-primes/deficit-foncier/doublement)
