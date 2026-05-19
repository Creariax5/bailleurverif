# Décision — Spawn `sub-seo-monitor` (Haiku 4.5, interval 24h)

**Date** : 2026-05-19T13:29Z (run-299)
**Type** : decisions (immutable post-décision)

## Contexte

- Brief Florian inbox TOP 2026-05-19T13:30Z : monitoring GEO/SEO automatique post Tier 1+2 (4 leviers SEO additifs en cours d'exécution).
- Cas d'usage explicitement listé dans `concepts/sub-agents-active.md` "Use-cases prescrits" (originellement #4 `sub-observatoire-publisher`, ici nouveau use-case dédié SEO monitor).
- Override discipline incremental « 1 sous-agent 2-3 cycles avant les 4 autres » sur cas explicite Florian (cycle 1 `sub-judilibre-enrich` outcome=ok run-298 = signal validé).

## Décision

Spawn 2ᵉ sous-agent J+0 du brief :

- **ID** : `d47a1a87-b317-488c-a449-c7326567f341`
- **Model** : `claude-haiku-4-5-20251001`
- **Schedule** : interval 86400s (24h)
- **Prompt** : 3301 chars, hash sha256[:16]=`58b9deeb9ec9201f`
- **Backup payload** : `agent-browser/prompts-backup/sub-seo-monitor-create-2026-05-19T1330Z.json`
- **Prompt source versioned** : `agent-browser/sub_seo_monitor_prompt.md`
- **Logs** : `data/sub-agents/seo-monitor.jsonl` + `data/sub-agents/seo-monitor-{ISO}.json` (output structuré complet).

## Fonctions

1. PageSpeed Insights API 6 pages clés (homepage + 4 observatoires + `/api/recourse`) mobile, capture perf/seo/accessibility/LCP/CLS/INP.
2. Crawler structurel sitemap (sample 30 URLs si full crawl >5 min) : title 30-60, meta 50-160, 1 H1, canonical match, JSON-LD valid, internal links ≥3, img alt.
3. LLM-bot extraction test : `curl -A "GPTBot"` vs `curl -A "Mozilla"` 3 pages, body length delta, cloaking flag si >20%.
4. Diff vs cycle précédent : régressions perf score / seo score / issues count.
5. Synthèse JSON dans `data/sub-agents/seo-monitor-{ISO}.json`.
6. Alert conditionnelle `inbox.md` HEAD : régression OU worst_score<70 OU cloaking détecté → append. Sinon silent.
7. Git commit (pas push).

## Garde-fous

- HARD BANS : pas de modif `.env`/`*.html`/`agent-browser/*.py`, pas de push, pas d'API agents-control, pas de spawn, pas Claude API, pas ScheduleWakeup.
- Exception §6 contrôlée : `inbox.md` HEAD append uniquement si conditions alert.
- Time-box 8 min dur.
- Drift_avoided log + EXIT si sitemap inaccessible ou PageSpeed 5xx répété.

## Économie

- Coût estimé ≈ $0.05/cycle × 30 cycles/mois ≈ **$1.50/mois** (≈ €1.40).
- Total sous-agents post-spawn : `sub-judilibre-enrich` ($0.05×24×30 ≈ $36/mois) + `sub-seo-monitor` ($1.50/mois) ≈ $37.50/mois ≈ €35. Sous hard limit €20/mois si on adjuste interval `sub-judilibre-enrich` (à observer cycles 2-3).
- **Note budget** : si `sub-judilibre-enrich` continue 1h interval ad libitum, on dépasse €20/mois. Builder doit envisager PATCH interval 3h ou 6h après cycle 2-3 saturation déclarée (cat-3 templates jurisprudence_refs saturent ~3 refs × 3 templates = 9 max, donc agent self-exit "saturated_3" rapidement).

## Asymétrie vs alternative

- Builder Opus 1×/jour ce monitoring = $0.50/cycle × 30 = $15/mois (Opus) vs $1.50/mois Haiku = **10× moins cher**.
- Audit déterministe + parsing JSON = Haiku 4.5 largement suffisant.
- Délégation propre : Builder lit seulement alertes inbox HEAD + ledger snapshot, pas le bruit raw.
- 2ᵉ démo Levier 2 (sub-agents) confirme pattern qui scale.

## Conditions d'arrêt sous-agent

- Outcome=error 2× consécutifs → Builder PATCH `enabled=0` + log incident.
- Brief Florian explicite STOP → DELETE + archive log.
- Budget €20/mois total sous-agents dépassé → Builder PATCH interval upward sur l'agent le plus coûteux.

## WHY THIS NOT THAT

- (a) NOT-THAT polish-méta consécutif = run-298 critic-20 ★★ #1 (cat-4 saturé 50%) → spawn opérationnel = pivot moat substantif (cat-1 visibilité via SEO maintained, cat-4 backlinks via crawler regression detection).
- (b) NOT-THAT Builder gère monitoring lui-même = anti-pattern brief Florian explicite délégation Haiku, et coût 10×.
- (c) NOT-THAT spawn 5 sous-agents d'un coup = anti-instruction Florian discipline incremental + budget €20/mois.
- (d) NOT-THAT attendre cycle 2 `sub-judilibre-enrich` avant spawn = anti-brief Florian "spawn 2ᵉ sub-agent priorité #1 démo Levier 2" + cycle 1 outcome=ok déjà observé run-298 = validation suffisante.

## Suivi attendu

- **Cycle 1 ~T+24h (2026-05-20T13:29Z)** : check `data/sub-agents/seo-monitor.jsonl` HEAD 1 ligne + `seo-monitor-{ISO}.json` baseline scores Lighthouse. Pas d'alert inbox attendue (1ʳᵉ run = pas de "yesterday" pour diff).
- **Cycle 2 ~T+48h** : 1ʳᵉ diff vs hier. Si Tier 1+2 SEO leviers shippés entre temps → on attend Δ positif perf/seo scores.
- Builder ne touche PAS HTML prod sur cette feedback loop (sub-agent recommande mais Builder décide).
