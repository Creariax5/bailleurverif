# Produits alternatifs — vertical bailleur FR

> Fichier créé suite à DIRECTIVE 4 §3 (2026-05-14T21:05Z). Backlog d'idées produit hors-BailleurVérif, dans le même vertical bailleur particulier FR 1-5 biens. Sert de **liste prête** si BailleurVérif rate (4 visites uniques en 36h, 0 capture). Ne pas confondre avec un pivot : on ne pivote QUE sur signal d'invalidation Phase 1bis (≥100 visites + <5% conversion email).
>
> Méthode d'évaluation par idée :
> - **Concept** : 1 phrase
> - **Audience** : qui paye, à quel moment (cycle de vie bailleur)
> - **Coût build agent** : V0 réalisable en autonomie ?
> - **Distribution** : canaux activables sans Florian
> - **Signal vs stock** : peut-on mesurer l'engagement sans 100€ de Google Ads ?
> - **Friction recouvrement** : LMNP/RGPD/légalité
> - **Reco** : priorité 1-5 et conditions d'activation

---

## Idée 1 — Générateur de lettres recommandées bailleur (LRAR)

**Concept** : tool gratuit qui génère le PDF d'une LRAR conforme (préavis non-renouvellement bail meublé, rappel impayés J+10, mise en demeure J+30, congé pour vente/reprise, révision IRL). Bailleur entre les variables (date, nom locataire, adresse, motif), reçoit le PDF rempli, prêt à imprimer pour La Poste.

**Audience** : bailleur en crise / fin de cycle. Demande forte : un impayé = un moment de stress + besoin d'agir vite + 50-150€ d'avocat si délégué. ChatGPT répond mais c'est friable et le bailleur doute. Un tool dédié = confiance + zéro réflexion juridique.

**Coût build agent** : V0 = template HTML + variables + génération PDF côté client (jsPDF) ou côté serveur (weasyprint/wkhtmltopdf). Estimation 4-6 heures agent. Templates juridiques = info publique (loi 89, Code civil 1730+).

**Distribution** :
- SEO longtails forts : "modèle lettre rappel loyer impayé", "lettre congé bail meublé fin", "mise en demeure locataire" → volume Google FR ~50-200k recherches/mois sur ces requêtes
- Mastodon `#immobilier` post : "Voici 5 modèles LRAR conformes 2026, gratuits"
- Cible explicitement les autres tools gratuits qui *ne génèrent pas* le PDF mais le markdown brut (ex : modele-de-lettre.com)

**Signal vs stock** : K-factor potentiel > BailleurVérif car le besoin est aigu (impayé en cours). Email gate "envoyez-moi mes 3 prochaines lettres en PDF" → conversion intuition >5% à 100 visites.

**Friction recouvrement** : aucune juridique tant qu'on ne se présente pas comme avocat / cabinet (mention "modèles informatifs, ne se substitue pas à un conseil juridique"). RGPD ≃ nul (les données restent client-side ou non-persistées).

**Reco** : **priorité 1**. À déclencher si BailleurVérif <10 captures à J+14 (vers 2026-05-28). Coût V0 estimé 1 sprint agent (2-3 wakes), réutilise le port 8103 du VPS. Migration aisée vers `lettres.bailleurverif.fr` si NDD acheté.

### Concurrence observée (cycle 2, run-74, 2026-05-15)

WebSearch 1 query → 10 acteurs identifiés sur le longtail "loyer impayé modèle lettre". Cartographie :

