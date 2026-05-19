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

## Action retenue (run-286)

**Documentation only**. Pas de refonte homepage sans validation Florian/strategic-critic. Ce concept sert d'intel pour le prochain audit strategic (critic-19 attendu ~11:00Z OR audit strategic-7 ≥2026-05-20T04:35Z).

## Action différée (post critic input)

- Si critic-19 recommande optim homepage CTA → ajouter bandeau « Voir l'observatoire (43 violations N=210 dernière vague) » au-dessus du fold.
- Sinon : continuer baseline, surveiller si `recurring_visitors_count` augmente sur ≥3 visiteurs distincts (seuil signal vs bruit).
