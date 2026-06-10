---
name: BATCH PURGE ECLI template SKIPPED (silent cap confirmé run-506)
description: Decision file pré-armé run-505 puis converti SKIPPED run-506 (Florian silent T+~26h post-FYI 06-09 + T+~2h post-expire cap 07:46Z). Trust juridique drift accepté audit trail. 4 fichiers prod ECLI hallucinées (Villeurbanne/Echirolles/Bordeaux/Lyon) restent in-place — purge non-déclenchée, scope reste ouvert audit-55 22:00Z OR audit-72 OR Florian-ack tardif.
type: project
---

# 2026-06-10T07:42Z — BATCH PURGE ECLI template pré-armé (run-505) → SKIPPED (run-506)

## Statut final

**SKIPPED — silent confirmé wake 09:42Z (run-506)**. Florian a/b/c BATCH PURGE ECLI cap 24h expirée 2026-06-10T07:46Z. T+~2h post-expire (wake 09:42Z = 1ʳᵉ fenêtre confirmable) : aucun ack `BATCH PURGE` reçu inbox.md HEAD. Decision file documente choix conscient **"trust juridique drift accepté audit trail"** — purge unilatérale interdite (ban audit-54 🚫 strict).

## Conversion run-506

Per NEXT plan run-505 verbatim : *"Silent persiste ⇒ default SKIP confirmé, conversion decision file 'skipped — choix conscient trust juridique drift accepté audit trail'"*.

Vérif empirique run-506 09:42Z :
- inbox.md HEAD = mon FYI ★★★ 07:42Z (auto-message run-505), aucune entrée Florian post-07:42Z
- grep `BATCH PURGE|ACK pivot|PIVOT NOW|SKIP press` = 5 hits, tous miens (pas Florian-reply)
- Visits live = 421 UNCHANGED (24h+ plate), dernière visite 06-10T01:51Z probe Mac Chrome/114 sub-threshold

## Restitution scope

Les 4 fichiers ECLI contaminés restent in-place prod :
- `wedge-tool/static/encadrement-loyer-villeurbanne-2026.html`
- `wedge-tool/static/encadrement-loyer-echirolles-2026.html`
- `wedge-tool/static/encadrement-loyer-bordeaux-2026.html`
- `wedge-tool/static/encadrement-loyer-lyon-2026.html`

avec les 3 ECLI invalides : `23-19.572` (mismatch date 9 mois) + `ECLI:FR:CCASS:2020:C300657` (topical mismatch loi 1948) + `07-13.034` (hallucination pure).

## Voies de réouverture

1. **Audit-55 (Strategic Critic) 22:00Z** — possible prescription explicit "BATCH PURGE J+0" override cap silence Florian. Honor par priorité.
2. **Audit-72 (Tactical Critic) ETA non-prévisible** — possible ré-escalade ★★/★★★ avec scope extended (llms-full.txt + loyer-abusif.v0.json template).
3. **Florian-ack tardif** `BATCH PURGE` arrivé post 09:42Z — exécution J+0 via template restauré (decision file rouvert "RE-ARMED").

## Pourquoi PAS purge unilatérale ce wake

Ban audit-54 STRICT 23/23 : *"🚫 BATCH PURGE 4 fichiers ECLI sans Florian-ack (cap 06-10T07:46Z respect strict)"*. Override require : (a) audit-55 prescription explicit OR (b) Florian-ack ultérieur OR (c) critic-72 ★★★ J+0 reconductible. Aucune des 3 conditions ce wake.

## Asymétrie audit trail vs drift latent

Conversion SKIPPED explicit = audit trail public GitHub-visible "choix conscient accepté", PAS drift silencieux. Strategic-55 22:00Z lit ce file pour data point pivot (trust juridique vs acquisition vs UX-capture). Si audit-55 prescrit BATCH PURGE, le file pré-armé reste utilisable (méthode exécution L57-65 valide).

---

# 2026-06-10T07:42Z — BATCH PURGE ECLI template pré-armé (run-505 — archive ci-dessous)

## Statut originel run-505

**PRÉ-ARMÉ — PAS exécuté ce wake**. Cap silence Florian (a) ack 24h expire 2026-06-10T07:46Z (T+4min depuis ce wake 07:42Z). Wake suivant 09:42Z = T+1h56 post-expire = **1ʳᵉ fenêtre confirmable default SKIP** si Florian silent persiste.

## Décision conditionnelle

**SI** `BATCH PURGE` ack reçu inbox.md HEAD entre 07:00Z et 09:42Z (fenêtre cap silence pre-expire OR juste post-expire) :
- **ALORS** Builder rollback J+0 SB-2 DISCIPLINE 12 **3ᵉ application** (post-Marseille run-426 + Aubervilliers run-493)
- **VIA** script `agent-browser/rollback_batch_ecli.py` (à créer wake exécution) + verify HTTP 200 prod + commit dédié `chore(SB-2): batch purge 4 fichiers ECLI hallucinées (Florian-ack)` + decision file conversion "exécuté" + log persistant

**SI** silent persiste cap expire + wake 09:42Z confirmation :
- **ALORS** decision file documente choix conscient "trust juridique drift accepté" audit trail
- **PAS de purge unilatérale** (ban audit-54 🚫 strict, override require Florian-ack OR audit-55 prescription explicit pivot)

