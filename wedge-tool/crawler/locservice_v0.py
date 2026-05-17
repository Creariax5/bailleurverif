#!/usr/bin/env python3
"""
Locservice V0 crawler — moat-builder MISSION Option 1 (DIRECTIVE 9).

Pourquoi Locservice : robots.txt User-agent:* permissive (vs LBC/SeLoger interdiction
explicite). Pages publiques /{dept}-{XX}/location.html listent ~20-50 annonces avec
data-accommodation-id ; pages détail exposent DPE via filename energie-{X}.png.

Garde-fous DIRECTIVE 9 + mission brief :
- UA : "BailleurVerifCompliance/0.1 (+https://bailleurverif.fr; contact@bailleurverif.fr)"
- Pace : 30s entre requêtes (PAUSE_SECONDS) — pas d'agression
- 0 stockage PII vendeur (nom/téléphone/email). Hash de l'URL + ville + loyer + surface + DPE.
- Output JSONL pour pipeline downstream (scoring conformité)
- Smoke mode : limite N listings, log explicit
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin
from urllib.request import Request, urlopen

UA = "BailleurVerifCompliance/0.1 (+https://bailleurverif.fr; contact@bailleurverif.fr) public-interest housing-compliance research"
PAUSE_SECONDS = 30
TIMEOUT = 20
BASE = "https://www.locservice.fr"
INDEX_URL = "https://www.locservice.fr/paris-75/location.html"
OUT_DIR = Path(__file__).resolve().parent.parent / "data" / "listings"

CARD_RE = re.compile(
    r'data-accommodation-id="(?P<aid>\d+)">\s*<article>.*?'
    r'<h3[^>]*><a href="(?P<url>https://www\.locservice\.fr/[^"]+)"[^>]*>(?P<title>[^<]+)</a>.*?'
    r'<li class="accommodation-ad-characteristic"><ls-icon[^>]*name="geo"></ls-icon>\s*(?P<loc>[^<]+?)</li>.*?'
    r'(?:<li class="accommodation-ad-characteristic"><ls-icon[^>]*name="bounding-box-circles"></ls-icon>\s*(?P<surface>\d+)\s*m'
    r'.*?)?'
    r'<li class="accommodation-ad-characteristic accommodation-ad-characteristic-price">'
    r'<ls-icon[^>]*></ls-icon>(?P<price>[^<]+?)</li>',
    re.DOTALL,
)

# image filename pattern : /build/shared/dpe/energie-{LETTER}.{hash}.png
DPE_RE = re.compile(r'/dpe/energie-([A-G])\.[a-f0-9]+\.png')
GES_RE = re.compile(r'/dpe/ges-([A-G])\.[a-f0-9]+\.png')
# Postal code from "Paris 17 (75017)" or "Paris (75001)"
CP_RE = re.compile(r"\((\d{5})\)")
PRICE_RE = re.compile(r"(\d[\d\s]*)\s*€")


def fetch(url: str) -> str:
    req = Request(url, headers={"User-Agent": UA, "Accept-Language": "fr-FR,fr;q=0.9"})
    with urlopen(req, timeout=TIMEOUT) as r:
        body = r.read()
        enc = r.headers.get_content_charset() or "utf-8"
        return body.decode(enc, errors="replace")


def parse_price(raw: str) -> int | None:
    cleaned = "".join(ch for ch in raw if ch.isdigit() or ch == "€")
    m = __import__("re").search(r"(\d+)€", cleaned)
    if m:
        return int(m.group(1))
    digits = "".join(ch for ch in cleaned if ch.isdigit())
    return int(digits) if digits else None


def parse_index(html: str) -> list[dict]:
    items: list[dict] = []
    for m in CARD_RE.finditer(html):
        d = m.groupdict()
        cp_m = CP_RE.search(d["loc"] or "")
        items.append(
            {
                "accommodation_id": d["aid"],
                "url": d["url"],
                "title": d["title"].strip(),
                "loc_raw": (d["loc"] or "").strip(),
                "code_postal": cp_m.group(1) if cp_m else None,
                "surface_m2": int(d["surface"]) if d["surface"] else None,
                "loyer_eur_total": parse_price(d["price"] or ""),
                "price_raw": (d["price"] or "").strip(),
            }
        )
    return items


def parse_detail_dpe(html: str) -> tuple[str | None, str | None]:
    dpe = DPE_RE.search(html)
    ges = GES_RE.search(html)
    return (dpe.group(1) if dpe else None, ges.group(1) if ges else None)


def hash_url(url: str) -> str:
    return hashlib.sha256(url.encode("utf-8")).hexdigest()[:16]


def main(limit: int = 5, index_url: str = INDEX_URL, city_slug: str = "paris"):
    log = lambda *a: print(f"[locservice_v0:{city_slug}]", *a, flush=True)
    log(f"START limit={limit} pace={PAUSE_SECONDS}s ua={UA[:40]}...")
    log(f"FETCH index {index_url}")
    html = fetch(index_url)
    log(f"  size={len(html)}b cards_regex_matches={len(CARD_RE.findall(html))}")
    items = parse_index(html)
    log(f"  parsed={len(items)} listings from index")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    out_path = OUT_DIR / f"locservice-{city_slug}-{today}.jsonl"
    n_emit = 0
    with out_path.open("a", encoding="utf-8") as out:
        for item in items[:limit]:
            log(f"  pause {PAUSE_SECONDS}s before detail fetch (aid={item['accommodation_id']})")
            time.sleep(PAUSE_SECONDS)
            try:
                detail = fetch(item["url"])
            except Exception as e:
                log(f"  FAIL fetch detail {item['url']}: {e}")
                continue
            dpe, ges = parse_detail_dpe(detail)
            rec = {
                "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                "source": "locservice",
                "url_hash": hash_url(item["url"]),
                "url": item["url"],
                "accommodation_id": item["accommodation_id"],
                "code_postal": item["code_postal"],
                "ville_label": item["loc_raw"],
                "surface_m2": item["surface_m2"],
                "loyer_eur_total": item["loyer_eur_total"],
                "dpe_letter": dpe,
                "ges_letter": ges,
                "title": item["title"][:200],
                "price_raw": item["price_raw"],
            }
            out.write(json.dumps(rec, ensure_ascii=False) + "\n")
            out.flush()
            n_emit += 1
            log(
                f"  OK aid={item['accommodation_id']} cp={item['code_postal']} "
                f"surf={item['surface_m2']}m2 loyer={item['loyer_eur_total']}EUR "
                f"dpe={dpe} ges={ges}"
            )
    log(f"DONE wrote {n_emit} records -> {out_path}")
    return n_emit


if __name__ == "__main__":
    # CLI: locservice_v0.py [LIMIT] [--index-url URL] [--city-slug SLUG]
    args = sys.argv[1:]
    index_url = INDEX_URL
    city_slug = "paris"
    if "--index-url" in args:
        i = args.index("--index-url")
        index_url = args[i + 1]
        args = args[:i] + args[i + 2 :]
    if "--city-slug" in args:
        i = args.index("--city-slug")
        city_slug = args[i + 1]
        args = args[:i] + args[i + 2 :]
    limit = int(args[0]) if args else 5
    main(limit=limit, index_url=index_url, city_slug=city_slug)
