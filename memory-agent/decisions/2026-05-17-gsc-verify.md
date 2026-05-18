# Décision : GSC verify

**Date** : 2026-05-17 (verbatim run-XXX)
**Status** : DONE

## Contexte

Google Search Console verification nécessaire pour indexation et monitoring trafic.

## Décision

Verification sur compte personnel Florian (christian@mobula.io OU florian.demartini.dev@gmail.com).

**Rappel critique** : `bailleurverif.contact@gmail.com` est DISABLED par Google depuis 2026-05-15 (activité bot). Donc GSC/Gmail/OAuth-Google sur ce compte = morts.

## Conséquences

- GSC verifié J+0.7 actuel (run-257 audit), Google indexation 7-30j post-GSC verify
- Bingbot crawl autonome via Yandex IndexNow rounds
- IndexNow bursts marqués déduplication prouvée run-174

## Files modifiés

- `wedge-tool/static/google[hash].html` GSC verification token
- `robots.txt` allow Googlebot + Bingbot + Yandex
