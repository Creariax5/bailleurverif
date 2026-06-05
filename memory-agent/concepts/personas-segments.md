---
name: Personas-segments
description: Segmentation users + intent distribution (locataire / bailleur / B2B) DILA-grounded, peuplé au fil des subscribers + signaux GSC
type: project
---

# Personas-segments — segmentation users BailleurVérif

> **Source décisive** : Florian brief inbox.md 2026-06-03T17:00Z item D (NEW concept), critic-61 prescription #1 ≥30 sub-personas DILA-grounded.
> **Statut** : v0 squelette 2026-06-05 run-445. Peuplé au fil mesure (subscribers_by_intent + GSC + funnel events + sub-personas confirmées par capture).
> **Trigger Phase 2** : ≥40% subscribers/humans qualifiés sur même persona = signal pivot conditionnel (cf `long-term-strategy.md`).

## Sources DILA-grounded (binding)

Chaque sub-persona ci-dessous est ancré dans un texte officiel français accessible via DILA (Direction de l'information légale et administrative) :
- **Loi 89-462** (1989) bail vide résidence principale + dérogations ALUR (mars 2014) bail meublé
- **Code de la construction et de l'habitation (CCH)** L.126-26-X (DPE F/G interdiction calendrier 2025/2028/2034 loi Climat 2021)
- **Décret 2015-650** + **arrêtés préfectoraux** (encadrement loyer zones tendues — Paris, Lyon, Lille, Plaine Commune, Est Ensemble, Bordeaux, Montpellier, Grenoble)
- **Code général des impôts (CGI)** art. 35 bis / 155 IV (LMNP/LMP statut fiscal)
- **CCH art. L.443** (HLM), **CCH art. L.631-7** (meublé tourisme), **Loi 1948** (rare baux historiques)

## A. Locataire (signal majoritaire à date — Bouygues pull-LLM + GSC #1+#3)

### A.1 Statut juridique du bail

| # | Sub-persona | Base légale | Signal Phase 1 |
|---|---|---|---|
| 1 | Locataire bail vide résidence principale (loi 89-462) | Loi 89-462 art. 3 | Majoritaire HumOps français (~85% parc privé) |
| 2 | Locataire bail meublé ALUR (loi 6 juillet 1989 art. 25-3+) | Décret 2015-981 | GSC #1 questions Reddit suggère contenu locataire-générique |
| 3 | Locataire bail mobilité (1-10 mois) | Loi ELAN 2018 art. 107 | Sub-segment étudiants/mobilité pro |
| 4 | Locataire colocation bail multi-locataires (clause solidarité) | Loi 89-462 art. 8-1 | Pain point clause solidarité majeur |
| 5 | Locataire HLM (statut locatif social) | CCH art. L.441 | Hors scope BailleurVérif (focus parc privé) |
| 6 | Locataire bail Loi 1948 | Loi 48-1360 1er sept 1948 | <2% parc, scope marginal |
| 7 | Locataire sous-locataire (autorisé/non-autorisé) | Loi 89-462 art. 8 | Sub-segment émergent plateformes |

### A.2 Géographie + encadrement loyer

| # | Sub-persona | Base légale | Signal Phase 1 |
|---|---|---|---|
| 8 | Locataire zone encadrement loyer (28 communes) | Décret 2015-650 + arrêtés | GSC #4 Villeurbanne / #5 Paris DRIHL signaux |
| 9 | Locataire zone tendue hors encadrement | Décret 2013-392 | Pré-encadrement, surveillance évolution loyer |
| 10 | Locataire zone détendue (95% territoire) | Hors décret | Majoritaire France hors métropoles |
| 11 | Locataire en quartier prioritaire ANRU | Loi 2014-173 | Spécificité aides + protection renforcée |

### A.3 Conformité technique du logement

| # | Sub-persona | Base légale | Signal Phase 1 |
|---|---|---|---|
| 12 | Locataire DPE G (interdit location depuis 01/01/2025) | CCH L.126-26 + loi Climat 2021 | Pain point chaud (GSC #3 long-tail spécifique) |
| 13 | Locataire DPE F (interdiction prévue 01/01/2028) | CCH L.126-26 | Pré-interdiction, vigilance travaux bailleur |
| 14 | Locataire DPE E (interdiction prévue 01/01/2034) | CCH L.126-26 | Horizon long |
| 15 | Locataire logement non-décent (loi 89-462 art. 6 + décret 2002-120) | Décret 2002-120 | Recours possible mais peu utilisé |
| 16 | Locataire logement insalubre/arrêté préfectoral | CSP L.1331 | Sub-segment minoritaire mais critique |

### A.4 Litiges récurrents (pain points BailleurVérif cat-3)

| # | Sub-persona | Base légale | Signal Phase 1 |
|---|---|---|---|
| 17 | Locataire victime loyer abusif (dépassement plafond zone encadrée) | Décret 2015-650 + art. 17 loi 89-462 | Cat-3 template loyer-abusif live |
| 18 | Locataire victime indexation IRL erronée | Loi 89-462 art. 17-1 | Calcul rétroactif 3 ans possible |
| 19 | Locataire victime dépôt garantie non restitué | Loi 89-462 art. 22 (M+2 délai légal) | Cat-3 template depot-garantie live |
| 20 | Locataire victime travaux non réalisés (engagements bail) | CCC art. 1719 | LRAR + saisine ADIL |
| 21 | Locataire préavis contesté (1m ZTL vs 3m hors ZTL) | Loi 89-462 art. 15 + décret 2013-392 | Sub-segment fréquent mais peu connu |
| 22 | Locataire état des lieux contesté (sortie) | Loi 89-462 art. 3-2 | Litige post-bail très fréquent |
| 23 | Locataire charges récupérables contestées | Décret 87-712 | Liste limitative charges récupérables |
| 24 | Locataire trouble jouissance (voisinage, bailleur intrusif) | CCC art. 1719 + 1724 | Recours civil possible |
| 25 | Locataire victime représailles bailleur post-signalement | Loi 89-462 art. 4 | Sub-segment fragile, sous-mesuré |

## B. Bailleur (signal émergent — sogibim subscriber dpe-bailleur via pull-LLM + GSC #2+#5)

### B.1 Statut juridique du bailleur

| # | Sub-persona | Base légale | Signal Phase 1 |
|---|---|---|---|
| 26 | Bailleur particulier mono-bien (résidence locative unique) | Loi 89-462 + IR foncier | Majoritaire parc privé FR |
| 27 | Bailleur particulier multi-bien 2-5 biens | Idem | **Persona cible Phase 2 modèle A** (cf long-term-strategy.md) |
| 28 | Bailleur particulier multi-bien 5+ biens (>seuil pro) | CGI art. 155 IV | Pré-LMP, comptabilité spécifique |
| 29 | Bailleur SCI (à l'IR) gestion personnelle/familiale | CGI art. 8 | Optimisation fiscale + transmission |
| 30 | Bailleur SCI à l'IS (rare en location résidentielle) | CGI art. 206 | Sub-segment marginal |
| 31 | Bailleur LMNP (meublé non-professionnel <€23k/an) | CGI art. 155 IV | Statut fiscal majoritaire meublé |
| 32 | Bailleur LMP (meublé professionnel >€23k recettes + >50% revenus) | CGI art. 155 IV | Statut pro, comptabilité BIC |
| 33 | Bailleur indivision (succession non-partagée) | CCC art. 815+ | Sous-segment complexe (signatures multiples) |
| 34 | Bailleur usufruitier (démembrement) | CCC art. 578+ | Spécificité juridique |

### B.2 Conformité travaux + DPE (pain point Phase 2 chaud)

| # | Sub-persona | Base légale | Signal Phase 1 |
|---|---|---|---|
| 35 | Bailleur DPE G interdit depuis 01/01/2025 (urgence travaux) | CCH L.126-26 | **GSC #2 aides bailleur 7imp** + sogibim subscriber |
| 36 | Bailleur DPE F travaux 2025-2028 prévisionnel | CCH L.126-26 | Horizon 3 ans, planification |
| 37 | Bailleur DPE E horizon 2034 | CCH L.126-26 | Horizon long, surveillance |
| 38 | Bailleur primo (1ère location, méconnait obligations) | Loi 89-462 | Sub-segment vulnérable erreurs |
| 39 | Bailleur post-travaux MaPrimeRénov + CEE | Décret 2020-26 + loi POPE 2005 | Aides multi-couches complexes |

### B.3 Conformité location

| # | Sub-persona | Base légale | Signal Phase 1 |
|---|---|---|---|
| 40 | Bailleur en zone encadrement loyer (compliance check) | Décret 2015-650 | **GSC #5 DRIHL** = persona expert |
| 41 | Bailleur en zone tendue hors encadrement (vigilance évolution) | Décret 2013-392 | Pré-encadrement risque |
| 42 | Bailleur meublé tourisme (Airbnb, changement usage) | CCH L.631-7 | Sub-segment grandes villes |

## C. B2B (signal hypothétique — non encore mesuré, à valider)

| # | Sub-persona | Base légale | Signal Phase 1 |
|---|---|---|---|
| 43 | Agence immobilière indépendante (mandat gestion locative) | Loi Hoguet 1970 | Inbound non mesuré (0/T+30j) |
| 44 | Agence franchise (Foncia, Century 21, Orpi, Stéphane Plaza) | Loi Hoguet 1970 | Volume potentiel élevé |
| 45 | Syndic copropriété (parties communes vs privatives) | Loi 65-557 | Hors scope direct mais B2B adjacent |
| 46 | Notaire (transactions location + droit logement) | Décret 71-942 | Adjacent, peu probable user récurrent |
| 47 | ADIL (conseil personnalisé bailleur/locataire) | Décret 2006-1117 | Concurrent + partenaire potentiel |
| 48 | Avocat droit logement / huissier | Hors scope SaaS | Référent recours contentieux |
| 49 | Journaliste / chercheur logement | Hors SaaS | Cible observatoire data + presse |
| 50 | Élu local / agent collectivité (politique logement) | Hors SaaS | Cible observatoire data + transparence |
| 51 | Association locataires (CNL, CLCV, CGL, Droit au Logement) | Loi 1901 | Distribution partner potentiel |
| 52 | Plateforme tech logement (Locservice, PAP, Hestia) | Hors SaaS | Concurrent direct + intégration data possible |

## Signal capture Phase 1 (mesure live)

Source = `/api/subscribe` field `intent_signal` (server run-433 + UI dropdown `/dpe-fiabilite.html` run-439 + `/aides-financieres-bailleur-2026.html` run-441).

Enum `intent_signal` actuellement déployé :
- `loyer-trop-cher` (mapping → A.4 #17)
- `arnaque-suspecte` (mapping → A.4 multiple)
- `litige-en-cours` (mapping → A.4 multiple)
- `curiosite` (non-segmentable)
- `bailleur-conformite` (mapping → B.2 ou B.3 ambigü)
- `bailleur-multi-bien` (mapping → B.1 #27) — NEW run-441 audit-44 cible
- `bailleur-proprio-unique` (mapping → B.1 #26) — NEW run-441 audit-44 cible
- `autre`

**État au 2026-06-05T07:42Z** : `subscribers_by_intent = {'unset': 1}` (sogibim run-431 ante-deploy enum). 0 capture sub-persona qualifiée.

## Distribution attendue post-Phase 1 (hypothèses à valider)

Avec N=100 subscribers cible Phase 2 :
- **A. Locataire** : ~50-65% (signal pull-LLM Bouygues + GSC #1+#3+#4 locataire-side)
- **B. Bailleur** : ~25-40% (signal sogibim + GSC #2+#5)
- **C. B2B** : <5% (très peu probable Phase 1)
- **Unset/curiosite** : ~5-10% (noise)

Si **B > 40%** ⇒ trigger Phase 2 modèle A (bailleur multi-bien) plus probable.
Si **A.4 #17/#18/#19 > 40% cumul** ⇒ trigger Phase 2 modèle C (locataire-victime premium "monter mon dossier").
Si **C ≥ 3 inbound** ⇒ trigger Phase 2 modèle B (B2B agences/syndics).

## Méthodologie update (binding)

À chaque NEW subscriber + GSC weekly batch :
1. Map `intent_signal` au sub-persona ci-dessus (A.X / B.X / C.X numbered)
2. Update `kpis/snapshot-current.md` champ `subscribers_by_persona_segment`
3. Si concentration émerge ≥30% sur 1 sub-persona ⇒ flag inbox HEAD Florian (signal Phase 2 anticipé)
4. Si GSC NEW query signal NEW sub-persona non-listé ⇒ append section ici + update enum `intent_signal` côté UI

## Anti-pattern à éviter

- ❌ **Pivoter Phase 2 sur N=1** (sogibim seul) — itérer N≥10 minimum par sub-persona avant claim
- ❌ **Inventer sub-personas non-DILA-grounded** — chaque ligne doit citer texte légal vérifiable
- ❌ **Confondre intent_signal capturé vs persona réelle** — capture = déclaré, persona réelle = inférée funnel + comportement
- ❌ **Spam sub-personas marginaux** (Loi 1948, HLM) — focus parc privé encadrable

## Risques persona-analyse

1. **Biais signal pull-LLM** : Applebot + ChatGPT capture surface bailleur-side (intent_signal UI placées sur pages bailleur). Locataires peut-être sous-représentés mesure.
2. **Sample contamination bot** : H5 traffic-signals.md = 76% BOT direct. Filtrer `direct_humans_after_ua_filter_lifetime` avant claims persona.
3. **Self-fulfilling prophecy** : ship plus pages bailleur ⇒ plus signal bailleur ⇒ Phase 2 bailleur. Vérifier locataire-side pages reçoivent intent_signal capture parité.
