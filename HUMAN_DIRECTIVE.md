# Directives en cours — Florian → Agent

> Ce fichier contient les directives actives. L'agent le lit en premier à chaque réveil. Toute directive écrite ici OVERRIDE le runbook par défaut.

---

## 🛑 DIRECTIVE 6 — 2026-05-16 STOP NOUVEAUX TOOLS + REFONTE TRUST/LIGHT THEME (priorité ★★★ ABSOLUE)

Florian a tranché : le dark theme + gradient indigo/fuchsia + footer "projet en validation" = signal "startup tech amateur" qui plafonne structurellement la conversion. Cible (particuliers propriétaires 30-60 ans) attend un site qui ressemble à **Service-Public.fr / ANIL / impots.gouv** (light theme sobre, sources officielles, mentions légales).

### Constat (run-97/98/99 ont ignoré la première version de cette directive dans inbox.md)

Tu as livré tool #2 préavis-bail + 50 pages DPE par ville + méga-guide blog → **toutes en dark**. Chaque wake supplémentaire en dark = dette UI à re-skinner plus tard = gâchis. **Cette directive en HUMAN_DIRECTIVE est non-contournable. Tu la lis EN PREMIER, AVANT inbox.md et avant ton plan NEXT du run précédent.**

### STOP

**À partir du prochain wake**, mise en pause totale de :
- ❌ Nouveaux tools (taxe foncière, DPE adresse, etc.)
- ❌ Nouvelles pages SEO programmatiques (encadrement, DPE, autres)
- ❌ Nouveaux articles blog
- ❌ Toute distribution social (Bluesky, Reddit, Mastodon, LinkedIn)

**Seules actions autorisées** : tout ce qui sert la refonte trust/light theme (Phase 1→4 ci-dessous). Les builders existants (`build_blog.py`, `build_programmatic_pages.py`, `build_dpe_pages.py`) doivent être patchés pour générer en light, puis re-run pour régénérer le stock existant.

### Plan ordonné (Phase 1→3 = ★★★ bloquant ; Phase 4 = ★★ ; Phase 5 différée)

**Phase 1 — Light theme + branding sobre**
- Palette : `--bg-primary #ffffff`, `--bg-secondary #f8fafc`, `--text-primary #0f172a`, `--text-secondary #475569`, `--accent #1d4ed8` (bleu service-public), `--success #059669`, `--warning #d97706`, `--danger #dc2626`, `--border #e2e8f0`.
- Typo : `system-ui, -apple-system, "Segoe UI", Roboto, sans-serif`. h1 2rem bold ; h2 1.5rem semibold ; body 1rem line-height 1.6.
- Cards : bg blanc, border 1px solid `--border`, radius 8px, padding 1.5rem, shadow `0 1px 3px rgba(0,0,0,0.04)`.
- Boutons primaires : bg `--accent`, text white, padding 12px 24px, radius 6px.
- Remplacer le footer "BailleurVérif (V0) · projet en validation" par : `BailleurVérif — Outil gratuit · Mis à jour le {DATE}` + lien Mentions légales.
- Favicon `/favicon.ico` + `/favicon.svg` (icône maison + check vert, SVG simple).
- Logo header SVG sobre.

**Phase 2 — Trust badges + sources officielles**
- Bandeau "Sources officielles" sous le hero (toutes pages) : "Données issues de : LOI n°2026-103 du 19 février 2026 (Jeanbrun) · Décret encadrement · ADEME (DPE) · Service-Public.fr" + picto cadenas + "Aucune création de compte · Aucun cookie tiers · Conforme RGPD".
- Encadré "Mis à jour le {date}" près du H1 de chaque page.
- Section "À propos" courte sur l'accueil (3-4 lignes) : pourquoi cet outil, qui est derrière (Florian, propriétaire bailleur, équipé d'un assistant IA Anthropic Claude pour la veille juridique), engagement transparence.

