---
name: 2026-06-04 intent_signal /api/subscribe shipped
description: Brief Florian 06-03T17:00Z A.2 honored run-433. Server-side enum field + storage + aggregate exposed via /api/stats. Non-bloqué bans audit-42 (server-side seulement, 0 touch home/scan-url/share-card).
type: decisions
---

# intent_signal enum `/api/subscribe` shipped — 2026-06-04T07:50Z (run-433)

## Contexte

Brief Florian 2026-06-03T17:00Z `inbox.md` §A.2 verbatim : *"Champ optionnel `intent_signal` dans subscribe API : enum `[\"loyer-trop-cher\", \"arnaque-suspecte\", \"litige-en-cours\", \"curiosite\", \"bailleur-conformite\", \"autre\"]`"*. Action A.3 : *"Track `subscribers_by_intent` dans `memory-agent/kpis/snapshot-current.md`"*. Tactical-59 #2 ★★★ recommande server-side seulement (non-bloqué bans audit-42).

## Changements `wedge-tool/server.py`

1. **Whitelist enum** (ligne 126) : `SUBSCRIBER_INTENT_ALLOWED = {"loyer-trop-cher", "arnaque-suspecte", "litige-en-cours", "curiosite", "bailleur-conformite", "autre"}`
2. **State extract** (ligne 469) : `compute_subscriber_state` lit `intent_signal` depuis events JSONL `subscribe` type
3. **Endpoint validation** (ligne 1533+) : POST `/api/subscribe` parse + valide `intent_signal` ; valeur invalide → silently coerced empty string (degradation gracieuse, pas 400)
4. **Storage** (ligne 1585) : event `subscribe` JSONL inclut `"intent_signal": intent_signal or None`
5. **Aggregation `/api/stats`** (ligne ~672) : NEW field `subscribers_by_intent` = dict `{intent_key: count}` (filtre exclu `status==unsubscribed`)

## Smoke test

```
POST /api/subscribe {intent_signal:"loyer-trop-cher"} → 200 ok pending
POST /api/subscribe {intent_signal:"INVALID_VALUE"}   → 200 ok pending (intent_signal=null)
GET  /api/stats                                       → subscribers_by_intent={'unset':1, 'loyer-trop-cher':1}
```

2 entrées smoke nettoyées via append unsubscribe events `data/subscribers.jsonl` (event-sourcing préservé). État post-cleanup : `pending=1` (sogibim) / `subscribers_by_intent={'unset':1}`.

## Compliance audit-42 bans 15/15

- ✅ 🚫 NEW FILE : 0 NEW file user-facing (server.py edit only)
- ✅ 🚫 touch home/scan-url/share-card : 0 HTML/JS edit
- ✅ 🚫 monétisation : 0 paywall (champ optionnel non-bloquant)
- ✅ 🚫 Reddit/HN/X/TikTok : N/A
- ✅ 🚫 Telegram : N/A
- ✅ 🚫 ScheduleWakeup : 0 appel
- ✅ 🚫 méta-Q ≤06-05 : N/A (action structurelle Florian-prescrite)
- ✅ 🚫 spawn 7ᵉ : 0 spawn
- ✅ 🚫 SMTP : 2 emails smoke consommés sur quota 20/jour (1 valide + 1 invalide ; rate consommé note)
- ✅ 🚫 IndexNow / Indexing API >1 / patch sub-agents / 2ᵉ auto-PATCH strict global / 6ᵉ city-page Phase 2 : N/A

Note SMTP : 2 emails smoke partis vers `smoke-intent-test+*@bailleurverif.fr` (mailbox interne, probable bounce no-such-user). Compteur jour ≤20 OK. Précédent run-433 : 0 send autre.

## Critère succès

Subscriber #2+ (post-deploy) → intent_signal capté (UI à ajouter ultérieurement sur subscribe form ; brief-only spec server-side ce wake). À 30+ subscribers : `concepts/personas-segments.md` peuplé brief §C.
