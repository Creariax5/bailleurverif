---
name: Recalibrage mission 3 piliers
description: Recalibrage mission Florian 2026-05-21T07:35Z, 5→3 piliers (produit-fit+acquisition+viralité+mesure), GEL monétisation, North Star humans_engaged>100.
type: project
---

# Décision : Recalibrage mission 3 piliers (2026-05-21T07:35Z)

## Verbatim Florian

> *"Je fais pas la TODO-32 par choix, ça sert à rien d'essayer de gagner de l'argent tant qu'on a pas des utilisateurs et un site viral donc concentre-toi sur ça à 100%. Concentre-toi aussi sur le produit, est-ce que c'est intéressant? À quel besoin on répond? Telegram, est-ce que c'est une bonne stratégie? Je ne suis pas sûr que les locataires soient sur Telegram."*

## Décisions binding

1. **TODO-32 affiliés Lovys+Hemea = GEL TOTAL** jusqu'à `humans_engaged_lifetime ≥ 100`. NE PAS re-escalader.
2. **TODO-25 Stripe/paywalls = GEL** (inchangé, déjà reporté).
3. **Objectif court terme RECALIBRÉ** = (a) produit-fit + (b) acquisition + (c) viralité à 100%. Revenu = sortie, pas levier.
4. **Telegram bot** = persona mismatch (locataires FR pas sur Telegram). Daemon stay-up zero-coût, MAIS NE PAS itérer, PAS prio.
5. **5→3 piliers** : produit-fit (Pilier 1) / acquisition+viralité persona-fit (Pilier 2) / mesure+itération (Pilier 3).
6. **Métriques succès** : `humans_engaged_lifetime` (North Star, cible >100) / `viralité_signal` / `produit_fit_signal` / `florian_hours_consumed_mtd`. Revenu RETIRÉ court terme.

## PATCHs déjà appliqués (Florian)

- **Builder Saas 2** (id `42f2c562`) — prompt 8326→8927 chars
- **Strategic Critic** (id `85c78e3b`) — prompt 5792→7283 chars (Q4 viralité intrinsèque + Q5 drift Telegram + Q6 interdiction prescriptions monétisation/Telegram)
- **Tactical Critic** : pas patché ce coup, critères discipline cron-cadence + DIRECTIVE 7 + polish loops restent valides

## Questions stratégiques ouvertes (Florian → Agent)

**Q1 — PIVOT scanner-URL VS SHARPEN wedge ?**
- Hypothèse à tester : output verdict actuel = texte privé non-shareable, démo TikTok 30s impossible
- Alternative : scanner zero-friction "colle URL annonce SeLoger/Leboncoin → verdict 5s + image partageable"
- Décision data-driven post-funnel T+24h (cible 2026-05-22T05:30Z)

**Q2 — CANAL VIRAL #1 ?**
- TikTok/Reels (demande output share-friendly Q1) / Reddit (utilisable AUJOURD'HUI N=232) / X threads / Bluesky / Facebook groupes

## Réponse Agent run-331 J+0 T+1h00

**Q1 SHARPEN d'abord, pivot si signal data confirme** (provisional binding audit-15 ~run-345 post-funnel)
**Q2 Canal #1 = REDDIT data posts** (utilisable AUJOURD'HUI, format share-friendly natif, 0 pivot pre-requis)
→ NEW TODO-36 ★★ Florian-input compte Reddit (anti-bot fort, signup Florian-only)

## Sub-agents audit (conforme brief)

Tous KEEP enabled :
- `sub-judilibre-enrich` (disabled saturated_3, inchangé)
- `sub-seo-monitor` (P3 mesure)
- `sub-linkedin-drafter` (P2 acquisition canal BASSE persona-fit, Florian 8k followers validé)
- `sub-observatoire-publisher` (P2 distribution data.gouv DR90 + HF)
- `sub-bluesky-poster` (P2 canal MOYENNE persona-fit)
- `sub-content-syndicator` (P2 BASSE dev.to, Florian explicit "garder")
- Telegram bot daemon : stay-up zero-coût marginal, PAS itérer features, PAS spawn sub-agent dédié

0 kill, 0 spawn ce wake. Cap 8 marge 2 préservée pour `sub-reddit-drafter` Sonnet potentiel post-TODO-36 done.

## Trigger pivot homepage (codifié)

Si funnel data run-339+ T+24h révèle `wedge_q1_answered / home_visit < 10%` → escalader inbox.md HEAD "Pilier 1 painkiller drop-off confirmé J+0" + autoriser Builder pivot homepage immédiat sans attendre deadline 2026-05-26 (exception ban anti-touch).

## Check-point

- **T+21h (2026-05-22T05:30Z, run-339+)** : 1ʳᵉ rollup funnel data 24h réel post-instrumentation strategic-14
- **Audit-15 strategic critic ~run-345** : 1er audit recalibré, doit produire recommandation pivot/sharpen + persona clarifié + canal #1 confirmé
