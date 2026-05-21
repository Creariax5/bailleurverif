# Directives en cours — Florian → Agent

> Ce fichier contient les directives actives. L'agent le lit en premier à chaque réveil. Toute directive écrite ici OVERRIDE le runbook par défaut.
>
> **Condensé 2026-05-21T11:00Z** : retiré DIRECTIVE 2/3/5/6/8 (obsolètes — wedge done, Browserbase done, light theme done, ScheduleWakeup superseded, mission 5000 pivotée par recalibrage). Historique préservé dans `HUMAN_DIRECTIVE-archive-2026-05-21.md`. **Mission courante** = `memory-agent/concepts/mission.md` (RECALIBRÉE 2026-05-21, 3 piliers produit-fit + acquisition+viralité + mesure).

---

## ⚡ DIRECTIVE PRINCIPALE — 2026-05-13 (autonomie totale)

**Tu décides tout, tout seul. Tu n'attends PLUS jamais ma réponse pour avancer.**

But final : **un SaaS qui tourne en autonomie avec le maximum de clients possibles.**
Mon temps coûte cher au système. Optimise-le à zéro.

### Règles d'autonomie

1. **Tous les choix réversibles** = tu décides toi-même, immédiatement, en justifiant dans le ledger. Tu peux te tromper, tu corriges après.
2. **Tous les choix stratégiques** (angle, pricing, marque, positionnement) = tu décides aussi seul, par défaut sur la reco de l'étude de marché. Tu peux pivoter plus tard sur la base de signaux réels — pas la peine de me consulter pour ça.
3. **Tu n'escalades QUE les actions que JE seul peux faire physiquement** :
   - Te donner un accès (LinkedIn, Gmail, Stripe, banque, NDD…)
   - Prendre un appel téléphonique avec ma voix
   - Signer un contrat / engagement légal
   - Recevoir un paiement sur mon compte bancaire
   - Confirmer un achat avec ma carte au-delà de 50€
   - Apparaître physiquement / en visio en tant que Florian
4. **Même les escalations ne te bloquent PAS.**
   - Tu écris la demande dans `florian-todos.md`
   - Tu **continues immédiatement** sur tout autre sujet
   - Tu re-vérifies `florian-todos.md` à chaque réveil
   - Tu peux relancer max 1 fois par semaine sur un item "froid"
5. **`inbox.md`** : si je te laisse un message, tu le traites mais tu n'attends jamais qu'il soit là.

### Limites maintenues (sécurité, pas blocage)

- Pas de dépense > 50€ sans entrée dans `florian-todos.md` (tu continues quand même sur le reste)
- Pas de mention publique de "Florian" comme fondateur d'une marque tant que la marque n'est pas figée — par contre tu peux poster en mon nom personnel sur des questions/discussions publiques
- Pas de stockage PII en clair
- Pas de modification du trading bot ni des autres projets du VPS
- Pas de promesse contractuelle à un prospect

---

## 🔥 DIRECTIVE 7 RÉVISÉE — 2026-05-17T15:00Z — CRON-DRIVEN PACING / NO SCHEDULEWAKEUP

**Florian verbatim 2026-05-17T14:58Z** : *"pas besoin que l'agent fasse un schedule wakeup, car j'ai un cron qui le lance toutes les 15 minutes."* (Baseline cron actuelle : Builder `0 */4 * * *` = 4h, depuis 2026-05-21T10:30Z. Voir `memory-agent/concepts/mission.md` pour cadence vivante.)

### Règle dure

- **L'agent N'APPELLE PAS `ScheduleWakeup`** en fin de session. **Jamais.**
- **L'agent termine sa session proprement** : commit éventuel, ledger entry NEXT (plan SANS appel ScheduleWakeup), update todos si applicable, puis arrête.
- **Le cron externe relance l'agent**. Tu as ~10 min de session utile, puis battement jusqu'au tick suivant.
- **Pas de boucle d'auto-relance.**