| Acteur | Type | Modèle d'affaire | Différenciateur |
|---|---|---|---|
| **laposte.fr** | Service officiel | Modèle gratuit + envoi LRAR papier 5-8€/envoi | Monopole physique LRAR + crédibilité institutionnelle |
| **ar24.fr** | LRE qualifiée | Envoi LRE 3-5€/envoi (valeur juridique équivalente loi 2016-1321) | Acteur tech B2B émergent, force de pénétration 2025-26 |
| **lebonbail.fr** | Plateforme bailleur | Modèles gratuits + outils SaaS (estimation, etc.) | **Vrai concurrent dédié bailleur**, déjà installé |
| **dooradoora.com** | Générateur interactif | "Mise en demeure en 1 minute" gratuit | Concurrent V0 direct = pattern Idée 1 déjà existant |
| **cautioneo.com** | Caution locative | Modèles gratuits = content marketing → lead caution | Acquisition pour produit caution |
| **bailpdf.com** | Modèles + GLI | Modèles gratuits + cross-sell assurance | Aggregator + apporteur GLI |
| **protectionloyer.com** | GLI | Modèles gratuits → lead GLI | idem |
| **empruntis.com** | Courtier crédit | Modèle gratuit éditorial | SEO content pour acquisition crédit immo |
| **droit-finances.commentcamarche.com** | Éditorial généraliste | Pub display | Trafic SEO masse |
| **adil75.org** | Association | PDF gratuit, statique | Référence institutionnelle (mais ADIL 1 par département) |

**Findings cycle 2** :

1. **Marché des modèles statiques = TOTALEMENT saturé**. ~10 sources sur la première page Google, gratuit, indexé depuis >5 ans. Différenciation par "tool qui fournit un texte modèle" = impossible.
2. **Concurrent direct V0 = Dooradoora + LeBonBail** = générateurs interactifs gratuits déjà en place. Notre V0 templated (Idée 1 §coût build) ne ferait que dupliquer.
3. **Vraie opportunité 2025-26 = LRE qualifiée (AR24, La Poste)**. Pricing 3-5€/envoi, valeur juridique pleine, courbe d'adoption forte côté bailleurs particuliers selon volume requêtes. Le bailleur cherche désormais "comment envoyer une mise en demeure SANS aller à La Poste" — c'est l'angle inbound restant.
4. **Volume estimé** : ~250-450k impayés/an FR (sources LeBonBail/Cautioneo/ADIL). Avec 1-3 LRAR par cas → marché 250k-1.4M envois/an minimum. À 4€/envoi commission apporteur 30% = 0.30M-1.7M€/an de revenu théorique apporteur. Plafond brut, pas adressable directement (faut une part de marché ≥1%).
5. **Aucun acteur n'offre le PACK cycle de vie complet** : J+10 relance → J+30 mise en demeure → J+60 résiliation → résiliation pour congé vente/reprise. Chaque acteur fait 1 modèle. Pas de produit "Suivi-impayé en 3 étapes assisté + envoi LRE intégré".

**Révision priorité Idée 1** :

- ❌ V0 templates statiques seuls = **priorité abandonnée** (concurrence saturée, pas de différenciation)
- ✅ V1 "Suivi-impayé assisté" (cycle 3-étapes + relances mail bailleur + intégration LRE AR24 apporteur) = **priorité 2 maintenue mais V1 obligatoire** (V0 sans valeur)
- Friction nouvelle identifiée : partenariat apporteur AR24/La Poste requis pour revenu → dépend de Florian (contrat B2B) → entrée dans florian-todos.md si l'idée est activée

**Conséquence sur synthèse priorisation (ligne ~145)** :

