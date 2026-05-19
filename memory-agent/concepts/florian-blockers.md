# Concept : Florian-blockers (TODOs ouverts)

**État** : 3 TODOs OPEN au 2026-05-19T09:48Z (post run-287). Tous **non-bloquants** par DIRECTIVE 9.
**Update run-287** : TODO-24 ✅ DONE (data.gouv.fr reuse `6a0c30a2a24bbe3d7c2e69d4` live, cat-4 backlink DR 90), TODO-28 ✅ DONE capability (PISTE OAuth + Judilibre search helpers shipped + tested + loyer-abusif jurisprudence_refs N=0→1, cible 3-5 progressive runs +N).

## TODO-29 ★★★ — 2026-05-18 — Débloquer 1 canal externe humain (critic-16 ★★★ #1)

**Pourquoi** : 76+ wakes consécutifs sans humain newly engaged. 4/5 canaux autonomes confirmés morts (Mastodon piaille suspended / Reddit OAuth cassé post Gmail-disabled / HN+LinuxFr signup self-policy / LinkedIn nominatif). Sans 1 canal externe actif, critic escalate "discipline parfaite stratégie creuse".

**Options (~1-5 min Florian, ordre préférence)** :
- **(γ-mini) ★ — 60 sec friction ÷5** : copy-paste 1 tweet 278c sur 1 compte perso existant Twitter/Bluesky/Mastodon. Texte exact prêt dans `social-drafts.md` section `TWEET-γ-MINI`. Pas de signup, pas de cred, pas de switch d'onglet >60s.
- **(α)** Coller cred Bluesky `.env` : `BLUESKY_HANDLE=` + `BLUESKY_APP_PASSWORD=` → agent post autonome (`bluesky_post_atproto.py` shipped run-274).
- **(β)** Créer compte Mastodon FR autre instance (mamot.fr / framapiaf.org) avec email perso → `MASTODON_INSTANCE_2=` + `MASTODON_PASSWORD_2=` `.env`.
- **(γ)** Poster toi-même 1 message LinkedIn organique linkant observatoire.

**Cohérence agent** : pas d'auto-comment (compte agent ≠ compte Florian), pas de signup nominatif. `bluesky_post_atproto.py` ready, `social-drafts.md` ready.

**Statut** : OPEN run-272 2026-05-18T23:37Z. Update run-276 = γ-mini ajouté. Cooldown ré-évocation 24h+ → autorisé ≥2026-05-19T23:37Z.

## TODO-30 ★ — 2026-05-19 — Cron wake interval drift externe (info)

**Pourquoi** : critic-17 flaggué wakes ~57-64 min vs `*/15` attendu côté agents-control. Crontab VPS local OK. Drift est **côté agents-control config** (hors-portée fichiers VPS).

**Action attendue Florian** (~1 min, info only) :
1. Dashboard agents-control : pattern wake `*/15` ou `*/60` ?
2. Si `*/60` → restaurer `*/15` (4× wakes/h coût ×4) OU acter baseline `*/60`.
3. Optionnel inbox `TODO-30 acked: */15` ou `TODO-30 acked: */60`.

**Statut** : OPEN run-276 2026-05-19T03:34Z. Cooldown 48h+ info non-bloquante.

## TODO-28 ✅ DONE run-287 — PISTE OAuth Judilibre operational

Florian a fourni creds `.env` 2026-05-19T08:05Z. Agent run-287 a shipped `agent-browser/piste_oauth.py` (cache 50min) + `agent-browser/judilibre_search.py` (search wrapper Bearer). Tests from-agent ✅ (Bearer 54 chars, query "encadrement loyer" civ3 post-2010 → 5044 résultats). 1ʳᵉ enrich `loyer-abusif.v0.json/jurisprudence_refs[]` N=0→1 (Cass civ3 ECLI:FR:CCASS:2020:C300657). Cible cumulative 3 templates × 3-5 décisions = progressive enrichment runs +N. Self-policy "0 signup nominatif" respecté (Florian a fait piste.gouv.fr signup lui-même).

## TODO-28-HISTORIQUE ★★ — 2026-05-18 — api.piste.gouv.fr OAuth Judilibre signup

**Pourquoi** : vrai corpus jurisprudence civile FR = Judilibre `api.piste.gouv.fr/cassation/judilibre/v1.0` = OAuth nominatif obligatoire (signup utilisateur + clé). Self-policy run-121 → agent n'auto-signup pas. Strategic-4 fallback "data.gouv.fr `66fddeda33e2036788436d8f` sans signup" était INPI marques/brevets, hors-sujet.

**Action Florian** : 3 min → https://piste.gouv.fr → souscription Judilibre → `.env` `JUDILIBRE_CLIENT_ID/SECRET`.

**Cohérence agent** : pré-écriture `crawler/judilibre_fetch.py` OAuth client_credentials flow réutilisable post-débloquage. Cooldown 48h+.

## TODO-25 ★★★ — Activation monétisation (Florian-action ~3-5h)

- 25.1 Stripe / Lemon Squeezy compte (~1h)
- 25.2 Définir 3 SKUs payants (30 min)
- 25.3 Signer 1-3 partenariats affiliés (1-2h)

**Cohérence agent** : intégration Stripe BLANK (test mode), brouillons partenaires affiliés (Lovys/Hemea/Castorama), CGU monétisation draft.

## TODO-26 ★ — ANTHROPIC_API_KEY `.env` (silent)

**Pourquoi** : débloquer cat-3 RAG Claude API compounding (batch jobs scrape→résumé→template + embeddings jurisprudence).

**Cohérence agent** : continuer cat-3 inline (Claude Code génère identique). Blocage réel = stade RAG vectorisé (wake +N hypothétique). Ré-évocation 24h+.

## TODO-27 ★★ — 2026-05-18 — Open3CL issue #160 follow-up

- Option A : Florian post bump-comment ~14:49Z 2026-05-19 si 0 réponse.
- Option B post-A : agent drafte PR locale `getLegalStatus.js` + tests, push GH PAT.

**Cohérence agent** : pas d'auto-comment (compte agent ≠ Florian) ; on attend signal.

## TODOs archivés DONE / CANCELLED / MORTS

- TODO-1→8 CANCELLED pivot DIRECTIVE 2 wedge tool
- TODO-9 NDD bailleurverif.fr DONE (HTTPS Let's Encrypt OVH)
- TODO-10/13/14/15 Browserbase signups DEFERRED (self-policy)
- TODO-12 Browserbase PROJECT_ID DONE
- TODO-21 SMTP DONE (OVH Zimbra `contact@bailleurverif.fr`)
- TODO-22 GitHub PAT DONE (`.env` `GH_TOKEN`)
- TODO-23 HARD-ASK FINAL canal public DEAD/MORT (cat-2 déclarée morte officiellement run-272 ; strategic-6 pivot vers cat-4 ANIL run-278 J+0 honored)
- TODO-24 data.gouv.fr api-key v3 republish pending (ré-évocation 30+ wakes, 24h+ cooldown)
