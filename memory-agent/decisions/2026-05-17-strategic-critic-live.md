# Décision : Strategic Critic live (DIRECTIVE 10)

**Date** : 2026-05-17T14:00Z (verbatim Florian 08:10Z validation)
**Status** : ACTIVE (jusqu'à 5 audits consécutifs prescription suivie + `moat_components_live ≥ 3`)

## Décision

3 mécanismes obligatoires :
1. **Strategic Critic sub-agent** invoqué toutes les **16 wakes**
2. **Ritual "Why this not that"** obligatoire avant CHAQUE feature
3. **Test "Demain disparition"** à chaque audit (tactical + strategic)

## Pourquoi

Combler le déficit "agent excelle à exécuter, peine à stratégiser". Tactical critic flag drift exécution. Strategic critic audit **moat + defensibility**.

## Strategic Critic sub-agent

- Cron : 86400s (24h) côté agents-control (ID `85c78e3b-6e4b-4bd5-84cf-5a675d1131b7`)
- Output : `inbox-from-strategic-critic.md` (append en tête)
- 6 questions standard : copyability / moat components live / concurrent gap / demain disparition / strategic drift / **prescription unique**
- Ignore vanity KPIs (pages_total, IndexNow rounds, sitemap urls)

## Ritual "Why this not that"

Avant écrire 1 ligne de code à valeur produit, agent écrit dans `runs/run-N.md` section `## WHY_THIS_NOT_THAT` :
- Feature considered
- Alternative 1 (autre feature) + pourquoi pas choisi
- Alternative 2 (1 wake moat-builder) + pourquoi pas choisi OU pourquoi choisi alternative non-moat
- Decision rationale
- Copyability check (%)
- Moat category if applicable (1/2/3/4/N/A)

## Test "Demain disparition"

À chaque audit, répond : *"Si bailleurverif.fr disparaît demain matin, qu'est-ce qui ne se reconstruit pas en 1 weekend par concurrent motivé ?"*

Si "rien substantiel" → flag rouge audit + pivot wake suivant moat-builder.
Si ≥1 composant → mentionner + estimer fragilité (heures-days-weeks-months).

## KPIs

- `wakes_since_last_strategic_critic` (cible ≤ 16)
- `why_this_not_that_rituals_completed_lifetime` (cible ≥ 1 par run substantif)
- `why_this_not_that_rituals_omitted_lifetime` (cible 0)
- `demain_disparition_test_passed` (cible true ≥ 50% audits)
- `strategic_critic_recommendations_followed_pct` (cible ≥ 80%)

## État

- `wakes_since_last_strategic_critic` : 6 selon state.md run-257 / mais raw count 18 selon tactical critic 13 = à clarifier
- 1 strategic critic audit pas suivi (prescription "poster /notation-agence sur 1 canal humain" non-exécutée — bloqueur self-policy)
- `strategic_critic_recommendations_followed_pct` ≈ 50% (1/2 audits suivis)
