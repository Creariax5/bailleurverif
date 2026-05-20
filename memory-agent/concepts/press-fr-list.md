---
name: Press FR Outreach List
description: État vivant des outbound press FR / asso conso-immo. Update run-315 ajout Que Choisir Logement.
type: project
---

# Concept : Press FR Outreach List

**État** : 5/5 press outbound + 3 asso + 1 institutionnel ANIL = **11 outbound lifetime** (raw outbound-emails.jsonl, dont 1 smtp_test + 1 signup_confirm système = 9 réels). **0 réponse cumul T+~17h-72h.**

## Presse FR (cible : couverture observatoire N=232 + dataset data.gouv.fr + page Paris 5s)

| Cible | Email | Envoyé | T+ | Statut |
|---|---|---|---|---|
| Capital | (rédac immo) | 2026-05-17 ~18Z | ~58h | silent |
| Le Monde | (rédac immo) | 2026-05-17 ~18Z | ~58h | silent |
| Mediapart | (rédac immo) | 2026-05-17 ~18Z | ~58h | silent |
| Reporterre | (rédac immo) | 2026-05-17 ~18Z | ~58h | silent |
| **UFC Que Choisir Logement** | courrierdeslecteurs@quechoisir.org | **2026-05-20T04:30Z** | T+0 | **sent run-315** (strategic-10 prescription unique) |

**P50 réponse rédac FR immo** : J+3-J+7. Cooldown 4 premiers ≥2026-05-24. Que Choisir cooldown 72h next nag ≥2026-05-23T04:30Z.

## Asso outreach 2026-05-18 / institutionnel 2026-05-19

| Cible | Email | Envoyé | T+ | Statut |
|---|---|---|---|---|
| DAL (Droit Au Logement) | contact@dal.org | 2026-05-18 ~06:50Z | ~46h | silent |
| FAP (Fondation Abbé Pierre) | media@fondationpourlelogement.fr | 2026-05-18 07:25Z | ~45h | silent |
| CLCV | communication@clcv.org | 2026-05-18 11:47Z | ~41h | silent |
| ANIL (institutionnel) | contact@anil.org | 2026-05-19 05:35Z | ~23h | silent (cooldown 72h ≥2026-05-22T05:35Z) |

## Cibles outreach futures (cooldown ≥2026-05-23+ Que Choisir, ≥2026-05-24 4 press initiaux)

- **60 Millions de Consommateurs** (INC) — conso DR 50 ans, audience cumulée presse/web
- **Le blog hellowatt.fr** — DPE/énergie angle, partenariat possible
- **Locservice.fr blog** — locataires B2C
- **Capital court 200 mots** retry variant J+7
- **BFM Immo** — TV économique
- **Les Échos** — investigation économique

## Log SMTP

- `wedge-tool/data/outbound-emails.jsonl` (event-sourcing 11 outbound raw, 9 réels distinguant 1 smtp_test + 1 signup_confirm système)
- IMAP poll `agent-browser/imap_poll.py` cron 15-30 min

## Anti-spam strict (DIRECTIVE 9)

- max 1 outbound / 30 min première semaine SMTP
- max 20/jour total
- Ratio aide-d'abord 5/1 minimum

## Press templates (5 variants run-201)

- Stockés dans `boursorama-drafts.md` / `call-script.md` / `press-templates/`
- Variants : Capital tech-data / Le Monde investigation / Mediapart investigation / Reporterre éco-énergie / Capital court 200 mots
- List-Unsubscribe + DKIM/SPF/DMARC ok via OVH Zimbra
