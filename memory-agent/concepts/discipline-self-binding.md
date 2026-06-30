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

## Règle SB-4 — IndexNow ship-time strict cap 1 URL (anti-théâtre cumulatif)

**Effective** : 2026-06-11T15:45Z run-521+, sans cap (discipline permanente affinement ban).

**Texte** : *"IndexNow ping autorisé UNIQUEMENT au ship-time d'une NEW page user-facing OR PATCH substantive ≥+50L FAQ/section utility, cap STRICT 1 URL ship-time, 0 batch ≥3 URLs hors-ship, 0 round wake-only re-ping même URL. Symétrie 1:1 avec pattern Indexing API Google. Si Builder PATCH ≥+50L section substantive utility d'une page existante OR ship NEW page user-facing → `agent-browser/indexnow_ping.py <url-unique>` autorisé au moment du commit ship. Sinon 0 IndexNow."*

**Source** : brief Florian 2026-06-11T08:00Z inbox.md HEAD (T+~7h45). Affinement verdict run-315 "IndexNow théâtre confirmé" qui mesurait mauvais signal (0 hit Bingbot T+6h server.log ≠ ping inutile, mécanisme alimente crawl queue priority Bing, hit peut arriver H+18/36 outside window). Symétrie avec pattern Indexing API Google ship-time 1 URL spec (audit-52 §11). Bing+Yandex+DuckDuckGo+Seznam = ~5-7% SERP FR — coût marginal 1 ligne code POST `api.indexnow.org/indexnow` avec `bailleurverif-key.txt` (clé `b0d2add1441ec161a5ba4ad975987bc8` active depuis run-XX, 0 secret nouveau).

**Triggers anti-récidive** :
- ❌ Si Builder s'apprête à ping IndexNow ≥2 URLs même wake OR re-ping URL déjà ping ≤7j OR ping batch hors ship-time → STOP, ban théâtre cumulatif préservé.
- ❌ Si Builder ping IndexNow sur PATCH ≤+50L typo/lien/métadonnée seule (non-substantive) → STOP, hors-cap critère substantive.
- ✅ Si Builder ship NEW user-facing page (≥100L Full ritual) + commit → `python3 agent-browser/indexnow_ping.py <url-nouvelle>` 1 ligne post-commit OK.
- ✅ Si Builder PATCH +≥50L section substantive utility (nouvelle FAQ JSON-LD, section data différenciée, ECLI cat-3 enrichi) → `python3 agent-browser/indexnow_ping.py <url-patchée>` 1 ligne post-commit OK.
- ✅ Si bans Strategic-N audit explicitent "🚫 IndexNow" intégralement (ex: audit-57 bans 19/19) → SB-4 SUSPENDU temporairement durant l'audit, attendre audit suivant pour réactivation (hiérarchie Strategic > SB Builder, sauf brief Florian explicit override).

**Cooldown override** : aucun. Affinement permanent. Si Florian patch HUMAN_DIRECTIVE.md restrict IndexNow → archiver SB-4. Si Strategic Critic ban explicit IndexNow audit-N → SB-4 dormant durant audit-N window.

**Anti-loophole** : NE PAS contourner via "batch 2 URLs autorisé car 1+1 ships" — 1 URL/ship STRICT, jamais cumul. NE PAS contourner via "re-ping même URL après 7j" — 1 ping/URL/lifetime strict (re-ping = théâtre cumulatif confirmé run-315).

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

## Règle SB-5 — Florian-silent post-fallback explicit ack = N/A tactical priorité (anti-flag récurrent récursif)

**Codifiée** : 2026-06-16T19:44Z run-583 honored critic-84 #2 ★★ recommandation (b).

**Énoncé** : Lorsqu'un blocker dépendant Florian (ex : PAT GitHub expiré) a déjà reçu un ack-fallback explicite ("commit local + pull manuel" inbox.md 17:50Z 06-15 ack run-570), les wakes subséquents NE re-flag PAS le blocker en HEAD-priorité tactique. Dette transparence GitHub-public (commits ahead unpushed) reconduit silently jusqu'à Florian-action proactive. Counter visits/commits passe en `ledger`-only ; pas de section dédiée snapshot ; pas de mention "BLOCKER" verbatim runs 5+ consécutifs.

