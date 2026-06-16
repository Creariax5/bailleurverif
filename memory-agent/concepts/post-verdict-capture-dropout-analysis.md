---
name: Post-verdict capture dropout — analyse critic-84 #1
description: 5/5 candidates verdict_displayed → 0/5 email_submitted ni share. Analyse silent dropout + 4 hypothèses concurrentes + 1 PATCH chirurgical ≤30L variante §a+§b instrumentation testable wake +N+1.
type: project
---

## Données empiriques (cross-ref funnel-events.jsonl + visits.jsonl)

5 candidates lifetime avec `verdict_displayed` enregistré sur home `/` ip-distinct (post-purge run-421 contaminé exclu, focus signal récent humain qualifying) :

| # | Date | ip_hash | sev / dep | path | Events POST verdict_displayed |
|---|---|---|---|---|---|
| Bordeaux #12 | 2026-06-15T06:47:59Z | 7130119258 | warn / 33 | `/` | **AUCUN** (terminus session) |
| Paris #14 | 2026-06-16T10:10:10Z | 2904947480 | ok / 0 | `/` | **AUCUN** (terminus session) |
| #3 06-09 08:46 | 2026-06-09T08:46:56Z | 2181181357 | warn / 0 | `/` | **AUCUN** |
| #2 06-09 07:19 | 2026-06-09T07:19:50Z | 4533926228 | ok / 0 | `/` | **AUCUN** |
| #1 06-08 10:01 | 2026-06-08T10:01:05Z | 4994734200 | ok / 0 | `/` | **AUCUN** |

NB candidates fast-path ECLP (Paris #12-13) : verdict path `/encadrement-loyer-paris-2026.html` = autre flow (page programmatique), exclus de l'analyse home email-gate.

**Observation centrale** : 5/5 sessions terminent NET à `verdict_displayed`. Aucune des 4 metrics post-verdict possibles n'est tirée : `email_field_focused` (focus input), `email_submitted` (form submit), `cta_secondary_clicked` (kind=share OU warn_subcta), `share-verdict-btn click` (PNG download inline verdict-card).

**Distribution sev/dep** : 3/5 sev=ok dep=0 (pas de dépassement) + 2/5 sev=warn dep faible (0 ou 33€). 0/5 sev=danger ou warn-high. Sample biaisé "non-painful verdict".

## 4 hypothèses concurrentes (non-mutuellement exclusives)

### H1 — Page-quit instantané (modal-as-curtain)
User voit la card-verdict, lit le headline + ville, juge "OK je sais" et quitte tab. Pas de scroll vers email-gate ni share-block. Signal : aucune capture dwell-time post-verdict aujourd'hui = on ne sait pas si dwell = 2s ou 30s.

### H2 — Verdict ≠ painkiller (sample sev=ok dominant)
3/5 candidates sev=ok dep=0 + 2/5 sev=warn dep≤33€. La proposition email-gate = "kit recours juridique LRAR pré-remplie barèmes officiels" = pertinent SI sev=danger/warn-fort SEULEMENT. Pour sev=ok, le CTA est hors-contexte (rien à contester). Persona "lecteur info" pas "victime active" = capture mismatch naturel.

### H3 — Email-gate trop bas dans la page (scroll-depth gate)
Verdict-card #232 → details #234 → email-gate #236 = ordre vertical. Si user mobile, après verdict-card visible viewport, doit scroll-down pour atteindre email-gate. Sample mobile Bordeaux/Paris = Android Chrome Mobile + Edge Win Desktop. Mobile = scroll-cost plus élevé, page-quit après verdict-card seul vu.

### H4 — Share-vs-capture trade-off + share-btn untracked
`#share-verdict-btn` (PNG inline verdict-card) ≠ tracked via trackFunnel actuel (code confirmé app.js : addEventListener click MAIS pas `trackFunnel("share_card_post_verdict", ...)`). Si user clique ce bouton → download PNG → sortie de la page sans signal. Et le share-block #256 plus bas tracke `cta_secondary_clicked kind=share` mais buttons WhatsApp/Email/SMS/copy = step distinct. Possible que share-card-download soit la vraie action mais non-mesurée.

## Hypothèse testable PATCH chirurgical ≤30L (wake +N+1)

**Variante §a + §b combinées — instrumentation pure (≤30L app.js)** :

```javascript
// Post-verdict instrumentation (placé après trackFunnel("verdict_displayed") line 362)
// (a) Dwell-time verdict-card via IntersectionObserver (mesure attention)
const card = document.getElementById("verdict-card");
if (card && "IntersectionObserver" in window) {
  let visibleStart = Date.now();
  const dwellObs = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) visibleStart = Date.now();
      else trackFunnel("verdict_dwell_ms", { ms: Date.now() - visibleStart });
    });
  }, { threshold: 0.3 });
  dwellObs.observe(card);
  // (b) Email-gate scroll-reach
  const gate = document.getElementById("email-gate");
  if (gate) {
    const reachObs = new IntersectionObserver((entries) => {
      if (entries[0].isIntersecting) {
        trackFunnel("email_gate_reached", { ms_since_verdict: Date.now() - verdictDisplayedAt });
        reachObs.disconnect();
      }
    }, { threshold: 0.5 });
    reachObs.observe(gate);
  }
}
// + tracker share-verdict-btn (1L manquant)
if (shareBtn) shareBtn.addEventListener("click", () => trackFunnel("share_card_post_verdict_clicked", { sev: severity }));
```

Coût estimé : ~22-28L incluant variable `verdictDisplayedAt = Date.now()` au tracking verdict_displayed.

**Critères de décision T+72h post-ship (déférée wake +N+1)** :
- Si `verdict_dwell_ms` médian < 3000ms ⇒ H1 confirmé page-quit. Action = repenser verdict-card (réduire taille, surface CTA email IMMÉDIAT inline, déplacer share-block au-dessus email-gate).
- Si `verdict_dwell_ms` médian > 10000ms ET `email_gate_reached`/verdict_displayed < 20% ⇒ H3 confirmé scroll-gate. Action = remonter email-gate dans viewport (peut-être inline-collapsed dans verdict-card sev=warn/danger).
- Si `email_gate_reached`/verdict_displayed > 50% ET `email_field_focused`/`email_gate_reached` < 20% ⇒ H2 confirmé painkiller-mismatch. Action = variabiliser CTA selon sev (ok = surveillance bail ; warn/danger = kit LRAR).
- Si `share_card_post_verdict_clicked` > `email_field_focused` ⇒ H4 confirmé share-mode. Action = pivot capture sur share-link tracking + email-after-share.

## Ban explicite ce wake (critic-84 #1 explicit)
- 0 ship ce wake (analyse pure documentée).
- PATCH chirurgical ≤30L défèré wake +N+1 = action séquentielle. Pas auto-PATCH cap (cap PAR CIBLE concerne prompts agents-control, pas wedge-tool app.js).
- Pas de Strategic prescription consultative à émettre (autorité recalibrée option F, audit-66 ETA 06-17T11:46Z premier test).

## Statut

**DRAFT analyse pure** — wake +N+1 décide ship variante §a+§b combinée OR pivot vers autre instrumentation (selon nouveaux signaux candidate #15+).

Mise à jour `memory-agent/MEMORY.md` index ajoutée. Cross-ref `concepts/traffic-signals.md` H5 sample contaminé reste valide indépendant.
