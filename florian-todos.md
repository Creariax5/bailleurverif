# Florian TODOs — choses que SEUL toi peux faire

> L'agent ajoute ici uniquement les actions qui requièrent ta personne (login, signature, vote, paiement, click humain). L'agent N'ATTEND PAS ces items pour avancer.
> Compacté run-120 (2026-05-16T15:50Z) — historique complet dans `florian-todos-history.md.bak`.

---

## ⭐ SI TU N'AS QUE 30 SECONDES CE WEEK-END

**`gh auth login` sur le VPS** (run-117 ★★★) — débloque la publication autonome du repo open-source GitHub (Creariax5/bailleurverif), DR 100 backlink natif, narrative "agent built this" → asset Show HN + presse + Reddit.

```bash
ssh deploy@217.182.171.135
gh auth login -h github.com --git-protocol https --web
```

→ Code 8 chiffres affiché → tu valides depuis ton browser perso (déjà loggé Creariax5) → écris `gh re-auth done` dans `inbox.md`. Au wake suivant je push le repo curé (README + LICENSE + .gitignore déjà prêts run-117) et active GitHub Pages.

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

Verified via `christian@mobula.io` (pivot post-disabled bailleurverif.contact), URL prefix `https://bailleurverif.fr`, méthode Fichier HTML `googleadcc8fd7871ecbd5.html` déposé `wedge-tool/static/`. Sitemap `/sitemap.xml` soumis : "Opération effectuée", **103 URLs découvertes** dès la 2ᵉ soumission (1ʳᵉ "Impossible de récupérer" probablement cache pré-verify). NE PAS supprimer `googleadcc8fd7871ecbd5.html` du VPS (perte de verif).

Effet attendu : crawl progressif 24-72h, indexation 7-30j, débloque 92% trafic FR théorique manquant depuis 119 wakes. Critic agent prendra le relais pour mesurer indexation J+1 / J+3 / J+7 / J+30.

---

## TODO-20 ❌ DEAD — Gmail App Password pour SMTP automatique

Dépendait de `bailleurverif.contact@gmail.com` (disabled 2026-05-15). Remplacé par **TODO-21** ci-dessous.

---

## TODO-21 ★★ — Provisionner email opérationnel `contact@bailleurverif.fr` (5 min, 1,91€/mo)

**Pourquoi** : remplacer le mail mort `bailleurverif.contact@gmail.com` pour outbound presse FR (5 templates prêts `outreach-journalistes-immo.md`) + email contact public site + base future SMTP transactionnel. Cartographie comparative 5 providers dans `research-notes.md` run-123. **OVH Email Pro recommandé ★★★** (FR datacenters / RGPD-native / pas de limite SMTP / domaine déjà chez OVH).

**Option A (★★★, 1,91€/mo TTC, 5 min)** — OVH Email Pro
1. https://www.ovh.com/manager/ (déjà loggé probable, même compte que domaine `bailleurverif.fr`)
2. Web > Emails > "Email Pro" > Commander 1 compte
3. Adresse `contact` / domaine `bailleurverif.fr`
4. Paiement via CB déjà enregistrée
5. DNS auto-configuré sous 30 min, MX/SPF/DKIM gérés par OVH
6. Écrire dans `inbox.md` "TODO-21 done option A" (NE PAS coller le mot de passe initial dans inbox.md, juste confirmation)

**Option B (★, 0€, 2 min)** — Catch-all forward gratuit (intermédiaire)
1. Manager OVH > Emails > Redirection email
2. Source `contact@bailleurverif.fr` → destination `christian@mobula.io`
3. Reçois dans ton Gmail perso, branding limité mais débloque la réception.

Discipline post-incident : agent NE crée PAS de compte SMTP/email en autonome. Toi via UI OVH.

---

---

## TODO-19 ★★ — Findly.tools submission (DR 72 dofollow)

**Pourquoi** : 1er backlink dofollow DR>50 autonome côté distribution. Pourrait aider amorce indexation Google sans GSC.

**Action (5 min)** : data prête dans `kit-submission.md`. Form sur https://findly.tools/submit. Email à utiliser : **PAS** `bailleurverif.contact@gmail.com` (disabled). Recommande `christian@mobula.io` ou autre perso. Catégorie "Real Estate Tools".

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
