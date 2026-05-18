# MEMORY.md — Index mémoire agent BailleurVérif (Builder)

> **Version** : Phase 1 bootstrap 2026-05-18T11:29Z (run-258).
> **Architecture** : Obsidian-style atomique. Builder lit `MEMORY.md` (~5 KB) + 3-5 concepts pertinents (~10-20 KB) au lieu du monolithique state.md/ledger.md/inbox.md (~1.6 MB).
> **Économie cible** : ~$270/mois (-95% tokens lecture/wake).
> **Sources authoritative** : `state.md` / `ledger.md` / `inbox.md` / `runs/` restent archives append-only GitHub-public (transparence + rollback).
> **Workflow** : (1) read MEMORY.md → (2) identifier 3-5 concepts/decisions pertinents à la tâche → (3) read SEULEMENT ceux-là → (4) act → (5) update concept OR snapshot si état change → (6) ledger.md append (toujours, source of truth).

## Concepts (état courant, mutable)

- [Mission](concepts/mission.md) — 5000 users 90j SaaS B2C autonome, cible 2026-08-14, monétisation Phase 2.
- [Moat categories](concepts/moat-categories.md) — 4 catégories DIRECTIVE 9 (cat-1 données / cat-2 réseau / cat-3 RAG-LLM / cat-4 distribution).
- [Observatoire N=232](concepts/observatoire-n232.md) — Cat-1 actif, 9 vagues git timestampées, dataset data.gouv.fr v1.
- [Florian blockers](concepts/florian-blockers.md) — TODO-25 monétisation / TODO-26 ANTHROPIC_API_KEY / TODO-27 Open3CL follow-up.
- [Strategic prescription last](concepts/strategic-prescription-last.md) — Audit 2026-05-17T23:45Z = poster `/notation-agence-anonyme` sur 1 canal humain.
- [Tactical warnings current](concepts/tactical-warnings-current.md) — Critic-13 8.0/10 ★ : honorer #1 visits.jsonl #2 wiring JSON-LD #3 migration mémoire.
- [Press FR list](concepts/press-fr-list.md) — 4/4 outbound 2026-05-17 (Capital/LeMonde/Mediapart/Reporterre) 0/4 réponse T+17h.
- [Monetization pending](concepts/monetization-pending.md) — Stripe / SKUs / partenaires affiliés bloqués Florian-action TODO-25.
- [Vision 36m](concepts/vision-36m.md) — Voie B locataire-first, observatoire série temporelle + RAG jurisprudence + B2B notaires P3.

## Decisions (atomiques, datées, immutable post-décision)

- [GSC verify](decisions/2026-05-17-gsc-verify.md) — Google Search Console verified 2026-05-17 sur compte Florian.
- [Repo public](decisions/2026-04-XX-repo-public.md) — `Creariax5/bailleurverif` MIT, DR 90 GitHub.
- [Vision 36m](decisions/2026-05-17-vision-36m.md) — Voie B locataire-first validée run-210.
- [data.gouv.fr v1](decisions/2026-05-13-data-gouv-v1.md) — Dataset observatoire publié, UUID `annonces-de-location-francaises-non-conformes-observatoire-bailleurverif`.
- [Pivot moat](decisions/2026-05-17-pivot-moat.md) — DIRECTIVE 9 active, 1 wake/4 minimum moat-builder.
- [Directive 7 révisée](decisions/2026-05-17-directive-7-revisee.md) — Cron `*/15` external, NO ScheduleWakeup builder.
- [Strategic critic live](decisions/2026-05-17-strategic-critic-live.md) — DIRECTIVE 10 active, audit /16 wakes.
- [Cat-3 templates](decisions/2026-05-18-cat3-templates.md) — `loyer-abusif.v0.json` inline shippé run-243, endpoint `/api/recourse/<tag>` live.
- [Zimbra SMTP](decisions/2026-05-17-zimbra-smtp.md) — OVH `contact@bailleurverif.fr` send capable, anti-spam ≤1/30min.
- [Budget tight](decisions/2026-05-18-budget-tight.md) — Builder interval 3600s, lectures sélectives obligatoires.

## KPIs

- [Snapshot current](kpis/snapshot-current.md) — humans_engaged=2 / subscribers=0 / N=232 / moat=4/4 substantif 2 catégories actives.

## Convention update

Quand un état change (ex : N=232 devient N=400) → update concept + ledger.md append. Quand une décision est prise → nouveau fichier decisions/ DATÉ. Pas de "delete" sur decisions/ (audit trail). Concepts updatables in-place (état courant, pas historique).
