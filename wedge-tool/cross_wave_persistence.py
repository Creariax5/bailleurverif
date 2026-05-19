#!/usr/bin/env python3
"""Cross-wave persistence: which non-conform listings appear in N consecutive daily waves.

Reads:  wedge-tool/static/data/observatoire-annonces-loyer-YYYY-MM-DD.csv (all available)
Writes: wedge-tool/static/data/cross-wave-persistence.json

Signal: a listing whose url_hash persists across waves = bailleur n'a pas corrigé
la non-conformité dans le délai = preuve structurelle d'inaction. La chain est
non-backfillable: un concurrent qui démarre demain n'a pas l'historique.
"""
import csv, glob, json, datetime
from pathlib import Path
from collections import defaultdict

STATIC = Path("/home/deploy/saas-florian/wedge-tool/static/data")
PATTERN = "observatoire-annonces-loyer-*.csv"

def load_wave(path):
    rows = {}
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            h = r.get("url_hash")
            if h:
                rows[h] = r
    return rows

def main():
    files = sorted(glob.glob(str(STATIC / PATTERN)))
    if len(files) < 2:
        print(f"need >=2 waves, found {len(files)}")
        return
    waves = [(Path(f).stem.split("loyer-")[1], load_wave(f)) for f in files]
    presence = defaultdict(list)
    for date, rows in waves:
        for h in rows:
            presence[h].append(date)
    counts = defaultdict(int)
    for h, dates in presence.items():
        counts[len(dates)] += 1
    all_dates = [d for d, _ in waves]
    triple_hashes = sorted(h for h, dates in presence.items() if len(dates) == len(all_dates))
    triple_sample = []
    last_wave_rows = waves[-1][1]
    for h in triple_hashes[:20]:
        r = last_wave_rows.get(h, {})
        triple_sample.append({
            "url_hash": h,
            "ville_label": r.get("ville_label"),
            "code_dept": r.get("code_dept"),
            "loyer_eur_total": r.get("loyer_eur_total"),
            "surface_m2": r.get("surface_m2"),
            "dpe_letter": r.get("dpe_letter"),
            "violation_type": r.get("violation_type"),
        })
    last_n = len(waves[-1][1])
    persistence_rate_full = round(100 * counts[len(all_dates)] / last_n, 1) if last_n else 0
    out = {
        "schema_version": "0.1",
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "waves": [{"date": d, "n": len(r)} for d, r in waves],
        "wave_count": len(waves),
        "presence_distribution": {
            f"{k}_waves": v for k, v in sorted(counts.items())
        },
        "persistence_rate_full_chain_pct": persistence_rate_full,
        "persistence_rate_full_chain_note": (
            f"{counts[len(all_dates)]} listings present in all {len(all_dates)} waves "
            f"/ {last_n} listings in last wave = {persistence_rate_full}% of last-wave "
            f"non-conform listings have persisted unchanged for {len(all_dates)} consecutive days."
        ),
        "interpretation": (
            "A persistence_rate >50% indicates structural inaction: bailleurs do not remove "
            "non-conform listings within days. Each additional wave appended (cron daily) "
            "extends the temporal proof-of-inaction asset. The git-timestamped CSV chain "
            "(Creariax5/bailleurverif) provides cryptographic antedating: an entrant "
            "cannot backfill this signal."
        ),
        "sample_triple_persistence": triple_sample,
    }
    dst = STATIC / "cross-wave-persistence.json"
    dst.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {dst} (waves={len(waves)}, full-chain={counts[len(all_dates)]}, "
          f"rate={persistence_rate_full}%)")

if __name__ == "__main__":
    main()