**Why** : critic-84 #2 ★★ a observé 5+ wakes consécutifs (runs 570→582) verbatim `GH PAT BLOCKER T+~Xh restant` decrementing = pattern récurrent récursif = surface inutile sustained audit-trail. Florian a déjà choisi le mode (fallback commit local). Re-flag ≠ ajoute information ≠ accélère décision.

**Triggers de réactivation** : (a) Florian-action proactive (PAT replace `.env` GH_TOKEN) → 1 ligne ledger acknowledgment + push reprend ; (b) Florian-message inbox HEAD nouveau topic PAT (override fallback) ; (c) impact opérationnel critique (ex : prod down) — pas dette transparence.

**Anti-loophole** : ne s'applique PAS à blockers OPS impactant prod (server down, scraper KO, dataset perdu) — reste flag HEAD priorité.

**Update protocol** : Si Florian patch HUMAN_DIRECTIVE.md ajoute règle "PAT obligatoire toujours flagué" → archiver SB-5. Sinon affinement permanent.

## Règle SB-6 — Wake gated = verify-and-stop (anti-filler supply-side)

**Codifiée** : 2026-06-24T08:00Z run-646 honored critic-95 #1 (verdict 7.0/10 : « 643-645 = rechute en busywork dès que tes vrais tests sont gated »).

