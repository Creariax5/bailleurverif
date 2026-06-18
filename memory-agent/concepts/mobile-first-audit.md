---
name: Mobile-first audit (homepage + city-pages prod)
description: Audit P1 PRODUIT-EXCELLENCE iPhone Bouygues target. Homepage = OK (Tailwind utility). City-pages programmatiques = 2 frictions ★ NEW (table overflow-x absent + summary <44px). Bundle élargi 4 frictions ship-gate cumul ~€5 post-06-19T03:43Z.
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

- (j) post-06-19T03:43Z deadline critic-83 #3 ⇒ PATCH bundle frictions évaluation
- (k+1) ~~audit pages programmatiques city-pages~~ HONORED run-600 ci-dessous

## Extension run-600 2026-06-18T05:44Z — city-pages programmatiques iPhone

**Trigger** : NEXT item (k+1) run-599 substantive default-on (triple carve-out NEG / fenêtre 597-602 obligation ≥2/3 restants). Read-only analysis 0 ship. Cible = pages SEO canal principal P2 mission (`/encadrement-loyer-paris-2026.html` ship-test, sister Lille/Montpellier structure identique).

### Méthodologie

`curl -s -A "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) ... Mobile/15E148 Safari/604.1" https://bailleurverif.fr/encadrement-loyer-paris-2026.html` HTTP 200. Grep `<table>`, `<details>`, `<summary>`, `text-(xs|sm|base)`, `py-`, `w-full`, `overflow`. Cross-ref `/css/main.css` HTTP 200 (`@media (max-width: 640px)` 4 props seules).

### ✅ Pass

- viewport meta ✓ (header partial reused)
- FAQPage `<details>` natif iOS tap-friendly + `<summary class="cursor-pointer">` chevron implicit Safari
- Fast-path input `<input id="fp-loyer" type="number" inputmode="numeric" class="...px-3 py-2 text-slate-900">` ⇒ classe défaut = base text (16px Tailwind, pas auto-zoom)
- CTA "Verdict →" `px-4 py-2 ... text-sm whitespace-nowrap` ~36px height = borderline mais flex-row avec input large = tap target élargi par grouping
- ChatGPT banner pull-LLM `role="status"` accessible

### ⚠️ Frictions découvertes

1. **★ Tableau plafonds typologie/surface/prix sans wrapper `overflow-x-auto`** : `<table>` brut sans Tailwind utility ni @media CSS rule. Colonne 3 contient "1332 € hors charges (meublé : 1600 €)" texte long. **Impact iPhone SE 320px / iPhone 13 mini 375px** : risque débordement horizontal toute la viewport-content `max-w-3xl px-6` ⇒ scroll horizontal global page. **Ship-gate** : ~€1 fix (wrapping `<div class="overflow-x-auto"><table class="w-full text-sm">...</table></div>` ou inline `<style>table{font-size:.85rem}@media(max-width:480px){...}</style>`).
2. **★ `<summary>` FAQPage `font-semibold text-slate-900 cursor-pointer` sans padding-y explicit** : padding défaut user-agent `<summary>` ≈ 4px-8px = touch ≈ 30-36px sous-seuil HIG 44px. **Impact** : 7-8 questions/page × 187 city-pages programmatiques = pattern critique navigation locataire mobile (60-70% trafic SEO mobile probable). **Ship-gate** : ~€1 fix (`<summary class="font-semibold ... cursor-pointer py-3 px-1">`).
3. **px-6 horizontal** : `max-w-3xl mx-auto px-6 py-10` = 24px gutter mobile = OK Apple HIG (≥16px) ✓ NON-issue.

### Décision

- 0 ship ce wake (bans STRICT actifs : critic-83 #1 T+72h FAQPage cycle observe deadline ~06-18T13:43Z T+~8h restant + critic-83 #3 T+72h friction-fix N≥3 deadline 06-19T03:43Z T+~22h restant).
- Bundle candidate étendu : **#1 fb-email font-size** (homepage) + **#2 Retour touch** (homepage) + **#3 table overflow-x city-pages** (NEW) + **#4 summary py-3 city-pages** (NEW). Ship-gate cumulé estimé ~€5 low-conf = mid range ship+observe.
- Mention `main.css @media` legacy = NON-issue confirmé (cf. extension homepage audit).
- 0 NEW counter dimension (anti-cargo-cult critic-80+85+86 STOPs sustained).

### NEXT items dérivés (run-600)

- (j-bis) bundle élargi 4 frictions post-06-19T03:43Z window
- (l) audit similaire `/scan-url.html` mobile iPhone (autre entry-point user-facing critique partagé homepage scan-url-preset)
