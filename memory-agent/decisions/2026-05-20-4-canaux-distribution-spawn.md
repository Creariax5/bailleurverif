# 4 canaux distribution débloqués + 2 spawns + 1 PATCH

**Date** : 2026-05-20T14:32Z  
**Run** : run-325  
**Trigger** : Brief Florian 2026-05-20T13:45Z (inbox.md HEAD)

## Contexte

Florian a runné agent navigateur browser-bridge ce wake (~13:30-13:45Z) pour setup API credentials de 4 plateformes additionnelles. Brief explicit : spawn 3 sous-agents + ship 1 daemon Python, capacité validée (cap 8, marge 4 disponible). Coût total compute ajouté estimé ≤ €4/mois.

| Palier | Statut Florian | Action Builder J+0 |
|---|---|---|
| 1 Bluesky | ✅ compte créé | ✅ spawn `sub-bluesky-poster` |
| 2 HuggingFace | ✅ token write | ✅ PATCH `sub-observatoire-publisher` (+step HF) |
| 3 Telegram | ✅ bot créé | ⏸ defer `telegram_bot.py` daemon run-326 (brief 1-2 wakes OK) |
| 4a dev.to | ✅ API key | ✅ spawn `sub-content-syndicator` |
| 4b Hashnode | ❌ SKIP (Pro-only) | n/a |
| 4c Medium | ⚠️ pas API | n/a (manuel Florian uniquement) |

## Décisions atomiques

### A. Spawn `sub-bluesky-poster` (Haiku 4.5, 24h)
- **ID** : `1a6b2a20-fe71-417c-adc7-7a561985366b`
- **Prompt** : 2838 chars, hash `2eeaad01ce700c06`
- **Backup** : `agent-browser/prompts-backup/sub-bluesky-poster-create-2026-05-20T1430Z.json`
- **Coût** : ≈€0.60/mois (€0.02 × 30 cycles)
- **Justification** : Priorité #1 explicite brief, script `bluesky_post_atproto.py` déjà shippé run-274 (AT Protocol via env BLUESKY_HANDLE/BLUESKY_APP_PASSWORD), pas de code prod nouveau à ship.
- **1ʳᵉ tick attendu** : ~2026-05-21T14:30Z

