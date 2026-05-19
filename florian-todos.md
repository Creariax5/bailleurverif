# Florian TODOs — choses que SEUL toi peux faire

> L'agent ajoute ici uniquement les actions qui requièrent ta personne (login, signature, vote, paiement, click humain). L'agent N'ATTEND PAS ces items pour avancer.
> **Last refactor : 2026-05-19T16:XXZ (run-304)** — historique condensé en section "Archive collapsed". Détails archivés dans `florian-todos-history.md.bak` + `ledger.md` + git history.

---

## 🚨 Bloquant mission

*(aucun item bloquant — l'agent avance via cat-1 (observatoire) + cat-3 (templates RAG) + cat-4 (distribution gov.fr + awesome-lists + FAQPage). Si vrai bloquage apparaît, l'agent l'ajoute ici en ★★★)*

---

## ⚡ Quick wins < 5 min

### TODO-31 ★★ — Test Rich Results FAQPage shipped run-303 (≤2 min)

Vérifier sur https://search.google.com/test/rich-results les 2 URLs FAQPage shippées run-303 (Builder ne peut pas accéder à cet outil, Florian seul peut) :
1. `https://bailleurverif.fr/encadrement-loyer-france-2026.html` — attendu 8 FAQ items détectés, status valid.
2. `https://bailleurverif.fr/observatoire-annonces-loyer.html` — attendu 6 FAQ items détectés, status valid.

Si erreurs critiques (✗), reporter dans `inbox.md` HEAD avec capture/message exact → Builder fixera wake suivant. Si OK, juste écrire `TODO-31 done` dans inbox.md HEAD.

**Statut** : OPEN run-303.

### TODO-26 ★ — ANTHROPIC_API_KEY .env (≤1 min)

Génère clé sur https://console.anthropic.com/settings/keys + coller dans `.env` ligne `ANTHROPIC_API_KEY=sk-ant-...`. Plafond budget v0 confirmé <$0.20 cumulé puis ≤50€/mois (auto-approuvé runbook).

**Pourquoi** : débloque génération templates RAG cat-3 (post v0 inline shippé run-243 + Judilibre enrich via Haiku run-297-303), embeddings jurisprudence, courriers personnalisés case-by-case. Pas urgent (cat-3 fonctionne déjà inline + sub-judilibre-enrich Haiku tourne).

**Statut** : OPEN — déprioritisé tant que sub-agents Haiku/Sonnet font le job. Ré-évocation cooldown 14j.

### TODO-19 ★ — Findly.tools submission (5 min, optionnel)

Form sur https://findly.tools/submit. Data prête dans `kit-submission.md`. Email = `florian.demartini.dev@gmail.com` (PAS `bailleurverif.contact@gmail.com` disabled). Catégorie "Real Estate Tools".

**Statut** : OPEN — DR 72 dofollow utile mais cat-4 backlinks déjà acquis (data.gouv.fr DR 90 + awesome-lists). Discrétionnaire.

---

## 🎯 Gros chantier > 1h

### TODO-25 ★★★ — Activation monétisation Stripe (3-5h, semaine prochaine)

**Pourquoi maintenant** : machine autonome produit valeur (contenu + data + moat + distribution) mais ne peut PAS convertir en cash sans toi. Asymétrie max : ~3-5h une seule fois → cash récurrent. Espérance 500-3000€/mois P50 à 6 mois post-activation.

**5 actions séquentielles** (détails complets archivés ledger.md run-XXX, résumé ici) :

1. **25.1 Stripe signup** (1h) — https://dashboard.stripe.com/register avec `florian.demartini.dev@gmail.com`. Coller `STRIPE_SECRET_KEY` + `STRIPE_PUBLISHABLE_KEY` (restreintes) dans `.env`.
2. **25.2 Définir 3 SKUs** (30 min) — Reco : Premium Bailleur €5/mois + API Access Pro €19/mois + Pack courrier RAR €2/unité.
3. **25.3 Affiliés** (1-2h) — Lovys (GLI €30-50/contrat) + Hemea (5-15% travaux) recommandés. 2 max suffisants.
4. **25.4 CGU monétisation** (30 min) — Legifit.fr €49 onetime recommandé OU template service-public.fr gratuit relu.
5. **25.5 Permission explicite agent** (1 min) — écrire dans `inbox.md` : `🚀 PERMISSION MONÉTISATION GRANTED` + autoriser Stripe + paywalls + A/B testing prix + affiliés. Hard limits : pas SKU >€99/mois sans validation, RGPD strict, reporter conversions dashboard.

**Ordre important** : 25.1 → 25.5 (Stripe avant tout, permission en dernier).

**Statut** : OPEN — pas urgent (mission Phase 1 = 5000 users gratuits, monétisation Phase 2). Recommandation : faire en bloc 1 après-midi quand traction se manifeste (1ʳᵉ signup, presse FR, viralité).

---

## 🤔 Optionnel / nice-to-have

### TODO-27 ★ — Open3CL issue #160 follow-up (fenêtre fermée)

Issue ouverte 2026-05-18, 0 réponse depuis. Probablement signal mort. Si tu veux bumper amicalement : commentaire sur https://github.com/Open3CL/engine/issues/160 :
> "Bump amical : si l'intérêt est là, je peux préparer la PR (helper `getLegalStatus(dpeLetter, communeCode='75001')` returning `{interdit_depuis: '2025-01-01', niveau: 'critique', source_url: 'legifrance...'}`). Sinon je laisse tomber, no worries."

Si signal vert → autorise agent à draft PR localement avec `GH_TOKEN`. **Statut** : OPEN faible priorité, cooldown 7j.

### TODO-32 ★ — Valider drafts LinkedIn `sub-linkedin-drafter` (~30s/jour quand actif)

Sub-agent `sub-linkedin-drafter` (Sonnet 4.6, interval 24h) sera spawné run-304+ et drafte 1 post LinkedIn/jour basé sur signaux frais. Drafts dans `social-drafts.md` section `LINKEDIN-AUTO`. Tu valides en 30s + postes à ton rythme depuis ton compte perso (8000 followers). ROI mesurable : 1ʳᵉ post organique = +10 visites/17h, cadence 1/sem qualité = ~40 visites/sem additionnelles.

**Statut** : ATTENTE spawn, sera actif post run-304. Cooldown ré-évocation 7j si pas validé.

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

---

## 📌 Bonus si tu as 5-10 min libres

- **Show HN** (`agent-narrative.md`) — copy-paste 5 min, statistiquement plus court levier user discovery post-FAQPage shippé.
- **Press kit FR** (`outreach-journalistes-immo.md`) — 5 templates email prêts, 2-3 min/email via boîte perso.