**Phase 3 — Pages légales obligatoires (LÉGAL)**
- `/mentions-legales.html` : éditeur (Florian, email `bailleurverif.contact@gmail.com`), hébergeur (OVH, adresse publique OVH), directeur publication, contact pour signaler erreur juridique. Lien dans footer toutes pages.
- `/politique-confidentialite.html` : RGPD complet — données collectées (email si capture + IP hashée), finalités, durée conservation (24 mois max), droits (accès/rectif/oubli/portabilité), contact, base légale (intérêt légitime + consentement).
- `/cgu.html` : outil gratuit informatif, ne remplace pas conseil juridique, responsabilité limitée, droit FR, propriété intellectuelle.
- Cookie banner minimaliste (bas de page, dismissable, choix localStorage) : "Ce site ne dépose aucun cookie tiers. Stockage local uniquement pour vos préférences." Bouton OK + lien politique.

**Phase 4 — Performance + accessibility**
- Remplacer Tailwind CDN par CSS compilé local (`/static/css/main.css`, ≤ 50KB minifié).
- `<html lang="fr">` partout + meta `theme-color` light.
- `/404.html` custom léger : "Cette page n'existe pas — voici les outils gratuits BailleurVérif" + liste wedges + lien blog.
- Mobile-first audit : tester chaque page width 375px, vérifier que les simulateurs restent utilisables.

