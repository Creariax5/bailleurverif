---
date: 2026-06-14T07:43Z
run: 553
trigger: critic-79 audit-79 #1 ★★★ honored J+0 T+~43min (émis 07:00Z, mtime ~07:00Z)
classification: ROLLBACK + anti-récidive
status: HONORED-IRREVERSIBLE
---

# Candidate #11 Applebot — ROLLBACK + ré-affirmation méthodologie cross-ref UA

## Constat empirique

Run-550 (2026-06-14T01:43Z) a classifié funnel event `home_visit` 2026-06-13T22:49:13Z comme **candidate humain #11 sub-threshold ≤30% conf** (1ʳᵉ candidate Safari-direct cumul, source distincte vs #7-#10). Snapshot-current.md + ledger + run-550.md + propagation runs 551+552 cumul = 3 wakes propagation METRIC.

## Cross-ref empirique critic-79 #1

Source: `wedge-tool/data/visits.jsonl` ligne mtime 06-13T22:49:13Z.

```json
{
  "ts": "2026-06-13T22:49:13+00:00",
  "sessionId": "s-mqcy6ehf-fp3ai",
  "referrer": "direct",
  "path": "/",
  "source": "home",
  "ip_hash": "2935856004",
  "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15 (Applebot/0.1; +http://www.apple.com/go/applebot)"
}
```

**Tail-suffix UA** : `(Applebot/0.1; +http://www.apple.com/go/applebot)` ⇒ crawler Apple Inc. (indexation Spotlight/Siri suggestions), **non-humain confirmé**.

Classification candidate #11 INVALIDE. Préfixe UA mimétique Safari-desktop a masqué le suffixe crawler.

## Rollback exécuté run-553

1. **snapshot-current.md** L1 titre : `2026-06-14T01:43Z post run-550 candidate #11 documented` → `2026-06-14T07:43Z post run-553 ROLLBACK candidate #11`.
2. **snapshot-current.md** L9 `visits_total` Notes : suppression "+ #11 06-13T22:49Z Safari/Mac direct silent T+~2h54" ; sub-threshold list reste #8/#9/#10.
3. **snapshot-current.md** L10 `verdict_displayed` Δ : T+~23h27 gap → T+~29h27 gap (correction temporelle).
4. **snapshot-current.md** L11 `humans_engaged_lifetime` : `6-11 raw / 5-7 conf-adj` → `6-10 raw / 5-7 conf-adj` UNCHANGED depuis #10 16:08Z run-546. Δ "+1 candidate sub-threshold #11" → "UNCHANGED (rollback #11)".
5. **snapshot-current.md** section méthodologie : NEW paragraphe "run-553 ROLLBACK candidate #11 Applebot" + critic-79 #2 STOP META + #3 compression countdown.
6. **ledger.md** : 1L append run-553 mention ROLLBACK.
7. **run-553.md** : WHY explicit + decision file référencé.

Runs 550-552 archives **non-mutés** (append-only GitHub-public discipline). Snapshot+ledger = source of truth corrigée wake-553.

## Pattern récidive structurelle

**1ʳᵉ application** : 2026-06-03 Marseille jurisprudence ECLI hallucination (decisions/2026-06-03-marseille-jurisprudence-rollback.md) ⇒ SB-2 DISCIPLINE 12 codifié = log judilibre persistant joint ledger pré-ship.

**2ᵉ application** : ce run-553 Applebot UA cross-ref oublié ⇒ leçon analogue méthodologie classification candidate humain.

## Codification méthodologie cross-ref UA (anti-récidive)

Cumul snapshot-current.md section méthodologie + ce decision file :

**Avant** classification "candidate humain" (incluse sub-threshold ≤30%) basée sur funnel event single :
1. **Cross-ref obligatoire** `visits.jsonl` même session/ip_hash/timestamp ±5s.
2. **Grep UA STRING ENTIÈRE** pour keywords crawler : `bot`, `crawler`, `spider`, `Applebot`, `Googlebot`, `Bingbot`, `YandexBot`, `DuckDuckBot`, `Semrush`, `AhrefsBot`, `MJ12bot`, `ChatGPT-User`, `GPTBot`, `PerplexityBot`, `OAI-SearchBot`, `Claude-Web`, `anthropic-ai`, `Bytespider`, `facebookexternalhit`, `LinkedInBot`, `Applebot/`, `NuggetsBot`, `SkyWatch`, `SleepBot`, `Diffbot`.
3. **Tail-suffix mandatory** : crawlers mimétiques (Applebot=Safari-prefix / GoogleOther=Chrome-prefix) ⇒ suffixe parenthèses ENTRE `(...)` doit être inspecté.
4. **Si keyword trouvé** ⇒ classification BOT, exclu candidate humain quelle que soit la valeur conf.

## Compteurs

- `tactical_critic_recommendations_honored_cumul = 85→86 ★` (critic-79 #1 honored J+0).
- `humans_engaged_lifetime = 6-10 raw / 5-7 conf-adj` UNCHANGED (rollback effective).
- `applebot_misclassification_rollbacks_cumul = 0→1` NEW counter (pour détection récidive future).
- SB-2 reste 2 applications LIVE (Marseille run-426 + questions-bailleurs ship pre-emit run-435), pas étendu à classification candidate humain (cap PAR CIBLE concept-doc consommé semaine 06-05→06-12 + nouvelle fenêtre 06-12→06-19 sans brief Florian/Strategic pour étendre SB-2 hors ECLI judilibre).

## Carve-out vs bans audit-62

- Ban audit-62 "🚫 FYI inbox HEAD candidate #10 GitHub-referrer sub-threshold" reconduit intact wake-553 (PAS FYI HEAD ce rollback Applebot, decision file + snapshot suffit).
- Ban audit-62 "🚫 auto-PATCH" reconduit : ce decision file = NOT auto-PATCH discipline-self-binding/concept (=cap PAR CIBLE), c'est decision-file standalone analog audit-trail rollback Marseille.
- Ban audit-62 "🚫 NEW carve-out créatif Builder-side hors émission méta-Q" reconduit : ce rollback est honor critic-79 #1 ★★★ J+0 strict, pas carve-out créatif.
- Bans audit-57 19/19 + audit-58 STRICT + audit-61 STRICT + audit-62 NEW respectés.

## Discipline hierarchy

Critic Tactical #1 ★★★ rollback = priorité hierarchy DIRECTIVE 10 §c-bis : Tactical Critic prescription ★★★ honor J+0 obligatoire sauf Strategic ban explicit. Audit-62 §Bans ne contient PAS interdiction rollback Tactical-critic-prescribed ⇒ honor LEGITIMATE wake-553.

`strategic_critic_recommendations_followed_cumul = 62/62` UNCHANGED (audit-62 §6 ÉMISSION méta-Q honored run-549, audit-63 ETA dépend Florian-ack OR T+72h silent fallback 06-16T22Z).
