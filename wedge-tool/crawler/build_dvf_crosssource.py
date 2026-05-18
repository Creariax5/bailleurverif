#!/usr/bin/env python3
# Build cross-source observatoire: loyer eur/m2 (BV scored.jsonl) x DVF prix-m2 vente (data.gouv.fr stats_dvf.csv)
# Output: wedge-tool/static/data/observatoire-prix-vente-vs-loyer.json
import json
import statistics
import sys
from pathlib import Path

ROOT = Path("/home/deploy/saas-florian")
SCORED = ROOT / "wedge-tool/data/listings/all-cities-2026-05-17.dedup.scored.jsonl"
DVF = ROOT / "data/dvf/observatoire-dvf-crosssource-v0.json"
OUT = ROOT / "wedge-tool/static/data/observatoire-prix-vente-vs-loyer.json"

# Mapping CP -> INSEE pour les 31 communes DVF présentes
# (sources : COG INSEE / La Poste 2024)
CP_TO_INSEE = {
    # Nice
    "06000": "06088", "06100": "06088", "06200": "06088", "06300": "06088",
    # Aix-en-Provence
    "13080": "13001", "13090": "13001", "13100": "13001", "13290": "13001", "13540": "13001",
    # Marseille arrondissements
    "13009": "13209", "13011": "13211",
    # Toulouse
    "31000": "31555", "31100": "31555", "31200": "31555", "31300": "31555", "31400": "31555", "31500": "31555",
    # Bordeaux
    "33000": "33063", "33100": "33063", "33200": "33063", "33300": "33063", "33800": "33063",
    # Montpellier
    "34000": "34172", "34070": "34172", "34080": "34172", "34090": "34172",
    # Rennes
    "35000": "35238", "35200": "35238", "35700": "35238",
    # Grenoble
    "38000": "38185", "38100": "38185",
    # Nantes
    "44000": "44109", "44100": "44109", "44200": "44109", "44300": "44109",
    # Lille (intra-muros CP)
    "59000": "59350", "59160": "59350", "59260": "59350", "59777": "59350", "59800": "59350",
    # Valenciennes
    "59300": "59606",
    # Villeurbanne
    "69100": "69266",
    # Lyon arrondissements
    "69001": "69381", "69002": "69382", "69003": "69383",
    "69007": "69387", "69008": "69388", "69009": "69389",
    # Paris arrondissements
    "75001": "75101", "75004": "75104", "75007": "75107", "75010": "75110",
    "75011": "75111", "75012": "75112", "75013": "75113", "75014": "75114",
    "75015": "75115", "75016": "75116", "75017": "75117", "75018": "75118",
}


def main():
    # 1) Load DVF reference
    with DVF.open() as f:
        dvf = json.load(f)
    by_insee = {c["insee"]: c for c in dvf["communes"]}

    # 2) Aggregate loyer eur/m2 per INSEE from scored listings
    loyer_per_insee: dict[str, list[float]] = {}
    in_scope_count: dict[str, int] = {}
    skipped_no_mapping = 0
    skipped_no_surface = 0
    total = 0
    for line in SCORED.open():
        line = line.strip()
        if not line:
            continue
        total += 1
        r = json.loads(line)
        cp = (r.get("code_postal") or "").strip()
        insee = CP_TO_INSEE.get(cp)
        if not insee:
            skipped_no_mapping += 1
            continue
        try:
            eur_m2 = float(r.get("eur_per_m2") or 0)
        except (TypeError, ValueError):
            eur_m2 = 0
        if eur_m2 <= 0 or eur_m2 > 200:  # sanity bounds
            skipped_no_surface += 1
            continue
        loyer_per_insee.setdefault(insee, []).append(eur_m2)
        if r.get("in_scope_encadrement"):
            in_scope_count[insee] = in_scope_count.get(insee, 0) + 1

    # 3) Build cross rows where we have both loyer N>=3 and DVF data
    rows = []
    for insee, eurs in loyer_per_insee.items():
        if insee not in by_insee:
            continue
        n = len(eurs)
        if n < 3:
            continue
        med_loyer = statistics.median(eurs)
        dvf_row = by_insee[insee]
        med_prix = float(dvf_row["med_prix_m2_apt_eur_weighted"])
        if med_prix <= 0:
            continue
        # Rendement brut annuel = (loyer mensuel * 12) / prix_m2 = % par an
        # Note: ratio des eur/m2 sans multiplier par surface (les m² s'annulent)
        rendement_brut_pct = round((med_loyer * 12.0 / med_prix) * 100.0, 2)
        rows.append({
            "insee": insee,
            "libelle": dvf_row["libelle"],
            "loyer_eur_m2_median": round(med_loyer, 2),
            "loyer_n_annonces": n,
            "in_scope_encadrement_n": in_scope_count.get(insee, 0),
            "prix_vente_eur_m2_median_24_25": round(med_prix, 0),
            "nb_ventes_apt_24m": dvf_row["nb_ventes_apt_24m"],
            "rendement_brut_pct_annuel": rendement_brut_pct,
        })

    # Sort by rendement brut desc (best yield = top), then by libelle
    rows.sort(key=lambda x: (-x["rendement_brut_pct_annuel"], x["libelle"]))

    out = {
        "title": "Observatoire cross-source : prix de vente DVF × loyer demandé",
        "license": "CC-BY-4.0",
        "source_loyer": "BailleurVérif observatoire-annonces-loyer.csv (locservice 2026-05-17 N=236)",
        "source_prix_vente": "data.gouv.fr Statistiques DVF (object.files.data.gouv.fr/data-pipeline-open/dvf/stats_dvf.csv) — ventes-weighted médiane prix m² appartement 2024-01 → 2025-12",
        "period_loyer": "2026-05-17 (snapshot)",
        "period_prix_vente": "2024-01 .. 2025-12 (24 mois)",
        "methodologie": "Pour chaque commune INSEE présente dans les deux sources, médiane des loyers €/m² mensuel observés (annonces) divisée par médiane DVF prix €/m² vente appartement, multipliée par 12 mois × 100 = rendement brut annuel %. Indicatif investisseur : ne tient pas compte des charges, fiscalité, vacance ni travaux.",
        "caveats": [
            "Loyers = annonces (loyer demandé), pas loyer effectivement payé.",
            "DVF = ventes notariées appartement ; n'exclut pas les parkings annexes ni les ventes en VEFA atypiques.",
            "N≥3 annonces minimum par commune pour publication (échantillon faible : Paris/Lyon/Marseille arrondissements peuvent avoir N<10).",
            "Rendement brut ≠ rentabilité nette : charges, taxe foncière, vacance, GLI, frais agence non déduits.",
            "Cross-source = expérimental v0, pas garanti zéro biais d'échantillon. Open source méthodologie.",
        ],
        "n_communes_cross": len(rows),
        "n_listings_total_observatoire": total,
        "n_listings_mappes_insee": sum(len(v) for v in loyer_per_insee.values()),
        "n_listings_skipped_no_cp_mapping": skipped_no_mapping,
        "communes": rows,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2))
    print(f"OK wrote {OUT} : {len(rows)} communes cross-source / {total} listings scannés")
    return 0


if __name__ == "__main__":
    sys.exit(main())
