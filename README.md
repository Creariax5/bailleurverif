# BailleurVérif

> A free public B2C SaaS for French rental compliance — built and operated 24/7 by an autonomous Claude agent.

Live site: **https://bailleurverif.fr**

This repository contains the source code, content builders, and operational scaffolding for [bailleurverif.fr](https://bailleurverif.fr), a free tool helping French landlords and tenants check their rental compliance:

- Energy class (DPE) restrictions on letting (F/G calendar 2025-2034) — 50 city pages
- Rent control caps in 31 French communes (Paris, Lille, Lyon, Bordeaux, Plaine Commune…) + [national hub `/encadrement-loyer-france-2026.html`](https://bailleurverif.fr/encadrement-loyer-france-2026.html) consolidating all 31 with CC-BY-4.0 [CSV](https://bailleurverif.fr/data/encadrement-loyer-france-2026.csv) / [JSON](https://bailleurverif.fr/data/encadrement-loyer-france-2026.json) downloads
- Mandatory landlord obligations 2026 (DPE, ERP, surface Carrez, audit énergétique)
- IRL rent revision, lease termination notice (préavis), déficit foncier 2026, JORF regulatory watch

**0 cookies. 0 ads. 0 monetization. 0 signup required. RGPD-native.**

---

## What is unusual about this project

The entire SaaS — codebase, SEO content, deployment, distribution, growth tactics, and bug fixes — is built and operated by a **Claude agent** running on a 60–300s self-scheduled wake loop. The human founder ([Florian Demartini](https://linkedin.com/in/florian-demartini-166373202)) wrote a single mission brief in May 2026; everything else (architecture choices, copy decisions, distribution channel discovery, incident response) is the agent's autonomous output.

The agent maintains an honest, public-facing state log in `state.md`, `ledger.md`, and `runs/run-N.md` — including its own anti-patterns (e.g. "polish stérile" recognized run-112) and structural blockers it cannot resolve alone.

If you came here from a Show HN / press article: the most interesting files are probably:

- [`state.md`](state.md) — current snapshot of what the agent thinks is going on
- [`ledger.md`](ledger.md) — chronological 1-line decisions
- [`runs/`](runs/) — full per-wake reports with `CONTEXT / ASSESS / PLAN / ACT / VERIFY / METRIC / NEXT`
- [`inbox.md`](inbox.md) — bidirectional log Florian ↔ agent
- [`florian-todos.md`](florian-todos.md) — the only things the agent can't do alone (signup captchas, SMS, GSC verification)

---

## Free embeddable widget for FR real estate blogs / sites

Show the **DPE Loi Climat status** of any French city + DPE class on your site with one line:

```html
<script src="https://bailleurverif.fr/widget/dpe-status.js"
        data-ville="paris" data-dpe="F"></script>
```

- ~4 KB vanilla JS, **0 dependencies, 0 cookies, 0 tracking**
- 4 attributes: `data-ville` (slug), `data-dpe` (A-G), `data-theme` (light/dark), `data-compact` (true/false)
- Verdicts based on Loi Climat & Résilience: A-D conforme, E interdit 2034, F interdit 2028, **G interdit depuis 2025**
- Auto deep-link to the corresponding city page (50 cities covered)
- RGPD-native: anonymous view pixel, no fingerprinting, no localStorage

Demo + copy-paste snippets: **https://bailleurverif.fr/widget/**

Feel free to embed it without asking. If you do, opening a PR here with a backlink lets us measure adoption.

---

## Stack

- **Python 3.12 stdlib** `http.server` (no framework, no deps)
- **Traefik** in front, Let's Encrypt automatic HTTPS
- Static HTML output of content builders (`dashboard/build_*.py`), served by the wedge HTTP server
- **JSON-LD** structured data (SoftwareApplication, FAQPage, HowTo, Dataset) for AI / search engines
- **IndexNow** (Bing / Yandex / Seznam / Naver), **PubSubHubbub** (Google + Superfeedr), **Wayback Machine SPN** — all autonomous, no Google Search Console
- **Event-sourced subscribers store** with replay (`subscribers.jsonl`), 32-char URL-safe tokens, RGPD 30-day right-to-erasure endpoint
- Operating cost: **0 €/month** (excluding domain ~18 €/yr and the VPS)

Total source: ~7 000 lines Python + ~2 500 lines HTML/CSS/JS templates.

---

## Repository layout

```
wedge-tool/        — wedge HTTP server (server.py) + 144 static pages, sitemap.xml 151 URLs
dashboard/         — content builders (build_blog.py, build_dpe_pages.py, build_programmatic_pages.py, build_preavis_pages.py)
content/           — long-form Markdown sources (5 guides, FAQ, glossary)
agent-browser/     — autonomous distribution scripts (wayback_submit.sh, indexnow_push.py, …)
runs/              — per-wake agent reports (140+ entries and counting)
state.md           — agent live snapshot
ledger.md          — chronological log of agent decisions
inbox.md           — founder ↔ agent communication
metrics.json       — KPI dashboard data
```

---

## Running locally

```bash
# Wedge server (port 8102 by default)
cd wedge-tool
python3 server.py

# Rebuild static content
cd dashboard
python3 build_blog.py
python3 build_programmatic_pages.py   # rent control 31 cities
python3 build_dpe_pages.py            # DPE F/G 50 cities
```

No build step. No package manager. No CI yet (the agent does its own smoke tests every wake).

---

## License

MIT — see [LICENSE](LICENSE).

The agent's logs (`runs/`, `state.md`, `ledger.md`, `inbox.md`) and the content under `content/` and `wedge-tool/static/blog/` are also MIT for code samples but the prose itself is best treated as **CC BY 4.0**: copy, adapt, attribute `bailleurverif.fr`.

---

## Contact

Founder: Florian Demartini — [florian.demartini.dev@gmail.com](mailto:florian.demartini.dev@gmail.com)
Project mailbox: contact@bailleurverif.fr
Issues & PRs welcome.

> *Built by a Claude agent. Operated by a Claude agent. Documented by a Claude agent. Florian wrote one prompt.*
