#!/usr/bin/env python3
"""Export observatoire JSONL → CSV with normalized columns.

Usage: export_observatoire_csv.py [YYYY-MM-DD]   (default: today UTC)

Reads:  wedge-tool/data/listings/all-cities-<DATE>.dedup.scored.jsonl
Writes: wedge-tool/static/data/observatoire-annonces-loyer-<DATE>.csv

Backward compat: if no scored file exists for today, falls back to most recent.
"""
import csv, json, sys, hashlib, datetime, glob
from pathlib import Path

LISTINGS_DIR = Path("/home/deploy/saas-florian/wedge-tool/data/listings")
STATIC_DIR = Path("/home/deploy/saas-florian/wedge-tool/static/data")

def resolve_date(argv):
    if len(argv) > 1 and argv[1] and argv[1] != "-":
        return argv[1]
    today = datetime.datetime.utcnow().strftime("%Y-%m-%d")
    if (LISTINGS_DIR / f"all-cities-{today}.dedup.scored.jsonl").exists():
        return today
    candidates = sorted(glob.glob(str(LISTINGS_DIR / "all-cities-*.dedup.scored.jsonl")))
    if not candidates:
        print("ERROR: no scored files found", file=sys.stderr)
        sys.exit(1)
    return Path(candidates[-1]).name.split("all-cities-")[1].split(".")[0]

DATE = resolve_date(sys.argv)
SRC = LISTINGS_DIR / f"all-cities-{DATE}.dedup.scored.jsonl"
DST = STATIC_DIR / f"observatoire-annonces-loyer-{DATE}.csv"

FIELDS = [
    "ts_score",
    "source",
    "url_hash",
    "accommodation_id",
    "ville_label",
    "code_postal",
    "code_dept",
    "in_scope_encadrement",
    "surface_m2",
    "loyer_eur_total",
    "eur_per_m2",
    "dpe_letter",
    "ges_letter",
    "meuble",
    "commune_slug",
    "plafond_applied_eur_m2",
    "encadrement_violation",
    "encadrement_excess_eur_m2",
    "encadrement_excess_pct",
    "dpe_violation",
    "violation_type",
    "violation_score",
    "score_version",
]

def derive_dept(cp):
    if not cp or not isinstance(cp, str):
        return ""
    cp = cp.strip()
    if cp.startswith("20"):
        return "2A_or_2B"
    return cp[:2] if len(cp) >= 2 else ""

def main():
    if not SRC.exists():
        print(f"ERROR: source missing {SRC}", file=sys.stderr)
        sys.exit(1)
    DST.parent.mkdir(parents=True, exist_ok=True)
    n_in = n_out = 0
    seen_hash = set()
    with SRC.open() as fin, DST.open("w", newline="") as fout:
        w = csv.DictWriter(fout, fieldnames=FIELDS, quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        for line in fin:
            line = line.strip()
            if not line:
                continue
            n_in += 1
            r = json.loads(line)
            uh = r.get("url_hash") or hashlib.sha1((r.get("url") or "").encode()).hexdigest()[:16]
            if uh in seen_hash:
                continue
            seen_hash.add(uh)
            row = {
                "ts_score": r.get("score_ts", ""),
                "source": r.get("source", ""),
                "url_hash": uh,
                "accommodation_id": r.get("accommodation_id", ""),
                "ville_label": r.get("ville_label", ""),
                "code_postal": r.get("code_postal", ""),
                "code_dept": derive_dept(r.get("code_postal", "")),
                "in_scope_encadrement": "true" if r.get("plafond_applied_eur_m2") is not None else "false",
                "surface_m2": r.get("surface_m2", ""),
                "loyer_eur_total": r.get("loyer_eur_total", ""),
                "eur_per_m2": r.get("eur_per_m2", ""),
                "dpe_letter": r.get("dpe_letter", "") or "",
                "ges_letter": r.get("ges_letter", "") or "",
                "meuble": "true" if r.get("meuble") else "false",
                "commune_slug": r.get("commune_slug", "") or "",
                "plafond_applied_eur_m2": r.get("plafond_applied_eur_m2", "") if r.get("plafond_applied_eur_m2") is not None else "",
                "encadrement_violation": r.get("encadrement_violation", "") or "",
                "encadrement_excess_eur_m2": r.get("encadrement_excess_eur_m2", "") if r.get("encadrement_excess_eur_m2") is not None else "",
                "encadrement_excess_pct": r.get("encadrement_excess_pct", "") if r.get("encadrement_excess_pct") is not None else "",
                "dpe_violation": r.get("dpe_violation", "") or "",
                "violation_type": r.get("violation_type", "") or "",
                "violation_score": r.get("violation_score", 0),
                "score_version": r.get("score_version", ""),
            }
            w.writerow(row)
            n_out += 1
    size = DST.stat().st_size
    print(f"OK rows_in={n_in} rows_out={n_out} bytes={size} dst={DST}")

if __name__ == "__main__":
    main()
