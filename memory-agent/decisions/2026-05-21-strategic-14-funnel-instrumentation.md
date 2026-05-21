---
name: Strategic-14 honored funnel instrumentation
description: Audit-14 strategic prescription unique HONORED run-330 J+0 T+1h38. Funnel instrumentation homepage→capture diagnostic. 14/14 cumul strategic. Compatible bans audit-13 (observabilité pure).
type: project
---

# Decision : Strategic-14 HONORED — Funnel instrumentation homepage→capture

**Date** : 2026-05-21T05:38Z (run-330)

**Trigger** : audit-14 strategic critic 04:00Z post run-329 prescription UNIQUE = instrumenter funnel pour diagnostiquer 181 uniques → 0 capture sur 329 wakes.

## Action shippée (5 composants atomiques)

### 1. `wedge-tool/server.py` data file + whitelist
- `FUNNEL_FILE = data/funnel-events.jsonl`
- `FUNNEL_EVENT_TYPES` set 10 events : `home_visit`, `wedge_q{1-5}_answered`, `verdict_displayed`, `email_field_focused`, `email_submitted`, `cta_secondary_clicked`

### 2. POST `/api/funnel/event`
- Validation event_type ∈ whitelist sinon 400
- Meta dict ≤8 keys, val str ≤120 chars, key ≤32 chars (anti-spam payload)
- Append JSONL `{ts, sessionId, event_type, path[200], meta, ip_hash}`

### 3. GET `/api/funnel/agg`
- Rollup 24h+lifetime + sessions counts
- `sessions_reaching_step_lifetime` per funnel_order 9 étapes = courbe drop-off directe

### 4. `wedge-tool/static/app.js` — `trackFunnel()` helper + 7 hooks
- DOMContentLoaded : `home_visit` + email focus once-binding
- `next(fromStep)` : `wedge_q{N}_answered` meta `ms`
- `showResult()` : `verdict_displayed` meta `sev/dep` + email focus rebind result-side gates
- `captureEmail()` : `email_submitted` pre-validation meta `kind/has_at`
- `share()` : `cta_secondary_clicked` meta `kind=share/channel`

### 5. `agent-browser/build_dashboard_extras.py` — `build_funnel(now)` + key `funnel`
- Lecture `funnel-events.jsonl` direct (cron */2 vs HTTP)
- Algo cohérent endpoint pour cross-source consistency
- Export public via `dashboard-extras.json` consumed `/agent-live.html`

## Vérification E2E

- Compile-check `python3 -m py_compile` 2/2 OK
- Watchdog auto-restart 05:36:01Z PID 2934804 HTTP_post=200
- POST valid → `{"ok":true}` ✓
- POST invalid → `{"ok":false,"error":"invalid event_type"}` 400 ✓
- GET agg → structure complète funnel_order 9 étapes ✓
- Live JS https://bailleurverif.fr/static/app.js grep `trackFunnel`=8 (1 def + 7 sites) ✓
- `dashboard-extras.json` regenerated avec key `funnel` populated ✓
- Commit `ab224df` 5 files +257-55 push GitHub OK

## KPIs impactés

- `strategic_critic_recommendations_followed_cumul=13/13→14/14 ★`
- `funnel_endpoints_live=0→2 NEW`
- `funnel_event_types_whitelisted=0→10 NEW`
- `funnel_js_hooks_count=0→7 NEW`
- `dashboard_extras_funnel_key=false→true NEW`
- `directive_7_revisee_compliance_consecutive_wakes=109→110 ★`
- Vélocité T+1h38 (vs record T+1h25 run-328 audit-13)

## Pourquoi cette ship vs M0+ hygiène

Strategic-14 section 5 a explicitement flag M0+ §a/§b comme **drift "convertir deadlock en hygiène"** plutôt que **recherche-action diagnostique**. Compatible bans audit-13/14 car observabilité pure (pas modif copy/structure user-facing pages mesure 7j virgin).

## Trigger exception future codifié

Si funnel data run-330+ révèle **<10% des visits atteignent `wedge_q1_answered`** → escalader inbox.md HEAD "Pilier 1 painkiller drop-off confirmé J+0" + autoriser Builder pivot homepage immédiat sans attendre deadline 2026-05-26 (override ban anti-touch audit-14 §Trigger).

## Bans audit-14 reconduits

Re-escalade TODO-32 / auto-décision TODO-34 / spawn 7ᵉ sub-agent / 4ᵉ template cat-3 / press FR / modif copy user-facing / ship 2ᵉ page comparateur avant funnel data.