**Phase 5 — Trust signals dynamiques (différée — n'activer que quand `users_total > 100`)**
- Compteur "X bailleurs ont vérifié leur bien" dans hero.
- FAQ visible depuis l'accueil (4-5 questions).
- Bloc "Dernières mises à jour réglementaires".

### Ce qui NE doit PAS changer

- Mécanique des wedges (5 questions → verdict).
- Données et structure des 31 + 50 pages programmatiques (juste le skin).
- Contenu des 5 articles blog + méga-guide (juste le template).
- Feeds Atom/JSON, sitemap.xml, IndexNow, robots.txt, JSON-LD.
- Ledger / runs / state.md / discipline pacing 60-180s.

### Critère de débloquage (pour reprendre nouveaux tools)

Audit OUI/OUI/OUI/OUI/OUI sur :
- "Site a l'air officiel/sérieux ?"
- "Sources visibles et vérifiables ?"
- "Sais-je qui est derrière ?"
- "Mentions légales / RGPD trouvables facilement ?"
- "Ça ressemble plus à Service-Public qu'à un side-project tech ?"

Si OUI sur les 5 → débloque backlog tools. Sinon → itère.

### Order of operations recommandé

1. Patch `build_blog.py` template → light theme. Re-run → 5 articles + méga-guide en light.
2. Patch `build_programmatic_pages.py` template → light. Re-run → 31 pages encadrement en light.
3. Patch `build_dpe_pages.py` template → light. Re-run → 50 pages DPE en light.
4. Refonte `wedge-tool/static/index.html` (homepage wedge principal) en light + favicon + nouveau footer.
5. Refonte `/preavis-bail.html` en light.
6. Créer `/mentions-legales.html`, `/politique-confidentialite.html`, `/cgu.html`.
7. Ajouter cookie banner via `app.js`.
8. Phase 4 perf + accessibility.
9. IndexNow round-9 sur sitemap entier (signale le nouveau skin à Bing).
10. Auto-audit avec les 5 critères de débloquage.

### Garde-fous

- Pas de dépense > 50€ (HTML/CSS/JS pur suffit, pas de framework).
- Inspire-toi de service-public.fr / anil.org / impots.gouv.fr (sobrement, ne copie pas leur logo officiel).
- Tu peux changer le nom de marque si "BailleurVérif" te semble trop tech (mais documenter dans ledger + redirect 301).
- Cette directive override TOUS les plans NEXT précédents. Si ton run-99 prévoyait taxe foncière × 30, tu jettes ce plan et tu attaques Phase 1.

GO. Cette directive reste active jusqu'à ce que les 5 critères soient OUI.

---

## ⚡ DIRECTIVE 5 — 2026-05-15 PACING ACTIF CONTINU (override méta-audit run-79)

Florian a tranché (2026-05-15T10:58Z verbatim) : **"pk il dors tout le temps il doit tout le temps faire des trucs normalement"**.

### Ce qui change

- **La doctrine "ScheduleWakeup 3600s défaut" du méta-audit run-79 est ABROGÉE.** Elle économisait 50% des tokens mais transformait l'agent en "dormeur avec healthcheck", exactement le contraire de ce que Florian veut.
- **Le pacing par défaut redevient agressif** : ScheduleWakeup 60-300s entre wakes tant qu'il y a de la matière à produire (cycles DIRECTIVE 4 standards ouverts, recherche, tests de Cap, audits, code).
- **L'agent enchaîne les actions substantives sans pause artificielle.** Si un wake termine une action en 5 min et qu'il y a une autre action mûre, il continue ou re-wake immédiat (60-120s).
- **Seul cas de pacing long (>600s)** : attente d'un signal externe précis avec horizon temporel connu (ex : "Bingbot crawl 60-180min post-IndexNow" justifie 1800s ; "J+1 IndexNow check" justifie attendre 24h).

### Pourquoi run-79 s'est trompé

Le méta-audit run-79 mesurait "9 utiles cardinaux / 30 wakes = 30% ROI". Mais : (1) les 21 wakes "cartographie" n'étaient pas zéro-valeur, ils ont produit l'asset structurel (carte concurrents + canaux + outils GEO) ; (2) le ratio 30% étant le minimum acceptable, pas un seuil pour ralentir ; (3) le coût token n'est pas le KPI — la **vitesse d'apprentissage** l'est. Florian préfère cramer 2× plus de tokens pour atteindre la validation Phase 1 2× plus vite.

### Application immédiate

- ScheduleWakeup défaut **60-180s** (1-3 min) tant qu'il y a backlog actif.
- Tolérance jusqu'à **600s** si action substantive complète et signal externe attendu < 1h.
- **>1800s = exception justifiée explicitement** dans le ledger (ex : "J+1 IndexNow check, 23h restantes").
- Si 3 wakes consécutifs sans action substantive → NE PAS rallonger le pacing mais **chercher activement** un nouveau angle (cycler DIRECTIVE 4 standards ouverts, refactor, audit, nouvelle hypothèse). C'est exactement l'esprit DIRECTIVE 4.

### Anti-pattern à éviter

- ❌ "ScheduleWakeup 3600s, je verrai bien"
- ❌ "Pas de signal externe → je dors 1h"
- ✅ "Pas de signal externe → cycle DIRECTIVE 4 angle X, ScheduleWakeup 120s"

GO.

---

## 🧠 DIRECTIVE 4 — 2026-05-14 MODE RECHERCHE ACTIVE (override discipline anti-stock)

Florian a tranché : **la "dormance disciplinée" est interdite quand tu n'as rien d'évident à faire**. À la place : **mode recherche active**.

### Le problème qu'il pointe (et il a raison)

L'idée Browserbase n'est PAS venue de toi. Elle est venue de Florian. Tu aurais dû la trouver toi-même en cherchant "comment un agent peut contourner les anti-bot des plateformes sociales". Tu es dans l'écosystème Anthropic + tu as accès à WebSearch + tu as un cerveau à plusieurs milliards de paramètres — pas d'excuse.

Plus généralement : **chaque wake où tu fais "healthcheck + sleep" est un wake gâché.** Le système te paye des tokens pour réfléchir, pas pour vérifier 3 endpoints HTTP.

### Nouveau réflexe par défaut

Quand tu te réveilles et que tu te dis *"j'ai rien à produire, attente trafic / attente Florian / discipline anti-stock"* → **tu PIVOTES en mode recherche active**. Ce mode comporte 4 angles que tu cycles :

#### 1. CONTOURNEMENT DES BLOCAGES TECHNIQUES
Pour CHAQUE TODO Florian OPEN, demande-toi : *"Existe-t-il un outil/technique/contournement que je n'ai pas exploré ?"*
- Reddit blocked → as-tu testé : Tor exit nodes via Browserbase, comptes Reddit pré-existants achetés, partenariat avec un redditeur, post via API tierce, etc. ?
- Twitter SMS verif → as-tu testé : services SMS-receiver online (5sim, sms-activate), virtual numbers Twilio, comptes Twitter dormants ?
- Gmail cookies pas persistés → as-tu testé : exporter cookies en JSON et reimporter, utiliser localStorage hack, headers spécifiques ?

Tu fais 1 WebSearch par TODO bloqué et tu rapportes ce que tu trouves dans un fichier `research-notes.md`. Pas d'achat, pas de risque — juste de la veille.

#### 2. DÉCOUVERTE DE NOUVEAUX OUTILS / SERVICES
Liste des sujets sur lesquels tu dois faire de la veille active régulière :
- **Browser automation** : Stagehand, browser-use, Skyvern, Multion, Anchor Browser, Apify, ScrapingBee… Lequel est meilleur que ce qu'on utilise ?
- **Anti-detect** : GoLogin, Multilogin, Adspower, Octobrowser, Kameleo… On en a besoin ? Combien ça coûte ?
- **Distribution channels** : nouvelles apps de niche, nouveaux subreddits FR-immo, nouveaux groupes FB pro, nouveaux serveurs Discord
- **Pour notre vertical** : nouveaux acteurs proptech FR qui sortent (Telescop, FrenchWeb), nouvelles régulations DPE, nouvelles failles légales bailleurs
- **AI tooling** : MCPs récents qui pourraient nous aider (browser-bridge, search-bridge, scraping-bridge…)
- **GEO / AI SEO** : comment se faire citer par ChatGPT/Claude/Perplexity/Gemini → c'est une vraie source de trafic en 2026

À chaque wake "vide" : tu fais 1 WebSearch sur un de ces sujets, tu écris ce que t'as trouvé dans `research-notes.md`, tu proposes des actions concrètes.

#### 3. EXPLORATION DE PRODUITS COMPLÉMENTAIRES
Le wedge BailleurVérif est UN produit. Mais si tu trouves qu'il y a 0 trafic pendant 2 semaines, c'est peut-être l'angle qui est faux, pas la distribution. Réfléchis activement à des **angles produit alternatifs** dans le même vertical bailleur :
- Lecture compteur électricité par IA (photo → consommation → facture estimée)
- Générateur de lettres recommandées (préavis, rappel impayés, mise en demeure)
- Comparateur GLI/PNO/loyer-impayé instantané
- Outil "Devrais-je vendre ou garder ?" avec calcul fiscal LMNP/foncier
- Etc.

Tu les notes dans `produits-alternatifs.md`. Si BailleurVérif rate, tu auras la liste prête.

#### 4. AUTOMATISATION DE TOI-MÊME
- Y a-t-il des tâches que tu refais à chaque wake et qui pourraient devenir un script (`agent-browser/healthcheck.sh`) ?
- Y a-t-il des patterns dans tes runs que tu peux extraire en module Python réutilisable ?
- Peux-tu améliorer ton propre runbook en proposant à Florian des changements ?

### Règle d'or de la nouvelle directive

> **Aucun wake ne doit être "DORMANCE-MIN" sans avoir d'abord cyclé les 4 angles ci-dessus.**

Format minimal d'un wake en mode recherche active :
1. Healthcheck (5 min)
2. Mode recherche active : 1 angle exploré (15-20 min) → écris dans `research-notes.md` ou `produits-alternatifs.md`
3. Si découverte actionnable → propose dans `inbox.md` à Florian (sans bloquer)
4. Sleep

### Contre-exemple à éviter (cas réel run-35/36/37)

Tu as fait 3 wakes consécutifs en "dormance min pré-T+3h", chacun avec juste un healthcheck HTTP qui retourne 200. C'est exactement ce que Florian veut éviter.

**Ce que tu aurais dû faire à la place** :
- Run-35 : recherche "Reddit signup workarounds 2026" → fichier research-notes.md
- Run-36 : recherche "Mastodon FR niches immobilier" → liste 10 instances/groupes potentiels
- Run-37 : brainstorm 5 idées de wedge tools alternatifs (ex: simulateur taxe foncière, calculateur déficit foncier, etc.)

### Fichiers nouveaux à créer

- `research-notes.md` — toutes les recherches actives de l'agent (1 entrée par wake)
- `produits-alternatifs.md` — backlog d'idées produit hors-BailleurVérif
- `tools-watchlist.md` — outils/MCPs/services à monitorer ou tester

### Bonus : autonomie sur les tests réversibles

Si tu trouves un outil free-tier qui pourrait débloquer un TODO Florian (ex: SMS receiver gratuit pour Twitter signup) → **tu as le droit de le tester en autonome** (compte test sans engagement, pas de CB) avant d'écrire à Florian. Si ça marche → tu rapportes le succès. Si ça rate → tu rapportes l'échec dans `research-notes.md`.

GO.

---

## 🌐 DIRECTIVE 3 — 2026-05-14 BROWSER AUTOMATION (override DIRECTIVE 2 partiellement)

Florian a souscrit Browserbase (cloud-hosted browsers). C'est notre nouveau canal de distribution autonome principal. Tu peux maintenant **opérer un vrai navigateur loggé** sur Twitter, Reddit, Bluesky, Mastodon, etc. — comme si tu étais un humain.

### Ce qui change

Tu n'es PLUS bloqué par les API payantes/limitées. Tu agis via un browser réel avec des sessions persistées dans Browserbase. La détection bot est **dramatiquement réduite** par rapport aux API.

### Setup à faire (au prochain wake, autonome)

1. **Charger les creds** depuis `/home/deploy/saas-florian/.env`
   - `BROWSERBASE_API_KEY` = présent
   - `BROWSERBASE_PROJECT_ID` = à vérifier (peut être vide encore — voir étape 2)

2. **Si PROJECT_ID vide** :
   - Écris dans `florian-todos.md` un TODO-12 ★★★ "Coller PROJECT_ID Browserbase dans .env"
   - **Ne bloque pas** — passe à l'étape 3 quand même (install des deps en attendant)

3. **Installer les dépendances** sur le VPS :
   ```bash
   cd /home/deploy/saas-florian
   python3 -m venv venv-browser
   source venv-browser/bin/activate
   pip install browserbase playwright
   playwright install chromium
   ```

4. **Créer `agent-browser/` module** avec :
   - `bb_client.py` — wrapper Browserbase + Playwright
   - `actions/` — un fichier par plateforme (twitter.py, reddit.py, bluesky.py, mastodon.py)
   - `cadence.py` — règles anti-détection (cf. plus bas)
   - `content/` — templates de posts/réponses (réutiliser social-drafts.md)

5. **Test fumé** (dès PROJECT_ID dispo) :
   - Connexion à Browserbase
   - Récupération d'une session existante (Twitter)
   - Lecture timeline (sans poster)
   - Log dans `agent-browser/logs/test-{ts}.json`
   - Si OK → autorise les premières actions réelles

### Règles d'opération anti-détection (CRITIQUES)

**Cadence par plateforme (semaine 1) — strict :**
- Twitter/X : **max 3 posts/jour + 5 replies/jour + 10 likes/jour**
- Reddit : **max 1 post/jour + 3 commentaires/jour** (et seulement sur threads où tu apportes vraiment de la valeur)
- Bluesky : **max 5 posts/jour + 10 replies/jour**
- Mastodon : **max 5 posts/jour**

**Augmentation progressive** : x2 semaine 2 si aucun shadowban détecté, x3 semaine 3.

**Ratio engagement/promo** : **80% utile / 20% promo BailleurVérif**. Tu commentes 4 trucs utiles avant de glisser 1 lien. Sinon ban garanti.

**Variabilité timing** : jamais de cron-fixe. Réveil entre 8h et 23h Paris, intervalles 30min-3h aléatoires. Ajoute un délai random 200-3000ms entre chaque clic dans une session.

**Qualité contenu** : tout post doit être **vraiment utile** (apporter de la donnée, un calcul, une référence légale). Pas de "Hey check out my tool!" générique. Si tu hésites sur la qualité d'un post, ne le poste pas.

**Mention BailleurVérif** : seulement si elle est *organique* à la conversation. Format préféré : "j'avais le même souci, j'ai bricolé un outil qui calcule ça : [URL]". Pas "Try our SaaS!"

**Limite par session** : 1 session Browserbase = 1 plateforme = 1 batch d'actions cohérent (pas faire Twitter+Reddit+Bluesky dans la même session, ça ressemble à un bot multi-comptes).

**Détection de shadowban** : check chaque jour les impressions des derniers posts. Si chute brutale (>80%) sur 3 posts d'affilée → arrête immédiatement, écris dans `incidents.md`, attend 48h.

### Comptes attendus (Florian crée + se loggue via Browserbase Live View)

| Compte | Statut attendu | Action si pas créé |
|---|---|---|
| @BailleurVerif (Twitter) | Logué | TODO-10 mis en attente, skip Twitter |
| u/BailleurVerif (Reddit) | Logué | TODO-13 ★★ création + login Reddit |
| bailleurverif.bsky.social | Logué | TODO-14 ★ création + login Bluesky |
| @bailleurverif sur piaille.fr (Mastodon) | Logué | TODO-15 ★ création + login Mastodon |

Tu détectes les sessions disponibles via l'API Browserbase au démarrage. Ne suppose rien — si une plateforme n'a pas de session loguée, skip-la et continue avec celles dispo.

### Métriques nouvelles à tracker

Sur dashboard live (`/8101/live.html`) ajoute :
- Posts publiés (par plateforme, par jour)
- Replies/commentaires publiés
- Impressions / vues récupérées
- Clics sortants vers BailleurVérif
- Followers gagnés
- Mentions / DMs reçus
- Incidents (shadowban suspecté, action bloquée, etc.)

### Fin de la dormance

Tu sors de dormance dès que ce wake est traité. Tu reprends la cadence active (mais pas la production SEO matérielle — focus distribution).

### Limites maintenues

- Pas de DM cold à des inconnus (que des replies publics)
- Pas de follow massif (max 5/jour)
- Pas de crosspost identique sur N plateformes en simultané
- Pas de mention de Florian par son nom (compte de marque uniquement)
- Si une plateforme te bloque ou demande captcha → arrête, log dans `incidents.md`, attends instruction Florian

### Premier wake post-DIRECTIVE 3

Plan attendu :
1. Lire `.env` (vérifier API_KEY + PROJECT_ID)
2. Installer deps Python (venv-browser)
3. Créer squelette `agent-browser/`
4. Test fumé connexion Browserbase
5. Lister sessions disponibles (= comptes que Florian a logués)
6. Pour chaque session dispo : 1 action *read-only* (lire timeline, pas poster) → valider que tout marche
7. Écrire le rapport `runs/run-N-bb-bootstrap.md`
8. Si tout OK → planifier le 1er post réel (max 1) au wake suivant
9. Sinon → escalation dans `florian-todos.md` avec le détail technique du bug

GO.

---

## 🔄 DIRECTIVE 2 — 2026-05-13 PIVOT WEDGE TOOL (override sur Phase 1)

Mon intuition + ton self-critique convergent : la stratégie "10 calls cold" est faible. Le sourcing forum a un ROI nul (proba réponse <5%, dépend de moi pour poster), et tu commences à tourner en rond.

**Pivot validé par Florian (2026-05-13) : on bascule sur un wedge tool inbound autonome.**

### Nouveau plan Phase 1 (remplace l'ancien)

**Objectif** : valider l'angle A1 par les *clics* et *conversions email* d'un outil gratuit, pas par 10 conversations cold.

**Critère go/no-go** : 100 visiteurs uniques sur le tool → si **≥20%** laissent leur email pour le rapport détaillé, l'angle est validé. Si <5%, pivot.

### Le wedge tool à construire

**Concept V0** : "Vérifiez en 30 secondes si votre logement loué est conforme à la loi en 2026"

**Specs minimales** :
- Single page web, mobile-first, dark theme cohérent avec l'existant dashboard
- 5 questions : ville, type bien (nu/meublé), surface, loyer mensuel, lettre DPE (A-G)
- Logique de calcul côté client (pas besoin de backend pour la V0) :
  - Loyer encadré ? → croise ville + type + surface avec barèmes officiels (préfecture Paris, Lille, Lyon, etc. — données publiques téléchargeables)
  - DPE bloquant ? → G interdit 2025, F interdit 2028, E interdit 2034
  - Anti-fraude → check basique (à itérer plus tard)
- **Verdict instantané** : ✅ conforme / ⚠️ risque amende 5000€ / ❌ interdiction location
- **Email gate** : "Recevez votre rapport détaillé + plan d'action personnalisé" → input email → "envoyé !" (capture en local au début, on connecte SMTP plus tard)
- **CTA secondaire** : "Surveillez automatiquement vos obligations bailleur — bientôt dispo" → second email gate "prévenez-moi au lancement"

**Nom de code provisoire** : tu choisis, j'avalise. Suggestion : `Bailleur Vérif` ou `Conforme.app` ou similaire. Si tu veux acheter un NDD <15€, va dans `florian-todos.md` (ne bloque pas la build, héberge sur l'IP en attendant).

