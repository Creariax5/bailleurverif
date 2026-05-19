# MEMORY.md — Index mémoire agent BailleurVérif (Builder)

> **Version** : Phase 1 bootstrap 2026-05-18T11:29Z (run-258).
> **Architecture** : Obsidian-style atomique. Builder lit `MEMORY.md` (~5 KB) + 3-5 concepts pertinents (~10-20 KB) au lieu du monolithique state.md/ledger.md/inbox.md (~1.6 MB).
> **Économie cible** : ~$270/mois (-95% tokens lecture/wake).
> **Sources authoritative** : `ledger.md` + `memory-agent/` (Phase 2 PATCH run-280). `state.md` DEPRECATED run-289 (ledger.md = source of truth headlines). `inbox.md` + `runs/` restent archives append-only GitHub-public (transparence + rollback).
> **Workflow** : (1) read MEMORY.md → (2) identifier 3-5 concepts/decisions pertinents à la tâche → (3) read SEULEMENT ceux-là → (4) act → (5) update concept OR snapshot si état change → (6) ledger.md append (toujours, source of truth).

## Concepts (état courant, mutable)

- [Mission](concepts/mission.md) — 5000 users 90j SaaS B2C autonome, cible 2026-08-14, monétisation Phase 2.
- [Moat categories](concepts/moat-categories.md) — 4 catégories DIRECTIVE 9 (cat-1 données / cat-2 morte / cat-3 RAG-LLM / cat-4 distribution).
- [Observatoire chain](concepts/observatoire-n232.md) — Cat-1 actif, 11 vagues git timestampées (vague-11 N=210 run-279), cron daily 7 villes 2 jours consécutifs prouvés.
- [Florian blockers](concepts/florian-blockers.md) — TODO-29 γ-mini canal externe / TODO-30 cron drift / TODO-25/26/27/28 backlog.
- [Strategic prescription last](concepts/strategic-prescription-last.md) — Audit-8 2026-05-19T16:05Z = spawn `sub-linkedin-drafter` Sonnet 4.6 HONORED run-304 J+0 (drift flag run-303 FAQPage polish vs directive Florian récente).
- [Tactical warnings current](concepts/tactical-warnings-current.md) — Critic-19 8.7/10 ★★★ : #1 state.md deprecated ✅ run-289, #2 ip 2124423717 ⏳ run-290, #3 ritual §b ✅.
- [Press FR list](concepts/press-fr-list.md) — 4/4 outbound 2026-05-17 (Capital/LeMonde/Mediapart/Reporterre) 0/4 réponse T+17h.
- [Monetization pending](concepts/monetization-pending.md) — Stripe / SKUs / partenaires affiliés bloqués Florian-action TODO-25.
- [Vision 36m](concepts/vision-36m.md) — Voie B locataire-first, observatoire série temporelle + RAG jurisprudence + B2B notaires P3.
- [Traffic signals](concepts/traffic-signals.md) — Visiteur récurrent ip_hash 6994446044 = 3 hits homepage-only, 0 deep nav. Signal bounce CTA faible (à confirmer critic-19).
- [Sub-agents actifs](concepts/sub-agents-active.md) — 3 sous-agents : `sub-judilibre-enrich` (Haiku 1h cat-3 enrich) + `sub-seo-monitor` (Haiku 24h audit GEO/SEO) + `sub-linkedin-drafter` (Sonnet 24h drafts LinkedIn run-304). Cap 8. Builder Opus seul POST/PATCH/DELETE.

## Decisions (atomiques, datées, immutable post-décision)

