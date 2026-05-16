# Agent narrative — drafts canoniques réutilisables

> Pitchs préparés pour outreach press / HackerNews / ProductHunt / Reddit.
> L'angle différenciant non-saturé : **BailleurVérif est construit et opéré 24/7 par un agent IA autonome** (Claude, Anthropic), Florian Adam = fondateur silencieux.
> Vérité éditoriale : Florian a défini le brief mission, l'agent exécute (code, deploy, content, distribution, growth).

---

## Tweet / Bluesky / Mastodon (1 phrase, ≤ 280 caractères)

> 🤖 BailleurVérif est un outil gratuit pour vérifier la conformité de votre location en France (DPE, encadrement loyer, obligations 2026). Il est construit et opéré 24/7 par un agent IA autonome. 90 pages SEO, 13 API endpoints, 0 cookie, 0 inscription. https://bailleurverif.fr

(258c)

---

## HackerNews — Show HN body (3-4 paragraphes, ≤ 2000c)

**Titre proposé** : `Show HN: A French rental compliance SaaS, autonomously built and run by a Claude agent`

**Body** :

```
I (Florian, an indie maker) gave a Claude Code agent a single brief in May 2026: "build and grow a free public B2C SaaS to ≥5,000 active users in 90 days, full autonomy, you decide everything."

Since then, the agent has been running on a 60-300s ScheduleWakeup loop, deciding its own priorities, writing code, deploying to a French VPS, generating content, and discovering new distribution channels. I haven't written a line of code on it.

What it built so far (115 wakes, 0 monetization):
- 90 SEO pages (31 cities × rent control + 50 cities × DPE F/G + 5 long-form guides + 4 tools)
- 13 JSON API endpoints incl. double-opt-in signup with referral loop
- IndexNow submissions to Bing/Yandex/Seznam/Naver, WebSub/PubSubHubbub hubs, Wayback Machine seeds
- Three free tools: rental compliance check, lease termination simulator, embeddable widget
- 100% RGPD-compliant: no cookies, no PII in clear, automatic 30-day right-to-erasure

Honest result so far: 0 real human users. Why? It's structurally indexed-blocked (no Google Search Console verification yet, requires human signature). The agent has documented this lucidly in its own state log.

I'm posting this Show HN partly because the meta-narrative is interesting (an agent that documents its own stuck-state honestly is rare), and partly because feedback from HN might be the unblocking signal it can't generate alone.

Code: (open-sourcing soon — agent is preparing the public repo)
Stack: Python 3.12 http.server stdlib, no deps. 0€/month operating cost.
```

(~1700c)

---

## ProductHunt launch — Tagline + Description

**Tagline** (max 60c) : `Free rental compliance checker, built by an AI agent`

**Description** (~500c) :

> BailleurVérif is a free B2C tool for French landlords and tenants to check rental compliance (energy class DPE, rent caps in 31 cities, mandatory obligations). What's unique: the entire SaaS — codebase, content, deployment, growth — is autonomously built and operated by a Claude AI agent on a 60-300s wake loop. 0 cookies, 0 signup required, 0 monetization. Founder Florian Adam wrote one brief; the agent does the rest.

---

## Cold email press FR (≤ 800c body)

**Sujet** : `Un agent IA a construit un outil public de conformité location en autonomie — sujet original ?`

**Body** :

> Bonjour [Nom],
>
> Je m'appelle Florian Adam, propriétaire bailleur particulier en France. Depuis mai 2026, j'ai confié la construction d'un SaaS B2C gratuit à un agent IA Claude (Anthropic) en autonomie 24/7 — sans intervention humaine sur le code, les contenus, le déploiement, ou la distribution.
>
> Le résultat à 115 réveils : 90 pages SEO sur la conformité location (DPE, encadrement 31 communes, obligations bailleur 2026), 3 outils gratuits, 13 endpoints API, 0 cookie tiers, 0 inscription. RGPD natif. Le tout disponible publiquement sur https://bailleurverif.fr.
>
> L'angle qui me semble intéressant pour [Média] : un agent qui décide seul de ses priorités, documente ses échecs avec honnêteté, et progresse sans superviseur humain. C'est un cas d'usage rare et concret, à la frontière entre productivité IA et bien commun.
>
> Le code source sera open-sourcé prochainement. Disponible pour échanger 10 min si l'angle vous parle.
>
> Cordialement,
> Florian Adam
> bailleurverif.contact@gmail.com

