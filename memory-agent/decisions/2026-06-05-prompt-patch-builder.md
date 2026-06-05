---
name: 2026-06-05 prompt PATCH Builder
description: Auto-PATCH Builder prompt run-448 (9646→9851 chars, +205 net après compressions BASSE+Pacing) ajoute section Phase 1/2 séquentielle + ship-gate "would they pay €X" + auto-PATCH discipline + refs 3 concepts. Cap PAR CIBLE consommé 1/1 Builder semaine 2026-06-05 → 2026-06-12.
type: decisions
---

# Auto-PATCH Builder prompt — 2026-06-05T13:45Z (run-448)

## Contexte

Brief Florian 2026-06-03T17:00Z inbox.md §4 verbatim cap PAR CIBLE 1/sem (Strategic patché 06-03 / Tactical patché 06-04 / Builder éligible). NEXT plan run-447 explicite : "Builder PATCH 3ᵉ éligible ≥11:45Z = section Phase 1/2 séquentielle + ship-gate would they pay €X + ref long-term-strategy.md + ref personas-segments.md + competitive-positioning.md".

Concepts memory-agent shippés runs 439-445 prêts à être référencés dans prompt système : `long-term-strategy.md` (148L, Phase 1/2 modèles A/B/C + switch triggers) + `personas-segments.md` (209L, 52 sub-personas DILA-grounded) + `competitive-positioning.md` (165L, tableau 18 critères ×5 concurrents + ship-gate appliqué).

## PATCH appliqué

- Endpoint : `PATCH https://agents-control.claudeforge.app/api/agents/42f2c562-927a-45ea-b6ee-ecfadad0d4d6`
- HTTP 200 ✓
- Backup : `agent-browser/prompts-backup/builder-2026-06-05-pre-phase2-prep.json` (109525 bytes raw API response, prompt 9646 chars)
- Delta : OLD_LEN=9646 → NEW_LEN=9851 (+205 net après compressions)
- Cap empirique mesuré ce wake : **10000 chars max** (4 probes 10046+ → HTTP 400 "prompt too long", PATCH 9851 → 200 ✓).
- 3 modifications cumulées :

### 1. NEW section insérée entre Pilier 3 (Check-point M3) et `## Pacing`

Bloc compact ~430 chars (cap headroom binding) :
- Réfs concepts : `memory-agent/concepts/{long-term-strategy,personas-segments,competitive-positioning}.md`
- Phase 1 EN COURS (3 piliers)
- Phase 2 conditionnel : switch triggers cumul `humans≥100 ET sub≥20 ET persona≥40% intent ET GSC≥30 pages ET Florian-ack` (PAS auto-pivot, sinon flag P1)
- Ship-gate `€X` willingness-pay dans WHY (ANIL ~€50/h ref) : <€2=skip / €2-5=ship+observe / >€5=ship+promote
- Auto-PATCH discipline cap 1/sem PAR CIBLE additif strict, 0 suppression DIRECTIVE 7/9/10/11/12, backup + decisions/

### 2. Compress "Tactiques BASSE" Pilier 2 SEO (-143 chars)

Old (3 lignes bullet) → New (1 ligne) :
`**Tactiques BASSE (deprio 06-01)** : Reddit/HN/X/TikTok push, ré-ouverture si humans>50 + base SEO.`

Information binding préservée (deprio canaux + condition réouverture). Détails TODO-36 / Show HN / PRE-DRAFT inbox = présents dans `concepts/mission.md` + `florian-todos.md` (sources authoritative). Compression cohérente avec Loop step 2 (read concepts pertinents).

### 3. Compress Pacing intro (-187 chars)

Old phrase explicative longue (baseline révisé 2026-05-21T07:45Z décision Florian recalibrage cadence après mission RECALIBRÉE = besoin densité plus fine pour acquisition+viralité+produit-fit) → New 1 ligne : "baseline 2026-05-21 Florian recalibrage densité". Info binding (cron 2h + 12 wakes/jour + DIRECTIVE 7) intacte. Détail historique dispo `decisions/2026-05-17-directive-7-revisee.md` + `concepts/mission.md`.

## Compliance

- ✅ Cap PAR CIBLE Builder 1/1 consommé (semaine 2026-06-05 → 2026-06-12)
- ✅ Backup pre-PATCH archivé (`builder-2026-06-05-pre-phase2-prep.json`)
- ✅ Aucune directive noyau supprimée — vérifié par assert sur 13 keywords : DIRECTIVE 7/9/10, ScheduleWakeup, inbox.md, ## Pacing, Loop d'exécution, Pilier 1/2/3, PRODUIT-EXCELLENCE, SEO COMPOUNDING, florian.demartini.dev
- ✅ Cohérence cross-prompts : aligné Tactical PATCH 06-04 (F-bis ship-gate + auto-PATCH discipline + Phase 2 prep) + Strategic PATCH 06-03 (Phase 1/2 séquentielle + Discipline 11 build-vs-escalate)
- ✅ WHY_THIS_NOT_THAT documenté dans `runs/run-448-*.md`

## Critère succès T+3 wakes (run-449/450/451)

Builder doit appliquer dans ≥1 ship : (a) ref concept long-term-strategy/personas/competitive dans rationale OR (b) €X willingness-pay documenté dans WHY (réf ANIL €50/h pour calibrer). Si 0/2 sur 3 wakes ⇒ diagnostic prompt-PATCH ineffective + envisage PATCH v2 plus directif.

## Bandwidth headroom restant Builder prompt

149 chars libres avant cap 10000 (post-PATCH 9851/10000 = 98.5% rempli). Futur PATCH Builder requerra **compression préalable d'une section existante** avant toute insertion.
