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

### Sub-règle SB-1.1 — ENRICH file existant ⇒ même seuil Full ritual que NEW FILE

**Effective** : 2026-06-10T19:42Z run-511, codifiée post critic-72 #3 ★ verdict "ENRICH +103L variante §a/§b sans Copyability+Moat+€X = drift DIR 10 §b" (Saint-Ouen ENRICH run-507).

**Texte** : *"ENRICH d'un fichier existant user-facing déclenche le même seuil Full ritual qu'un NEW FILE : si net-add ≥100L user-facing au fichier (mesuré post-Edit), Builder DOIT inclure Copyability% + Moat category + ship-gate €X dans le WHY, MÊME pour un ENRICH validé par prescription Strategic-N §6 (carve-out de ban NEW FILE)."*

**Triggers anti-récidive** :
- ❌ Si Builder ENRICH +100L user-facing en variante §a/§b sans Copyability+Moat+€X (même sur ENRICH explicit-autorisé Strategic) → STOP, switch Full ritual obligatoire au moment du WHY pré-ship.
- ✅ Si ENRICH 50-99L user-facing avec WHY substantive (nouvelle section différenciée, FAQPage JSON-LD nouveau, données moat ajoutées) → variante §a/§b OK avec mention §a substance MAIS Copyability+Moat+€X RECOMMANDÉS (zone gris).
- ✅ Si ENRICH ≤50L fix chirurgical (typo, lien, métadonnée seule, 1 section refactor sans data add) → variante §a/§b OK sans Copyability+Moat+€X (L161 cohérent).
- ✅ Si ENRICH ≥100L mais 100% scaffold/internal (memory-agent/, dataset, ledger, doc) → variante §a/§b OK avec §a substance.

**Anti-loophole** : NE PAS contourner via "Strategic-N §6 autorisé ENRICH ⇒ pas Full ritual nécessaire". Le carve-out §6 lève le **ban NEW FILE** PAS le seuil discipline §b DIR 10. L'autorisation Strategic = quoi shipper, pas comment justifier.

### Règle SB-1 (originale, conservée intacte ci-dessous)

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

## Règle SB-3 light — DIR 10 §b file integrity (run-N.md MUST exist post-commit ledger)

**Effective** : 2026-06-09T19:43Z run-499+, sans cap (discipline permanente hygiène audit-trail).

**Texte** : *"Chaque wake qui append une ligne `ledger.md` DOIT créer le fichier correspondant `runs/run-${N}-*.md` AVANT ou DANS le même commit. Pré-commit check : `ls runs/run-${N}-*.md` doit retourner ≥1 fichier. Si run-N file manquant post-commit ledger ⇒ reactive-correction wake-suivant + 1 mention NEXT plan (PAS compteur tracker METRIC vanity, codification = solution structurelle)."*

**Source** : critic-70 #3 ★ 2026-06-09T19:00Z post run-498. Précédent : run-497 commit `96f09d0` 15:43Z = ledger-append-only sans `runs/run-497-*.md` créé = ritual DIR 10 step 7 partiel. Reactive-corrected run-498 file créé. Rétro-création **interdite** (faisifierait timing). STOP critic-70 #3 anti-vanity METRIC : NE PAS propager compteur `wake_file_missed_cumul=N` propagation verbose ledger (1 mention NEXT plan suffit). Codification SB-3 light = solution structurelle > METRIC incrémental.

**Triggers anti-récidive** :
- ❌ Si Builder s'apprête à `git commit` ledger sans run-N.md créé → STOP, `Write` run-${N}-${TIMESTAMP}.md d'abord, puis commit combiné.
- ✅ Si run-N.md créé pré-commit + ledger append + 1-shot commit → OK.
- ✅ Cas exception explicite (ex: rollback wake d'urgence où run-N file rédigé pas encore committé) → mention NEXT plan + reactive-correction wake-suivant max.

**Cooldown override** : aucun. Discipline permanente. Tactical critic peut flagger ≥1 récidive futur (run-N.md absent post-commit ledger).

**Anti-loophole** : NE PAS contourner via "ledger seul = source of truth". Mémoire-agent MEMORY.md L6 explicite : `inbox.md + runs/ restent archives append-only GitHub-public (transparence + rollback)` ⇒ run-N.md = audit-trail public obligatoire en plus du ledger.

**Why "light"** : pas Full ritual SB-1 (≥100L user-facing) ni SB-2 (ECLI Judilibre log) — juste check pré-commit `ls` 1 ligne shell, donc tag "light".

## Update protocol

Si Florian patch HUMAN_DIRECTIVE.md L160 → archiver cette règle SB-1 (déprécié), keep historical reference. Si nouvelle règle SB-N émerge audit futur → append section.

## Historique

- 2026-05-21T21:37Z run-336 — concept créé, règle SB-1 binding ce wake. Flag inbox.md HEAD avec 3 options Florian arbitrage.
- 2026-06-03T19:50Z run-427 — SB-2 ECLI Judilibre log persistant codifié post-rollback 3 fausses ECLI Marseille (decisions/2026-06-03-marseille-jurisprudence-rollback.md).
- 2026-06-09T19:43Z run-499 — SB-3 light file integrity codifié post run-497 ledger-only commit `96f09d0` (run-497 file missed reactive-corrected run-498). Critic-70 #3 ★ STOP anti-vanity METRIC `wake_file_missed_cumul` substitué codification structurelle.
- 2026-06-10T19:42Z run-511 — Sub-règle SB-1.1 ENRICH file existant codifiée post critic-72 #3 ★ verdict drift Saint-Ouen ENRICH +103L variante §a/§b sans Copyability+Moat+€X (run-507). Clarif seuil Full ritual = même critère que NEW FILE pour ENRICH user-facing net-add ≥100L. Carve-out Strategic §6 lève ban NEW FILE pas seuil discipline §b.
