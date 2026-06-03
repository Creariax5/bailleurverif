---
name: Discipline self-binding (Builder-side rules complétant HUMAN_DIRECTIVE)
description: Règles auto-imposées par Builder sans éditer HUMAN_DIRECTIVE.md (territoire Florian). Codifié pour anti-récidive. Sera consolidé par Florian au prochain patch HUMAN_DIRECTIVE explicite.
type: project
---

# Concept : Self-binding discipline rules (Builder side)

**Pourquoi** : Quand un audit tactical/strategic prescrit un patch HUMAN_DIRECTIVE.md mais Florian est silent, Builder ne peut PAS éditer HUMAN_DIRECTIVE.md autonome (territoire Florian, anti-vol décision). MAIS Builder peut auto-binder règle plus stricte côté concept pour anti-récidive en attendant arbitrage Florian.

## Règle SB-1 — DIRECTIVE 10 §b L160 NEW FILE user-facing strict

**Effective** : 2026-05-21T21:37Z run-336+, jusqu'à Florian arbitrage explicite inbox.md HEAD options (a)/(b)/(c).

**Texte** : *"Tout NEW FILE ≥100L user-facing = Full ritual obligatoire (Copyability% + Moat category fields explicites) MÊME SI le fichier est marqué démo `noindex,nofollow` non-intégré au moment du ship, dès lors qu'il est servi par HTTP server prod (curl 200 OK depuis bailleurverif.fr)."*

**Source** : audit-32 tactical 2026-05-21T18:55Z ★★★ #1 (run-333 récidive `share-card.js` 118L). Lecture stricte L95 HUMAN_DIRECTIVE.md ("tout nouveau fichier user-facing/sub-agent prompt = Full ritual obligatoire"). 

**Triggers anti-récidive** :
- ❌ Si Builder s'apprête à ship NEW FILE `*.js` / `*.html` / `*.py` user-facing ≥100L en variante §a/§b sans Copyability+Moat → STOP, switch Full ritual obligatoire.
- ✅ Si fichier ≥100L mais 100% scaffold/internal (test, fixture, doc concept memory-agent/, dataset csv, sub-agent prompt déjà existant patch) → variante §a/§b OK avec justification §a substance.
- ✅ Si fichier <100L user-facing → variante §a/§b OK per L161 fix chirurgical ≤50L (zone 50-99L = gris, default variante §a/§b avec mention §a).

**Cooldown override** : si Florian reply inbox.md HEAD options (b) ou (c) → override immédiat self-bind, codifier nouvelle règle. Si silent ≥48h ≥2026-05-23T21:37Z → escalade audit-33 tactical pour confirmation default (a) tient.

**Anti-loophole** : NE PAS différer cette règle sous prétexte "PAS 3 piliers recalibrés". Discipline méta = compose 3 piliers (qualité code + audit trail moat-builder). Patch §b NE PAS différé.

## Règle SB-2 — ECLI affirmée user-facing ⇒ log Judilibre persistant obligatoire (DISCIPLINE 12)

**Effective** : 2026-06-03T19:50Z run-427+, sans cap (discipline permanente trust juridique).

**Texte** : *"Tout ECLI Cass./CA affirmée dans contenu user-facing (page HTML / API recourse / sub-agent draft) DOIT avoir un log persistant `agent-browser/judilibre_<context>_<pourvoi-id>.log` joint au ledger du wake où affirmée. Pourvoi→ECLI mapping verification via PISTE Judilibre query (chamber + pourvoi) pre-ship obligatoire. Log = preuve ECLI correspond bien au pourvoi cité au date affirmée."*

**Source** : run-426 ledger a affirmé "3 ECLI vérifiées via PISTE OAuth ✓" mais sans log persistant. Verif critic-58 #3 run-427 a découvert 3/3 ECLI INCORRECTES :
- 06-22.069 → vraie ECLI 2008:C300110 (pas C300321)
- 13-17.289 → vraie ECLI 2014:C300721 (pas C300747, sommaire = chauffage pas trouble jouissance)
- 15-26.557 → vraie ECLI 2016:C310470 (pas 2017:C300179, date 17/11/2016 pas 9/02/2017)

URLs `courdecassation.fr/decision/{id}` shippées pointaient vers IDs inexistants/non-matching. Risque trust juridique majeur + propagation LLM ingest contaminé.

**Triggers anti-récidive** :
- ❌ Si Builder s'apprête à ship ECLI sans `agent-browser/judilibre_*.log` joint à wake ledger → STOP, query PISTE d'abord ou remove ECLI claim.
- ✅ Si ECLI déjà sauvegardé dans `agent-browser/judilibre_<topic>_<pourvoi-clean>.log` JSON output PISTE search → OK ship + reference log path ledger.
- ✅ Si mention contextuelle non-ECLI ("Cour d'appel Aix-en-Provence article R. 311-1 COJ" sans pourvoi spécifique) → vérifiable Légifrance code organisation judiciaire, OK.

**Cooldown override** : aucune — discipline permanente. Tactical critic peut bloquer prochain wake si non-respect.

**Anti-loophole** : NE PAS contourner via affirmation "vérifié PISTE OAuth" sans log persistant. Trace ledger = preuve. Run-426 = exemple anti-pattern.

## Update protocol

Si Florian patch HUMAN_DIRECTIVE.md L160 → archiver cette règle SB-1 (déprécié), keep historical reference. Si nouvelle règle SB-N émerge audit futur → append section.

## Historique

- 2026-05-21T21:37Z run-336 — concept créé, règle SB-1 binding ce wake. Flag inbox.md HEAD avec 3 options Florian arbitrage.
- 2026-06-03T19:50Z run-427 — SB-2 ECLI Judilibre log persistant codifié post-rollback 3 fausses ECLI Marseille (decisions/2026-06-03-marseille-jurisprudence-rollback.md).
