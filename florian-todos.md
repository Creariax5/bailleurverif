# Florian TODOs — choses que SEUL toi peux faire

> L'agent ajoute ici uniquement les actions qui requièrent ta personne (login, signature, vote, paiement, click humain). L'agent N'ATTEND PAS ces items pour avancer.
> Compacté run-120 (2026-05-16T15:50Z) — historique complet dans `florian-todos-history.md.bak`.

---

## 🔐 ACTION ★★★ — RÉVOQUE LE TOKEN GH MAINTENANT

Tu m'as donné un PAT classic full-scope (admin org / delete_repo / workflow / repo / etc.) pour push le repo. Repo désormais public et live, mission accomplie. **Va sur https://github.com/settings/tokens → Delete** le token `ghp_6kUw...`. 30s. Je ne le réutiliserai plus.

## ✅ FAIT — `gh auth login` + publication repo (run-121, 2026-05-16T16:36Z)

Repo public live : https://github.com/Creariax5/bailleurverif (281 fichiers, README + LICENSE + .gitignore agressif + code wedge-tool + content + dashboard + state logs ledger/runs/inbox). Publication via token Florian (env var, jamais sur disque). Audit PII fait pre-push (1 phone Florian redacted dans ledger ligne 566).

## ⭐ SI TU AS 5 MINUTES EN BONUS

**Show HN copy-paste** (run-116 ★★) — tout est prêt dans `agent-narrative.md`. Statistiquement le levier le plus court pour casser le 0-user en 119 wakes.

1. Aller sur https://news.ycombinator.com/submit
2. Titre : `Show HN: A French rental compliance SaaS, autonomously built and run by a Claude agent`
3. URL : `https://bailleurverif.fr`
4. Body : copier section "Body" de `agent-narrative.md`
5. Timing optimal : mardi-jeudi 13-15h UTC (peak USA tech)

## ⭐ SI TU AS 10 MINUTES EN BONUS

**Press kit FR** (run-112 ★★) — 5 templates email prêt-à-coller dans `outreach-journalistes-immo.md` (Le Monde / Le Figaro / Capital / BFM / Les Échos). 2-3 min par email via ta boîte perso.

---

## 🚨 INCIDENT 2026-05-16 — bailleurverif.contact@gmail.com DISABLED par Google

Compte désactivé le 2026-05-15 (motif "bot-like / multi-account violation", cause probable activité agent automatisée). Détails complets dans inbox.md (2026-05-16T16:10Z) + ledger run-121. TODO-17 / TODO-18 / TODO-20 ci-dessous reformulés en conséquence.

---

## TODO-17 ✅ DONE — Google Search Console verification (2026-05-16T16:24Z)

Verified via `florian.demartini.dev@gmail.com` (pivot post-disabled bailleurverif.contact), URL prefix `https://bailleurverif.fr`, méthode Fichier HTML `googleadcc8fd7871ecbd5.html` déposé `wedge-tool/static/`. Sitemap `/sitemap.xml` soumis : "Opération effectuée", **103 URLs découvertes** dès la 2ᵉ soumission (1ʳᵉ "Impossible de récupérer" probablement cache pré-verify). NE PAS supprimer `googleadcc8fd7871ecbd5.html` du VPS (perte de verif).

Effet attendu : crawl progressif 24-72h, indexation 7-30j, débloque 92% trafic FR théorique manquant depuis 119 wakes. Critic agent prendra le relais pour mesurer indexation J+1 / J+3 / J+7 / J+30.

---

## TODO-20 ❌ DEAD — Gmail App Password pour SMTP automatique

Dépendait de `bailleurverif.contact@gmail.com` (disabled 2026-05-15). Remplacé par **TODO-21** ci-dessous.

---

## TODO-21 ★★★ — Provisionner email opérationnel `contact@bailleurverif.fr` (5 min, 1,91€/mo) — URGENCE BUMP

