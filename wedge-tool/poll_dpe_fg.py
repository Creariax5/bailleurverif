#!/usr/bin/env python3
"""
poll_dpe_fg.py — Moat-builder #1 / DIRECTIVE 9.

Crawl quotidien ADEME DPE Logements existants (dataset `dpe03existant`) pour les
nouveaux diagnostics DPE F/G dans les 31 communes prioritaires (zones tendues +
encadrement loyer + métropoles). Accumule un flux JSONL local + état de pagination
par INSEE.

Pourquoi moat (catégorie 1 données propriétaires accumulées) :
- Time-series construite jour après jour, impossible à reconstituer
  rétroactivement par un concurrent (ADEME ne stocke pas l'historique de découverte
  côté client).
- Devient observatoire public "Annonces logements F/G qui vont être proposés à la
  location FR" plus la base grossit.
- L'avantage défensif augmente linéairement avec le temps : T+30j = 30 jours d'avance.

Usage:
    python3 poll_dpe_fg.py                     # crawl prio des 31 INSEE codes
    python3 poll_dpe_fg.py --insee 75101       # 1 seul code
    python3 poll_dpe_fg.py --max-per-insee 50  # rotation rapide

Sortie:
    data/dpe-fg-stream.jsonl       (append-only, dedup par clé hash)
    data/dpe_fg_poll_state.json    (anchors par INSEE + runs_lifetime)
    data/dpe-fg-rollup.json        (agrégation live par commune, regen full)
"""

import argparse
import hashlib
import json
import os
import sys
import time
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from datetime import datetime, timezone

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
STREAM_PATH = os.path.join(DATA_DIR, "dpe-fg-stream.jsonl")
STATE_PATH = os.path.join(DATA_DIR, "dpe_fg_poll_state.json")
ROLLUP_PATH = os.path.join(DATA_DIR, "dpe-fg-rollup.json")

ADEME_BASE = "https://data.ademe.fr/data-fair/api/v1/datasets/dpe03existant/lines"
UA = "BailleurVerif-Moat/0.1 (+https://bailleurverif.fr; contact@bailleurverif.fr)"
SELECT_FIELDS = (
    "etiquette_dpe,etiquette_ges,date_etablissement_dpe,code_insee_ban,"
    "code_postal_ban,nom_commune_ban,nom_rue_ban,numero_voie_ban,"
    "surface_habitable_logement,type_batiment,annee_construction,"
    "conso_5_usages_par_m2_ep,emission_ges_5_usages_par_m2"
)
TIMEOUT = 12
DEFAULT_MAX_PER_INSEE = 25  # 25 fresh records per city / poll (=750/run for 31 codes)
SLEEP_BETWEEN_CALLS = 1.2

# 54 INSEE codes prioritaires : ADEME indexe au niveau arrondissement pour Paris /
# Lyon / Marseille (les codes "commune-mère" 69123 / 13055 ne renvoient quasi rien).
PRIORITY_INSEE = [
    # Paris 1-20
    "75101", "75102", "75103", "75104", "75105", "75106", "75107", "75108",
    "75109", "75110", "75111", "75112", "75113", "75114", "75115", "75116",
    "75117", "75118", "75119", "75120",
    # Lyon 1-9
    "69381", "69382", "69383", "69384", "69385", "69386", "69387", "69388", "69389",
    # Marseille 1-16
    "13201", "13202", "13203", "13204", "13205", "13206", "13207", "13208",
    "13209", "13210", "13211", "13212", "13213", "13214", "13215", "13216",
    # Métropoles encadrement loyer + zones tendues
    "31555",  # Toulouse
    "33063",  # Bordeaux
    "59350",  # Lille
    "44109",  # Nantes
    "67482",  # Strasbourg
    "06088",  # Nice
    "34172",  # Montpellier
    "35238",  # Rennes
    "38185",  # Grenoble
]


def _now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _load_state():
    if not os.path.exists(STATE_PATH):
        return {
            "first_run_at": _now_iso(),
            "last_run_at": None,
            "runs_lifetime": 0,
            "by_insee": {},  # insee -> {last_max_date_seen, total_seen, last_poll_at}
            "seen_keys": [],  # ring buffer of last ~5000 seen hash keys for dedupe across runs
        }
    with open(STATE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def _save_state(state):
    tmp = STATE_PATH + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)
    os.replace(tmp, STATE_PATH)


def _entry_key(rec):
    """Best-effort unique key — ADEME pas d'id stable côté client."""
    parts = [
        str(rec.get("date_etablissement_dpe") or ""),
        str(rec.get("code_insee_ban") or ""),
        str(rec.get("nom_rue_ban") or "").lower(),
        str(rec.get("numero_voie_ban") or ""),
        str(rec.get("surface_habitable_logement") or ""),
        str(rec.get("etiquette_dpe") or ""),
    ]
    h = hashlib.sha1("|".join(parts).encode("utf-8")).hexdigest()[:16]
    return h


def _fetch_one_insee(insee, max_records):
    """Fetch the latest F/G DPE for one INSEE code. Returns list[dict]."""
    qs = f"(etiquette_dpe:F OR etiquette_dpe:G) AND code_insee_ban:{insee}"
    params = {
        "qs": qs,
        "size": min(max_records, 50),
        "select": SELECT_FIELDS,
        "sort": "-date_etablissement_dpe",
    }
    url = ADEME_BASE + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "application/json",
    })
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        data = json.loads(r.read())
    return data.get("results") or [], data.get("total") or 0


