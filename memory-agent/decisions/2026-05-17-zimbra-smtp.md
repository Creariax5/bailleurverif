# Décision : SMTP OVH Zimbra `contact@bailleurverif.fr`

**Date** : 2026-05-17T05Z (run-205, post DIRECTIVE 6 trust)
**Status** : DONE + ACTIVE (sending OK, IMAP poll OK)

## Décision

Configurer compte mail pro `contact@bailleurverif.fr` via OVH Zimbra pour outreach presse + asso + List-Unsubscribe RGPD.

## Pourquoi vs Gmail

- `bailleurverif.contact@gmail.com` DISABLED par Google 2026-05-15 (activité bot suspectée)
- OVH Zimbra contrôlé par Florian + agent (SMTP auth `.env`)
- DKIM/SPF/DMARC OK chez OVH
- List-Unsubscribe header pour conformité RGPD

## Config technique

- SMTP : `ssl0.ovh.net:465 SSL`
- IMAP : `ssl0.ovh.net:993 SSL`
- Credentials : `.env` `SMTP_USER` + `SMTP_PASS`
- Send : `agent-browser/smtp_send.py`
- Poll : `agent-browser/imap_poll.py` cron 15-30 min

## Anti-spam strict (DIRECTIVE 8 garde-fou)

- **Max 1 outbound / 30 min** première semaine SMTP
- **Max 20/jour total**
- Ratio aide-d'abord 5/1 minimum
- List-Unsubscribe header obligatoire
- DKIM/SPF/DMARC PASS check avant chaque outbound

## Outbound lifetime (au 2026-05-18T11:29Z)

- 7 lifetime envoyés
- Aujourd'hui : 2 (DAL+FAP outreach asso)
- 4/4 presse 2026-05-17 (Capital/LeMonde/Mediapart/Reporterre)

## Files

- `agent-browser/smtp_send.py` (sendmail wrapper)
- `agent-browser/imap_poll.py` (poll UNSEEN messages)
- `wedge-tool/data/outbound-emails.jsonl` (event-sourcing log)
- `wedge-tool/data/subscribers.jsonl` (event-sourcing signups Phase 2 capture email)
- `wedge-tool/static/api/unsubscribe` endpoint (RGPD droit oubli)

## Cohérence DIRECTIVE 9

PAS de 3ᵉ outreach SMTP même jour (cooldown 30min + max 20/j). Spam massif (>200/j sans warmup) **interdit par garde-fou légal dur**.
