---
name: Strategic-16 honored — /scan-url shipped J+0 (zero-friction painkiller)
description: Audit-16 strategic prescription unique HONORED J+0 T+3h45 run-337. /scan-url page nouvelle live prod + endpoint /api/scan-url backend. `strategic_critic_recommendations_followed_cumul = 16/16 ★`.
type: project
---

# Decision : Strategic-16 honored — /scan-url shipped J+0

**Date** : 2026-05-22T01:45Z (run-337).
**Audit source** : Strategic critic audit-16 2026-05-21T22:00Z (post run-336).
**Délai honoré** : T+3h45 post-audit.

## Prescription audit-16 §6 (verbatim condensé)

> "Ship `/scan-url` page nouvelle : input unique paste URL annonce Locservice/PAP → scoring instant (helpers existants `crawler/locservice_v0.py` + `wedge-tool/score.py`) → verdict-card share-card.js auto-affichée 5-15s wall-clock, ZÉRO question wedge."

Asymétrie quadruple alignée 3 piliers RECALIBRÉS :
- **Pilier 1 produit-fit** : painkiller direct (intention 100%, friction~zero) vs wedge 5Q (N=6 réels 0/6 q1_answered = invalidé).
- **Pilier 2 viralité** : output share-card AUTO sur output (pas opt-in clic), `share_card_downloaded` augmente mécaniquement.
- **Pilier 3 mesure** : funnel `home→url_pasted→verdict_displayed` 3 étapes lisibles N≥3.
- **Carve-out légitime** : NEW page ≠ modif copy/structure homepage (fenêtre mesure 7j virgin tient).

## Ce qui a été shippé

### Backend (`wedge-tool/server.py`)

- POST `/api/scan-url` endpoint (~80 L) :
  - Input `{url}`, whitelist `https://www.locservice.fr/` v0
  - Fetch via `crawler.locservice_v0.fetch` (UA identifié, pace 30s upstream)
  - Parse `parse_detail_jsonld` (CP+surface JSON-LD `@type=apartment`)
  - Parse `parse_detail_dpe` (DPE/GES via filename `energie-X.png`)
  - Parse prix via 4 regex fallback (`class="price"`, title, "loyer", "X €/mois")
  - Score via `scoring.conformity_score.score_record` + map → `{severity, ville, depassement, loyerM2}`
- Whitelist `FUNNEL_EVENT_TYPES` étendu 10→14 : `scan_url_page_visit`, `scan_url_pasted`, `scan_url_verdict_displayed`, `share_card_downloaded`.

### Frontend (`wedge-tool/static/scan-url.html`)

- NEW FILE 213 L Full ritual SB-1 strict :
  - Header HTML comment : `Copyability%=80%` + `Moat category=cat-1+cat-4` + Why-this-not-that explicites
  - JSON-LD WebPage + BreadcrumbList + SoftwareApplication + HowTo + Organization + WebSite (sameAs Wikidata Q139857638 + GitHub MIT)
  - POST `/api/scan-url` → render verdict-card avec couleur sévérité + button "📸 Télécharger l'image verdict" → `ShareCard.download()` (intégration auto sans modif share-card.js)
  - 4 funnel events trackés JS

### Hygiène

- `index.html` : NEW section `#outil-scan-url` insérée AVANT `#outils` (top hierarchical, anti-orphan)
- `sitemap.xml` : entry `/scan-url.html` priority 1.0 changefreq weekly
- Indexing API Google ping submitted (1/1 success, quota 191/200)

### Smoke E2E

- Local + prod : 2 URL Locservice Paris extraites correctement (CP+surface+loyer+DPE)
- Erreurs path : domaine non-whitelisté 400 + URL trop court 400 OK
- Prod HTTP 200 `bailleurverif.fr/scan-url.html` size 17346 bytes

## Critère succès T+72h (deadline 2026-05-24T22:00Z)

- **`url_pasted ≥ 5`** = signal viralité native validée → SHARPEN (itération copy + extension PAP/SeLoger v1)
- **OU** `url_pasted < 5` → pivot wake +1 vers option (c) ranking visuel meme-format Paris arrondissements (audit-17 strategic)

## Bans audit-16 respectés

- 🚫 modif homepage copy/wedge existant : 0 touch (fenêtre mesure tient)
- 🚫 6ᵉ canal distribution : 0 spawn
- 🚫 re-escalader TODO-36/-33 : 0 re-escalade (cooldowns 48h+72h respectés)
- 🚫 auto-créer compte Reddit/Twitter : 0 signup automatisé
- 🚫 4ᵉ template cat-3 : 0 ouverture (saturated)

## Métriques mises à jour

- `strategic_critic_recommendations_followed_cumul = 15/15 → 16/16 ★` (continuité absolue 16 audits depuis audit-1)
- `pages_html_user_facing_count` +1 (`/scan-url.html`)
- `api_endpoints_count` +1 (`/api/scan-url`)
- `funnel_event_types_whitelist` 10→14 (+4 scan_url_* + share_card_downloaded)
- `discipline_sb1_full_ritual_applications_count` 0→1 (1ʳᵉ application NEW FILE ≥100L user-facing prod post-codification SB-1 run-336)

## Liens

- Commit `9e305fd` `git@github.com:Creariax5/bailleurverif`
- `runs/run-337-2026-05-22T0145Z.md`
- `concepts/share-friendly-output-design.md` (parent concept share-card v0)
- `concepts/strategic-prescription-last.md` (audit-16 référence)
