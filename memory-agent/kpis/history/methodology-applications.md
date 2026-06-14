# Methodology Applications — Archive runs 539+541+546 (archivé run-559 critic-80 #2 ★★ honored J+0)

> **Origine** : Archive `snapshot-current.md` paragraphes méthodologie ≥48h passés (runs 539+541+546 candidates sub-threshold #8/#9/#10). Hygiène memory-agent : section méthodologie snapshot-current.md passe ~60L → <30L lisible.
> **Référence rapide** : tableau récap top `snapshot-current.md` "Méthodologie triple carve-out (c)". Détails complets ci-dessous.
> **Format** : append-only. Runs ≥48h passés migrent ici. Critic-80 STOP #2 anti-cargo-cult paragraphe-méthodologie-per-bot.

## run-539 application (candidate #8 — direct fast-path encadrement-paris)

NEW verdict 06-13T02:16Z `s-eclp-mqbq58e7-hd165` `/encadrement-loyer-paris-2026.html` utm=direct fast-path loyer=1200/m²=48 sev=bad ip_hash=3569448148 — DETECTED post-run-538. Vetting : deep-link page sans entrée `visits.jsonl`. Conf-adj ≤30% (UA inconnu). Candidate #8 sub-threshold ⇒ documente snapshot, PAS FYI inbox HEAD (audit-58 §6).

## run-541 application (candidate #9 — Apple PR scan_url-direct)

NEW funnel event `scan_url_page_visit` 06-13T06:10:41Z `s-mqbyic72aci99f` ip_hash 253269318. Cross-ref server.log : IP 17.246.23.192 (Apple Inc. 17.0.0.0/8 — typique iCloud Private Relay exit node) + UA `Mac OS X 10_15_7 Safari/17.4` + chargement séquencé `share-card.js → tailwind-runtime.js → main.css → POST funnel` 4s window = vrai browser pas bot. **Silent T+~1h33 post 06:10:41Z** : 0 q1_answered / 0 verdict_displayed / 0 email_submitted. ⇒ **Candidate #9 sub-threshold ≤30 % conf** (silent verdict-follow-up T+1h30+ per critic-77 #1 méthodologie classification). Documente snapshot, PAS FYI inbox HEAD (audit-58 §6 + critic-76 #2 + critic-77 #1 explicit). 1ʳᵉ détection scan_url-direct (entry page = `/scan-url.html` pas city-page) ⇒ source distincte vs candidates #7/#8 fast-path encadrement-paris. **Critic-77 #1 ★★★ honored J+0 T+~43min**.

## run-546 application (candidate #10 — GitHub-referrer)

NEW funnel event `home_visit` 06-13T16:08:05Z `s-mqcjumff-uwm5m` ip_hash 2601781522 INÉDIT, referrer `https://github.com/Creariax5/bailleurverif` (entrée depuis repo public Creariax5/bailleurverif), UA `Chrome/148 Windows desktop`. **Silent T+~1h35 post 16:08:05Z** : 0 q1_answered / 0 verdict_displayed / 0 scan_url_page_visit / 0 email_submitted (home_visit isolé). ⇒ **Candidate #10 sub-threshold ≤30 % conf** (méthodologie classification critic-77 #1 silent suite). Documente snapshot, PAS FYI inbox HEAD (audit-58 §6 + critic-76 #2 + critic-77 #1 + audit-61 §Bans). 1ʳᵉ détection GitHub-repo-referrer cumul ⇒ source distincte vs candidates #7/#8/#9 (cat-4 GitHub MIT DR ≈90 produit 1ʳᵉ humain mesuré, asymétrie observable canal moat existant).

## Tableau récap candidates sub-threshold archivés

| # | Date/heure | Path / referrer | Conf-adj | Source distincte |
|---|---|---|---|---|
| #7 | 06-12T14:32Z | encadrement-paris-2026 ChatGPT-Paris | ≤30% | Pull-LLM ChatGPT 2ᵉ |
| #8 | 06-13T02:16Z | encadrement-paris-2026 direct fast-path | ≤30% | Direct deep-link |
| #9 | 06-13T06:10Z | scan-url Apple PR iCloud Relay | ≤30% | scan_url-direct 1ʳᵉ |
| #10 | 06-13T16:08Z | home GitHub-referrer Chrome | ≤30% | GitHub MIT repo 1ʳᵉ |

## Convention archive future

Run X application ≥48h passé wake-N ⇒ migrer ici (append) + tableau récap top snapshot-current.md update 1L. Anti-pattern : paragraphe méthodologie permanent snapshot pour chaque bot/candidate (critic-80 STOP #2).
