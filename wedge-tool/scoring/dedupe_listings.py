#!/usr/bin/env python3
"""Dedupe locservice JSONL listings by accommodation_id (keep latest ts)."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def main(inputs: list[str], out_path: str) -> None:
    log = lambda *a: print("[dedupe]", *a, flush=True)
    by_aid: dict[str, dict] = {}
    n_in = 0
    n_skip_no_aid = 0
    for p in inputs:
        path = Path(p)
        log(f"reading {path}")
        with path.open(encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                rec = json.loads(line)
                n_in += 1
                aid = rec.get("accommodation_id")
                if not aid:
                    n_skip_no_aid += 1
                    continue
                prev = by_aid.get(aid)
                if prev is None or rec.get("ts", "") > prev.get("ts", ""):
                    by_aid[aid] = rec
    outp = Path(out_path)
    outp.parent.mkdir(parents=True, exist_ok=True)
    with outp.open("w", encoding="utf-8") as f:
        for aid in sorted(by_aid):
            f.write(json.dumps(by_aid[aid], ensure_ascii=False) + "\n")
    log(f"input_lines={n_in} unique_aid={len(by_aid)} skipped_no_aid={n_skip_no_aid}")
    log(f"wrote {len(by_aid)} -> {outp}")


if __name__ == "__main__":
    args = sys.argv[1:]
    if "-o" not in args:
        print("usage: dedupe_listings.py -o out.jsonl in1.jsonl [in2.jsonl ...]")
        sys.exit(2)
    i = args.index("-o")
    out = args[i + 1]
    args = args[:i] + args[i + 2 :]
    if not args:
        print("usage: dedupe_listings.py -o out.jsonl in1.jsonl [in2.jsonl ...]")
        sys.exit(2)
    main(args, out)
