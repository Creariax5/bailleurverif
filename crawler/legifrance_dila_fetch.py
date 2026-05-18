#!/usr/bin/env python3
"""
legifrance_dila_fetch.py — moat cat-3 self-served ingestion path.

Fetches French codified law bulk archives from the DILA open-data portal
(https://echanges.dila.gouv.fr/OPENDATA/LEGI/) and indexes article XML
files relevant to BailleurVérif domain (bail/loyer/DPE/copropriété).

Unlike judilibre_fetch.py which requires OAuth nominatif (TODO-28 Florian
signup api.piste.gouv.fr), the DILA LEGI bulk dump is plain HTTPS open-data
(Licence Ouverte Etalab v2.0) — no signup, no credentials, no OAuth.
Self-served cat-3 path identified run-264 (tactical critic-14 hypothesis
"pivot cat-3 self-served si TODO-23/TODO-28 silent J+2").

The archive lists daily LEGI snapshots/deltas (~500KB-3MB each, ~70MB full).
We download the latest delta and walk *article/.../LEGIARTI*.xml to extract
{id, num, etat, date_debut, date_fin, contexte.texte.num (loi number),
contexte.texte.nor, titre, bloc_textuel/contenu}. Output JSONL one article
per line in data/legifrance/legi-<date>.jsonl, intended to populate the
`legal_basis[]` array of interpretation-library-v0 templates with real
timestamped article citations + verbatim text (vs hand-typed copies).

Usage:
    python3 crawler/legifrance_dila_fetch.py --latest-delta
    python3 crawler/legifrance_dila_fetch.py --file LEGI_20260517-204556.tar.gz
    python3 crawler/legifrance_dila_fetch.py --list-only

Stdlib only (urllib + tarfile + xml.etree). 0 external deps. Honest UA.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tarfile
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin
from urllib.request import Request, urlopen
from xml.etree import ElementTree as ET

BASE_URL = "https://echanges.dila.gouv.fr/OPENDATA/LEGI/"
USER_AGENT = "BailleurVerifCompliance/0.1 (+https://bailleurverif.fr)"
OUT_DIR = Path("data/legifrance")
PACE_SECONDS = 0.5
TIMEOUT = 60

# Article XML files live deep in the tarball under JORFTEXT/.../article/LEGI/ARTI/.../LEGIARTI*.xml
ARTICLE_RE = re.compile(r"article/LEGI/ARTI/.*/LEGIARTI\d+\.xml$")


def http_get(url: str, *, binary: bool = False) -> bytes | str:
    req = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(req, timeout=TIMEOUT) as resp:
        data = resp.read()
    return data if binary else data.decode("utf-8", errors="replace")


def list_archives() -> list[str]:
    html = http_get(BASE_URL)
    names = re.findall(r'href="(LEGI_\d{8}-\d{6}\.tar\.gz)"', html)
    return sorted(set(names))


def download_archive(name: str, dest_dir: Path) -> Path:
    dest_dir.mkdir(parents=True, exist_ok=True)
    target = dest_dir / name
    if target.exists():
        return target
    url = urljoin(BASE_URL, name)
    print(f"[fetch] GET {url}", file=sys.stderr)
    data = http_get(url, binary=True)
    target.write_bytes(data)
    print(f"[fetch] wrote {target} ({len(data)} bytes)", file=sys.stderr)
    return target


def parse_article(xml_bytes: bytes) -> dict | None:
    try:
        root = ET.fromstring(xml_bytes)
    except ET.ParseError:
        return None
    if root.tag != "ARTICLE":
        return None

    def first(path: str) -> str | None:
        el = root.find(path)
        return el.text.strip() if el is not None and el.text else None

    def text_of(path: str) -> str:
        el = root.find(path)
        if el is None:
            return ""
        # Flatten inner text (BLOC_TEXTUEL/CONTENU contains <br/>, <p>, etc.)
        return "".join(el.itertext()).strip()

    texte_el = root.find("CONTEXTE/TEXTE")
    titre = ""
    if texte_el is not None:
        titre_tt = texte_el.find("TITRE_TXT")
        if titre_tt is not None and titre_tt.text:
            titre = titre_tt.text.strip()
    return {
        "id": first("META/META_COMMUN/ID"),
        "num": first("META/META_SPEC/META_ARTICLE/NUM"),
        "etat": first("META/META_SPEC/META_ARTICLE/ETAT"),
        "date_debut": first("META/META_SPEC/META_ARTICLE/DATE_DEBUT"),
        "date_fin": first("META/META_SPEC/META_ARTICLE/DATE_FIN"),
        "nature": first("META/META_COMMUN/NATURE"),
        "texte_num": texte_el.get("num") if texte_el is not None else None,
        "texte_nor": texte_el.get("nor") if texte_el is not None else None,
        "texte_nature": texte_el.get("nature") if texte_el is not None else None,
        "texte_date_publi": texte_el.get("date_publi") if texte_el is not None else None,
        "titre_court": titre,
        "contenu": text_of("BLOC_TEXTUEL/CONTENU"),
    }


def walk_articles(archive_path: Path, limit: int | None = None):
    with tarfile.open(archive_path, "r:gz") as tar:
        count = 0
        for member in tar:
            if not member.isfile():
                continue
            if not ARTICLE_RE.search(member.name):
                continue
            f = tar.extractfile(member)
            if f is None:
                continue
            xml_bytes = f.read()
            article = parse_article(xml_bytes)
            if article:
                yield article
                count += 1
                if limit and count >= limit:
                    return


def main() -> int:
    p = argparse.ArgumentParser(description="Fetch DILA LEGI bulk and index articles")
    p.add_argument("--list-only", action="store_true", help="List available archives and exit")
    p.add_argument("--latest-delta", action="store_true", help="Fetch most recent dated delta")
    p.add_argument("--file", help="Specific tarball filename (e.g. LEGI_20260517-204556.tar.gz)")
    p.add_argument("--max-articles", type=int, default=200, help="Max articles to extract (smoke cap)")
    p.add_argument("--out", default=None, help="Output JSONL path (default data/legifrance/legi-<date>.jsonl)")
    p.add_argument(
        "--keywords",
        default=None,
        help="Comma-separated keywords; keep only articles whose titre/contenu matches any (case-insensitive)",
    )
    args = p.parse_args()
    keywords = [k.strip().lower() for k in args.keywords.split(",")] if args.keywords else None

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    if args.list_only:
        archives = list_archives()
        print(f"[list] {len(archives)} archives in {BASE_URL}", file=sys.stderr)
        for name in archives[-10:]:
            print(name)
        return 0

    if args.file:
        archive_name = args.file
    elif args.latest_delta:
        archives = list_archives()
        # Skip "Freemium_legi_global" — those are full snapshots, much larger
        deltas = [a for a in archives if a.startswith("LEGI_")]
        if not deltas:
            print("[error] no LEGI_* delta archives found", file=sys.stderr)
            return 1
        archive_name = deltas[-1]
        print(f"[latest] picked {archive_name}", file=sys.stderr)
    else:
        print("[error] specify --list-only, --latest-delta, or --file", file=sys.stderr)
        return 2

    archive_path = download_archive(archive_name, OUT_DIR)
    time.sleep(PACE_SECONDS)

    # Date stamp from filename e.g. LEGI_20260517-204556.tar.gz → 20260517
    m = re.search(r"(\d{8})", archive_name)
    stamp = m.group(1) if m else datetime.now(timezone.utc).strftime("%Y%m%d")
    out_path = Path(args.out) if args.out else OUT_DIR / f"legi-{stamp}.jsonl"

    extracted = 0
    scanned = 0
    with out_path.open("w", encoding="utf-8") as fh:
        for article in walk_articles(archive_path, limit=None if keywords else args.max_articles):
            scanned += 1
            if keywords:
                hay = (article.get("titre_court", "") + " " + article.get("contenu", "")).lower()
                if not any(kw in hay for kw in keywords):
                    continue
            fh.write(json.dumps(article, ensure_ascii=False) + "\n")
            extracted += 1
            if keywords and extracted >= args.max_articles:
                break
    print(f"[done] scanned {scanned}, extracted {extracted} articles → {out_path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
