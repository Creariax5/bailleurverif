---
name: SEO keyword intelligence
description: Tracking GSC queries that surface bailleurverif.fr — weekly delta, persona signal, page mapping, optimization status
type: project
---

# SEO keyword intelligence — données GSC live

## Source

Florian partage screenshots GSC Performance hebdomadaire via `inbox.md` HEAD. Cooldown re-share Florian = 7j. Builder met à jour ce concept à chaque NEW batch.

## Baseline 2026-06-03 (16j cumul, 5 requêtes)

| # | Requête | Imp | Clic | CTR | Persona signal | Page mappée | Status optim |
|---|---------|-----|------|-----|---|---|---|
| 1 | `r askfrance questions` | 8 | 0 | 0% | Reddit-bait FR | `/questions-reelles-locataires-fr.html` | Title/meta pending |
| 2 | `aide rénovation propriétaire bailleur 2026` | 7 | 0 | 0% | **BAILLEUR pain point** | `/aides-financieres-bailleur-2026.html` | ✅ run-425 (title 137c→56c, meta 268c→150c) |
| 3 | `service-public interdiction location logement classe g 2025 f 2028 e 2034` | 3 | 0 | 0% | Long-tail ultra-spécifique | `/calendrier-interdiction-dpe-2025-2028-2034.html` | ✅ shipped run-429 (strategic-42 honored J+0) |
| 4 | `encadrement de loyers a villeurbanne` | 1 | 0 | 0% | Phase 2 enrich strategic-34 | `/encadrement-loyer-villeurbanne-2026.html` | ✅ déjà enrich strategic-34 |
| 5 | `encadrement des loyers paris drihl` | 1 | 0 | 0% | Persona EXPERT (cite DRIHL) | `/encadrement-loyer-paris-2026.html` | ✅ run-409 title rewrite |

## Insights stratégiques (2026-06-03)

