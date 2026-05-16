# Étude de marché — SaaS pour propriétaires bailleurs particuliers (France)

**Date** : 2026-05-13
**Pour** : Florian
**Objectif** : décider si on lance un SaaS sur ce segment, et avec quel angle.

---

## 0. TL;DR — verdict honnête

| Question | Réponse |
|---|---|
| Le marché est-il gros ? | **OUI** — 5,9M de foyers fiscaux, ~10M d'individus bailleurs |
| Le pain est-il réel ? | **OUI** — confirmé par citations Finary, stats fiscalité (32% citent fiscalité comme frein principal) |
| Le marché est-il libre ? | **NON** — 8+ acteurs établis sur la gestion locative, 6+ sur la compta LMNP |
| Y a-t-il encore de la place ? | **OUI mais conditionnel** — uniquement si vrai angle de différenciation |
| Match avec un agent IA opéré 24/7 ? | **TRÈS BON** — workflow ultra prévisible, support templatable, marketing SEO dense |
| Plafond réaliste à 18-24 mois ? | **$1-3M ARR** atteignable si bon angle, $5M+ très difficile |

**Ma recommandation honnête** : **NE PAS** faire un nieme "logiciel de gestion locative" générique. **OUI**, attaquer un sous-segment ultra spécifique encore mal servi (3 angles détaillés en section 9).

---

## 1. Taille du marché

### 1.1 Population des bailleurs particuliers

- **5,9 millions** de foyers fiscaux possèdent au moins un bien en location (impots.gouv 2024-2025)
- **~10 millions** d'individus concernés (couples)
- **11% de la population française** (vs 13% en 2022 → tendance baissière)
- **22,8% du parc de résidences principales** est en location privée (INSEE 2025)

### 1.2 Segmentation par nombre de biens

| Segment | Part | Volume estimé | Profil |
|---|---|---|---|
| Mono-propriétaire (1 bien) | **70%** | ~4,1M foyers | Cible principale d'un SaaS auto-gestion |
| 2 biens | ~15-20% | ~900k foyers | Cible premium, multi-bien |
| 3+ biens | ~10-15% | ~600k foyers | Cible "investisseur sérieux", LMNP régime réel |
| Concentration extrême | 3,5% des ménages | détiennent **50%** des logements en location | Pas notre cible (gros patrimoines, professionnels) |

### 1.3 Mode de gestion (clé pour le SaaS)

- **50% confient à un professionnel** (agence) → contre 41% en 2022 → tendance hausse
- **50% gèrent eux-mêmes** → ~3M de foyers en auto-gestion = TAM SaaS
- Causes de la délégation croissante : complexité réglementaire (DPE, encadrement, GLI, fraude doc)

### 1.4 Type de location

- **56% location nue** (régime micro-foncier ou réel)
- **30% location meublée** (LMNP / LMP, régime BIC)
- **14% location saisonnière** (Airbnb-like)

### 1.5 Profil socio-démo des bailleurs

- 62% actifs professionnellement
- 75% en couple
- 53% propriétaires de leur résidence principale **sans crédit**
- 39% disposent d'un patrimoine financier > 100k€
- 49% en agglomération > 100k habitants (dont 22% en région parisienne)

**→ Conclusion** : public solvable, urbain, déjà à l'aise avec le digital. Pas un public à éduquer.

### 1.6 TAM / SAM / SOM réalistes

| Niveau | Calcul | Volume |
|---|---|---|
| **TAM** (auto-gérants × $39/mois × 12) | 3M × $39 × 12 | **$1,4 Md/an** |
| **SAM** (auto-gérants urbains 25-65 ans, 1-3 biens) | ~1,5M | **$700M/an** |
| **SOM réaliste à 3 ans** (1% de SAM) | 15 000 clients × $39 | **$7M/an ARR** |
| **SOM réaliste à 18 mois** (0,1-0,3% de SAM) | 1500-4500 clients | **$700k-2M ARR** |

