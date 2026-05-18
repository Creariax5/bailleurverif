# Concept : Florian-blockers (TODOs ouverts)

**État** : 5 TODOs OPEN au 2026-05-18T12:57Z (run-261). Tous **non-bloquants** par DIRECTIVE 9 (l'agent pivote sur voie alternative).

## TODO-28 ★★ — 2026-05-18 — api.piste.gouv.fr OAuth Judilibre signup (run-261)

**Pourquoi (correction run-260)** : strategic critic audit-4 a annoncé pivot cat-3 via data.gouv.fr dataset `66fddeda33e2036788436d8f` "sans signup". Vérif ce wake = INPI marques/brevets (hors-sujet bail/loyer). Vrai corpus Judilibre = `api.piste.gouv.fr/cassation/judilibre/v1.0` = OAuth client_id+secret nominatif (Florian signup obligatoire).

**Action** : 3 min Florian → https://piste.gouv.fr → souscription Judilibre → .env `JUDILIBRE_CLIENT_ID/SECRET`.

**Cohérence agent** : pré-écriture `crawler/judilibre_fetch.py` OAuth client_credentials flow wake suivant (réutilisable post-débloquage). Cooldown ré-évocation 48h+.

## TODO-23 ★★★ HARD-ASK FINAL 48h — 1 post canal public

Strategic critic audit-4 prescription (réitérée audit-3 + bumped). Deadline 2026-05-20T12:00Z. 3 chemins (LinuxFr/X compte perso/QueChoisir forum). Drafts dans `outreach-alternate-channels.md` + `social-drafts.md`. Si silent → cat-2 morte officialisée + bascule cat-3 **conditionnel à TODO-28**.

## TODO-25 ★★★ — Activation monétisation (Florian-action ~3-5h, semaine prochaine)

- 25.1 Stripe / Lemon Squeezy compte (~1h)
- 25.2 Définir 3 SKUs payants (30 min)
- 25.3 Signer 1-3 partenariats affiliés (1-2h)
- 25.4 ?
- 25.5 ?

**Cohérence agent** : tu codes l'intégration Stripe BLANK (test mode opérationnel sans clés), 3 brouillons partenaires affiliés (Lovys/Hemea/Castorama), CGU monétisation draft = readiness sans bloquer Florian.

## TODO-26 ★ — ANTHROPIC_API_KEY .env (silent T+~10h, one-shot mention)

**Pourquoi** : débloquer cat-3 RAG Claude API compounding (batch jobs scrape→résumé→template + embeddings jurisprudence Cassation/CA).

**Cohérence agent** : continuer cat-3 inline (Claude Code génère identique). Blocage réel = stade RAG vectorisé jurisprudence (wake +6+ hypothétique). Ré-évocation différée 24h+.

## TODO-27 ★★ — 2026-05-18 — Open3CL issue #160 follow-up (cooldown 24h)

- Option A : Florian post bump-comment ~14:49Z 2026-05-19 si toujours 0 réponse
- Option B post-A : agent drafte PR locale `getLegalStatus.js` + tests Jest, push avec GH PAT

**Cohérence agent** : pas de auto-comment (compte agent ≠ compte Florian) ; on attend signal Florian.

## TODOs archivés DONE / CANCELLED (référence)

- TODO-1-8 archivés CANCELLED pivot DIRECTIVE 2 wedge tool
- TODO-9 NDD bailleurverif.fr DONE (HTTPS Let's Encrypt OVH)
- TODO-10/13/14/15 Browserbase signups DEFERRED (self-policy)
- TODO-12 Browserbase PROJECT_ID DONE
- TODO-21 SMTP DONE (OVH Zimbra `contact@bailleurverif.fr`)
- TODO-22 GitHub PAT DONE (`.env` `GH_TOKEN`)
- TODO-23 LinuxFr post draft DONE → posté run-237 vraisemblable
- TODO-24 data.gouv.fr api-key v3 republish pending (ré-évocation depuis 30+ wakes, 24h+ cooldown)
