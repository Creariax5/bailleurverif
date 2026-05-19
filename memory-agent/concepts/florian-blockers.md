---
name: Florian Blockers (TODOs ouverts)
description: État vivant des TODOs Florian-action OPEN. Synchro florian-todos.md run-310.
type: project
---

# Concept : Florian-blockers (TODOs ouverts)

**État** : 6 TODOs OPEN au 2026-05-19T23:30Z (post run-309 ship Paris + post run-310 update concepts). Tous **non-bloquants** par DIRECTIVE 9.

**Source authoritative** : `florian-todos.md` (last refactor 2026-05-19T16:35Z run-304, cooldown ré-refactor ≥2026-06-02).

## OPEN (par priorité)

### TODO-32 ★★ — 2026-05-19 — Signer 2 affiliés Lovys (GLI) + Hemea (travaux) (1-2h, Florian-action)

**Pourquoi** : Florian 17:XXZ réorientation — affiliés AVANT subscriptions (zéro infrastructure, €30-50/lead). Skip TODO-25 Stripe tant que pas 100+ signups réels. Une fois IDs collés `.env` (`LOVYS_AFFILIATE_ID=` + `HEMEA_AFFILIATE_ID=`), Builder intègre liens trackés pages programmatiques (`/loyer-legal-paris.html` + futurs).

**Statut** : OPEN 2026-05-19T17:XXZ. Aucun cooldown (priorité revenu passif).

### TODO-33 ★ — 2026-05-19 — Parler 5 personnes entourage (~1h, débloque pivot painkiller)

**Pourquoi** : Recherche utilisateur qualitative pour valider painkiller pivot homepage. 5 personnes × 12 min × 1 question "Si tu avais 10s pour comprendre si tu te fais arnaquer sur ton loyer/dépôt/DPE, qu'est-ce que tu voudrais voir?". Findings → inbox.md HEAD = data réelle remplace hypothèses qualitatives Builder.

**Statut** : OPEN 2026-05-19T17:XXZ. Pas de cooldown (débloque Pilier 1 pivot).

### TODO-34 ★★ — 2026-05-19 — DÉCISION Pilier 4 viral notation agences : upgrade scraper vs pivot angle (NEW run-310)

**Pourquoi** : CSV observatoire 23 colonnes n'a PAS `agence`/`brand`/`annonceur`. Pages dédiées `/notation-agence/<brand>/<ville>.html` data-driven impossibles sans upgrade scraper (extraction nom agence + classification pro vs particulier à chaque listing). 3 options Florian-decide :
- (a) **Upgrade scraper** (Builder code 2-4 wakes, ajouter `agence_brand` + `is_professional` colonnes + re-scrape) → enable Pilier 4 viral data-driven authentique.
- (b) **Pivot angle Pilier 4** : namedshaming non-agences (ex: top arrondissements/codes postaux % violation = `/top-violations-loyer-paris-arrondissement.html`) sans brand info. Data already in CSV.
- (c) **Pause Pilier 4** indéfini, focus Piliers 1+2+5 cumul = enough proof-of-pattern.

**Statut** : OPEN run-310. Default Builder = (c) pause indéfini (anti-théâtre + respect 5 piliers ≠ tous obligatoires). Si Florian dit (a) ou (b) → Builder exécute.

### TODO-32-bis ★ — 2026-05-19 — Valider draft LinkedIn `sub-linkedin-drafter` cycle 1 (~30s Florian-action)

**Pourquoi** : Sub-linkedin-drafter Sonnet 4.6 1ʳᵉ tick 16:45Z EARLY a draft 1184c "Neuf références jurisprudence Cass. pour 3 modèles recours" dans `social-drafts.md` L626-665. Florian valide en 30s + poste à son rythme 8000 followers. ROI cible +10 visites/17h P10.

**Statut** : OPEN 2026-05-19T16:45Z (cycle 1 livré). Cooldown ré-évocation 7j+ (LinkedIn discipline post-TODO-23). Si non-validé cycle 2 ≥2026-05-20T16:45Z re-drafte automatiquement signal frais.

### TODO-31 ★ — 2026-05-19 — Test Rich Results FAQPage shipped run-303 (~2 min)

**Pourquoi** : Vérifier sur Google Rich Results Test les 2 URLs FAQPage shippées + désormais 3 URLs incluant `/loyer-legal-paris.html` run-309. Builder ne peut pas accéder à cet outil.

**Statut** : OPEN run-303. Cooldown ré-évocation 48h+.

### TODO-26 ★ — ANTHROPIC_API_KEY `.env` (silent, déprioritisé)

**Pourquoi** : sub-Haiku/Sonnet via agents-control font le job (sub-judilibre €0.72 lifetime, sub-seo-monitor Haiku 24h, sub-linkedin-drafter Sonnet 24h). Builder Opus reste pour décisions stratégiques.

**Statut** : OPEN silent. Cooldown ré-évocation 24h+.

### TODO-27 ★★ — 2026-05-18 — Open3CL issue #160 follow-up (signal mort acceptable)

**Statut** : OPEN silent (cooldown passé sans bump = signal mort acceptable). 0 ré-évocation forte.

## TODOs récemment archivés (cooldown ≥7j)

- **TODO-23 / TODO-29 PARTIAL DONE archived run-304** — Florian LinkedIn organique 2026-05-18T15:45 Paris (+10 visites/17h P10). NE PAS ré-évoquer avant 2026-05-26.
- **TODO-30 CLOSED archived run-304** — Cron `0 * * * *` baseline officielle.
- **TODO-28 DONE run-287** — PISTE OAuth + Judilibre. Sub-judilibre saturated 3/3 €0.72.
- **TODO-24 DONE run-287** — data.gouv.fr reuse `6a0c30a` live (1ʳᵉ dofollow gov.fr DR 90).
- **TODO-25 ⏸️ REPORTÉ post-100 signups** (Florian 2026-05-19T17:XXZ réorientation).

## Anti-patterns flaggés

- Ne PAS ré-évoquer TODO-23/29 (LinkedIn) avant signal Florian explicite (cooldown ≥2026-05-26).
- Ne PAS ouvrir 4ᵉ template cat-3 (BAN strategic-7/8/9).
- Ne PAS spam 4ᵉ sous-agent avant ≥2 cycles drafter (cycle 2 ≥2026-05-20T16:45Z).
- Ne PAS re-refactor florian-todos.md avant 14j+ (cooldown ≥2026-06-02).
- Ne PAS scaler Paris→Lyon/Marseille avant signal Paris 7j (BAN audit-9 implicite, deadline mesure 2026-05-26T22:30Z).
- Ne PAS auto-générer PDF lettre LRAR tant que 0 capture Paris (BAN strategic-9 résolu tension tactical-23 ★★★).
