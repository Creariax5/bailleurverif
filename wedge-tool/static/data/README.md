# BailleurVérif — Données ouvertes

## Encadrement des loyers en France (2026)

Dataset libre listant les **31 communes françaises** où s'applique l'encadrement des loyers en 2026 (loi ALUR / Climat & Résilience), avec les plafonds légaux de référence par mètre carré.

### Fichiers

| Fichier | Format | Taille | Description |
|---|---|---|---|
| `encadrement-loyer-france-2026.csv` | CSV (UTF-8) | ~4 ko | 31 lignes, 8 colonnes — usage tableur/Excel/dataviz |
| `encadrement-loyer-france-2026.json` | JSON | ~12 ko | Wrapper enveloppe + tableau communes — usage code/API |

### Schéma (CSV)

| Colonne | Type | Description | Exemple |
|---|---|---|---|
| `slug` | string | Identifiant URL (kebab-case) | `paris`, `saint-ouen` |
| `commune` | string | Nom officiel de la commune | `Paris`, `Saint-Ouen-sur-Seine` |
| `plafond_nu_eur_m2` | float | Loyer plafond légal location nue (€/m²/mois) | `33.3` |
| `plafond_meuble_eur_m2` | float | Loyer plafond légal location meublée (€/m²/mois) | `40.0` |
| `perimetre` | string | Zone géographique d'application | `20 arrondissements` |
| `date_debut_encadrement` | string | Date d'entrée en vigueur de l'arrêté | `1er juillet 2019` |
| `autorite_prefectorale` | string | Préfecture qui publie l'arrêté annuel | `Préfecture de Paris (DRIHL)` |
| `intercommunalite` | string | EPCI/Métropole de rattachement | `Métropole Européenne de Lille (MEL)` |

### Source

Arrêtés préfectoraux 2026 publiés par les préfectures concernées (Paris, Nord, Rhône, Gironde, Hérault, Seine-Saint-Denis, Isère) conformément aux articles L.302-7-1 et suivants du Code de la construction et de l'habitation. Les plafonds représentent un loyer de référence (médian + 20%) — le plafond exact dépend du secteur géographique précis, du nombre de pièces, du caractère meublé/nu, et de l'époque de construction.

### Licence

**CC BY 4.0** — Vous pouvez utiliser, modifier et redistribuer librement ce dataset, à condition de citer la source : `BailleurVérif (https://bailleurverif.fr/)`.

### Couverture

- 31 communes (Paris + Lille + Lyon + Bordeaux + Montpellier + Grenoble + 25 communes d'Île-de-France et Métropole de Lille/Lyon/Grenoble)
- 7 préfectures
- 7 intercommunalités (Paris intra-muros, MEL, Métropole de Lyon, Bordeaux Métropole, 3M, Plaine Commune, Est Ensemble, Grenoble-Alpes Métropole)
- Dates d'entrée en vigueur : 2019 (Paris) → 2023 (Grenoble)

### Méthodologie

Les plafonds publiés représentent les **loyers médians de référence majorés de 20%** (encadrement strict). Le plafond exact applicable à un logement spécifique dépend de critères additionnels (épôque de construction, surface, secteur OLAP précis). Le calculateur en ligne sur [bailleurverif.fr](https://bailleurverif.fr/) couvre ces nuances commune par commune.

### Citation suggérée (BibTeX-like)

```
@dataset{bailleurverif_encadrement_2026,
  title  = {Encadrement des loyers en France 2026 — 31 communes},
  author = {BailleurVérif},
  year   = {2026},
  url    = {https://bailleurverif.fr/data/encadrement-loyer-france-2026.csv},
  license = {CC-BY-4.0}
}
```

### Contact

- Projet : https://bailleurverif.fr/
- Code open-source : (en cours de publication)
- Corrections / signalements : ouvrir un ticket sur le repository (à venir)

### Changelog

- **2026-05-16** : Première publication. 31 communes. CSV + JSON.
