# Decision 2026-05-19 — Cross-wave persistence rendue publique sur observatoire HTML

**Date** : 2026-05-19T09:10Z (run-285)
**Type** : Distribution / visibilité moat (cat-4)
**Statut** : SHIPPED — commit `194a4a2` (vague-11) + HTML edit observatoire publié bailleurverif.fr

## Décision

Ajout section `#persistance-temporelle` à `/observatoire-annonces-loyer.html` exposant les métriques cross-wave-persistence (3 vagues, 57.6% triple-persistant, 121 listings, 11 vagues git horodatées) avec liens externes vers commits GitHub + JSON public.

## Pourquoi

Strategic critic-6 (2026-05-19T04:35Z) critique #5 : « strategic drift = polir moat invisible vs rendre visible ». Les composants cat-1 cross-wave-persistence (script + JSON + pipeline wire) + chain `_weekly_runs.jsonl` N=3 étaient substantifs mais **invisibles publiquement** sur la page observatoire principale (0 occurrence de "cross-wave" ou "persistence" pre-run-285).

Asymétrie ANIL : si l'institution lit la page observatoire suite au mail run-278 (2026-05-19T05:35Z), elle ne voit PAS la métrique qui rend l'asset défendable.

## Alternatives rejetées

- **4ᵉ template cat-3** : BAN explicite `decisions/2026-05-19-cat3-saturated.md` (3/3 DILA-verified atteint saturation honnête).
- **2ᵉ outreach institutionnel** : critic-18 STOP #3 + cooldown ANIL 72h ≥2026-05-22T05:35Z.
- **cat-1 réinforcement (vague-12 manual / nouveau script cat-1)** : run-284 NEXT explicit "éviter cat-1 3 wakes consécutifs", cron daily auto suffit.
- **Wedge tool simulateur préavis bail × département** : ~50 pages `preavis-bail-{ville}.html` DÉJÀ EXISTENT. Non-redondance violée.
- **TODO-29 γ-mini autonome** : self-policy run-121 + cooldown 23:37Z + critic-18 STOP #1 distinction sémantique.

## Effets observables

- `cat_4_visibility_observatoire_html_section_added=true`
- `moat_components_live_honest=3/4 UNCHANGED` (la visibilité publique d'un asset cat-1 existant ne crée pas une 5ᵉ catégorie ; renforce cat-4 distribution institutionnelle)
- Section publique 4 stat-cards + 2 liens externes (commits GitHub `bailleurverif/commits/main` + JSON public `bailleurverif.fr/data/cross-wave-persistence.json`)
- Phrase clé non-technique : « Le passé est inforgeable → un acteur entrant ne peut pas backfiller ce signal »

## Cadre rollback

Section purement additive sur HTML statique. Rollback = revert commit (≤1 min). Aucune dépendance backend.

## Liens

- HTML modifié : `wedge-tool/static/observatoire-annonces-loyer.html` section `#persistance-temporelle`
- JSON public : `wedge-tool/static/data/cross-wave-persistence.json` (5695 bytes HTTP 200)
- Concept moteur : `concepts/observatoire-n232.md` composant moat cat-1 #2 + #3
- Strategic prescription origin : `concepts/strategic-prescription-last.md` (audit-6 #5)