| Avant | Après cycle 2 |
|---|---|
| Idée 1 LRAR = priorité 1 | Idée 1 LRAR V0 = abandon ; V1 LRAR-pack-assisté = priorité 3 (besoin apporteur) |
| Idée 5 déficit foncier = priorité 3 (ROI/coût peut-être #1) | **Idée 5 = priorité 1** (synergie max wedge, 100% autonome, pas de concurrence frontale identifiée) |
| Idée 3 Vendre/garder = priorité 2 | Idée 3 = priorité 2 (inchangé, à valider au cycle 3) |

**Audit concurrence à faire cycle 3** : Idée 5 (déficit foncier — qui propose un calculateur public ? impots.gouv.fr ? simulateurs notaires ?) avant de monter en priorité 1 ferme.

---

## Idée 2 — Comparateur GLI / PNO / Loyer-Impayé instantané

**Concept** : bailleur entre profil (loyer, ville, type de bien, profil locataire) → tool affiche en 30s le comparatif des 4-6 contrats du marché (Galian, Verlingue, Lovys, SACAPP, etc.) avec primes annuelles + couvertures + franchises. Email gate pour devis personnalisé via partenaire.

**Audience** : bailleur en début de cycle (achat / signature nouveau bail). Décision GLI ≈ 200-700€/an, donc 30-60 min de recherche actuellement = friction réelle.

**Coût build agent** : V0 = tableau statique des grilles publiques + simulateur de prime. Estimation 3-4 heures agent. **Difficulté** : les grilles GLI ne sont pas toutes publiques — nécessite scraping/négociation API avec les courtiers, ce qui dépend d'accords B2B.

**Distribution** :
- SEO : "comparateur GLI", "meilleure assurance loyer impayé" (10-30k/mois FR)
- Lien partenaire = revenu d'apporteur ~50-200€/lead côté courtier (modèle classique aggregator)

**Signal vs stock** : signal très clair (clic lien partenaire = qualified intent). Mais : ROI dépend d'un partenariat courtier signé, donc dépend de Florian. Pas autonome.

**Friction recouvrement** : IOBSP (Intermédiaire en Opérations de Banque et Services de Paiement) = statut ORIAS requis dès qu'on touche du commissionnement assurance. **Bloqueur réglementaire dur** : pas faisable sans immatriculation préalable (~6 mois + 300€ d'inscription + responsabilité civile pro).

**Reco** : **priorité 4**. Modèle économique potentiellement plus rentable que SaaS abo (commission unitaire haute) mais friction réglementaire bloque V0 autonome. Garde-en-tête pour Phase 2-3 si BailleurVérif valide.

---

## Idée 3 — "Vendre ou garder ?" — simulateur fiscal LMNP / foncier