### B. PATCH `sub-observatoire-publisher` v2 (HF dataset)
- **ID** : `576fb185-9c51-4ca9-9453-ac9088a223ac` (existant)
- **Prompt** : 6396→8634 chars (+2238), hash `8ecbb525d87e22c5`→`6e432483f1eca7f8`
- **Backup** : `agent-browser/prompts-backup/sub-observatoire-publisher-patch-hf-2026-05-20T1432Z.json`
- **Changements** :
  - Step 1 : env load étendu `+HF_TOKEN +HF_USERNAME` (fail-soft si absent)
  - Step 6.5 NEW : (a) check dataset existe HEAD 200/404, (b) one-shot create si 404, (c) upload CSV cycle via multipart
  - Step 7 log schema étendu : `datagouv_outcome` + `hf_outcome` + `hf_url` + `hf_error` séparés
  - Discipline HF : fail soft (n'affecte jamais data.gouv.fr primary), cap 1 upload/cycle, pas modif metadata global
- **Justification** : Asymétrie totale — 1 PATCH ≤50 lignes prompt = 2ᵉ destination dataset perpétuelle pendant 12+ mois sans charge Builder. HuggingFace audience tech ML/data globale + dataset hub = backlink DR ≈ 80.
- **1ʳᵉ tick avec HF** : ~2026-05-27T06:31Z (cycle 2 du sub-agent)

### C. Spawn `sub-content-syndicator` (Sonnet 4.6, 7j)
- **ID** : `cc0f6fb3-c226-4574-a74c-a35355621c47`
- **Prompt** : 3948 chars, hash `451e6b896b2b93dd`
- **Backup** : `agent-browser/prompts-backup/sub-content-syndicator-create-2026-05-20T1431Z.json`
- **Coût** : ≈€0.60/mois (€0.15 × 4 cycles)
- **Justification** : Audience dev.to = devs tech opendata immo (alignée pilier SEO compounding + LinkedIn). Sonnet 4.6 vs Haiku : 800-1500 mots qualité narrative (1ère personne agent, hook + story + code snippet + takeaway), Haiku produirait flat copy. Skip Hashnode (Pro-only paid 2025+) + Medium (no API publication).
- **1ʳᵉ tick attendu** : ~2026-05-27T14:31Z

### D. ⏸ Défer `telegram_bot.py` daemon (run-326)
- **Brief explicit** : "Time-box ship 1-2 wakes Builder Opus (script + service + test)" — autorise différer.
- **Pourquoi pas ce wake** : Script Python long-polling + systemd service unit + venv install python-telegram-bot lib + sudo systemctl enable + test E2E DM `@BailleurVerifBot` = trop pour 10 min Builder budget actuelle wake (déjà 2 spawn + 1 PATCH + registry + memory consumés).
- **Prochain wake action** : Ship script + service + test.

## Architecture cumul post run-325

**6 sous-agents actifs** (cap 8, marge 2) :

| Sous-agent | Model | Interval | Coût/mois | Canal |
|---|---|---|---|---|
| sub-judilibre-enrich | Haiku | (disabled saturated_3) | €0 | n/a — moat cat-3 complete |
| sub-seo-monitor | Haiku | 24h | ≈€1.50 | monitoring SEO/GEO |
| sub-linkedin-drafter | Sonnet | 24h | ≈€2.50 | Distribution canal #1 (LinkedIn) |
| sub-observatoire-publisher v2 | Haiku | 7j | ≈€0.12 | Distribution canal #2 (data.gouv.fr) + **#3 HuggingFace NEW** |
| sub-bluesky-poster | Haiku | 24h | ≈€0.60 | **Distribution canal #4 (Bluesky) NEW** |
| sub-content-syndicator | Sonnet | 7j | ≈€0.60 | **Distribution canal #5 (dev.to) NEW** |

**Total compute additionnel** : ≈€1.20/mois (€0.60 Bluesky + €0.60 dev.to), HF inclus dans observatoire-publisher gratuit (prompt patch). **Bien sous budget €20/mois sub-agents** + bien sous estimation brief Florian ≤€4/mois.

**5 canaux distribution actifs perpétuels post-Telegram ship** (target run-326) :
1. ✅ LinkedIn (Florian poste + sub-linkedin-drafter Sonnet drafts)
2. ✅ Bluesky (sub-bluesky-poster Haiku) — NEW
3. ✅ HuggingFace dataset (sub-observatoire-publisher v2) — NEW (cycle 2)
4. ⏸ Telegram daemon — TODO run-326
5. ✅ dev.to (sub-content-syndicator Sonnet) — NEW

## Asymétrie revenu passif

1 wake Builder Opus (~€0.20) = 5 canaux distribution autonomes pour 12+ mois sans charge récurrente Florian/Builder.

Test E2E obligatoire : 1ʳᵉ tick chaque sous-agent vérifié vs heartbeat dans wakes suivants (24h Bluesky, 7j observatoire/content-syndicator).

## Fenêtres ouvertes préservées (BANS rappel)

- ✅ Paris page mesure 7j (deadline 2026-05-26T22:30Z) — pas A/B touch
- ✅ ANIL silence check 2026-05-22T05:35Z
- ✅ Que Choisir cooldown 2026-05-23T04:30Z
- ✅ Homepage post-sharpen run-322 mesure 7j — pas touch

## Smoke tests

- `python3 -c "import json; d=json.load(open('agent-browser/sub-agents-registry.json')); print(len(d['agents']))"` → 6
- `curl -X HEAD https://api.bsky.app/` (Bluesky reachable) → 200/405
- `cat .env | grep -c "^HF_\|^BLUESKY_\|^DEVTO_\|^TELEGRAM_"` → 8
- POST/PATCH agents-control = HTTP 201/200 confirmés (responses logged backups)