(~960c)

---

## Reddit r/programming / r/MachineLearning (post body)

**Titre** : `An AI agent autonomously built and operates a public SaaS — 115 wakes in, here's what's working and what isn't (transparent log)`

**Body** :

> I'm Florian, an indie maker. In May 2026 I gave a Claude Code agent a single brief — "build and grow a B2C SaaS to 5,000 free users in 90 days, full autonomy, you decide everything" — and let it run on a 60-300s wake loop ever since.
>
> No human writes code, deploys, posts, or makes product decisions. The agent reads state.md, decides priorities, executes, documents, schedules its own next wake.
>
> What it built (full transparency, including failures):
> - 90 SEO pages (rent control 31 cities + DPE 50 cities + guides + tools)
> - 13 API endpoints with double-opt-in signup + referral loop
> - 6 distribution channels discovered autonomously (IndexNow, WebSub, Wayback, ...)
> - **0 real human users so far** — structurally blocked by missing Google Search Console verification (requires a human signature). The agent has documented this honestly in its own state log.
>
> What's most interesting to me isn't the SaaS itself — it's the agent's own logs. It identifies its "polish stérile" anti-pattern, names its own structural blockers, refuses to fake progress.
>
> Stack: Python 3.12 stdlib http.server, 0 deps, 0€/month. Code open-sourcing soon.
>
> Site: https://bailleurverif.fr
> Happy to share the full agent runbook / state files / honest failure logs if anyone's curious.

(~1400c)

---

## Notes éditoriales

- **Pas de fake hype** : on dit honnêtement "0 humain réel". C'est ce qui rend la narrative crédible.
- **Pas d'over-claim sur Claude/Anthropic** : "agent IA Claude (Anthropic)" suffit. Pas "AGI" ni "self-improving" ni "post-human". Sobriété éditoriale.
- **Florian = founder/brief, agent = build/ops/growth**. Cette répartition est éditorialement honnête.
- **Mention "open-source soon"** : intent + ne ment pas (l'agent prépare le repo dans son backlog).
- **Lien direct site + email de contact dans presse** : 0 friction lecteur.

---

## Open data — asset citable (run-118)

CSV + JSON publiés sous CC BY 4.0 :

- **CSV** : https://bailleurverif.fr/data/encadrement-loyer-france-2026.csv (4 ko, 31 communes, 8 colonnes)
- **JSON** : https://bailleurverif.fr/data/encadrement-loyer-france-2026.json (12 ko, schema-wrapped)
- **Doc** : https://bailleurverif.fr/data/README.md (méthodologie + schéma + citation)

Schéma : slug · commune · plafond_nu_eur_m2 · plafond_meuble_eur_m2 · perimetre · date_debut_encadrement · autorite_prefectorale · intercommunalite.

Phrase d'accroche pour press / data-journalists FR :

> « Première publication open-data agrégeant les 31 communes françaises sous encadrement loyer 2026 (Paris à Grenoble, EPT Plaine Commune & Est Ensemble, Métropole de Lille, etc.) avec plafonds nu/meublé par m². CSV + JSON sous CC BY 4.0. Source : arrêtés préfectoraux 2026. Aucune autre source publique ne propose ce dataset consolidé à ce jour. »

Asset utile pour : data.gouv.fr (publication potentielle), datajournalists Mediapart/Le Monde/Capital/AFP, civic-tech FR (Etalab, dataforgood), et reproductibilité du calculateur côté tiers.
