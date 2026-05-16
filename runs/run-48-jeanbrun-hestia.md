# Run-48 — 2026-05-14T23:50Z — DIRECTIVE 4 angles 1+5 cumulés : Jeanbrun + Hestia audit

## TL;DR

- **Découverte ★★★** : Dispositif Jeanbrun = vraie loi française en vigueur (LoF 2026 publiée 2026-02-21, jusqu'au 2028-12-31). Amortissement 12k€/an, location nue résidence principale 9 ans, loyer + ressources encadrés. Toute la filière promoteur en parle.
- **Audit Hestia** : 9 EPCI couverts, B2C bailleur, modèle hybride contenu + SaaS gratuit empilé (simulateur + bail + diagnostics + quittances + EDL). Pays Basque manque chez nous.
- **3 implications produit** : (a) article #5 monté ★★★ Phase 2, (b) wedge V1 Q6 Jeanbrun OU mini-wedge #2, (c) Phase 2 architecturale empiler 2-3 outils gratuits.
- **Gap content** : nos articles citent "LoF 2025 art. 84" sans nommer Jeanbrun → vérification Legifrance différée.
- **POST-001** : T+234min = 0/0/0 (11e mesure stable, audience hashtag minuscule, profil corrigé n'a pas (encore ?) débloqué)
- **Wedge** : 11/4/1/0/0/0/0 inchangé 15e wake consécutif. Pas de signal trafic externe.

---

## Contexte

Wake 23:45Z, T+234min après POST-001. Lecture obligatoire OK (HUMAN_DIRECTIVE/state/tasks/ledger/bugs/inbox/florian-todos). DIRECTIVE 4 active (mode recherche active). Healthcheck via `agent-browser/healthcheck.py --human` = all_ok=true. Aucun nouveau message Florian (dernier 21:05Z DIRECTIVE 4). 7 TODO Florian OPEN inchangés.

Run-47 NEXT proposait 3 options :
- (a) refactor mastodon_api.py DRY (angle 4)
- (b) WebSearch "dispositif Jeanbrun 2026" (angle 1)
- (c) WebFetch Hestia (angle 5)

**Décision** : combiner (b) + (c) en parallèle. ROI immédiat plus haut que (a) sans signal d'utilité. Coût ~5s pour 2 actions, 100% réversible.

---

## Actions

### 1. WebSearch "dispositif Jeanbrun 2026"

10 sources analysées (Vinci Immobilier, Bouygues Immobilier, Cogedim, Lamotte, Defiscalisation.immo, Afedim, Adnova, Koliving, Valority, locationloijeanbrun.fr) = toute la filière promoteur immobilier fait du content marketing dessus.

**Synthèse** :
- Vraie loi (LoF 2026), promulguée 2026-02-21, application jusqu'au 2028-12-31
- Remplace Pinel : amortissement fiscal du bien (jusqu'à 12 000 €/an déductible des revenus fonciers) vs réduction d'impôt Pinel
- Éligibilité : location **nue**, résidence principale, **9 ans minimum**, loyer encadré, ressources locataire encadrés
- **Pas de zonage géographique** (contrairement à Pinel)
- Objectif gouvernement : 50k logements supplémentaires dès 2026, 400k/an d'ici 2030

**Implications BailleurVérif** :
1. **Article #5 monté ★★★** (était ★★) : "Dispositif Jeanbrun 2026 — Statut du bailleur privé" devient priorité absolue Phase 2. Recherche active confirmée par toute filière promoteur.
2. **Opportunité produit** : (a) wedge V1 Q6 mini-flux 3Q éligibilité, ou (b) mini-wedge #2 dédié. Décision différée à signal trafic wedge #1.
3. **Gap content existant** : nos articles citent "nouveau statut du bailleur privé (loi finances 2025 article 84)" sans nommer Jeanbrun (LoF 2026). Possible confusion. Vérification Legifrance différée.
4. **Cross-impact angle B Conformité** : Jeanbrun impose loyer + ressources encadrés → renforce notre angle "vérification conformité". Pas seulement DPE+encadrement classique.
5. **Différenciation possible** : promoteurs ont biais pro-investissement-neuf (vendre programmes). BailleurVérif peut prendre angle **neutre** ("Que vous achetiez du neuf ou déteniez de l'ancien, voici comment...").

### 2. WebFetch hestia.software/encadrement-loyer/

**Architecture** :
- Hub avec intro + simulateur + 5 régions
- 9 EPCI couverts : Paris, Plaine Commune, Est Ensemble, Lyon/Villeurbanne, Grenoble, Lille, Bordeaux, **Pays Basque**, Montpellier
- Une **page dédiée par territoire** (`/encadrement-loyer/{ville}`)
- 2 CTAs primaires : "Vérifier mon loyer" + "Créer un bail gratuit"

**Modèle économique** :
- B2C bailleur particulier confirmé (pas B2B agence)
- Modèle hybride : contenu informatif + SaaS gratuit empilé (simulateur + bail + diagnostics + quittances + EDL numérique)
- Monétisation probable premium (GLI / LMNP), à investiguer

**Implications BailleurVérif** :
1. **Gap périmètre** : Pays Basque (Bayonne+Biarritz) absent de notre wedge (31 communes / 8 EPCI). Volume probable faible mais trou visible. Action différée : ajouter si barème officiel trouvable.
2. **Différenciation produit confirmée** : Hestia mélange conformité + gestion locative. Notre angle "conformité-as-a-Service indépendant" reste différencié.
3. **Funnel acquisition** : Hestia capture en amont via SEO encadrement → up-sell SaaS gestion. Notre funnel théoriquement similaire mais sans SaaS livré. Implication : si TODO-9 NDD + TODO-4 email pro débloqués, on rattrape.
4. **Verrou compétitif Hestia** : empilement 5+ outils gratuits = écosystème. Notre wedge mono-outil ne peut matcher. **Direction Phase 2** : empiler 2-3 outils gratuits cohérents (bail simple + calculateur Jeanbrun + simulateur foncier) plutôt que mono-wedge + landing. Pivot architecturale à acter après go/no-go Phase 1.

### 3. Grep articles existants

`grep -ri 'Jeanbrun|bailleur privé|statut bailleur' content/` → 2 fichiers matchent :
- `obligations-bailleur-particulier-2026.md` : cite "loi de finances 2025 article 84" + "nouveau statut du bailleur privé". Pas de mention "Jeanbrun".
- `content/README.md` : liste article #5 todo = "nouveau-statut-bailleur-prive-2026" (cible déjà nommée correctement).

Mot "Jeanbrun" jamais utilisé. **Gap content confirmé**.

### 4. Mise à jour fichiers

- `research-notes.md` : append entrée run-48 ~110 lignes (2 findings + 5+4 implications + 6 actions différées + 4 sources).
- `concurrents.md` : update bloc Hestia (9 EPCI + 2 CTAs + SaaS empilé) + section "Lecture stratégique" enrichie + 1 action cochée + 4 nouvelles.
- `tasks.md` : 3 tasks cochées (audit Hestia, WebSearch Jeanbrun, run-48). Article #5 README.md monté ★★★. 4 nouvelles tasks (vérif Legifrance, outline article #5, audit page dédiée Hestia, Pays Basque).
- `state.md` : header run-48 + run-47 archivé.
- `ledger.md` : 17 entrées run-48.
- `inbox.md` : message Agent→Florian (signal Jeanbrun stratégique, sans bloquer).

---

## Findings méta

- **Pattern signal faible** : Le signal Jeanbrun aurait été manqué si run-47 s'était limité à constater "concurrents proptech identifiés". Discipline DIRECTIVE 4 = creuser tout signal anormal/inconnu, pas seulement le top 3. À retenir : noter TOUS les ranks 8-10 anormaux dans futures baselines.
- **Pattern double-angle** : Cumuler 2 angles à coût ~5s (WebSearch + WebFetch parallèles) plutôt que 1 angle profond. Tradeoff acceptable quand les 2 ont ROIs indépendants et complémentaires (Jeanbrun = produit, Hestia = stratégie).
- **Audit pré-construction** : Auditer le concurrent direct AVANT de construire Phase 2 architecturale évite de construire à l'aveugle. Hestia nous dit où sont les verrous (empilement outils).

---

## Métriques

| Métrique | Avant run-48 | Après run-48 | Cible |
|---|---|---|---|
| wakes_post_publish_T_minutes | 219 | 234 | — |
| wakes_avec_milestone_recherche_active | 7 | **8** | ≥1/wake |
| wakes_sans_budget_bb_consomme_consecutifs | 9 | **10** | discipline |
| angle_1_explored | 1 | **2** | cycler |
| angle_5_explored | 1 | **2** | cycler |
| jeanbrun_signal_resolved | false | **true** ✅ | — |
| hestia_audit_completed | false | **true** ✅ | — |
| article5_priority | ★★ | **★★★** | Phase 2 |
| content_gap_identified | 0 | **1** (Jeanbrun) | — |
| wedge_geographic_gap_identified | 0 | **1** (Pays Basque) | — |
| visits_unique | 4 | 4 | 100 (go/no-go) |
| results_total | 1 | 1 | — |
| captures_total | 0 | 0 | ≥20 (go) |
| mastodon_post001_engagement | 0/0/0 (10e) | 0/0/0 (11e) | >0 |
| florian_todos_open | 7 | 7 | — |

---

## Next

**Run-49 reco** (priorité ordre) :
1. **1 WebFetch Legifrance "dispositif Jeanbrun loi 2026"** pour identifier source primaire (N° loi + article + texte exact). Éliminer ambiguïté LoF 2025 art. 84 vs LoF 2026 Jeanbrun. Coût ~10s.
2. **1 WebFetch `hestia.software/encadrement-loyer/plaine-commune`** pour audit page dédiée vs hub (structure, JSON-LD, profondeur, CTAs).
3. **Outline article #5 Jeanbrun** (~30 min, peut attendre run-50 si autre signal).

**POST-002** : J+1 ≥06h52 UTC = 2026-05-15 08h52 Paris (~7h restants). Draft prêt `drafts/POST-002.txt`.
**Test GEO J+7** : 2026-05-21. Pré-requis 4/4 articles 3/3 livré run-46.
**Audit J+1 wedge** : 2026-05-15.

**Signal Florian rédigé** dans `inbox.md` (non bloquant) : Jeanbrun = découverte stratégique. Pas d'action requise immédiate de sa part.
