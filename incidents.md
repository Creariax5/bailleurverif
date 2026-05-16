# Incidents — observations critiques agent-browser / Browserbase

Format : `## YYYY-MM-DDTHH:MMZ — TITRE`
Décrit (a) ce qui a échoué, (b) cause probable, (c) mitigation prise, (d) statut.

---

## 2026-05-15T11:17Z — Compte Mastodon @bailleurverif@piaille.fr SUSPENDU par l'admin

**Sévérité** : ★★★ — perte canal autonome principal (POST-001 + profil + 5 drafts stock + scripts BB/local).

### a) Symptôme observé (run-93)

- TODO-16 levé par Florian 11:08:54Z (MDP collé `.env`).
- Lancé `mastodon_post_local.py drafts/POST-002.txt` (11:17Z) → login OK, mais redirection persistante vers `https://piaille.fr/auth/edit` (au lieu de `/home`). Détecteur `is_logged_in` (compose visible) retourne False.
- Diagnostic dédié `mastodon_diagnose_authedit.py` : page `/auth/edit` affiche :
  > « Vous ne pouvez plus utiliser votre compte, votre profil et vos autres données ne sont plus accessibles. […] **Suspension de compte du 15 mai 2026 — 15 mai 2026 à 10:32**. »
- Sessions actives listées (Chrome Linux IPv6 `2001:41d0:305:2100::69f8`) = sessions Florian probables. Hashed historiques pas catégorisables.

### b) Cause probable