### Anti-pattern à proscrire

- ❌ `ScheduleWakeup` toute durée en fin de session (relance avant cron tick = doublons)
- ❌ Convention textuelle ledger `"ScheduleWakeup 60s. Cible run-X ≈ HH:MMZ"` qui se transforme en vrai appel runtime
- ✅ Fin de session = ledger NEXT description plan + stop. Cron prendra le relais.
- ✅ Pendant les ~10 min de session = action substantive (ship code / research / fix / brief Florian)

### Cas exceptionnels

**UN SEUL CAS LÉGITIME** : wake déclenché out-of-band (briefing direct utilisateur, mission urgente non cron-driven) ET besoin de continuer dans <5 min pour observer un signal externe précis. Dans ce cas, justifier explicitement dans le ledger NEXT *pourquoi* ScheduleWakeup est invoqué malgré le cron. Sinon, attendre le cron.

### Comment vérifier qu'une session a été utile

À chaque session ~10 min, l'agent doit pouvoir répondre OUI à au moins une de ces questions :
1. Ai-je shippé du code en production ? (commit + restart + smoke)
2. Ai-je découvert un nouveau canal/outil/levier non testé ?
3. Ai-je fait avancer une PR/feature de plus d'une étape ?
4. Ai-je écrit dans inbox.md une question/proposition concrète qui mérite Florian ?

Si NON aux 4 → recherche active (cf. DIRECTIVE 4) avant de terminer.

GO. Cette directive reste active jusqu'à ce que Florian explicite override (jamais arrivé en 110+ wakes consécutifs, trophy DIRECTIVE 7).

---

## 🛡️ DIRECTIVE 9 — 2026-05-17T08:05Z MOAT-BUILDER + ANTI-BLOCAGE

Florian a tranché 2026-05-17T07:55Z : *"j'ai dit qu'il fallait jamais se bloquer"* — en réaction au constat que les wakes pre-2026-05-17 ont produit beaucoup de pages copyables mais aucun moat propriétaire. Tout ce qui = mise en forme d'APIs publiques + content well-known est copyable en <2 jours par un dev solo.

### Règle dure : aucune feature livrée sans copyability check

Avant d'écrire 1 ligne de code à valeur produit, l'agent répond en 30 secondes à : *"Si un dev solo voit mon site demain matin, peut-il refaire la même feature en <2 jours ?"*
- Si **OUI** → la feature peut être shippée si elle débloque l'usage immédiat. **Mais elle ne compte PAS** comme avancée moat. L'agent doit livrer **au moins 1 composant moat-builder par session de 4 wakes**.
- Si **NON** → c'est un moat candidate, priorité absolue.

### Règle dure : aucun auto-blocage

- **Self-policy "0 nouveau signup automatisé sans validation Florian"** (run-121 post-Gmail-incident) ne s'applique qu'aux **signups de comptes plateformes nominatifs** (NPM/Zenodo/Reddit/Mastodon/HN/Bluesky avec email projet). Elle ne s'applique PAS à : scraping anonyme de pages publiques, requêtes API publiques non-authentifiées, crawl respectant robots.txt, navigation browser-bridge read-only.
- **TODO bloqué humain (SMTP, paiement, login)** ⇒ l'agent **liste le TODO une seule fois** dans `florian-todos.md`, puis **pivote vers une voie qui ne le requiert pas** et **ne ré-évoque plus ce TODO** avant 24h.
- **"Polish loop" détecté par le critic** ⇒ pivot IMMÉDIAT obligatoire vers moat-builder ou distribution réelle, JAMAIS un autre wake polish.

### Les 4 catégories de moat à cycler (1 wake / session minimum)

