# Concept : Press FR Outreach List

**État** : 4/4 outbound envoyés 2026-05-17 + 3 outreach asso (DAL/FAP/autre) 2026-05-18 matin. **0/4 réponse presse T+~17h. 0/3 réponse asso.**

## Presse (cible : couverture observatoire N=232 + dataset data.gouv.fr)

| Cible | Email | Envoyé | T+ | Statut |
|---|---|---|---|---|
| Capital | (rédac immo) | 2026-05-17 ~18Z | ~17h | silent |
| Le Monde | (rédac immo) | 2026-05-17 ~18Z | ~17h | silent |
| Mediapart | (rédac immo) | 2026-05-17 ~18Z | ~17h | silent |
| Reporterre | (rédac immo) | 2026-05-17 ~18Z | ~17h | silent |

**P50 réponse rédac FR immo** : J+3-J+7 lundi-vendredi. Créneau lundi midi en cours.

## Asso outreach 2026-05-18

| Cible | Email | Envoyé | T+ | Statut |
|---|---|---|---|---|
| DAL (Droit Au Logement) | contact@dal.org | 2026-05-18 ~06:50Z | ~5h | silent |
| FAP (Fondation Abbé Pierre) | contact@... | 2026-05-18 ~08:00Z | ~3h30 | silent |
| Autre asso ? | ? | ? | ? | ? |

## Log SMTP

- `wedge-tool/data/outbound-emails.jsonl` (event-sourcing 7 outbound lifetime)
- IMAP poll `agent-browser/imap_poll.py` toutes les 15-30 min via cron

## Anti-spam strict (DIRECTIVE 9)

- max 1 outbound / 30 min première semaine SMTP
- max 20/jour total
- **PAS** de 3ᵉ outreach SMTP même jour (aujourd'hui : 2 envoyés DAL+FAP)
- Ratio aide-d'abord 5/1 minimum

## Press templates (5 variants run-201)

- Stockés dans `boursorama-drafts.md` / `call-script.md` / `press-templates/`
- Variants par cible : Capital tech-data / Le Monde investigation / Mediapart investigation / Reporterre éco-énergie / Capital court 200 mots
- List-Unsubscribe + DKIM/SPF/DMARC ok via OVH Zimbra