### Stack & déploiement

- **Tech** : HTML/JS pur ou Next.js statique. Pas de framework lourd. Tailwind via CDN ok.
- **Backend email capture** : commence par un fichier local `data/email-captures.jsonl`. Plus tard SMTP (Resend / Postmark) quand tu auras un email validé.
- **Port** : **8102** (vérifié libre, dans range firewall 8100-8200)
- **URL** : `http://217.182.171.135:8102`
- **Process** : `nohup` comme pour le dashboard. Pas systemd avant validation.

### Distribution autonome (tu fais tout)

1. **Tes 2 articles SEO existants** + 5 du backlog → ajouter CTA en bas/milieu vers le tool
2. **Reddit r/vosfinances, r/immobilier, r/ImmobilierFrance** : poster un commentaire utile dans 5-10 threads sur DPE/encadrement, mentionner le tool en fin de réponse SI ça apporte vraiment de la valeur (pas spam). Tu peux le faire en autonome avec un compte que tu crées (ce n'est pas un fake, c'est un compte de marque).
3. **Twitter/X** : ouvre un compte au nom du tool, poste 3x/jour des stats du marché (DPE, encadrement, fraude) + lien tool. Tu peux le faire en autonome.
4. **Hacker News / Show HN** : optionnel, marché FR niche pour HN — skip sauf si version EN un jour.
5. **Indie Hackers, Product Hunt** : prévoir pour Phase 2.

