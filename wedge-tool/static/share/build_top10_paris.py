#!/usr/bin/env python3
"""
build_top10_paris.py — génère meme PNG 1080x1080 top arrondissements Paris % non-conformité.
Source : observatoire BailleurVérif (dedup combine 3 vagues CSV + listings scored).
Output : top10-arrondissements-paris-2026-05.png
"""
import csv
import glob
import json
import os
from collections import defaultdict
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # static/
PROJECT_ROOT = os.path.dirname(os.path.dirname(ROOT))  # saas-florian/
OUT = os.path.join(os.path.dirname(__file__), "top10-arrondissements-paris-2026-05.png")


def aggregate():
    seen = set()
    data = defaultdict(lambda: {"enc": 0, "total": 0})
    # Listings scored
    for f in sorted(glob.glob(os.path.join(PROJECT_ROOT, "wedge-tool/data/listings/locservice-paris-*.scored.jsonl"))):
        for line in open(f):
            try:
                r = json.loads(line)
            except Exception:
                continue
            aid = r.get("accommodation_id", "")
            if aid in seen:
                continue
            seen.add(aid)
            cp = r.get("code_postal", "")
            if not cp.startswith("75"):
                continue
            data[cp]["total"] += 1
            if r.get("violation_type") == "encadrement":
                data[cp]["enc"] += 1
    # Observatoire CSV (fallback for waves without scored.jsonl)
    for f in sorted(glob.glob(os.path.join(PROJECT_ROOT, "wedge-tool/static/data/observatoire-annonces-loyer-*.csv"))):
        for r in csv.DictReader(open(f)):
            cp = r.get("code_postal", "")
            if not cp.startswith("75"):
                continue
            aid = r.get("accommodation_id", "")
            if aid in seen:
                continue
            seen.add(aid)
            data[cp]["total"] += 1
            if r.get("violation_type") == "encadrement":
                data[cp]["enc"] += 1
    return data


def load_font(size, bold=False):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ]
    for p in candidates:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def main():
    data = aggregate()
    total_all = sum(d["total"] for d in data.values())
    total_enc = sum(d["enc"] for d in data.values())
    pct_all = 100 * total_enc / max(total_all, 1)

    # Honesty: filter N >= 2 (les N=1 ne sont pas un signal défendable).
    eligible = [(cp, d) for cp, d in data.items() if d["total"] >= 2]
    # Sort: % desc, then N desc (tie-break preferring higher sample)
    rows = sorted(eligible, key=lambda kv: (-kv[1]["enc"] / max(kv[1]["total"], 1), -kv[1]["total"]))
    top = rows[:10]

    # Canvas
    W, H = 1080, 1080
    BG = (245, 247, 250)
    INK = (17, 24, 39)
    MUTED = (107, 114, 128)
    RED = (220, 38, 38)
    AMBER = (217, 119, 6)
    GREEN = (5, 150, 105)

    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # Top accent band
    d.rectangle([0, 0, W, 12], fill=RED)

    # Title
    f_title = load_font(54, bold=True)
    f_sub = load_font(28, bold=False)
    f_huge = load_font(96, bold=True)
    f_lbl = load_font(30, bold=True)
    f_val = load_font(26, bold=True)
    f_foot = load_font(22, bold=False)
    f_tag = load_font(20, bold=True)

    d.text((60, 50), "Loyers Paris : annonces", fill=INK, font=f_title)
    d.text((60, 110), "qui dépassent le plafond légal", fill=INK, font=f_title)

    # Headline number
    headline = f"{pct_all:.0f}%"
    d.text((60, 195), headline, fill=RED, font=f_huge)
    d.text((60, 305), f"des {total_all} annonces Paris scrappées", fill=MUTED, font=f_sub)
    d.text((60, 340), "violent l'encadrement des loyers", fill=MUTED, font=f_sub)

    # Bars area
    bar_top = 410
    bar_h = 42
    bar_gap = 8
    label_w = 220
    bar_x0 = 60 + label_w
    bar_x_max = W - 60
    bar_width_full = bar_x_max - bar_x0

    for i, (cp, dd) in enumerate(top):
        pct = 100 * dd["enc"] / max(dd["total"], 1)
        y = bar_top + i * (bar_h + bar_gap)
        # Label (arrondissement)
        arr = cp[-2:]
        try:
            label = f"Paris {int(arr)}ᵉ"
        except Exception:
            label = cp
        d.text((60, y + 7), label, fill=INK, font=f_lbl)
        # Bar background
        d.rectangle([bar_x0, y, bar_x_max, y + bar_h], fill=(229, 231, 235))
        # Bar fill
        bw = int(bar_width_full * pct / 100)
        color = RED if pct >= 70 else (AMBER if pct >= 40 else GREEN)
        d.rectangle([bar_x0, y, bar_x0 + bw, y + bar_h], fill=color)
        # Value text (right of bar)
        val_txt = f"{pct:.0f}%  ({dd['enc']}/{dd['total']})"
        txt_color = (255, 255, 255) if pct >= 8 else INK
        d.text((bar_x0 + 12, y + 9), val_txt, fill=txt_color, font=f_val)

    # Footer (source)
    foot_y = H - 130
    d.line([(60, foot_y - 20), (W - 60, foot_y - 20)], fill=(229, 231, 235), width=2)
    d.text((60, foot_y), f"Source : observatoire BailleurVérif — N={total_all} annonces (vagues 17-19 mai 2026, dedup, N≥2/arr.).", fill=MUTED, font=f_foot)
    d.text((60, foot_y + 32), "Dataset CC-BY-4.0 sur data.gouv.fr — méthode : prix > plafond Art. 17 loi ALUR.", fill=MUTED, font=f_foot)

    # Brand
    d.rectangle([0, H - 50, W, H], fill=INK)
    d.text((60, H - 38), "bailleurverif.fr  /  vérifie ton loyer en 5 sec.", fill=(255, 255, 255), font=f_tag)

    img.save(OUT, "PNG", optimize=True)
    print(f"OK {OUT} ({os.path.getsize(OUT)} bytes) N={total_all} enc={total_enc} {pct_all:.1f}%")


if __name__ == "__main__":
    main()