---

## 2. Mapping concurrentiel

### 2.1 Logiciels de gestion locative B2C (segment principal)

| Acteur | Cible | Pricing | Force | Faiblesse | Note Trustpilot |
|---|---|---|---|---|---|
| **Smartloc** | Particuliers + GLI | 6,50€/mois | 100k bailleurs, IA anti-fraude, GLI intégrée | Signature élec en option, pas de SCI avancée, écart Google/Trustpilot suspect | 4,4 Google / 2,9 Trustpilot |
| **BailFacile** | Particuliers conformité | 9,99€/mois | 70+ procédures conformes, signature SES illimitée | Pas de réconciliation bancaire avancée | 4,7 |
| **Rentila** | Particuliers low-cost | 49€/an (4€/mois) | Le moins cher, jusqu'à 5 biens | Features basiques, pas d'IA | 4,6 |
| **GererSeul** | Particuliers compta | 117€/an | Réconciliation bancaire ACPR, 3 biens gratuit | Interface vieillotte | **4,8 (top du marché)** |
| **FairePlace** | Particuliers reg-tech | 14,90€/mois | Vérification auto encadrement loyer (9 territoires), API publique, signature AES | Plus cher, plus complexe | NC |
| **MonsieurHugo** | Particuliers + IA | 29,90€/mois (~15€ après déduction fiscale) | Premium, état des lieux IA, support juridique inclus | Cher | 4,0 (297 avis) |
| **PropManager** | Particuliers + IA | NC | "Nouvelle génération IA", 2000 utilisateurs | Petit, peu visible | NC |
| **Manda** / **Qlower** / **Maslow** | Hybrides (logiciel + service) | 2-4% du loyer | Moitié prix d'une agence, gestion déléguée | Pas pure SaaS, modèle service | NC |
| **Ublo.immo** | B2B (gestionnaires pro, coliving) | Sur devis | Plateforme complète, API ouverte | Pas pour le particulier 1 bien | NC |

**Verdict sur ce segment** : **saturé**. 5 acteurs dominants se partagent les particuliers, 2-3 acteurs IA émergent (PropManager, MonsieurHugo, Smartloc). Très peu de place pour un nieme acteur "généraliste".

### 2.2 Comptables LMNP en ligne (segment fiscal meublé)

| Acteur | Cible | Pricing | Force | Faiblesse |
|---|---|---|---|---|
| **JD2M (JeDéclareMonMeublé)** | LMNP régime réel | 289-799€/an | **Leader marché** : 94k clients, 170k déclarations, 4,8/5 sur 7000 avis | Cher, vieux site |
| **LMNP.AI** | LMNP IA-first | 179€/an (illimité) | Moins cher, positionnement IA | Petit, marque récente |
| **Decla.fr** | LMNP simplifié | 219-249€/an | Bon rapport qualité/prix | Peu de marketing |
| **Indy Premium** | LMNP + freelance | 24€HT/mois (~346€/an) | Marque connue, écosystème | Pas spécialiste |
| **Ownily** | LMNP + SCI | 299-355€/an | Multi-statut | Niche |
| **Amarris Solo** | LMNP | 210-310€/an | Cabinet expert-comptable | Vieux/cher |

**Verdict** : également saturé, mais **LMNP.AI** prouve qu'un challenger IA peut rentrer (positionnement = pricing -40% + automatisation IA).

### 2.3 Acteurs réglementaires verticaux

- **DossierFacile** (gov, gratuit) : 1,3M utilisateurs, 40k+ propriétaires, validation dossier locataire — **dominant et gratuit**
- **GarantMe** (B2C garant) : 15M€ levés, leader caution
- **Smartloc + GLI intégrée** : couvre le risque impayé pour 2-5% du loyer
- **BailNotarie** : bail authentique notarié, 150 notaires, 200 dossiers — émergent mais petit