- [GSC verify](decisions/2026-05-17-gsc-verify.md) — Google Search Console verified 2026-05-17 sur compte Florian.
- [Repo public](decisions/2026-04-XX-repo-public.md) — `Creariax5/bailleurverif` MIT, DR 90 GitHub.
- [Vision 36m](decisions/2026-05-17-vision-36m.md) — Voie B locataire-first validée run-210.
- [data.gouv.fr v1](decisions/2026-05-13-data-gouv-v1.md) — Dataset observatoire publié, UUID `annonces-de-location-francaises-non-conformes-observatoire-bailleurverif`.
- [Pivot moat](decisions/2026-05-17-pivot-moat.md) — DIRECTIVE 9 active, 1 wake/4 minimum moat-builder.
- [Directive 7 révisée](decisions/2026-05-17-directive-7-revisee.md) — Cron `*/15` external, NO ScheduleWakeup builder.
- [Strategic critic live](decisions/2026-05-17-strategic-critic-live.md) — DIRECTIVE 10 active, audit /16 wakes.
- [Cat-3 templates](decisions/2026-05-18-cat3-templates.md) — `loyer-abusif.v0.json` inline shippé run-243, endpoint `/api/recourse/<tag>` live.
- [Cat-3 saturated 3/3](decisions/2026-05-19-cat3-saturated.md) — 3/3 templates legal_basis DILA-verified run-275 (loyer-abusif + dpe-invalide + depot-garantie), ban 4ᵉ template.
- [Cat-2 morte](decisions/2026-05-19-cat2-morte.md) — Notation/signalement déclarés morts run-272 (T+63h+ post-V2 ship, 0 record).
- [ANIL outreach J+0](decisions/2026-05-19-anil-outreach.md) — Strategic-6 prescription mail ANIL HONORÉ run-278 SMTP success, cooldown 72h ≥2026-05-22T05:35Z.
- [Phase 2 PATCH](decisions/2026-05-19-phase2-patch.md) — Agent prompt 8326→5349 chars -35.7% run-280, loop compliance observée run-281 J+0.
- [Cross-wave public section](decisions/2026-05-19-cross-wave-public-section.md) — Section `#persistance-temporelle` shipped observatoire HTML run-285 (cat-4 visibilité moat cat-1).
- [TODO-24 reuse publié](decisions/2026-05-19-todo-24-reuse-published.md) — data.gouv.fr reuse `6a0c30a2a24bbe3d7c2e69d4` live run-287 (cat-4 dofollow gov.fr DR ≈90, 1ʳᵉ backlink institutionnel).
- [TODO-28 Judilibre pipeline](decisions/2026-05-19-todo-28-judilibre-pipeline.md) — piste_oauth + judilibre_search helpers shipped + tested + loyer-abusif jurisprudence_refs N=0→1 run-287.
- [Awesome-list PR](decisions/2026-05-19-awesome-list-pr.md) — PR `awesomedata/apd-core#410` OPENED run-288 (cat-4 distribution external, strategic-7 prescription J+0).
- [Awesome-real-estate PR](decisions/2026-05-19-awesome-real-estate-pr.md) — PR `etewiah/awesome-real-estate#28` OPENED run-296 (2ᵉ awesome-list, audience EN global real-estate, 0 nag ≥14j).
- [state.md deprecated](decisions/2026-05-19-state-md-deprecated.md) — state.md + metrics.json `_meta` dépréciés run-289 (critic-19 ★★★ #1, source of truth = ledger.md + memory-agent/).
- [Zimbra SMTP](decisions/2026-05-17-zimbra-smtp.md) — OVH `contact@bailleurverif.fr` send capable, anti-spam ≤1/30min.
- [Budget tight](decisions/2026-05-18-budget-tight.md) — Builder interval 3600s, lectures sélectives obligatoires.
- [Sub-agents capability](decisions/2026-05-19-sub-agents-capability.md) — Champ `model` agents-control activé run-297, Builder Opus seul POST/PATCH/DELETE, 1er spawn `sub-judilibre-enrich` Haiku 4.5, max 6 sous-agents budget €20/mois.
- [Sub-seo-monitor spawn](decisions/2026-05-19-sub-seo-monitor-spawn.md) — 2ᵉ sous-agent Haiku 4.5 interval 24h spawné run-299 (brief Florian 13:30Z monitoring SEO/GEO post Tier 1+2). Override discipline incremental sur cas explicite.
- [Sub-linkedin-drafter spawn](decisions/2026-05-19-sub-linkedin-drafter-spawn.md) — 3ᵉ sous-agent Sonnet 4.6 interval 24h spawné run-304 (brief Florian 16:XXZ priorité #1 post-TODO-23 partial done LinkedIn organique). Cap relevé 6→8. florian-todos.md refacto 390→125 lignes.

## KPIs

- [Snapshot current](kpis/snapshot-current.md) — humans_engaged=2 / subscribers=0 / N=232 / moat=4/4 substantif 2 catégories actives.

## Convention update

Quand un état change (ex : N=232 devient N=400) → update concept + ledger.md append. Quand une décision est prise → nouveau fichier decisions/ DATÉ. Pas de "delete" sur decisions/ (audit trail). Concepts updatables in-place (état courant, pas historique).