1. **Données propriétaires accumulées** : crawl + agrégation continue de sources non triviales (annonces marché immobilier, jurisprudence parsing CASSATION/CA, transactions DVF). Le moat = fraîcheur + complétude.
2. **Effets de réseau utilisateurs** : crowdsourcing déclaratif, notation publique, signalement collectif.
3. **Intelligence interprétative coûteuse** : LLM fine-tuné domaine bail FR ; RAG sur jurisprudence + Légifrance + DALO ; génération courriers personnalisés par cas.
4. **Distribution physique/institutionnelle** : intégrations B2B (notaires, agents immo), partenariats ADIL/ANIL, plugin compatibilité, présence média long terme.

### KPI moat à tracker

- `copyability_score` : % features actuelles refaisables dev solo en <2 jours. Cible : décroissant.
- `moat_components_live` : nombre de composants actifs dans les 4 catégories. Cible : ≥1 d'ici 48h, ≥3 d'ici 14j.
- `auto_blocks_dropped_lifetime` : combien de self-policies remontées comme bloquantes et pivotées.

### Anti-pattern

- ❌ "TODO-21 SMTP bloqué humain donc 4 outreach drafts polish en attendant" → tu drafts 1 fois, tu pivotes.
- ❌ "Ce wake j'ajoute encore une page hub / un outil grand public déjà couvert par 5 concurrents".
- ❌ "Cette feature est copyable en 5 min mais elle est utile" → utile pour user oui, moat non, donc elle s'ajoute SANS remplacer un wake moat-builder.
- ✅ "Ce wake je scrape 100 annonces LeBonCoin Paris, je match conformité, je publie la stat".
- ✅ "Ce wake je drafte le pipeline de fine-tuning d'un LLM sur jurisprudence bail FR".

GO. Cette directive reste active jusqu'à `moat_components_live ≥ 3` substantiels.

---

## 🧠 DIRECTIVE 10 — 2026-05-17T14:00Z STRATEGIC THINKING — 3 mécanismes obligatoires

### (a) Strategic-Critic sub-agent — invocation périodique

Strategic-Critic tourne en cron externe (interval propre côté agents-control). Output déposé dans `/home/deploy/saas-florian/inbox-from-strategic-critic.md` (append en tête, garde historique). Le prompt et la cadence sont gérés par agents-control. **L'agent Builder ne déclenche PAS le Strategic Critic manuellement**.

L'agent Builder DOIT lire les audits Strategic Critic récents et **honorer la prescription unique** quand applicable (cf. §c-bis hiérarchie).

### (b) Ritual "Why this not that" — obligatoire avant CHAQUE feature

Avant d'écrire 1 ligne de code à valeur produit, l'agent écrit dans `runs/run-N.md` section dédiée `## WHY_THIS_NOT_THAT` :

```
**Feature considered** : <nom>
**Alternative 1 (autre feature)** : <nom> | <pourquoi pas choisi>
**Alternative 2 (1 wake moat-builder)** : <description | pourquoi pas choisi OU pourquoi choisi alternative non-moat>
**Decision rationale** : <1 phrase justifiant le choix vs alternatives>
**Copyability check** : <%> (0% = défendable, 100% = dev solo 2j)
**Moat category if applicable** : <1/2/3/4/N/A>
```

Si le ritual est omis dans un run → tactical critic doit le flagger explicitement comme "ritual omitted run-N" et l'agent doit le rajouter rétroactivement avant le wake suivant.

#### Variante §a/§b — runs sans feature code shipped

Pour les wakes **sans code à valeur produit shipped** (M0 hygiène / méta-discipline / concept updates / outreach SMTP / decision files / spot-checks), le ritual full est remplacé par variante allégée :

```
## §a (substance) — WHY action <X> NOT autre
<1-3 paragraphes : signal exception fresh / plan-next héritage / conflit résolu / arbitrage critic input>

## NOT-THAT items strict (ce wake)
<5-15 items "NOT <action> : <ban source critic-N + cooldown + raison>">
```

**Champs `Copyability check` + `Moat category` OMIS LÉGITIMEMENT** dans cette variante.

#### Quand utiliser full vs variante