### 2.4 Diagnostic global de la concurrence

```
Logiciel gestion locative   →  ████████ saturé (8+ acteurs)
Compta LMNP en ligne        →  ███████  saturé (6+ acteurs)
Détection encadrement loyer →  █        FairePlace seul
État des lieux IA           →  █        MonsieurHugo seul
Anti-fraude dossier IA      →  ██       Smartloc + DossierFacile
Multi-bien stratégie patrimoine  →  ░       trou de marché
Conformité bailleur all-in-one (DPE + encadrement + Alur)  →  ░       trou de marché
Outil agent IA proactif (notifie les obligations à venir)  →  ░       trou de marché
```

---

## 3. Pain points utilisateurs (citations directes)

### 3.1 Forum Finary (vrais propriétaires bailleurs)

> *"Le filtre des candidatures: beaucoup repondent avec des messages generiques"*
> *"[candidats qui] ne disent pas bonjour, répondent mal ou ne répondent pas"*
> *"[candidats] sans dossier complet de prêt"*
> *"une après-midi de visites lors du changement de locataire"*
> *"la gestion c'est chronophage"*
> *"les travaux, la copropriété, les petits problèmes courant"*
> *"2h d'AG / an"* (assemblée générale copropriété)

### 3.2 Forum CommentCaMarche

> *"J'en ai vraiment marre de ces locataires qui ne paient pas leurs loyers"*
> *"Tous les mois, tu doit cavaler après ton argent"*
> *"prend énormément de temps et d'énergie"* (procédures impayés)

### 3.3 Stats macro de la souffrance

- **32%** des bailleurs citent **la fiscalité** comme frein principal (45% chez les 35-49 ans)
- **25%** citent **la complexité de gestion**
- **20%** citent **les travaux énergétiques** (DPE)
- **25%** prévoient de **se désengager** dans les 5 ans
- Étude Sage : **56% des PME** passent **>5h/semaine sur de l'admin répétitif**

### 3.4 Pain points opérationnels mappés

| Pain | Fréquence | Coût pour le bailleur | Solution actuelle |
|---|---|---|---|
| Filtrage candidats locataires | À chaque rotation (~2-3 ans) | 1 après-midi visites + tri 50 dossiers | DossierFacile (gratuit, basique) |
| Vérification dossier (faux papiers) | À chaque rotation | Risque impayé majeur | Aucune solution simple grand public |
| Génération bail conforme | À chaque rotation | 30 min + risque erreur clause | Modèles statiques |
| État des lieux | À chaque rotation | 1-2h + litiges | MonsieurHugo (premium) |
| Quittances mensuelles | Mensuel | 5 min/mois | Tous les SaaS |
| Réconciliation bancaire | Mensuel | 15 min/mois | GererSeul, Smartloc |
| Relance impayé | 4-5% des cas/mois | Énorme stress | GLI ou rien |
| Déclaration fiscale annuelle | 1× par an | 2-8h selon régime | JD2M, expert-comptable |
| Conformité encadrement loyer | À chaque relocation/révision | Amende jusqu'à 5000€ | FairePlace |
| Conformité DPE | 1×/relocation | Impossibilité de louer si G/F/E | Diagnostiqueur |
| Travaux et urgences | Aléatoire | Stress + temps | Aucun outil |
| Suivi du parc multi-bien | Continu | Excel maison | Aucun bon outil pour 2-5 biens |

---

## 4. Cadre réglementaire — les tailwinds

### 4.1 DPE et passoires énergétiques (loi Climat & Résilience)

- **1er janvier 2025** : interdiction de louer les logements DPE **G** → 600k logements concernés
- **1er janvier 2028** : DPE **F** → +1,2M logements
- **1er janvier 2034** : DPE **E** → +2M logements
- **Total : 3,9M de logements** (12,7% du parc) seront progressivement interdits à la location
- Concerne **nouveaux baux + renouvellements + reconductions tacites**

