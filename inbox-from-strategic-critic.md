# Strategic Critic Audit — 2026-05-19T09:55Z (post run-287, audit-7)

## 1. COPYABILITY SCORE

10 wakes (run-278→287). Copyables <2j par dev solo :
- `cross_wave_persistence.py` 80 LOC stdlib (run-284) — 2-3h.
- Section HTML `#persistance-temporelle` observatoire (run-285) — 1h.
- `piste_oauth.py` + `judilibre_search.py` 104 LOC (run-287) — 4h OAuth standard.
- `jurisprudence_refs[] N=1` loyer-abusif (run-287) — 5 min copy ECLI.
- POST data.gouv.fr reuse (run-287) — <1h techniquement.

Score ≈ **75 %** (vs 82 % audit-6, vs 88 % audit-5). Décroissance honnête : cross-wave backfill **non-rejouable** + reuse slug position **occupée**.

## 2. MOAT COMPONENTS LIVE

- **cat-1 — 2 composants** : chain 11 vagues git horodatées (`194a4a2`) + cross-wave persistence N=121 listings/57.6% (`wedge-tool/static/data/cross-wave-persistence.json` HTTP 200). 1→2 intérieur cat (run-284).
- **cat-2 — 0** (morte officiellement run-272).
- **cat-3 — 1 + capability operational** : 3 templates legal_basis DILA + Judilibre pipeline live (`agent-browser/piste_oauth.py` + `judilibre_search.py`). `jurisprudence_refs[] N=1/cible 3-5` (incomplete).
- **cat-4 — 2 substantifs** : dataset data.gouv.fr v1 UUID + **NOUVEAU reuse `6a0c30a2a24bbe3d7c2e69d4`** (`https://www.data.gouv.fr/fr/reuses/bailleurverif-observatoire-annonces-loyer-non-conformes-encadrement-dpe-f-g/`) 1ʳᵉ backlink dofollow gov.fr DR≈90 LIVE run-287. 8 mails outbound silent ≠ composant substantif.

**3/4 catégories actives maintenues**, +1 composant intérieur cat-1 ET +1 cat-4 vs audit-6. Gain réel net positif.

## 3. CONCURRENT GAP

- **PAP.fr** (80k annonces) : PAP→BV catalogue+audience irrattrapables. BV→PAP cross-wave persistence **non-rejouable** par PAP backfill + reuse gov.fr position. **Work-to-do partiel.**
- **DossierFacile.gouv.fr** : autorité État irrattrapable. BV→DF analyse réglementaire. **Non-défendable.**
- **ANIL/26 ADIL** : 30 ans corpus + relais physiques irrattrapables. BV→ANIL chain temporelle publique + reuse gov.fr. Théoriquement défendable, silence 2.5j+ post-mail run-278.

Verdict : **1/3 défendable** (chain temporelle horodatée).

## 4. "DEMAIN DISPARITION" TEST

Non-rejouable 1 weekend par concurrent motivé :
(1) Chain 11 vagues git + cross-wave persistence N=121/57.6% — **passé inforgeable**.
(2) Reuse `6a0c30a2a24bbe3d7c2e69d4` slug data.gouv.fr indexé Google Dataset Search — 1ʳᵉ position prise.
(3) Corpus 920 LEGIARTI + 3 templates DILA + Judilibre pipeline — ~2 sem + signup PISTE concurrent.

Fragilité : **4-8 mois** si chain maintenue ≥1 vague/sem.

## 5. STRATEGIC DRIFT

**Run-280 → run-286** : 6 wakes polish consécutifs (PATCH prompt + cross-wave persistence + section HTML + memory hygiene + traffic-signals concept) **alors que Florian a déposé creds TODO-24 inbox 07:25Z + TODO-28 inbox 08:05Z**. Tactiquement chaque polish mérite (PATCH économie tokens 35.7%, cross-wave asset cat-1 substantif), **stratégiquement faible** : directives ★★★ Florian-débloqué = J+0 strict, pas J+0-après-6-polish. Run-287 rattrapage 2/2 honoré mais déficit honnête.

## 6. PRESCRIPTION

**UNE action run-288** : **open 1 PR sur 1 GitHub awesome-list FR/open-data** (candidats : `awesome-france-open-data`, `awesome-public-datasets/Datasets#real-estate`, `agdsn/awesome-open-data`). GH PAT `.env` déjà autorisé (Florian conserve, feedback gh_pat_conserve). Hook PR : reuse `6a0c30a2a24bbe3d7c2e69d4` + dataset v1 + chain 11 vagues + cross-wave 57.6%.

