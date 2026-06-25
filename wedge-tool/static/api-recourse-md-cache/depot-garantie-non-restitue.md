---
tag: depot-garantie-non-restitue
title: "Dépôt de garantie non restitué dans les délais ou retenu abusivement — recours locataire"
version: v0
wave_ts: 2026-05-18T04:00:00Z
canonical: https://bailleurverif.fr/api/recourse/depot-garantie-non-restitue
markdown_alternate: https://bailleurverif.fr/api/recourse/depot-garantie-non-restitue.md
source: BailleurVérif interpretation-library-v0/recourse-templates
license: CC-BY-4.0
expected_resolution_p50_days: 75
success_rate_estimated_pct: 80
---

# Dépôt de garantie non restitué dans les délais ou retenu abusivement — recours locataire

**Champ d'application** — Bail d'habitation résidence principale (vide ou meublé hors bail mobilité) régi par la loi n°89-462 du 6 juillet 1989, ayant donné lieu au versement d'un dépôt de garantie à l'entrée. Sortie effective du logement avec restitution des clés constatée. Cas couverts : (a) absence totale de restitution au-delà du délai légal (1 mois si EDL sortie = EDL entrée, 2 mois sinon) ; (b) retenue partielle non justifiée par devis/facture/courriers conformes ; (c) imputation de vétusté ou dégradation que le bailleur n'a pas démontrée ; (d) compensation avec charges non régularisées ou récupérables ; (e) défaut de versement de la majoration légale 10 %/mois en cas de retard. Hors champ : bail loi 1948, sous-location, location saisonnière, hébergement de courtoisie, dépôt versé à une caution (Visale) non récupéré par le bailleur.


## Base légale (DILA Open Data, Licence Ouverte Etalab v2.0)

- **Loi n° 89-462 du 6 juillet 1989 tendant à améliorer les rapports locatifs et portant modification de la loi n° 86-1290 du 23 décembre 1986** — 


## Citations légales croisées

- **Loi n°89-462 du 6 juillet 1989 — art. 22 (dépôt de garantie : plafond, délais, majoration de retard)** —  _( [source](https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000031060815/) )_
- **Décret n°87-712 du 26 août 1987 — liste des réparations locatives à charge du locataire** —  _( [source](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000874522/) )_
- **Décret n°2016-382 du 30 mars 2016 — modalités d'établissement de l'état des lieux** —  _( [source](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000032347631) )_
- **Code civil — art. 1731 (présomption en l'absence d'état des lieux)** —  _( [source](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006442930/) )_
- **Code de procédure civile — art. R. 211-3-22 et suiv. (juge des contentieux de la protection, procédure simplifiée ≤ 5 000 €)** —  _( [source](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000041615528/) )_


## Vérifications préalables

- **Un état des lieux de sortie contradictoire a-t-il été établi (signé des deux parties, daté, avec inventaire pièce par pièce) ?** — Si OUI et EDL sortie ≡ EDL entrée → délai restitution = 1 mois. Si OUI et différences notées → délai = 2 mois et retenues envisageables. Si NON ou EDL sortie non contradictoire → présomption art. 1731 favorable au locataire, recours fort.
- **Combien de mois se sont écoulés depuis la remise effective des clés et la fourniture d'une nouvelle adresse au bailleur ?** — Si <1 mois → attendre (sauf EDL sortie ≡ entrée). Si 1 à 2 mois → délai dépassé si EDL sortie ≡ entrée. Si >2 mois → délai dépassé dans tous les cas. Majoration légale 10 %/mois de retard cumulée pour chaque mois commencé.
- **Si le bailleur a opéré une retenue, l'a-t-il justifiée par devis chiffré et signé (ou facture acquittée) joint à la lettre de restitution ?** — Si retenue + devis/facture conformes + dégradation imputable (≠ vétusté + listée décret 87-712) → retenue valide pour ce poste. Si retenue sans devis/facture → retenue contestable intégralement. Si devis/facture inclut des postes non locatifs ou de vétusté → contestable au prorata.
- **Les dommages reprochés relèvent-ils d'une dégradation imputable au locataire ou d'une vétusté normale de l'usage du bien ?** — Vétusté = usure normale liée à l'usage et au temps (peintures défraîchies après 5+ ans, sols rayés par usage courant, joints noircis, etc.) → 0 imputation possible. Dégradation = négligence ou faute (trou non rebouché, vitre brisée, fait du locataire prouvé) → imputable mais valeur résiduelle à appliquer (grille de vétusté si annexée au bail).
- **La retenue est-elle motivée par une régularisation de charges non encore opérée par le bailleur ?** — Le bailleur peut retenir une provision raisonnable pour solde de charges en attente de l'arrêté annuel de copropriété (max 20 % du dépôt selon usage), mais doit régulariser sous 1 mois après réception de l'arrêté de charges. À défaut de régularisation dans l'année suivante, l'intégralité est due au locataire (art. 22 al. 3 loi 89-462).


