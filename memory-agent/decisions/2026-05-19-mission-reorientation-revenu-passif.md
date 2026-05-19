# Decision : Mission reorientation revenu passif (Florian 2026-05-19T17:XXZ)

**Date** : 2026-05-19T17:XXZ (Florian verbatim inbox.md)
**Ack agent** : run-307 J+0 (2026-05-19T20:28Z, après run-306 critic-22 priorities qui avait éclipsé cette directive)
**Type** : Strategic / Mission directive (verbatim)

## Verbatim Florian

> *"Mon vrai but est de laisser faire l'agent pour que au bout d'un moment ça me fasse du revenu passif. Et pour TODO-25 je pense que c'est pas utile tant que y a pas des vrais users."*

## Décision

**Mission cible** : revenu passif sustainable. Court terme €100-500/mois @ 6m. Long terme €500-3000/mois @ 12m. Input Florian ≤1h/mois post-setup.

**"5000 users 90j" = stretch goal motivant, PAS la métrique de succès.**

## 5 piliers stratégiques validés Florian

1. SHARPEN homepage UN single painkiller (ex: "Loue-je à un loyer légal? Tape ton adresse" → signup-gated PDF lettre baisse loyer).
2. SEO COMPOUNDING pages programmatiques ville-par-ville (200+ pages, post-pilier 1 validé).
3. AFFILIÉS AVANT subscriptions (Lovys + Hemea, skip Stripe TODO-25 actuel).
4. VIRAL MECHANIC notation agences immobilières publique (naming and shaming).
5. CONTENU LINKEDIN automatisé (`sub-linkedin-drafter` déjà spawné, Florian 8000 followers).

## Métriques succès (remplacent 5000 users)

1. `affiliate_revenue_mtd` (principal)
2. `signups_real_qualified_mtd` (proxy revenu)
3. `organic_traffic_30d_compounding_growth`
4. `florian_hours_consumed_mtd` (DOIT décroître, North Star autonomie)
5. (post-affiliés) `signups_to_paying_conv_pct`

## Bans explicites

- TODO-25 (Stripe + paywalls + SKUs B2C €5-19/mo) → **REPORTÉ post-100 signups**. NE PAS re-prompter avant signal Florian.
- Vanity metrics : `pages_total`, IndexNow rounds, JSON-LD coverage 100%, sitemap URLs counted.
- Cible "5000 users 90j" comme métrique chiffrée stricte.

## Nouveaux TODOs Florian

- **TODO-32 ★★** (NEW) : Signer 2 affiliés Lovys + Hemea (1-2h, `.env` `LOVYS_AFFILIATE_ID=` + `HEMEA_AFFILIATE_ID=`).
- **TODO-33 ★** (NEW) : Parler 5 personnes entourage, 1 question painkiller (1h one-shot).
- **TODO-32 ancien** (drafter LinkedIn validation) → renommé TODO-32-bis ★ section Optionnel.

## Pivot exécution

**Priorité #1 prochain wake** : démarrer pivot homepage painkiller (audit `wedge-tool/templates/index.html` puis refactor incrémental sur 2-3 wakes Builder cumulé).

**Critères pivot painkiller** : 1 question urgente googlée en panique, réponse 5s, signup gate sur action (PDF lettre).

**Pivot autorisé** si data montre painkiller alternatif plus prometteur (DPE F/G, dépôt garantie). Doit documenter `WHY_THIS_NOT_THAT`.

## Cooldown / Trigger reverse

- Réorientation = active jusqu'à signal Florian explicite "stop" ou nouvelle directive.
- Critic prompts (tactical + strategic) PATCHés par Florian inbox.md 17:XXZ pour refléter direction (drift signal → `CRITIC PATCH suggested:` ligne inbox).
- Trigger subscriptions (TODO-25 ré-ouvrable) : 100+ signups gratuits + feature payante demandée par utilisateurs réels.
