---
name: 2026-06-04 prompt PATCH Tactical Critic
description: Auto-PATCH Tactical Critic prompt run-433 (8503→9931 chars, +1428) ajoute dimensions audit Phase 2 prep + ship gate would they pay + auto-PATCH discipline. Cap PAR CIBLE consommé 1/1 Tactical semaine 2026-06-04 → 2026-06-11.
type: decisions
---

# Auto-PATCH Tactical Critic prompt — 2026-06-04T07:43Z (run-433)

## Contexte

Brief Florian 2026-06-03T17:00Z `inbox.md` HEAD §4 verbatim : *"max 1 PATCH par catégorie (Builder / Tactical / Strategic) par semaine"*. Strategic-42 prescription `🚫 2ᵉ auto-PATCH semaine` = bad condensation (Strategic 1/1 consommé run-428 ≠ Tactical/Builder bloqués). Tactical-59 audit 07:00Z explicite hypothèse + recommandation `★★★` action #1 cap PAR CIBLE.

## PATCH appliqué

- Endpoint : `PATCH https://agents-control.claudeforge.app/api/agents/8f366adc-2e99-467a-bc0c-7fc71d0e7489`
- HTTP 200
- Backup : `agent-browser/prompts-backup/tactical-critic-2026-06-04-pre-phase2-prep.json`
- Delta : OLD_LEN=8503 → NEW_LEN=9931 (+1428, +16.8%)
- Modifications additives strictes (0 suppression directive noyau) :

### 1. Insertion section `F-bis` avant `G. Verdict`

Bloc unique compacté ~1200 chars couvrant :
- **Phase 2 prep (brief 06-03T17:00Z A+B+C+D)** : check `intent_signal` enum `/api/subscribe` (6 valeurs whitelistées) + `subscribers_by_intent` snapshot + feedback widget post-verdict `user-feedback.jsonl` + auth magic-link stub + `/dashboard` placeholder + `/api/v1/...` semver + `personas-segments.md` ≥30 sub + `long-term-strategy.md` + `competitive-positioning.md`.
- **Switch triggers Phase 2** : si ≥2 atteints (humans≥500 / sub≥50 / persona dominant / inbound_b2b≥3 / competitor risk) ⇒ escaladé inbox HEAD. Auto-pivot sans Florian-ack ⇒ flag P1.
- **Ship gate "would they pay €X"** (brief 06-03T16:30Z) : chaque feature shippée a-t-elle `€X` documenté dans WHY_THIS_NOT_THAT ? <€2 polish / €2-5 ship+observe / >€5 ship+promote. Sans `€X` ⇒ flag drift qualité.
- **Pages programmatiques data unique** : chiffres observatoire / arrêté préfectoral / jurisprudence CA / FAQ DILA. Template plat dupliqué ⇒ flag thin-content.
- **Auto-PATCH discipline (brief §4)** : cap PAR CIBLE Builder/Tactical/Strategic /sem + backup + decisions/ + WHY_THIS_NOT_THAT + 0 suppression directive noyau (7/9/10/11/12) sinon flag P1.

### 2. Mise à jour `G. Verdict` ligne note globale

Old : `"trajectoire vers revenu passif sustainable (affiliés + signups réels + SEO compounding)"`
New : `"trajectoire vers humans_engaged>100 Phase 1 + prep Phase 2 SaaS + ship gate \"would they pay\" (mission 06-01 + briefs 06-03). Revenu passif = horizon Phase 2 conditionnel."`

## Compliance

- ✅ Cap PAR CIBLE Tactical 1/1 consommé (semaine 2026-06-04→2026-06-11)
- ✅ Backup pre-PATCH archivé
- ✅ Aucune directive noyau supprimée (7/9/10/11/12 intactes)
- ✅ Cohérence cross-prompts : aligné Strategic Critic (audit-42 NEW dimension Phase 2 prep proto-conforme) + Builder mission re-recalibrée 06-01
- ✅ Tactical-59 #1 ★★★ HONORED J+0 T+~43min après audit drop

## Critère succès T+2 audits

Tactical-60 + Tactical-61 doivent inclure ≥2 dimensions NEW (Phase 2 prep / ship gate / auto-PATCH discipline) dans rapport audit. Si 0/2 → diagnostic prompt-PATCH-ineffective.
