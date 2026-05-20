# MEMORY.md — Index mémoire agent BailleurVérif (Builder)

> **Version** : Phase 1 bootstrap 2026-05-18T11:29Z (run-258).
> **Architecture** : Obsidian-style atomique. Builder lit `MEMORY.md` (~5 KB) + 3-5 concepts pertinents (~10-20 KB) au lieu du monolithique state.md/ledger.md/inbox.md (~1.6 MB).
> **Économie cible** : ~$270/mois (-95% tokens lecture/wake).
> **Sources authoritative** : `ledger.md` + `memory-agent/` (Phase 2 PATCH run-280). `state.md` DEPRECATED run-289 (ledger.md = source of truth headlines). `inbox.md` + `runs/` restent archives append-only GitHub-public (transparence + rollback).
> **Workflow** : (1) read MEMORY.md → (2) identifier 3-5 concepts/decisions pertinents à la tâche → (3) read SEULEMENT ceux-là → (4) act → (5) update concept OR snapshot si état change → (6) ledger.md append (toujours, source of truth).

## Concepts (état courant, mutable)

- [Mission](concepts/mission.md) — RÉORIENTÉE 2026-05-19T17:XXZ : revenu passif €100-500/mo @6m + €500-3000/mo @12m, Florian ≤1h/mois, 5 piliers (sharpen+SEO+affiliés+viral+LinkedIn). Pilier 1+2 LIVE run-308/309. **Pilier 4 BLOCKER data column missing run-310 → TODO-34 décision Florian**. Skip TODO-25.
- [Moat categories](concepts/moat-categories.md) — 4 catégories DIRECTIVE 9 (cat-1 données / cat-2 morte / cat-3 RAG-LLM / cat-4 distribution).
- [Observatoire chain](concepts/observatoire-n232.md) — Cat-1 actif, 11 vagues git timestampées (vague-11 N=210 run-279), cron daily 7 villes 2 jours consécutifs prouvés.
- [Florian blockers](concepts/florian-blockers.md) — 6 TODOs OPEN run-310 : TODO-32 ★★ affiliés / TODO-33 ★ entourage / **TODO-34 ★★ NEW décision Pilier 4** / TODO-32-bis drafter validate / TODO-31 Rich Results / TODO-26/27 silent.
- [Strategic prescription last](concepts/strategic-prescription-last.md) — Audit-9 2026-05-19T21:55Z = ship `/loyer-legal-paris.html` Pilier 2 proof-of-pattern AVANT auto-gen LRAR. **HONORED run-309 J+0**. Bans audit-9 actifs jusqu'à audit-10 ~run-325 (incl. NEW pas scaler Paris→Lyon avant signal 7j 2026-05-26).
- [Tactical warnings current](concepts/tactical-warnings-current.md) — Audit-23 8.7/10 (+0.2) post run-308 : ★★★ #1 auto-gen LRAR BLOQUÉ strategic-9 (tension résolue) / ★★ #2 IndexNow round-69 partial / ★★ #3 seuils Pilier 1 mission.md L80-91 ✅ run-309.
- [Press FR list](concepts/press-fr-list.md) — 4/4 outbound 2026-05-17 (Capital/LeMonde/Mediapart/Reporterre) 0/4 réponse T+17h.
- [Monetization pending](concepts/monetization-pending.md) — RÉORIENTÉ : skip Stripe/SKUs B2C, focus affiliés (Lovys+Hemea) via TODO-32 NEW. TODO-25 REPORTÉ post-100 signups.
- [Vision 36m](concepts/vision-36m.md) — Voie B locataire-first, observatoire série temporelle + RAG jurisprudence + B2B notaires P3.
- [Traffic signals](concepts/traffic-signals.md) — Visiteur récurrent ip_hash 6994446044 = 3 hits homepage-only, 0 deep nav. Signal bounce CTA faible (à confirmer critic-19).
- [Sub-agents actifs](concepts/sub-agents-active.md) — 4 sous-agents : `sub-judilibre-enrich` (Haiku 1h disabled saturated_3) + `sub-seo-monitor` (Haiku 24h, **PATCHED v2 run-321** prompt 5766 chars +tâche 2bis BreadcrumbList audit) + `sub-linkedin-drafter` (Sonnet 24h) + `sub-observatoire-publisher` (Haiku 7j). Cap 8.
- [SEO discipline no-orphan + BreadcrumbList rule](concepts/seo-discipline.md) — ★ run-318+**run-321 EXTENDED** : (1) anti-orphan (linkée depuis ≥1 page indexée avant ship) ; (2) **BreadcrumbList JSON-LD** doit avoir `item` URL sur tous ListItem (81 pages cassées fix run-321 brief Florian 09:45Z).

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
- [Cat-3 jurisprudence_refs 3/3 ★](decisions/2026-05-19-cat3-jurisprudence-saturated-3-3.md) — 9 ECLI Cass. cumul (3/3 templates ×3 refs) run-305 cycle 5 ship, sub-judilibre auto-disabled saturated_3 exit-clause.
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
- [Mission reorientation revenu passif](decisions/2026-05-19-mission-reorientation-revenu-passif.md) — Florian 17:XXZ verbatim : revenu passif vs 5000 users, 5 piliers validés (sharpen+SEO+affiliés+viral+LinkedIn), TODO-25 REPORTÉ post-100 signups, TODO-32 Affiliés NEW + TODO-33 5 personnes NEW. Ack run-307 J+0.
- [Strategic-9 loyer-legal-paris shipped](decisions/2026-05-19-strategic-9-loyer-legal-paris-shipped.md) — Pilier 2 proof-of-pattern `/loyer-legal-paris.html` shipped run-309 J+0 strategic-9 prescription. Tactical-23 ★★★ auto-gen LRAR différé (BAN strategic-9 jusqu'à signal capture). Seuils Pilier 1 iter-1 explicites mission.md (≥3/7j validé, ≤1/14j pivot).
- [Pilier 4 data-missing](decisions/2026-05-19-pilier-4-data-missing.md) — CSV observatoire 23 cols sans `agence`/`brand` ⇒ pages `/notation-agence/<brand>/<ville>.html` data-driven impossibles sans upgrade scraper. Pilier 4 PAUSE par défaut, TODO-34 ★★ escalade décision Florian (a/b/c).
- [Strategic-10 Que Choisir outreach](decisions/2026-05-20-strategic-10-quechoisir-outreach.md) — Audit-10 strategic prescription unique HONORED run-315 J+0 = mail SMTP `courrierdeslecteurs@quechoisir.org`. IndexNow round-69 verdict théâtre confirmé T+6h (0 hit Paris). 10/10 strategic audits HONORED cumul. M0 plafond cassé (compteur 2→0 reset).
- [Sub-observatoire-publisher spawn](decisions/2026-05-20-sub-observatoire-publisher-spawn.md) — 4ᵉ sous-agent Haiku 4.5 interval 7j spawné run-317 (brief Florian 05:40Z "Oui go" deadline 2026-05-24). Republie ressource CSV observatoire hebdo dataset data.gouv.fr `6a09ca8088345193c180e0b5`. ID `576fb185-9c51-4ca9-9453-ac9088a223ac`. Coût €0.12/mois. Asymétrie data.gouv.fr DR 90 fresh perpétuel sans charge Builder.
- [Orphan fix + SEO discipline](decisions/2026-05-20-orphan-fix-and-seo-discipline.md) — ★ Brief Florian 2026-05-20T06:35Z HONORED run-318 J+0 (3 étapes 4/4 + sub-seo-monitor PATCH différé confirmation Florian). 2 liens internes Paris pages ajoutés homepage `#outils-paris` + observatoire `#voir-aussi`. seo-discipline.md concept créé. TODO-35 ★ Indexing API Google ajouté florian-todos.
- [Wikidata Q139857638 intégrée](decisions/2026-05-20-wikidata-q139857638-integration.md) — ★ Brief Florian 2026-05-20T07:35Z HONORED run-319 J+0 (3 étapes 3/3). Wikidata `Q139857638` créée Florian via bot API. JSON-LD `sameAs` étendu 1→4 URLs + footer link Wikidata+GitHub visibles + moat-categories cat-4 +1 substantif (3 cumul, audit-10 stagnation 18 wakes cassée).
- [BreadcrumbList fix + discipline](decisions/2026-05-20-breadcrumblist-fix-and-discipline.md) — ★ Brief Florian 2026-05-20T09:45Z HONORED run-321 J+0 (3 étapes 3/3). 90 pages HTML BreadcrumbList JSON-LD fix (commit `3ee81da`) + discipline codifiée seo-discipline.md + sub-seo-monitor PATCH v2 prompt 3301→5766 chars (+tâche 2bis BreadcrumbList audit).

## KPIs

- [Snapshot current](kpis/snapshot-current.md) — humans_engaged=2 / subscribers=0 / N=232 / moat=4/4 substantif 2 catégories actives.

## Convention update

Quand un état change (ex : N=232 devient N=400) → update concept + ledger.md append. Quand une décision est prise → nouveau fichier decisions/ DATÉ. Pas de "delete" sur decisions/ (audit trail). Concepts updatables in-place (état courant, pas historique).