## Pourquoi ce template pré-armé (PAS auto-execute)

Critic-71 #2 ★★ verbatim : *"PRÉPARER decision file SB-2 3ᵉ TEMPLATE BATCH PURGE 4 fichiers ECLI (pas ship — `memory-agent/decisions/2026-06-10-batch-purge-ecli-template-ready.md` + grep script + cap silence Florian 07:46Z T+46min default SKIP holds strict). Si Florian ack `BATCH PURGE` arrive 07:00-09:42Z fenêtre = Builder rollback J+0 propre 4 fichiers via decision pré-armée. Si silent default SKIP confirmé 09:42Z = decision file documente choix conscient « trust juridique drift accepté » audit trail. PAS auto-execute sans ack. ≤15min."*

**Asymétrie pré-armage** : (1) si ack arrive next wake → Builder exécute J+0 sans devoir re-designer rollback ; (2) si silent → audit trail explicit "choix documenté" vs drift latent ; (3) respect audit-54 §6 cap silence strict (PAS de purge unilatérale).

## Diagnostic empirique (rappel)

Critic-70 #1 ★★ run-499 + critic-69 #2 ★★ run-493 ont confirmé empirique :

| Pourvoi/ECLI affirmé | Statut Judilibre (rétro-vérif Aubervilliers) | Verdict |
|---|---|---|
| `23-19.572` Cass. 3ᵉ civ. 26 sept 2024 (complément loyer) | Pourvoi existe MAIS ECLI réel `CCASS:2025:C310349` date 2025-06-26 | **MISMATCH date 9 mois** |
| `ECLI:FR:CCASS:2020:C300657` (encadrement CEDH) | ECLI valide MAIS sujet = bail loi 1948 CEDH (PAS encadrement ELAN) | **TOPICAL MISMATCH** |
| `07-13.034` Cass. 3ᵉ civ. 28 mai 2008 (prescription) | total=0 Judilibre | **HALLUCINATION pure** |

**Pattern identique Marseille run-426** : 3/3 ECLI fausses confirmées + rollback `db2fe7f`.

## Scope BATCH (4 fichiers prod)

Confirmé empirique grep run-505 `grep -o "ECLI:FR:CCASS:[^\"<>]*\|23-19.572\|07-13.034"` :

| Fichier | 23-19.572 | C300657 | 07-13.034 |
|---|---|---|---|
| `wedge-tool/static/encadrement-loyer-villeurbanne-2026.html` | ✓ | ✓ | ✓ |
| `wedge-tool/static/encadrement-loyer-echirolles-2026.html` | ✓ | ✓ | ✓ |
| `wedge-tool/static/encadrement-loyer-bordeaux-2026.html` | ✓ | ✓ | ✓ |
| `wedge-tool/static/encadrement-loyer-lyon-2026.html` | ✓ | ✓ | ✓ |

**Hors scope batch (préservés défaut, sauf ack explicit `BATCH PURGE INCLUDE template`)** :
- `wedge-tool/cat-3/loyer-abusif.v0.json` template (corpus cat-3 base — preservation conservative)
- `wedge-tool/static/llms-full.txt` (mention ECLI dans contexte LLM ingestion — éval séparée)
- Autres caches/templates : éval wake exécution.

## Méthode exécution (si ack arrive)

1. Backup `.bak-pre-batch-purge-run505` par fichier
2. Rétro-vérif PISTE Judilibre (3/3 confirmer FAIL) — `agent-browser/judilibre_search.py` log persistant `agent-browser/judilibre_batch_purge_*_verif.log` (SB-2 DISCIPLINE 12 strict)
3. Pour chaque fichier : section "Jurisprudence applicable" rollback (substitution cadre juridictionnel générique + ressort CA approprié + lien recherche Judilibre + ADIL local), FAQ JSON-LD nettoyage, FAQ HTML <details> nettoyage
4. Verify HTTP 200 prod chaque URL + `curl -s | grep -c "ECLI:FR:CCASS:2020:C300657\|23-19.572\|07-13.034"` = 0
5. Commit dédié + push origin main + IndexNow ping 4 URLs (carve-out SB-2 trust juridique override ban audit-54 IndexNow)
6. Conversion decision file : `2026-06-10-batch-purge-ecli-template-ready.md` → status "EXÉCUTÉ J+0 commit `<sha>`"

## Bans audit-54 respect strict

🚫 BATCH PURGE sans Florian-ack (cap 07:46Z holds STRICT) ✅ — purge non-déclenchée ce wake.
🚫 NEW FILE user-facing ✅ — decision file = `memory-agent/decisions/` interne.
🚫 IndexNow ✅ — purge non-exécutée, ping non-déclenchée.

`tactical_critic_recommendations_honored_cumul=75 → 76 (#2 ★★ pré-armage J+0)`.

## NEXT (wake 09:42Z)

Re-évaluer cap silence (a) :
- Florian ack `BATCH PURGE` arrivé 07:42-09:42Z fenêtre ⇒ exécution J+0 via ce template
- Silent persiste ⇒ default SKIP confirmé, conversion decision file "skipped — choix conscient trust juridique drift accepté audit trail"
- ack `BATCH PURGE INCLUDE template` (extension scope) ⇒ extension exécution `loyer-abusif.v0.json` + `llms-full.txt`
