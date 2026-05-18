#!/usr/bin/env python3
"""Seed corpus cat-3 RAG v0 N+2 — ANIL parole-expert-logement-location 5 pages publiques.
Sortie : data/corpus/anil-v0.jsonl (append).
Pace : 30s entre requêtes (respect courtoisie).
UA identifié + email contact.
robots.txt ANIL vérifié 2026-05-18T01:57Z : pages /parole-expert-logement-location/* PAS disallow.
"""
import datetime as dt
import html
import json
import pathlib
import re
import sys
import time
import urllib.request

OUT_PATH = pathlib.Path("/home/deploy/saas-florian/data/corpus/anil-v0.jsonl")
UA = "BailleurVerifBot/0.1 (+https://bailleurverif.fr; contact@bailleurverif.fr)"
PACE_SECONDS = 30
URLS = [
    ("anil-pe-loc-hub", "https://www.anil.org/parole-expert-logement-location/", "hub-parole-expert-location"),
    ("anil-fixer-loyer", "https://www.anil.org/parole-expert-logement-location/comment-fixer-le-montant-dun-loyer/", "fixation-loyer"),
    ("anil-resiliation-bail", "https://www.anil.org/parole-expert-logement-location/parole-expert-logement-location-resiliation-bail/", "resiliation-bail"),
    ("anil-discrimination-logement", "https://www.anil.org/parole-expert-logement-location/la-discrimination-dans-le-logement-quels-sont-vos-droits/", "discrimination-logement"),
    ("anil-location-pas-garant", "https://www.anil.org/parole-expert-logement-location-pas-garant/", "location-sans-garant"),
]


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "fr"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.status, resp.read().decode("utf-8", errors="replace")


def extract_title(htmlsrc):
    m = re.search(r"<title>(.*?)</title>", htmlsrc, re.IGNORECASE | re.DOTALL)
    if not m:
        return ""
    return html.unescape(re.sub(r"\s+", " ", m.group(1))).strip()


def extract_main_text(htmlsrc):
    for tag in ("main", "article"):
        m = re.search(rf"<{tag}\b[^>]*>(.*?)</{tag}>", htmlsrc, re.IGNORECASE | re.DOTALL)
        if m:
            inner = m.group(1)
            break
    else:
        inner = htmlsrc
    inner = re.sub(r"<script\b.*?</script>", " ", inner, flags=re.IGNORECASE | re.DOTALL)
    inner = re.sub(r"<style\b.*?</style>", " ", inner, flags=re.IGNORECASE | re.DOTALL)
    inner = re.sub(r"<[^>]+>", " ", inner)
    text = html.unescape(inner)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def main():
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    rows_written = 0
    skipped = 0
    for i, (slug_short, url, topic) in enumerate(URLS):
        if i > 0:
            time.sleep(PACE_SECONDS)
        ts = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        try:
            status, body = fetch(url)
        except Exception as e:
            print(f"{ts} ERROR fetch {url}: {e}", flush=True)
            skipped += 1
            continue
        if status != 200:
            print(f"{ts} SKIP status={status} {url}", flush=True)
            skipped += 1
            continue
        title = extract_title(body)
        text = extract_main_text(body)
        text_truncated = text[:12000]
        row = {
            "source": "anil.org",
            "slug_short": slug_short,
            "url": url,
            "topic": topic,
            "ts_fetched": ts,
            "http_status": status,
            "title": title,
            "body_text": text_truncated,
            "body_text_len_original": len(text),
            "body_text_len_stored": len(text_truncated),
            "ua_used": UA,
            "license_note": "anil.org — extrait public éditorial, citation source obligatoire, usage RAG non-commercial recherche",
        }
        with OUT_PATH.open("a", encoding="utf-8") as f:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
        rows_written += 1
        print(f"{ts} OK {slug_short} title={title[:60]!r} len={len(text)}", flush=True)
    print(f"DONE wrote={rows_written} skipped={skipped} out={OUT_PATH}", flush=True)


if __name__ == "__main__":
    sys.exit(main())