**Bump urgence run-132 (2026-05-16T19:50Z)** : **23 références à `contact@bailleurverif.fr`** désormais sur prod (10 fichiers : index.html footer + h-card, cgu.html, mentions-legales.html, politique-confidentialite.html, data/*.html /.json /.xml /.cff, .well-known/security.txt). Avant run-132 elles pointaient toutes vers le Gmail mort `bailleurverif.contact@gmail.com` (bug latent #10 trouvé et fixé). Effet : (1) bouncer NXDOMAIN actuel = mieux que dead Gmail mais (2) Option B catch-all OVH 0€/2min suffit à les rendre live globalement.

**Pourquoi** : remplacer le mail mort `bailleurverif.contact@gmail.com` pour outbound presse FR (5 templates prêts `outreach-journalistes-immo.md`) + email contact public site + **23 pages prod déjà câblées** + base future SMTP transactionnel. Cartographie comparative 5 providers dans `research-notes.md` run-123. **OVH Email Pro recommandé ★★★** (FR datacenters / RGPD-native / pas de limite SMTP / domaine déjà chez OVH).

**Option A (★★★, 1,91€/mo TTC, 5 min)** — OVH Email Pro
1. https://www.ovh.com/manager/ (déjà loggé probable, même compte que domaine `bailleurverif.fr`)
2. Web > Emails > "Email Pro" > Commander 1 compte
3. Adresse `contact` / domaine `bailleurverif.fr`
4. Paiement via CB déjà enregistrée
5. DNS auto-configuré sous 30 min, MX/SPF/DKIM gérés par OVH
6. Écrire dans `inbox.md` "TODO-21 done option A" (NE PAS coller le mot de passe initial dans inbox.md, juste confirmation)

**Option B (★, 0€, 2 min)** — Catch-all forward gratuit (intermédiaire)
1. Manager OVH > Emails > Redirection email
2. Source `contact@bailleurverif.fr` → destination `florian.demartini.dev@gmail.com`
3. Reçois dans ton Gmail perso, branding limité mais débloque la réception.

Discipline post-incident : agent NE crée PAS de compte SMTP/email en autonome. Toi via UI OVH.

---

---

## TODO-23 ★★ — 1 post LinuxFr OU Village-Justice (5-10 min, bypass SMTP/PAT)

**Pourquoi** : run-141 sub-agent a identifié **8 canaux distribution FR actionnables sans email transactionnel ni GitHub PAT** (cf `outreach-alternate-channels.md`). 1ʳᵉ humain externe en 139 wakes est venu via GitHub repo (19:33Z, ip_hash 8950554031). Multiplier signaux entrants devs/juristes = priorité distribution honnête.

**Top 2 actions asymétriques** :

1. **LinuxFr commentaire** sur thread DPE 133-comm (https://linuxfr.org/users/niconico/journaux/le-dpe-immobilier-est-mal-concu) — 5 min, brouillon copy-paste prêt dans `outreach-alternate-channels.md` § Cible 1A. Audience dev/sysadmin FR overlap notre 1er humain repo.
2. **Que Choisir forum** (https://forum.quechoisir.org/investissement-locatif-t355250.html) — 5 min, brouillon générique forums § Priorité 3.

Brouillons FR neutres (ton sobre, MIT/OSS), liens vers démo + GitHub. 0 agenda commercial.

**Statut** : OPEN run-141. Asymétrie : ces canaux bypassent TODO-21 (SMTP) ET TODO-22 (PAT) — déblocables ce week-end sans dépendance.

---

## TODO-22 ★★ — Nouveau GitHub PAT scope `repo` (≤2 min) — débloque distribution widget Open3CL

**Pourquoi** : run-138 a livré le widget DPE `<script>` embeddable + identifié **Open3CL/engine** (16 ★ MIT actif) comme cible asymétrique #1 : leur demo affiche le score DPE brut mais PAS le statut légal Loi Climat. Une issue + PR polite (texte prêt copy-paste dans `outreach-widget-targets.md` section "Brouillon issue") = 1ʳᵉ tentative distribution viralité widget concrète. Sans PAT je ne peux ni filer issue ni push PR.

**Action (2 min)** :
1. https://github.com/settings/tokens/new (fine-grained ou classic)
2. Scope minimum **`repo` uniquement** (lecture/écriture issues + PRs sur repos publics)
3. Expiration 7 jours (pas plus, sécurité)
4. Coller le token dans `inbox.md` (ligne dédiée `TODO-22 token: ghp_...`) puis je révoque dès usage fait

**Alternative** : Toi-même copy-paste l'issue depuis `outreach-widget-targets.md` sur https://github.com/Open3CL/engine/issues/new — 1 min, texte 100% prêt. Aucun PAT requis.

**Statut** : OPEN run-138. Asymétrie : 16★ projet open-source DPE = audience dev FR exact-cible widget.

---

## TODO-24 ★★★ — data.gouv.fr réutilisation (payload prêt run-193, choix 2 chemins) — UPGRADED

**Pourquoi** : `data.gouv.fr/reuses/` = dofollow gov.fr DR 90, 0€. BailleurVérif réutilise légitimement 4 datasets officiels (DPE ADEME, BAN, Encadrement Paris, JORF) → cite l'URL pivot de l'observatoire (N=160, 7 villes, 59 % violations) = backlink + visibilité data analysts / journalistes FR.

**Probes API run-193 (vérifiées 11:55Z)** :
- `POST /api/1/reuses/` sans auth = **HTTP 401** (X-API-KEY obligatoire — confirmé 1ʳᵉ fois empiriquement).
- `POST /api/1/discussions/` sans auth = **HTTP 401** aussi.
- → 0 chemin anonyme. Action humaine inéluctable.

**Le payload est désormais 100 % pré-écrit** (run-193) :
- `data-gouv-fr-reuse-payload.json` (3,7 KB description markdown + 4 dataset UUIDs vérifiés HTTP 200 + tags + topic `housing_and_development` + type `application` + URL pivot `https://bailleurverif.fr/observatoire-annonces-loyer.html`).
- `submit-data-gouv-fr-reuse.sh` (POST cURL, lit `DGVFR_API_KEY` env var, jamais persisté disque).

### Chemin A (5 min, agent auto-soumet) ★★★ recommandé

1. Login https://www.data.gouv.fr/fr/login/ (email `florian.demartini.dev@gmail.com`)
2. Profile → Settings → "Clé API" → Générer
3. Coller dans `inbox.md` une ligne unique : `TODO-24 api-key: <clé>`
4. Au wake suivant je lis la clé, `export DGVFR_API_KEY=…`, `bash submit-data-gouv-fr-reuse.sh`, archive `reuse_id` + URL canonique dans ledger.md, et te demande de révoquer la clé.

### Chemin B (5 min, toi 100 % UI) — alternative

1. https://www.data.gouv.fr/fr/reuses/new/
2. Ouvrir `data-gouv-fr-reuse-payload.json`, copier-coller champ par champ :
   - **Titre** : valeur de `title`
   - **URL** : valeur de `url`
   - **Type** : `application`
   - **Thème** : `Logement & développement` (housing_and_development)
   - **Description (markdown)** : valeur de `description` (3,7 KB)
   - **Tags** : valeurs de `tags` (8 tags)
   - **Datasets** : ajouter 4 UUIDs (DPE 66c2ff…, BAN 5530fb…, Encadrement Paris 62a724…, JORF 53ca35…) via le picker UI
3. Publier → confirmer dans `inbox.md` "TODO-24 done chemin B" + URL du reuse.

**Statut** : OPEN run-156, payload READY run-193. Asymétrie : 1ʳᵉ canal gov.fr + bypass SMTP TODO-21 + bypass PAT TODO-22.

---

## TODO-19 ★★ — Findly.tools submission (DR 72 dofollow)

**Pourquoi** : 1er backlink dofollow DR>50 autonome côté distribution. Pourrait aider amorce indexation Google sans GSC.

**Action (5 min)** : data prête dans `kit-submission.md`. Form sur https://findly.tools/submit. Email à utiliser : **PAS** `bailleurverif.contact@gmail.com` (disabled). Recommande `florian.demartini.dev@gmail.com` ou autre perso. Catégorie "Real Estate Tools".

**Statut** : OPEN depuis run-104. Déprio si TODO-17 GSC fait. **Discipline post-incident (run-121)** : agent ne tentera plus de signup autonome sur Findly sans ta validation explicite — patron bot-detection trop coûteux. Toi-même peux soumettre quand tu veux.

---

## TODO-18 ❌ DEAD — Gmail MCP scope insufficient

Compte source `bailleurverif.contact@gmail.com` disabled (2026-05-15). Élargir scope d'un compte disabled n'apporte rien. À redéfinir post-pivot email infrastructure.

---

## ABANDONNÉS (l'agent ne te demande PLUS)

- **TODO-16 Mastodon** : compte @bailleurverif@piaille.fr suspendu run-93, canal abandonné
- **TODO-14 Bluesky / TODO-13 Reddit / TODO-3-bis Twitter** : captcha/SMS verif, ROI < HN
- **TODO-11 Boursorama drafts** : faible ROI vs presse / HN
- **TODO-15 Discord FR-immo** : reporté post-traction
- **TODO-3 LinkedIn / TODO-4 email pro / TODO-5 Calendly** : Phase 2+ (post-traction)

Historique complet : `florian-todos-history.md.bak`.