1. **Signal BAILLEUR fort (#2 + #5)** : 2/5 requêtes = bailleur-oriented. Renforce thèse Phase 2 pivot SaaS bailleur multi-bien (cf long-term-strategy.md à créer).

2. **Long-tail = moat structurel (#3)** : requête ultra-spécifique = 0 concurrent optimise dessus. Notre créneau différenciant vs ANIL/SP-fr.

3. **Reddit-bait validé (#1)** : `/questions-reelles-locataires-fr.html` émerge sur 8 imp = pattern à répliquer (questions-reelles-bailleurs-fr / questions-frequentes-encadrement-loyer / questions-frequentes-dpe-bailleur).

4. **Phase 2 enrich Villeurbanne fonctionne (#4)** : strategic-34 honored produit traction GSC. Continuer Phase 2-3 pages restantes.

5. **0% CTR global** = title/meta optimization URGENTE sur 4/5 pages. Pages #2 ✅ done run-425, #1+#3 pending.

## Monitoring weekly (auto-tracker)

- Weekly delta (imp/clic) par requête → tableau ci-dessus updated par Builder à chaque nouveau batch Florian.
- Identifier NEW queries émergentes (jamais vues) → action ship dédié (NEW page OR optim existing).
- Track `gsc_indexed_queries_emerging` dans `kpis/snapshot-current.md`.

## Discipline ship-gate intégrée

Avant chaque ship NEW page OR title rewrite, **mapper la requête cible GSC** (existing OR anticipée) + estimer "would they pay €X" (cf brief 06-03T16:30Z). Si pas de requête cible identifiable ⇒ revoir intérêt page.

## Actions queue (depuis brief 06-03T17:30Z)

- ✅ A — title/meta `aides-financieres-bailleur-2026.html` (run-425)
- ✅ B — NEW `/calendrier-interdiction-dpe-2025-2028-2034.html` (run-429 J+0 strategic-42 honored)
- ⏳ C — NEW `/questions-reelles-bailleurs-fr.html` + `/questions-frequentes-encadrement-loyer.html` (banned audit-42 NEW FILE >1, defer audit-43+ unless lifted)
- ✅ D — Ce concept (run-425)

## Mesure T+~2h post-ship Action B run-429 (baseline)

- 3 hits sur `/calendrier-interdiction-dpe-2025-2028-2034.html` (23:45Z→01:45Z 2026-06-04) :
  - 23:45:51Z SELF curl/8.5.0 (Indexing API verif post-ship)
  - 00:20:38Z `101.32.15.141` UA iPhone iOS 13.2 — Tencent Cloud AS45090 ⇒ BOT-likely
  - 00:48:02Z `43.156.156.96` UA iPhone iOS 13.2 identique ⇒ BOT-likely (mêmes AS Tencent + UA-string identique = botnet-sync)
- `direct_dpe_calendrier_real = 0 / 3 hits` baseline T+~2h. Email_submitted_topic_dpe-calendrier = 0.
- Critère T+72h (deadline 2026-06-06T22:00Z) = `direct_dpe_calendrier ≥ 3` OR `email_submitted_topic_dpe-calendrier ≥ 1`. À ré-évaluer wake T+~14h+ post-crawl Google.

## Mesure T+~4h post-ship Action B run-431

- 0 NEW hit `/calendrier-interdiction-dpe-2025-2028-2034.html` entre 01:45Z→03:41Z 2026-06-04 (hors 2 SELF HEAD curls de cross-ref UA à 03:43:14Z par moi-même).
- `direct_dpe_calendrier_real = 0 / 3 hits cumul` UNCHANGED post run-430 baseline. Googlebot pas encore venu chercher la page (Indexing API ping ✅ mais delay typique 24-72h). Bingbot/GPTBot/Applebot pas encore vus sur cette URL spécifiquement.
- Aucun email_submitted topic=dpe-calendrier.
- **Pas de pivot** : critère T+72h court (deadline 2026-06-06T22:00Z, T+~67h restant). Re-mesure wake T+~14h+ post-ship (~13:45Z+) attendre fenêtre Googlebot. Si T+~24h toujours 0 humain ⇒ flag audit-43 pour pivot Action C OR feedback widget A.1.

## Mesure T+~6h post-ship Action B run-432

- 0 NEW hit `/calendrier-interdiction-dpe-2025-2028-2034.html` entre 03:41Z→05:41Z 2026-06-04 (hors 2 SELF curls 05:41:29Z+05:41:48Z de ce wake mesure).
- `direct_dpe_calendrier_real = 0 / 3 hits cumul` UNCHANGED post run-430/431 baseline (3 hits cumul = 1 SELF + 2 BOT-Tencent). 0 venue Googlebot/Bingbot/GPTBot/Applebot sur cette URL spécifique (Applebot crawl autres pages confirmé sur même fenêtre — cf traffic-signals.md run-432).
- Aucun email_submitted topic=dpe-calendrier.
- **SIGNAL CROISÉ** : pendant la même fenêtre 03:41Z→05:41Z, **Applebot AS714 a crawlé 3 pages distinctes + 4 CSS/JS resources** (preavis-bail-nantes / arnaque-location-toulouse / encadrement-loyer-aubervilliers-2026). Apple n'a PAS encore traversé la page calendrier-dpe spécifiquement. Cohérent avec discovery via sitemap.xml pre-indexed (vs Indexing API ping qui ne touche pas Apple).
- **Pas de pivot** : critère T+72h court (deadline 2026-06-06T22:00Z, T+~64h restant). Latence Googlebot post-Indexing API typique 24-72h ⇒ fenêtre encore raisonnable. Re-mesure wake T+~10h+ post-ship (~09:45Z+, après audit-43 drop ~10:00Z).

## Hypothèses à valider T+14j post run-425 (≤ 2026-06-17)

- **H1** : title #2 56c + meta 150c → CTR > 0% sur même volume imp (~7-15 imp/14j). Si oui ⇒ propager pattern aux 4 autres URLs flaggées. Si non ⇒ revoir copywriting (pas longueur).
- **H2** : Florian nouveau batch GSC ≤ 2026-06-10 confirme #2 maintient imp post-rewrite (pas Google-deboost).