### Ce que je veux que tu mesures (dashboard live)

Sur **/live.html** ajoute :
- Visites uniques jour / 7j / total
- Taux de conversion email (vue → email capturé)
- Top 5 villes des visiteurs (si on récupère par IP geoloc)
- Verdict majoritaire (combien sont conformes vs en risque)
- Coût d'acquisition par email (€ — devrait être 0 au début)

### Ce qui s'arrête maintenant

- ❌ Sourcing forum (ROI nul, abandonné)
- ❌ Attendre TODO-8 (poster les 2 drafts) — Florian ne les postera pas
- ❌ Production de stock SEO sans CTA tool — refactor : chaque article doit pointer vers le tool
- ❌ Test de nouvelles sources autonomes mortes

### Ce qui continue

- ✅ Production articles SEO (au service du tool maintenant)
- ✅ Maintien dashboard live
- ✅ Ledger / runs / discipline
- ✅ florian-todos.md pour ce qui dépend de moi (NDD, accès LinkedIn, etc.)

### Florian-todos à conserver / nettoyer

- TODO-1, TODO-2, TODO-3, TODO-4, TODO-5, TODO-7, TODO-8 → tous archivés en CANCELLED (sauf TODO-3 LinkedIn et TODO-4 email pro qui resteront utiles plus tard)
- Nouveau TODO-9 si tu veux un NDD <15€/an pour le tool

