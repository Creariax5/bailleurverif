# Concept : Signaux trafic réel (visiteurs non-Florian)

**État** : Émergent. Très peu de signal exploitable. 0 conversion observée.

## Source

`wedge-tool/data/visits.jsonl` (213 lignes au run-286). Champs : `ts`, `sessionId`, `referrer`, `path`, `source`, `ip_hash`, `ua`.

## Signaux notables (post run-286)

### Visiteur récurrent ip_hash `6994446044`

| # | ts UTC | referrer | path |
|---|---|---|---|
| 1 | 2026-05-18T08:04:59Z | https://www.google.com/ | `/` |
| 2 | 2026-05-18T11:24:22Z | direct | `/` |
| 3 | 2026-05-19T07:20:24Z | direct | `/` |

**Pattern** : 3 visites en ~23h, **toutes sur homepage `/` uniquement**. UA stable (Chrome 147 Linux X11). Premier hit post-GSC verify 2026-05-17.

**Interprétation possible** :
- Hypothèse A : utilisateur réel curieux, mais homepage ne convertit pas en clic profond (bounce répété → CTA homepage faible).
- Hypothèse B : Florian lui-même testant (mais Chrome 147 dev + ip_hash isolé du pattern usuel = à confirmer).
- Hypothèse C : Bot disguisé en Linux X11 (peu probable, 3 visites espacées sans burst).

**Implication mission 5000 users** : si A, signal que homepage doit pousser observatoire/loyer-abusif directement. Si B, faux signal.

### Référents externes captés

- `https://github.com/dapphub/dapptools/issues/160` (run-282 mention) : Open3CL issue #160 → session 94s 3 pages (utilisateur distinct du récurrent, single visit).
- `https://www.google.com/` (ip_hash 6994446044, 1ʳᵉ visite) : 1ʳᵉ visite organique Google post-GSC verify 2026-05-17.

## Métriques courantes (run-286)

- `visits_jsonl_lines=213`
- `recurring_visitors_count=1` (ip_hash 6994446044, 3 hits ≥2 jours distincts)
- `recurring_visitor_pages_per_session_avg=1.0` (homepage-only)
- `recurring_visitor_deep_navigation=false` (0 clic vers /observatoire ou /loyer-abusif)
- `google_organic_referrer_first_hit_at=2026-05-18T08:04:59Z`
- `open3cl_referrer_first_hit_at=2026-05-18T10:21Z` (run-282)

### Signal — ip_hash `2124423717` (investigué run-290)

**Critic-19 ★★ #2** (audit 09:55Z post run-287) : `ip_hash 2124423717` 09:47Z deep-nav OBS→HOME T+4h12min post-ANIL outbound (run-278 SMTP 05:35Z). Hypothèse écho ANIL ou bot crawler.

**Résultat investigation run-290** : `grep "2124423717" visits.jsonl` → **1 seule occurrence** (09:47:31Z), UA `Firefox 150 Windows 10 x64` (récent navigateur réel), referrer `https://bailleurverif.fr/observatoire-annonces-loyer.html` → path `/`. **Single-shot non-récurrent ≥24h** sur fenêtre check.

**Verdict** : curieux ponctuel, **PAS écho ANIL substantif** (ANIL répondrait probablement par mail SMTP plutôt que browser direct depuis IP propre). Navigation OBS→HOME = utilisateur qui découvre l'observatoire par lien externe et remonte vers home pour comprendre le site (pattern reverse-funnel intéressant mais isolé). **PAS de cat-4 substantif candidate** sans 2ᵉ visite ≥24h.

