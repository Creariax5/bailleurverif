# Decision : Pilier 4 viral notation agences — BLOCKER data column missing

**Date** : 2026-05-19T23:30Z (run-310)
**Statut** : Pilier 4 en PAUSE jusqu'à décision Florian TODO-34
**Type** : strategic-blocker-discovered

## Contexte

Mission RÉORIENTATION 2026-05-19T17:XXZ (Florian verbatim "revenu passif") liste 5 piliers validés. **Pilier 4 = viral mechanic notation agences immobilières publique** via pages dédiées `/notation-agence/<brand>/<ville>.html` (ex: `/notation-agence/foncia/paris`, `/notation-agence/citya/lyon`).

Strategic-9 audit-9 21:55Z a flagué Pilier 4 comme "surface morte non-retravaillée" depuis réorientation, mais a prescrit run-309 ship Paris page (Pilier 2) AVANT Pilier 4 — donc Pilier 4 dormant attendu.

Run-310 23:30Z : Builder examine sérieusement faisabilité Pilier 4 (anti-théâtre + pas RÉCIDIVE "STOP éclipser Florian par hygiène critic" déjà flag critic-22/audit-9).

## Constat technique

Schema CSV observatoire actuel (`wedge-tool/static/data/observatoire-annonces-loyer-2026-05-19.csv`, 211 lignes, 23 colonnes) :

```
ts_score,source,url_hash,accommodation_id,ville_label,code_postal,code_dept,
in_scope_encadrement,surface_m2,loyer_eur_total,eur_per_m2,dpe_letter,ges_letter,
meuble,commune_slug,plafond_applied_eur_m2,encadrement_violation,
encadrement_excess_eur_m2,encadrement_excess_pct,dpe_violation,violation_type,
violation_score,score_version
```

**Aucune colonne** : `agence`, `agency`, `brand`, `annonceur`, `is_professional`, `lister_name`, `pro_id`, ou équivalent.

Sources scrapées actuelles (locservice + autres listés dans column `source`) : extraction listing limitée à propriétés annonce + adresse + caractéristiques bien. Brand annonceur **non capturé** dans pipeline scraper.

## Conséquence

Pages `/notation-agence/<brand>/<ville>.html` data-driven authentiques **IMPOSSIBLES** sans upgrade pipeline scraper (add 2 colonnes minimum + re-scrape 7 villes daily + backfill historique optionnel). Estimation Builder : 2-4 wakes Opus, ~€10-20.

## Workarounds 0-data-upgrade examinés et rejetés

1. **Placeholder page** `/notation-agences-immobilieres.html` "à venir — méthodologie + appel data" → théâtre + low quality + 0 ROI. Rejeté.
2. **Hall of shame anonymisé** : top 20 violations CSV (URLs originales) avec ville/excès/m² sans brand → pas viral car pas namedshaming identifiable. Couvre déjà observatoire HTML (`/observatoire-annonces-loyer.html`). Redondant.
3. **Crowdsourcing form témoignages** : signup-gated email + form anonyme → vide content (cold start = 0 témoignage) + 0 utilisateur 92+ wakes humans_engaged=2. Trap UX.

Aucun workaround = Pilier 4 viral mécanisme authentique sans soit (a) upgrade scraper, soit (b) pivot angle non-agence (ex: top arrondissements % violation = data already in CSV).

## Décision

**Pause Pilier 4 par défaut**, escalade à Florian via TODO-34 ★★ florian-todos.md (3 options : upgrade scraper / pivot angle / pause indéfini).

**Default Builder = (c) pause indéfini** si silence Florian 14j (cooldown ≥2026-06-02). Cohérent avec :
- DIRECTIVE 9 anti-blocage : 5 piliers ≠ tous obligatoires, focus Piliers 1+2+5 enough proof-of-pattern.
- Anti-théâtre : pas shipper placeholder page de mauvaise qualité juste pour "toucher Pilier 4".
- Économie Builder Opus ~€10-20 upgrade scraper = bloqué tant que Pilier 1+2 pas validés signal (deadline 2026-05-26 Paris page).
- Respect strategic-9 ban "pas big-bang refactor index.html" applicable par analogie aux gros upgrades sans signal validation préalable.

## Conditions de ré-évocation

- Florian écrit `TODO-34 pilier-4: (a)|(b)|(c)` dans `inbox.md` HEAD → Builder exécute J+0 si (a) ou (b).
- Pilier 1+2 signal positif (≥3 captures qualifiées 7j Paris page) → Builder peut reconsidérer Pilier 4 = next levier viralité.
- Pilier 1+2 signal nul (≤1 capture 14j) → Builder pivote painkiller (DPE F/G ou dépôt garantie) AVANT Pilier 4.

## Documentation

- `memory-agent/concepts/mission.md` Pilier 4 section : BLOCKER data discovered noted.
- `memory-agent/concepts/florian-blockers.md` : TODO-34 ★★ NEW entry.
- `florian-todos.md` : TODO-34 ★★ section "Gros chantier > 1h" (en réalité 5 min Florian-action décision).
- `MEMORY.md` : decision pointer added.
