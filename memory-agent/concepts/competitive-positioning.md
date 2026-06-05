---
name: Competitive positioning
description: Tableau honnête BailleurVérif vs ANIL/Service-Public.fr/DRIHL/PAP-SmartLoc — différenciateurs factuels + ship-gate "would they pay"
type: project
---

# Competitive positioning — BailleurVérif vs alternatives FR

> **Source décisive** : Florian brief inbox.md 2026-06-03T16:30Z (standard "would they pay" + tableau) + 2026-06-03T17:00Z item D (NEW concept), critic-61 prescription #1 (5 colonnes).
> **Statut** : v0 2026-06-05 run-445. Update à chaque NEW feature shippée + à chaque changement parité fonctionnelle concurrent.
> **Discipline** : factuel binding. Pas d'invention. Si une feature qu'on revendique n'existe pas vraiment ou est superficielle ⇒ refactor avant claim (Florian 06-03T16:30Z).

## Tableau comparatif (binding factuel)

| Critère | ANIL | Service-Public.fr | DRIHL (Préfecture IDF) | PAP / SmartLoc | BailleurVérif |
|---|---|---|---|---|---|
| **Verdict 30s annonce/loyer** | ❌ | ⚠️ Simulateur séparé "loyer encadré Paris" | ❌ | ❌ | ✅ wedge 5Q + scan-url |
| **LRAR pré-remplie auto** | ❌ (template à recopier) | ❌ (modèle PDF générique) | ❌ | ❌ | ⚠️ template `/api/recourse/<tag>` mais pas LRAR final juridique vérifié |
| **Calcul trop-perçu rétroactif 3 ans** | ❌ | ❌ | ❌ | ❌ | ⚠️ formule présente loyer-abusif mais pas UI calculateur dédié |
| **Jurisprudence Cassation linked** | partiel (ADIL conseil oral) | ❌ | ❌ | ❌ | ✅ 9 ECLI Cass. (3×3 templates cat-3) |
| **Observatoire data live (CSV)** | ❌ | ❌ | ❌ | ❌ | ✅ N=232+ data.gouv.fr CC-BY 4.0 + chain 11 vagues git |
| **Open source MIT GitHub** | ❌ | ❌ | ❌ | ❌ | ✅ `Creariax5/bailleurverif` |
| **Couverture villes encadrement** | nationale | nationale | Paris seul | nationale | 11 city-pages (Paris/Lyon/Lille/Villeurbanne/Plaine Commune/Est Ensemble/Bordeaux/Montpellier/Grenoble/Marseille/Nice…) |
| **Conseiller humain personnalisé** | ✅ ADIL (RDV gratuit) | ❌ | ⚠️ form contact lent | ❌ | ❌ |
| **Brand ancienneté / légitimité** | ✅ ANIL depuis 1971 (loi 70-9) | ✅ État officiel | ✅ Préfecture IDF | ✅ PAP 1975 | ❌ 2026 (≤6 mois) |
| **Avis juridique opposable** | partiel (note conseil ADIL) | ❌ | ✅ arrêté préfectoral source | ❌ | ❌ |
| **DPE calendrier 2025/28/34** | ✅ fiche pédagogique | ✅ fiche service-public | ❌ | ⚠️ mention basique | ✅ `/calendrier-interdiction-dpe-2025-2028-2034.html` (run-429) |
| **Questions-réponses bailleur** | ✅ FAQ générique | ✅ FAQ générique | ❌ | ❌ | ✅ `/questions-reelles-bailleurs-fr.html` 10Q DILA+CCH+CGI (run-435) |
| **Aides bailleur 2026 (MaPrimeRénov+CEE+éco-PTZ)** | partiel | ✅ fiche dédiée | ❌ | ❌ | ✅ `/aides-financieres-bailleur-2026.html` (post-rewrite run-425) |
| **Indexation IRL calcul rétroactif** | ❌ (oral ADIL) | ✅ simulateur IRL | ❌ | ⚠️ basique | ⚠️ template présent, calculateur UI à ship |
| **Carte heatmap conformité** | ❌ | ❌ | ❌ | ❌ | ❌ (à ship Phase 2 sur observatoire data) |
| **Alerte JORF/jurisprudence push** | ❌ | ❌ (newsletter génér.) | ❌ | ❌ | ❌ (rail Phase 2) |
| **Tableau bord multi-bien bailleur** | ❌ | ❌ | ❌ | ❌ | ❌ (rail Phase 2 modèle A) |
| **API publique** | ❌ | ❌ | ❌ | ❌ | ⚠️ endpoints internes pas semver /v1/ |

