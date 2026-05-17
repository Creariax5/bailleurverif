#!/usr/bin/env python3
"""Mesure compounding moat : N unique aids / jour / ville depuis le corpus dedup.

Usage:
    python3 moat_growth_tracker.py <dedup.jsonl>

Sortie : table jour × ville (aids first-seen ce jour) + ligne cumulative + JSON résumé.
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

DEP_TO_SLUG = {
    "75": "paris",
    "92": "paris-banlieue", "93": "paris-banlieue", "94": "paris-banlieue",
    "69": "lyon",
    "59": "lille",
    "13": "marseille-aix",
    "44": "nantes",
    "31": "toulouse",
    "33": "bordeaux",
}


def city_from_cp(cp: str | None) -> str:
    if not cp or len(cp) < 2:
        return "other"
    return DEP_TO_SLUG.get(cp[:2], "other")


def main(path_in: str) -> None:
    p = Path(path_in)
    if not p.exists():
        print(f"[tracker] ERR not found: {p}", file=sys.stderr)
        sys.exit(2)

    first_seen: dict[str, str] = {}
    city_of: dict[str, str] = {}
    n_in = 0
    with p.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rec = json.loads(line)
            aid = rec.get("accommodation_id")
            ts = rec.get("ts", "")
            if not aid or not ts:
                continue
            n_in += 1
            day = ts[:10]
            prev = first_seen.get(aid)
            if prev is None or day < prev:
                first_seen[aid] = day
                city_of[aid] = city_from_cp(rec.get("code_postal"))

    by_day_city: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for aid, day in first_seen.items():
        by_day_city[day][city_of[aid]] += 1

    days = sorted(by_day_city)
    cities = sorted({c for d in by_day_city.values() for c in d})

    print(f"[tracker] input_records={n_in} unique_aids={len(first_seen)} days={len(days)} cities={len(cities)}")
    print()
    header = ["day"] + cities + ["total_new", "cumulative_N"]
    print("\t".join(header))
    cumulative = 0
    for day in days:
        per_city = [by_day_city[day].get(c, 0) for c in cities]
        total = sum(per_city)
        cumulative += total
        print("\t".join([day] + [str(x) for x in per_city] + [str(total), str(cumulative)]))

    summary = {
        "input_records": n_in,
        "unique_aids_lifetime": len(first_seen),
        "days_observed": len(days),
        "first_day": days[0] if days else None,
        "last_day": days[-1] if days else None,
        "cities": cities,
        "per_day": {
            day: {
                "by_city": dict(by_day_city[day]),
                "total_new": sum(by_day_city[day].values()),
            }
            for day in days
        },
    }
    summary["cumulative_N"] = cumulative
    print()
    print("--- JSON summary ---")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: moat_growth_tracker.py <dedup.jsonl>", file=sys.stderr)
        sys.exit(2)
    main(sys.argv[1])
