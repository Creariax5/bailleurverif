#!/usr/bin/env python3
"""
diag_recall.py — Diagnostic recall regex sur tarballs JORF déjà vus.
Mode read-only : scanne les tarballs JORF distants (sans persistence), affiche
TOUS les TITRE_TXT contenant des indicateurs broad housing/baux/préavis, puis
compare au filtre regex actuel pour quantifier le miss-rate par topic.
"""
import io
import json
import os
import re
import sys
import tarfile
import urllib.request
from datetime import datetime, timezone, timedelta

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
from poll_jorf import (
    DILA_INDEX, UA, HTTP_TIMEOUT, parse_section_ta_xml,
    classify_topics, list_dila_tarballs, COMPILED_TOPIC_KEYWORDS,
)

# Broader regex pour pêcher les vrais candidats par topic.
BROADER = {
    "loyer-legal": [
        r"\bloyer", r"\bbail\b", r"\bbaux\b",
        r"\blocation\b", r"\bcontrat de location", r"\bcommission de conciliation",
        r"\brevalorisation", r"\bIRL\b", r"\bindice de référence",
        r"\bplafond", r"\bencadrement",
    ],
    "preavis": [
        r"\bpréavis", r"\bcongé\b", r"\brésili", r"\bdépart du locataire",
        r"\bbail\b", r"\blocation\b",
    ],
    "veille-reglementaire-bailleur": [
        r"\blogement", r"\blocataire", r"\bbailleur", r"\bcopropriét",
        r"\bdécence", r"\bhabitabilité", r"\bdiagnostic",
    ],
    "aides-financieres": [
        r"MaPrimeRén", r"\bCEE\b", r"certificat d'économies",
        r"FEEBAT", r"PROFEEL", r"aide.*rénovation", r"prêt.*taux zéro",
        r"\bPTZ\b", r"aide personnalisée au logement", r"\bAPL\b",
    ],
}
COMP_BROADER = {k: [re.compile(p, re.IGNORECASE) for p in pats] for k, pats in BROADER.items()}


def fetch_titles(tarballs):
    titres = []
    for fname in tarballs:
        url = DILA_INDEX + fname
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT) as r:
                body = r.read()
        except Exception as e:
            print(f"  ERR fetch {fname}: {e}", file=sys.stderr)
            continue
        try:
            with tarfile.open(fileobj=io.BytesIO(body), mode="r:gz") as tar:
                for member in tar:
                    if not member.isfile():
                        continue
                    if "/section_ta/" not in member.name or not member.name.endswith(".xml"):
                        continue
                    try:
                        f = tar.extractfile(member)
                        if not f:
                            continue
                        xml = f.read()
                    except Exception:
                        continue
                    parsed = parse_section_ta_xml(xml)
                    if not parsed:
                        continue
                    titres.append(parsed)
        except Exception as e:
            print(f"  ERR untar {fname}: {e}", file=sys.stderr)
            continue
    return titres


def main():
    days = int(sys.argv[1]) if len(sys.argv) > 1 else 60
    max_tb = int(sys.argv[2]) if len(sys.argv) > 2 else 30
    tarballs = list_dila_tarballs(days)[-max_tb:]
    print(f"scanning last {len(tarballs)} tarballs covering ~{days} days")
    titres = fetch_titles(tarballs)
    print(f"parsed_titles={len(titres)}")

    # Dédup par (cid, nor)
    seen = set()
    uniq = []
    for t in titres:
        k = (t.get("cid"), t.get("nor"))
        if k in seen:
            continue
        seen.add(k)
        uniq.append(t)
    print(f"unique_by_cid_nor={len(uniq)}")

    # Filtre temporel date_publi
    cutoff = datetime.now(timezone.utc) - timedelta(days=180)
    recent = []
    for t in uniq:
        if t.get("date_publi"):
            try:
                d = datetime.strptime(t["date_publi"], "%Y-%m-%d").replace(tzinfo=timezone.utc)
                if d >= cutoff:
                    recent.append(t)
            except Exception:
                pass
    print(f"after_cutoff_180j={len(recent)}")
    print()

    # Pour chaque topic broader : trouve les candidats. Pour chacun, vérifie
    # si le regex actuel matche le topic correspondant.
    topic_map = {
        "loyer-legal": "loyer-legal",
        "preavis": "preavis",
        "veille-reglementaire-bailleur": "veille-reglementaire",
        "aides-financieres": "dpe-bailleur",  # actuel : rangé sous dpe-bailleur
    }
    for broad_topic, broad_patterns in COMP_BROADER.items():
        actual_topic = topic_map[broad_topic]
        matched_broad = []
        for t in recent:
            for p in broad_patterns:
                if p.search(t["titre"]):
                    matched_broad.append((t, p.pattern))
                    break
        print(f"=== {broad_topic} (actual_topic={actual_topic}) ===")
        print(f"broader matches: {len(matched_broad)}")
        hit_by_actual = 0
        for (t, bp) in matched_broad:
            topics, _ = classify_topics(t["titre"])
            covered = actual_topic in topics
            if covered:
                hit_by_actual += 1
            mark = "OK" if covered else "MISS"
            print(f"  [{mark}] {t['date_publi']} {t['titre'][:120]}")
            if not covered:
                print(f"        broader_hit={bp} | current_topics={topics}")
        print(f"  -> recall_actual={hit_by_actual}/{len(matched_broad)}")
        print()


if __name__ == "__main__":
    main()