## Forces défendables BailleurVérif (binding factuel)

1. **Verdict 5Q 30s avec source DILA** — aucun concurrent ne livre verdict instantané. ANIL = RDV humain (24-72h délai). SP-fr = simulateur séparé. ✅ ship-gate "would they pay €5 pour économiser 15 min recherche" = OUI confirmé.
2. **Jurisprudence Cass. cross-référencée 9 ECLI** — ANIL cite jurisprudence oralement (RDV), pas de DB publique. Nous = cross-link `/recourse/<tag>` + UI verdict. ✅ ship-gate "would they pay €10 LRAR + jurisprudence" = OUI si LRAR opposable.
3. **Observatoire data live N=232+** — APUR+Fondation Logement vendent leurs études. Nous = data.gouv.fr CC-BY 4.0 + chain 11 vagues git timestampée inforgeable. ✅ ship-gate "would they (chercheur/journaliste) pay €50 CSV + méthodo" = OUI niveau APUR.
4. **Open source MIT** — différenciateur trust + audit + intégrabilité B2B futur. Asymétrie vs ANIL/SP-fr/DRIHL (closed). ✅ ship-gate trust gain.
5. **Couverture programmatique 11 villes (extensible)** — DRIHL = Paris seul, ANIL national mais générique. Nous = data unique par ville (arrêté + observatoire local + FAQ DILA territorialisée). ⚠️ ship-gate "would they pay €1 page Lyon vs Wikipedia" = OUI **uniquement si data unique** sinon NON.

## Faiblesses honnêtes (binding transparence = moat)

1. **Brand <6 mois** — ANIL+SP-fr+DRIHL ont 30-50 ans de légitimité institutionnelle. Compensé par open source + transparency observatoire + GitHub history.
2. **0 avis juridique opposable** — vs DRIHL (arrêté officiel) ou ADIL (note conseil). Compensé par citation DILA + jurisprudence Cass. publique (lecteur peut vérifier).
3. **0 conseiller humain** — ANIL = ADIL RDV gratuit, c'est leur force. Nous = self-service. Compensé par verdict 30s vs RDV 72h.
4. **LRAR pas finale juridique vérifiée** — template présent mais pas niveau "envoyable telle quelle 100% conforme loi 89-462 + jurisprudence". À polish run-446+ (Florian critère ship-gate "would they pay €10" non encore atteint strict).
5. **Calculateur trop-perçu UI non-shippé** — formule présente mais pas widget interactif (input loyer payé + plafond + durée → résultat €X récupérables). Ship priorité Phase 1 polish.
6. **Couverture villes 11 vs national** — work-in-progress, pas weakness perçue tant que paramétrable + sitemap montre extension.
7. **0 alerte push** — rail Phase 2 modèle A.

## Critère ship-gate "would they pay €X" — appliqué (binding)

Chaque feature/page NEW DOIT passer ce filtre AVANT ship (Florian 06-03T16:30Z) :

| Feature | "Would Bouygues iPhone user pay €X ?" | Verdict ship |
|---|---|---|
| Wedge homepage 30s verdict | €5 économise 15min recherche service-public + calcul plafond | ✅ live |
| Scan-url annonce automatique | €2-5 verdict instantané "illégale + recours" si analyse pointe articles loi 89-462 exact | ⚠️ live mais score conformité à enrichir |
| LRAR pré-remplie | €10 lettre opposable juridique + calcul rétroactif 3 ans | ⚠️ template présent, polish requis |
| Pages programmatiques ville | €1 page Lyon vs Wikipedia/SP-fr UNIQUEMENT si data unique observatoire+arrêté+FAQ locale | ⚠️ 4/11 enrichies (Paris, Lyon, Villeurbanne, Echirolles) |
| Observatoire data CSV | €50 chercheur/journaliste pour méthodo+chain 12 vagues | ✅ data.gouv.fr live |
| Calendrier DPE 2025-2034 | €3 calendrier clair + verdict "MON DPE concerné ?" | ⚠️ page live, verdict-DPE-personnel UI manquant |
| Questions-réelles bailleurs | €5 corpus 10Q DILA-grounded vs FAQ générique SP-fr | ⚠️ live, mesure T+72h en cours |
| Aides bailleur 2026 | €3 compilation MaPrimeRénov+CEE+éco-PTZ structuré par bien | ⚠️ live post-title rewrite, mesure GSC pending |

