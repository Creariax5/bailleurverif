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
| 3 | `service-public interdiction location logement classe g 2025 f 2028 e 2034` | 3 | 0 | 0% | Long-tail ultra-spécifique | À créer : `/calendrier-interdiction-dpe-2025-2028-2034.html` | PENDING (brief 17:30Z Action B) |
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
- ⏳ B — NEW `/calendrier-interdiction-dpe-2025-2028-2034.html` (long-tail #3, brief Action B)
- ⏳ C — NEW `/questions-reelles-bailleurs-fr.html` + `/questions-frequentes-encadrement-loyer.html` (brief Action C)
- ✅ D — Ce concept (run-425)

## Hypothèses à valider T+14j post run-425 (≤ 2026-06-17)

- **H1** : title #2 56c + meta 150c → CTR > 0% sur même volume imp (~7-15 imp/14j). Si oui ⇒ propager pattern aux 4 autres URLs flaggées. Si non ⇒ revoir copywriting (pas longueur).
- **H2** : Florian nouveau batch GSC ≤ 2026-06-10 confirme #2 maintient imp post-rewrite (pas Google-deboost).
