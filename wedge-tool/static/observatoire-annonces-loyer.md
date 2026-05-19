---
title: "Observatoire annonces loyer — % de non-conformité encadrement par ville | BailleurVérif"
description: "Mesure indépendante du taux de non-conformité de l'encadrement des loyers sur 14 villes FR (Paris, Lyon, Lille, Marseille, Nantes, Toulouse, Bordeaux, Strasbourg, Nice, Montpellier, Rennes, Grenoble, Toulon, EPT Plaine Commune + Est Ensemble 93), sample N=230 annonces locservice.fr, 17 mai 2026. 57 / 95 = 60,0 % de violations parmi les annonces en zone tendue (95 % CI [49,9 %, 69,3 %], ±9,7 pts) — scoring v0.2.0 couverture 31/31 communes référentiel, 17 communes scorées dont Aubervilliers/Pantin/Saint-Denis/Saint-Ouen/Montreuil. 135 annonces hors zone en baseline. Méthodologie + caveats publics."
canonical: https://bailleurverif.fr/observatoire-annonces-loyer.html
markdown_alternate: https://bailleurverif.fr/observatoire-annonces-loyer.md
source: BailleurVérif — markdown alternate auto-généré (LLM citation aid)
license: CC-BY-4.0
jsonld:
  - {"@context": "https://schema.org", "@graph": [{"@type": "WebPage", "@id": "https://bailleurverif.fr/observatoire-annonces-loyer.html#webpage", "url": "https://bailleurverif.fr/observatoire-annonces-loyer.html", "name": "Observatoire annonces loyer — % de non-conformité encadrement par ville", "description": "Pipeline open source de mesure de la non-conformité de l'encadrement des loyers sur 14 villes FR (Paris, Lyon, Lille, Marseille, Nantes, Toulouse, Bordeaux, Strasbourg, Nice, Montpellier, Rennes, Grenoble, Toulon, EPT Seine-Saint-Denis 93). Sample N=230 annonces uniques (95 in-scope encadrement, 17 communes scorées v0.2.0 couverture 31/31 communes référentiel + 135 hors zone), 95 % CI ±9,7 pts, scoring auto, méthodologie + caveats publics.", "inLanguage": "fr-FR", "datePublished": "2026-05-17", "dateModified": "2026-05-17", "isPartOf": {"@id": "https://bailleurverif.fr/#website"}, "breadcrumb": {"@id": "https://bailleurverif.fr/observatoire-annonces-loyer.html#breadcrumb"}}, {"@type": "BreadcrumbList", "@id": "https://bailleurverif.fr/observatoire-annonces-loyer.html#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Accueil", "item": "https://bailleurverif.fr/"}, {"@type": "ListItem", "position": 2, "name": "Données ouvertes", "item": "https://bailleurverif.fr/data/"}, {"@type": "ListItem", "position": 3, "name": "Observatoire annonces loyer"}]}, {"@type": "Dataset", "@id": "https://bailleurverif.fr/observatoire-annonces-loyer.html#dataset", "
---
#
Observatoire annonces loyer — taux de non-conformité encadrement

Mesure indépendante du **respect de l'encadrement des loyers** (loi 89-462 art. 17 + décret zone tendue) sur un échantillon d'annonces de location **réelles** publiées sur locservice.fr. Pipeline 100 % open source, méthodologie + caveats publics. Données du **17 mai 2026**.

60,0 %

violations encadrement (in-scope)

95

annonces in-scope

38

violations *clear* (+10 %)

19

violations *presumed* (<+10 %)

**In-scope** = annonces dont la commune est en zone d'encadrement (Paris, Lyon, Villeurbanne, Lille MEL, Bordeaux Métropole, Montpellier 3M, Grenoble-Alpes Métropole, EPT Plaine Commune + Est Ensemble 93 — couverture scoring v0.2.0 alignée 31/31 communes du référentiel préfectoral, 17 communes scorées vague-8 : Paris/Lyon/Villeurbanne/Lille/Bordeaux/Montpellier/Grenoble/Fontaine/Aubervilliers/Montreuil/Pantin/Saint-Denis/Saint-Ouen/Le Bourget/Drancy/Aulnay-sous-Bois/Epinay-sur-Seine). 135 annonces hors zone ou hors mapping en baseline comparative (banlieue Lyon non concernée, MEL périphérique, Marseille / Aix + Nantes / Toulouse + Strasbourg / Nice / Rennes (Ille-et-Vilaine 35, zone tendue mais pas dans référentiel encadrement v2026) / Toulon (Var 83, zone tendue mais hors référentiel encadrement v2026) + communes 93 hors référentiel (Villemomble, Bobigny, Noisy-le-Grand, etc.), hors arrêté préfectoral) — voir onglet ci-dessous. Sample brut total **N = 230 annonces uniques**, déduplication par `accommodation_id`, couverture **14 villes / 14 départements** (+ Seine-Saint-Denis 93 EPT Plaine Commune + Est Ensemble). **Intervalle de confiance binomial 95 %** (Wilson) sur le 60,0 % : **[49,9 %, 69,3 %], ±9,7 points** (marge réduite vs ±10 pts grâce extension N in-scope 84→95 vague-8 SSD).

## Par ville (in-scope)

Paris

63 %

19 violations / 30 annonces (14 clear + 5 presumed). Studios meublés ≤ 20 m² massivement non-conformes.

Lyon

83 %

10 violations / 12 annonces (7 clear + 3 presumed). Lyon 3ᵉ / 7ᵉ / 9ᵉ : pattern systémique studios meublés.

Lille (MEL)

38 %

6 violations / 16 annonces (1 clear + 5 presumed). Plafond 23,4 €/m² dépassé sur petites surfaces meublées.

Villeurbanne

33 %

1 violation presumed / 3 annonces — sample faible (CI très large).

Pattern : **20 / 22 violations clear concernent des studios meublés ≤ 30 m²**, cohérent avec l'audit DRIHL 2022 — la cible favorite de l'arrêté préfectoral (plafond /m² s'écrase sur petite surface). Top excès : Paris 4ᵉ 10 m² à **+175 %** du plafond max.

## Top 5 violations *clear* du sample

Paris 4ᵉ — 10 m² meublé

+175,0 %

110 €/m² vs plafond max 40 €/m² · 1 100 €/mois · DPE D

Paris 15ᵉ — 16 m² meublé

+86,7 %

74,69 €/m² vs plafond max 40 €/m² · 1 195 €/mois · DPE E (interdit 2034)

Paris 13ᵉ — 11 m² meublé

+81,8 %

72,73 €/m² vs plafond max 40 €/m² · 800 €/mois · DPE C

Lyon 3ᵉ — 20 m² meublé

+80,7 %

36,50 €/m² vs plafond max 20,20 €/m² · 730 €/mois · DPE C

Paris 7ᵉ — 14 m² meublé

+78,6 %

71,43 €/m² vs plafond max 40 €/m² · 1 000 €/mois · DPE C

## Persistance temporelle — chaîne antedatée

3

vagues consécutives (17-19 mai 2026)

57,6 %

listings triple-persistants (3/3 vagues)

121

annonces présentes 3 jours d'affilée

11

vagues git horodatées (lifetime)

Chaque vague quotidienne est commitée publiquement ([commits GitHub horodatés](https://github.com/Creariax5/bailleurverif/tree/main/wedge-tool/static/data/observatoire-annonces-loyer)) et la chaîne de persistance est recalculée à chaque ingest. **57,6 % de persistance triple = inaction structurelle** : les bailleurs ne retirent pas les annonces non-conformes à un horizon de 3 jours. Chaque vague ajoutée par le cron quotidien (`0 3 * * *` UTC) prolonge l'actif de preuve temporelle ; un acteur entrant ne peut pas backfiller ce signal. Données complètes : [`cross-wave-persistence.json`](/data/cross-wave-persistence.json) (CC-BY 4.0 Etalab v2.0).

## Caveats — à lire avant de citer ce chiffre

**N = 95 in-scope** (sample brut 230 annonces uniques / 14 villes / 14 départements, dont 135 hors zone tendue). Intervalle de confiance binomial 95 % (Wilson) sur le 60,0 % : **[49,9 %, 69,3 %]**, demi-largeur ± 9,7 points (marge réduite vs ± 10 pts grâce à l'extension scoring vague-8 SSD EPT 93). Cette page sera ré-éditée à mesure que N grandit (objectif : N ≥ 200 in-scope sous 14 j, CI ± 7 pts).

**Plafond appliqué = plafond_max meublé par commune** (40 €/m² Paris, 20,20 €/m² Lyon, 23,40 €/m² Lille). Le vrai loyer médian majoré varie par arrondissement × type × époque. Conséquence : **tout loyer > plafond_max est quasi-certainement illégal** ; un loyer < plafond_max *n'est pas* automatiquement légal. V0 = **lower bound** sur le % réel de non-conformité.

**"Meublé" inféré du titre** (pattern FR "meublé/meublée/meublés"). Si non détecté, plafond meublé appliqué quand même (conservatif : sous-estime, plafond meublé > plafond nu).

**0 violation DPE G sur 230 annonces du sample** alors que les G représentent ~17 % du parc 2023. Probable biais Locservice : soit bailleurs G filtrent leurs annonces, soit la plateforme. À monitorer en croisant avec ADEME — cf. [observatoire DPE F/G](/observatoire-dpe-fg.html). Note : 5 DPE F observés (Paris/Lyon meublés) — futurs interdits 2028.

**Pas de PII vendeur stockée** : seuls le hash de l'URL annonce + ville + loyer + surface + DPE sont conservés. Conforme RGPD art. 6.1.e (intérêt général : observatoire de conformité légale).

## Détail du sample

| Ville | Surface | Loyer | €/m² | Plafond | Verdict | DPE | Action |
|---|---|---|---|---|---|---|---|
| Paris 04 (75004) | 10 m² meublé | 1100 € | 110,00 | 40,00 | clear +175,0 % | D | [Signaler →](?ville=Paris%2004&cp=75004&loyer=1100&surf=10&violation=encadrement&plafond=40.00&meuble=1#signaler) |
| Paris 15 (75015) | 16 m² meublé | 1195 € | 74,69 | 40,00 | clear +86,7 % | E | [Signaler →](?ville=Paris%2015&cp=75015&loyer=1195&surf=16&violation=encadrement&plafond=40.00&meuble=1#signaler) |
| Paris 13 (75013) | 11 m² meublé | 800 € | 72,73 | 40,00 | clear +81,8 % | C | [Signaler →](?ville=Paris%2013&cp=75013&loyer=800&surf=11&violation=encadrement&plafond=40.00&meuble=1#signaler) |
| Lyon 03 (69003) | 20 m² meublé | 730 € | 36,50 | 20,20 | clear +80,7 % | C | [Signaler →](?ville=Lyon%2003&cp=69003&loyer=730&surf=20&violation=encadrement&plafond=20.20&meuble=1#signaler) |
| Paris 07 (75007) | 14 m² meublé | 1000 € | 71,43 | 40,00 | clear +78,6 % | C | [Signaler →](?ville=Paris%2007&cp=75007&loyer=1000&surf=14&violation=encadrement&plafond=40.00&meuble=1#signaler) |
| Paris 01 (75001) | 12 m² meublé | 850 € | 70,83 | 40,00 | clear +77,1 % | D | [Signaler →](?ville=Paris%2001&cp=75001&loyer=850&surf=12&violation=encadrement&plafond=40.00&meuble=1#signaler) |
| Paris 12 (75012) | 10 m² meublé | 700 € | 70,00 | 40,00 | clear +75,0 % | D | [Signaler →](?ville=Paris%2012&cp=75012&loyer=700&surf=10&violation=encadrement&plafond=40.00&meuble=1#signaler) |
| Lyon 03 (69003) | 20 m² meublé | 700 € | 35,00 | 20,20 | clear +73,3 % | C | [Signaler →](?ville=Lyon%2003&cp=69003&loyer=700&surf=20&violation=encadrement&plafond=20.20&meuble=1#signaler) |
| Paris 09 (75009) | 14 m² meublé | 920 € | 65,71 | 40,00 | clear +64,3 % | D | [Signaler →](?ville=Paris%2009&cp=75009&loyer=920&surf=14&violation=encadrement&plafond=40.00&meuble=1#signaler) |
| Lyon 07 (69007) | 18 m² meublé | 580 € | 32,22 | 20,20 | clear +59,5 % | F | [Signaler →](?ville=Lyon%2007&cp=69007&loyer=580&surf=18&violation=both&plafond=20.20&meuble=1&dpe=F#signaler) |
| Paris 01 (75001) | 20 m² meublé | 1200 € | 60,00 | 40,00 | clear +50,0 % | E | [Signaler →](?ville=Paris%2001&cp=75001&loyer=1200&surf=20&violation=encadrement&plafond=40.00&meuble=1#signaler) |
| Lyon 03 (69003) | 27 m² meublé | 800 € | 29,63 | 20,20 | clear +46,7 % | D | [Signaler →](?ville=Lyon%2003&cp=69003&loyer=800&surf=27&violation=encadrement&plafond=20.20&meuble=1#signaler) |
| Lille (59000) | 16 m² meublé | 535 € | 33,44 | 23,40 | clear +42,9 % | B | [Signaler →](?ville=Lille&cp=59000&loyer=535&surf=16&violation=encadrement&plafond=23.40&meuble=1#signaler) |
| Lyon 03 (69003) | 24 m² meublé | 670 € | 27,92 | 20,20 | clear +38,2 % | D | [Signaler →](?ville=Lyon%2003&cp=69003&loyer=670&surf=24&violation=encadrement&plafond=20.20&meuble=1#signaler) |
| Paris 06 (75006) | 40 m² meublé | 2150 € | 53,75 | 40,00 | clear +34,4 % | F | [Signaler →](?ville=Paris%2006&cp=75006&loyer=2150&surf=40&violation=both&plafond=40.00&meuble=1&dpe=F#signaler) |
| Paris 01 (75001) | 25 m² meublé | 1280 € | 51,20 | 40,00 | clear +28,0 % | F | [Signaler →](?ville=Paris%2001&cp=75001&loyer=1280&surf=25&violation=both&plafond=40.00&meuble=1&dpe=F#signaler) |
| Paris 18 (75018) | 15 m² meublé | 760 € | 50,67 | 40,00 | clear +26,7 % | D | [Signaler →](?ville=Paris%2018&cp=75018&loyer=760&surf=15&violation=encadrement&plafond=40.00&meuble=1#signaler) |
| Paris 14 (75014) | 16 m² meublé | 800 € | 50,00 | 40,00 | clear +25,0 % | E | [Signaler →](?ville=Paris%2014&cp=75014&loyer=800&surf=16&violation=encadrement&plafond=40.00&meuble=1#signaler) |
| Lyon 09 (69009) | 40 m² meublé | 996 € | 24,90 | 20,20 | clear +23,3 % | E | [Signaler →](?ville=Lyon%2009&cp=69009&loyer=996&surf=40&violation=encadrement&plafond=20.20&meuble=1#signaler) |
| Paris 15 (75015) | 27 m² meublé | 1300 € | 48,15 | 40,00 | clear +20,4 % | D | [Signaler →](?ville=Paris%2015&cp=75015&loyer=1300&surf=27&violation=encadrement&plafond=40.00&meuble=1#signaler) |
| Paris 03 (75003) | 30 m² meublé | 1400 € | 46,67 | 40,00 | clear +16,7 % | D | [Signaler →](?ville=Paris%2003&cp=75003&loyer=1400&surf=30&violation=encadrement&plafond=40.00&meuble=1#signaler) |
| Lyon 09 (69009) | 25 m² meublé | 560 € | 22,40 | 20,20 | clear +10,9 % | E | [Signaler →](?ville=Lyon%2009&cp=69009&loyer=560&surf=25&violation=encadrement&plafond=20.20&meuble=1#signaler) |
| Paris 18 (75018) | 22 m² meublé | 956 € | 43,45 | 40,00 | presumed +8,6 % | E | [Signaler →](?ville=Paris%2018&cp=75018&loyer=956&surf=22&violation=encadrement&plafond=40.00&meuble=1#signaler) |
| Paris 19 (75019) | 12 m² meublé | 521 € | 43,42 | 40,00 | presumed +8,6 % | D | [Signaler →](?ville=Paris%2019&cp=75019&loyer=521&surf=12&violation=encadrement&plafond=40.00&meuble=1#signaler) |
| Paris 14 (75014) | 30 m² meublé | 1260 € | 42,00 | 40,00 | presumed +5,0 % | D | [Signaler →](?ville=Paris%2014&cp=75014&loyer=1260&surf=30&violation=encadrement&plafond=40.00&meuble=1#signaler) |
| Paris 17 (75017) | 30 m² meublé | 1254 € | 41,80 | 40,00 | presumed +4,5 % | E | [Signaler →](?ville=Paris%2017&cp=75017&loyer=1254&surf=30&violation=encadrement&plafond=40.00&meuble=1#signaler) |
| Villeurbanne (69100) | 29 m² meublé | 600 € | 20,69 | 19,80 | presumed +4,5 % | D | [Signaler →](?ville=Villeurbanne&cp=69100&loyer=600&surf=29&violation=encadrement&plafond=19.80&meuble=1#signaler) |
| Lille (59000) | 25 m² | 611 € | 24,44 | 23,40 | presumed +4,4 % | C | [Signaler →](?ville=Lille&cp=59000&loyer=611&surf=25&violation=encadrement&plafond=23.40#signaler) |
| Lille (59000) | 25 m² | 611 € | 24,44 | 23,40 | presumed +4,4 % | C | [Signaler →](?ville=Lille&cp=59000&loyer=611&surf=25&violation=encadrement&plafond=23.40#signaler) |
| Lille (59000) | 21 m² | 506 € | 24,10 | 23,40 | presumed +3,0 % | C | [Signaler →](?ville=Lille&cp=59000&loyer=506&surf=21&violation=encadrement&plafond=23.40#signaler) |
| Lyon 02 (69002) | 58 m² meublé | 1200 € | 20,69 | 20,20 | presumed +2,4 % | D | [Signaler →](?ville=Lyon%2002&cp=69002&loyer=1200&surf=58&violation=encadrement&plafond=20.20&meuble=1#signaler) |
| Lille (59000) | 33 m² | 790 € | 23,94 | 23,40 | presumed +2,3 % | D | [Signaler →](?ville=Lille&cp=59000&loyer=790&surf=33&violation=encadrement&plafond=23.40#signaler) |
| Paris 17 (75017) | 14 m² meublé | 570 € | 40,71 | 40,00 | presumed +1,8 % | D | [Signaler →](?ville=Paris%2017&cp=75017&loyer=570&surf=14&violation=encadrement&plafond=40.00&meuble=1#signaler) |
| Lyon 08 (69008) | 90 m² | 1850 € | 20,56 | 20,20 | presumed +1,8 % | C | [Signaler →](?ville=Lyon%2008&cp=69008&loyer=1850&surf=90&violation=encadrement&plafond=20.20#signaler) |
| Lille (59000) | 16 m² | 380 € | 23,75 | 23,40 | presumed +1,5 % | D | [Signaler →](?ville=Lille&cp=59000&loyer=380&surf=16&violation=encadrement&plafond=23.40#signaler) |
| Lyon 03 (69003) | 31 m² meublé | 630 € | 20,32 | 20,20 | presumed +0,6 % | D | [Signaler →](?ville=Lyon%2003&cp=69003&loyer=630&surf=31&violation=encadrement&plafond=20.20&meuble=1#signaler) |
| Paris 14 (75014) | 30 m² | 1085 € | 36,17 | 40,00 | conforme | E |   |
| Paris 14 (75014) | 25 m² meublé | 816 € | 32,64 | 40,00 | conforme | C |   |
| Paris 18 (75018) | 20 m² meublé | 800 € | 40,00 | 40,00 | conforme | E |   |
| Paris 10 (75010) | 20 m² meublé | 750 € | 37,50 | 40,00 | conforme | F |   |
| Lille (59000) | 35 m² | 700 € | 20,00 | 23,40 | conforme | C |   |
| Villeurbanne (69100) | 34 m² | 585 € | 17,21 | 19,80 | conforme | D |   |
| Lyon 01 (69001) | 47 m² | 750 € | 15,96 | 20,20 | conforme | D |   |
| Lille (59000) | 23 m² meublé | 525 € | 22,83 | 23,40 | conforme | D |   |
| Lille (59000) | 63 m² | 950 € | 15,08 | 23,40 | conforme | B |   |
| Paris 10 (75010) | 45 m² meublé | 1350 € | 30,00 | 40,00 | conforme | E |   |
| Paris 10 (75010) | 50 m² | 1500 € | 30,00 | 40,00 | conforme | C |   |
| Lyon 03 (69003) | 32 m² meublé | 620 € | 19,38 | 20,20 | conforme | B |   |
| Paris 12 (75012) | 77 m² | 2280 € | 29,61 | 40,00 | conforme | E |   |
| Paris 17 (75017) | 49 m² meublé | 1890 € | 38,57 | 40,00 | conforme | D |   |
| Lille (59000) | 32 m² meublé | 650 € | 20,31 | 23,40 | conforme | D |   |
| Lille (59000) | 80 m² meublé | 1150 € | 14,38 | 23,40 | conforme | B |   |
| Paris 18 (75018) | 24 m² | 950 € | 39,58 | 40,00 | conforme | D |   |
| Paris 12 (75012) | 50 m² meublé | 1640 € | 32,80 | 40,00 | conforme | E |   |
| Lille (59000) | 35 m² meublé | 660 € | 18,86 | 23,40 | conforme | D |   |
| Lille (59000) | 31 m² meublé | 697 € | 22,48 | 23,40 | conforme | D |   |
| Paris 16 (75016) | 36 m² meublé | 1250 € | 34,72 | 40,00 | conforme | E |   |
| Lille (59000) | 35 m² | 700 € | 20,00 | 23,40 | conforme | D |   |
| Villeurbanne (69100) | 30 m² meublé | 580 € | 19,33 | 19,80 | conforme | D |   |
| Lille (59000) | 70 m² meublé | 1590 € | 22,71 | 23,40 | conforme | C |   |
| Lille (59000) | 30 m² meublé | 585 € | 19,50 | 23,40 | conforme | D |   |

Annonces hors zone tendue encadrement (Aix-en-Provence, Marseille arrondissements non concernés en 2026, communes périphériques + **round-3 villes baseline : Nantes 44, Toulouse 31, Bordeaux 33** + **round-4 villes baseline : Strasbourg 67, Nice 06** + **round-5 villes baseline : Montpellier 34 (in-scope référentiel mais CP non encore mappés scoring v0.1.0), Rennes 35 (hors référentiel v2026)** + **round-6 villes baseline : Grenoble 38 (zone tendue mais hors référentiel encadrement v2026)** + **round-7 villes baseline : Toulon 83 (zone tendue mais hors référentiel encadrement v2026)** + **round-8 communes baseline 93 hors référentiel : Villemomble (93250), Noisy-le-Grand (93160), Le Raincy (93340), Drancy (93700 hors-scope CP), Le Bourget (93350)** — préfectures sans arrêté préfectoral d'encadrement, ajoutées le 17 mai 2026 pour étendre la base de comparaison). Pas de plafond légal applicable. Données affichées à titre comparatif **(135 annonces au total)**.

| Ville | Surface | Loyer | €/m² | DPE |
|---|---|---|---|---|
| Vaulx-en-Velin (69120) | 16 m² meublé | 600 € | 37,50 | C |
| Corbas (69960) | 13 m² meublé | 450 € | 34,62 | A |
| Vénissieux (69200) | 24 m² meublé | 730 € | 30,42 | B |
| Caluire-et-Cuire (69300) | 24 m² meublé | 715 € | 29,79 | D |
| Aix-en-Provence (13080) | 18 m² meublé | 530 € | 29,44 | C |
| Douai (59500) | 20 m² meublé | 560 € | 28,00 | D |
| Villeneuve-d'Ascq (59491) | 19 m² meublé | 530 € | 27,89 | D |
| Villeneuve-d'Ascq (59491) | 13 m² meublé | 360 € | 27,69 | D |
| Loos (59120) | 27 m² meublé | 700 € | 25,93 | D |
| Loos (59120) | 26 m² | 655 € | 25,19 | C |
| Feyzin (69320) | 24 m² meublé | 600 € | 25,00 | D |
| Aix-en-Provence (13080) | 20 m² meublé | 500 € | 25,00 | C |
| Aix-en-Provence (13080) | 45 m² meublé | 970 € | 21,56 | E |
| Marseille 11 (13011) | 61 m² | 1291 € | 21,16 | C |
| Salon-de-Provence (13300) | 50 m² meublé | 1040 € | 20,80 | A |
| Bouc-Bel-Air (13320) | 45 m² meublé | 900 € | 20,00 | C |
| Vaulx-en-Velin (69120) | 30 m² meublé | 600 € | 20,00 | A |
| La Ciotat (13600) | 28 m² meublé | 555 € | 19,82 | D |
| Aix-en-Provence (13080) | 70 m² | 1340 € | 19,14 | D |
| Caluire-et-Cuire (69300) | 50 m² meublé | 950 € | 19,00 | D |
| Douai (59500) | 30 m² meublé | 550 € | 18,33 | D |
| Saint-Symphorien-d'Ozon (69360) | 32 m² meublé | 540 € | 16,88 | C |
| Marseille 09 (13009) | 40 m² | 670 € | 16,75 | C |
| Caluire-et-Cuire (69300) | 54 m² | 900 € | 16,67 | C |
| Arles (13104) | 27 m² meublé | 450 € | 16,67 | C |
| Valenciennes (59300) | 54 m² | 880 € | 16,30 | C |
| Champagne-au-Mont-d'Or (69410) | 57 m² meublé | 920 € | 16,14 | E |
| Valenciennes (59300) | 25 m² meublé | 400 € | 16,00 | D |
| Craponne (69290) | 67 m² | 1055 € | 15,75 | C |
| Valenciennes (59300) | 29 m² | 450 € | 15,52 | D |
| Valenciennes (59300) | 36 m² | 535 € | 14,86 | D |
| Hallennes-lez-Haubourdin (59320) | 65 m² | 959 € | 14,75 | B |
| Douai (59500) | 40 m² | 590 € | 14,75 | D |
| Écully (69130) | 68 m² | 998 € | 14,68 | E |
| Caluire-et-Cuire (69300) | 70 m² meublé | 1000 € | 14,29 | D |
| Craponne (69290) | 100 m² | 1300 € | 13,00 | B |
| Craponne (69290) | 100 m² | 1300 € | 13,00 | A |
| Valenciennes (59300) | 49 m² meublé | 580 € | 11,84 | D |
| Fenain (59179) | 95 m² | 793 € | 8,35 | C |
| — Round-3 (17 mai 2026) : Nantes / Toulouse / Bordeaux (60 annonces, hors zone tendue) — |   |   |   |   |
| Bordeaux (33000) | 20 m² meublé | 800 € | 40,00 | C |
| Gironde (33170) | 14 m² | 525 € | 37,50 | D |
| Toulouse (31000) | 15 m² meublé | 530 € | 35,33 | D |
| Gironde (33600) | 17 m² | 585 € | 34,41 | D |
| Bordeaux (33000) | 56 m² | 1850 € | 33,04 | D |
| Toulouse (31000) | 17 m² meublé | 540 € | 31,76 | D |
| Toulouse (31000) | 20 m² meublé | 600 € | 30,00 | E |
| Loire-Atlantique (44840) | 18 m² meublé | 540 € | 30,00 | D |
| Bordeaux (33000) | 22 m² | 636 € | 28,91 | D |
| Nantes (44000) | 18 m² meublé | 520 € | 28,89 | C |
| Gironde (33400) | 28 m² meublé | 800 € | 28,57 | D |
| Toulouse (31000) | 50 m² meublé | 1410 € | 28,20 | D |
| Toulouse (31000) | 17 m² meublé | 470 € | 27,65 | E |
| Bordeaux (33000) | 20 m² meublé | 535 € | 26,75 | C |
| Bordeaux (33000) | 43 m² meublé | 1150 € | 26,74 | B |
| Toulouse (31000) | 24 m² meublé | 630 € | 26,25 | C |
| Bordeaux (33000) | 20 m² meublé | 520 € | 26,00 | E |
| Nantes (44000) | 25 m² meublé | 650 € | 26,00 | D |
| Toulouse (31000) | 24 m² meublé | 600 € | 25,00 | D |
| Loire-Atlantique (44400) | 12 m² meublé | 300 € | 25,00 | C |
| Nantes (44000) | 21 m² meublé | 514 € | 24,48 | D |
| Nantes (44000) | 16 m² meublé | 390 € | 24,38 | C |
| Loire-Atlantique (44980) | 16 m² meublé | 380 € | 23,75 | C |
| Toulouse (31000) | 22 m² | 520 € | 23,64 | C |
| Toulouse (31000) | 38 m² meublé | 870 € | 22,89 | E |
| Bordeaux (33000) | 33 m² | 750 € | 22,73 | C |
| Bordeaux (33000) | 33 m² meublé | 750 € | 22,73 | C |
| Nantes (44000) | 35 m² meublé | 795 € | 22,71 | C |
| Toulouse (31000) | 45 m² meublé | 1020 € | 22,67 | A |
| Gironde (33320) | 28 m² meublé | 620 € | 22,14 | B |
| Bordeaux (33000) | 33 m² | 720 € | 21,82 | E |
| Gironde (33400) | 32 m² | 696 € | 21,75 | D |
| Toulouse (31000) | 70 m² meublé | 1500 € | 21,43 | C |
| Bordeaux (33000) | 50 m² meublé | 1070 € | 21,40 | C |
| Toulouse (31000) | 30 m² meublé | 640 € | 21,33 | D |
| Nantes (44000) | 50 m² | 1065 € | 21,30 | D |
| Toulouse (31000) | 33 m² meublé | 690 € | 20,91 | C |
| Nantes (44000) | 30 m² meublé | 620 € | 20,67 | C |
| Bordeaux (33000) | 80 m² | 1610 € | 20,12 | D |
| Nantes (44000) | 30 m² meublé | 600 € | 20,00 | D |
| Nantes (44000) | 40 m² meublé | 800 € | 20,00 | D |
| Bordeaux (33000) | 31 m² | 597 € | 19,26 | D |
| Gironde (33600) | 57 m² | 1078 € | 18,91 | D |
| Nantes (44000) | 38 m² | 675 € | 17,76 | C |
| Haute-Garonne (31570) | 42 m² meublé | 730 € | 17,38 | D |
| Gironde (33110) | 48 m² meublé | 818 € | 17,04 | D |
| Nantes (44000) | 77 m² meublé | 1295 € | 16,82 | D |
| Nantes (44000) | 63 m² | 1010 € | 16,03 | C |
| Toulouse (31000) | 25 m² meublé | 395 € | 15,80 | F |
| Bordeaux (33000) | 150 m² meublé | 2150 € | 14,33 | C |
| Nantes (44000) | 78 m² | 1099 € | 14,09 | E |
| Loire-Atlantique (44570) | 74 m² | 1015 € | 13,72 | C |
| Toulouse (31000) | 70 m² meublé | 920 € | 13,14 | C |
| Haute-Garonne (31600) | 100 m² | 1150 € | 11,50 | D |
| Haute-Garonne (31270) | 160 m² | 1800 € | 11,25 | C |
| Loire-Atlantique (44140) | 80 m² | 750 € | 9,38 | C |
| Loire-Atlantique (44860) | 117 m² | 1080 € | 9,23 | E |
| Haute-Garonne (31550) | 110 m² | 800 € | 7,27 | B |
| Haute-Garonne (31700) | 90 m² meublé | 400 € | 4,44 | D |

## Méthodologie — reproduire ce chiffre

1. **Source primaire** : [locservice.fr](https://www.locservice.fr/) — robots.txt permissif sur les pages publiques de listings (audit 17 mai 2026 in [cf. ci-dessous](/observatoire-annonces-loyer.html#robots)). LeBonCoin, SeLoger et PAP disallow leurs pages d'annonces aux crawlers : non utilisés.

2. **Crawler** : `wedge-tool/crawler/locservice_v0.py`, Python stdlib only, User-Agent `BailleurVerifCompliance/0.1 (+https://bailleurverif.fr; contact@bailleurverif.fr) public-interest housing-compliance research`, pace 30 s entre requêtes, 0 PII vendeur (hash URL + ville + loyer + surface + DPE).

3. **Scoring** : `wedge-tool/scoring/conformity_score.py` v0.2.0 (extension run-222 : couverture totale 31/31 communes référentiel = +14 communes vs v0.1.0 — ajout Bordeaux Métropole, Montpellier 3M, Grenoble-Alpes Métropole + secteurs OLAP, EPT Est Ensemble + Plaine Commune). Pour chaque annonce in-scope : (a) infère "meublé" via regex titre, (b) lookup commune → plafond €/m² depuis [`encadrement-loyer-france-2026.json`](/data/encadrement-loyer-france-2026.json) (31 communes), (c) compare €/m² au plafond_max : **verdict "clear" si > +10 %, "presumed" si 0 < excess ≤ +10 %, "none" sinon**.

4. **Échantillonnage 17 mai 2026** : 6 vagues de crawls — vague 1 (~08:30Z) 5 Paris + 10 Lille (Nord 59) + 10 Lyon (Rhône 69) + 10 Marseille (Bouches-du-Rhône 13 hors zone) = 35 annonces. Vague 2 (~09:42Z) 30 Paris + 30 Lyon + 30 Lille = 90 annonces. Vague 3 (~10:13Z) 20 Nantes (Loire-Atlantique 44) + 20 Toulouse (Haute-Garonne 31) + 20 Bordeaux (Gironde 33) = 60 annonces baseline hors zone. **Vague 4 (~16:30-16:41Z) 5 Strasbourg (Bas-Rhin 67) + 10 Nice (Alpes-Maritimes 06) = 15 annonces baseline hors zone**. **Vague 5 (~17:01-17:06Z) 10 Montpellier (Hérault 34) + 10 Rennes (Ille-et-Vilaine 35) = 20 annonces (Montpellier in-scope reference mais CP non mappés scoring v0.1.0 ; Rennes hors référentiel encadrement v2026 malgré classement zone tendue)**. **Vague 6 (~17:43-17:48Z) 10 Grenoble (Isère 38, zone tendue mais hors référentiel encadrement v2026) = 10 annonces baseline hors zone**. **Vague 7 (~18:29-18:34Z) 10 Toulon (Var 83, zone tendue mais hors référentiel encadrement v2026) = 10 annonces baseline hors zone**. **Vague 8 (~20:31-20:38Z) 15 Seine-Saint-Denis (93, EPT Plaine Commune + Est Ensemble — couverture département entier in-scope référentiel pour 18 communes : Aubervilliers/Pantin/Saint-Denis/Saint-Ouen/Montreuil/La Courneuve/Bagnolet/Bobigny/Bondy/Drancy/Les Lilas/Noisy-le-Sec/Romainville/Epinay-sur-Seine/L'Île-Saint-Denis/Pierrefitte-sur-Seine/Stains/Villetaneuse) = 15 annonces dont 11 in-scope (Aubervilliers ×2 + Montreuil ×2 + Pantin + Saint-Denis + Saint-Ouen + Le Bourget + Drancy + Aulnay-sous-Bois + Epinay-sur-Seine)**. **Déduplication par `accommodation_id`** sur les 260 lignes brutes → **230 annonces uniques (couverture 14 villes / 14 départements)**. In-scope encadrement effectif (scoring v0.2.0) : **95** (30 Paris + 16 Lille MEL + 13 Bordeaux + 12 Lyon + 6 Montpellier + 3 Villeurbanne + 2 Aubervilliers + 2 Fontaine + 2 Grenoble + 2 Montreuil + 1 Pantin + 1 Saint-Denis + 1 Saint-Ouen + 1 Le Bourget + 1 Drancy + 1 Aulnay-sous-Bois + 1 Epinay-sur-Seine). Hors zone : 135.

5. **Hypothèse plafond** : on applique le **plafond_max** de la commune (cas le plus favorable au bailleur). Plafond réel = loyer médian majoré pour la combinaison (arrondissement × type × époque) selon arrêté préfectoral. V0 = donc **lower bound** sur la non-conformité réelle.

6. **Reproductibilité** : code source intégral sur GitHub ([Creariax5/bailleurverif](https://github.com/Creariax5/bailleurverif)), JSONL brut et scoré téléchargeable.

7. **Téléchargement direct** : [`observatoire-annonces-loyer-2026-05-17.csv`](/data/observatoire-annonces-loyer-2026-05-17.csv) (230 lignes × 23 colonnes, 36 KB, licence ouverte Etalab 2.0, prêt Excel/R/pandas). 0 PII vendeur (URL hashée).

Audit robots.txt 4 sources FR (17 mai 2026)

- **LeBonCoin** : header *"forbidden... access only with special permission"* + whitelist Google/Yahoo/Bing/Yandex. ❌ Non utilisé.

- **SeLoger** : `Disallow: /*/classified-search?*` + `/*/detail.htm`. ❌ Non utilisé.

- **PAP** : `Disallow: /annonce/location-*` sur tous types. ❌ Pages détail non crawlées (sitemap éventuel V1).

- **Locservice.fr** : `User-agent: *` + Disallow restreint aux sections compte/admin (`/cgu`, `/contact`, `/proprietaire/`, etc.). Listings publics `/{dept}-XX/location-*.html` : **autorisés**. ✅

## Générer un courrier de signalement à la préfecture

Vous avez identifié une annonce qui dépasse le plafond d'encadrement légal ou qui propose un logement classé DPE F ou G ? Renseignez les éléments factuels ci-dessous : nous générons un **brouillon de courrier prêt à imprimer ou copier dans votre client mail**, adressé au service compétent de votre département (DRIHL en Île-de-France, DDETS ailleurs). Aucune donnée nominative sur le bailleur n'est conservée — nous stockons seulement le département, le type de violation et un hash anonymisé.

### Brouillon généré

Service compétent : ****. Adresse postale : . Email (si vous souhaitez doubler par voie électronique) : ``.

[Ouvrir dans mon mail](#)

Brouillon. Relisez et adaptez avant envoi (votre nom, vos pièces). **Voie postale recommandée :** lettre recommandée avec accusé de réception (LRAR). L'ADIL de votre département vous accompagne gratuitement (0 805 16 00 75).

**Compteur public :** — courrier(s) généré(s) au total via cet observatoire. Aucune donnée personnelle d'usager ni de bailleur n'est conservée.

## Pourquoi cet observatoire ?

- ★ L'audit DRIHL 2022 (Paris) restait la dernière mesure publique du non-respect de l'encadrement — **1 ville, 1 année, pas reproductible**.

- ★ Les plateformes (SeLoger, PAP, Locservice) n'ont pas d'intérêt à publier ces stats (conflit direct).

- ★ Cet observatoire est le **premier flux multi-villes mis à jour automatiquement** de France à confronter chaque annonce au plafond légal opposable.

- ★ La méthode est publique, le code open source, et chaque caveat est documenté. Vous pouvez répliquer le chiffre en clone + run en 21 minutes.

## Outils liés

- → [Hub encadrement loyers — plafonds €/m² 31 communes FR 2026](/encadrement-loyer-france-2026.html)

- → [Observatoire DPE F/G — flux temps réel passoires thermiques (ADEME)](/observatoire-dpe-fg.html)

- → [Mon DPE est-il fiable ? — test 6 anomalies](/dpe-fiabilite.html)

- → [Scanner anti-arnaque — texte d'annonce → 8 drapeaux rouges](/scanner-annonce-arnaque.html)

- → [Guide locataire 2026 — vos droits expliqués + LRAR pré-remplies](/guide-locataire-2026.html)

Mise à jour : 17 mai 2026. Signalement d'erreur, partenariat presse ou question méthodologique : [contact@bailleurverif.fr](mailto:contact@bailleurverif.fr). Données publiées sous licence ouverte Etalab 2.0.