## Données utilisateur nécessaires

- adresse_complete
- date_signature_bail
- loyer_mensuel_hors_charges_eur
- depot_garantie_initial_eur
- type_location_vide_ou_meuble
- date_remise_cles
- date_nouvelle_adresse_communiquee
- edl_entree_existe_oui_non
- edl_entree_contradictoire_oui_non
- edl_sortie_realise_oui_non
- edl_sortie_contradictoire_oui_non
- edl_sortie_identique_entree_oui_non
- retenue_montant_eur
- retenue_motif_bailleur
- devis_factures_jointes_oui_non
- postes_litige_description
- anciennete_logement_annees_au_depart
- grille_vetuste_annexee_bail_oui_non
- departement


## Données calculées

- delai_legal_restitution_jours (30 si EDL sortie = entrée, 60 sinon)
- date_limite_restitution_calculee
- delai_depasse_mois_arrondi_superieur
- majoration_legale_eur (10% loyer_hc * mois_retard)
- solde_du_avant_majoration_eur
- solde_du_total_avec_majoration_eur
- regime_art_1731_applicable_booleen (true si pas d'EDL d'entrée contradictoire)
- retenue_contestable_booleen (true si pas de devis/facture conformes)
- competence_juridiction (juge contentieux protection si <=5000€, TJ sinon)


## Étapes de la procédure

- **Constituer le dossier de preuves** — 
    - Récupérer une copie signée du bail (clause dépôt de garantie + montant).
    - Récupérer copie de l'EDL d'entrée et EDL de sortie (signés et datés des deux parties si contradictoires).
    - Garder copie horodatée du courrier ou e-mail de communication de la nouvelle adresse au bailleur (déclenche le délai légal).
    - Photographier le logement à la sortie (toutes les pièces, équipements, points sensibles), datées si possible (EXIF photo).
    - Récupérer la quittance ou le relevé bancaire du versement initial du dépôt de garantie (preuve du montant exact).
- **Mise en demeure amiable par lettre recommandée avec accusé de réception** — 
    - Adresser au bailleur (ou agence mandataire) une LRAR exigeant : (a) restitution intégrale du dépôt de garantie sous 15 jours, (b) versement de la majoration légale de 10 %/mois de retard pour chaque mois commencé depuis l'expiration du délai, (c) si retenues abusives : motivation détaillée pièce par pièce avec devis/facture joints, (d) à défaut, saisine du juge des contentieux de la protection.
    - Conserver l'accusé de réception et copie de la lettre (preuve datée de la mise en demeure).
- **Saisine de la Commission Départementale de Conciliation (CDC)** — 
    - Si pas de réponse satisfaisante à 15 j : saisir la CDC du département du logement par courrier (formulaire CERFA n°15728*01) ou lettre simple précisant : parties, montant en litige, pièces jointes (bail, EDL, LRAR, accusé de réception).
    - Gratuit. Convocation des deux parties sous 2 à 3 mois. Avis non contraignant mais opposable au juge ensuite.
    - Compétence CDC explicite sur le dépôt de garantie depuis la loi ALUR 2014 (avant : litige direct TJ).
