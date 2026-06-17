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

### Statut deadline 2026-06-17T01:44Z (run-586)

- **H1 + H2 = INCONCLUSIVE-NO-BATCH** : 0 NEW batch GSC partagé par Florian depuis baseline 2026-06-03T17:30Z (T+~14j cumul, cooldown 7j attendu ≥ 2026-06-10 MISS T+~7j). Aucune mesure CTR / imp delta possible sans data fresh. Hypothèses ni validées ni réfutées.
- **Cause empirique** : Florian-silent post-fallback continu T+~40h+ depuis brief 06-15T09:15Z option (e) recalibrage Strategic ; SB-5 active = N/A re-flag inbox HEAD (anti-récidive).
- **Conséquence ship-gate** : Action C (NEW pages questions-bailleurs + questions-encadrement) reste defer — `/questions-reelles-bailleurs-fr.html` shipped run-435 strategic-43 J+0 mais sans validation propagation pattern H1 sur 4 autres URLs flaggées avant GSC batch fresh.
- **Action passive** : continuer ship-gate Mission §1.1 sur next ship, attendre batch Florian naturel (PAS request HEAD inbox, SB-5 anti-récidive récursive applicable analogue à PAT BLOCKER). Re-check status à chaque NEW batch share.

## Audit internal-linking depth + FAQPage gap pattern N=5 (run-587 03:43Z micro-action P2 substantive)

**Contexte** : pattern N=5 city-page→home INTERNAL formalisé moat cat-4 #5 run-577 (Montreuil 06-05 + Saint-Denis 06-08 + Bordeaux 06-15 + Paris 06-16 verdict + Montpellier 06-15 abandoned q2). Mission P2 tactique HAUTE explicit "≥2 hubs + ≥3 connexes" internal-linking depth + "FAQPage JSON-LD 8+ Q/R DILA-verified".

**Findings empirique 7 pages crossref** (5 candidates pattern + Lille+Villeurbanne backstop comparaison) :

| Page | Hubs | Connexes-city | FAQPage JSON-LD | Status pattern |
|---|---|---|---|---|
| Paris-2026 | 9 | 7 | ✅ (run-568) | Candidate #14 verdict 06-16 |
| Bordeaux-2026 | 8 | 6 | ✅ (antérieur) | Candidate #12 verdict 06-15 |
| Lille-2026 | 8 | 6 | ✅ (run-571) | Backstop comparaison |
| Montpellier-2026 | 8 | 6 | ✅ (run-573) | Candidate #13 abandon q2 06-15 |
| Villeurbanne-2026 | 9 | 7 | ✅ (strategic-34 antérieur) | Backstop comparaison |
| **Montreuil-2026** | 7 | 6 | ❌ | **Candidate #1 06-05 (1ᵉʳ pattern)** |
| **Saint-Denis-2026** | 7 | 6 | ❌ | **Candidate #2 06-08 (2ᵉ pattern)** |

**Findings** : (1) internal-linking depth SUSTAINED 7/7 satisfaction mission tactique HAUTE (hubs 7-9 ≥2 ✅ ; connexes-city 6-7 ≥3 ✅) ; (2) **gap FAQPage Montreuil + Saint-Denis** = 2 PREMIERS candidats du pattern N=5 SANS FAQPage JSON-LD vs 5/7 autres ✅ ; (3) audit dedup risk run-488 documenté ces 2 villes en tier **boilerplate strict** = dédup-risk MAX cumul ⇒ ajout FAQPage = différenciation prioritaire double-justifiée (signal empirique pattern + tier dedup).

