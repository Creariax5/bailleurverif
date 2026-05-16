#!/usr/bin/env python3
"""Audit factuel du funnel wedge — distingue visites bot vs humain réel.

Usage:
    python3 wedge-tool/audit_funnel.py [--json]

Lit visits.jsonl, results.jsonl, email-captures.jsonl, shares.jsonl, feedbacks.jsonl
et produit un rapport texte (defaut) ou JSON (--json).

Heuristiques bot/test :
  - sessionId is null      → endpoint hit direct (curl/script), pas d'UI
  - UA contient "X11; Linux x86_64" Chrome non-headless → testing dev VPS
  - UA "HeadlessChrome" → bot explicite (scanner, scraper)
  - UA "Mac OS X 10_15_7" Chrome → Googlebot rendering (Chrome obsolète stable utilisé par
    le renderer Google). Frozen version 10_15_7 = signature Googlebot moderne.
  - UA "iPhone OS 26_3" → AppleBot mobile (iOS récent latest non-standard)
  - UA "Android 10; K" → Googlebot mobile rendering (K = template Pixel test agent)
  - Tous ces patterns "humain stealth" + 0 /api/result dans la session → "likely_crawler".
  - UA Mac/Windows/iPhone classiques avec 0 result → "unknown_passive" (rebond ou bot non
    catalogué).
  - UA + sessionId + ≥1 /api/result → "human_engaged" (vrai humain qui a vu un verdict).
"""
import json
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
FILES = ["visits.jsonl", "results.jsonl", "email-captures.jsonl",
         "shares.jsonl", "feedbacks.jsonl"]


def load(name):
    p = DATA_DIR / name
    if not p.exists() or p.stat().st_size == 0:
        return []
    out = []
    for line in p.read_text().splitlines():
        line = line.strip()
        if line:
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return out


CRAWLER_UA_MARKERS = (
    "HeadlessChrome",
    "Mac OS X 10_15_7",
    "iPhone OS 26_3",
    "Android 10; K",
)


def classify(v, sessions_with_result):
    """Retourne 'bot_no_session' | 'dev_testing' | 'likely_crawler' |
    'unknown_passive' | 'human_engaged'."""
    sid = v.get("sessionId")
    if sid is None:
        return "bot_no_session"
    ua = v.get("ua", "")
    if "X11; Linux x86_64" in ua and "HeadlessChrome" not in ua:
        return "dev_testing"
    if sid in sessions_with_result:
        return "human_engaged"
    if any(m in ua for m in CRAWLER_UA_MARKERS):
        return "likely_crawler"
    return "unknown_passive"


def main():
    json_out = "--json" in sys.argv

    visits = load("visits.jsonl")
    results = load("results.jsonl")
    captures = load("email-captures.jsonl")
    shares = load("shares.jsonl")
    feedbacks = load("feedbacks.jsonl")

    sessions_with_result = {r.get("sessionId") for r in results if r.get("sessionId")}

    classes = Counter(classify(v, sessions_with_result) for v in visits)
    by_ip = Counter(v.get("ip_hash") for v in visits)
    by_session = Counter(v.get("sessionId") for v in visits if v.get("sessionId"))
    by_referrer = Counter(v.get("referrer", "") for v in visits)
    by_ua = Counter(v.get("ua", "") for v in visits)

    engaged_sessions = {v["sessionId"] for v in visits if classify(v, sessions_with_result) == "human_engaged"}
    engaged_results = [r for r in results if r.get("sessionId") in engaged_sessions]
    engaged_captures = [c for c in captures if c.get("sessionId") in engaged_sessions]

    report = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "visits_total_raw": len(visits),
        "visits_classified": dict(classes),
        "unique_sessions_with_ui": len(by_session),
        "unique_ip_hashes": len(by_ip),
        "results_total_raw": len(results),
        "captures_total_raw": len(captures),
        "shares_total_raw": len(shares),
        "feedbacks_total_raw": len(feedbacks),
        "funnel_engaged_human": {
            "visits_engaged": classes.get("human_engaged", 0),
            "sessions_engaged": len(engaged_sessions),
            "results_engaged": len(engaged_results),
            "captures_engaged": len(engaged_captures),
        },
        "top_referrers": by_referrer.most_common(5),
        "top_user_agents_truncated": [
            (ua[:80] + ("..." if len(ua) > 80 else ""), n)
            for ua, n in by_ua.most_common(5)
        ],
        "verdict": (
            "0 humain engagé — aucune session n'a déclenché /api/result."
            if classes.get("human_engaged", 0) == 0
            else f"{classes.get('human_engaged', 0)} visite(s) engagée(s) (= a calculé un verdict)."
        ),
    }

    if json_out:
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return

    print(f"# Audit funnel wedge — {report['generated_at']}")
    print()
    print(f"Total visites brutes : {report['visits_total_raw']}")
    print(f"  - bot_no_session         : {classes.get('bot_no_session', 0)}")
    print(f"  - dev_testing            : {classes.get('dev_testing', 0)}")
    print(f"  - likely_crawler         : {classes.get('likely_crawler', 0)}")
    print(f"  - unknown_passive        : {classes.get('unknown_passive', 0)}")
    print(f"  - human_engaged          : {classes.get('human_engaged', 0)}")
    print()
    print("Funnel humain engagé (= au moins un /api/result) :")
    f = report["funnel_engaged_human"]
    print(f"  visits  : {f['visits_engaged']}")
    print(f"  sessions: {f['sessions_engaged']}")
    print(f"  results : {f['results_engaged']}")
    print(f"  emails  : {f['captures_engaged']}")
    print()
    print("Top referrers :")
    for r, n in report["top_referrers"]:
        print(f"  {n:3d}  {r or '(empty)'}")
    print()
    print("Top UA :")
    for ua, n in report["top_user_agents_truncated"]:
        print(f"  {n:3d}  {ua}")
    print()
    print(f"Verdict : {report['verdict']}")


if __name__ == "__main__":
    main()