**Énoncé** : Lorsque les deux leviers d'avancement réels d'un wake sont simultanément bloqués — (a) test/mesure dépendant Florian (ex : GSC API TODO-39, baseline `gsc_inspect` 32×403) ET (b) mesure dépendante du temps non-échue (ex : `signup_confirm_clicked` deadline 06-26, `recourse_letter_copied` deadline 06-30) — Builder NE fabrique PAS un refresh page / publish canal / fix cosmétique « pour faire quelque chose ». Le wake légitime = **verify-and-stop** : (1) vérifier l'état des gates (1-3 commandes), (2) logger le constat, (3) optionnel 1 action d'hygiène/intégrité VRAIE (defect réel servi en prod, source-of-truth d'un sous-agent à confirmer) OU codification discipline, (4) stop. Un wake M0/minimal est un OUTCOME VALIDE quand tout est gated — pas un échec à compenser par du volume.

**Why** : critic-94 (STOP#3) puis critic-95 ont observé 6 wakes (640-645) dont 0 n'a bougé l'acquisition ; dès que les vrais tests étaient gated, Builder produisait refresh Villeurbanne (643) + publish dev.to redondant sur fausse prémisse (644) + nettoyage de sa propre erreur (645). Le filler supply-side donne l'illusion de productivité mais (i) ne touche pas la contrainte liante (acquisition, gsc~8<30), (ii) crée de la surface d'erreur (chiffres faux, log local ≠ vérité), (iii) brûle des tokens sans signal. Mieux vaut un wake court honnête.

**Triggers anti-récidive** :
- ❌ Si gate-Florian ET gate-temps tous deux fermés ET Builder s'apprête à refresh une city-page / publish un canal / enrichir une page « parce qu'il faut agir » → STOP, verify-and-stop.
- ❌ Si l'action envisagée est un 2ᵉ+ refresh/enrichissement supply-side dans une fenêtre où humans=flat ET 0 nouveau signal funnel → STOP (anti-boucle 643-645).
- ✅ Hygiène/intégrité VRAIE autorisée même en wake gated : defect réel servi en prod (chiffre faux actif moat public), source-of-truth d'un sous-agent à reconcilier (critic-95 #3), codification discipline self-binding, correction audit-trail.
- ✅ Action acquisition NON-gated ET NON-GEL'd réelle autorisée (mais cf. anti-loophole affiliés ci-dessous).
- 📁 **Convention archive SB-6 pur (codifiée 2026-06-30 run-721, tactical audit-108 #2)** : un wake SB-6 pur (0 event qualifiant, 0 action substantive au-delà du verify) = **rituel en `ledger.md` SEUL**, PAS de `runs/run-N.md`. Créer un fichier run dédié pour un constat « rien n'a bougé » re-fabrique du filler supply-side. Un wake SB-6 qui porte une vraie action (ex : cette codification) PEUT créer son run-N.md. Trancher une fois, ne PAS osciller (audit-108 stop#3), ne PAS back-fill les runs 719/720 ledger-only (corrects).

**Anti-loophole affiliés (critic-95 #2)** : « brancher 1 lien affilié » N'EST PAS un lever zéro-Florian non-gated disponible : (i) monétisation toute forme est GEL'd par mission tant que `humans_engaged < 100` (live 7-9 conf-adj) ; (ii) les placeholders `?ref=PENDING_FLORIAN` (strategic-13 run-328) requièrent des IDs de programmes affiliés réels que seul Florian peut fournir (self-policy run-121 : 0 signup nominatif automatisé). Donc critic-95 #2 reste documenté mais NON-actionné contre la GEL binding. Réactivable si humans≥100 OR Florian fournit IDs + lève GEL explicitement.

**Cooldown override** : aucun. Affinement permanent. Si Florian rouvre un canal distribution (option b inbox HEAD 20:00Z) OR lève la GEL monétisation → la définition de « gated » se rétrécit (un lever acquisition redevient disponible), SB-6 reste mais ses triggers s'assouplissent.

## Update protocol

Si Florian patch HUMAN_DIRECTIVE.md L160 → archiver cette règle SB-1 (déprécié), keep historical reference. Si nouvelle règle SB-N émerge audit futur → append section.

## Historique

- 2026-05-21T21:37Z run-336 — concept créé, règle SB-1 binding ce wake. Flag inbox.md HEAD avec 3 options Florian arbitrage.
- 2026-06-03T19:50Z run-427 — SB-2 ECLI Judilibre log persistant codifié post-rollback 3 fausses ECLI Marseille (decisions/2026-06-03-marseille-jurisprudence-rollback.md).
- 2026-06-09T19:43Z run-499 — SB-3 light file integrity codifié post run-497 ledger-only commit `96f09d0` (run-497 file missed reactive-corrected run-498). Critic-70 #3 ★ STOP anti-vanity METRIC `wake_file_missed_cumul` substitué codification structurelle.
- 2026-06-10T19:42Z run-511 — Sub-règle SB-1.1 ENRICH file existant codifiée post critic-72 #3 ★ verdict drift Saint-Ouen ENRICH +103L variante §a/§b sans Copyability+Moat+€X (run-507). Clarif seuil Full ritual = même critère que NEW FILE pour ENRICH user-facing net-add ≥100L. Carve-out Strategic §6 lève ban NEW FILE pas seuil discipline §b.
- 2026-06-11T15:45Z run-521 — SB-4 IndexNow ship-time strict cap 1 URL codifiée post brief Florian 08:00Z (decisions/2026-06-11-indexnow-ban-affined.md). Affinement verdict run-315 "IndexNow théâtre confirmé" : ban global → cap 1 URL/ship-time NEW page OR PATCH ≥+50L substantive. Symétrie 1:1 Indexing API Google. SB-4 dormant durant Strategic-N ban explicit (audit-57 bans 19/19 = SB-4 suspendu jusqu'audit-58).
- 2026-06-16T19:44Z run-583 — SB-5 Florian-silent post-fallback ack = N/A tactical priorité codifiée post critic-84 #2 ★★ recommandation (b). Anti-flag récurrent récursif PAT GitHub blocker (5+ wakes verbatim 570→582). Fallback Florian explicit 17:50Z 06-15 = mode autorisé ; re-flag HEAD ≠ accélère décision. Triggers réactivation 3 carve-outs explicites.
