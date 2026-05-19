---
tag: loyer-abusif
title: "Loyer abusif en zone d'encadrement — recours locataire"
version: v0
wave_ts: 2026-05-18T03:00:00Z
canonical: https://bailleurverif.fr/api/recourse/loyer-abusif
markdown_alternate: https://bailleurverif.fr/api/recourse/loyer-abusif.md
source: BailleurVérif interpretation-library-v0/recourse-templates
license: CC-BY-4.0
expected_resolution_p50_days: 90
success_rate_estimated_pct: 60
---

# Loyer abusif en zone d'encadrement — recours locataire

**Champ d'application** — Bail d'habitation résidence principale (logement vide ou meublé hors bail mobilité), commune située en zone tendue avec encadrement du niveau des loyers actif (Paris, Est Ensemble, Plaine Commune, Bordeaux, Grenoble-Alpes Métropole partiel, Lille/Hellemmes/Lomme, Lyon/Villeurbanne, Montpellier, Pays Basque). Hors champ : logements loi de 1948, conventionnés Anah, HLM, meublés de tourisme, sous-locations.


## Base légale (DILA Open Data, Licence Ouverte Etalab v2.0)

- **Loi n° 89-462 du 6 juillet 1989 tendant à améliorer les rapports locatifs et portant modification de la loi n° 86-1290 du 23 décembre 1986** — Champ d'application : définit la résidence principale (≥ 8 mois/an), exclut logements-foyers, meublés (titre Ier bis), bail mobilité (titre Ier ter), logements de fonction, dispositif occupation temporaire L. 2018-1021. _( LEGIARTI `LEGIARTI000047900014` )_
- **Loi n° 89-462 du 6 juillet 1989 tendant à améliorer les rapports locatifs et portant modification de la loi n° 86-1290 du 23 décembre 1986** — Révision annuelle du loyer plafonnée à l'IRL (I). Travaux d'amélioration permettent majoration explicite contractualisée (II). **Interdiction de toute révision ET majoration pour logements DPE F ou G au sens de l'article L. 173-1-1 du CCH (III)**. Source légale directe de `applicability_checks.check-5-dpe-f-g`. _( LEGIARTI `LEGIARTI000043977085` )_
- **Loi n° 89-462 du 6 juillet 1989 tendant à améliorer les rapports locatifs et portant modification de la loi n° 86-1290 du 23 décembre 1986** — Exclusions périmètre : (I) logements HLM hors convention L. 831-1 CCH exclus de divers articles dont 15-18 (incluant 17-1) ; (II) logements loi 1948 chapitre III ; (III) HLM conventionnés L. 831-1 CCH partiellement exclus (sauf I de 17-1 maintenu). Source légale de `scope` du template (hors HLM/1948/conventionné). _( LEGIARTI `LEGIARTI000038834701` )_


## Citations légales croisées

