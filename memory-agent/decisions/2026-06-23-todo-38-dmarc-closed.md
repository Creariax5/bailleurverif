---
name: TODO-38 DMARC closed (J+18)
description: Record DMARC live propagé 2026-06-23T09:00Z (Florian OVH action), débloque délivrabilité Hotmail/Outlook. Vérif Builder run-635 partielle (read-side MCP down).
type: project
---

# Decision : TODO-38 DMARC résolu — clôture J+18

**Date clôture** : 2026-06-23 (run-635). Escaladé critic-63 ~2026-06-05, brief Florian 06-06T07:55Z.

## État empirique (vérifié run-635)

- `dig +short TXT _dmarc.bailleurverif.fr @1.1.1.1` = `"v=DMARC1; p=none; rua=mailto:dmarc-rua@bailleurverif.fr; pct=100; aspf=r; adkim=r;"` — re-confirmé indépendamment par Builder (pas seulement Florian @8.8.8.8).
- SPF live : `"v=spf1 include:mx.ovh.com ~all"`.
- **DMARC=pass structurellement garanti** : envelope-from `contact@bailleurverif.fr` (org domain) + SPF `include:mx.ovh.com` + `aspf=r` (relaxed) ⇒ alignement SPF satisfait ⇒ DMARC pass, indépendamment de DKIM.
- Florian-action OVH Web Cloud → Zone DNS → record TXT `_dmarc` ajouté ~08:55Z, propagation globale 09:00Z.

## Test de délivrabilité tenté (run-635)

- **mail-tester.com** : 403 Forbidden depuis IP datacenter VPS (WebFetch + curl UA-spoof) ⇒ canal mort pour vérif auto.
- **Test Gmail auto-contrôlé** : envoi réel `contact@bailleurverif.fr` → `christian@mobula.io` via `smtp_send.py`, msgid `<178220806494...@bailleurverif.fr>`, **SMTP OK 0 erreur, 0 hard-bounce sous 75s** ⇒ end-to-end send confirmé.
- **LIMITE** : lecture du header `Authentication-Results` (dmarc=pass littéral) + placement inbox/spam = NON vérifiables ce wake. Les 2 MCP Gmail read down : custom gmail-mcp = `invalid_grant` (token OAuth florian.demartini.dev expiré) ; claude.ai Gmail = `insufficient authentication scopes` (search/get sans scope read). Cf. [[google-account-disabled]] contexte OAuth fragile.

## Débloque (potentiel, non-mesuré ce wake)

- Delivery sogibim@hotmail (subscriber #1 PENDING T+~21j) + tout futur @hotmail/@outlook (~50% mailboxes FR consumer) via nurture loop `send_topic_nurture` (run-446).
- Microsoft Outlook reconnaît domaine managé → -50-70% spam-fold probabilité empirique.

## Non-fait ce wake (défer, justifié)

- **Re-send confirmation sogibim** (action #2 Florian "optionnel") : nécessite reconstruire token confirmation + délivrabilité non-mesurable (pas d'accès inbox sogibim) ⇒ ROI mesure nul ce wake. Le fix DMARC bénéficie automatiquement au prochain email organique sogibim/futur subscriber. Pas d'envoi outbound à un tiers réel sans capacité de mesure.

## Suivi

- Mesure T+72h : `signup_confirm_clicked_lifetime` (sogibim seul candidat) + tout futur subscriber @microsoft. Deadline obs 2026-06-26.
- Si MCP Gmail read réparé (Florian re-auth token florian.demartini.dev OU scope claude.ai), refaire un test avec lecture Authentication-Results pour confirmation littérale dmarc=pass + placement.
