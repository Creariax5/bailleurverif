---
name: Florian Blockers (TODOs ouverts)
description: État vivant des TODOs Florian-action OPEN. Synchro florian-todos.md run-304 refactor 390→125.
type: project
---

# Concept : Florian-blockers (TODOs ouverts)

**État** : 5 TODOs OPEN au 2026-05-19T19:30Z (post run-306, post refactor florian-todos.md run-304). Tous **non-bloquants** par DIRECTIVE 9.

**Source authoritative** : `florian-todos.md` (125 lignes, last refactor 2026-05-19T16:35Z run-304, cooldown ré-refactor ≥2026-06-02).

## OPEN (par priorité)

### TODO-32 ★★ — 2026-05-19 — Valider draft LinkedIn `sub-linkedin-drafter` cycle 1 (~30s Florian-action)

**Pourquoi** : Sub-linkedin-drafter Sonnet 4.6 1ʳᵉ tick 16:45Z EARLY (T+14min post-spawn) a draft 1184c high confidence sur "Neuf références jurisprudence Cass. pour 3 modèles recours". Texte dans `social-drafts.md` L626-665 section `## LINKEDIN-AUTO 2026-05-19T16:45:00Z`. Hashtags : #Immobilier #EncadrementLoyer #DroitDesLocataires #JurisprudenceCivile #PropTech. CTA → `loyer-abusif.html`. ROI cible 1 post/sem × +10 visites/17h (P10 vs post 18/05 7462136169473126400) = ~40 visites/sem additionnelles humaines réelles.

**Action Florian** : (a) Lire L626-665 (30s). (b) Si OK → copier-coller LinkedIn perso 8000 followers (1 min). (c) Si pas OK → réponse inbox.md HEAD avec critique → drafter ajustera cycle 2 (≥2026-05-20T16:45Z).

**Statut** : OPEN 2026-05-19T16:45Z (cycle 1 livré). Sans validation, drafter cycle 2 va re-drafter mais 0 user spillover. Cooldown re-évocation 7j+ (LinkedIn discipline post-TODO-23).

### TODO-25 ★★★ — Activation monétisation (Florian-action ~3-5h)

**Pourquoi** : Phase 2 monétisation reportée semaine prochaine (decision file `monetization-pending.md`). 5 sous-actions séquentielles : Stripe compte (1h) / 3 SKUs (30min) / 1-3 partenariats affiliés (1-2h). Cohérence agent : intégration Stripe BLANK test mode + brouillons Lovys/Hemea/Castorama + CGU draft.

**Statut** : OPEN >5j Florian-action. Pas de cooldown ré-évocation (TODO ★★★).

### TODO-31 ★ — 2026-05-19 — Test Rich Results FAQPage Google (~2 min Florian-action)

**Pourquoi** : 2 pages FAQPage shippées run-303 (encadrement-loyer-france-2026 + observatoire) avec JSON-LD valide json.loads. Google Rich Results Test (`https://search.google.com/test/rich-results`) valide eligible pour SERP rich snippets +20-40% CTR potentiel. ~2 min Florian.

**Statut** : OPEN run-303 2026-05-19T15:30Z. Cooldown ré-évocation 48h+.

### TODO-26 ★ — ANTHROPIC_API_KEY `.env` (silent, déprioritisé)

**Pourquoi** : sub-Haiku/Sonnet via agents-control font le job (sub-judilibre €0.72 lifetime saturated 9 ECLI, sub-seo-monitor Haiku 24h, sub-linkedin-drafter Sonnet 24h). Builder Opus reste pour décisions stratégiques. ANTHROPIC_API_KEY débloquerait Builder Claude API external (batch jobs scrape→résumé→template, embeddings jurisprudence) mais stade vectorisé hypothétique wake +N.

**Statut** : OPEN silent. Cohérence agent : cat-3 inline (Claude Code génère identique). Cooldown ré-évocation 24h+.

### TODO-27 ★★ — 2026-05-18 — Open3CL issue #160 follow-up (signal mort acceptable)

**Pourquoi** : 14:49Z 2026-05-19 cooldown bump-comment passé sans signal Florian. Optionnel : Option A Florian post bump / Option B post-A agent drafte PR locale `getLegalStatus.js` + tests + push GH PAT. Cohérence agent : pas d'auto-comment (compte agent ≠ Florian).

**Statut** : OPEN silent (cooldown passé sans bump = signal mort acceptable). 0 ré-évocation forte.

## TODOs récemment archivés (cooldown ≥7j)

- **TODO-23 / TODO-29 PARTIAL DONE archived run-304** — Florian a posté LinkedIn organique 2026-05-18T15:45 Paris (urn:li:activity:7462136169473126400, +10 visites/17h P10). Canal LinkedIn perso validé HORS-Builder. Spawn `sub-linkedin-drafter` Sonnet pour cadence soutenue. **NE PAS ré-évoquer avant signal Florian explicite (cooldown ≥2026-05-26)**.
- **TODO-30 CLOSED archived run-304** — Cron `0 * * * *` confirmé baseline officielle (vs `*/15` initial). Drift acté budget credits Florian. 24 wakes/jour Builder Opus ≈ €2.40/jour.
- **TODO-28 DONE run-287** — PISTE OAuth + Judilibre operational. Sub-judilibre saturated 3/3 = mission accomplie €0.72 lifetime 5 cycles run-305.
- **TODO-24 DONE run-287** — data.gouv.fr reuse `6a0c30a2a24bbe3d7c2e69d4` live (1ʳᵉ backlink dofollow gov.fr DR 90).

## Anti-patterns flaggés

- Ne PAS ré-évoquer TODO-23/29 (LinkedIn) avant signal Florian explicite (critic-22 flag persistence latente).
- Ne PAS ouvrir 4ᵉ template cat-3 (saturated 3/3, decision file `cat3-saturated.md` BAN strategic-8).
- Ne PAS spam 4ᵉ sous-agent avant ≥2 cycles drafter (cycle 2 ≥2026-05-20T16:45Z, anti-spawn-bomb).
- Ne PAS re-refactor florian-todos.md avant 14j+ (cooldown ré-refactor ≥2026-06-02).
