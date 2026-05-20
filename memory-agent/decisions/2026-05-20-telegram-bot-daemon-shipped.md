---
name: Telegram bot daemon shipped
description: telegram_bot.py systemd long-polling daemon shipped run-326, brief 13:45Z step 4/4 closed J+1 wake
type: project
---

# Telegram bot daemon shipped — run-326 J+1 wake

**Date** : 2026-05-20T17:30Z
**Brief origine** : Florian 2026-05-20T13:45Z step #3 (4 canaux distribution), différé run-326 par run-325 (budget wake insuffisant, "1-2 wakes" autorisé).

## Ce qui a été shippé

| Composant | Path | Statut |
|---|---|---|
| Daemon Python long-polling stdlib-only | `agent-browser/telegram_bot.py` (218 L) | ✅ shippé |
| Service systemd | `/etc/systemd/system/bailleurverif-telegram-bot.service` | ✅ enabled + active |
| Log dir | `logs/telegram-bot.log` | ✅ append-only |
| Events JSONL | `data/telegram-bot-events.jsonl` (hash chat_id, pas PII) | ✅ initialisé |

## Architecture

- **Stack** : `urllib.request` stdlib only (zéro nouvelle dépendance vs `python-telegram-bot` brief suggéré). PID Main 2750444, RSS ~11 MB stable.
- **Long-polling** : `getUpdates` timeout 30s, backoff exponential 1→60s sur erreur réseau.
- **Handlers** : `/start`, `/help`, `/check <adresse>`, `/observatoire`.
- **Driver trafic** : footer `🔗 bailleurverif.fr` automatique sur toutes réponses + lien `/?q=<addr>` direct vers fiche site.
- **API interne** : appelle `http://127.0.0.1:8102/api/lookup-adresse` + `/api/observatoire-dpe-fg`.
- **Anti-PII** : chat_id hashed SHA256 dans events jsonl (anonymisé conforme self-policy).

## Pourquoi stdlib > python-telegram-bot

1. Zéro nouvelle dépendance (pip install peut fail réseau, lock chain `python-telegram-bot` lourde).
2. Code 218 L lisible, debug facile.
3. Lifecycle systemd simple, pas async lib gymnastics.
4. Telegram Bot API HTTP est trivial (sendMessage, getUpdates) = pas besoin abstractions.

## Test E2E requis (Florian, hors-Builder)

1. Ouvrir `https://t.me/BailleurVerifBot`
2. Taper `/start` → vérifier menu reçu avec footer
3. Taper `/check 10 rue de Rivoli 75004 Paris` → vérifier encadrement Paris + DPE voisinage
4. Taper `/observatoire` → vérifier stats nationales
5. Logger résultat dans `inbox.md` HEAD si bug ou OK

## Implications mission

- **Pilier 5 (LinkedIn + canaux externes)** : Telegram = 5ᵉ canal distribution actif (LinkedIn + Bluesky + HuggingFace + dev.to + Telegram). Telegram est unique car **bidirectionnel** (DM users), pas que push. Forwards naturels dans groupes immo FR = viralité latente.
- **Conversion** : footer `bailleurverif.fr` sur 100% réponses = funnel Telegram → site. Mesurable via `referer` server.log (à vérifier post-1ʳᵉ user).
- **Cost** : zéro (Telegram API gratuit, bot RSS 11 MB sur VPS existant).

## Sub-agents impact

- **Pas un sub-agent** (long-running, pas cron). Pas dans `sub-agents-registry.json`. Compté séparément.
- **6 sub-agents actifs UNCHANGED** : sub-judilibre-enrich (disabled) + sub-seo-monitor + sub-linkedin-drafter + sub-observatoire-publisher v2 +HF + sub-bluesky-poster + sub-content-syndicator.
- **Telegram daemon = 1 long-running service** (systemd, pas cron, pas Builder).

## Brief 13:45Z statut final

- ✅ Step 1 sub-bluesky-poster spawn (run-325)
- ✅ Step 2 sub-observatoire-publisher PATCH +HF (run-325)
- ✅ Step 3 sub-content-syndicator spawn (run-325)
- ✅ Step 4 telegram_bot.py daemon (run-326)

**4/4 J+0/J+1 = brief 13:45Z COMPLETE.**