## Discipline factuelle binding (Florian 06-03T16:30Z)

- ❌ Pas d'invention features que nous n'avons pas vraiment ⇒ refactor avant claim publique
- ❌ Pas de cacher faiblesses (couverture villes limitée, pas avis opposable) — transparence = moat
- ❌ Pas marketing aveugle ("meilleure plateforme FR") sans backing factuel
- ✅ Lien sortant vers ANIL/SP-fr/DRIHL sur chaque page programmatique = trust gain + honnêteté
- ✅ Tableau ci-dessus mis à jour à chaque ship NEW feature (✅ → ⚠️ → ❌ état réel)

## Persona-fit par sub-persona (cf personas-segments.md)

| Sub-persona | Concurrent dominant actuel | BailleurVérif avantage |
|---|---|---|
| A.4 #17 Locataire loyer abusif zone encadrée | ANIL (RDV oral) | Verdict 30s + cat-3 jurisprudence linked |
| A.4 #18 Locataire IRL erronée | SP-fr simulateur IRL | Calcul rétroactif 3 ans + recours structuré |
| A.4 #19 Locataire dépôt garantie | ANIL générique | Cat-3 template + délai M+2 binding |
| A.3 #12 Locataire DPE G | SP-fr fiche statique | Verdict perso "MON DPE concerné ?" UI à polish |
| B.1 #27 Bailleur multi-bien 2-5 | ❌ (pas de concurrent positionné) | **Persona Phase 2 cible** — alertes JORF + dashboard |
| B.2 #35 Bailleur DPE G urgence | ANIL/SP-fr générique | Aides 2026 compilées + calendrier travaux |
| C.1 #43 Agence immobilière | logiciels métier (Vesta, Adésia, Krea) | Pas concurrent direct, API future |

## Roadmap Phase 1 polish (priorité ship-gate)

**Court terme (≤2 wakes)** :
1. UI calculateur trop-perçu IRL (formule existe, widget manquant) — passe "would they pay €5" si UX fluide
2. Verdict-DPE-personnel `/calendrier-interdiction-dpe-2025-2028-2034.html` (input DPE class → output "votre échéance + recours bailleur")
3. Section "Pourquoi BailleurVérif ≠ ANIL ≠ SP-fr" homepage avec lien comparateur (cf brief 06-03T16:30Z action #2)

**Moyen terme (≤5 wakes)** :
4. LRAR-final-juridique-opposable polish (mentions obligatoires loi 89-462 + format LRAR conforme + jurisprudence Cass. précise)
5. Page `/bailleurverif-vs-alternatives.html` comparateur honnête (BAN audit-44 NEW FILE → defer audit-45+)
6. Section "Quoi de plus que ANIL/SP-fr" 3 lignes factuelles sur CHAQUE page programmatique

## Anti-pattern proscrit (binding)

- ❌ Ship features superficielles "ça remplit roadmap" — qualité > quantité (Florian P1)
- ❌ Comparateur biaisé pro-BailleurVérif — table ci-dessus DOIT rester factuel binding
- ❌ Copy template programmatique sans data unique — Google déduplique + €X = 0
- ❌ Cacher faiblesses brand <6mois / 0 opposable — transparence binding moat

## Méthodologie update tableau

À chaque ship NEW feature/page :
1. Update colonne BailleurVérif (❌ → ⚠️ → ✅)
2. Vérifier concurrent column si claim "ils n'ont pas" est toujours vraie (check trimestriel ANIL/SP-fr/DRIHL/PAP UPDATES)
3. Si concurrent shippe parité ⇒ flag inbox HEAD + replan différenciation

Cooldown re-audit concurrent : 90j (sauf signal externe : presse / sub-seo-monitor flagge évolution majeure).
