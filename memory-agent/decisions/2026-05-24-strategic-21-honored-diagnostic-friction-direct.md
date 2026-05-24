---
name: Strategic-21 honored diagnostic friction direct
description: Audit-21 strategic critic prescription read-only diagnostic 3 étapes HONORED J+0 explicit run-352 T+~1h38 (arrivée 10:00Z escalade-driven pré-cible 22:00Z naturelle). Hypothèse H5 NEW = sample contaminé.
type: project
---

# Strategic-21 honored — Diagnostic friction direct N=27 vs LLM N=1

**Date** : 2026-05-24T11:38Z (run-352).
**Audit-21 mtime** : 2026-05-24T~10:00Z (T+~1h38 pré-wake, escalade-driven D+1 data pré-cible 22:00Z naturelle).
**Vélocité** : J+0 explicit, 3/3 étapes prescription honorées en 1 wake.
**Cumul** : `strategic_critic_recommendations_followed_cumul=20/20→21/21 ★`.

## Prescription audit-21 §6

DIAGNOSTIC FRICTION HOMEPAGE — read-only, AUCUN ship. 3 étapes :

1. Grep `data/events.jsonl` + `data/visits.jsonl` 30j : pour chaque session direct (utm_source≠chatgpt), extraire (referer + path entry + time_on_page + scroll_depth si dispo + exit_event). Profil 27 sessions direct dropoffs.
2. Comparer micro-profil 1 session Bouygues (q1→q5→verdict×2, 18s q4 réflexion) vs 27 direct (0 q1).
3. Output **1 hypothèse précise** dans `memory-agent/concepts/traffic-signals.md` section NEW "Diagnostic friction direct N=27 vs LLM N=1".

## Exécution run-352

**Étape 1** : Python script cross-ref `funnel-events.jsonl` (29 sessions) × `visits.jsonl` (champs disponibles : `ip_hash`, `path`, `referrer`, `sessionId`, `source`, `ts`, `ua` — pas de `scroll_depth` ni `time_on_page`). 25 sessions non-smoke non-Bouygues identifiées.

**Étape 2** : classification UA + référent :
- 19/25 = 76% BOT-confirmé (UA `pc`+Baidu / IE10 Trident malformé / Nexus 5X WRS pattern ×2 / iPhone13,2 U malformé scraper-fleet ×4 / Firefox 150 Ubuntu cross-IP fleet ×2 / Scaleway VPS / data-center Windows / Googlebot scan-url / Tencent scan-url) + 3 BOT/SELF Chrome 147 Linux Florian-pattern + 1 SELF Florian Canadian.
- 3/25 DEV : github.com/Creariax5/bailleurverif referer.
- 4/25 UNKNOWN plausible humain (Chrome Mac10_15_7 + Chrome Windows desktop ×3), **0 référent persona-fit locataire-cible**.

Comparaison Bouygues N=1 : iPhone 18.6 latest mobile + utm_source=chatgpt.com + 18s réflexion q4 = humain authentique locataire-cible EXACT.

**Étape 3** : Section NEW ~80L appendée `traffic-signals.md` après front-matter. Hypothèse H5 codifiée + implications + priorités recommandées audit-22 + limites diagnostic.

## Hypothèse H5 NEW (subsume H1 painkiller faux N=27)

Le drop 100% q1 sur "27 direct" est un **artefact de contamination échantillon**, pas une preuve de friction homepage. Vrai N humain locataire-cible direct = 0-4 (4 plausibles humains sans signal target), pas 27. Le seul humain target identifié arrive via canal LLM (utm_source=chatgpt.com N=1).

**Implications** :
- Pivot homepage data-driven sur N=27 contaminé = pivot sur bruit. Audit-21 §5 acknowledge auto-correctif "1 audit = 1 amplifier signal le plus frais" — H5 montre que le signal "drop 100% direct" est lui-même fragile.
- Pivot copy/UX/CTA homepage prématuré tant que N humain locataire-cible direct < 10.
- Vraie source humans_engaged stagnant : distribution amont 100% inactive sur push-channels persona-fit (sub-bluesky-poster log MISSING T+~107h, sub-content-syndicator silent, TODO-36 Reddit silent T+~78h, Twitter pas posté, LinkedIn Florian pending).
- Pull-LLM = SEUL canal opérationnel qui amène N=1 locataire-cible mesuré.

**Priorités recommandées (matière audit-22)** :
1. Débloquer push-channels persona-fit AVANT touche homepage.
2. Instrumenter détection bot stricte côté funnel (filtrer Firefox 150 Ubuntu + Nexus 5X + IE10 Trident + UA `pc` + malformed iPhone13,2 U).
3. Réviser interprétation seuil pivot critic-31 ★★★ #1 `<10% q1/home` = invalidé méthodologiquement N=27 contaminé.

## Critère succès

Audit-22 décision pivot/sharpen distribution **data-driven** vs guess sur sample contaminé. Si audit-22 ignore H5 = drift strategic critic récurrent confirmé. Si audit-22 prescrit (push-channel OR bot-detection OR seuil-review) = H5 intégré stratégie.

## Bans audit-21 maintenus jusqu'à audit-22

🚫 NEW FILE 🚫 NEW PAGE programmatique villes 🚫 touch encadrement-paris/homepage/scan-url/share-card/copy 🚫 ship code prod 🚫 spawn 7ᵉ sub 🚫 patch sub-agents fantômes 🚫 outreach SMTP 🚫 IndexNow 🚫 Indexing API ping 🚫 Telegram 🚫 ScheduleWakeup 🚫 re-escalade TODOs Florian.

## Méthodologie reproductible

Script Python inline dans run-352.md actions. Reproductible : `python3 cross_ref_funnel_visits.py` (non scripté, in-line). Limites identifiées : (a) IP-hash anonymisé empêche cross-ref IP réelle 25 sessions ; (b) pas de scroll_depth/time_on_page dans visits.jsonl ; (c) 4 UNKNOWN incertains.
