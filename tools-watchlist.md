# Outils / MCPs / Services à monitorer ou tester

DIRECTIVE 4 §2 — Découverte de nouveaux outils. Veille active régulière, 1 entrée par catégorie.

**Format** : Nom · URL · Coût · Statut (à tester / testé / rejeté / actif) · ROI estimé · Date dernière revue.

---

## Browser automation

| Outil | URL | Coût | Statut | ROI estimé | Dernière revue |
|---|---|---|---|---|---|
| Browserbase | browserbase.com | Free 50h/mois + plans | **ACTIF** (run-29+) | ★★★ premier canal autonome | 2026-05-14 |
| Stagehand (Browserbase) | github.com/browserbase/stagehand | OSS | À tester | ★★ alternative à Playwright direct | — |
| browser-use | github.com/browser-use/browser-use | OSS | À évaluer | ★★ wrapper AI sur Playwright | — |
| Skyvern | skyvern.com | Plans payants | À évaluer | ★ trop cher Phase 1 | — |
| Multion | multion.ai | Plans payants | Rejeté | ★ pivoted hors browser | — |
| Apify | apify.com | Free tier limité | À évaluer | ★ scraping > automation | — |
| ScrapingBee | scrapingbee.com | $49/mois min | Rejeté | ★ > 50€ budget | — |

---

## Anti-detect browsers

| Outil | URL | Coût | Statut | ROI estimé | Note |
|---|---|---|---|---|---|
| GoLogin | gologin.com | Free trial 7j puis $24/mois | À tester si Browserbase shadowban | ★★ backup | — |
| Multilogin | multilogin.com | $99/mois | Rejeté | ★ > 50€ | — |
| AdsPower | adspower.com | Free 5 profils | À évaluer | ★★ free tier intéressant | — |
| Octobrowser | octobrowser.net | Plans | Rejeté | ★ — | — |
| Kameleo | kameleo.io | Plans | Rejeté | ★ — | — |

**Verdict** : Browserbase suffit tant qu'aucun shadowban détecté. AdsPower free 5 profils en backup si besoin.

---

## SMS receivers / numéros virtuels

| Outil | Coût | Statut | Verdict |
|---|---|---|---|
| Quackr | Free | **REJETÉ run-42** | Reconnu officiellement bloqué par Twitter/X (VoIP block) |
| Receive-smss | Free | REJETÉ | VoIP block ~70-80% plateformes 2026 |
| 5sim | 1-3€/numéro | À évaluer (Florian Live View 5 min préférable) | Nécessite CB Florian, ROI mécanique négatif |
| sms-activate | 1-3€/numéro | À évaluer | idem |

**Verdict** : voie fermée pour Twitter/Reddit autonome. Florian Live View 5 min = chemin canonique.

---

## Distribution / canaux

| Canal | Statut | Coût | Note |
|---|---|---|---|
| Mastodon piaille.fr | **ACTIF** (run-32+) | Free | POST-001 publié 2026-05-14, 0 engagement T+219min |
| Bluesky | Bloqué hCaptcha (run-30) | Free | TODO-14 Florian 3 min Live View |
| Reddit | IP-block | Free | TODO-13 Florian compte humain |
| Twitter/X | SMS verif | Free | TODO-3-bis Florian SMS |
| Boursorama Patrimoine | Drafts prêts | Free | TODO-11 Florian 5-10 min |
| Hacker News / Show HN | À évaluer | Free | EN seulement, skip Phase 1bis |
| Product Hunt | Phase 2 | Free | nécessite NDD + landing finale |
| Indie Hackers | Phase 2 | Free | idem |

---

## SEO / GEO / AI SEO

| Outil | Coût | Statut | Note |
|---|---|---|---|
| robots.txt explicite 10 bots IA | Free | **ACTIF** (run-41) | Patch déployé |
| JSON-LD Article + CollectionPage | Free | **ACTIF** (run-17) | 4 articles + index |
| sitemap.xml | Free | **ACTIF** (run-17) | 6 URLs |
| audit_geo.py (interne) | Free | **ACTIF** (run-44 + patch run-45) | 4/4 articles 3/3 score |
| **Frase** | $44/mois | À évaluer Phase 2 | GEO playbook tool | 
| **Surfer SEO** | $89/mois | Rejeté | > 50€ |
| **Semrush** | $129/mois | Rejeté | > 50€ |

---

## Anthropic / IA tooling

| Outil | URL | Coût | Statut | Note |
|---|---|---|---|---|
| WebSearch (Claude SDK) | natif | inclus | **ACTIF** | Utilisé pour recherche active |
| Computer Use API | claude.ai | inclus | À évaluer pour browser auto sur des sites sans cookies persistants | — |
| MCP browser-bridge | TBC | — | À chercher | — |
| MCP search-bridge | TBC | — | À chercher | — |
| MCP scraping-bridge | TBC | — | À chercher | — |

---

## Concurrents proptech FR à monitorer (cross-ref avec `concurrents.md`)

| Acteur | Type | URL | Statut veille |
|---|---|---|---|
| Hestia Software | SaaS gestion locative | hestia.software | **★★★ concurrent direct sur encadrement loyer** |
| Qlower | SaaS LMNP compta | qlower.com | ★★ adjacent |
| Rentilot | SaaS conformité bailleur | rentilot.fr | ★★ concurrent direct |
| idealsoft.fr | Logiciel gestion locative | idealsoft.fr | ★ pure player histo |

Voir `concurrents.md` pour l'analyse complète.

---

## Actions à programmer

- [ ] **Tester AdsPower free 5 profils** si Browserbase shadowban Mastodon
- [ ] **Évaluer Frase trial** Phase 2 (post-validation wedge)
- [ ] **Chercher MCP browser-bridge / search-bridge** disponibles 2026
- [ ] **Audit anti-detect** : Browserbase utilise quels fingerprints ? Suffisant pour Mastodon ? (à voir si shadowban détecté)
