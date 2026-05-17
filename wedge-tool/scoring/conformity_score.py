#!/usr/bin/env python3
"""
Conformity scoring pipeline — moat-builder MISSION Option 1 (DIRECTIVE 9).

Input  : JSONL output from wedge-tool/crawler/locservice_v0.py
         (one annonce per line, fields: code_postal, surface_m2, loyer_eur_total,
         dpe_letter, ges_letter, title, url_hash, ts, ...)

Output : JSONL one record per scored annonce, with added fields :
  - eur_per_m2 (float|None)
  - meuble (bool|None)         — inferred from title
  - commune_slug (str|None)    — matched against encadrement reference
  - plafond_applied_eur_m2 (float|None)
  - encadrement_violation (str)   — "none" | "presumed" | "clear"  (clear = >+10%)
  - encadrement_excess_eur_m2 (float|None)
  - encadrement_excess_pct (float|None)
  - dpe_violation (str)           — "none" | "presumed_G_2025" | "future_F_2028" | "future_E_2034"
  - violation_type (str)          — "none" | "encadrement" | "dpe" | "both"
  - violation_score (int)         — 0..3 (0=none, 1=encadrement OR dpe presumed,
                                         2=clear encadrement OR DPE G, 3=clear+G)
  - score_version (str)           — semver of scoring rules
  - score_ts (iso)

Caveats (V0 — documented in observatoire-annonces.html):
  * plafond_meuble / plafond_nu are MAXIMUM caps per commune ; real Paris encadrement
    is per arrondissement × type × epoch (loyer médian majoré). V0 = strict upper bound :
    if loyer/m² > plafond_max → "presumed_violation" (probably illegal) ; >+10% → "clear".
    A listing below the max cap is NOT guaranteed legal — only that it's not above the
    universal ceiling. Use this metric as a LOWER BOUND on real non-conformity %.
  * DPE calendar 2025-2034 (loi Climat & Résilience 2021):
      - G interdit location nouveau bail depuis 2025-01-01
      - F interdit 2028-01-01
      - E interdit 2034-01-01
    Existing leases grandfathered. We flag G as "presumed violation" for 2026.
"""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

SCORE_VERSION = "0.1.0"
HERE = Path(__file__).resolve().parent
REF_PATH = (
    HERE.parent / "static" / "data" / "encadrement-loyer-france-2026.json"
)

# Postal-code prefix → commune slug. V0 covers the 31 communes in the reference
# dataset that are explicitly under encadrement préfectoral.
# Paris (75) maps regardless of arrondissement; intercommunalités MEL/Lyon/etc
# map by CP. Extend as the reference dataset grows.
CP_TO_SLUG = {
    "75": "paris",
    "59000": "lille",
    "59260": "hellemmes",
    "59160": "lomme",
    "69003": "lyon",
    "69001": "lyon",
    "69002": "lyon",
    "69004": "lyon",
    "69005": "lyon",
    "69006": "lyon",
    "69007": "lyon",
    "69008": "lyon",
    "69009": "lyon",
    "69100": "villeurbanne",
    "93000": "bobigny",
    "93200": "saint-denis",
    "93220": "gagny",  # placeholder, not in zone tendue strict
    "93240": "stains",
    "93300": "aubervilliers",
    "93310": "le-pre-saint-gervais",
    "93330": "neuilly-sur-marne",
    "93350": "le-bourget",
    "93380": "pierrefitte-sur-seine",
    "93400": "saint-ouen",
    "93410": "vaujours",
    "93430": "villetaneuse",
    "93440": "dugny",
    "93450": "ile-saint-denis",
    "93500": "pantin",
    "93600": "aulnay-sous-bois",
    "93700": "drancy",
    "93800": "epinay-sur-seine",
}

# DPE letters interdites à la location nouveau bail à date donnée (loi Climat 2021).
DPE_BAN_CALENDAR = [
    ("G", "2025-01-01"),
    ("F", "2028-01-01"),
    ("E", "2034-01-01"),
]


def load_reference() -> dict[str, dict]:
    with REF_PATH.open(encoding="utf-8") as f:
        data = json.load(f)
    return {c["slug"]: c for c in data["communes"]}


def infer_meuble(title: str) -> bool | None:
    if not title:
        return None
    t = title.lower()
    if "meublé" in t or "meuble" in t.replace("é", "e"):
        return True
    if "non meublé" in t or "nu " in t or t.endswith(" nu") or "vide" in t:
        return False
    return None


def cp_to_slug(cp: str | None) -> str | None:
    if not cp:
        return None
    if cp in CP_TO_SLUG:
        return CP_TO_SLUG[cp]
    # Paris arrondissements 75001-75020 → "paris"
    if cp.startswith("75") and len(cp) == 5:
        return "paris"
    # Lyon 69001-69009 → lyon
    if cp.startswith("690") and len(cp) == 5:
        return "lyon"
    return None


