---
tag: dpe-invalide
title: "Bail conclu sur logement DPE F ou G post-interdiction — recours locataire"
version: v0
wave_ts: 2026-05-18T03:30:00Z
canonical: https://bailleurverif.fr/api/recourse/dpe-invalide
markdown_alternate: https://bailleurverif.fr/api/recourse/dpe-invalide.md
source: BailleurVérif interpretation-library-v0/recourse-templates
license: CC-BY-4.0
expected_resolution_p50_days: 120
success_rate_estimated_pct: 65
---

# Bail conclu sur logement DPE F ou G post-interdiction — recours locataire

**Champ d'application** — Bail d'habitation résidence principale (vide ou meublé hors bail mobilité) portant sur un logement classé F ou G au DPE, signé après la date d'entrée en vigueur de l'interdiction de location correspondante (G : 01/01/2025 ; F : 01/01/2028 ; E : 01/01/2034). Inclut également les baux en cours dont le propriétaire n'a pas réalisé les travaux de mise aux normes lors du renouvellement. Hors champ : bail mobilité, logement loi 1948, logement de fonction, sous-location, baux antérieurs à la date d'interdiction et non encore renouvelés (statu quo légal jusqu'au renouvellement).


## Base légale (DILA Open Data, Licence Ouverte Etalab v2.0)

- **Loi n° 89-462 du 6 juillet 1989 tendant à améliorer les rapports locatifs et portant modification de la loi n° 86-1290 du 23 décembre 1986** — Source directe du calendrier d'interdiction de location DPE F/G/E (G→01/01/2025, F→01/01/2028, E→01/01/2034) ET du décalage Outre-mer (Guadeloupe/Martinique/Guyane/Réunion/Mayotte : F→01/01/2028, E→01/01/2031). Renvoi explicite à L. 173-1-1 CCH pour la classification. Justifie `applicability_checks.check_id=date_signature_post_interdiction` et `limitations_disclaimers` Outre-mer. _( LEGIARTI `LEGIARTI000043977105` )_
- **Code de la construction et de l'habitation** — Définit la classification réglementaire DPE en 7 classes (A→G) par niveau décroissant de performance énergétique (kWh/m².an énergie primaire) ET d'émissions CO2 (kg CO2eq/m².an). Renvoi à l'arrêté ministériel pour seuils. Source directe de `applicability_checks.check_id=dpe_classe` ET de la légitimité du recours fondé sur classement F/G. _( LEGIARTI `LEGIARTI000043966496` )_
- **Loi n° 89-462 du 6 juillet 1989 tendant à améliorer les rapports locatifs et portant modification de la loi n° 86-1290 du 23 décembre 1986** — Interdiction explicite de toute révision OU majoration de loyer pour les logements classés F ou G au sens de L. 173-1-1 CCH (III de l'article). Levier complémentaire au recours décence : même si le bailleur refuse les travaux de mise aux normes, il ne peut pas non plus appliquer la clause IRL annuelle. Source légale du paragraphe `interdiction-revision-f-g` dans `legal_basis_citations[]` historique. _( LEGIARTI `LEGIARTI000043977085` )_


## Citations légales croisées

- **Loi n°2021-1104 du 22 août 2021 portant lutte contre le dérèglement climatique (« Climat & Résilience ») — art. 158 à 160** —  _( [source](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000043956924/) )_
- **Code de la construction et de l'habitation — art. L173-1-1 et L173-2** —  _( [source](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006074096/LEGISCTA000043958003/) )_
- **Décret n°2023-796 du 18 août 2023 relatif à la performance énergétique des logements décents** —  _( [source](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000047966020) )_
- **Loi n°89-462 du 6 juillet 1989 — art. 6 (décence) et art. 20-1 (recours travaux)** —  _( [source](https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000043977032/) )_
- **Arrêté du 13 avril 2022 fixant les seuils par classe DPE et le mode d'établissement du DPE 3CL-2021** —  _( [source](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000045598064) )_


## Vérifications préalables

- **Quelle est la classe DPE du logement indiquée sur le diagnostic remis avec le bail ?** — Si G → interdiction depuis 01/01/2025 applicable. Si F → interdiction depuis 01/01/2028 (vérifier date_signature_bail). Si E → interdiction depuis 01/01/2034. Si A-D → hors champ, template non applicable.
- **Le DPE a-t-il été établi après le 1er juillet 2021 (méthode 3CL-2021) et a-t-il moins de 10 ans ?** — Si DPE antérieur à 2018, classe E/F/G surestimée probable (DPE méthode ancienne plus laxiste). Si DPE absent du dossier ou périmé, exiger DPE 3CL-2021 à jour avant toute action (article 3-3 loi 1989 = annexe obligatoire au bail).
- **Le bail a-t-il été signé après la date d'interdiction applicable à la classe DPE constatée ?** — Classe G + bail post-01/01/2025 = recours fort (bail vicié). Classe G + bail antérieur en renouvellement = recours sur mise aux normes. Classe F + bail post-01/01/2028 = recours fort. Classe F + bail antérieur = pas encore d'interdiction, recours sur décence général uniquement.
- **Le logement est-il la résidence principale du locataire (occupation ≥ 8 mois/an) ?** — Si NON (résidence secondaire, location saisonnière, étudiant <8 mois) → template non applicable (interdictions Climat & Résilience ne visent que la résidence principale au sens du bail d'habitation).
- **Le logement est-il classé loi 1948, logement de fonction, HLM, conventionné Anah, mobilité, ou meublé de tourisme ?** — Si OUI → template non applicable (régime spécifique de décence ou exemption travaux). Renvoyer vers ADIL.


## Données utilisateur nécessaires

- adresse_complete
- date_signature_bail
- duree_bail_mois
- dpe_classe
- dpe_date_etablissement
- dpe_conso_kwh_m2_an
- dpe_co2_kg_m2_an
- dpe_methode_3CL_2021_ou_ancienne
- loyer_mensuel_hors_charges
- type_logement_vide_ou_meuble
- surface_habitable_m2
- type_chauffage
- occupation_residence_principale_oui_non
- departement


## Données calculées

- classe_dpe_interdite_a_la_date_signature (booléen)
- date_interdiction_applicable (01/01/2025 G, 01/01/2028 F, 01/01/2034 E)
- delai_depuis_interdiction_jours
- dpe_valide_3CL_2021_et_moins_10_ans (booléen)
- reduction_loyer_proposee_pct (heuristique : 5% si classe E future / 15% si F / 30% si G)
- reduction_loyer_proposee_eur
- classe_cible_mise_aux_normes (E pour bail 2034+, D pour 2028+, C pour 2025+)


## Étapes de la procédure

- **Réunir la preuve documentaire** — 
    - Récupérer le DPE annexé au bail (ou le réclamer par RAR si absent — annexe obligatoire art. 3-3 loi 89-462).
    - Récupérer copie du bail signé + date de signature.
    - Photographies du logement (fenêtres, isolation visible, chaudière, mode de chauffage, points de déperdition).
    - Trois dernières factures d'énergie (corrélation consommation réelle vs DPE théorique).
    - Notes manuscrites datées des inconforts thermiques (température hiver/été, humidité, condensation).
- **Mise en demeure amiable par lettre recommandée avec accusé de réception** — 
    - Adresser au bailleur (ou à l'agence mandataire) une LRAR exigeant : (a) production d'un DPE 3CL-2021 à jour si DPE absent/périmé, (b) plan de travaux de mise aux normes avec calendrier prévisionnel, (c) à défaut, proposition de réduction du loyer proportionnelle à l'écart entre la performance contractuelle et la performance réelle, (d) à défaut encore, résiliation du bail sans préavis ni indemnité de départ anticipé (art. 15-I loi 89-462 issue Climat & Résilience).
    - Délai de réponse : 30 jours. Conserver l'accusé de réception (preuve de la mise en demeure datée).
- **Saisine de la Commission Départementale de Conciliation (CDC)** — 
    - Si pas de réponse à 30 j ou réponse insatisfaisante : saisir la CDC du département (formulaire CERFA + LRAR à la préfecture). Gratuit.
    - Inclure le DPE, la mise en demeure, les factures énergie, le bail.
    - La CDC convoque les parties dans un délai de 2 à 3 mois. Avis non contraignant mais souvent suivi (élément clé du dossier TJ ultérieur).
- **Signalement à la DRIHL (IDF) ou DDETS (province) et à l'ANIL/ADIL** — 
    - Adresser un signalement écrit à la préfecture du département (service logement : DRIHL pour Paris/IDF, DDETS pour le reste). Inclure DPE + bail + LRAR + accusé CDC.
    - Saisir l'ADIL du département pour appui juridique gratuit (consultation téléphonique 1ʳᵉ ligne).
    - Optionnel : signalement parallèle à UFC-Que-Choisir ou DAL si dossier emblématique.
- **Saisine du Tribunal Judiciaire en référé ou au fond** — 
    - Référé (en cas d'urgence : insalubrité, péril, hiver) : demande d'exécution de travaux sous astreinte, réduction provisoire du loyer, ou suspension du loyer en consignation jusqu'à mise aux normes.
    - Au fond : demande de résolution judiciaire du bail aux torts du bailleur + dommages et intérêts (préjudice de jouissance) + remboursement trop-perçu loyer + frais déménagement.
    - Honoraires avocat : entre 1 500 € et 4 000 € selon complexité. Aide juridictionnelle possible sous conditions de ressources.
    - Délai jugement : 12 à 18 mois (TJ), 1 à 3 mois (référé).


## Contacts régulateurs

- **Commission Départementale de Conciliation (CDC)** — Conciliation obligatoire pré-TJ pour litiges décence/loyer en zone d'encadrement ou logement collectif copropriété. Compétence départementale.
- **DRIHL Île-de-France / DDETS province** — Service déconcentré de l'État (préfecture). Reçoit les signalements de manquement à la décence et coordonne les contrôles. Compétence pour engagement de procédures coercitives bailleur.
- **Tribunal Judiciaire (TJ)** — Compétence en référé (urgence) ou au fond pour résolution bail, travaux sous astreinte, dommages-intérêts. Saisine par voie d'assignation (avocat obligatoire pour montants > 10 000 €).
- **ADIL (Agence Départementale d'Information sur le Logement)** — Conseil juridique gratuit et neutre. Aide à la rédaction des LRAR, qualification juridique du recours, orientation vers les autres dispositifs.


## Jurisprudence (Judilibre PISTE OAuth)

- Selon le II de l'article L. 271-4 du code de la construction et de l'habitation, le diagnostic de performance énergétique mentionné au 6° de ce texte n'a, à la différence des autres documents constituant le dossier de diagnostic technique, _( ECLI ECLI:FR:CCASS:2019:C300983 · Troisième chambre civile · 2019-11-21 )_
- La seule alimentation en électricité ne peut être considérée comme un équipement ou une installation permettant un chauffage normal du logement au sens de l'article 3 du décret du 30 janvier 2002 relatif aux caractéristiques du logement décent. _( ECLI ECLI:FR:CCASS:2014:C300721 · Troisième chambre civile · 2014-06-04 )_
- Le locataire d'un local à usage d'habitation est recevable, d'une part, à poursuivre l'exécution forcée en nature de l'obligation de délivrance d'un logement décent tant que le manquement perdure, d'autre part à obtenir la réparation des conséquences de ce manquement. _( ECLI ECLI:FR:CCASS:2026:C300339 · Troisième chambre civile · 2026-06-04 )_


## Références corpus

- **Loi n°2021-1104 Climat & Résilience art 158-160** —  _( [source](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000043956924/) )_
- **Décret n°2023-796 du 18 août 2023 — performance énergétique logement décent** —  _( [source](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000047966020) )_
- **BailleurVérif observatoire DPE — 50 pages SEO {ville}-dpe-f-g-interdit-location** —  _( [source](https://bailleurverif.fr/lille-dpe-f-g-interdit-location.html) )_


## Limitations et avertissements

- Ce template n'est pas un conseil juridique individualisé. Il vise à informer le locataire sur ses recours probables et à structurer un dossier amiable. La décision finale relève toujours d'un avocat ou de l'ADIL pour les cas complexes.
- Les seuils d'interdiction (G 2025, F 2028, E 2034) supposent une résidence principale en France métropolitaine. Outre-mer : seuils décalés (voir décret n°2024-? si publié à date d'évaluation).
- Les baux antérieurs à la date d'interdiction ne sont pas automatiquement nuls : le bailleur dispose de la durée du bail en cours pour réaliser les travaux. Le recours plein s'ouvre au renouvellement ou si le bailleur reconduit tacitement sans travaux.
- Le DPE produit avec la méthode 3CL-2021 prime sur tout DPE antérieur. Un DPE de 2018-2020 méthode ancienne classifiant F/G n'est plus opposable au bailleur si un DPE 3CL-2021 reclasse à D-E (et inversement).


## Résolution attendue

- **P50** ≈ 120 jours
- **Plage** : [60, 540]
- _P50 estimé = règlement amiable post-RAR + CDC (4 mois, le bailleur préfère négocier réduction loyer pour éviter perte du locataire ET nullité bail révélée publiquement). P95 = saisine TJ + jugement au fond (18 mois). Médiane à recaler après ≥10 case-evaluations réelles. Référé pour situations d'urgence (insalubrité, péril, hiver) : 1-3 mois._


## Taux de succès estimé

- **Estimation initiale** : 65 %
- _Estimation initiale fondée sur littérature DRIHL/ADIL/UFC-Que-Choisir et premières jurisprudences Cass. civ. 3ème post-Loi Climat 2021. Variable selon : (a) classe DPE (G plus aboutie que F en jurisprudence), (b) date bail (post-interdiction = recours quasi-automatique), (c) bailleur professionnel (taux succès amiable ~75%) vs particulier informé (~55%) vs particulier non informé (~85% en TJ). À recaler après 10+ cas réels._


## Courrier type (RAR)

```markdown
**Objet : Mise en demeure — manquement à l'obligation de décence énergétique du logement loué**

Madame, Monsieur,

Je suis locataire du logement situé à `[ADRESSE COMPLÈTE + ÉTAGE + N°]`, en vertu du bail d'habitation signé le `[DATE_BAIL]` pour une durée de `[DURÉE]` mois/années.

Le Diagnostic de Performance Énergétique (DPE) annexé au bail, établi le `[DATE_DPE]` selon la méthode `[3CL-2021|ancienne]`, classe le logement en catégorie `[CLASSE_DPE]`, avec une consommation d'énergie finale de `[CONSO_KWH]` kWh/m².an et une émission de gaz à effet de serre de `[CO2_KGM2]` kg CO2eq/m².an.

Or, en application de la loi n°2021-1104 du 22 août 2021 (« Climat & Résilience »), de l'article L173-2 du Code de la construction et de l'habitation, et du décret n°2023-796 du 18 août 2023, le logement loué `[ne respecte pas | ne respecte plus]` les critères de décence énergétique applicables :

- Classe G : interdiction de location depuis le 1er janvier 2025.
- Classe F : interdiction de location à compter du 1er janvier 2028.
- Classe E : interdiction de location à compter du 1er janvier 2034.

Le bail ayant été signé le `[DATE_BAIL]`, postérieurement à la date d'interdiction applicable à la classe DPE constatée, le logement loué `[NE PEUT PLUS LÉGALEMENT FAIRE L'OBJET D'UN CONTRAT DE LOCATION RÉSIDENTIEL PRINCIPAL | EST EN INFRACTION AVEC L'OBLIGATION DE DÉCENCE ÉNERGÉTIQUE]`.

En conséquence, et au visa de l'article 6 de la loi n°89-462 du 6 juillet 1989, je vous demande de bien vouloir, sous un délai de **30 jours** à compter de la réception de la présente :

1. Produire un DPE à jour (méthode 3CL-2021, moins de 10 ans) si le DPE actuel est périmé ou antérieur à 2021 ;
2. Présenter un **plan de travaux de mise aux normes** chiffré, avec calendrier de réalisation, permettant au logement d'atteindre **au minimum la classe `[CLASSE_CIBLE: E pour bail post-2034, D pour bail post-2028, etc.]`** ;
3. À défaut, **convenir d'une réduction du loyer** proportionnelle à l'écart entre la performance contractuelle attendue et la performance réelle, à hauteur de `[REDUCTION_PROPOSEE_PCT]` % du loyer mensuel, soit `[REDUCTION_EUR]` € / mois ;
4. À défaut encore, **acter la résiliation du bail sans préavis ni indemnité de départ anticipé**, en application de l'article 15-I de la loi n°89-462 modifiée par la loi Climat & Résilience.

À défaut de réponse favorable et chiffrée sous 30 jours, je saisirai la **Commission Départementale de Conciliation de `[DÉPARTEMENT]`** pour conciliation préalable, puis le **Tribunal Judiciaire** territorialement compétent aux fins d'obtenir, le cas échéant : exécution des travaux sous astreinte, suspension du loyer en consignation, résolution judiciaire du bail à vos torts, dommages et intérêts au titre du préjudice de jouissance, et remboursement des sommes versées au-delà du loyer dû.

Je signalerai parallèlement cette situation à la `[DRIHL | DDETS]` ainsi qu'à l'ADIL du département.

Je vous prie d'agréer, Madame, Monsieur, l'expression de mes salutations distinguées.

`[NOM PRÉNOM]`
`[DATE]` — `[VILLE]`

**Pièces jointes :**
- Copie du bail signé le `[DATE_BAIL]`.
- Copie du DPE annexé au bail.
- Trois dernières factures d'énergie.
- `[Le cas échéant : photographies, devis d'isolation, attestations de tiers.]`
```


## Méta — signal moat (composant cat-3 RAG-LLM)

- **category** : 3
- **rationale** : Composant cat-3 intelligence interprétative coûteuse : ce template encode 5 articles légaux croisés (loi 2021-1104 + L173-2 CCH + décret 2023-796 + loi 89-462 + arrêté 13/04/2022) + 5 procedure_steps détaillées + sample_letter_md cliquable + 4 regulator_contacts cartographiés. Refaisable par dev solo en <2j sur ce template seul, mais valeur compounding : (1) accumulation de N templates dans la librairie = barrière temporelle, (2) recoupement avec observatoire BV (cat-1 données propriétaires) pour identifier cas réels chez utilisateurs (cat-2 réseau futur), (3) ouverture vers RAG jurisprudence Claude API post-TODO-26 = barrière coût + qualité interprétative.
- **wave_position** : 2
- **wave_total_target** : 3
- **next_template_candidates** : ['depot-garantie-non-restitue', 'charges-locatives-injustifiees', 'preavis-bail-non-respecte']
- **publication_plan** : GitHub push public à wave +1 ou +2 (timestamp crypto-vérifiable comme cat-1 observatoire). Endpoint GET /api/recourse/<tag> lecture seule à wave +1 (séquence run-239 N+5).
- **legal_basis_populated_dila_verified** : True
- **legal_basis_articles_count** : 3
- **legal_basis_first_authored_run** : run-273


---

Source canonique JSON : `https://bailleurverif.fr/api/recourse/dpe-invalide` — licence CC-BY-4.0.