**Action queued post-observation T+72h cycle 1** : ETA ≥ 06-18T13:43Z+ (Paris+Lille+Montpellier observation deadline run-577 critic-83 #1 binding). SI cycle 1 valide signal compounding ⇒ ship Montreuil + Saint-Denis FAQPage 8 Q/R DILA (Seine-Saint-Denis arrêté préfectoral + Cass. ECLI judilibre-verified SB-2 strict). SI cycle 1 invalide ⇒ pivot UX hypothesis vs FAQPage replication (anti-cargo-cult).

**Ban active** : critic-83 #1 STRICT "STOP chain-shipping FAQPage SANS 4ᵉ ship Lyon/Marseille avant mesure effet" → applicable Montreuil + Saint-Denis same logic (4ᵉ + 5ᵉ ship FAQPage = chain-shipping pre-observation). 0 ship ce wake. 0 NEW counter (critic-81 STOP #3 sustained). Action passive : ledger run-587 + concept snapshot statique.

## Audit dedup risk city pages programmatic (run-488 wake-8 substantive)

**Contexte** : critic-67 STOP #3 codifié auto-limit wake-8 = basculement substantive research-only non-banni. Wake-8 trigger atteint (M0 cycle 3 wake-7→8). Mission 06-01 binding : *"chaque ville-page = data unique (chiffres locaux observatoire, FAQs locales, arrêté préfectoral exact, jurisprudence locale). Sinon Google déduplique → 1-2 indexées sur 50."*

**Méthode** : `wc -l encadrement-loyer-*-2026.html` sur les 33 pages city + `diff` 2-à-2 sur 4 villes (Montreuil/Saint-Denis/Aubervilliers/Pantin).

**Findings empiriques** :

| Tier | Lignes | N | Villes | Dedup risk |
|---|---|---|---|---|
| **Boilerplate strict** | 255L exactes | **21** | Aubervilliers, Bagnolet, Bobigny, Bondy, Epinay-sur-Seine, Hellemmes, Ile-Saint-Denis, La-Courneuve, Le-Pre-Saint-Gervais, Les-Lilas, Lomme, Montpellier, **Montreuil**, Noisy-le-Sec, Pantin, Pierrefitte-sur-Seine, Romainville, **Saint-Denis**, Saint-Ouen, Stains, Villetaneuse | **MAX (probable Google dedup ≥80%)** |
| **Light diff** | 260-262L | 5 | Lille, Eybens, Fontaine, Grenoble, Saint-Martin-d-Heres | MOYEN |
| **Différencié substantif** | 306-383L | 7 | Paris, Marseille, Echirolles, Villeurbanne, Bordeaux, Lyon, France (hub) | FAIBLE |

**Diff Montreuil ↔ Saint-Denis (255L vs 255L)** : 12 chunks de diff isolant uniquement (a) city name (b) prix €/m² nu+meublé (c) date "1er X 2021" (d) ancres `?q=City`. Aucune FAQ locale, aucune référence arrêté préfectoral numéro, aucune jurisprudence locale, aucune donnée observatoire ville-spécifique. Texte ELAN boilerplate identique 90%+.

**Cohérence avec GSC live (5 requêtes 16j)** : seule Villeurbanne (330L, enrich strategic-34) est dans les requêtes captées. Aucune des 21 boilerplate-255L n'apparaît en GSC ⇒ **dedup déjà actif Google probable**.

**Conséquence Mission Pilier 2 SEO compounding** : objectif 50+ pages indexées @ M3 INATTEIGNABLE en l'état si 21/33 city pages sont dedup-éligibles. Cible binding mission = data unique par ville (FAQs locales DILA-grounded / arrêté préfectoral numéro+date / jurisprudence locale Cass. + ECLI / chiffres observatoire ville-spécifique).

**Lien candidate humans #4+#5** : reach via Montreuil + Saint-Denis (les 2 boilerplate-255L) ⇒ si signal réel (post-caveat self-test ≥50%), Google sert encore les pages mais dedup peut frapper anytime. Si self-test, no real signal SEO city programmatic actuellement.

**Actions queue NEXT cycle (bans-lift dependent — PAS ship ce wake)** :
- C1 : enrich 4 plus prioritaires des 21 boilerplate (Saint-Denis / Montreuil / Aubervilliers / Pantin = cluster 93 où humans #4+#5 sont arrivés) à pattern Villeurbanne (FAQ locale + arrêté préfectoral + observatoire local).
- C2 : audit Bondy/Romainville/Bagnolet (les plus boilerplate-pur, dedup imminent).
- C3 : critère ship-gate `€X` par ville = "would they (locataire 93) pay €X" si verdict + LRAR pré-rempli local-specific.

**Discipline** : ship-gate Mission §1.1 + bans 20/20 audit-51 strict ⇒ pas de ship ce wake. Documenté pour exploitation post-lift (Florian-validate ou audit-52 06-10T22Z carve-out).

**Reference** : `decisions/2026-05-19-strategic-9-loyer-legal-paris-shipped.md` (1ʳᵉ proof-of-pattern Paris différencié) + `concepts/competitive-positioning.md` (city-page data unique = différenciateur vs ANIL/SP-fr).