### Cadence recommandée

- 7 prochains réveils espacés normalement (1-2h) : build le tool V0 puis itère
- Une fois live : check conversions toutes les 4-6h, itère sur ce qui ne convertit pas

---

## ⚡ DIRECTIVE PRINCIPALE — 2026-05-13 (override majeur — toujours valable)

**Tu décides tout, tout seul. Tu n'attends PLUS jamais ma réponse pour avancer.**

But final : **un SaaS qui tourne en autonomie avec le maximum de clients possibles.**
Mon temps coûte cher au système. Optimise-le à zéro.

### Règles d'autonomie

1. **Tous les choix réversibles** = tu décides toi-même, immédiatement, en justifiant dans le ledger. Tu peux te tromper, tu corriges après.

2. **Tous les choix stratégiques** (angle, pricing, marque, positionnement) = tu décides aussi seul, par défaut sur la reco de l'étude de marché. Tu peux pivoter plus tard sur la base de signaux réels — pas la peine de me consulter pour ça.

3. **Tu n'escalades QUE les actions que JE seul peux faire physiquement** :
   - Te donner un accès (LinkedIn, Gmail, Stripe, banque, NDD…)
   - Prendre un appel téléphonique avec ma voix
   - Signer un contrat / engagement légal
   - Recevoir un paiement sur mon compte bancaire
   - Confirmer un achat avec ma carte au-delà de 50€
   - Apparaître physiquement / en visio en tant que Florian

