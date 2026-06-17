---
name: Output share-friendly verdict-card design (Pilier 1 PRIO ABSOLU)
description: Image PNG verdict shareable (1200×630 OG-format) LIVE verdict-card homepage run-334 strategic-15 prescription. Critère succès T+72h share_card_downloaded ≥1 deadline 2026-05-24T13:45Z.
type: project
---

# Concept : Share-friendly output design (verdict-card PNG)

**État** : v0 LIVE verdict-card homepage prod run-334 2026-05-21T13:45Z (strategic-15 prescription HONORED J+0 T+3h45). Carve-out légitime ban anti-touch audit-14 (ajout asset ≠ modif copy). Critère succès T+72h `share_card_downloaded ≥ 1` OU `referrals_from_share ≥ 1` deadline 2026-05-24T13:45Z.

## Pourquoi (alignement mission RECALIBRÉE)

Mission 2026-05-21T07:35Z PRIO ABSOLU explicite : *"Output share-friendly à concevoir (image meme verdict, ranking)"*. Florian verbatim : *"output verdict actuel = texte privé non-shareable"*. Sans image partageable :
- TikTok 30s démo impossible (pas de thumb visuel)
- Reddit data posts manquent screenshot
- Twitter/X threads sans visuel = engagement -70% (étude Twitter)
- Word-of-mouth (user copie-colle verdict texte privé à un ami) = friction max

Avec image PNG verdict :
- 1 clic → download → repost natif Twitter/Instagram/Reddit
- OG-image 1200×630 = preview link unfurl automatique
- Couleur danger/warn/ok = signal viralité émotionnel direct
- Footer attribué `bailleurverif.fr` = traffic compounding

## Architecture v0 (shipped run-333)

### Files

- `wedge-tool/static/share-card.js` (110 L) — API publique `window.ShareCard`
- `wedge-tool/static/share-card-demo.html` (60 L, `noindex,nofollow`) — preview Florian
- Pas de modif `app.js` / `index.html` (anti-touch respect)

### API publique

```js
ShareCard.buildSvg(verdict);     // → string SVG inline (1200×630)
ShareCard.generatePng(verdict);  // → Promise<objectURL PNG>
ShareCard.download(verdict);     // → trigger download direct + trackFunnel("share_card_downloaded")
```

### Input expected (verdict object)

Mêmes champs que `computeVerdict()` app.js retourne :
- `severity` : "danger" | "warn" | "ok"
- `ville` : string
- `depassement` : number (€/mois, 0 si pas violation)
- `loyerM2` : number (€/m², optionnel)

### Output

PNG 1200×630, transparent palette par sévérité :
- `danger` : fond rouge `#7f1d1d` + accent rose `#fca5a5` + emoji 🚨 + label "VIOLATION DÉTECTÉE"
- `warn`   : fond ambre `#78350f` + accent jaune `#fcd34d` + emoji ⚠️ + label "À VÉRIFIER"
- `ok`     : fond vert `#14532d` + accent vert clair `#86efac` + emoji ✅ + label "LOYER CONFORME"

Footer : `bailleurverif.fr` + sous-texte "Vérification gratuite • Sources : INSEE OLAP + DILA + ADEME" + mention observatoire 232+ annonces.

## Anti-patterns évités

- ❌ Server-side rendering (Puppeteer/Playwright) = +€5-10/mois coûts vs 0€ client-side SVG→Canvas
- ❌ Library externe (html2canvas, satori) = bundle +20-30 KB, latency download user
- ❌ Inclure adresse user dans image = leak PII si user share publiquement → anonymisé (juste ville)
- ❌ Brand watermark agressif = baisse repostabilité ; on garde footer discret
- ❌ Texte trop dense = illisible thumbnail TikTok/Twitter ; headline 64px + subline 32px

## Intégration différée (cible run-345+)

### Conditions de ship

