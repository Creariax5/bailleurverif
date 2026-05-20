---
name: BreadcrumbList fix 81+ pages + discipline codified
description: Brief Florian 2026-05-20T09:45Z HONORED run-321 J+0 (3 étapes 3/3). 90 pages HTML BreadcrumbList JSON-LD fix (item field manquant position 2), discipline codifiée seo-discipline.md, sub-seo-monitor PATCH v2 ajout audit task 2bis.
type: project
---

# BreadcrumbList fix 90 pages + discipline + sub-seo-monitor PATCH v2 — 2026-05-20T10:30Z (run-321)

## Décision

Brief Florian 2026-05-20T09:45Z HONORED J+0 (3 actions 3/3 + 1 commit + 1 push + 1 PATCH agents-control API + 1 concept update + 1 registry update).

**Why** : Découverte Florian via GSC URL Inspection sur `/encadrement-loyer-paris-2026.html` = 81 pages prod cassées BreadcrumbList JSON-LD (item #2 sans champ `item` URL). Invalidité silencieuse Rich Results breadcrumb pour 81 pages (31 encadrement + 50 DPE) = perte CTR SERP 5-15% docs Google + signal sémantique faible Knowledge Graph + LLM scrapers. Fix Florian Python `str.replace()` pre-wake (90 fichiers vs 81 = propagation guides/scanner/IRL/preavis/deficit/locataire-loyer-legal/loyer-legal-paris). Agent exécute propagation GitHub + codification discipline + PATCH sub-agent détection structurelle pérenne.

**How to apply** :

1. **Commit 3ee81da** : `git add wedge-tool/static/*.html` + message verbatim "fix: add missing item field on BreadcrumbList position 2 (81+ pages)" + push origin main via PAT.
2. **Concept `seo-discipline.md`** : section BreadcrumbList template rule ajoutée (+~80 lignes). Pattern correct JSON-LD documenté avec 3 positions `item` obligatoire. Table 6 hubs catégorie canoniques. 4 anti-patterns. Détection auto sub-seo-monitor cycle suivant. Canary post-fix 2 pages mentionnée.
3. **PATCH sub-seo-monitor v2** : prompt 3301→5766 chars (+2465). Tâche 2bis "BreadcrumbList JSON-LD audit" insérée. Python parse `wedge-tool/static/*.html` (~190 fichiers), grep `ListItem` sans `item`, output `breadcrumb_audit` JSON synthèse. Alert trigger §6 4ᵉ condition. Backup `prompts-backup/sub-seo-monitor-patch-v2-2026-05-20T1031Z.json`. Registry updated v1/v2 history.

## Hubs catégorie canoniques (à respecter pour futures pages)

| Nom catégorie | URL hub `item` |
|---|---|
| `Encadrement des loyers` | `/encadrement-loyer-france-2026.html` |
| `Loyer légal` | `/encadrement-loyer-france-2026.html` |
| `DPE & passoires thermiques` | `/dpe-fiabilite.html` |
| `Guides` | `/` (homepage) |
| `Outils gratuits` | `/` (homepage) |
| `Observatoire` | `/observatoire-annonces-loyer.html` |

## Canary indexation post-fix

Florian à demander indexation GSC manuelle 2 pages canary :
- `https://bailleurverif.fr/encadrement-loyer-paris-2026.html`
- `https://bailleurverif.fr/aix-en-provence-dpe-f-g-interdit-location.html`

Re-check breadcrumb status "valid" J+1/J+2 cible 2026-05-22T10:30Z → confirme fix systémique 90 pages.

## Impact métrique

- `breadcrumb_pages_with_missing_item=81→0` ★ NEW
- `florian_briefs_honored_j0_lifetime=NEW initialized cumul=3` (run-318 orphan-fix + run-319 Wikidata + run-321 BreadcrumbList)
- `directive_7_revisee_compliance_consecutive_wakes=100→101` ★ post-trophy
- `sub_seo_monitor_prompt_chars=3301→5766` (+2465)
- `pages_html_modified_this_wake=90`

## Note ban-strategic-9/10 anti-touch Paris page

Touche `/loyer-legal-paris.html` ce wake = metadata-only JSON-LD `item` URL position #2. Pas contenu visible humain, pas FAQPage, pas Dataset, pas simulateur. Pas content-level A/B variable. BAN non-violé (mandaté Florian brief explicite 3-étapes). Documenté ledger ACTION run-321 + ce decision.

## Tactical-26/27 alignment

Audit critic-27 audit-2026-05-20-0955.md = 8.7/10 (+0.1) pre-wake. Audit critic-28 ~run-330 verra : 3 briefs Florian J+0 cumul honored (run-318/319/321), 0 vol décision TODO-34/32/33 maintenu 10ᵉ wake silent, sub-seo-monitor PATCH v2 sans spawn 5ᵉ sous-agent (anti-bomb), 90 pages HTML fix sans page nouvelle (anti-bookkeeping), 0 server restart (read-only).
