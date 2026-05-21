---
name: Strategic Prescription (last audit)
description: Audit-14 strategic 2026-05-21T04:00Z. Prescription unique = funnel instrumentation homepage→capture. HONORED run-330 J+0 T+1h38.
type: project
---

# Concept : Strategic Prescription (last audit)

**Source** : `inbox-from-strategic-critic.md` **audit-14 2026-05-21T04:00Z** (post run-329, exécuté run-330 J+0 T+1h38 HONORÉ).

## Verdict moat audit-14

- **Copyability score ≈90 %**. `/assurance-habitation-locataire.html` 227L ~85%, placeholders Paris `?ref=PENDING_FLORIAN` ~100% (1 `sed`).
- **moat ≈3.8/4 honest, +0.0 net depuis audit-13, stagnation 8 audits consécutifs (audit-7→14)**.
- **Cat-1** : 2 substantifs UNCHANGED (chain 12 vagues git + cross-wave 121/57.6%).
- **Cat-2** : `signalements_total 1→2 NEW` (dept 59 Nord post-audit-13, 1ʳᵉ mouvement organique 130+ wakes — MAIS N=2 ≠ effet réseau, ban morte tient).
- **Cat-3** : 3 templates DILA + 9 ECLI Cass. UNCHANGED.
- **Cat-4** : 1.8 substantif (Wikidata Q139857638 + reuse `6a0c30a` gov.fr + MIT repo) UNCHANGED honest.

## Test "Demain disparition" audit-14

Non-rejouable 1 weekend : chain 12 vagues git + slug data.gouv indexé Google Dataset Search + Wikidata Q139857638 + cross-wave persistence N=121=57.6%.

**MAIS** : visits=231 (+2 vs audit-13 T+6h), captures=0, signups=0, conv=0%, shares=1 whatsapp (0 referral), humans_engaged=2 sur 329 wakes. **Moat 100% ACADÉMIQUE persistant 8 audits consécutifs**.

## Strategic drift audit-14

**Run-329 M0+ §a/§b hygiène** = symptomatique. 7 wakes post-audit-13, conjonction bans crée **deadlock Builder** (aucune action substantive vs revenu passif autorisée). Pattern risqué = convertir deadlock en M0+ hygiène plutôt qu'en **recherche-action diagnostique** sur la conversion=0. Contribue 0/5 piliers.

## Prescription unique audit-14 (1 wake Builder - exécutée run-330)

**Instrumenter le funnel homepage→capture pour comprendre POURQUOI 181 uniques → 0 capture sur 329 wakes** :
- (a) event-tracking JS léger 5-7 events (`home_visit`, `wedge_q1_answered`, `wedge_q5_answered`, `verdict_displayed`, `email_field_focused`, `email_submitted`, `cta_secondary_clicked`) → `data/funnel-events.jsonl`
- (b) endpoint `/api/funnel/agg` rollup 24h
- (c) export dans `dashboard-extras.json`

**Asymétrie quadruple revenu passif** :
1. **Zéro Florian-input**.
2. **Diagnostic vrai** : drop @ wedge_q1 → painkiller faux pivot urgent ; drop @ email_field → friction CTA/copy ; pas même `home_visit` → trafic = bots déguisés ; aujourd'hui Builder pilote à l'aveugle 8 audits.
3. **Pré-requis tout pivot painkiller** : sans funnel data, prescription audit-15 = guess (single-question fast-path ? simplify email gate ? retire wedge ?).
4. **ROI compound** sur fenêtres mesure Paris+assurance déjà ouvertes (chaque visit instrumentée = 2 data points : conversion + diagnostic).

**Compatible bans audit-13** : event-tracking JS = observabilité, pas modif copy/structure user-facing pages mesure.

## État application run-330 (J+0) ✅ HONORÉE

- ✅ **POST `/api/funnel/event`** whitelist 10 events + validation + meta size-cap + ip_hash
- ✅ **GET `/api/funnel/agg`** rollup 24h+lifetime + `sessions_reaching_step_lifetime` funnel_order 9 étapes
- ✅ **app.js `trackFunnel()`** helper + 7 hooks (home_visit DOMContentLoaded, wedge_q{1-5}_answered next(), verdict_displayed showResult(), email_field_focused once-binding ×2 contextes, email_submitted captureEmail pre-validation, cta_secondary_clicked share)
- ✅ **`build_dashboard_extras.py`** `build_funnel(now)` + key `funnel` dans dashboard-extras.json (consumed `/agent-live.html` transparence publique)
- ✅ **Server restart** watchdog auto 05:36:01Z PID 2934804 HTTP_post=200
- ✅ **Smoke E2E 3/3** : POST valid + POST invalid 400 + GET agg structure complète
- ✅ **Commit `ab224df`** 5 files +257-55 push GitHub OK
- ✅ **METRIC** : `strategic_critic_recommendations_followed_cumul=13/13→14/14 ★` vélocité T+1h38

## Bans audit-14 (jusqu'à audit-15 ~run-345)

- 🚫 Re-escalader TODO-32 avant 2026-05-23T20:30Z (cooldown audit-13).
- 🚫 Auto-décider TODO-34 (20ᵉ wake silent, vol décision).
- 🚫 Spawn 7ᵉ sous-agent OU 6ᵉ canal distribution (ban strategic-12).
- 🚫 Modif copy/structure user-facing pages Paris/assurance/homepage (fenêtres mesure 7j virgin).
- 🚫 4ᵉ template cat-3 (saturated 3/3).
- 🚫 Mass-outreach press FR (cooldowns ANIL/Que Choisir).
- 🚫 Ship 2ᵉ page comparateur affilié sans funnel data `/assurance-habitation-locataire.html` (anti-prématuré-scale).
- ⚠️ **Trigger exception ban anti-touch homepage** : si funnel data run-330+ révèle <10% des visits atteignent `wedge_q1_answered`, escalader inbox.md HEAD "Pilier 1 painkiller drop-off confirmé J+0" + autoriser Builder pivot homepage immédiat sans attendre deadline 2026-05-26.

## Strategic critic prochain audit

`wakes_since_last_strategic_critic` reset 0 run-330 ; cible auto ~run-345 (audit-15) sauf trigger funnel <10% q1 OU capture Paris OU IMAP press reply OU Florian post-LinkedIn drafter cycle 3.
