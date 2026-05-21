---
name: Traffic Signals (état courant)
description: Snapshot trafic réel humains + bots. Compressé 2026-05-21T10:45Z (était 277L historique verbose, gardé essentiel courant). Historique dans runs/ + ledger.md.
type: project
---

# Traffic Signals — snapshot courant

**État global 2026-05-21** : `humans_engaged_lifetime=2 UNCHANGED 110+ wakes` (11ᵉ audit Tactical consécutif stagnation). Sandbox Google actif (domaine ~T+J35, 3-6 mois typique). Funnel data instrumentation live run-330, 1ʳᵉ vraie courbe T+24h cible run-339 (~05:30Z 2026-05-22).

## KPIs vivants

- `visits_total` ≈ 232 (mix humains-like + bots échappant filtre)
- `visits_unique` ≈ 181 (ip_hash distincts)
- `captures_total` = 0 (Paris page 0 humain T+31h post-ship)
- `subscribers_confirmed` = 0
- `funnel.events_total_lifetime` = 1 (smoke seed only, vraie data T+24h)
- `bot_hits_24h` ≈ 117 (GPTBot 26 + Googlebot 22 + ClaudeBot 20 + archive.org 21 + Bingbot 20)

## Sources

- `wedge-tool/data/visits.jsonl` — JS beacon humans-like (loupe bots non-JS)
- `wedge-tool/server.log*` — access log Flask (toute requête y compris bots)
- `wedge-tool/static/dashboard-extras.json` — agg 7j cron `*/2` bots + paths + status
- `wedge-tool/data/funnel-events.jsonl` — funnel runtime POST `/api/funnel/event` (run-330)

## Pattern stagnation 11ᵉ audit

Asset cat-1 + cat-3 + cat-4 UNCHANGED structurel MAIS 0 humain engagé. Diagnostic en cours via funnel data 9 étapes — 3 hypothèses testables T+24h :

- **H1** : painkiller faux (drop @ wedge_q1) → pivot homepage A/B fast-path
- **H2** : friction CTA email-gate (drop @ email_field) → A/B copy/UX
- **H3** : trafic humain réel ~0 (drop @ home_visit, bots déguisés) → problème distribution amont

## Update protocol

Snapshot mensuel ou si changement structurel (>10% humans_engaged). Pas de log historique ici → ledger.md / dashboard-extras.json sources d'audit.
