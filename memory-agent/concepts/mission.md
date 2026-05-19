# Concept : Mission

**État** : Active depuis 2026-05-19T17:XXZ (RÉORIENTATION Florian verbatim, run-307 ack J+0). Remplace mission "5000 users 90j" 2026-05-16T09:13Z.

## Vraie cible (verbatim Florian 2026-05-19T17:XXZ)

> *"Mon vrai but est de laisser faire l'agent pour que au bout d'un moment ça me fasse du revenu passif. Et pour TODO-25 je pense que c'est pas utile tant que y a pas des vrais users."*

**Reformulation officielle** :

Construire et faire grandir BailleurVérif (ou pivot si nécessaire) pour générer **revenu passif sustainable** :
- Court terme : €100-500/mois @ 6 mois (cible ~2026-11-19)
- Long terme : €500-3000/mois @ 12 mois (cible ~2027-05-19)
- Input Florian **récurrent ≤ 1h/mois** post-setup

**"5000 users 90 jours" = stretch goal motivant, PAS la métrique de succès** (Florian explicite).

Pas de deadline rigide. Optimise compounding long-terme > spikes court-terme.

## Métriques succès (remplacent "5000 users")

1. **`affiliate_revenue_mtd`** — objectif principal (Lovys GLI / Hemea travaux / autres affiliés)
2. **`signups_real_qualified_mtd`** — proxy direct revenu (signups - bots - Florian)
3. **`organic_traffic_30d_compounding_growth`** — foundation acquisition passive (GSC + visits.jsonl growth rate vs precedent 30d)
4. **`florian_hours_consumed_mtd`** — DOIT décroître au fil du temps (North Star autonomie)
5. (post-affiliés) `signups_to_paying_conv_pct`

KPI snapshot à mettre à jour : `memory-agent/kpis/snapshot-current.md` ajouter 4 nouvelles métriques.

## 5 piliers stratégiques (Florian validés)

### Pilier 1 — SHARPEN homepage UN single painkiller use case

**Constat** : produit actuel = vitamine multi-outil conformité. Conversion 0% sur 20-40 humains réels @ 93+ wakes. Pain pas assez sharp pour signup spontané.

**Reco pivot homepage** : *"Loue-je à un loyer légal ? Tape ton adresse."*
- Input : adresse (BAN autocomplete) + loyer actuel + surface m²
- Output 5s : OUI / NON / PROBABLEMENT NON + delta €/mois récupérable + bouton "Générer ma lettre de baisse de loyer" → **signup gate sur génération PDF**
- Reste du site (DPE, dépôt garantie, observatoire) → secondaire dans nav, pas supprimé mais relégué

**Pivot autorisé** si data montre autre painkiller plus prometteur (ex: "DPE F/G : ce bien peut-il être loué légalement?", "Mon dépôt garantie : combien récupérable + lettre type"). Critère : 1 question urgente googlée en panique, réponse 5s, signup gate sur action.

### Pilier 2 — SEO COMPOUNDING via pages programmatiques

**Strategy proven** (Pretto, MeilleurTaux, Effy) : 1 page/ville-arrondissement = 1 porte d'entrée Google. 200 pages = 200 portes.

**Sous-agent futur** : `sub-page-generator` (Haiku ou Sonnet selon qualité) — 5-10 pages/jour. NE PAS SPAWNER tant que pilier 1 homepage painkiller pas validé (sinon 200 pages pointent vers funnel cassé).

Cibles : `/loyer-paris-11.html`, `/loyer-lyon-3.html`, `/dpe-marseille-13e.html`, `/depot-garantie-toulouse.html`. Chaque page = données fraîches (loyer plafond, % violations, exemples annonces) + CTA homepage painkiller.

### Pilier 3 — AFFILIÉS AVANT subscriptions (skip TODO-25 actuel)

Florian explicite : *"TODO-25 pas utile tant que pas de vrais users"*. **Skip Stripe + paywalls + SKUs B2C €5-19/mo** dans leur forme actuelle.

À la place : **affiliés**.
- Lovys (GLI bailleur) — €30-50/lead — https://lovys.fr/partenaires
- Hemea (travaux rénovation) — 5-15% — https://hemea.com/affiliation
- MaPrimeRénov démarcheurs (futur)

**Zero infrastructure** : visiteur clique → partenaire → tu touches passivement. **2 affiliés à signer = 1-2h Florian** (TODO-32 nouveau).

**Trigger subscriptions** : 100+ signups gratuits + signal feature payante demandée par utilisateurs réels → ALORS subscriptions.

### Pilier 4 — VIRAL MECHANIC notation agences publique

Asset existant (`/notation-agence-anonyme.html`) à pousser en pages dédiées : `/notation-agence/foncia/paris`, `/notation-agence/citya/lyon`, etc. Données scrapées + témoignages anonymes vérifiables.

**Mécanique virale FR éprouvée** (Que Choisir / 60M Consommateurs) : naming and shaming = partageable Twitter/Reddit naturellement.

**Risque légal** : sourcer chaque accusation vérifiable + ne pas inventer + droit de réponse activable. Restrictif mais faisable.

**⚠️ BLOCKER DATA DISCOVERED run-310** : CSV observatoire (`wedge-tool/static/data/observatoire-annonces-loyer-*.csv` schema 23 colonnes) n'a **PAS de colonne `agence`/`brand`/`annonceur`/`professional`**. Donc pages dédiées `/notation-agence/<brand>/<ville>.html` data-driven IMPOSSIBLE sans upgrade scraper (ajout extraction nom agence + classification particulier vs pro à chaque listing). **TODO-34 NEW florian-todos.md** : décision Florian (upgrade scraper vs pivot Pilier 4 angle). Workarounds 0-data-upgrade examinés et rejetés run-310 : (a) placeholder page = théâtre + low quality ; (b) hall of shame anonymisé annonces (sans brand) = pas viral car pas namedshaming ; (c) crowdsourcing form témoignages = vide content + 0 utilisateur. Pilier 4 EN PAUSE jusqu'à décision TODO-34.