- **Saisine du juge des contentieux de la protection (ex-tribunal d'instance)** — 
    - Si pas de conciliation ou refus du bailleur : déposer une requête au greffe du tribunal de proximité du lieu du logement (procédure simplifiée pour litiges ≤ 5 000 €). Pas d'avocat obligatoire.
    - Joindre : copie du bail, EDL entrée et sortie, LRAR + accusé, lettre CDC + avis CDC le cas échéant, photographies, devis/facture du bailleur si contestés, relevé bancaire versement dépôt.
    - Demandes : (a) restitution intégrale du dépôt de garantie, (b) majoration légale 10 %/mois capitalisée jusqu'à paiement effectif, (c) dommages-intérêts pour résistance abusive si bailleur de mauvaise foi caractérisée (art. 1240 Code civil), (d) frais de procédure (timbre fiscal, signification huissier le cas échéant).
- **Exécution forcée du jugement** — 
    - Une fois le jugement obtenu (titre exécutoire), le bailleur dispose d'un délai d'appel (1 mois) puis l'exécution est possible.
    - Si non-paiement spontané : signification du jugement par huissier (~80 €), puis saisie sur compte bancaire (saisie-attribution) ou saisie des loyers que le bailleur perçoit du locataire suivant.
    - Frais d'huissier et de saisie sont à la charge du bailleur condamné en sus du principal.


## Contacts régulateurs

- **Commission Départementale de Conciliation (CDC)** — Conciliation amiable obligatoire ou facultative (selon département) avant toute saisine du juge pour les litiges relatifs au dépôt de garantie. Compétence départementale, saisine LRAR gratuite.
- **Juge des contentieux de la protection (tribunal de proximité)** — Compétence exclusive pour litiges locatifs ≤ 5 000 € (procédure simplifiée). Saisine par requête au greffe sans avocat obligatoire. Audience contradictoire.
- **ADIL (Agence Départementale d'Information sur le Logement)** — Conseil juridique gratuit et neutre. Aide à la rédaction de la LRAR, qualification juridique du recours, calcul de la majoration légale, orientation procédure simplifiée.
- **UFC-Que Choisir locale** — Association de consommateurs habilitée à représenter les locataires adhérents devant le juge dans les litiges locatifs simples. Médiation amiable.


## Jurisprudence (Judilibre PISTE OAuth)

- Le bailleur d'un local d'habitation peut retenir, sur le dépôt de garantie versé par le locataire, le montant de l'indemnité d'occupation due par celui-ci lorsqu'il se maintient dans les lieux au-delà du terme du bail _( ECLI ECLI:FR:CCASS:2026:C300075 · Troisième chambre civile · 2026-01-29 · pourvoi n° 24-12.185 )_
- Il résulte de l'article 3-2 de la loi n° 89-462 du 6 juillet 1989 que, lorsque les parties n'ont pas été convoquées par lettre recommandée avec demande d'avis de réception adressée au moins sept jours à l'avance, celle qui a pris l'initiati _( ECLI ECLI:FR:CCASS:2023:C300706 · Troisième chambre civile · 2023-10-26 · pourvoi n° 22-20.183 · Publié au bulletin )_
- Il incombe au bailleur de justifier des sommes lui restant dues venant en déduction du montant du dépôt de garantie qu'il est tenu de restituer au locataire au départ des lieux loués. _( ECLI ECLI:FR:CCASS:2012:C300216 · Troisième chambre civile · 2012-02-15 · pourvoi n° 11-13.014 · Publié au bulletin )_


## Références corpus

- **Loi n°89-462 art. 22 — dépôt de garantie** —  _( [source](https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000031060815/) )_
- **Décret n°87-712 — réparations locatives** —  _( [source](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000874522/) )_
- **Service-Public.fr F31269 — Restitution dépôt de garantie** —  _( [source](https://www.service-public.fr/particuliers/vosdroits/F31269) )_
- **BailleurVérif corpus v0 SP.fr + ANIL — 10 fiches sourcées runs 240/241** —  _( [source](internal:data/interpretation-library-v0/recourse-templates/) )_


## Limitations et avertissements

- Ce template n'est pas un conseil juridique individualisé. Il vise à informer le locataire sur ses recours probables et à structurer un dossier amiable et contentieux. La décision finale relève toujours d'un avocat, d'une association habilitée ou de l'ADIL pour les cas complexes.
- Les délais et seuils (1 mois EDL identique / 2 mois EDL différent / majoration 10 %/mois / compétence juge des contentieux ≤ 5 000 €) s'appliquent aux baux régis par la loi du 6 juillet 1989. Hors champ : loi 1948, sous-location, baux commerciaux ou ruraux.
- La majoration légale 10 %/mois est due de plein droit, sans mise en demeure préalable (Cass. civ. 3ème, jurisprudence constante). Toute clause du bail qui l'écarterait ou la limiterait est réputée non écrite (art. 4 loi 89-462).
- Si le bailleur est en redressement ou liquidation judiciaire au moment de la demande de restitution, le locataire doit déclarer sa créance auprès du mandataire judiciaire dans les délais légaux (généralement 2 mois après publication BODACC).
- L'absence d'EDL d'entrée signé bascule la charge de la preuve sur le bailleur (art. 1731 Code civil). Si néanmoins l'EDL d'entrée existe mais que le bailleur invoque une dégradation absente du document, la présomption de bon état joue contre lui.


## Résolution attendue

- **P50** ≈ 75 jours
- **Plage** : [30, 360]
- _P50 = règlement amiable post-LRAR sous 30-90 jours (le bailleur préfère restituer pour éviter la majoration cumulée + frais de procédure). P95 = saisine juge + jugement + exécution forcée (12 mois). Cas exceptionnels (bailleur insolvable, indivision conflictuelle) : peut s'étirer 18+ mois._


## Taux de succès estimé

- **Estimation initiale** : 80 %
- _Estimation initiale fondée sur jurisprudence constante sur la charge de la preuve au bailleur (Cass. 3ᵉ civ. 15 févr. 2012, n° 11-13.014, Publié au bulletin ; nombreuses CA Paris/Versailles/Lyon 2018-2024), littérature ADIL et statistiques UFC-Que Choisir. Variable selon : (a) présence EDL d'entrée contradictoire (sans EDL d'entrée signé = ~95 % succès locataire via art. 1731 Code civil), (b) devis/facture conformes joints (sans devis = ~90 % retenue annulée), (c) bailleur professionnel (taux succès amiable ~70 % avant saisine) vs particulier informé (~50 %) vs particulier de mauvaise foi (~85 % en jugement)._


## Courrier type (RAR)

```markdown
**Objet : Mise en demeure — restitution du dépôt de garantie et application de la majoration légale de retard**

Lettre recommandée avec accusé de réception

Madame, Monsieur,

J'ai été locataire du logement situé `[ADRESSE COMPLÈTE + ÉTAGE + N° APPARTEMENT]`, en vertu du bail signé le `[DATE_SIGNATURE_BAIL]` pour un loyer mensuel hors charges de `[LOYER_HC_EUR]` €, et ayant donné lieu au versement d'un dépôt de garantie de `[DEPOT_GARANTIE_EUR]` € à la signature.

J'ai effectivement quitté le logement le `[DATE_REMISE_CLES]` avec remise des clés et établissement d'un état des lieux de sortie `[contradictoire et signé | non contradictoire]`. Je vous ai communiqué ma nouvelle adresse le `[DATE_NOUVELLE_ADRESSE_COMMUNIQUEE]`, ce qui a déclenché le délai légal de restitution.

En application de l'article 22 de la loi n°89-462 du 6 juillet 1989, vous étiez tenu de me restituer le dépôt de garantie dans un délai de :

- **1 mois** si l'état des lieux de sortie était identique à celui d'entrée ;
- **2 mois** dans le cas contraire ;

soit au plus tard le `[DATE_LIMITE_RESTITUTION]`. À ce jour, `[DELAI_DEPASSE_MOIS]` mois se sont écoulés au-delà de cette échéance, sans que le solde dû ne m'ait été versé `[entièrement | en totalité].

`[OPTIONNEL si retenue : Le solde retenu de `[RETENUE_EUR]` € est motivé par `[MOTIF_BAILLEUR]`. Or, à défaut de devis chiffré ou de facture acquittée joint à votre courrier, et au visa du décret n°87-712 du 26 août 1987 qui énumère limitativement les réparations à la charge du locataire, cette retenue ne peut être considérée comme justifiée. De plus, `[POSTES_VETUSTE]` relèvent de la vétusté normale et non d'une dégradation imputable.]`

En conséquence, je vous demande de bien vouloir, sous un délai de **15 jours** à compter de la réception de la présente :

1. Restituer la somme de `[SOLDE_DU_EUR]` € correspondant `[au dépôt de garantie intégral | au solde non justifié]` ;
2. Verser la majoration légale prévue à l'article 22 de la loi du 6 juillet 1989, soit 10 % du loyer mensuel hors charges (`[10PCT_LOYER_HC_EUR]` €) pour chaque mois commencé en retard, soit à ce jour `[MAJORATION_TOTALE_EUR]` € ;
3. À défaut, motiver précisément, pièce par pièce, vos retenues éventuelles par devis chiffrés et signés ou factures acquittées.

Le versement est à effectuer par virement bancaire sur le compte suivant :

```
Titulaire : [NOM PRÉNOM]
IBAN : [IBAN]
BIC : [BIC]
```

À défaut de réponse favorable et chiffrée sous 15 jours, je saisirai la **Commission Départementale de Conciliation de `[DÉPARTEMENT]`** pour conciliation préalable, puis, à défaut, le **juge des contentieux de la protection** (procédure simplifiée gratuite ≤ 5 000 €) aux fins d'obtenir, outre la restitution principale et la majoration légale, des dommages-intérêts pour résistance abusive caractérisée et la prise en charge des frais de procédure.

Je vous prie d'agréer, Madame, Monsieur, l'expression de mes salutations distinguées.

`[NOM PRÉNOM]`
`[DATE]` — `[VILLE]`

**Pièces jointes :**
- Copie du bail signé le `[DATE_SIGNATURE_BAIL]`.
- Copie de l'état des lieux d'entrée.
- Copie de l'état des lieux de sortie.
- Relevé bancaire attestant du versement du dépôt de garantie.
- Copie du courrier de communication de la nouvelle adresse daté du `[DATE_NOUVELLE_ADRESSE_COMMUNIQUEE]`.
- `[Le cas échéant : photographies de sortie du logement, devis contradictoires sur les postes litigieux.]`
```


## Méta — signal moat (composant cat-3 RAG-LLM)

- **category** : 3
- **rationale** : Composant cat-3 intelligence interprétative coûteuse : ce template encode 5 articles légaux croisés (art. 22 loi 89-462 + décret 87-712 + décret 2016-382 + art. 1731 Code civil + art. R. 211-3-22 CPC) + 5 procedure_steps détaillées de la preuve à l'exécution forcée + sample_letter_md substantiel 17 placeholders + 4 regulator_contacts cartographiés avec coûts et délais P50. La barrière technique seule est faible (refaisable par dev solo en <2j sur ce template isolé), mais valeur compounding : (1) accumulation cohérente de N templates dans la librairie = barrière temporelle + qualité de schéma normalisé, (2) recoupement avec observatoire BV cat-1 = identification cas réels chez utilisateurs (cat-2 réseau futur via /api/signalement et /api/notation-agence), (3) ouverture vers RAG jurisprudence Claude API post-TODO-26 = barrière coût + qualité interprétative supérieure.
- **wave_position** : 3
- **wave_total_target** : 3
- **next_template_candidates** : ['charges-locatives-injustifiees', 'preavis-bail-non-respecte', 'etat-lieux-abusif', 'reparations-bailleur-defaillant']
- **publication_plan** : Wake N+6 = endpoint GET /api/recourse/<tag> lecture seule + référence sitemap + redirect index. Wake N+7+ = git push interpretation-library-v0/ pour timestamp public GitHub crypto-vérifiable (audit-trail compounding moat-signal). Wake N+8+ = wave +1 : enrichissement jurisprudence_refs ≥3 décisions / template + lien LégiFrance Cassation.
- **threshold_3templates_3substantif_atteint** : True
- **threshold_3templates_endpoint_remaining** : True


---

Source canonique JSON : `https://bailleurverif.fr/api/recourse/depot-garantie-non-restitue` — licence CC-BY-4.0.