- **Loi n° 89-462 du 6 juillet 1989 — article 17** — Fixation et révision du loyer en zone non tendue (principe de liberté contractuelle), encadrement légal en zone tendue, modalités complément de loyer. _( [source](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000038814935/) )_
- **Loi n° 89-462 du 6 juillet 1989 — article 17-1** — Plafonnement de l'augmentation annuelle de loyer à l'IRL Insee (Indice de Référence des Loyers). Calcul : nouveau loyer = loyer actuel × (IRL trim. réf. année N / IRL trim. réf. année N-1). _( [source](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000038814917/) )_
- **Loi n° 89-462 du 6 juillet 1989 — article 25-9** — Encadrement expérimental du niveau des loyers en zone tendue (plafond = loyer de référence majoré × surface). Amende administrative pour non-respect : jusqu'à 5 000 € (personne physique) / 15 000 € (personne morale). _( [source](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000041419993/) )_
- **Loi n° 2026-103 du 19 février 2026 (loi Jeanbrun)** — Cadre actualisé 2026 fixation/révision loyer + sanctions encadrement. Référence locale BailleurVérif. _( [source](https://www.legifrance.gouv.fr/loda/id/LEGITEXT00026103/) )_
- **Interdiction de révision loyer pour logements DPE F/G** — Pour tout bail signé/renouvelé/tacitement reconduit depuis le 24 août 2022 (métropole) ou 1er juillet 2024 (DROM), un logement classé F ou G sur le DPE ne peut PAS faire l'objet d'une révision annuelle de loyer, même avec clause IRL contractuelle. _( [source](https://www.service-public.fr/particuliers/vosdroits/F1311) )_


## Vérifications préalables

- **La commune est-elle classée en zone tendue avec encadrement du niveau des loyers actif ?** — OUI si commune appartient à : Paris, Est Ensemble (9 communes), Plaine Commune (9 communes), Bordeaux, Grenoble-Alpes Métropole (liste partielle), Lille/Hellemmes/Lomme, Lyon/Villeurbanne, Montpellier, Pays Basque (24 communes). Sinon : encadrement évolution (relocation/renouvellement) possible mais PAS encadrement niveau, recours différent.
- **Le logement est-il loué comme résidence principale du locataire (ou bail mobilité) ?** — OUI requis. NON exclut le périmètre encadrement (meublés tourisme, secondaires hors résidence).
- **Le loyer mensuel hors charges (loyer de base) dépasse-t-il le loyer de référence majoré applicable (€/m² × surface habitable) ?** — Si oui : prima facie irrégularité encadrement. Calcul = surface habitable (m²) × loyer_ref_majoré (€/m²) selon arrêté préfectoral en vigueur à la date de signature/renouvellement.
- **Le bail contient-il un complément de loyer mentionné explicitement (caractéristiques exceptionnelles de localisation/confort) ?** — Si oui : le complément doit être justifié par des caractéristiques exceptionnelles et le bail doit les mentionner. Caractéristiques disqualifiantes (interdisent complément) : sanitaires palier, humidité murs, DPE F/G, mauvaise isolation thermique, fenêtres non étanches, évacuation eau défectueuse, électricité dégradée, vis-à-vis <10m, mauvaise exposition.
- **Le DPE du logement est-il classé F ou G ?** — Si oui ET bail signé/renouvelé depuis 24/08/2022 (métropole) : (1) interdiction de révision annuelle, même si clause IRL ; (2) complément de loyer interdit ; (3) DPE G interdit à la location depuis 2025 (renouvellements non autorisés) ; (4) DPE F interdit à la location à partir de 2028.


## Données utilisateur nécessaires

- adresse_complete
- commune
- code_postal
- date_bail
- type_bail (vide|meuble|mobilite)
- surface_habitable_m2
- nb_pieces
- loyer_base_mensuel_eur
- complement_loyer_mensuel_eur
- charges_mensuelles_eur
- dpe_classe (A|B|C|D|E|F|G|non-renseigne)
- type_bailleur (particulier|agence|sci|professionnel)


## Données calculées

- loyer_ref_majore_applicable_eur_m2
- plafond_calcule_mensuel_eur
- ecart_eur
- ecart_pct
- remboursement_12_mois_eur
- is_complement_loyer_justifiable_bool
- is_dpe_blocking_revision_bool


## Étapes de la procédure

- **Étape 1 — Constituer la preuve** — 
    - Récupérer copie du bail signé (clauses loyer + complément + IRL).
    - Récupérer copie DPE du logement (date + classe énergétique).
    - Récupérer 3 dernières quittances de loyer (loyer base + charges détaillées).
    - Calculer écart constaté : loyer_payé − (surface × loyer_référence_majoré). Conserver capture de l'arrêté préfectoral en vigueur à la date du bail.
- **Étape 2 — Lettre amiable RAR au bailleur** — 
    - Envoyer courrier recommandé avec accusé de réception (RAR) au bailleur (ou agence mandataire) demandant : (a) régularisation du loyer au plafond légal pour les mois à venir, (b) remboursement des sommes trop perçues sur 12 derniers mois (prescription quinquennale).
    - Délai de réponse raisonnable : 1 mois calendaire.
- **Étape 3 — Saisine Commission Départementale de Conciliation (CDC)** — 
    - Si pas de réponse / refus du bailleur sous 1 mois, saisir CDC du département (gratuit, écrit, sous 2 mois suite refus bailleur).
    - Joindre : bail, DPE, quittances, lettre RAR + accusé, calcul écart, copie de l'arrêté préfectoral.
    - Audience CDC sous 2-4 mois en moyenne (variable selon préfecture).
- **Étape 4 — Saisine préfet — sanction administrative encadrement** — 
    - Si CDC n'aboutit pas à régularisation OU pour signaler infraction encadrement : signaler au préfet (DRIHL en Île-de-France, DDETS en province) qui peut prononcer amende administrative jusqu'à 5 000 € (PP) / 15 000 € (PM).
    - Procédure indépendante de la conciliation, peut être menée en parallèle.
- **Étape 5 — Saisine tribunal judiciaire** — 
    - Si conciliation CDC échoue : saisine tribunal judiciaire (TJ) du lieu de situation de l'immeuble pour : (a) fixation judiciaire du loyer au plafond, (b) restitution du trop-perçu, (c) éventuels dommages-intérêts.
    - Procédure : 6-18 mois selon juridiction. Représentation avocat non obligatoire mais conseillée (litiges < 10 000 €).


## Contacts régulateurs

- **Commission Départementale de Conciliation (CDC)** — Préfecture du département de situation du logement
- **Préfet (DRIHL en Île-de-France / DDETS en province)** — Sanction administrative encadrement niveau loyers
- **Tribunal judiciaire (lieu de situation de l'immeuble)** — Fixation judiciaire du loyer + restitution trop-perçu
- **ADIL — Agence Départementale d'Information sur le Logement** — Conseil juridique gratuit en amont (qualifier l'irrégularité avant action)


## Jurisprudence (Judilibre PISTE OAuth)

- L'acquéreur d'un logement donné à bail sous le régime de la loi n° 48-1360 du 1er septembre 1948 ne peut se prévaloir d'une atteinte disproportionnée portée par ce régime locatif au droit au respect de ses biens garanti par l'article 1er du premier protocole additionnel à la CEDH. _( ECLI ECLI:FR:CCASS:2020:C300657 · civ3 · 2020-09-24 · [source](https://www.courdecassation.fr/decision/5fca33d50c7b4623bd8b0b2f) )_


## Références corpus

- https://www.service-public.fr/particuliers/vosdroits/F1311
- https://www.service-public.fr/particuliers/vosdroits/F1314
- https://www.anil.org/parole-expert-logement-location/comment-fixer-le-montant-dun-loyer/


## Limitations et avertissements

- Ce template est un outil d'information ne remplaçant pas un conseil juridique personnalisé d'un avocat ou de l'ADIL.
- Le contenu reflète l'état du droit au 2026-05-18 (corpus SP.fr F1314 vérifié 01/04/2026, F1311 vérifié 08/08/2025, ANIL fiche màj 26/11/2024). Vérifier toute évolution réglementaire avant action.
- Les loyers de référence majorés et la liste des communes encadrées sont actualisés annuellement par arrêté préfectoral. Toujours vérifier l'arrêté en vigueur à la date du bail.
- BailleurVérif ne représente pas le locataire en justice et ne se porte garant d'aucune issue procédurale.


## Résolution attendue

- **P50** ≈ 90 jours
- **Plage** : [30, 540]
- _P50 estimé = règlement amiable post-RAR si bailleur professionnel (1 mois) OU passage CDC (3 mois). P95 = saisine TJ + jugement (12-18 mois). Médiane à recaler après ≥10 case-evaluations réelles._


## Taux de succès estimé

- **Estimation initiale** : 60 %
- _Estimation initiale fondée sur littérature DRIHL/ANIL/UFC-Que-Choisir (à recaler après 10+ cas réels). Variable selon : (a) bailleur pro (taux succès amiable ~70%) vs particulier (~40%), (b) ampleur écart (>20% facilite saisine), (c) DPE F/G (renforce dossier)._


## Courrier type (RAR)

```markdown
**Objet : Demande de mise en conformité du loyer — encadrement zone tendue**

Madame, Monsieur,

Je suis locataire du logement situé à `[ADRESSE COMPLÈTE + ÉTAGE + N°]`, en vertu du bail signé le `[DATE_BAIL]` pour une durée de `[DURÉE]` mois/années. La commune de `[COMMUNE]` est située en zone tendue et fait l'objet d'un encadrement du niveau des loyers en vertu de l'article 25-9 de la loi n° 89-462 du 6 juillet 1989, conformément à l'arrêté préfectoral du `[DATE_ARRÊTÉ]`.

Pour mon logement (surface habitable : `[SURFACE]` m², `[NB_PIÈCES]` pièces, `[ÉPOQUE]`, `[MEUBLÉ|VIDE]`), le loyer de référence majoré applicable s'établit à `[LOYER_REF_MAJORÉ]` € / m², soit un loyer plafond mensuel hors charges de `[PLAFOND_CALCULÉ]` €.

Or, le loyer mensuel hors charges effectivement versé s'élève à `[LOYER_PAYÉ]` €, soit un dépassement de `[ÉCART_EUR]` € (`[ÉCART_PCT]` %) par rapport au plafond légal. `[SI_COMPLÉMENT_LOYER : Le complément de loyer mentionné au bail n'est pas justifié par des caractéristiques exceptionnelles au sens de l'article 25-9 puisque le logement présente : (lister défauts disqualifiants ANIL).]`

En conséquence, je vous demande de bien vouloir :

1. Procéder à la mise en conformité du loyer au plafond légal à compter du `[1ER_MOIS_CIBLE]`.
2. Procéder au remboursement des sommes indûment perçues sur les 12 derniers mois, soit un montant total de `[REMBOURSEMENT_EUR]` €.

À défaut de réponse favorable sous 30 jours à compter de la réception de la présente, je saisirai la Commission Départementale de Conciliation et, parallèlement, signalerai cette infraction au préfet de `[DÉPARTEMENT]` qui peut prononcer une amende administrative pouvant atteindre 5 000 € (15 000 € pour une personne morale) en vertu de l'article 25-9.

Je vous prie d'agréer, Madame, Monsieur, l'expression de mes salutations distinguées.

`[NOM PRÉNOM]`
`[DATE]` — `[VILLE]`

**Pièces jointes :**
- Copie du bail.
- Copie du DPE.
- 3 dernières quittances de loyer.
- Capture de l'arrêté préfectoral en vigueur.
- Calcul détaillé de l'écart.
```


## Méta — signal moat (composant cat-3 RAG-LLM)

- **component_category** : intelligence-interpretative-coûteuse
- **wake_first_authored** : run-243
- **wave_ts** : 2026-05-18T03:00:00Z
- **git_commit_target** : post-run-243
- **compounding_basis** : 1ʳᵉ entrée interpretation-library-v0/recourse-templates/. Run-265 : `legal_basis[]` peuplé via crawler DILA bulk Open Data (3 articles Loi 89-462 — art. 2, art. 17-1, art. 40 — LEGIARTI horodatés, archive XML provenance vérifiable Licence Etalab v2.0). Bascule cat-3 « path validé » → « composant actif #2 substantif » (intelligence interprétative coûteuse au sens DIRECTIVE 9). Cible 30 wakes = 7-10 templates × ≥3 articles LEGIARTI chacun, cadence ingest hebdo non-rejouable rétroactivement.
- **legal_basis_populated_dila_verified** : True
- **legal_basis_articles_count** : 3


---

Source canonique JSON : `https://bailleurverif.fr/api/recourse/loyer-abusif` — licence CC-BY-4.0.
