#!/usr/bin/env python3
"""migrate_reclassify.py — re-classify entries dans reglementation-changes.jsonl
avec le TOPIC_KEYWORDS courant. Idempotent : ré-écrit topics + keywords_matched.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
from poll_jorf import classify_topics, CHANGES_FILE


def main():
    if not os.path.exists(CHANGES_FILE):
        print(f"{CHANGES_FILE} absent", file=sys.stderr)
        return 1
    rows = []
    with open(CHANGES_FILE) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))
    n = 0
    changed = 0
    for r in rows:
        n += 1
        topics, kw = classify_topics(r["titre"])
        if not topics:
            # garde une trace : si rien ne match plus, on ne l'enlève pas (rare),
            # mais on logge le warning
            print(f"  WARN no topic match: {r['titre'][:90]}", file=sys.stderr)
            continue
        old_topics = sorted(r.get("topics", []))
        new_topics = sorted(topics)
        if old_topics != new_topics:
            print(f"  RECLASSIFIED {r['date_publi']} {r['titre'][:80]}")
            print(f"    {old_topics} -> {new_topics}")
            r["topics"] = topics
            r["keywords_matched"] = kw[:6]
            changed += 1
    # write back atomically
    tmp = CHANGES_FILE + ".tmp"
    with open(tmp, "w") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    os.replace(tmp, CHANGES_FILE)
    print(f"DONE total={n} changed={changed}")


if __name__ == "__main__":
    main()
