---
name: TODO-28 Judilibre pipeline opérationnel
description: piste_oauth.py + judilibre_search.py shipped + loyer-abusif jurisprudence_refs N=1 run-287
type: decision
---

# Decision — TODO-28 Judilibre pipeline opérationnel (run-287 2026-05-19T09:46Z)

**Décision** : (1) Coder `agent-browser/piste_oauth.py` + `agent-browser/judilibre_search.py` réutilisables stdlib pur. (2) Tester from-agent OAuth + search → succès. (3) Enrichir `loyer-abusif.v0.json/jurisprudence_refs[]` avec 1 décision Cass civ3 verified (N=1/cible 3-5, progressive enrich).

## Pourquoi (motivation)

- TODO-28 ★★★ Florian directive inbox 2026-05-19T08:05Z (PISTE creds `.env`, OAuth+search testés from-VPS).
- Strategic critic-6 audit-6 a flaggué cat-3 saturated legal_basis (3/3 templates) MAIS jurisprudence_refs vide = composant moat invisible. Judilibre = LA réponse exacte au gap.
- Pipeline OAuth client_credentials + Bearer search réutilisable pour 3 templates cat-3 + futures expansions.
- Self-policy run-121 "0 signup nominatif" respectée : Florian a fait le signup piste.gouv.fr, agent utilise creds existants.

## Implémentation

- `piste_oauth.py` 52 LOC stdlib urllib pur :
  - POST `oauth.piste.gouv.fr/api/oauth/token` grant_type=client_credentials
  - Scope par défaut "openid", scope étendu "openid resource.READ" pour Judilibre
  - Cache JSON `/tmp/piste_token_cache.json` chmod 600, TTL 50 min (refresh ≥10 min avant expiry nominal 60 min)
  - Sécurité : `PISTE_CLIENT_SECRET` env-only jamais loggée, cache disque chmod 600
- `judilibre_search.py` 52 LOC stdlib pur + import piste_oauth :
  - GET `api.piste.gouv.fr/cassation/judilibre/v1.0/search` Bearer auth
  - Params : query (string), size (int default 5), chamber (optional), date_start (optional ISO)
  - Output : 8 fields/decision (id, ecli, decision_date, chamber, jurisdiction, summary 240 chars, themes, source_url courdecassation.fr)
- Tests from-agent ✅ :
  - `python3 piste_oauth.py` → `OK (chars=54)` Bearer token
  - `python3 judilibre_search.py "encadrement loyer" --size 5 --chamber civ3 --date-start 2010-01-01` → `total=5044, results=5`

## Enrich loyer-abusif.v0.json N=1

- Sélection Cass civ3 `ECLI:FR:CCASS:2020:C300657` `decision_id=5fca33d50c7b4623bd8b0b2f` 2020-09-24
- Thème : loi 1948 bail / loyer / fixation / CEDH atteinte disproportionnée
- Pertinence : Cass confirme régime encadrement loyer (loi 1948, par extension loi 89-462 + Jeanbrun 2026-103) NE constitue PAS atteinte disproportionnée droit propriété CEDH art 1 protocole 1 → renforce position locataire face à bailleur contestant encadrement
- Format 8-field complet (ecli, decision_id, decision_date, chamber, jurisdiction, summary 240c, relevance_to_template, source_url)
- Honnêteté : `jurisprudence_refs_note` documente N=1/cible 3-5 (~20%) avec plan progressive enrichment runs +N (queries restantes "complément de loyer" ALUR / "loyer indu" zone tendue post-2014 / "art 17-2 loi 89-462")

## Pas de re-publication endpoint ce wake

- Cible N=3+ avant SHA1/ETag bump + IndexNow ciblé (anti polish-loop critic STOP "trophy KPI 3 wakes consécutifs")
- Endpoint `/api/recourse/loyer-abusif` continue à servir version run-243 (N=0 jurisprudence_refs) jusqu'à atteinte cible

## Alternatives rejetées

- **Alt 1 — Enrichir 3 templates × 3-5 décisions en run-287** : sur-engineering vs session budget ~10 min. Quality > quantity : 1 décision verified pertinente > 5 décisions noisy bail commercial.
- **Alt 2 — Skip enrich, ship helpers only** : helpers sans usage immédiat = capabilité fantôme. 1 enrich démontre pipeline end-to-end.
- **Alt 3 — Enrichir avec décisions arbitraires top-5 query brute** : noise (bail commercial vs habitation). Sélection 1 pertinente > 5 indistinctes.

## Effets observables KPIs

- `piste_oauth_helper_shipped=true` ★★ NEW
- `judilibre_search_helper_shipped=true` ★★ NEW
- `cat_3_jurisprudence_pipeline_operational=true` ★★★ NEW
- `loyer_abusif_jurisprudence_refs_count=0→1` ★
- `todo_28_status=DONE_capability_PROGRESSIVE_enrich`
- `agent_browser_python_helpers_count_added=2`

## Rollback

- `git checkout HEAD~1 -- agent-browser/piste_oauth.py agent-browser/judilibre_search.py data/interpretation-library-v0/recourse-templates/loyer-abusif.v0.json` → revert
- `/tmp/piste_token_cache.json` peut être supprimé (recréé au prochain run)

## Liens

- `agent-browser/piste_oauth.py`
- `agent-browser/judilibre_search.py`
- `data/interpretation-library-v0/recourse-templates/loyer-abusif.v0.json`
- Florian directive : `inbox.md` 2026-05-19T08:05Z
- Judilibre doc : `https://api.piste.gouv.fr/cassation/judilibre/v1.0/search`
