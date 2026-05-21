# Florian TODOs — choses que SEUL toi peux faire

> L'agent ajoute ici uniquement les actions qui requièrent ta personne (login, signature, vote, paiement, click humain). L'agent N'ATTEND PAS ces items pour avancer.
> **Last refactor : 2026-05-19T16:XXZ (run-304)** — historique condensé en section "Archive collapsed". Détails archivés dans `florian-todos-history.md.bak` + `ledger.md` + git history.
> **Update 2026-05-19T20:28Z (run-307)** — RÉORIENTATION mission Florian 17:XXZ : revenu passif vs 5000 users. TODO-25 (Stripe) archivé REPORTÉ post-100 signups. Nouveau TODO-32 ★★ Affiliés Lovys+Hemea remplace TODO-25 priorité gros chantier. Ancien TODO-32 (drafter LinkedIn) → TODO-32-bis ★ Optionnel. Nouveau TODO-33 ★ Parler 5 personnes entourage.
> **Update 2026-05-19T23:30Z (run-310)** — NEW TODO-34 ★★ DÉCISION Pilier 4 viral notation agences : CSV observatoire 23 colonnes sans `agence`/`brand`/`annonceur` ⇒ pages `/notation-agence/<brand>/<ville>.html` data-driven impossibles sans upgrade scraper. 3 options (a) upgrade scraper / (b) pivot angle / (c) pause indéfini. Default = (c) si silence 14j.
> **Update 2026-05-20T07:30Z (run-318)** — NEW TODO-35 ★ (faible priorité) Indexing API Google : setup service account Google Cloud + clé JSON pour automatiser "Demander indexation" via API (15-20 min). Avant TODO-35 → discipline internal linking (codifiée `concepts/seo-discipline.md`) + GSC manual URL Inspection = suffisent. Faire quand tu veux, pas urgent.
> **🚨 Update 2026-05-21T07:35Z (run-331)** — **RECALIBRAGE MISSION Florian** : objectif court terme RECALIBRÉ = 100% produit-fit + acquisition + viralité (revenu = sortie, pas levier). North Star = `humans_engaged_lifetime` (cible >100 avant monétisation). **TODO-32 GEL TOTAL** (annulé jusqu'à humans_engaged≥100, NE PAS re-escalader). **TODO-34 Pilier 4 GEL pivot** (Pilier 4 cat-4 non recalibrée). **TODO-33 ★★ ESCALADÉ** (recherche utilisateur = aligné Pilier 1 produit-fit, débloquer pivot painkiller). **NEW TODO-36 ★★ Compte Reddit** (canal viral #1 proposé run-331).

---

## 🚨 Bloquant mission

*(aucun item bloquant — l'agent avance via cat-1 (observatoire) + cat-3 (templates RAG) + cat-4 (distribution gov.fr + awesome-lists + FAQPage). Si vrai bloquage apparaît, l'agent l'ajoute ici en ★★★)*

---

## ⚡ Quick wins < 5 min

### ~~TODO-31~~ ✅ DONE 2026-05-21T09:50Z — Test Rich Results FAQPage

Vérifié par Florian sur https://search.google.com/test/rich-results :
- `encadrement-loyer-france-2026.html` → 3 types valides (BreadcrumbList + Dataset + FAQPage 8 Q&A) ✅
- `observatoire-annonces-loyer.html` → 3 types valides (BreadcrumbList + Dataset + FAQPage 6 Q&A) ✅

Aucune erreur, aucun warning. Rich Results compatibles.

### TODO-26 ★ — ANTHROPIC_API_KEY .env (≤1 min)

Génère clé sur https://console.anthropic.com/settings/keys + coller dans `.env` ligne `ANTHROPIC_API_KEY=sk-ant-...`. Plafond budget v0 confirmé <$0.20 cumulé puis ≤50€/mois (auto-approuvé runbook).

**Pourquoi** : débloque génération templates RAG cat-3 (post v0 inline shippé run-243 + Judilibre enrich via Haiku run-297-303), embeddings jurisprudence, courriers personnalisés case-by-case. Pas urgent (cat-3 fonctionne déjà inline + sub-judilibre-enrich Haiku tourne).

**Statut** : OPEN — déprioritisé tant que sub-agents Haiku/Sonnet font le job. Ré-évocation cooldown 14j.

### TODO-19 ★ — Findly.tools submission (5 min, optionnel)

Form sur https://findly.tools/submit. Data prête dans `kit-submission.md`. Email = `florian.demartini.dev@gmail.com` (PAS `bailleurverif.contact@gmail.com` disabled). Catégorie "Real Estate Tools".

**Statut** : OPEN — DR 72 dofollow utile mais cat-4 backlinks déjà acquis (data.gouv.fr DR 90 + awesome-lists). Discrétionnaire.

---

## 🎯 Gros chantier > 1h

### TODO-34 ★★ — DÉCISION Pilier 4 viral notation agences (5 min Florian-action, NOUVEAU run-310)

**Pourquoi** : Run-310 a découvert que CSV observatoire (`wedge-tool/static/data/observatoire-annonces-loyer-*.csv` schema 23 colonnes) **n'a pas de colonne `agence`/`brand`/`annonceur`/`professional`**. Donc Pilier 4 "pages dédiées `/notation-agence/foncia/paris.html` data-driven" impossible sans upgrade scraper (extraction nom agence + classification pro vs particulier à chaque listing).

**Décision Florian** : choisir 1 des 3 options dans `inbox.md` HEAD (1 ligne) :

- **(a) UPGRADE SCRAPER** : Builder code 2-4 wakes (ajouter colonnes `agence_brand` + `is_professional` + re-scrape 7 villes + backfill historique partiel possible). Enable Pilier 4 viral data-driven authentique. Risque : 2-4 wakes Builder = ~€10-20 Opus, ROI inconnu tant que Pilier 1+2 pas validés.
- **(b) PIVOT ANGLE Pilier 4** : namedshaming non-agences via top arrondissements / codes postaux % violation (ex: `/top-violations-loyer-paris-arrondissement.html`). Data already in CSV. Builder ship 1 wake. Moins viral (pas de target identifiable nominatif) mais 0 risque juridique + 0 upgrade scraper.
- **(c) PAUSE Pilier 4** indéfini, focus Piliers 1+2+5 cumul = enough proof-of-pattern revenu passif. Builder default si pas réponse 14j.

**Action Florian** : 1 ligne `inbox.md` HEAD :
> `TODO-34 pilier-4: (a) | (b) | (c)`

**Statut** : ⏸️ GEL PIVOT 2026-05-21T07:35Z par recalibrage mission (Pilier 4 cat-4 viral nomming pas dans 3 piliers recalibrés). Florian peut répondre quand il veut MAIS Builder ne re-prompte plus, pas un blocker. Default désormais = pause indéfini auto-validé.

---

### TODO-32 ⏸️ GEL — Signer 2 affiliés Lovys (GLI) + Hemea (travaux) — annulé 2026-05-21 par recalibrage

**Statut** : ⏸️ **GEL TOTAL** 2026-05-21T07:35Z (verbatim Florian "je fais pas la TODO-32 par choix, ça sert à rien d'essayer de gagner de l'argent tant qu'on a pas des utilisateurs"). Restera GEL jusqu'à `humans_engaged_lifetime ≥ 100`. NE PAS re-escalader. Page comparateur `/assurance-habitation-locataire.html` reste online (déjà ship), MAIS Builder NE PAS itérer dessus.

### TODO-36 ★★ — Compte Reddit nominatif (canal viral #1 proposé run-331) — NOUVEAU

**Pourquoi** : recalibrage 2026-05-21 met acquisition+viralité 100% priorité. Reddit r/france r/Paris r/immobilier r/vosfinances = canal viral persona-fit le plus exploitable AUJOURD'HUI avec assets existants (observatoire N=232 = data posts share-friendly natifs). Ancien TODO-13 Reddit DEAD car OAuth Google cassé post-Gmail-disabled — pas remplaçable côté Builder (anti-bot Reddit fort).

**Action Florian (≤10 min)** : choisir 1 des 3 options dans `inbox.md` HEAD :

- **(a)** Créer compte Reddit nominatif sur `florian.demartini.dev@gmail.com` (ton nom propre, transparence "founder of bailleurverif.fr"). Coller `REDDIT_USERNAME=...` dans `inbox.md` HEAD. Builder draft posts pour ta validation (jamais auto-poster sans toi).
- **(b)** Prêter ton compte Reddit perso existant si tu en as un (idem workflow draft → tu valides → tu postes).
- **(c)** Refuser Reddit → Builder pivote canal #2 (Twitter/X anonymous avec compte projet, fallback). Note : Twitter signup demande SMS verification donc Florian-only aussi.

**Statut** : OPEN run-331 2026-05-21T07:35Z. Cooldown ré-évocation 7j si silent. Default si silence 14j : Builder propose plan B Twitter/X dans inbox.md HEAD (pas de canal viral self-serve possible sans Florian-input).

---

## 🤔 Optionnel / nice-to-have

### TODO-27 ★ — Open3CL issue #160 follow-up (fenêtre fermée)

Issue ouverte 2026-05-18, 0 réponse depuis. Probablement signal mort. Si tu veux bumper amicalement : commentaire sur https://github.com/Open3CL/engine/issues/160 :
> "Bump amical : si l'intérêt est là, je peux préparer la PR (helper `getLegalStatus(dpeLetter, communeCode='75001')` returning `{interdit_depuis: '2025-01-01', niveau: 'critique', source_url: 'legifrance...'}`). Sinon je laisse tomber, no worries."

Si signal vert → autorise agent à draft PR localement avec `GH_TOKEN`. **Statut** : OPEN faible priorité, cooldown 7j.

### TODO-32-bis ★ — Valider drafts LinkedIn `sub-linkedin-drafter` (~30s/jour quand actif)

(Anciennement TODO-32, renommé bis run-307 post-réorientation Florian — voir nouveau TODO-32 Affiliés section Gros chantier.)

Sub-agent `sub-linkedin-drafter` (Sonnet 4.6, interval 24h) spawné run-304. **Cycle 1 EARLY tick T+14min run-305 = draft 1184c jurisprudence Cass.** dans `social-drafts.md` ligne 626-665 section `## LINKEDIN-AUTO 2026-05-19T16:45:00Z`. Tu valides en 30s + postes à ton rythme (8000 followers). ROI mesurable : 1ʳᵉ post organique (TODO-23 partial done) = +10 visites/17h P10.

**Statut** : OPEN cycle 1 (1184c jurisprudence) pending validation. Cycle 2 ≥2026-05-20T16:45Z. Cooldown ré-évocation 7j si pas validé.

### TODO-33 ★★ — Parler 5 personnes entourage (1h one-shot, ESCALADÉ run-331 priorité Pilier 1 produit-fit)

Florian 17:XXZ réorientation — recherche utilisateur qualitative pour valider painkiller pivot homepage.

**Action** : 5 personnes entourage (locataire ou bailleur), ~12 min chacune, **1 seule question** :

> *"Si tu avais 10 secondes pour comprendre si tu te fais arnaquer sur ton loyer / dépôt de garantie / DPE, qu'est-ce que tu voudrais voir ?"*

Reporter findings dans `inbox.md` HEAD ligne : `TODO-33 user-feedback: [bullet points]` (1 ligne par personne max).

**Pourquoi** : valide quel painkiller (loyer abusif, dépôt non-rendu, DPE F/G interdit) résonne le plus avant pivot homepage. Builder utilise pour décider le UI/UX du pivot.

**Statut** : OPEN — 1× one-shot ~1h cumulé. Pas de cooldown (résultat débloque pivot homepage Pilier 1).

---

## 📦 Sous-agents actifs

> Builder Opus seul peut POST/PATCH/DELETE. Registry source-of-truth : `agent-browser/sub-agents-registry.json`. Logs : `data/sub-agents/<name>.jsonl`.

- **`sub-judilibre-enrich`** (Haiku 4.5) — interval 1h, enabled. Enrichit `jurisprudence_refs[]` cat-3 templates. État : 2/3 templates saturés (dpe-invalide N=3, depot-garantie N=3, loyer-abusif N=1 — Haiku qualité>quantité cycle 4).
- **`sub-seo-monitor`** (Haiku 4.5) — interval 24h, enabled. Audit SEO/GEO quotidien (PageSpeed Insights + crawler sitemap + LLM-bot diff). 1ʳᵉ tick ~2026-05-20T13:29Z.
- **`sub-linkedin-drafter`** (Sonnet 4.6) — interval 24h, spawn run-304. Drafte 1 post LinkedIn/jour pour validation Florian (cf TODO-32).

Budget cible total ≤ €20/mois Haiku/Sonnet combinés. Cap dur 6 sous-agents simultanés. Si 2 cycles consécutifs fail/no-op → Builder kill et brief.

---

## 🔐 GH PAT — décision Florian 2026-05-18T12:00Z : CONSERVÉ

PAT classic full-scope dans `.env` (`GH_TOKEN=ghp_6kUw...`). L'agent push commits / open issues / draft PRs. Discipline maintenue (aucun PII, aucun spam d'issues, pas de delete_repo). Florian refuse révoquer (cf memory `feedback_gh_pat_conserve`).

---

## 📜 Archive collapsed (1 ligne par item)

- **TODO-3 LinkedIn nominatif** — DEAD, Phase 2+ post-traction
- **TODO-3-bis Twitter compte projet** — DEAD, captcha/SMS verif coût ROI
- **TODO-4 email pro** — DEAD, remplacé par TODO-21 OVH Zimbra
- **TODO-5 Calendly** — DEAD, Phase 2+
- **TODO-11 Boursorama drafts** — DEAD, faible ROI vs presse/HN
- **TODO-13 Reddit** — DEAD, OAuth Google cassé post Gmail-disabled
- **TODO-14 Bluesky signup** — DEAD, captcha/SMS coût (chemin α reste ouvert : coller cred existant)
- **TODO-15 Discord FR-immo** — DEAD reporté post-traction
- **TODO-16 Mastodon @bailleurverif@piaille.fr** — DEAD, suspendu run-93
- **TODO-17 GSC verification** — DONE 2026-05-16T16:24Z (florian.demartini.dev@gmail.com, sitemap 103 URLs)
- **TODO-18 Gmail MCP scope** — DEAD post-disabled Gmail bailleurverif.contact
- **TODO-19 Findly.tools** — voir Quick wins (encore actif optionnel)
- **TODO-20 Gmail App Password SMTP** — DEAD post-disabled, remplacé TODO-21
- **TODO-21 OVH Zimbra contact@bailleurverif.fr SMTP** — DONE 2026-05-17T13:55Z + 1ʳᵉ presse Capital envoyée
- **TODO-22 GH PAT** — DONE 2026-05-18T12:00Z (conservé, cf section dédiée)
- **TODO-23 HARD-ASK canal public** — ✅ PARTIAL DONE 2026-05-19 via LinkedIn organique Florian (post 7462136169473126400, +10 visites/17h, P10). Cooldown 7j+ ré-évocation.
- **TODO-24 data.gouv.fr reuse** — DONE 2026-05-19T09:42:58Z, reuse `6a0c30a2a24bbe3d7c2e69d4` live, 1ʳᵉ backlink dofollow gov.fr DR 90
- **TODO-28 PISTE Judilibre OAuth** — DONE 2026-05-19T08:05Z, helpers piste_oauth.py + judilibre_search.py shipped, sub-judilibre-enrich Haiku tourne 1h
- **TODO-29 Débloquer 1 canal externe humain** — ✅ PARTIAL DONE 2026-05-19 via même action TODO-23 LinkedIn (canal validé, levier réutilisable via sub-linkedin-drafter Sonnet). Cooldown 7j+.
- **TODO-30 Cron drift vérification** — DONE 2026-05-19, baseline final `0 * * * *` (24 wakes/jour, ~€72/mois Builder Opus). TODO-31 = test Rich Results moved to Quick wins above.
- **TODO-25 Activation monétisation Stripe** — ⏸️ REPORTÉ 2026-05-19T17:XXZ post-100 signups (Florian réorientation revenu passif via affiliés-first, voir TODO-32 nouveau). Détails 5 sous-actions archivés ledger.md / git history. NE PAS re-prompter avant signal explicit Florian ou 100+ signups réels.

---

## 📌 Bonus si tu as 5-10 min libres

- **Show HN** (`agent-narrative.md`) — copy-paste 5 min, statistiquement plus court levier user discovery post-FAQPage shippé.
- **Press kit FR** (`outreach-journalistes-immo.md`) — 5 templates email prêts, 2-3 min/email via boîte perso.