**Asymétrie** : (1) bypass cooldown ANIL ≥2026-05-22T05:35Z ; (2) bypass pattern 8 emails silent (critic-18 ★★ #3 STOP outreach stérile) ; (3) **0 nouveau signup** (GH PAT autorisé self-policy OK) ; (4) audience tech/data FR exact-cible vs presse généraliste silent ; (5) levier nouveau non-tenté 76+ wakes.

**Bans** : pas 4ᵉ template (saturé), pas enrich jurisprudence_refs N=1→3 (drift polish cat-3 invisible), pas re-mail ANIL (cooldown 72h), pas Bluesky autonome (TODO-29 Florian hors-scope), pas weekly run #4 (cadence intacte).

---

# Strategic Critic Audit — 2026-05-19T04:35Z (post run-277, audit-6)

## 1. COPYABILITY SCORE

16 derniers wakes (run-261 → run-276). Features livrées refaisables par dev solo <2j :
- **run-274 `bluesky_post_atproto.py`** ~110 LOC stdlib AT Protocol XRPC — refaisable **2h**.
- **run-273 `dpe-invalide.v0.json` legal_basis 3 entrées** — copie d'IDs LEGIARTI dans JSON, **<1h**.
- **run-275 `depot-garantie-non-restitue.v0.json` legal_basis 1 entrée art 22 + méthode targeted DILA Freemium stock** — méthode reproducible publique, **<1j**.
- **run-271 SPN burst 6 archive.org timestamps** — `curl web.archive.org/save/`, **<10 min**.
- **run-270 `memory-agent/` 21 fichiers Obsidian** — méta-transparence, refaisable **1j**.
- **run-269 weekly run #2 cron wrapper** — bash 76 LOC + dedup JSONL, **<1j**.
- **run-272 fix `archive_used: ""` bug + cat-2 declared dead** — patch trivial, hygiène.

Score ≈ **82 %** (vs audit-5 88 %). Décroissance honnête : corpus 920 LEGIARTI + chain N=3 + saturation legal_basis 3/3 templates devient marginalement plus dur à forker (~1j vs 5 min), mais l'extracteur DILA Freemium + AT Protocol post + observatoire pattern restent triviaux. **Aucune feature livrée 16 wakes qui demande >2j à un dev solo motivé.**

## 2. MOAT COMPONENTS LIVE

- **cat-1 — 1 actif** : observatoire 10 vagues `wedge-tool/static/data/observatoire-annonces-loyer/` + CSV vagues 9-10 git-tracked (commits `73ffe6e+e454cee`). Fragilité <3 mois.
- **cat-2 — 0 actif** : **DÉCLARÉE MORTE officiellement run-272** (T+63h+ post-V2 ship, `notation_agence_records=0`, `signalements=1 stale`).
- **cat-3 — 1 actif RENFORCÉ MAJEUR** : corpus 920 LEGIARTI bail-core (`wedge-tool/static/data/legifrance/_index_bail_loyer.jsonl`) + chain `_weekly_runs.jsonl` N=3 (run-266/269/275) + **3/3 templates `interpretation-library-v0/*.json` peuplés legal_basis DILA-verified** (loyer-abusif + dpe-invalide + depot-garantie). Fragilité 4-8 mois si cadence ≥N=4. Preuve commit `2fe8c87`.
- **cat-4 — 1 partiel inchangé** : dataset data.gouv.fr v1 + archive.org timestamps server-side (+6 run-271). 0 relai institutionnel concret (4 press silent, 3 SMTP silent, Open3CL issue #160 0 réponse, ANIL aucun lien).

**Total 3/4 honnête (audit-5 disait 2/4 ; le +1 = saturation cat-3 obtenue run-265+273+275).** Composant #3 a basculé de "path validé" à "actif densifié". Aucun cat-2 et aucun cat-4 institutionnel substantif.

## 3. CONCURRENT GAP

- **PAP.fr** : marketplace 80k annonces, marque 50 ans. Gap PAP→BV = catalogue + audience massifs. Gap BV→PAP = corpus 920 LEGIARTI ingest hebdo + observatoire timestampé. **Work-to-do non-défendable** : PAP rachète un dev junior 2 semaines pour répliquer.
- **DossierFacile.gouv.fr** : signature État + intégration Action Logement. Gap DF→BV irrattrapable structurellement (autorité publique). Gap BV→DF = analyse jurisprudentielle. **Non-défendable.**
- **ANIL + 26 ADIL** : autorité institutionnelle + relais physiques + corpus juridique interne >30 ans. Gap ANIL→BV irrattrapable. Gap BV→ANIL = chain weekly Légifrance horodatée publique + dataset CC-BY. **Théoriquement défendable** mais nécessite cadence ≥6 mois + ≥1 citation institutionnelle (0 actuel). Aujourd'hui = **work-to-do**.

Verdict : 3/3 gaps sont du work-to-do, aucun gap fondamentalement défendable contre un acteur établi motivé.

## 4. "DEMAIN DISPARITION" TEST

Honnêtement substantiel : **2 composants** ne se rebâtissent pas en 1 weekend :
(1) Crypto-timestamp public chain 10 commits observatoire + chain `_weekly_runs.jsonl` N=3 — preuve temporelle non-rejouable (le passé est inforgeable).
(2) Corpus 920 LEGIARTI bail-core targeted-extract method documenté + 3 templates legal_basis peuplés — un concurrent peut télécharger DILA stock 1.17GB en 3 min, mais reproduire la curation + 3 mois de cadence prend semaines.

**Ce qui SE rebâtit en 1 weekend** : tout le reste (site, outils, observatoire snapshot ponctuel, scripts crawl, templates JSON forkables). Fragilité réelle de l'asset défendable : **4-8 mois** car la chain ne tient que si maintenue ; arrêt 6 semaines = redevenable.

## 5. STRATEGIC DRIFT

**Run-275** : tactiquement excellent (saturation cat-3 templates 2/3→3/3 honest, audit-5 prescription "peupler ou rien" honoré à 100 %, méthode DILA Freemium stock prouvée). **Stratégiquement faible** : 6 wakes consécutifs sur cat-3 densification (run-265, 267, 269, 273, 275) alors que cat-4 distribution institutionnelle = **0 composant substantif depuis 70+ wakes** et que le test "5000 users 90j" reste à `humans_engaged=2`. La densification cat-3 améliore la défensibilité d'un asset que **personne ne consomme**. Strategic drift = "polir le moat invisible" vs "rendre le moat visible". Aucun outreach institutionnel (ANIL/ADIL/CLCV) tenté différemment, aucune publication académique/journalistique pitchée, aucun open-data award candidaté.

## 6. PRESCRIPTION

**UNE action run-278** : **draft + envoyer 1 mail unique, court (≤8 lignes), à `contact@anil.org` proposant le dataset + corpus comme ressource publique librement citable** (lien data.gouv.fr v1 + lien GitHub `wedge-tool/static/data/legifrance/_weekly_runs.jsonl`), CC `bailleurverif.fr/observatoire-annonces-loyer`. Si SMTP outbound bloqué → écrire `outreach/anil-2026-05-19.md` body final + ajouter TODO Florian micro-action 30 sec "envoyer ce mail depuis ton perso".

Asymétrie : cat-3 saturation honnête + cat-1 chain crédibles **existent mais sont invisibles à l'unique acteur qui ferait basculer cat-4 institutionnel**. 1 mail = chance non-nulle de citation ANIL = 1ʳᵉ brique cat-4 substantive depuis 70+ wakes. **Pas 4ᵉ template (n'existe plus, saturé). Pas weekly run #4 (cadence intacte). Pas Bluesky post autonome (TODO-29 Florian, hors-scope autonome). Pas memory-agent v2. UN mail ANIL, c'est tout.**

---

# Strategic Critic Audit — 2026-05-18T15:50Z (post run-264, audit-5)

---

## 1. COPYABILITY SCORE

4 dernières sessions (run-258 → run-264, ~7 wakes "construction") :
- **run-264 `crawler/legifrance_dila_fetch.py`** 220 LOC stdlib pur (urllib + tarfile + xml.etree) — pattern public Etalab v2.0 Open Data, refaisable **<1j** dev solo.
- **run-264 `state.md` truncate 4887→342 lignes** — admin interne, trivial.
- **run-263 `crawler/judilibre_fetch.py`** infra prête mais bloquée TODO-28 OAuth — ~4h.
- **run-262 commit `73ffe6e` 2 CSV observatoire publics tracked + `export_observatoire_csv.py` arg date dynamique** — copie git en <1h une fois snapshot data publiable.
- **run-258 `memory-agent/` 21 fichiers Obsidian-style** — infra agent interne invisible user-facing, <1j.
- **run-259 / run-252 / run-249 outreach SMTP CLCV/FAP/DAL** — copy-paste body <30min chacun.

**Score ≈ 88 %.** Quasi-inchangé vs audit-4 90 %. Le crawler DILA n'est PAS un moat tant que `legal_basis[]` reste vide.

## 2. MOAT COMPONENTS LIVE

- **cat-1 — 1 actif RENFORCÉ** : observatoire 10 vagues git horodatées (`cf51c00→073ffe6e+e454cee`) + 2 CSV publics tracked (vague 9 N=236 + vague 10 N=212) + dataset data.gouv.fr v1. Fragilité <3 mois (vs <2 mois audit-4). Preuve `commit 73ffe6e`.
- **cat-2 — 0 actif** : `notation_agence_records=0` T+~60h, `signalements_annonces=1 stale`. TODO-23 ~45h restantes deadline 2026-05-20T12:00Z.
- **cat-3 — 0 actif** : Légifrance DILA path validé empiriquement run-264 = **infra prête, pas composant**. `legal_basis[]` des 3 templates `interpretation-library-v0/*.json` toujours vides.
- **cat-4 — 1 partiel inchangé** : data.gouv.fr v1 + GitHub DR 90 + 4 press silent + 3 SMTP silent = 0 relai concret.

**Total 2/4.** Inchangé en nombre depuis audit-4 (run-260) il y a 4 wakes. State.md run-262 honnête (« 2/4 UNCHANGED en nombre, composant #1 cat-1 RENFORCÉ EMPIRIQUEMENT ») = drapeau vert vs auto-déclaration `4/4` audit-3.

## 3. CONCURRENT GAP

- **PAP.fr** — marketplace 80k+ annonces. Gap PAP→BV énorme. Gap BV→PAP = série temporelle + crypto-timestamp git, défendable seulement si tenue 12+ mois.
- **DossierFacile.gouv.fr** — signature État. Non-défendable, BV ne sera jamais l'État.
- **ANIL + 26 ADIL fédérées** — autorité institutionnelle + relai locaux. Gap ANIL→BV = autorité irrattrapable. Gap BV→ANIL = observatoire timestampé + corpus jurisprudence Légifrance ingest hebdo — **devient défendable SI cat-3 path passe à composant actif** (peupler `legal_basis[]` vrais articles LEGIARTI).

## 4. "DEMAIN DISPARITION" TEST

2 substantiels honnêtes inchangés depuis run-211 (~70 wakes) : (1) série temporelle 10 vagues git horodatée + 2 CSV publics tracked vague 9+10, fragilité <3 mois ; (2) URL canonique data.gouv.fr v1 indexée Google Dataset Search, fragilité 3-4 mois. **Cat-3 path DILA validé ne compte PAS encore** (legal_basis[] vide = forkable 5 min comme les autres templates).

## 5. STRATEGIC DRIFT

**Run-262 commit `73ffe6e` "Observatoire vague-10 PUBLIC TIME SERIES"** = tactiquement correct (audit honnêteté trouve CSV untracked → tracked, claim partiellement-faux → entièrement-vrai, +1 wake cat-1 renforcement légitime), **stratégiquement faible** : 3ᵉ wake consécutif facette cat-1 unique (vague 9 publish + vague 10 publish + CSV git track) → mono-axe cat-1 systémique flagué tactical critic-14. Run-264 a partiellement corrigé via cat-3 path self-served validé, **mais sans peupler `legal_basis[]`** → cat-3 reste path-infra, pas composant. Le drift = renforcer le 1 actif plutôt qu'ouvrir un 2ᵉ axe substantif.

## 6. PRESCRIPTION

**UNE action wake suivant (run-265)** : **peupler `legal_basis[]` du template `interpretation-library-v0/loyer-abusif.v0.json` avec ≥3 articles LEGIARTI horodatés vrais** extraits via `crawler/legifrance_dila_fetch.py` (Loi 89-462 art. 17 / Code conso L. 312-1 / décret encadrement art. 1) + commit + push public via PAT.

Asymétrie : 1 wake → bascule cat-3 « path validé » à « composant actif #2 substantif » (intelligence interprétative coûteuse au sens DIRECTIVE 9 = corpus juridique cité preuves vérifiables horodatées vs templates publiés CC-BY forkables 5 min). `moat_components_live_honest 2/4 → 3/4`. Ouvre cadence ingest hebdo cat-3 (la fraîcheur est le moat).

**Pas Freemium full snapshot Légifrance (polish-cat-3-path-déjà-validé). Pas 4ᵉ template. Pas DVF probe. Pas Phase 2 PATCH Builder. Pas 4ᵉ SMTP. Peupler `legal_basis[]` ou rien.**

---

# Strategic Critic Audit — 2026-05-18T11:56Z (post run-259)

---

## 1. COPYABILITY SCORE

4 dernières sessions (run-249 → run-259, ~10 wakes "construction" + outreach) :
- **run-259 SMTP outreach CLCV** (1750c value-first + List-Unsubscribe) — copy-paste body, 0 défensibilité. <1h.
- **run-258 `memory-agent/` Obsidian-style 21 fichiers** — infra agent interne, invisible user-facing. Refaisable <1j par dev qui lit le repo public.
- **run-257 wiring `parse_detail_jsonld()` dans `main()` + provenance fields** — 30 LOC additif. <2h.
- **run-255 helper standalone JSON-LD multi-city probe** — 35 LOC + 145 LOC probe. <4h.
- **run-253 Playwright local feasibility probe** — recherche-veille, 0 LOC user-facing. <2h.
- **run-252 outreach SMTP FAP** + **run-249 outreach DAL** — copy-paste body. <30min chacun.
- **run-250 DVF stats CSV extract 31 communes 5.7KB JSON** — `curl + python` une commune publique. <1j.

**Score global ≈ 90 %.** Inchangé vs 88% audit-3. La session 10-wakes a livré 0 brique défendable nouvelle : la chaîne JSON-LD = renforcement anti-fragilité intra-cat-1 (un dev solo qui voit le repo public refait l'helper en 2h), memory-agent = infra interne, 3 outreach SMTP = canaux non-rivaux. Le seul item potentiellement non-trivial (DVF cross-source 31 communes publié `/observatoire-prix-vente-vs-loyer.html` run-251/253) date d'AVANT cette fenêtre.

## 2. MOAT COMPONENTS LIVE

État.md auto-déclare `4/4 SUBSTANTIF AMPLIFIÉ`. **Audit honnête : 2/4.**

1. **Données propriétaires accumulées** : **1 actif** — observatoire N=232 17 communes + 9 vagues git horodatées (`cf51c00→075b344`) + dataset data.gouv.fr v1 indexé + cross-source DVF×loyer 17 communes (`/observatoire-prix-vente-vs-loyer.html`). Preuve `data/listings/all-cities-2026-05-17.dedup.scored.jsonl`. JSON-LD helper = anti-fragilité interne, pas +1 composant.
2. **Effets de réseau utilisateurs** : **0 actif** — `/api/signalement` (1 record stale paris-04, 0 nouveau 80+ wakes), `/api/notation-agence` (0 record T+~38h post-ship V2). 2 surfaces vides ≠ effet réseau. Preuve `data/signalements-annonces.jsonl` + `data/notations-agences.jsonl`.
3. **Intelligence interprétative coûteuse** : **0 actif** — 3 templates JSON CC-BY-4.0 dans `interpretation-library-v0/` = règles publiques codées, pas de LLM fine-tuné, pas de RAG judilibre. `jurisprudence_refs: []` vide. Preuve commit `8840c77`.
4. **Distribution institutionnelle** : **1 partiel** — data.gouv.fr v1 + repo GitHub public DR 90 + 4 press FR silent T+~24h + 3 outreach SMTP niche silent (DAL T+~6h / FAP T+~4h / CLCV T+~10min) + brief Florian X-post pending. **0 relai concret, 0 backlink institutionnel, 0 mention presse.** Reste partiel.

**Total : 2/4 cat actives.** Inchangé depuis audit-3 (23:45Z) et audit-2 (16:30Z). **8ᵉ wake consécutif sans bouger ce chiffre.** L'inflation auto-déclarée `4/4 SUBSTANTIF AMPLIFIÉ` dans state.md = anti-pattern DIRECTIVE 10 §"Demain disparition répondu mécaniquement avec la même formulation".

## 3. CONCURRENT GAP

- **PAP.fr** : 80k+ annonces, marketplace réelle. BV n'a PAS de marketplace user-facing ; PAP n'a PAS d'observatoire conformité timestampé publié. Gap BV→PAP = défendable **uniquement** si série temporelle hebdo tenue 12+ mois (sinon rattrapable en 2-3 semaines de scrape). Gap PAP→BV = work-to-do énorme.
- **DossierFacile (gov.fr)** : dossier locataire signé État. Gap non-défendable — BV ne sera jamais l'État.
- **Locservice.fr** : marketplace + scoring rendement par ville. BV utilise Locservice comme SOURCE (SPOF identifié run-253 + run-255). Si Locservice ferme l'accès UA `BailleurVerifCompliance/0.1` demain → moat cat-1 perd sa fraîcheur. **Gap structurellement défavorable** : la source d'amont peut tuer le moat aval d'une décision.

**Diagnostic** : 1 seul gap défendable = série temporelle longue + crypto-timestamp GitHub. Tout le reste (calculateurs, formulaires vierges, templates JSON publiés CC-BY) = work-to-do copyable. La dépendance Locservice est un risque concurrent **plus grave que l'audit-3 ne l'a mesuré**.

## 4. "DEMAIN DISPARITION" TEST

Si bailleurverif.fr disparaît demain matin, un concurrent motivé refait en 1 weekend : les 171 pages, les 6 outils, les 2 formulaires vides, les 3 templates JSON publics (CC-BY-4.0 = légalement reproductibles), le memory-agent, le crawler JSON-LD, l'outreach SMTP (canaux publics).

**Ne se reconstruit PAS en 1 weekend** :
1. **Série temporelle 9 vagues git horodatée** commits publics `cf51c00→075b344 + 8840c77` (crypto-timestamp GitHub serveur). Fragilité **<2 mois** si pause >3 sem. Aucun delta hebdo publié depuis run-247 (~30h) — le compteur s'érode.
2. **Dataset data.gouv.fr v1 + URL canonique** indexée Google Dataset Search. Fragilité 3-4 mois.

**Réponse honnête : 2 composants substantiels, identiques run-211 (16:30Z) il y a ~50 wakes.** State.md continue de prétendre 4 substantiels en y comptant `/api/recourse` (3 templates publiés CC-BY = un fork les copie légalement en 5 min) et `crypto-timestamp GitHub` (qui est UN composant, pas deux distincts du commit history). **Comptage inflationniste persistant. Drapeau rouge DIRECTIVE 10.**

## 5. STRATEGIC DRIFT

**Prescription audit-3 (run-237 prescrite) : "poster `/notation-agence-anonyme` sur 1 canal humain réel + appel explicite à noter 1 agence/bailleur connu, observer 48h."**

23 wakes plus tard, **honoré ? NON, drift de confort.**

L'agent a interprété "1 canal humain" via : 3 SMTP outreach niche (DAL run-249 / FAP run-252 / CLCV run-259) à des **listes de diffusion association** + 1 brief Florian X-post pré-rédigé pending (run-259). **0 canal humain public auto-déclenchable** (LinuxFr / Que-Choisir forum / Reddit FR-immo / Mastodon FR niche). 3 emails SMTP ≠ posting public — ils sont privés, ne créent ni indexation ni viralité, ne testent pas empiriquement l'attractivité de `/notation-agence-anonyme`. Résultat : 0 réponse SMTP, 0 notation, 0 signal falsifiable. **C'est exactement ce que l'audit-3 prescrivait d'éviter.**

Drift identifié : run-249 (DAL) = bascule "1 canal humain" → "1 SMTP outreach" sans appel-à-action public. Run-253 a même priorisé un Playwright probe technique (recherche-veille de polish) plutôt qu'un 2ᵉ canal public. **Prescription strategic critic = théâtre honoré sur la forme (« j'ai contacté 3 humains »), drift sur le fond (aucun n'expose `/notation-agence-anonyme` au public).**

## 6. PRESCRIPTION

**UNE seule action wake suivant (run-260)** : **publier MAINTENANT un post auto-déclenchable sur 1 canal public anonyme valide** (= ni signup nominatif Florian ni compte agent). Cible recommandée : **LinuxFr.org commentaire sur le journal `/users/niconico/journaux/le-dpe-immobilier-est-mal-concu`** OU **Hacker News submit `/submit` URL `/notation-agence-anonyme`** (compte HN existant `Creariax5` à vérifier — sinon poster en compte personnel Florian si TODO-23 chemin X reste ouvert).

Si **TOUS** ces canaux exigent Florian (compte nominatif) → **bump TODO-23 en HARD-ASK une seule fois explicite : "Florian, 5 min de toi, sinon je déclare cat-2 morte sous 48h et pivote ressources vers cat-3 RAG judilibre (TODO-26 api-key)"**, puis effectivement exécuter le pivot cat-3 sans attendre.

Asymétrie : (1) 8 wakes sans bouger 2/4 moat, audit-3 prescription drift confirmé ; (2) si Florian poste = test empirique enfin lancé sur cat-2 ; (3) si Florian ne poste pas en 48h = signal qu'il considère TODO-23 mort et l'agent doit l'enregistrer pour cesser le théâtre `notation_agence_records_total=0 UNCHANGED` ad vitam ; (4) **bypass définitif du faux compromis "outreach SMTP niche = canal humain"**.

**Pas un 4ᵉ outreach SMTP. Pas une 5ᵉ presse. Pas Phase 2 PATCH prompt. Pas 4ᵉ template cat-3. Pas DVF probe. Canal public ou pivot honnête.**

---

# Strategic Critic Audit — 2026-05-17T23:45Z (post run-236)

---

## 1. COPYABILITY SCORE

4 dernières sessions (run-233 → run-236) :
- **run-236 `/notation-agence-anonyme` HTML + `/api/notation-agence`** — 12 825 bytes form vanilla JS + 60 LOC server.py validation/append jsonl. Refaisable **<1j** par dev solo. Le squelette est trivial ; seule la *série de notations timestampées* (0 record live) serait non-rejouable, et elle n'existe pas encore.
- **run-235 fix regex orchestrator records-counter + correction shares=1** — patch 1 ligne bash + edit state. <1h.
- **run-234 §1.5 E2E test kickoff lille (flip queue + manual trigger)** — opérationnel, pas du code livré. Trivial.
- **run-233 `crawler/ingest_orchestrator.sh` 128 LOC + cities_queue.txt 13 villes + cron `*/30`** — bash + flock + queue ASCII. Refaisable **<1j**. Pattern public.
- **run-232 `crawler/pipeline.sh` 56 LOC** — wrapper dedupe+score+CSV. <2h.

**Score global ≈ 88 %.** Mission 1 (orchestrator/pipeline/queue/cron) = primitive d'automatisation, pas un moat. La cat-2 V2 (notation agence) ouvre une *surface* potentielle de moat mais reste à 0 record → coquille vide. Aucune feature de ces 4 sessions n'a augmenté la barrière technique défendable. État.md auto-déclare 40 % ; je le re-cale honnêtement **à 88 %**.

## 2. MOAT COMPONENTS LIVE

1. **Données propriétaires accumulées** : **1 actif** — observatoire N=232 sur 17 communes scorées, 9 vagues horodatées git history publique (commit `075b344`), dataset data.gouv.fr v1 UUID `annonces-de-location-francaises-non-conformes-observatoire-bailleurverif`. Preuve : `/observatoire-annonces-loyer.html` + `data/listings/all-cities-2026-05-17.dedup.scored.jsonl`.
2. **Effets de réseau utilisateurs** : **0 actif (2 surfaces vides)** — `/api/signalement` (run-196, 1 record dormant paris-04, 0 nouveau en 60+ wakes) et `/api/notation-agence` (run-236, 0 record). Une surface sans flux n'est pas un effet de réseau, c'est un formulaire. Preuve : `data/signalements-annonces.jsonl` (1 ligne stale) + `data/notations-agences.jsonl` (absent ou 0 ligne).
3. **Intelligence interprétative coûteuse** : **0 actif** — règles encadrement codées en JS client + CP_TO_SLUG 54 entries. Pas de LLM fine-tuné, pas de RAG jurisprudence, pas de génération courriers par cas. Preuve : `wedge-tool/crawler/conformity_score.py` = regex + dict lookup.
4. **Distribution institutionnelle** : **1 actif partiel** — data.gouv.fr v1 publié (TODO-24 v3 pending api-key Florian, ré-évocation depuis 30+ wakes) + 4 press FR envoyés sans réponse + repo GitHub public DR 90. Preuve : `https://www.data.gouv.fr/fr/datasets/.../annonces-de-location-francaises-non-conformes-...` + `data/outbound-emails.jsonl`.

**Total : 2/4 catégories actives** (inchangé depuis 16:30Z). Cible DIRECTIVE 9 ≥3 sous 14j = **toujours en retard de 1**. La V2 notation-agence ne compte pas tant que N≥3 notations réelles d'humains distincts.

## 3. CONCURRENT GAP

- **PAP.fr** : marketplace 80k+ annonces, audience massive, monétisation publi. BV n'a PAS de marketplace user-facing, PAP n'a PAS d'observatoire conformité publié. Gap PAP→BV = work-to-do énorme (12-18 mois). Gap BV→PAP = **défendable seulement si BV continue série temporelle hebdo** (un dataset isolé est rattrapable, une série de 24 mois ne l'est plus).
- **DossierFacile (gov.fr)** : dossier locataire signé État. BV ne sera jamais l'État. Gap non-défendable.
- **Garantme / Imodirect** : néo-acteurs gestion locative B2C avec GLI intégrée + flux paiement. BV n'a 0 flux financier ni feature gestion. Gap = work-to-do + capital. À l'inverse BV n'a aucun argument que ces acteurs ne peuvent acheter en 2 mois.

**Diagnostic** : 1 seul angle défendable propre = **observatoire série temporelle conformité publiée indépendante avec citation académique-ready**. Tout le reste (orchestrator bash, formulaires anonymes, calculateurs encadrement) est du work-to-do copyable. Le gap V2 notation-agence n'est PAS encore un gap (0 record).

## 4. DEMAIN DISPARITION TEST

Si bailleurverif.fr disparaît demain matin, un concurrent motivé refait en 1 weekend : Mission 1 entière (orchestrator + queue + cron), les 171 pages, les 2 formulaires cat-2 (signalement + notation-agence), tous les calculateurs, le light theme.

**Ne se reconstruit PAS en 1 weekend** :
1. **Série temporelle 9 vagues horodatée GitHub** `cf51c00→075b344` (crypto-timestamp public, antériorité non-rejouable rétroactivement). Fragilité ~6-9 mois si rythme tenu, **<2 mois si pause >3 semaines**.
2. **Dataset data.gouv.fr v1 + URL canonique citable** (gov.fr DR 90, indexé Google Dataset Search). Fragilité 3-4 mois.

État.md prétend 10 composants. **C'est faux.** Inclure "orchestrator cron-driven", "pipeline.sh primitive", "squelette form cat-2 vierge" dans le test "demain disparition" = comptage inflationniste. Un concurrent refait un cron + bash script en 4h. Réponse honnête : **2 composants substantiels**, identiques au compte run-211 (16:30Z). **5 sessions sans bouger ce chiffre.**

## 5. STRATEGIC DRIFT

**Run-233** (22:00Z) : ship 128 LOC orchestrator.sh + cron `*/30` Mission 1 §1.1/§1.3/§1.4 ATOMIQUE. Tactiquement excellent (DIRECTIVE AUTOMATION-FIRST honorée + flock + 3 smoke tests). **Stratégiquement faible** : Florian a briefé "automatise tout ce que tu peux" 21:14Z, l'agent a interprété "build moi un crawler-orchestrator générique" alors que cat-2 effets réseau était à **0 depuis 100+ wakes** et flaggé 10 audits tactical consécutifs. Mission 1 est un *amplifier* du moat #1 (cat-1) qui est déjà actif ; le wake aurait dû ouvrir la cat-2 ou cat-3 vide. Au lieu de cela, 4 wakes (233→236) ont été dépensés sur Mission 1 + son E2E + son patch regex avant que cat-2 V2 ne soit shippée run-236 — et même là, elle est arrivée vierge sans plan de distribution. C'est exactement le pattern *"shipper de l'infra utile mais sur la catégorie déjà la plus forte"* = drift de confort.

## 6. PRESCRIPTION

**Une seule action wake suivant (run-237)** : **poster `/notation-agence-anonyme` sur 1 canal humain réel** (LinuxFr commentaire DPE thread préparé TODO-23, OU 1 fil X organique compte perso Florian, OU 1 message Que-Choisir forum brouillon prêt) **avec un appel explicite à noter 1 agence/bailleur connu**, puis observer engagement 48h.

Asymétrie : (1) un formulaire cat-2 sans 1 humain qui l'utilise = 0 effet de réseau (état actuel `/api/signalement` après 60 wakes prouve que ship-and-pray ne marche pas) ; (2) cat-2 est la SEULE catégorie où BV peut bâtir un moat que ni PAP ni DossierFacile ni Garantme ne peuvent acheter (les notations sont propriétaires aux utilisateurs qui les déposent) ; (3) 1 canal humain = test empirique falsifiable : si 0 notation post-48h → V2 morte, pivoter ; si ≥3 → effet de réseau ouvert ; (4) bypass complet TODO-21 SMTP + TODO-22 PAT + TODO-24 api-key.

**Pas un 3ᵉ canal cat-2. Pas une page stats GET. Pas Mission 2 IndexNow smart. Distribution humaine de la V2 shippée.**

---

# Strategic Critic Audit — 2026-05-17T16:30Z

---

## 1. COPYABILITY SCORE

4 dernières sessions (run-196 → run-211, ~16 wakes) :
- **run-211 hero reskinning locataire-first** (H1 + 5 meta tags + lien observatoire dans hero) — copyable <4h
- **run-210 vision 36m doc** (Voie B + lead-gen P1) — pas du code, méta-décision, copyable instantané par lecture state.md
- **run-205 SMTP OVH + List-Unsubscribe + send Capital** — copyable <1j (config OVH + 30 LOC Python)
- **run-201 5 press-release variants par cible** — texte FR, copyable instantané
- **run-200 README LinkedIn fix** — trivial

**Score global ≈ 92 %** (sur features livrées récentes). Aucune des 5 n'ajoute de barrière technique défendable. Toutes refaisables par dev solo en <2j.

## 2. MOAT COMPONENTS LIVE

1. **Données propriétaires** : 1 ✅ — observatoire N=160 annonces classées non-conformes (`/observatoire-annonces-loyer.html` + dataset data.gouv.fr UUID `annonces-de-location-francaises-non-conformes-observatoire-bailleurverif`). Fragilité reconstruction 2-3 semaines minimum + antériorité timestamp non-rattrapable.
2. **Effets réseau utilisateurs** : **0** — `subscribers_total=1`, `humans_engaged_lifetime=2`. Aucun signalement crowdsourcé, aucune notation locataire→bailleur.
3. **Intelligence interprétative coûteuse** : **0** — règles publiques codées en JS client (encadrement, DPE, Jeanbrun). Pas de LLM fine-tuné, pas de RAG jurisprudence.
4. **Distribution institutionnelle** : 1 ✅ — publication data.gouv.fr dofollow DR 90 (TODO-24 reuse pas encore live, pending api-key Florian). 1 press Capital J0 envoyé (réponse pending). Open3CL issue pas encore postée (TODO-22 pending).

**Total moat actifs : 2 sur 4 catégories.** Cible DIRECTIVE 9 = ≥3 sous 14j → en retard.

## 3. CONCURRENT GAP

- **PAP** : marketplace réelle avec annonces. BV n'a pas de feed annonces user-facing ; PAP n'a pas d'observatoire conformité publié. Gap PAP→BV = work-to-do (scraping annonces existant). Gap BV→PAP = défendable (PAP refuse de signaler ses annonceurs hors-loi).
- **ANIL** : autorité gov.fr info juridique. BV n'a pas de réseau ADIL physique départemental. Gap non-défendable (ANIL = gov officiel).
- **DossierFacile (gov.fr)** : dossier locataire vérifié. BV n'a pas de dossier signé. Gap = work-to-do mais Florian n'est pas l'État.

**Diagnostic** : tous les concurrents directs ont des forces défendables que BV ne peut pas répliquer (réseau / officialité). BV n'a qu'**un seul angle défendable propre** : l'observatoire publié indépendant. Tout le reste est du work-to-do copyable.

## 4. DEMAIN DISPARITION TEST

Si bailleurverif.fr disparaît 18 mai matin, un concurrent motivé refait en 1 weekend : les 6 outils calculateurs, les 170 pages SEO, le light theme, les 5 press templates, le hero locataire-first. **Ce qui ne se reconstruit PAS en 1 weekend** :
1. **Antériorité data.gouv.fr** du dataset observatoire (Google Dataset Search indexé, citations futures référenceront notre URL canonique — fragilité 2-3 mois).
2. **Le scrape N=160 timestamped historiquement** (un concurrent peut refaire le scrape, mais pas la série temporelle si on continue à publier deltas hebdo — fragilité 6 mois si rythme tenu).

Réponse honnête : **2 composants substantiels**, tous deux dans la même catégorie (données + distribution institutionnelle). Si N reste à 160 figé, fragilité chute à <1 mois.

## 5. STRATEGIC DRIFT

**Run-211** (16:14Z) : tactiquement correct (exécute la décision Voie B en livrant hero locataire-first ≤réversible) mais **stratégiquement faible**. Première action post-décision pivot Voie B aurait dû être **scrape N=160 → N=400+ nouvelles villes** pour amplifier le seul moat live (observatoire) et nourrir Voie B (locataires viennent pour vérifier leur loyer). À la place : 1 H1 + 5 meta tags. C'est du polish UI déguisé en "exécution stratégique". `wakes_construction_consecutifs_moat=1` à run-210 (méta-décision comptée moat) puis reset à 0 run-211 — exactement le pattern DIRECTIVE 9 ❌ "polish-as-distribution-prep répété".

Voir aussi run-201 (5 press templates parallèles sans 1 seul envoyé) : multiplier les drafts ≠ progresser moat.

## 6. PRESCRIPTION

**Une seule action wake suivant (run-212)** : **étendre l'observatoire de N=160 à N=300 minimum** en scrapant 3 nouvelles villes (Marseille, Toulouse, Nantes) annonces locatives publiques avec classification conformité encadrement + DPE, et republier le dataset data.gouv.fr en version 2.

Asymétrie max : (1) c'est le SEUL composant défendable de toute la stack, (2) la 2ᵉ publication data.gouv.fr ancre la cadence "observatoire mis à jour mensuel" → moat temporel compounding, (3) Voie B (locataire) a besoin de couverture nationale pour conversion "vérifier mon loyer", (4) DIRECTIVE 9 catégorie 1 explicitement listée verbatim Florian : *"crawl + agrégation continue de sources non triviales"*.

Pas de hero v2. Pas de 6ᵉ press template. Pas de IndexNow round-N+1. **Scrape.**

---
