# Prompt PATCH — Strategic Critic — 2026-06-03T21:43Z

## Contexte

Florian brief inbox.md HEAD 2026-06-03T17:00Z verbatim : *"Dis à l'agent de faire tout ça lui-même, même modif son prompt et les critic et strategy si besoin."* Autorisation explicit auto-PATCH 3 prompts (Builder + Tactical + Strategic) via `PATCH /api/agents/{id}` agents-control API. Cap 1 PATCH/cible/semaine.

Tactical critic-58 ★★★ #1 (2026-06-03T19:00Z) flag 6h+ defer post-brief comme matérialisant pattern Florian verbatim 11:00Z *"Il aurait d'ailleurs dû prendre cette décision par lui-même"*. Run-428 = 1ʳᵉ application autonomie élargie auto-PATCH (cible safest = Strategic Critic, modifications additives uniquement).

## Cible PATCH

- **Agent ID** : `85c78e3b-6e4b-4bd5-84cf-5a675d1131b7`
- **Nom** : Saas Strategic Critic
- **Endpoint** : `PATCH $AGENTS_CONTROL_BASE/api/agents/85c78e3b-6e4b-4bd5-84cf-5a675d1131b7`
- **HTTP status** : 200 ✓ (T+~3 min après build patched prompt)
- **Verify persisted** : `curl GET /api/agents/{id}` ⇒ marker `Stratégie long terme Florian 2026-06-03` présent x1 dans `.prompt` ✓

## Delta

- **OLD chars** : 7418
- **NEW chars** : 8995
- **Delta** : +1577 chars (+21.3%)
- **Lignes ajoutées** : 9 (block A : Phase 1/2 + Discipline 11) + 1 (carve-out NEW page injecté dans question 6)
- **Lignes supprimées** : 0 (additif strict per Discipline auto-patch §3)

## Backup

`agent-browser/prompts-backup/strategic-critic-2026-06-03-pre-strategy-longterm.json` (49810 bytes, full JSON agent state pre-PATCH).

## Insertion 1 — après "DÉPRIORITISÉS 2026-06-01" (avant "Question stratégique permanente")

### Verbatim AJOUTÉ

```
**Stratégie long terme Florian 2026-06-03T17:00Z (binding)** :
- **Phase 1 (M0-M9 estimé) = état actuel** : produit gratuit utility, acquisition users + brand. Monétisation OFF. Mission RE-RECALIBRAGE 06-01 inchangé.
- **Phase 2 (M9-M12+ conditionnel)** : pivot SaaS scalable récurrent SI triggers atteints (≥50 subscribers + segmentation persona dominant émerge). Cible €10-50k€/mois récurrent.
- **Long terme cible** : vrai SaaS scalable via persona dominant (probablement bailleur multi-bien + alertes JORF + IRL/DPE/conformité continue, OU pivot B2B agences/syndics, selon signal user).
- Prescriptions Strategic doivent servir **préparation Phase 2** (signal capture user qualitatif / rails techniques pré-construits non-exposés / narrative pivot pré-construit) ≠ déclencher pivot Phase 2 immédiat.

**Discipline 11 build-vs-escalate (Florian explicit 2026-06-03T11:00Z)** : Builder décide AUTONOMIE par défaut (build small + ship). Escalade Florian = exception réservée (auto-PATCH prompts agents / dépense >50€ unique ou >100€/mois / engagement légal / brand decisions). NE PAS prescriber escalade Florian sauf cas listé. Si choix prescription = "déléguer Builder via build" vs "escalader Florian" → défaut = Builder build.
```

### Pourquoi

Brief Florian 17:00Z = stratégie séquentielle binding. Strategic Critic doit auditer en cohérence Phase 1/2 sinon prescriptions risquent recommander pivot SaaS prématuré (humans=4 << 50 trigger Phase 2). Discipline 11 codifie default "Builder build" vs escalade Florian (ack pattern frustration verbatim 11:00Z).

## Insertion 2 — dans question 6 PRESCRIPTION (après "Interdiction prescriptions Telegram itération")

### Verbatim AJOUTÉ

```
**Carve-out NEW page** : si Florian brief inbox.md propose explicit Action = NEW page user-facing (ex Action B/C brief 2026-06-03T17:30Z DPE calendrier + askfrance), prescription Strategic PEUT lift ban NEW FILE (Builder décide ritual SB-1 + Full ritual SB-1 ≥100L). Sinon ban NEW FILE strict reste défaut (focus enrich+sharpen vs scaffolding).
```

### Pourquoi

Brief Florian 17:30Z propose 4 actions A-D dont 3 NEW pages (DPE calendrier 2025/2028/2034 + questions-reelles-bailleurs-fr + questions-frequentes-encadrement-loyer). Sans carve-out, ban audit-41 "🚫 NEW FILE" + audit-42+ prescriptions defaut "STOP NEW FILE" empêcheraient Builder honorer brief Florian explicit. Discipline §c-bis (Brief Florian > Strategic) déjà autorisait override case-par-case mais codifie ici dans le prompt Strategic même = audit cohérent au lieu de carve-out adhoc.

## Discipline auto-patch (binding, brief 17:00Z §3-§6) respectée

- §1 WHY_THIS_NOT_THAT obligatoire ✓ (cf runs/run-428.md)
- §2 Document `decisions/2026-06-03-prompt-patch-strategic-critic.md` ✓ (ce fichier)
- §3 Modifications additives uniquement ✓ (diff = +9 lignes block A + +1 ligne injection question 6, 0 suppression)
- §4 Cap PATCH 1/cible/sem ✓ (0/1 consommé Strategic, ce PATCH = 1/1)
- §5 Cohérence cross-prompts → Builder prompt (mission.md concept) + Tactical déjà alignés Phase 1+2 implicite ; PATCH Builder/Tactical séparés différés future wakes (cap 1/sem chacun)
- §6 Backup pré-PATCH ✓ (cf chemin ci-dessus)

## Critère succès

- Audit-42+ Strategic doivent désormais référencer Phase 1/2 binding (pas just Pilier 1+2+3)
- Audit-42+ ne doivent plus prescrire escalade Florian sauf cas Discipline 11 listé
- Audit-43+ doivent honorer carve-out NEW page si Florian brief Action explicit
- Rollback condition : si audit-42 incohérent ou Strategic recommande pivot Phase 2 immédiat avant triggers atteints → restore backup.

## Liens

- Brief Florian 17:00Z verbatim : `inbox.md` HEAD ~L60-110
- Brief Florian 17:30Z (carve-out source) : `inbox.md` HEAD ~L1-60
- Tactical critic-58 prescription : `inbox-from-critic.md` HEAD (2026-06-03T19:00Z)
- Run : `runs/run-428.md`
- Ledger entry : `ledger.md` block run-428 2026-06-03T21:43Z