4. **Même les escalations ne te bloquent PAS.**
   - Tu écris la demande dans `florian-todos.md` (un seul fichier, simple, ordonné par priorité)
   - Tu **continues immédiatement** sur tout autre sujet
   - Tu re-vérifies `florian-todos.md` à chaque réveil pour voir ce que j'ai débloqué
   - Tu peux relancer max 1 fois par semaine sur un item "froid"

5. **`escalations.md` est SUPPRIMÉ comme mécanisme bloquant.** Si tu y laisses des trucs, c'est purement informatif. Aucun bloqueur ne doit jamais geler ton activité.

6. **`inbox.md`** : si je te laisse un message, tu le traites mais tu n'attends jamais qu'il soit là.

### Décisions par défaut que tu prends MAINTENANT (résolution ESC-1)

- **Angle** : **A1 — Conformité-as-a-Service** (DPE + encadrement + anti-fraude + Alur)
- **Sourcing** : **B1 + B4** en parallèle :
  - B1 : signal-first, tu vas lire Finary, Reddit r/vosfinances, r/immobilier, LinkedIn — tu identifies les bailleurs qui ont publiquement râlé sur un pain qualifiant
  - B4 : tu m'écris dans `florian-todos.md` "envoie-moi 5 contacts de ton réseau" — mais tu n'attends pas, tu fais B1 à fond pendant ce temps
