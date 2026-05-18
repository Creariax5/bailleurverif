#!/usr/bin/env python3
"""Seed corpus cat-3 RAG v0 — Service-Public.fr 5 fiches publiques bail FR.
Sortie : data/corpus/service-public-v0.jsonl (append).
Pace : 30s entre requêtes (respect courtoisie).
UA identifié + email contact.
"""
import datetime as dt
import html
import json
import pathlib
import re
import sys
import time
import urllib.request

OUT_PATH = pathlib.Path("/home/deploy/saas-florian/data/corpus/service-public-v0.jsonl")
UA = "BailleurVerifBot/0.1 (+https://bailleurverif.fr; contact@bailleurverif.fr)"
PACE_SECONDS = 30
URLS = [
    ("F920", "https://www.service-public.fr/particuliers/vosdroits/F920", "bail-habitation-vide"),
    ("F1311", "https://www.service-public.fr/particuliers/vosdroits/F1311", "preavis-locataire-vide"),
    ("F2050", "https://www.service-public.fr/particuliers/vosdroits/F2050", "etat-des-lieux"),
    ("F1314", "https://www.service-public.fr/particuliers/vosdroits/F1314", "depot-de-garantie"),
    ("F1334", "https://www.service-public.fr/particuliers/vosdroits/F1334", "revision-loyer-bail-vide"),
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
    # Try <main> first, else <article>, else body
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
            "source": "service-public.fr",
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
            "license_note": "service-public.fr Etalab v2.0 / Open Licence — citation source obligatoire",
        }
        with OUT_PATH.open("a", encoding="utf-8") as f:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
        rows_written += 1
        print(f"{ts} OK {slug_short} title={title[:60]!r} len={len(text)}", flush=True)
    print(f"DONE wrote={rows_written} skipped={skipped} out={OUT_PATH}", flush=True)


if __name__ == "__main__":
    sys.exit(main())