**Concept** : bailleur entre son bien (prix d'achat, loyer, charges, ville, statut LMNP/foncier, années détenues, situation TMI), tool calcule en 30s :
- Rentabilité nette nette actuelle (post-impôts)
- Estimation plus-value si vente aujourd'hui (avec abattement durée détention)
- Comparatif "garder 5 ans de plus" vs "vendre maintenant et placer en SCPI/ETF/livret"
- Verdict actionnable : ✅ garder / ⚠️ neutre / 🚫 vendre

**Audience** : bailleur en *milieu* de cycle (5-15 ans détention). Décision irrégulière, à fort enjeu (10-100k€ d'écart selon scénario). Demande latente forte, peu d'outils français crédibles (impots.gouv ne le fait pas).

**Coût build agent** : V0 = formules Excel-like en JS + tables LMNP régime micro/réel + table abattement plus-value durée détention. Estimation 6-8 heures agent. Doit citer impots.gouv.fr / service-public.fr pour crédibilité.

**Distribution** :
- SEO : "vendre LMNP avant 5 ans", "comparer foncier LMNP fiscalité", "plus-value immobilière calcul 2026" (~30-80k/mois FR)
- Lien interne wedge BailleurVérif → "et au fait, vendre ou garder ?" augmente friction utile post-verdict
- Mastodon : posts factuels "Saviez-vous que LMNP réel permet d'amortir le bien + déduire 100% des intérêts ?"

**Signal vs stock** : moins viral que LRAR (décision moins urgente) mais email-gate "recevez le détail du scénario optimisé" devrait convertir 8-15% sur intent qualifié.

**Friction recouvrement** : aucune dans la V0 informative. Si on ajoute un volet "mise en relation expert comptable" = même friction IOBSP que GLI (mais moindre, conseil comptable hors-réglementé).

**Reco** : **priorité 2**. Synergie forte avec BailleurVérif (même audience, complète le funnel "conformité → fiscalité → décision"). Activable si Phase 1bis valide et qu'on veut monter en gamme. Build agent autonome 100%.

---

## Idée 4 — Lecteur compteur électricité IA (photo → conso → facture estimée)

**Concept** : bailleur photographe le compteur EDF du locataire entrant/sortant. Tool extrait par vision IA le chiffre, calcule la consommation depuis dernière relève, estime facture EDF/Engie associée. Permet régularisation charges sans contestation possible.

**Audience** : bailleur de meublé / location courte durée (mise à charge réelles vs forfait), bailleur en fin de bail (état des lieux + relevé compteur).

**Coût build agent** : V0 = upload photo → API vision (Claude/GPT-4V) → parse chiffre → calcul. **MAIS** : API vision = coût ~0.01-0.05€ par image. À 100 utilisateurs/mois × 2 photos = 1-10€/mois. Sous seuil mais récurrent.

**Distribution** : niche, moins de SEO volume (estimation <5k/mois cumulé). Plus utile en cross-sell qu'en wedge standalone.

**Signal vs stock** : besoin réel mais rare (1-2 fois par bail × 5 ans). Pas un produit récurrent.

**Friction recouvrement** : modèle freemium difficile (l'usage est trop rare pour justifier un abo). Plutôt pay-per-use ou inclus dans abo "BailleurVérif Pro".

**Reco** : **priorité 5**. Idée gadget. À garder en cross-sell éventuel. Pas une bonne tête de pont.

---

## Idée 5 — Calculateur déficit foncier (10 700€) et report 10 ans

**Concept** : bailleur entre travaux récents/prévus, revenus fonciers actuels, TMI. Tool calcule :
- Économie d'impôt immédiate (jusqu'à 10 700€/an déductible du revenu global)
- Reportabilité 10 ans si plafond dépassé
- Verdict : "vos travaux 2026 vous économisent X € d'impôt sur Y ans"

**Audience** : bailleur en cycle de rénovation (DPE F→E, isolation, fenêtres) = exactement notre cible BailleurVérif (urgence DPE). **Cible quasi-identique au wedge**.

**Coût build agent** : V0 = formules fiscales standards (LOI 1976 + LF 2023-2024 ajustements). Estimation 4-5 heures agent. Tables : barème IR 2026, plafond déficit foncier, abattements régime micro vs réel.

**Distribution** :
- SEO : "déficit foncier 2026", "calcul déficit foncier travaux", "économie impôt travaux bailleur" (~20-50k/mois FR)
- **Cross-sell BailleurVérif** : après verdict DPE F (⚠️) sur le wedge, proposer "Économisez X € sur vos travaux DPE → calculer". Conversion potentielle élevée.

**Signal vs stock** : timing parfait. Le bailleur en risque DPE F est *exactement* celui qui va investir 10-30k€ de travaux = exactement la cible déficit foncier. Bundle wedge + déficit = funnel complet.

**Friction recouvrement** : aucune (calcul informatif, source legifrance/BOFIP).

**Reco** : **priorité 3**. Synergie max avec BailleurVérif. Activable en sous-page du wedge actuel (`/deficit-foncier`) sans nouveau projet. **Possiblement le meilleur ratio coût/synergie de la liste**.

### Concurrence observée cycle 3 (run-75, 2026-05-15)

**Méthode** : 1 WebSearch « calculateur déficit foncier 2026 simulateur travaux bailleur impôt en ligne gratuit France acteurs ». 10 résultats SERP page 1 cartographiés.

| # | Acteur | URL/handle | Type produit | Modèle d'affaire | Différenciateur déclaré |
|---|---|---|---|---|---|
| 1 | Lybox | `blog-investissement-immobilier.lybox.fr/calcul-deficit-foncier/` | Article blog + exemples | SaaS LMNP/déficit | Méthode 2 régimes (micro/réel) |
| 2 | Optivest | `optivest.fr/calcul-impots-revenus-foncier-simulateur/` | **Simulateur interactif gratuit** | CGP lead-gen | "guide + simulateur" tout-en-un |
| 3 | Dividom | `dividom.com/simulateurs/simulateur-investissement-deficit-foncier` | **Simulateur déficit foncier dédié** | Promoteur immo + lead-gen CGP | Calcul + investissement combinés (vend leur portefeuille) |
| 4 | Hagnère Patrimoine | `hagnere-patrimoine.fr/.../simulateur-impot-revenu` | **Calculateur IR 2026 LF 2026** | CGP | LF 2026 officiel + quotient familial + décote + PER + frais réels + CDHR + PFU 31.4% ; "100% gratuit sans inscription" |
| 5 | Expert Impôts | `expertimpots.com/articles/deficit-foncier` | Article + définition | Expert-comptable | Calcul classique + report |
| 6 | K&P Finance | `kp-finance.com/.../simulation-defiscalisation-deficit-foncier/` | **Simulation détaillée envoyée 48h** | CGP lead-gen | Élaborée par CGP humain, gratuite sans engagement (= form-fill + appel) |
| 7 | Cleerly | `cleerly.fr/impots/calcul-deficit-foncier` | **Modèle Excel téléchargeable** | Calcul rendement locatif | Exemples chiffrés + fichier Excel |
| 8 | Réduction-Impots.fr | `reduction-impots.fr/.../simulateur-deficit-foncier/` | **Simulateur dédié** | Lead-gen défisc générale | Simulateur stricto sensu |
| 9 | Investissement-Locatif | `investissement-locatif.com/deficit-foncier.html` | Article guide | Promoteur clés-en-main | Sourçage clients pour leurs offres |
| 10 | Thomas Poinsard (Ma Stratégie Patri) | `mastrategiepatrimoniale.fr/deficit-foncier-2026` | Article + simulation + "l'erreur qui coûte 2 800€" | CGP individuel | Angle pédago hook "erreur coûte 2800€" |

### Findings empiriques

1. **Marché simulateurs déficit foncier = SATURÉ frontalement** : ~10 acteurs SERP page 1 dont **6 simulateurs interactifs gratuits déjà installés** (Optivest, Dividom, Hagnère, K&P, Réduction-Impots, + tableur Cleerly). Pas de gap technique évident à combler par un V0 supplémentaire.

2. **Modèle d'affaire dominant = lead-gen CGP/promoteur** (8/10 acteurs) : le simulateur n'est PAS le produit, c'est l'aimant à email/téléphone pour vendre derrière (LMNP, défisc, conseil patrimoine). Notre modèle Conformité-as-a-Service B2C SaaS récurrent **n'a pas de hook lead-gen vertical fort** sur ce calcul → pas d'avantage compétitif sur ce segment.

3. **Hagnère Patrimoine = différenciateur "100% gratuit sans inscription"** : précisément l'angle que nous aurions pris (calcul instantané sans email-gate, comme le wedge actuel). Donc même cette différenciation est déjà saturée.

4. **Aucun simulateur ne combine "déficit foncier" + "DPE F/G urgence"** : c'est la seule synergie réelle observée, mais en isolation elle est minuscule (audience = "bailleur DPE F+travaux" ⊂ "bailleur travaux" ⊂ "tous bailleurs"). Le sur-set "tous bailleurs avec travaux" est exactement la cible saturée par les 6 simulateurs ci-dessus.

5. **Sources de calcul = mêmes que nos articles SEO** : LF 2026 (déficit majoré 21 400€ travaux énergétiques 2023-2026 confirmé), CGI art. 156 I 3°, plafond standard 10 700€. Aucune asymétrie d'expertise. Le calcul est commodité.

### Implication priorisation Idée 5

**INVALIDATION partielle de la promotion priorité 1 du run-74.** Reasoning :

- ✅ Validité tient toujours : audience cible synchronisée avec wedge DPE F/G, 100% autonome, peu de friction recouvrement, formules publiques.
- ❌ Invalidité partielle : **différenciation V0 stand-alone = zéro vs 10 acteurs déjà SERP page 1**. Un nouveau simulateur déficit foncier seul ne sortira pas de SERP page 5-10. Le canal SEO promis (~20-50k recherches/mois) **est déjà capturé** par lead-gen CGP qui ont des budgets backlinks/ads >>> nous.

**Révision priorité Idée 5** :
- ❌ **Idée 5 V0 stand-alone** (sous-page autonome `/deficit-foncier` avec son propre SEO) **abandonnée** — concurrence frontale CGP/promoteurs trop installée, lead-gen modèle leur paie les backlinks.
- ✅ **Idée 5 V1 = composante du wedge BailleurVérif** = priorité 1 conditionnelle. Pas un produit séparé : un **bloc additionnel dans le wedge actuel** après verdict DPE F/G, qui dit "Vos travaux DPE 2026 peuvent vous économiser jusqu'à X € via déficit foncier majoré 21 400€" → conversion email-gate du wedge réutilisée. Pas de nouveau projet, pas de nouveau SEO, juste une **value-prop additionnelle** sur le funnel existant.
- ⏳ Coût build agent V1 = **2-3h** au lieu de 4-5h (formule simplifiée + intégration UI wedge existant), pas un nouveau projet à 4-5h.

### Implication structurelle backlog

| # | Idée | Avant cycle 3 | Après cycle 3 | Raison |
|---|------|---------------|---------------|--------|
| 1 | LRAR V0 statique | priorité 1 | **abandonnée** | Saturation cycle 2 |
| 1 | LRAR V1 suivi-impayé + LRE | priorité 1 | priorité 3 conditionnelle | Saturation cycle 2 |
| 5 | Déficit foncier V0 stand-alone | priorité 1 candidate | **abandonnée** | Saturation cycle 3 ↑ |
| 5 | Déficit foncier V1 composante wedge | — | **priorité 1 confirmée** | Réutilise funnel wedge, 2-3h build, value-prop additive |
| 3 | Vendre ou garder ? LMNP | priorité 2 | priorité 2 (à auditer cycle 4) | Pas encore audité concurrence |
| 6 | Suivi DPE auto récurrent ADEME | Phase 2 cible | Phase 2 cible (inchangé) | Produit final SaaS ARR — pas audité concurrence |

### Sources cycle 3

- [Calcul déficit foncier 2026 — Lybox](https://blog-investissement-immobilier.lybox.fr/calcul-deficit-foncier/)
- [Optivest simulateur revenus fonciers](https://optivest.fr/calcul-impots-revenus-foncier-simulateur/)
- [Dividom simulateur déficit foncier](https://www.dividom.com/simulateurs/simulateur-investissement-deficit-foncier)
- [Hagnère Patrimoine simulateur IR 2026](https://www.hagnere-patrimoine.fr/ressources/simulateurs/simulateur-impot-revenu)
- [Expert Impôts — déficit foncier](https://expertimpots.com/articles/deficit-foncier)
- [K&P Finance simulation défisc](https://www.kp-finance.com/defiscaliser/simulation-defiscalisation-deficit-foncier/)
- [Cleerly calcul déficit foncier Excel](https://cleerly.fr/impots/calcul-deficit-foncier)
- [Réduction-Impots simulateur déficit foncier](https://reduction-impots.fr/defiscalisation-immobilier/deficit-foncier/simulateur-deficit-foncier/)
- [Investissement-Locatif guide](https://www.investissement-locatif.com/deficit-foncier.html)
- [Thomas Poinsard 2 800€](https://www.mastrategiepatrimoniale.fr/deficit-foncier-2026)

### Décision après 3 cycles audit concurrence

Sur les 6 idées du backlog produits-alternatifs (run-43), **2 ont été auditées concurrence-empirique (cycles 2-3)** = Idée 1 LRAR + Idée 5 déficit foncier. **Les deux V0 stand-alone abandonnées pour saturation frontale.** Pattern émergent : **toute V0 stand-alone seule contre concurrents installés depuis 5+ ans = ROI faible.** Pivot doctrinal :

> **Le seul produit nouveau qui vaut la peine d'être construit est celui qui exploite un asset existant (le wedge BailleurVérif), pas un nouveau site SEO ou un nouveau SaaS à amorcer from-scratch.**

Implication : les 4 idées restantes du backlog (3, 4, 6, et V1 LRAR/déficit foncier) doivent être réévaluées dans cette lentille = **chacune doit s'installer comme module/bloc additionnel au wedge actuel ou à BailleurVérif Phase 2, pas comme produit séparé.** Cycles 4-6 à venir auditeront les 4 restants sur ce critère.

---

## Idée 6 (bonus) — Suivi DPE automatique + alerte expiration

**Concept** : bailleur enregistre son adresse + numéro DPE. Tool monitore la base ADEME, alerte par email à J-180 et J-30 avant expiration (DPE validité 10 ans). Bundle natural avec BailleurVérif (qui est ponctuel) → BailleurMoniteur (récurrent).

**Audience** : tous bailleurs avec DPE (≈ tous, obligation depuis 2007). Renouvellement ≈ 150-300€ via diag, donc anticipation = ROI réel.

**Coût build agent** : V0 = scraper API ADEME open data (`data.ademe.fr/datasets/dpe-france`) qui est publique + cron VPS + envoi mail (SMTP encore à mettre en place côté Florian).

**Distribution** : difficile en standalone (intent latent, pas urgent). Bundle "BailleurVérif + monitoring" = up-sell naturel post-wedge.

**Signal vs stock** : c'est *le* produit récurrent du vertical. ARR-friendly (19€/mois conforme à pricing target).

**Friction recouvrement** : aucune. ADEME ouvre les données sous licence Etalab.

**Reco** : **priorité 1bis**. Pas un wedge mais le **produit final SaaS** que BailleurVérif devait devenir. À tenir en tête comme cible Phase 2.

---

## Synthèse priorisation

| # | Idée | Coût V0 agent | Synergie BailleurVérif | Autonomie | Priorité (post-cycle 3) |
|---|------|---------------|------------------------|-----------|----------|
| 5 V1 | **Déficit foncier comme bloc additionnel du wedge** | 2-3h | **Max (module wedge même funnel)** | ✅ 100% | **1 confirmée cycle 3** |
| 3 | Vendre ou garder ? LMNP | 6-8h | Forte (même audience) | ✅ 100% | **2** (à auditer cycle 4) |
| 1 V1 | LRAR suivi-impayé + apporteur AR24 | 6-8h | Moyenne | ❌ contrat B2B | **3 conditionnelle** (audit cycle 2) |
| 6 | Suivi DPE auto récurrent ADEME | 8-12h | **Bundle natural** | ✅ 100% (sauf SMTP) | **Cible Phase 2** (à auditer cycle 5+) |
| 4 | Lecteur compteur IA | 3-4h | Faible | ⚠️ coût API | **5** |
| 2 | Comparateur GLI | 3-4h | Forte (audience) | ❌ IOBSP requis | **6 (gel)** |
| 1 V0 | LRAR statique | — | — | — | ❌ **abandonnée** (cycle 2) |
| 5 V0 | Déficit foncier stand-alone | — | — | — | ❌ **abandonnée** (cycle 3)|

## Conditions d'activation

- **Si BailleurVérif <10 captures à J+14 (≈ 2026-05-28)** : ouvrir un 2e wedge (priorité 1 ou 3) en parallèle, pas en remplacement. Cross-link entre les deux.
- **Si BailleurVérif >50 captures à J+30** : ne PAS pivoter, doubler la mise sur le wedge actuel + monter Idée 6 en cross-sell.
- **Si BailleurVérif >100 captures à J+30** : Phase 2 validée, attaquer Idée 6 (récurrent) puis Idée 5 (synergie max) en sous-pages BailleurVérif.

## Méta — pourquoi cette liste maintenant

Wake 43 (DIRECTIVE 4 angle 3) : on n'a aucun signal qui dit que BailleurVérif fonctionne (4 visites en 36h sur IP brute, 0 capture). On n'a aucun signal non plus qu'il ne fonctionne pas — la cause #1 est probablement la **distribution** (1 post Mastodon, 0 NDD, 0 Reddit/Twitter). Mais en cas de validation négative, on aura besoin d'une réponse rapide. Cette liste sert d'**option** stratégique : 6 idées analysées au lieu de partir de zéro le jour J.

Coût de la liste : 1 wake (~15 min). Valeur d'option : ≥1 sprint agent économisé si pivot. ROI méta positif même si jamais utilisée — discipline "préparer la canalisation avant le débit" (pattern run-39 généralisé).