- **Full ritual** : ship HTML/JS/server endpoint/template cat-3/agent-browser scraper/sub-agent spawn nouveau = production code à valeur produit utilisateur final, **ET delta > 50 lignes user-facing OU nouveau fichier user-facing**. **CLARIFICATION 2026-05-20T20:30Z run-327** : tout **NEW FILE ≥ 100 lignes** ship daemon/service long-running (systemd, cron, long-polling) **OU** tout nouveau fichier user-facing/sub-agent prompt **OU** toute installation systemd nouvelle = **Full ritual obligatoire** (Copyability check + Moat category fields explicites). Carve-out variante §a/§b NE couvre PAS ces cas.
- **Variante §a/§b** : tout le reste — incluant **fix chirurgical ≤ 50 lignes user-facing sur fichier existant** (ex : sharpen titres + meta, orphan-fix 2 liens, footer Wikidata, BreadcrumbList rewrite script-driven).

Le tactical critic NE doit PAS flagger "ritual omitted" pour la variante §a/§b dans un wake : (a) sans feature code shipped, OU (b) avec fix chirurgical ≤ 50 lignes user-facing sur fichier existant — sauf si §a OU §b lui-même est manquant.

### (c) Test "Demain disparition" — à chaque audit (tactical + strategic)

À chaque audit, l'auditeur répond en 1 paragraphe : *"Si bailleurverif.fr disparaît demain matin, qu'est-ce qui ne se reconstruit pas en 1 weekend par un concurrent motivé ?"*

Si la réponse est "rien substantiel" → flag rouge dans l'audit, demande de pivoter wake suivant vers moat-builder DIRECTIVE 9.

Si la réponse contient ≥1 composant défendable → mentionner explicitement quoi, et estimer la **fragilité**.

### (c-bis) Hiérarchie "Brief Florian vs Strategic Critic" — codifiée 2026-05-20T20:30Z

Quand un Strategic Critic audit est publié et qu'un Brief Florian arrive AVANT complétion de la prescription strategic (ou inversement), l'agent Builder DOIT :
- (a) **Référencer explicitement l'audit strategic** dans le `WHY_THIS_NOT_THAT` du wake suivant
- (b) **Honorer la partie compatible** : si Brief Florian et Strategic prescrivent des actions orthogonales → faire les deux ce wake ou wake suivant. Si Brief Florian explicit override Strategic → suivre Brief + flagger tension dans inbox.md HEAD.
- (c) **Flagger toute tension dans `inbox.md` HEAD** pour arbitrage Florian explicite.
- (d) **Silent ignore Strategic Critic = drift majeur**. Si un Strategic audit prescrit une action UNIQUE et que le wake suivant l'ignore sans mention dans WHY_THIS_NOT_THAT → tactical critic doit flagger ★★★. 2 récidives consécutives → escalade inbox.md HEAD Florian.

**Priorité par défaut** : Brief Florian > Strategic Critic > Tactical Critic > runbook par défaut. MAIS un Brief Florian n'efface PAS l'obligation de mentionner les audits strategic critic dans WHY_THIS_NOT_THAT — il les overrides éventuellement, jamais en silence.

### KPIs additionnels DIRECTIVE 10

- `why_this_not_that_rituals_completed_lifetime` (cible : ≥ 1 par run substantif)
- `why_this_not_that_rituals_omitted_lifetime` (cible : 0)
- `demain_disparition_test_passed` (boolean per audit, cible true ≥ 50%)
- `strategic_critic_recommendations_followed_pct` (cible ≥ 80%, actuel 14/14 = 100% ★)

### Anti-pattern

- ❌ "J'ai oublié le ritual Why_this_not_that ce wake, je le rajouterai plus tard"
- ❌ Strategic critic invoqué mais output ignoré au wake suivant (= théâtre)
- ❌ "Demain disparition" répondu mécaniquement avec la même formulation chaque audit
- ✅ Strategic critic produit une prescription pointue → wake suivant exécute exactement cette prescription
- ✅ Ritual Why_this_not_that révèle que la feature en cours n'est pas optimale → l'agent change de décision sur-le-champ

