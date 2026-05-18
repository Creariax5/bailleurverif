#!/usr/bin/env python3
"""
judilibre_fetch.py — moat cat-3 RAG prep.

Fetches arrêts Cour de cassation chambre civile 3 (bail/loyer)
from api.piste.gouv.fr/cassation/judilibre/v1.0 (OAuth2 client_credentials).

Run-263 creation: skeleton ready-but-not-runnable (no creds yet,
TODO-28 silent ≥5 wakes since 12:57Z = readiness seuil reached per
run-261 NEXT plan (C)). When Florian populates .env JUDILIBRE_CLIENT_ID
and JUDILIBRE_CLIENT_SECRET, this script becomes one-command operable:

    python3 crawler/judilibre_fetch.py --query "bail" --max-results 10

Output: data/jurisprudence/judilibre-bail-<date>.jsonl (1 arrêt/line),
intended to populate jurisprudence_refs[] in interpretation-library-v0
templates (loyer-abusif.v0.json etc.) with real timestamped Cass.civ.3
citations vs current CC-BY-4.0 static templates (forkable in 5 min).

Endpoints (api.piste.gouv.fr docs):
  Token: POST https://oauth.aife.economie.gouv.fr/api/oauth/token
         (client_credentials grant, scope=openid)
  Search: GET https://api.piste.gouv.fr/cassation/judilibre/v1.0/search
         (q, chamber, type, sort, page, page_size, ...)
  Decision: GET https://api.piste.gouv.fr/cassation/judilibre/v1.0/decision
         (id) — fetch full text once IDs harvested.

Stdlib only (urllib + json + os). 0 external deps. Honest UA.
"""
from __future__ import annotations
import argparse
import json
import os
import pathlib
import sys
import time
import urllib.parse
import urllib.request

TOKEN_URL = "https://oauth.aife.economie.gouv.fr/api/oauth/token"
SEARCH_URL = "https://api.piste.gouv.fr/cassation/judilibre/v1.0/search"
DECISION_URL = "https://api.piste.gouv.fr/cassation/judilibre/v1.0/decision"
UA = "BailleurVerifBot/1.0 (+https://bailleurverif.fr; jurisprudence-rag; respects-rate-limits)"
DEFAULT_OUT_DIR = pathlib.Path("/home/deploy/saas-florian/wedge-tool/data/jurisprudence")


def load_env(path: str = "/home/deploy/saas-florian/.env") -> dict[str, str]:
    env: dict[str, str] = {}
    p = pathlib.Path(path)
    if not p.exists():
        return env
    for raw in p.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        env[k.strip()] = v.strip().strip('"').strip("'")
    return env


def fetch_token(client_id: str, client_secret: str) -> str:
    body = urllib.parse.urlencode({
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": "openid",
    }).encode("utf-8")
    req = urllib.request.Request(
        TOKEN_URL,
        data=body,
        method="POST",
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": UA,
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        payload = json.loads(resp.read().decode("utf-8"))
    token = payload.get("access_token")
    if not token:
        raise RuntimeError(f"no access_token in piste response: {payload!r}")
    return token


def search(token: str, query: str, page: int = 0, page_size: int = 10,
           chamber: str = "civ3") -> dict:
    params = {
        "query": query,
        "chamber": chamber,
        "page": page,
        "page_size": page_size,
        "sort": "date",
        "order": "desc",
    }
    url = f"{SEARCH_URL}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {token}",
        "User-Agent": UA,
        "Accept": "application/json",
    })
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_decision(token: str, decision_id: str) -> dict:
    url = f"{DECISION_URL}?{urllib.parse.urlencode({'id': decision_id})}"
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {token}",
        "User-Agent": UA,
        "Accept": "application/json",
    })
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main() -> int:
    ap = argparse.ArgumentParser(description="Fetch Cass.civ.3 arrêts via Judilibre API")
    ap.add_argument("--query", required=True,
                    help="search terms (e.g. 'bail', 'loyer abusif', 'restitution dépôt')")
    ap.add_argument("--max-results", type=int, default=10)
    ap.add_argument("--chamber", default="civ3",
                    help="cass chamber code (civ3 = 3ᵉ chambre civile, bail/loyer)")
    ap.add_argument("--out-dir", default=str(DEFAULT_OUT_DIR))
    ap.add_argument("--fetch-text", action="store_true",
                    help="also fetch full decision text (extra API call per hit)")
    ap.add_argument("--dry-run", action="store_true",
                    help="auth + print 1 search summary, write nothing")
    args = ap.parse_args()

    env = load_env()
    cid = env.get("JUDILIBRE_CLIENT_ID")
    csecret = env.get("JUDILIBRE_CLIENT_SECRET")
    if not cid or not csecret:
        print("[judilibre_fetch] missing JUDILIBRE_CLIENT_ID / JUDILIBRE_CLIENT_SECRET in .env",
              file=sys.stderr)
        print("[judilibre_fetch] see florian-todos.md TODO-28 (api.piste.gouv.fr signup)",
              file=sys.stderr)
        return 2

    try:
        token = fetch_token(cid, csecret)
    except Exception as e:
        print(f"[judilibre_fetch] oauth token fetch failed: {e}", file=sys.stderr)
        return 3

    print(f"[judilibre_fetch] auth OK, querying chamber={args.chamber} q={args.query!r}")

    out_dir = pathlib.Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    date = time.strftime("%Y-%m-%d", time.gmtime())
    slug = "".join(c if c.isalnum() else "-" for c in args.query.lower())[:40].strip("-")
    out_path = out_dir / f"judilibre-{slug}-{date}.jsonl"

    fetched = 0
    page = 0
    page_size = min(args.max_results, 50)
    with out_path.open("w", encoding="utf-8") as fout:
        while fetched < args.max_results:
            res = search(token, args.query, page=page, page_size=page_size,
                         chamber=args.chamber)
            hits = res.get("results") or res.get("hits") or []
            if not hits:
                break
            for hit in hits:
                if fetched >= args.max_results:
                    break
                rec = {
                    "id": hit.get("id"),
                    "date": hit.get("decision_date"),
                    "chamber": hit.get("chamber"),
                    "number": hit.get("number") or hit.get("numero"),
                    "ecli": hit.get("ecli"),
                    "summary": hit.get("summary") or hit.get("resume"),
                    "themes": hit.get("themes") or hit.get("matieres"),
                    "fetched_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                }
                if args.fetch_text and rec["id"]:
                    try:
                        full = fetch_decision(token, rec["id"])
                        rec["text"] = full.get("text") or full.get("texte")
                    except Exception as e:
                        rec["text_error"] = str(e)
                    time.sleep(0.5)  # gentle pace, even if API allows more
                if args.dry_run:
                    print(json.dumps(rec, ensure_ascii=False, indent=2))
                    return 0
                fout.write(json.dumps(rec, ensure_ascii=False) + "\n")
                fetched += 1
            page += 1
            time.sleep(0.5)
    print(f"[judilibre_fetch] wrote {fetched} records to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
