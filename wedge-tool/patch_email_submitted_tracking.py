#!/usr/bin/env python3
"""
Patch inline subscribe forms across static/*.html to emit `email_submitted`
funnel event before POST /api/subscribe. Bug fix run-415 cross-ref UA finding:
73+ files had inline `fetch('/api/subscribe')` without trackFunnel.

Excludes index.html (audit-39 ban touch home). Idempotent.
"""
import re
import sys
from pathlib import Path

STATIC = Path(__file__).parent / "static"
EXCLUDE = {"index.html"}

INJECT = (
    "try{fetch('/api/funnel/event',{method:'POST',"
    "headers:{'Content-Type':'application/json'},"
    "body:JSON.stringify({sessionId:null,event_type:'email_submitted',"
    "path:location.pathname,"
    "meta:{kind:'inline_subscribe',has_at:(email||'').indexOf('@')>=0}"
    "})}).catch(function(){});}catch(e){}"
)

MARK = "event_type:'email_submitted'"
PAT = re.compile(r"^(\s*)((?:(?:const|let|var)\s+\w+\s*=\s*)?(?:await\s+)?fetch\(['\"]\/api\/subscribe['\"]\s*,)")

def patch(path: Path) -> int:
    src = path.read_text()
    if MARK in src:
        return 0
    out, changes = [], 0
    for line in src.split("\n"):
        m = PAT.match(line)
        if m:
            indent = m.group(1)
            out.append(f"{indent}{INJECT}")
            changes += 1
        out.append(line)
    if changes:
        path.write_text("\n".join(out))
    return changes

def main():
    sub_re = re.compile(r"fetch\(['\"]\/api\/subscribe['\"]")
    targets = sorted(p for p in STATIC.glob("*.html")
                     if p.name not in EXCLUDE
                     and sub_re.search(p.read_text()))
    total_files = 0
    total_inserts = 0
    for p in targets:
        n = patch(p)
        if n:
            total_files += 1
            total_inserts += n
    print(f"files_patched={total_files} inserts={total_inserts} skipped_already_done={len(targets)-total_files}")

if __name__ == "__main__":
    main()