**→ Implication SaaS** : énorme pull pour outils qui :
- alertent sur le DPE de chaque bien
- aident à anticiper la rénovation (devis, financement, MaPrimeRénov)
- conseillent vendre vs rénover

### 4.2 Encadrement des loyers

- Actif dans **9 territoires** : Paris, Lille, Plaine Commune, Lyon, Villeurbanne, Est Ensemble, Montpellier, Bordeaux, Pays Basque, Grenoble-Alpes (69 communes)
- **Amende jusqu'à 5 000€ pour personne physique**, 15 000€ personne morale
- Compliance moyenne : Paris 31%, Lille 31%, Plaine Commune **41% non-compliant**
- **FairePlace** est le seul à automatiser cette vérification

**→ Implication SaaS** : risque légal réel = appétit fort pour outil de vérification automatique

### 4.3 Loi anti-fraude documentaire (2024-2025)

- **10% des dossiers** locataires sont falsifiés en 2025 (vs 6% en 2024 = +40% en 1 an)
- DossierFacile certifie les vrais dossiers mais reste optionnel
- Smartloc a une "IA anti-fraude" mais peu défensible

**→ Implication SaaS** : créneau "DossierFacile pour propriétaires" avec certification anti-fraude IA

### 4.4 Facturation électronique B2B (sept 2026)