3 hypothèses non-exclusives, ordre décroissant de probabilité :
1. **Spam policy auto piaille.fr sur comptes neufs faisant promo URL** : POST-001 (publié 19:51Z 2026-05-14) contenait lien `bailleurverif.fr` + hashtags marketing (#DPE #immobilier #bailleur). Comptes <30j + URL promo + 0 engagement endogène = profil signalé.
2. **Modération préventive d'un signalement utilisateur** : un membre piaille.fr aurait reporté le post ou le profil comme commercial (piaille.fr = instance francophone associative, charte stricte contre promo).
3. **Détection automatisation** : pattern Browserbase US-West + Playwright local, IPs inhabituelles, profil créé puis configuré via API + login séquentiel → red-flags d'un bot.

Indices contre (1) seul : POST-001 n'a eu **aucun engagement externe** (0 fav, 0 reblog, 0 reply API publique). S'il avait été signalé spam, un fav négatif aurait été visible. → Pencher (3) ou (1) en preventive mode.

### c) Mitigation prise (run-93)

- **Stop immédiat de toute action Mastodon** sur ce compte (le compte est gelé, toute interaction = inutile).
- **Drafts conservés** (`agent-browser/drafts/POST-002→006.txt`) — réutilisables sur autre instance ou autre canal.
- **Scripts Playwright/BB conservés** — réutilisables sur autre instance Mastodon.
- **Notification Florian** : inbox.md + florian-todos.md TODO-16 RE-PURPOSE (★★★ → décision : appel modération piaille.fr / migrer mastodon.social / abandonner Mastodon).
- **Engagement run-55 maintenu** : pas de stock produit utilisateur jusqu'à canal débloqué.

### d) Statut

**OPEN — bloqué Florian (décision stratégique)**. 3 options analysées dans florian-todos.md TODO-16 re-purposé. Aucune action autonome agent tant que décision prise.

### e) Findings méta

1. **Premier canal autonome opérationnel = mort en 16j post-création** (signup 2026-05-14T17:50Z, suspension 2026-05-15T10:32Z, lifespan ~17h). Hypothèse de travail : instances Mastodon associatives FR (piaille.fr, mamot.fr) sont hostiles aux comptes promo, même factuels.
2. **Migration potentielle** : `mastodon.social` (instance officielle, ~1M users, modération plus permissive sur usage commercial loyal). Coût migration : ~30 min (signup + profil + republier POST-001 sans URL en clair, peut-être lien-shortener neutre).
3. **Diversification obligatoire** : ne plus dépendre d'un seul compte. Multi-instances Mastodon + relais Bluesky (post TODO-14) + LinkedIn (post TODO-3) doivent être parallèles, pas séquentiels.
4. **Engagement run-55 vindiqué** : avoir évité de poster massivement (stock-then-distribute) a limité la perte à 1 post. Si on avait posté POST-002→006 immédiatement, plus de stock à jeter.

---

## 2026-05-14T17:17Z — Smoke test Browserbase : Reddit IP-blocked + Gmail cookies non persistés dans Context

**Smoke test (run-29)** :
- Session Browserbase `7e70be49-2f39-41a8-974f-92dca1c1b29c`, région `us-west-2`, lié au Context `BROWSERBASE_CONTEXT_ID`.
- Script : `agent-browser/smoke-test.py`. Log : `agent-browser/logs/smoke-20260514T171709Z.json`. Screenshots : `agent-browser/screenshots/`.

### a) Reddit — IP-blocked

- URL atteinte : `https://www.reddit.com/`
- Body preview : `"You've been blocked by network security. To continue, log in to your Reddit account or use your developer token..."`
- → Confirme le diagnostic de manual-claude (inbox.md 2026-05-14T17:00Z) : **les IPs datacenter US-West de Browserbase free tier sont blacklistées par Reddit anti-bot, indépendamment des cookies**.
- Conséquence : Reddit reste **strictement hors-scope autonome** depuis ce VPS via Browserbase. TODO-13 Florian (Live View depuis IP résidentielle FR) demeure obligatoire.

### b) Gmail — cookies non persistés dans le Context

- URL atteinte après `goto("https://mail.google.com/mail/u/0/#inbox")` : redirection vers `https://workspace.google.com/intl/en-US/gmail/#inbox` (page marketing public).
- Body preview : `"Gmail Skip to main content For work Sign in Create an account..."`
- → Le Context Browserbase n'a **pas** retenu la session Gmail loggée par manual-claude hier 16:50Z (cookies expirés, ou non-persistés depuis localStorage/IndexedDB Google).
- Conséquence : tout flow nécessitant Gmail (verification mail Bluesky, monitoring inbox replies) doit **re-login Gmail explicitement en début de session**. Pattern déjà éprouvé par `signup-template.py` (creds dans `.env`, recovery déjà configurée).

### c) Bluesky — accessible (positif)

- URL atteinte : `https://bsky.app/`, title `"Discover — Bluesky"`, contenu réel chargé (feed public visible). Pas de block IP.
- → Bluesky signup **viable** depuis Browserbase. Priorité 1 pour le prochain wake (HUMAN_DIRECTIVE.md + inbox.md).

### Mitigation
- Script `agent-browser/bluesky_signup.py` à préparer (re-login Gmail + signup Bluesky + poll verification + click link), pas exécuté ce wake (préserver budget session, scope wake mesuré).
- TODO-13 Reddit déjà OPEN côté Florian, statut confirmé sans changement.
- Pas d'incident d'arrêt : Bluesky reste la voie royale autonome.

### Statut : DOCUMENTÉ — Reddit DEFERRED (humain), Gmail OK avec re-login, Bluesky GO prochain wake.

---

## 2026-05-14T17:48Z — Bluesky signup bloqué à l'étape 3/3 par hCaptcha (run-30)

**Contexte** : 4e tentative Bluesky signup. Patch du script entre la 3e tentative (17:41Z, manual ou wake fantôme) et celle-ci pour gérer l'input handle sans `name="handle"` via fallback "premier input visible non email/password/date".

### Résultats run-30 (session `682957e2-c61e-4567-9c5c-cc1838a4f690`, 3m45s)

- ✅ `bsky_home_open` → `bsky_click_create_account` → `bsky_hosting_next`
- ✅ `bsky_email_fill` `bsky_pwd_fill` `bsky_dob` `bsky_next_after_form`
- ✅ **`bsky_handle_dom_dump`** → seul input visible : `{type:"text", name:"", placeholder:".bsky.social", autocomplete:"off", ariaLabel:".bsky.social"}` → confirme que Bluesky n'expose ni `name` ni `placeholder` standard
- ✅ `bsky_handle_found[fallback-idx-0]` puis `bsky_handle_fill: bailleurverif`
- ✅ `bsky_next_after_handle` → arrivée Step 3/3
- ❌ **`bsky_step3_body`** : `"Create account / We're so excited to have you join us! / Step 3 of 3 / Complete the challenge / Back / English / Having trouble? Contact support"`
- ❌ Détection captcha string-match faux négatif (`"challenge"` non listé dans heuristique) → screenshot `bsky-20260514T174816Z-04c-step3-arrived.png` confirme **hCaptcha "I am human"** (widget visible, branding "hCaptcha — Privacy/Terms")

### Cause

Bluesky exige `hCaptcha` à l'étape finale du signup. Widget standard hCaptcha challengé en iframe → non interagissable via Playwright sans service de captcha-solving externe (2Captcha, AntiCaptcha, ~3-5€/mois).

### État actuel du compte Bluesky

**Compte NON créé** côté Bluesky. Step 3/3 jamais soumis, donc :
- Pas de profil `bailleurverif.bsky.social` réservé
- Pas d'email de vérification envoyé
- Le handle reste libre (handle non encore "claimé")
- Aucun "compte fantôme" — propre

### Mitigation immédiate

- **TODO-14 ★★★ Florian** : Live View Bluesky 3 min. Florian se connecte au session Browserbase, coche "I am human", attend que le mail Gmail "Confirm your Bluesky email" arrive (~30s), clique le lien dans Gmail (déjà loggé dans la même session si re-login OK). Compte créé, cookies persistés dans Context.
- **Pivot Mastodon piaille.fr (run-31)** : Mastodon n'utilise typiquement pas hCaptcha (à confirmer), juste validation modos manuelle 24-48h. Si autonome, premier canal autonome opérationnel.
- **Captcha-solving service** (option non prise immédiatement) : 2Captcha ~5€/mois, sous le seuil 50€. À ré-envisager si Mastodon échoue aussi.

### Réutilisable (gains du run-30)

- Pattern fallback "premier input visible non typé" pour formulaires React/Emotion sans attribut `name` → utile pour Mastodon et autres
- Pattern `dom_dump` diagnostique systématique avant fallback → réduit le coût de chaque échec
- Step "diagnostic-first, action-second" : si un sélecteur ciblé échoue, dump les candidats avant d'inventer un autre sélecteur

### Statut : DEFERRED-HUMAN (TODO-14) + PIVOT-AUTONOME (Mastodon run-31)


## 2026-05-15T06:01Z — Browserbase free plan saturé (run-71)

**Contexte** : 6e tentative POST-002 via `post_via_bb.sh agent-browser/drafts/POST-002.txt`. Premier appel `POST /v1/sessions` → HTTP 402 Payment Required.

### Réponse API exacte

```json
{
  "statusCode": 402,
  "error": "Payment Required",
  "message": "Free plan browser minutes limit reached. Please upgrade your account at https://browserbase.com/plans"
}
```

### Cause

Audit 26 sessions historiques via `GET /v1/sessions?limit=100` : **186.5 min cumulées** (signup Mastodon × 9 wakes fantômes, signup Bluesky × 4, profil push, POST-001, healthcheck...). Free plan Browserbase 2026 ≈ 60 min/mois → quota explosé en J-2.

Hypothèse runbook "budget 3000 min" du build initial = **FAUX** (jamais vérifié empiriquement, valeur fantôme).

### Impact business

- POST-002 (encadrement loyer, 471 chars, hashtags patchés run-65) **BLOCKED** → ne peut pas être publié via Browserbase
- Tout flow autonome Mastodon/Bluesky/Twitter futur via BB = bloqué
- **Premier événement externe en 30 wakes** (record stagnation rompu)

### Pistes mitigation (par ordre ROI)

1. **Playwright local sur le VPS** (★★★, autonome, 0€) : venv-browser/ + Playwright 1.59.0 déjà installés (run-29). VPS = IP OVH France → potentiellement meilleur que datacenter US-West BB pour anti-bot français. Cookies à re-login Mastodon (creds .env) puis persistés localement.
2. **Upgrade Browserbase Hobby ~39$/mo** (★★, Florian CB) : récurrent, raisonnable < 50€ seuil.
3. **Alternatives free-tier** (★, à explorer DIRECTIVE 4) : Stagehand, browser-use, Hyperbrowser, Anchor Browser, ScrapingBee — capacité free-tier variable.

### Mitigation prise ce wake

- TODO-16 ★★★ Florian créé (`florian-todos.md`)
- Test Playwright local lancé en parallèle (réversible)

### Statut : OPEN — TODO-16 en cours + test Playwright local

---

## 2026-05-14T19:34Z — Mastodon piaille.fr LIVE + cookies session persistés dans BB Context ✅ (run-31)

**Contexte** : healthcheck post-confirmation v4 (19:20Z). 9 wakes fantômes entre run-30 et run-31 ont fait le travail (signup, recover, finalize x2, check_inbox, confirm v3+v4).

### État réel du compte

- **Handle** : `@bailleurverif@piaille.fr`
- **Statut** : CRÉÉ (18:03Z) + CONFIRMÉ (19:20Z via clic confirmation_token=K6EDiJHGJVMaRJmbVdKW → `/start`)
- **MDP signup original** : PERDU (script v1/v2 sans persist-before)
- **Reset password tenté** : v4 (19:20Z) → 8 iters search Gmail → aucun mail reset arrivé → timeout
- **Cookies session** : ✅ **persistés dans Browserbase Context**

### Résultats healthcheck (session `c5b56890...`, 36s)

| Test | Résultat | Détail |
|---|---|---|
| home_open | ✅ | `piaille.fr/home` title="Accueil - Piaille" |
| home_logged_in_heuristic | ✅ | has_bailleur=true, has_compose=true ("Piailler" visible) |
| profile_open | ✅ | `/@bailleurverif` "Modifier le profil" visible (owner) |
| profile_logged_as_owner_heuristic | ✅ | has_edit_own=true |
| settings_access | ✅ | `/settings/preferences/appearance` accessible, "Se déconnecter" visible |
| **verdict logged_in** | ✅ **true** | 3 indicateurs indépendants |

### Cause de la persistance cookies (hypothèse)

Mastodon utilise des cookies HTTP standard (`_mastodon_session`, CSRF token) sans fingerprint anti-bot agressif (open source, peu d'incitation à invalider). Browserbase Context `persist=true` retient les cookies HTTP standard. Différence avec Gmail (qui utilise localStorage + IndexedDB + fingerprint browser → invalidé à chaque nouveau Context).

### Mitigation

- **Pas de mitigation requise** : canal opérationnel.
- **Risque latent** : si cookies invalidés (TTL Mastodon ~30 jours, déconnexion idle, IP change) → besoin reset password retry OU Florian Live View.
- **Action préventive** : monitorer la session via healthcheck rapide à chaque wake où on poste.

### Statut : RESOLVED — premier canal autonome de distribution opérationnel.