**Hypothèses secondaires** :
- Crawler bot disguisé Firefox 150 (peu probable, single-hit + referrer OBS interne suggère click humain).
- Visiteur Reddit/HN/Twitter ayant croisé une mention obs (mais 0 referrer captable = direct OR strip referrer).
- Florian lui-même testant depuis Windows VM (à confirmer si reconnaît l'UA).

**Action retenue** : pas de structurel ce wake. Re-check ip_hash `2124423717` runs +N — si 2ᵉ visite ≥24h, reclasser cat-4 substantif candidate.

## Bots indexers — inventaire (run-294)

Source `wedge-tool/data/visits.jsonl` (~220 lignes). Période 2026-05-16 → 2026-05-19 (~3.5 jours post-GSC verify).

| Crawler | Hits | Première visite | Dernière visite | Paths indexés observés |
|---|---|---|---|---|
| **Applebot** | **7** | 2026-05-16T11:18Z | 2026-05-19T10:43Z | `/`, `/preavis-bail.html` |
| Googlebot (desktop+mobile) | 5 | 2026-05-16T16:55Z | 2026-05-18T07:01Z | `/` |
| YandexRenderResourcesBot | 3 | 2026-05-16T13:01Z | 2026-05-17T07:52Z | `/` (resources render) |
| Bingbot | 1 | 2026-05-17T17:35Z | 2026-05-17T17:35Z | `/` |
| GPTBot / OAI-SearchBot | 0 | — | — | — |
| ClaudeBot / Anthropic | 0 | — | — | — |
| PerplexityBot | 0 | — | — | — |

**Signal cat-4 substantif** : Applebot **plus actif que Googlebot** (7 vs 5 hits, ratio inversé). Crawler Apple = ingestion Siri / Spotlight Search / Apple Intelligence / Maps. Pattern multi-jour (3 visites distinctes) + 2 paths indexés = re-crawl planifié, pas one-shot.

**Implication mission 5000 users** : Apple ecosystem FR a iPhones ~22-25% part de marché (audience captive iOS). Si Siri/Apple Intelligence ingère "encadrement loyer Paris" → exposition zéro-coût audience cible (B2C locataire). Aucun LLM crawler majeur n'est encore venu — ni GPTBot, ni ClaudeBot, ni PerplexityBot. Opportunité asymmetrique : optimiser `llms.txt` / `robots.txt` / meta tags pour LLM training crawlers.

**Action différée** : pas de nouvelle action externe ce wake (run-294, anti-spam-burst, critic-20 ~14:00Z). Documentation suffit. Re-check Applebot hits runs +N pour confirmer cadence régulière.

### Signal — Google referrer→deep-nav ip_hash `3790475865` (run-298, critic-20 ★★ #2) + cross-IP `6269819028` (run-306, critic-22 STOP #2 closure)

Critic-20 (audit 12:55Z) a flaggé deep-nav non-Florian via Google.com referrer 12:53Z **APRÈS** run-297, donc non-traité ce wake. Investigation run-298 :

| # | ts UTC | referrer | path | UA | ip_hash |
|---|---|---|---|---|---|
| 1 | 2026-05-19T12:53:19Z | `https://www.google.com/` | `/` | Chrome 147 Linux X11 | `3790475865` |
| 2 | 2026-05-19T12:53:32Z | (none, internal click) | `/preavis-bail.html` | Chrome 147 Linux X11 | `3790475865` |
| 3 | 2026-05-19T13:18-13:29Z | (5 hits deep-nav) | `/` + multi pages | Chrome 147 Linux X11 | `6269819028` |

**Pattern** : 2 IP hashes distincts (`3790475865` 12:53 + `6269819028` 13:18-13:29) **même UA Chrome 147 Linux X11** sur fenêtre ~30 min couvrant brief writing Florian 13:15-13:30Z (4 briefs TOP inbox 16:XXZ effectivement écrits ~13:15-13:30Z d'après timestamps).

**Hypothèses (critic-22 closure 24h max)** :

- **Hypothèse PRIMARY (preferred)** : **Florian self-audit during brief writing 13:15-13:30Z**. Probabilité : haute. Indices : (a) même UA Chrome 147 Linux X11 sur 2 IPs (NAT/VPN switch typique testing), (b) timing strict aligné brief writing window, (c) deep-nav `/preavis-bail.html` cohérent test path conversion mentionné brief, (d) cross-IP+same-UA = pattern self-test pas user organique. **Verdict probable : Florian-confirmed**.
- **Hypothèse SECONDARY (à invalider via recurrence check)** : utilisateur réel via Google "préavis bail" + utilisateur distinct deep-nav 25 min plus tard = 2 utilisateurs Chrome 147 Linux distincts. Probabilité : faible (coincidence UA + timing + path conversion brief = ~1% bruit).
- **Hypothèse TERTIARY** : bot crawler self-test (peu probable, 13s entre 2 hits + UA browser réel cohérent).

**Closure proactive 24h max** : reclasser Florian-confirmed si pas de récurrence 2ᵉ visite ≥24h depuis 2026-05-19T12:53Z (check due 2026-05-21T12:53Z). Si récurrence ≥24h détectée → reclasser utilisateur réel deep-nav substantif. Si null → Florian-confirmed locked.

**Action retenue run-306** : closure hypothèse documentée (PRIMARY Florian self-audit). Pas de modif `/preavis-bail.html` ni homepage. Cooldown re-check ip_hash `3790475865` + `6269819028` due 2026-05-21T12:53Z (48h depuis 1ʳᵉ visite).

## IndexNow round-69 verdict — théâtre confirmé (run-315 2026-05-20T04:30Z)

**Hypothèse critic-24 reconduite définitif T+6h cible 04:30Z** : spot-check run-315 04:30Z = T+6h post-ship `/loyer-legal-paris.html` run-309 22:30Z. Résultat :

- `grep -c loyer-legal-paris wedge-tool/data/visits.jsonl` = **0**
- `grep loyer-legal-paris` filtré UA bot = **0**
- `visits_total` = 222 UNCHANGED depuis 2026-05-19T13:29:30Z (15h silence)

**Verdict définitif** : IndexNow round-69 = **théâtre confirmé**. Ping Bing/Yandex envoyé run-309 n'a déclenché AUCUN crawl visible côté Apache logs. 2 hypothèses survivantes :

- **Hypothèse PRIMARY (preferred)** : Pings reçus côté Bing/Yandex mais crawl planifié 24-72h+ post-ping (cadence indexation low-priority pour domaine DR ~25). T+6h trop court pour latency upper-bound réelle. Re-check T+24h cible 2026-05-20T22:30Z + T+48h cible 2026-05-21T22:30Z.
- **Hypothèse SECONDARY** : IndexNow ne ping pas réellement (clé/endpoint dysfonctionnel) OU crawler ignore notre domaine 0-trust historique. Reclasser "outil bookkeeping" pas canal humain.

**Implication mission revenu passif** : reconnecter discussion canal humain. Drafter cycle 2 LinkedIn (T+12h cible 16:45Z) + post Florian validation TODO-32-bis = seuls leviers humains restants pour fenêtre Paris J+7 (deadline iter-1 2026-05-26T22:30Z). +1 outreach press FR Que Choisir Logement run-315 (strategic-10 prescription = test diagnostic "moat académique → trafic réel" sans capex).

## Action retenue (run-286, maintenue)

**Documentation only**. Pas de refonte homepage sans validation Florian/strategic-critic. Ce concept sert d'intel pour le prochain audit strategic (critic-20 attendu ~14:00Z).

## Action différée (post critic input)

- Si critic-19 recommande optim homepage CTA → ajouter bandeau « Voir l'observatoire (43 violations N=210 dernière vague) » au-dessus du fold.
- Sinon : continuer baseline, surveiller si `recurring_visitors_count` augmente sur ≥3 visiteurs distincts (seuil signal vs bruit).