def score_encadrement(
    eur_per_m2: float | None,
    meuble: bool | None,
    commune_row: dict | None,
) -> tuple[str, float | None, float | None, float | None]:
    """Returns (violation, plafond_applied, excess_eur_m2, excess_pct)."""
    if eur_per_m2 is None or commune_row is None:
        return ("none", None, None, None)
    if meuble is True:
        plafond = commune_row.get("plafond_meuble_eur_m2")
    elif meuble is False:
        plafond = commune_row.get("plafond_nu_eur_m2")
    else:
        # Unknown → apply the HIGHER cap (meublé) to be conservative
        plafond = commune_row.get("plafond_meuble_eur_m2")
    if plafond is None:
        return ("none", None, None, None)
    excess = eur_per_m2 - plafond
    pct = (excess / plafond) * 100.0
    if excess <= 0:
        return ("none", plafond, 0.0, 0.0)
    if pct >= 10.0:
        return ("clear", plafond, round(excess, 2), round(pct, 1))
    return ("presumed", plafond, round(excess, 2), round(pct, 1))


def score_dpe(letter: str | None, ref_date: str | None = None) -> str:
    """V0 : only G is interdit in 2026. F/E flagged as future."""
    if not letter:
        return "none"
    letter = letter.upper().strip()
    today = ref_date or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    for lt, ban_date in DPE_BAN_CALENDAR:
        if letter == lt:
            if today >= ban_date:
                return f"presumed_{lt}_{ban_date[:4]}"
            return f"future_{lt}_{ban_date[:4]}"
    return "none"


def score_record(rec: dict, ref: dict[str, dict]) -> dict:
    surface = rec.get("surface_m2")
    loyer = rec.get("loyer_eur_total")
    eur_per_m2 = round(loyer / surface, 2) if (surface and loyer) else None
    meuble = infer_meuble(rec.get("title") or "")
    slug = cp_to_slug(rec.get("code_postal"))
    commune_row = ref.get(slug) if slug else None
    enc_v, plafond, excess, excess_pct = score_encadrement(
        eur_per_m2, meuble, commune_row
    )
    dpe_v = score_dpe(rec.get("dpe_letter"))
    dpe_clear = dpe_v.startswith("presumed_")
    has_enc = enc_v in ("presumed", "clear")
    has_dpe = dpe_clear
    if has_enc and has_dpe:
        vtype = "both"
    elif has_enc:
        vtype = "encadrement"
    elif has_dpe:
        vtype = "dpe"
    else:
        vtype = "none"
    score = 0
    if enc_v == "presumed":
        score += 1
    elif enc_v == "clear":
        score += 2
    if dpe_clear:
        score += 1 if rec.get("dpe_letter", "").upper() != "G" else 2
        # G > F > E severity already encoded by calendar
    score = min(score, 3)
    out = dict(rec)
    out.update(
        {
            "eur_per_m2": eur_per_m2,
            "meuble": meuble,
            "commune_slug": slug,
            "plafond_applied_eur_m2": plafond,
            "encadrement_violation": enc_v,
            "encadrement_excess_eur_m2": excess,
            "encadrement_excess_pct": excess_pct,
            "dpe_violation": dpe_v,
            "violation_type": vtype,
            "violation_score": score,
            "score_version": SCORE_VERSION,
            "score_ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        }
    )
    return out


def main(inputs: list[str], out_path: str | None = None):
    log = lambda *a: print("[conformity_score]", *a, flush=True)
    ref = load_reference()
    log(f"loaded {len(ref)} communes from reference")
    written = 0
    n_total = 0
    n_violation = 0
    by_type = {"none": 0, "encadrement": 0, "dpe": 0, "both": 0}
    rows_out: list[str] = []
    for p in inputs:
        path = Path(p)
        log(f"reading {path}")
        with path.open(encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                rec = json.loads(line)
                scored = score_record(rec, ref)
                n_total += 1
                by_type[scored["violation_type"]] += 1
                if scored["violation_type"] != "none":
                    n_violation += 1
                rows_out.append(json.dumps(scored, ensure_ascii=False))
    if out_path:
        outp = Path(out_path)
        outp.parent.mkdir(parents=True, exist_ok=True)
        with outp.open("w", encoding="utf-8") as f:
            for r in rows_out:
                f.write(r + "\n")
        written = len(rows_out)
        log(f"wrote {written} scored records -> {outp}")
    else:
        for r in rows_out:
            print(r)
    log(
        f"TOTAL={n_total} violations={n_violation} "
        f"none={by_type['none']} encadrement={by_type['encadrement']} "
        f"dpe={by_type['dpe']} both={by_type['both']}"
    )
    return rows_out


if __name__ == "__main__":
    args = sys.argv[1:]
    out = None
    if "-o" in args:
        i = args.index("-o")
        out = args[i + 1]
        args = args[:i] + args[i + 2 :]
    if not args:
        print("usage: conformity_score.py [-o out.jsonl] in1.jsonl [in2.jsonl ...]")
        sys.exit(2)
    main(args, out_path=out)