- Touche les bailleurs en **société** (SCI à l'IS, SAS de gestion patrimoniale)
- Pas la majorité des bailleurs particuliers (qui sont en nom propre)
- Marginal pour notre cible

### 4.5 Réformes fiscales LMNP (2025)

- Suppression de la réduction OGA/CGA
- Ré-intégration des amortissements dans la plus-value à la revente (loi finance 2025)
- Complexité accrue → demande pour outils + comptables augmentée

### 4.6 GLI (Garantie Loyers Impayés)

- Marché en explosion : **6% des loyers couverts en 2020 → 20% en 2024**
- Coût : **2,15-5% du loyer annuel** (déductible au régime réel)
- Distribution principalement par les agences ; opportunité pour un SaaS d'intégrer la GLI en upsell

---

## 5. Distribution channels — où trouver les clients

### 5.1 SEO (canal #1)

Mots-clés à fort volume mensuel (estimés) :
- "gestion locative en ligne" : 5-10k recherches/mois
- "logiciel gestion locative" : 3-5k
- "déclaration revenus fonciers" : 50k+ (saisonnier mai)
- "déclaration LMNP" : 20k+
- "DPE interdiction location" : 30k+
- "encadrement loyer Paris" : 5-10k
- "modèle bail location" : 30k+

**Concurrents SEO** : Smartloc, BailFacile, Rentila ont 5+ ans de domain authority. Stratégie possible : SEO programmatique sur les longtails ("encadrement loyer Lyon 6e", "DPE F interdiction 2028 propriétaire", "modèle bail meublé étudiant").

### 5.2 Partenariat notaires

- **75 000 notaires en France** (~6 500 offices)
- Plateformes existantes : **FoxNot**, **Quai des Notaires**, **BailNotarie**
- Le bail authentique notarié devient un atout (loi 2025 : force exécutoire en cas d'impayé)
- **Angle** : intégration où le SaaS génère un bail prêt à authentifier chez le notaire partenaire → revenue share

### 5.3 Partenariat banques / assureurs

- Les banques (Société Générale, Crédit Agricole) ont des programmes "investissement locatif"
- Les assureurs (Macif, MAAF, Matmut) vendent déjà la GLI et la PNO
- **Angle** : partenariat white-label "votre banque vous offre 6 mois de [SaaS]"

### 5.4 Marketplace immobilières

- LeBonCoin, SeLoger, PAP, MeilleursAgents
- LeBonCoin a 300k+ annonces de location → audience massive de bailleurs particuliers
- **Angle** : intégration / partenariat / pub ciblée

### 5.5 Communautés bailleurs

- **Forum Finary** : community d'investisseurs
- **r/vosfinances**, **r/immobilier** Reddit FR (forte croissance)
- **UNPI** (Union Nationale des Propriétaires Immobiliers, lobby propriétaires)
- **APAGL** (Association Pour l'Accès aux Garanties Locatives)
- **Angle** : sponsoring + posts utiles + offre membres

### 5.6 Outbound automatisé

- Cadastre = données publiques sur les propriétaires
- Croisement avec annonces de location LeBonCoin = identifier qui loue quoi
- Email/courrier ciblé : "Vous louez le bien rue X, voici un outil pour vous"
- **Limite RGPD** importante mais legal sur données cadastrales

---

## 6. Pricing benchmarks

### 6.1 Auto-gestion (notre zone)

| Tier | Prix | Acteurs | Features attendues |
|---|---|---|---|
| Free / freemium | 0€ | DossierFacile, Rentila (1 bien), GererSeul (3 biens) | Bail, quittance, 1-3 biens |
| Low | 4-10€/mois | Rentila, Smartloc (6,50€), BailFacile (9,99€) | Signature SES, dépôt garantie |
| Mid | 10-20€/mois | FairePlace (14,90€) | Conformité encadrement, multi-bien |
| Premium | 25-35€/mois | MonsieurHugo (29,90€) | IA, support juridique, état des lieux |

### 6.2 Compta LMNP

| Tier | Prix annuel | Acteurs |
|---|---|---|
| Software-only | 179-289€ | LMNP.AI, JD2M Essential |
| Software + revue comptable | 290-450€ | Decla, Ownily, Amarris |
| Expert-comptable en ligne | 400-900€ | JD2M Integral, Indy, cabinets |

### 6.3 Délégation (concurrence indirecte)

| Type | Coût |
|---|---|
| Agence traditionnelle | 6-10% du loyer (= $60-150/mois sur loyer $1000) |
| Agence digitale (Manda, Qlower, Maslow) | 2-4% du loyer |
| GLI (assurance) | 2,15-5% du loyer annuel |

### 6.4 Notre pricing cible (à valider)

**Hypothèse de positionnement** :
- **Free** : 1 bien, fonctions de base (concurrence Rentila/GererSeul)
- **Pro** : 19€/mois, multi-bien illimité, IA, conformité réglementaire, alertes proactives
- **Premium** : 39€/mois, + comptable LMNP, + GLI, + état des lieux IA, support prioritaire

ARPU cible : **$22/mois** moyen pondéré.

---

## 7. Funding & exits récents (proptech FR gestion locative)

| Acteur | Levée | Année | Investisseurs |
|---|---|---|---|
| **Garantme** | 15M€ Série B | 2023 | Bpifrance Digital, Bonsaï, 115K |
| **Kaliz** | 20M€ Série A | 2022 | NC |
| **Masteos** | 40M€ | 2022 | DST Global, Daphni |
| **Smartloc** | NC mais 100k bailleurs | — | NC |
| **JD2M** | NC mais 94k clients | — | Probable bootstrap |

**Tendance** : 70% des investissements PropTech vont à l'IA en 2025-2026 (source : Telescop). Les VCs cherchent des plays IA-natives.

**Exits notables** : pas d'exit majeur sur ce segment précis ces 2 dernières années en France.

---

## 8. SWOT global du marché

### 8.1 Forces (du marché bailleur particulier)

- TAM massif (~$700M-1,4Md/an)
- Public solvable et urbain
- Pain réel et récurrent
- Tailwinds réglementaires forts (DPE, encadrement, fiscal)
- Modèle SaaS B2C "petit ticket récurrent" prouvé (8+ acteurs rentables)

### 8.2 Faiblesses

- Marché ultra concurrentiel sur le générique
- Acteurs établis avec années de SEO et marque
- Difficulté à se différencier sur les features de base
- Public de proprios = sensible au prix, churn élevé si pas de valeur claire
- Marché qui décroît légèrement (11% vs 13% en 2022)

### 8.3 Opportunités

- L'IA n'a été ajoutée qu'en surface chez les acteurs en place
- Sous-segments mal couverts : multi-bien (2-5), conformité all-in-one, anti-fraude IA
- Tailwinds reg vont créer des besoins nouveaux (DPE, sanctions encadrement)
- 70% des VC PropTech cherchent du IA-native = financement disponible si play crédible

### 8.4 Menaces

- Pennylane / Qonto / Indy peuvent ajouter le LMNP en feature
- Smartloc + JD2M peuvent fusionner (ou être rachetés par Pennylane)
- Possible interdiction politique de la GLI ou modification fiscale soudaine
- Décroissance du nombre de bailleurs (gens vendent à cause du DPE)

---

## 9. Angles d'attaque encore ouverts (3 directions concrètes)

### 🎯 Angle A — "Le copilote IA du bailleur multi-bien" (2-5 biens)

**Insight** : les acteurs en place ciblent soit le mono-propriétaire (Rentila, Smartloc) soit les pros (Ublo). **Le segment 2-5 biens est mal servi** — trop complexe pour les premiers, trop léger pour les seconds.

**Produit** : un agent IA qui :
- Centralise tous les biens (vue patrimoniale)
- Optimise la stratégie globale (vendre lequel ? passer en LMNP lequel ? travaux DPE rentables ?)
- Alerte proactivement (DPE expirant, encadrement, IRL, déclaration impôts, GLI à renouveler)
- Génère les déclarations fiscales pour TOUT le portefeuille
- Conseille comme un expert-comptable — mais 24/7 et à $39/mois

**Cible** : 1,5M de propriétaires multi-bien
**Pricing** : $39/mois (entre Smartloc et MonsieurHugo)
**Distribution** : SEO patrimoine + partenariat Finary + Reddit r/vosfinances + outbound cadastre

**Plafond réaliste 18 mois** : 2000 clients × $39 × 12 = **$936k ARR**

### 🎯 Angle B — "Conformité-as-a-Service pour bailleurs"

**Insight** : DPE 2025/2028/2034 + encadrement loyer + anti-fraude + Alur = un mille-feuille reg que personne n'agrège bien. FairePlace est le plus proche mais reste un logiciel statique.

**Produit** : un agent qui surveille en continu la conformité de chaque bien :
- Scan DPE → alerte avant interdiction + plan rénovation + simulation financement (MaPrimeRénov, éco-PTZ)
- Vérifie le loyer face à l'encadrement → alerte avant amende
- Vérifie chaque dossier locataire (anti-fraude IA, croisement open data)
- Génère les baux conformes automatiquement
- Suit toutes les échéances légales (révision IRL, DDT, etc.)

**Cible** : tous les bailleurs en zones tendues + DPE F-G (au moins 2M de biens concernés directement)
**Pricing** : $19/mois single bien, $39/mois multi-bien
**Distribution** : SEO sur "DPE interdiction" / "encadrement loyer Paris" → trafic massif et qualifié, aujourd'hui mal capté

**Plafond réaliste 18 mois** : 3000 clients × $25 × 12 = **$900k ARR**

### 🎯 Angle C — "JD2M killer pour LMNP nouvelle génération" (LMNP IA-first)

**Insight** : JD2M domine (94k clients) mais cher (289-799€/an), interface vieille, marketing classique. **LMNP.AI** prouve qu'un challenger IA peut entrer (179€/an).

**Produit** : agent IA qui fait toute la compta LMNP automatiquement — connexion bancaire, classification automatique des charges, amortissements, génération liasse fiscale BIC, télétransmission. Plus chatbot conseil fiscal 24/7.

**Cible** : bailleurs en location meublée régime réel = **30% des bailleurs × 30% en réel** = ~500k cibles
**Pricing** : $99/an autonome, $199/an avec revue humaine annuelle
**Distribution** : SEO "déclaration LMNP" (énorme volume saisonnier mai), partenariat avec les SaaS de gestion (white-label)

**Plafond réaliste 18 mois** : 5000 clients × $150/an = **$750k ARR**, scalable à $5M sur 4 ans (taille du marché JD2M)

### Synthèse comparée

| Angle | TAM | TTR | Defensibility | Agent-operability | Match capacités Florian |
|---|---|---|---|---|---|
| A — Copilote multi-bien | 1,5M | 12 mois | 🟢🟢 | 🟢🟢🟢 | 🟢🟢🟢 |
| B — Conformité-as-a-Service | 2M | 9 mois | 🟢🟢🟢 (reg moat) | 🟢🟢🟢 | 🟢🟢 |
| C — JD2M killer | 500k | 6 mois | 🟢 (besoin trust expert-comptable) | 🟢🟢 | 🟢🟢 |

---

## 10. Ma recommandation

### Pick principal : **Angle B — Conformité-as-a-Service**

**Pourquoi** :
1. **Vrai pull réglementaire** (DPE, encadrement) qui force le marché — pas besoin d'éduquer
2. **Moat reg** : la complexité légale française est une barrière (pas de concurrent US qui rentre)
3. **SEO ouvert** : les concurrents ne captent pas bien "DPE interdiction" / "encadrement loyer ville X"
4. **Agent-operability max** : surveillance, alertes, génération de docs = parfait pour agent IA
5. **Cross-sell évident** vers les autres pains (déclaration, GLI, gestion) une fois le pied dans la porte
6. **Plafond honnête** : $1-2M ARR à 18-24 mois, $5M+ atteignable à 4 ans

### Pick secondaire : Angle A si tu veux jouer la valeur ajoutée patrimoniale

### À éviter
- "Yet another logiciel de gestion locative" → marché saturé, tu meurs
- Pure compta LMNP → JD2M trop fort sans angle IA radical

---

## 11. Plan de validation 7 jours (avant de coder)

1. **J0-J2** : 30 propriétaires bailleurs identifiés via Finary + LinkedIn (filtre "investisseur immobilier")
2. **J3-J5** : 10 RDV téléphone de 20 min, 3 questions :
   - "Quelles sont vos 3 plus grosses galères de bailleur ?"
   - "Vous payez quoi aujourd'hui pour gérer (agence, comptable, GLI) ?"
   - "Si je vous propose un agent IA qui surveille votre DPE, votre conformité loyer et vos échéances pour 19€/mois, vous prenez ?"
3. **J5-J6** : Post sur Finary + r/vosfinances : "Je code un agent IA pour bailleurs, voilà la promesse [maquette], qui veut beta-tester ?"
4. **J7** : décision

**Critère go/no-go** : si **5+ sur 10** disent "où je signe", tu y vas. Sinon tu pivotes (vers A) ou tu changes de marché (aidants familiaux).

---

## 12. Sources

### Marché et statistiques
- [INSEE — Un tiers des propriétaires possède deux logements ou plus](https://www.insee.fr/fr/statistiques/8538622)
- [INSEE — Parc de logements au 1er janvier 2025](https://www.insee.fr/fr/statistiques/8640662)
- [LocService — Part de propriétaires-bailleurs en recul](https://www.locservice.fr/actualites/la-part-de-proprietaires-bailleurs-dans-la-population-francaise-est-en-recul-15685.html)
- [Géraldine Arrou — 91 chiffres clés du marché locatif 2025](https://www.geraldinearrou.fr/blog/statistiques-marche-immobilier-locatif/)

### Pain points
- [Forum Finary — Pire galère des bailleurs](https://community.finary.com/t/proprietaires-bailleurs-cest-quoi-votre-pire-galere-au-quotidien/29079)
- [Rentila Blog — Causes de stress chez le bailleur](https://www.rentila.com/blog/2022/12/quelles-sont-les-principales-causes-de-stress-chez-le-proprietaire-bailleur/)
- [CommentCaMarche — Marre de mes locataires](https://droit-finances.commentcamarche.com/forum/affich-4633033-marre-de-mes-locataires-et-de-la-location)

### Concurrents (gestion locative)
- [Comparatif logiciels gestion locative 2026 — FairePlace](https://faireplace.com/comparatif-logiciel-gestion-locative/)
- [Smartloc Avis 2026](https://investissement-locatif-avis.fr/smartloc-avis/)
- [BailFacile Avis 2026](https://investissement-locatif-avis.fr/bailfacile-avis/)
- [GererSeul vs BailFacile](https://www.gererseul.com/gererseul-vs-bailfacile-quel-logiciel-de-gestion-locative-choisir-en-2025-notre-comparatif/)
- [PropManager — Logiciel IA 2026](https://propmanager.fr/)
- [MonsieurHugo Trustpilot](https://www.trustpilot.com/review/monsieurhugo.com)
- [Ublo — Top 10 logiciels gestion locative](https://www.ublo.immo/blog/notre-top-10-des-logiciels-de-gestion-locative)

### Concurrents (LMNP)
- [JD2M — Tarifs](https://www.jedeclaremonmeuble.com/tarif/)
- [JD2M — Top 6 comptables LMNP 2026](https://www.jedeclaremonmeuble.com/meilleur-comptable-lmnp/)
- [Comparatif logiciels LMNP 2026 — LMNP.AI](https://lmnp.ai/comparatif-logiciels-lmnp-2026)

### Réglementation
- [Service Public — Interdiction passoires énergétiques](https://www.service-public.gouv.fr/particuliers/actualites/A17975)
- [Hellio — Calendrier interdiction DPE](https://copropriete.hellio.com/blog/actualites/interdiction-location-dpe-f-g)
- [Smartloc — Guide encadrement loyers 2025](https://www.smartloc.fr/blog/encadrement-des-loyers/)
- [ANIL — Encadrement loyers zones tendues 2025](https://www.anil.org/aj-encadrement-evolution-loyers-zones-tendues-2025/)
- [FNPR — Loyers impayés en 2025](https://www.fnpr.fr/loyers-impayes-en-2025-comprendre-anticiper-et-securiser-vos-revenus/)
- [France-Épargne — Guide GLI 2025](https://www.france-epargne.fr/academy/assurance-habitation/assurance-garantie-loyer-impaye-gli-2025-le-guide-complet-pour-proprietaires-bailleurs)

### Distribution / partenariats
- [BailNotarie](https://www.bailnotarie.fr/)
- [FoxNot — Partenaire numérique des notaires](https://www.foxnot.com/)
- [Quai des Notaires](https://www.quaidesnotaires.com/)
- [DossierFacile — beta.gouv.fr](https://beta.gouv.fr/startups/dossierfacile.html)

### Funding / proptech
- [Garantme lève 15M€ — Usine Digitale](https://www.usine-digitale.fr/article/la-proptech-garantme-leve-15-millions-d-euros-et-compte-etre-rentable-d-ici-2024.N2095356)
- [Kaliz lève 20M€ — FrenchWeb](https://www.frenchweb.fr/serie-a-proptech-kaliz-leve-20-millions-deuros-pour-sa-plateforme-de-gestion-locative/433904)
- [Telescop — PropTech startups 2026](https://www.telescop.com/proptech-les-startups-immobilieres-a-suivre-en-2026/)
- [FrenchWeb — IA gestion locative](https://www.frenchweb.fr/la-gestion-locative-nouveau-champ-de-bataille-de-lia/457895)
- [24matins — IA bouleverse les bailleurs](https://www.24matins.fr/lintelligence-artificielle-bouleverse-le-quotidien-des-proprietaires-bailleurs-1399172)
