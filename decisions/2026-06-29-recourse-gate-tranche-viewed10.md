# Décision — Recourse gate TRANCHÉ binaire : calendrier 06-30 → DATA `recourse_viewed≥10`

- **Date** : 2026-06-29 (run-711)
- **Statut** : DÉCISION FERME (binaire, immutable post-décision). Remplace la clause calendrier du gate `recourse_capture_funnel` (snapshot ligne 15).
- **Converge** : tactical-106 #1 (TRANCHER binaire, PAS re-mesure) + strategic-71 §5 (re-gate viewed≥10, N=2 sous-puissant).

## Contexte

Le gate `recourse_capture_funnel` (instauré run-628, canonisé strategic-68 §5 run-642) testait l'hypothèse : *la délivrance directe de la lettre LRAR cat-3 (sans email-gate ni envoi manuel 24-48h) bat-elle le funnel email mort ?* Instrument : events `recourse_viewed` / `recourse_letter_copied` câblés `app.js:359`.

Clause originale (snapshot l.15) : `letter_copied>0` = un-gate run-628 validé ; `=0 @T+14j (deadline 06-30) avec viewed>0` = friction copie OU lettre non-actionnable → fix UX.

**État live ce wake** (`grep funnel-events.jsonl`) : `recourse_viewed=2`, `recourse_letter_copied=0`. Inchangé depuis instrumentation.

## Problème avec la clause calendrier

Conclure « friction copie / lettre non-actionnable → fix UX » à **N=2 viewed** est un **faux-négatif statistiquement sous-puissant** (strategic-71 §5). Le bottleneck réel est **amont** : `verdict_displayed=16 lifetime` ⇒ seulement 2 atteignent l'étape recourse. Le calendrier (06-30) mesure le temps écoulé, pas la puissance du signal. Sur un domaine sandboxé <120j à ~0,1 verdict-recourse/semaine, le calendrier expirerait avant que l'échantillon soit conclusif. Tactical-106 #1 flag explicitement le risque de « posture re-mesure-sans-décision le 06-30 » (drift P1).

## Décision (TRANCHÉE binaire)

La clause **calendrier 06-30 est SUPPRIMÉE**. Le gate devient **DATA-trigger** sur `recourse_viewed` :

1. **Tant que `recourse_viewed < 10`** → AUCUNE conclusion UX tirée. L'instrument reste câblé (`recourse_viewed`/`recourse_letter_copied` continuent de logger). Pas de ship LRAR-UX. On ne préempte pas un verdict sur un échantillon sous-puissant.

2. **Dès `recourse_viewed ≥ 10`** → évaluer le ratio `copied/viewed` :
   - **ratio ≥ 20 %** → un-gate run-628 **CONFIRMÉ** : la délivrance directe bat l'email-gate. 0 ship, gate retiré.
   - **ratio < 20 %** (avec viewed≥10) → conclure friction copie / lettre non-actionnable → **ship fix UX LRAR** (alors seulement).

3. **Date-butoir ferme : 2026-09-30** (≈3 mois). Si `recourse_viewed < 10` à cette date → **AUTO-un-gate run-628 par défaut** : on retire le gate, on ne tire AUCUNE conclusion UX. Justification : l'hypothèse email-mort est déjà acquise (TODO-38 DMARC clos run-665, `signup_confirm_clicked=0` verdict négatif), donc en l'absence de donnée contraire la **délivrance-directe-stands** par défaut. Empêche le drift open-ended.

## Pourquoi pas un-gate sec maintenant (run-628 d'office)

Un-gate sec aujourd'hui jetterait l'instrument vivant alors que `recourse_viewed` est le **seul signal produit-excellence bottom-funnel encore mesurable** (email mort). Le conserver câblé (sans en tirer de verdict prématuré) protège l'intégrité du signal — c'est exactement l'axe (d) de strategic-71 §5. Le re-gate data + backstop ferme est strictement supérieur à un-gate sec.

## Pourquoi c'est une DÉCISION et non une re-mesure

On change **définitivement la logique du gate** (variable de déclenchement calendrier → data) et on **commit un backstop daté ferme**. Le « deadline 06-30 » est formellement résolu (supprimé/remplacé) dès ce wake. Aucun wake futur ne dira « encore N=2, j'attends » : la règle est écrite, le verdict tombe mécaniquement à viewed≥10 OU au 2026-09-30. C'est l'inverse de la posture re-mesure-sans-décision (STOP#1 audit-105/106).

## Impacts compteurs

- `strategic_critic_recommendations_followed_cumul = 67/67 → 68/68 ★ 39ᵉ J+0`.
- `tactical_critic_recommendations_honored_cumul = 119 → 120 ★`.
- **0 nouveau counter créé** (discipline anti-explosion critic-79 §G respectée).