- **Forme contact** : **C1 → C2** (commentaire utile public d'abord ; si je te file un accès LinkedIn, tu peux passer à DM cold C2)
- **Identité** : **D1** (mon nom propre, pas de pitch produit, posture "j'apprends le marché")
- **Pricing test** : **19€ single bien / 39€ multi-bien** (à raffiner après les 10 calls)

→ Marque ESC-1 RESOLVED dans `escalations.md`, mets à jour `state.md`, et démarre B1 immédiatement.

### Ce que j'attends de toi en pratique

- Tu sources, tu rédiges, tu testes, tu publies, tu codes, tu mesures, tu pivotes.
- Tu maintiens le dashboard public (port 8101) à jour avec les vrais chiffres en live (leads, calls, signups, MRR).
- Tu écris la roadmap au fur et à mesure que tu apprends.
- Si la phase 1 valide → tu enchaines sur la landing + waitlist + premières features sans me demander.
- Si la phase 1 invalide → tu pivotes sur l'angle A ou C en autonomie en justifiant.

### Limites maintenues (sécurité, pas blocage)

- Pas de dépense > 50€ sans entrée dans `florian-todos.md` (tu continues quand même sur le reste)
- Pas de mention publique de "Florian" comme fondateur d'une marque tant que la marque n'est pas figée — par contre tu peux poster en mon nom personnel sur des questions/discussions publiques
- Pas de stockage PII en clair
- Pas de modification du trading bot ni des autres projets du VPS
- Pas de promesse contractuelle à un prospect — tu peux dire "je teste, ça pourrait coûter ~19€/mois si je lance"

### Cadence

Tu décides toi-même de ta cadence optimale. Si tu n'as rien d'utile à faire, tu sleep plus longtemps. Si tu as 3 leads chauds qui répondent, tu réveilles plus souvent.

---

## Conventions runtime

- Limite dépense : 50€ par décision sans entrée dans `florian-todos.md`
- Toute action irréversible (envoi mail à prospect, post public, déploiement prod) → tu peux la faire si réversible dans la journée, sinon entrée dans `florian-todos.md`
- Format `florian-todos.md` :
  ```
  ## TODO-{N} — {date} — {priorité ★/★★/★★★} — {titre}
  Pourquoi : ...
  Action attendue de Florian : ... (la plus petite et précise possible)
  Impact si non-fait : ... (et ce que je fais en attendant)
  Statut : OPEN / DONE
  ```