Audit-15 strategic critic ~run-345 doit produire décision pivot/sharpen wedge :
- Si **SHARPEN gagne** : ajouter button "📸 Partager" sur `#verdict-card` post-verdict → 1-line `app.js` `ShareCard.download(verdictObject)`
- Si **PIVOT scanner-URL gagne** : intégrer dans nouveau frontend zero-friction → adapter `buildSvg()` pour input scanner (URL → verdict 5s)

### Plan d'intégration sharpen path (5 min Builder)

```js
// app.js dans la fonction qui affiche verdict-card (~line 270)
const shareBtn = document.createElement("button");
shareBtn.textContent = "📸 Partager mon verdict";
shareBtn.className = "share-btn"; // styler CSS terra
shareBtn.onclick = function() {
  ShareCard.download({ severity, ville, depassement, loyerM2 });
};
card.appendChild(shareBtn);

// index.html <head>
<script defer src="/share-card.js"></script>
```

### Funnel event whitelist à ajouter (strategic-14 LIVE)

Ajouter `share_card_downloaded` à la whitelist 10 events `/api/funnel/event` :
- Fichier : `wedge-tool/server.py` (whitelist set)
- Step 10 nouvelle : "share_card_downloaded"
- Permet mesure ratio `share_card_downloaded / verdict_displayed` = signal viralité intrinsèque

## Métriques cibles post-intégration (audit-16+)

| Métrique | Baseline pré-share | Cible J+30 post-ship |
|---|---|---|
| `verdict_displayed / wedge_q5_answered` | inconnu (funnel T+24h pending) | maintenu (sharpen) ou +20% (pivot) |
| **`share_card_downloaded / verdict_displayed`** ★ NEW | 0 (pas de feature) | ≥5% (signal output partageable utilisé) |
| `referer_non_google_30d` | ~0 (silent) | ≥10 visits/30d (preuve share ↔ traffic) |

## Risques connus + mitigations

1. **iOS Safari `canvas.toBlob` partial support** → fallback `canvas.toDataURL("image/png")` à ajouter v1 si Safari users ratio >20%
2. **Emoji rendering Linux Chrome dépend fonts système** → SVG embed `<text>` natif, emojis fallback noir & blanc possible ; cosmétique seulement
3. **~~Foreign object accessibility~~ RÉSOLU run-588 2026-06-17T05:44Z** : `<foreignObject>` ne rend pas via WebKit drawImage→canvas (subline disparaissait du PNG sur iPhone Safari = persona Bouygues target). Fix: remplacement par `<text>` natif + `<tspan>` 2-lignes word-boundary wrap (helper `wrapAt(s, 46)`). Smoke 3/3 PASS (danger/warn/ok). +12L net commit `d066a28`.
4. **Anti-leak PII** : adresse exclue volontairement (juste ville). Tester aucune fuite avant ship homepage.

## Lien avec funnel T+24h décision (strategic-14)

- Si funnel data run-339+ montre `q1<10%` → pivot scanner-URL : `buildSvg()` reste valide, adapter input
- Si q1≥30% → sharpen : ship share button homepage 1-line
- Si q1 10-30% → ambigu : ship share button QUAND MÊME (zero-risk, anti-touch homepage ≠ ajout button non-disruptif), permet test viralité parallèle au sharpen

## Update history

- 2026-05-21T10:00Z run-333 — v0 prototype shipped, design doc créé, intégration différée audit-15
- 2026-05-21T13:45Z run-334 — strategic-15 prescription HONORED J+0 T+3h45. v0 LIVE verdict-card homepage prod (script tag index.html L710 + shareBlock button id `share-verdict-btn` app.js L279-298 + handler addEventListener click → ShareCard.download). Cumul +17 L modifs minimales, 0 modif copy/structure (carve-out audit-14 explicit strategic-15 §6 §1). Critère succès T+72h codifié : `share_card_downloaded ≥ 1` OU `referrals_from_share ≥ 1` deadline 2026-05-24T13:45Z → si 0 audit-16 pivote output (meme/ranking/scorecard).
