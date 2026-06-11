---
name: IndexNow ban affined ship-time cap 1 URL (Florian brief 2026-06-11T08:00Z honored J+0)
description: Affinement verdict run-315 "IndexNow théâtre confirmé" → ban global devient cap STRICT 1 URL ship-time NEW page OR PATCH ≥+50L substantive. Symétrie 1:1 Indexing API Google. SB-4 codifié + tool indexnow_ping.py + decision audit trail. Run-521 honored T+~7h45.
type: project
---

# Decision : IndexNow ban affiné ship-time strict cap 1 URL

**Date** : 2026-06-11T15:45Z run-521.

**Source brief** : Florian inbox.md HEAD 2026-06-11T08:00Z (T+~7h45) — "AFFINER BAN INDEXNOW : autoriser 1 URL ship-time NEW page (symétrie Indexing API Google)".

**Contexte trigger** : Bing Webmaster Tools flag HIGH severity sur `encadrement-loyer-paris-2026.html` "not submitted via IndexNow". Verdict Builder run-315 "IndexNow théâtre confirmé" mesurait mauvais signal (0 hit Bingbot T+6h server.log) sur 1 spot-check 1 page 6h fenêtre = statistiquement insignifiant. Bing co-créateur protocole IndexNow + Cloudflare 25M+ sites = data terrain qu'on n'a pas.

## Affinement granulaire (Florian verbatim tableau brief)

| Usage IndexNow | Statut nouveau |
|---|---|
| 🚫 IndexNow ping rounds répétés (re-ping même URL chaque wake) | INTERDIT (théâtre cumulatif confirmé) |
| 🚫 IndexNow batch ≥3 URLs wake hors-ship | INTERDIT (vanity métrique) |
| ✅ IndexNow 1 URL au ship-time NEW page user-facing | AUTORISÉ (symétrie Indexing API Google 1 URL spec) |
| ✅ IndexNow 1 URL au ship-time PATCH substantive ≥+50L FAQ/section utility | AUTORISÉ même règle |

## Asymétrie ROI (Florian arguments verbatim)

1. **Symétrie pattern existant** : Indexing API Google ping ship-time 1 URL strict (audit-52 §11 spec). Asymétrie Bing ≠ Google injustifiée si même contrainte 1 URL strict.
2. **Test run-315 mauvais signal** : mécanisme IndexNow alimente crawl queue priority Bing, pas fetch instantané. Hit peut arriver H+18/36 outside window mesuré.
3. **Coût marginal nul** : 1 ligne `curl POST api.indexnow.org/indexnow` avec clé `b0d2add1441ec161a5ba4ad975987bc8` (active depuis run-XX). 0 secret nouveau, 0 dépense.
4. **ROI asymétrique** : Bing+Yandex+DuckDuckGo+Seznam ~5-7% SERP FR. Marginal mais coût marginal aussi.
5. **Garde-fou anti-théâtre intacte** : ban rounds répétés + batch ≥3 conserve discipline anti-vanity. Binaire 100% ban → cap 1 URL ship-time strict.

## Actions Builder honored run-521

- **(a) Auto-PATCH `concepts/discipline-self-binding.md`** : section SB-4 nouvelle "IndexNow ship-time strict cap 1 URL" insérée avant SB-3 + entrée historique 2026-06-11T15:45Z. Cap PAR CIBLE concept doc (cible distincte vs Builder prompt sem 06-05→06-12 consommé). Additif strict, 0 suppression SB-1/-1.1/-2/-3.
- **(b) Decision file** : ce fichier `2026-06-11-indexnow-ban-affined.md` (audit trail Florian brief honored J+0).
- **(c) Tool creation** : `agent-browser/indexnow_ping.py` 113L Python stdlib (mirror `indexing_api_ping.py` CLI signature). Refuse 0-arg + N≥2 args + URLs hors host + déjà ping ≤lifetime (cap lifetime 1 ping/URL via log `wedge-tool/data/indexnow-pings.jsonl`).
- **(d) USE deferred** : 0 use IndexNow ce wake (audit-57 ban 🚫 IndexNow STRICT actif). SB-4 dormant jusqu'audit-58. Hierarchy Strategic Critic > SB Builder sauf brief Florian explicit override — ici Florian brief = override Strategic-future-bans, MAIS audit-57 bans 19/19 actuels reconduits cette session (carve-out wake-spécifique non-engagé pour use IndexNow).

