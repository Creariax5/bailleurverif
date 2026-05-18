# Bugs & issues connues

## Bug latent #16 — 2026-05-18T02:30Z — FIXÉ run-242

**Symptôme** : 86% des `/api/visit` records (164/190 lifetime) avaient `path=""` et `source=""` → impossible de mesurer conversion par page.

**Root cause** : 50 pages SEO `*-dpe-f-g-interdit-location.html` envoyaient au handler un body `{src:"dpe_simulator", classe:c, ville:"X"}` au lieu de `{path, source}`. Handler `server.py:1060-1070` fait `data.get("path") or ""` → enregistre vide.

**Fix** : sed -i sur 50/50 pages, body passe `{path: location.pathname, source: "dpe_simulator", classe:c, ville:"X"}`. Prod sert version fixée (curl Lille OK). 0 restart (static files).

**Effet attendu** : à partir de run-242, série temporelle `path` valable pour audit funnel par page SEO.

---

Aucun produit en code → aucun bug technique pour l'instant.

---

## Conventions / contrats à respecter (gotchas non-bug)

- `leads.jsonl` : un lead par ligne, JSON. Champs minimum :
  ```json
  {"id":"lead-001","sourced_at":"2026-05-13T...","source":"finary|reddit|linkedin|other","source_url":"https://...","persona":"bailleur 1 bien / multi-bien / LMNP","handle_or_alias":"...","public_signal":"phrase qu'ils ont écrite qui les qualifie","contact_method":"public-post|dm|email-pending","status":"sourced|contacted|replied|call-scheduled|call-done|positive|negative|ghost","notes":"..."}
  ```
- Pas de PII en clair dans les commits/fichiers. Pour ce qui est public (handle Finary, post URL), c'est OK. Email/tel = chiffré ou hors fichier git.
- `runs/run-{ISO}.md` : 1 fichier par réveil, jamais d'écrasement.
- Tous les ports libres VPS sont dans 8100-8200 (UFW). Trading bot intouchable dans `/home/deploy/Autonomous trading bot/`.

## Blocages d'accès web (run-6, 2026-05-13)

| Source | Statut accès agent | Bloqueur observé | Mitigation |
|---|---|---|---|
| forum.quechoisir.org (thread individuel) | OK (run-3, run-4) | — | Continue |
| forum.quechoisir.org/location-f178 (index) | **404 run-5** | URL slug changé ou forum réorganisé | run-6 : testé /location → 404 et /immobilier-f12 → 404. Forum réorganisé. Drill-down only via Google site:. Acter perte source S2 (index). |
| forum.quechoisir.org/diagnostic-immobilier-f176/ (index) | **404 run-5** | idem | idem |
| investisseurs-heureux.fr (thread individuel) | **403 run-5** (avait été OK run-3) | Cloudflare durci | TODO-7 (Florian colle les URLs ET le contenu) |
| investisseurs-heureux.fr (index) | 403 depuis run-4 | Cloudflare | idem TODO-7 |
| reddit.com (via WebFetch direct) | 403 (run-3) | Cloudflare anti-bot | run-6 : old.reddit.com testé → **bloqué côté agent** ("unable to fetch"). Idem r/vosfinances et r/immobilier. Reddit définitivement inaccessible en autonome. |
| finary.com / community.finary.com | 403 / login | Login requis | TODO-2 (Florian colle URLs et contenu) |
| linkedin.com | login | Login requis | TODO-3 |
| pap.fr | 403 (run-3) | Cloudflare | — |
| **boursorama.com/patrimoine/forum/immobilier** | **OK run-6** ✨ | — | **Nouvelle source S6 ajoutée**. Densité bailleur 13-17% (vs 5% quechoisir). **Limite** : pseudos anonymisés (M2244825 type) = non contactables hors-forum, seul C1 (commentaire dans thread) possible. |
| forum.hardware.fr/immobilier | **404 run-6** | Forum réorganisé ou page test invalide | À retenter avec une URL plus précise si motivé |
| forum-juridique.net-iris.fr | **ECONNREFUSED run-6** | Hôte down ou changement DNS | À déprio |
| universimmo.com/forum (ancien) | **HTTP 200 mais archive figée 2009** (run-7) | Forum migré, ancien gelé | Inexploitable pour sourcing 2026 |
| universimmo.com/forum_universimmo/ (nouveau) | **HTTP 500** (run-7) | Plateforme cassée ou en maintenance | À retenter dans 1-2 mois, sinon source morte |
| leblogpatrimoine.com/immobilier | **HTTP 200** (run-7) | — | Blog, pas de lead contactable. Utile uniquement pour veille marché / inspiration SEO. Pas une source S-N |
| pap.fr/conseils/ | 403 run-7 (idem run-3) | Cloudflare | TODO Florian (potentiel C1 sur commentaires articles) |

**Conclusion run-6** : Une nouvelle source autonome a été trouvée (Boursorama forum patrimoine immobilier) avec densité bailleur ~3x supérieure à quechoisir, mais les pseudos sont anonymisés (M2244825 type) ce qui restreint l'outreach au C1 in-forum (pas de DM, pas d'enrichissement hors-Boursorama). Sources fraîches (avr 2026) limitées : 5-6 threads bailleurs sur 30, dont 1 marginal qualifiant (LEAD-003 ajouté). **Le mur sourcing autonome reste réel mais respire un peu** : Boursorama peut servir de source de relance C1 toutes les 2-3 semaines (rythme de threads bailleurs visible). Ne remplace pas TODO-1 / TODO-7.

**Conclusion run-7** : Test universimmo.com (réputé historiquement gros forum bailleurs FR) → ancien forum gelé en 2009 (4264 sujets dans la section "Appel à expériences similaires bailleurs" mais dernier message juillet 2009), nouveau forum HTTP 500 = inaccessible. Source morte. **Verdict consolidé après run-5/6/7** : sources autonomes saturées à 1 source active (Boursorama) de rendement modeste (~1-2 leads qualifiants/mois). Aucune nouvelle source de volume n'est trouvable côté agent — l'effort de recherche n'a plus de ROI. Le levier dominant reste TODO-1/7/8 (actions Florian). Pivot consolidé : production stock SEO Phase 2 + monitoring bi-mensuel Boursorama.

## Risques RGPD à surveiller

- Sourcing depuis Finary/Reddit = info publique mais usage commercial = base légale "intérêt légitime" à documenter. Préférer signal opt-in (réponse à post utile) que cold email.
- Cadastre + LeBonCoin = données publiques mais cross-référence peut être qualifiée de traitement disproportionné. À étudier avant d'industrialiser.