def _append_stream(records):
    with open(STREAM_PATH, "a", encoding="utf-8") as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def _regen_rollup():
    """Re-aggregate the full stream into a small JSON for the public page."""
    if not os.path.exists(STREAM_PATH):
        return {"by_commune": {}, "by_etiquette": {}, "total": 0, "generated_at": _now_iso()}
    by_commune = defaultdict(lambda: {"F": 0, "G": 0, "commune": None, "insee": None, "first_seen": None, "last_seen": None})
    by_etiquette = Counter()
    total = 0
    with open(STREAM_PATH, "r", encoding="utf-8") as f:
        for line in f:
            try:
                rec = json.loads(line)
            except Exception:
                continue
            insee = rec.get("code_insee_ban") or "?"
            commune = rec.get("nom_commune_ban") or "?"
            et = rec.get("etiquette_dpe") or "?"
            date_dpe = rec.get("date_etablissement_dpe") or ""
            by_commune[insee][et] = by_commune[insee].get(et, 0) + 1
            by_commune[insee]["commune"] = commune
            by_commune[insee]["insee"] = insee
            if not by_commune[insee]["first_seen"] or date_dpe < by_commune[insee]["first_seen"]:
                by_commune[insee]["first_seen"] = date_dpe
            if not by_commune[insee]["last_seen"] or date_dpe > by_commune[insee]["last_seen"]:
                by_commune[insee]["last_seen"] = date_dpe
            by_etiquette[et] += 1
            total += 1
    rollup = {
        "by_commune": dict(by_commune),
        "by_etiquette": dict(by_etiquette),
        "total": total,
        "generated_at": _now_iso(),
        "source": "ADEME data.ademe.fr/datasets/dpe03existant",
        "license_source": "Licence Ouverte 2.0 Etalab",
    }
    tmp = ROLLUP_PATH + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(rollup, f, ensure_ascii=False, indent=2)
    os.replace(tmp, ROLLUP_PATH)
    return rollup


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--insee", action="append", default=None, help="restrict to one or more INSEE codes")
    ap.add_argument("--max-per-insee", type=int, default=DEFAULT_MAX_PER_INSEE)
    ap.add_argument("--no-write", action="store_true")
    ap.add_argument("--regen-rollup-only", action="store_true")
    args = ap.parse_args()

    os.makedirs(DATA_DIR, exist_ok=True)
    state = _load_state()

    if args.regen_rollup_only:
        rollup = _regen_rollup()
        print(json.dumps({"action": "regen_rollup", "total": rollup["total"], "by_etiquette": rollup["by_etiquette"]}, ensure_ascii=False))
        return 0

    insee_list = args.insee if args.insee else PRIORITY_INSEE
    seen_keys = set(state.get("seen_keys") or [])
    new_records = []
    fetched_total = 0
    errors = []
    by_insee_added = {}

    for insee in insee_list:
        try:
            results, total = _fetch_one_insee(insee, args.max_per_insee)
        except Exception as e:
            errors.append({"insee": insee, "error": str(e)[:160]})
            time.sleep(SLEEP_BETWEEN_CALLS)
            continue
        added = 0
        last_max_date = state.get("by_insee", {}).get(insee, {}).get("last_max_date_seen") or ""
        max_date_this_call = last_max_date
        for rec in results:
            fetched_total += 1
            k = _entry_key(rec)
            if k in seen_keys:
                continue
            seen_keys.add(k)
            rec["_seen_at"] = _now_iso()
            rec["_key"] = k
            new_records.append(rec)
            added += 1
            d = rec.get("date_etablissement_dpe") or ""
            if d > max_date_this_call:
                max_date_this_call = d
        by_insee_added[insee] = added
        state.setdefault("by_insee", {})[insee] = {
            "last_poll_at": _now_iso(),
            "last_max_date_seen": max_date_this_call,
            "total_in_ademe": total,
            "last_added": added,
        }
        time.sleep(SLEEP_BETWEEN_CALLS)

    # Trim seen_keys ring to last 8000
    seen_keys_list = list(seen_keys)
    if len(seen_keys_list) > 8000:
        seen_keys_list = seen_keys_list[-8000:]
    state["seen_keys"] = seen_keys_list

    if new_records and not args.no_write:
        _append_stream(new_records)

    state["last_run_at"] = _now_iso()
    state["runs_lifetime"] = (state.get("runs_lifetime") or 0) + 1

    if not args.no_write:
        _save_state(state)
        rollup = _regen_rollup()
    else:
        rollup = None

    summary = {
        "run_at": state["last_run_at"],
        "runs_lifetime": state["runs_lifetime"],
        "insee_polled": len(insee_list),
        "fetched_total": fetched_total,
        "new_records": len(new_records),
        "errors": errors[:5],
        "by_insee_added": by_insee_added,
        "stream_path": STREAM_PATH,
        "rollup_total": (rollup or {}).get("total"),
        "rollup_by_etiquette": (rollup or {}).get("by_etiquette"),
    }
    print(json.dumps(summary, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