## Cap par cible (Auto-PATCH discipline HUMAN_DIRECTIVE prompt §2026-06-05)

Cap "1/sem PAR CIBLE additif strict, 0 suppression DIRECTIVE 7/9/10/11/12, backup + decisions/" :
- **Cible Builder prompt** : 1/1 consommé sem 06-05→06-12 (run-448 PATCH 9646→9851 chars). Indisponible jusqu'au 06-12.
- **Cible Strategic Critic prompt** : 0/1 disponible. NON ENGAGÉ ce wake.
- **Cible Tactical Critic prompt** : 0/1 disponible. NON ENGAGÉ ce wake.
- **Cible concepts/discipline-self-binding.md** : 0/1 disponible → **1/1 CONSOMMÉ run-521 SB-4 + entrée historique**. Reset 06-12T00:00Z.
- **Cible sub-agent prompts** : 0/1 disponible chacun. NON ENGAGÉ ce wake.

0 suppression DIRECTIVE noyau confirmée. Backup git auto (commit pre-Edit gardé en ledger commit history). decisions/ file présent = ce fichier.

## Audit-57 bans 19/19 STRICT compatibilité

- 🚫 IndexNow → respecté ce wake (0 use, tool creation = infra non-use)
- 🚫 NEW FILE user-facing site → `indexnow_ping.py` agent-browser/ = infra interne, non-user-facing site ✅
- 🚫 auto-extension carve-out créatif HORS draft 2 wiki → Florian brief explicit override via DIRECTIVE 10 §c-bis Hierarchy 4 règles (Florian > Strategic Critic). Brief verbatim "Builder applique cap PAR CIBLE (Strategic récent = OK, Builder 1/sem disponible si DIRECTIVE 10 §c-bis applicable)". Cible distincte concept-doc ≠ Builder prompt.
- 🚫 méta-Q ≤06-13 → 0 méta-Q émise ce wake ✅
- 🚫 push social → 0 push ✅
- Autres bans (NEW user-facing/touch 8 surfaces/Indexing API ping/spawn/SMTP/sub-agent patch/funnel event/Reddit-HN-X-TikTok/2ᵉ PATCH Builder/3ᵉ Wikipedia draft/publication wiki) → tous respectés ce wake ✅

## Critère succès & échec

**Succès** : SB-4 active immédiatement post-commit run-521. Au prochain ship NEW page user-facing OR PATCH ≥+50L substantive (post audit-57 ban window expiration audit-58+), Builder applique 1 ligne `python3 agent-browser/indexnow_ping.py <url>` post-commit. Log persistant `wedge-tool/data/indexnow-pings.jsonl` audit-trail. Bing+Yandex+DuckDuckGo+Seznam queue priority alimenté.

**Échec rétro-mesurable** : 0 indexation Bing nouvelles pages T+30j post-1ʳᵉ application SB-4 → audit Strategic-N pivot vers ban global réintégré OR investigation cause.

## Cumul compteurs run-521

- `florian_briefs_honored_j0_lifetime` : N→N+1 ★ (brief 08:00Z honored T+~7h45)
- `discipline_self_binding_rules_lifetime` : SB-1/-1.1/-2/-3 light → SB-1/-1.1/-2/-3/-4 light + SB-4 strict
- `strategic_critic_recommendations_followed_cumul` : 57/57 UNCHANGED (audit-57 bans respectés intacts)
- `tactical_critic_recommendations_honored_cumul` : 78 UNCHANGED (audit-73 #1 SMOKE honored = honoré pré-existant)
