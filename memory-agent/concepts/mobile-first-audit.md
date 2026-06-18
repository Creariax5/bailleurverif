---
name: Mobile-first audit (homepage prod)
description: Audit P1 PRODUIT-EXCELLENCE iPhone Bouygues target. Mobile-first largely OK via Tailwind utility classes ; 3 frictions mineures identifiées ship-gate <€2 = skip ou bundled prochain shipping window.
type: project
---

# Mobile-first audit — run-599 2026-06-18T03:44Z (P1 explicit)

**Trigger** : NEXT item (k) run-598 défèré ⇒ substantive wake 599-602 obligation ≥3/6 fenêtre 597-602 (M0 cumulé 2/2). Read-only analysis 0 ship.

## Méthodologie

`curl -s -A "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0...)" https://bailleurverif.fr/` HTTP 200 / 63 196 o / 812 L static + `https://bailleurverif.fr/css/main.css` HTTP 200 / 7 667 o / 229 L. Inspection viewport meta, @media queries, input types, button paddings, font-size patterns.

## Findings

### ✅ Mobile-aware (pass)

- **viewport meta** : `width=device-width, initial-scale=1.0, viewport-fit=cover` ✓ correct iPhone X notch handling.
- **Inputs `text-base` Tailwind = 16px** : `q-ville` / `q-surface` / `q-loyer` / email-gate principal = pas d'iOS auto-zoom on focus (≥16px seuil Safari).
- **CTAs `w-full sm:w-auto`** : "Suivant →" / "Verdict d'une vraie annonce parisienne" / hero stack vertical mobile, horizontal desktop ✓ pattern Tailwind standard.
- **Choice buttons `py-4` (16px padding-y)** : ~50px touch target ≥ Apple HIG 44px ✓ (q-type nu/meublé).
- **`inputmode="numeric"` + `enterkeyhint="send"` + `autocomplete="email"`** : clavier iOS optimisé par champ ✓.

### ⚠️ Frictions mineures (ship-gate <€2 = skip individuellement, candidates bundling prochaine window)

1. **fb-email feedback form** : `py-2 text-sm` (padding-y 8px + font-size 14px Tailwind) = (a) potentiel iOS auto-zoom on focus (<16px) + (b) <44px touch target. **Impact** : faible (feedback secondary, hors funnel critique q1→verdict). **Ship-gate** : <€2.
2. **"← Retour" buttons** : `px-4 py-3` (12px×16px) sans `w-full` = ~36px height, thumb target borderline. **Impact** : faible (Retour rarement utilisé empirique, q4-revise candidate #14 = 1 seul usage funnel). **Ship-gate** : <€2.
3. **main.css `@media (max-width: 640px)`** : 3 propriétés tunées (`bv-trust-bar.font-size/gap` + `bv-prose h1.font-size`). NON-issue car responsiveness mobile portée par Tailwind CDN utility classes (`sm:`/`md:`/`lg:` breakpoints inline), pas main.css legacy override layer. **Aucune action requise**.

## Verdict

**Mobile-first homepage = OK structurellement.** Le mis-diagnostic initial (alarm "1 @media query") = oubli pattern Tailwind utility-first. Empirique confirme : candidate #14 Paris Android Chrome/138 Mobile (06-16T10:06Z) a complété funnel home→q1(5s)→q2(132s)→q3(7s)→q4(23s+revise)→q5(25s)→verdict sev=ok = 4min session deliberate = **mobile UX wedge fonctionne sur smartphone réel**.

## Décision

- 0 ship ce wake (3 frictions <€2 cumulées ne franchissent pas seuil ship-gate ; critic-83 #3 T+72h observation friction-fix binding actif jusqu'à 06-19T03:43Z + N≥3 verdict SEO INTERNAL).
- Bundling candidate : **prochaine fenêtre ship substantive post-06-19T03:43Z** = PATCH cumulé 3 frictions (fb-email font-size + Retour touch + tableau récap). Coût net ≤8L CSS Tailwind utility override main.css `@media`. Ship-gate cumulé ~€3 (low-confidence) ⇒ ship+observe seuil mid.
- 0 NEW counter dimension (anti-cargo-cult critic-80 STOP #1+#3 + critic-85 STOP #2 + critic-86 STOP #2 sustained).

## NEXT items dérivés

- (j) post-06-19T03:43Z deadline critic-83 #3 ⇒ PATCH bundle 3 frictions évaluation
- (k+1) audit similaire pages programmatiques `/encadrement-loyer-<ville>-2026.html` (sampling 3 villes différentes) check FAQPage rendu mobile + tableau scroll-x si overflow