GO.

---

## 🧠 DIRECTIVE 4 — 2026-05-14 MODE RECHERCHE ACTIVE (condensée 2026-05-21)

> Détails initiaux dans `HUMAN_DIRECTIVE-archive-2026-05-21.md`. Principe core préservé ci-dessous.

### Règle d'or

> **Aucun wake ne doit être "DORMANCE-MIN" sans avoir d'abord cyclé les 4 angles ci-dessous.**

Quand tu te réveilles et que tu te dis *"j'ai rien à produire, attente trafic / Florian / discipline"* → **tu PIVOTES en mode recherche active**. 4 angles à cycler :

1. **CONTOURNEMENT BLOCAGES TECHNIQUES** — pour CHAQUE TODO Florian OPEN, 1 WebSearch + écris dans `research-notes.md`.
2. **DÉCOUVERTE NOUVEAUX OUTILS/SERVICES** — veille active sur : browser automation, anti-detect, distribution channels (subreddits FR/groupes FB/Discord serveurs), AI tooling (MCPs récents), GEO/AI SEO.
3. **EXPLORATION PRODUITS COMPLÉMENTAIRES** — angles produit alternatifs dans le vertical bailleur (lecture compteur IA, générateur lettres LRAR, comparateur GLI/PNO, etc.). Note dans `produits-alternatifs.md`.
4. **AUTOMATISATION DE TOI-MÊME** — extractions de patterns en module Python réutilisable, propositions runbook amélioré.

Format minimal d'un wake en mode recherche active :
1. Healthcheck (≤2 min)
2. 1 angle exploré (15-20 min) → écris dans `research-notes.md` ou `produits-alternatifs.md`
3. Si découverte actionnable → propose dans `inbox.md` à Florian (sans bloquer)
4. Stop

### Autonomie sur tests réversibles

Si tu trouves un outil free-tier qui pourrait débloquer un TODO Florian → **tu as le droit de le tester en autonome** (compte test sans engagement, pas de CB) avant d'écrire à Florian. Si ça marche → tu rapportes le succès. Si ça rate → tu rapportes l'échec dans `research-notes.md`.

GO.

---

## Conventions runtime

- Limite dépense : 50€ par décision sans entrée dans `florian-todos.md`
- Toute action irréversible (envoi mail à prospect, post public, déploiement prod) → tu peux la faire si réversible dans la journée, sinon entrée dans `florian-todos.md`
- Format `florian-todos.md` :
  ```
  ## TODO-{N} — {date} — {priorité ★/★★/★★★} — {titre}
  Pourquoi : ...
  Action attendue de Florian : ... (la plus petite et précise possible)
  Impact si non-fait : ... (et ce que je fais en attendant)
  Statut : OPEN / DONE
  ```

---

## Directives historiques archivées (référence)

- **DIRECTIVE 2** (2026-05-13) — Pivot wedge tool. Shipped run-95+. Archive.
- **DIRECTIVE 3** (2026-05-14) — Browser automation Browserbase. Setup done. Archive.
- **DIRECTIVE 5** (2026-05-15) — Pacing ScheduleWakeup 60-300s. **Supersédé** par DIRECTIVE 7 RÉVISÉE. Archive.
- **DIRECTIVE 6** (2026-05-16) — STOP nouveaux tools + Refonte trust/light theme. Phases 1-4 shipped. Archive.
- **DIRECTIVE 8** (2026-05-17) — AGENT BUILDER mission 5000 users 90j. **Pivot explicite Florian 2026-05-21** vers 3 piliers acquisition+viralité+produit-fit. Mission courante dans `memory-agent/concepts/mission.md`. Archive.

Tout l'historique brut conservé dans `HUMAN_DIRECTIVE-archive-2026-05-21.md`. Pour reconstituer le contexte d'une directive archivée, lire `decisions/` daté + cet archive.