### Pilier 5 — CONTENU LINKEDIN automatisé

**Florian = 8000 followers LinkedIn perso = canal externe humain N°1 validé** (post 7462136169473126400 = +10 visites/17h P10).

`sub-linkedin-drafter` Sonnet 4.6 interval 24h **déjà spawné run-304** (id `d1a89a62-26ab-4223-8f21-0eae41ca7e97`). Drafte 1 post/jour basé sur signaux frais. Florian valide en 30s + poste à son rythme.

Cycle 1 EARLY tick T+14min run-305 = draft 1184c pending validation TODO-32-bis.

## Seuils opérationnels Pilier 1 (run-309, tactical critic-23 ★★ #3)

Définitions opérationnelles pour arbitrer iter-1 vs pivot painkiller sans drift feel-good :

- **`signup_real_qualified`** = capture email `/api/capture` avec : `severity ∈ {warn, danger}` + `depassement_eur_mois > 100` + IP ≠ Florian (filtre `ip_hash ∉ {Florian-known}` voir traffic-signals.md) + survit 24h sans rétractation explicite inbox/feedback.
- **iter-1 VALIDÉ** = ≥ 3 `signup_real_qualified` sous 7 jours fenêtre glissante depuis run-308 ship (= deadline 2026-05-26T21:30Z). Action si validé : invest auto-gen template lettre LRAR server-side (Pilier 1 iter-2).
- **PIVOT painkiller déclenché** = ≤ 1 `signup_real_qualified` sous 14 jours (= deadline 2026-06-02T21:30Z). Action si pivot : tester DPE F/G interdit ou dépôt garantie comme painkiller alternatif (changer reframe homepage + créer 1 page programmatique équivalente).
- **AMBIGU (2-3 signups sous 14j, ≥3 mais après 7j)** = continuer mesure 7j supplémentaires sans iter-2 invest. Signal painkiller borderline → besoin d'amplification trafic (Pilier 5 LinkedIn) avant verdict définitif.

Source de données : `wedge-tool/data/email-captures.jsonl` + `wedge-tool/data/visits.jsonl` (corrélation `sessionId`).

Budget time Builder mesure : 1 wake/72h à compter run-309 pour spot-check jusqu'à seuil franchi. Pas plus (anti-polish-méta).

## Ce qui devient NON-PRIORITAIRE

- "5000 users 90j" cible chiffrée stricte
- TODO-25 (Stripe + paywalls + SKUs B2C €5-19/mo) — REPORTÉ post-100 signups
- Vanity metrics : `pages_total` brut, IndexNow rounds, JSON-LD coverage 100%, sitemap URLs counted
- Polish FAQPage 3/5 pages restantes (différable sine die)
- 4ᵉ template cat-3 (saturated 3/3 BAN strategic-7)

## Ce qui devient PRIORITAIRE

- Conversion visiteur → signup (sharpen homepage, friction signup réduit)
- Affiliés revenue setup (page comparative + liens trackés post-Florian-action)
- Pages programmatiques compounding SEO (post-pilier 1 validé)
- 1 viral mechanic notation agences
- `sub-linkedin-drafter` qualité (signal Florian post = viralité conditionnelle)

## Asset live actuel (héritage)

- 6 wedge tools (lookup adresse / DPE / loyer encadré / préavis-bail / charges-récup / état-des-lieux)
- Observatoire N=232 annonces non-conformes 17 communes scorées 9 vagues git horodatées
- Dataset data.gouv.fr v1 + reuse `6a0c30a` (DR ≈90 dofollow gov.fr)
- 171 pages HTML prod
- Repo public GitHub MIT (DR 90)
- SMTP `contact@bailleurverif.fr` OVH Zimbra send-capable
- API `/api/recourse/<tag>` cat-3 3 templates saturated 3/3 + 9 ECLI Cass.
- 2 awesome-list PRs ouvertes (`awesomedata/apd-core#410`, `etewiah/awesome-real-estate#28`)

## Update history

- 2026-05-13 : Phase 1 wedge tool conformité bailleur
- 2026-05-16T09:13Z : pivot B2C (target 5000 users, monétisation off)
- 2026-05-16T13:00Z : DIRECTIVE 6 STOP nouveaux tools + light theme refonte
- 2026-05-17T07:18Z : DIRECTIVE 8 AGENT BUILDER re-cadrage
- 2026-05-17T08:05Z : DIRECTIVE 9 moat-builder + anti-blocage
- 2026-05-17T14:00Z : DIRECTIVE 10 strategic thinking
- 2026-05-17T15:00Z : DIRECTIVE 7 RÉVISÉE cron-driven pacing
- 2026-05-17T16:10Z : pivot Voie B locataire-first
- **2026-05-19T17:XXZ : RÉORIENTATION revenu passif** (verbatim Florian, run-307 ack J+0). 5 piliers validés. Skip TODO-25 actuel.
- 2026-05-19T21:30Z : Pilier 1 iter-1 LIVE (run-308 verdict €/mois + reframe lettre baisse loyer).
- 2026-05-19T22:30Z : Pilier 2 proof-of-pattern LIVE `/loyer-legal-paris.html` (run-309 strategic-9 honored) + seuils Pilier 1 explicites L80-91.
- 2026-05-19T23:30Z : Pilier 4 BLOCKER data-missing column `agence` documenté (run-310, TODO-34 NEW dataset upgrade décision Florian).
