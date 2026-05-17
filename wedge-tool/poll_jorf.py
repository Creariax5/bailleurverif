#!/usr/bin/env python3
"""
poll_jorf.py — Feature A watch-list (run-125).

Scanne les archives quotidiennes du Journal Officiel (DILA OPENDATA JORF),
filtre les textes par mots-clés liés au logement / bail / DPE / encadrement,
persiste les entrées matchées dans data/reglementation-changes.jsonl.

Source : https://echanges.dila.gouv.fr/OPENDATA/JORF/
  (Apache index — listing public sans clé, tarballs ~100K-10M)
État de polling : data/jorf_poll_state.json (last_seen_tarball, last_run_at)
Dédup : (CID, NOR) idempotent — relancer = safe, append-only mais sans doublons.

Usage : python3 poll_jorf.py [--lookback-days N] [--dry-run]
Cron suggéré : */30 * * * * (toutes les 30min — DILA publie 1-2 fois/jour).
"""
import argparse
import json
import os
import re
import sys
import tarfile
import tempfile
import time
import urllib.parse
import urllib.request
import urllib.error
from datetime import datetime, timezone, timedelta

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT, "data")
os.makedirs(DATA_DIR, exist_ok=True)

CHANGES_FILE = os.path.join(DATA_DIR, "reglementation-changes.jsonl")
STATE_FILE = os.path.join(DATA_DIR, "jorf_poll_state.json")

DILA_INDEX = "https://echanges.dila.gouv.fr/OPENDATA/JORF/"
UA = "BailleurVerif/1.0 (+https://bailleurverif.fr) DILA-JORF-watcher"
HTTP_TIMEOUT = 30

# Mots-clés de filtrage par topic. Tout texte JORF dont le TITRE_TXT matche
# au moins un mot-clé sous un topic est rangé sous ce topic.
# Casse insensitive, accents NFC (regex matched on raw XML titles).
TOPIC_KEYWORDS = {
    "loyer-legal": [
        r"\bloyer", r"\bencadrement (des )?loyer",
        r"\bzones? tendues?", r"\bplafonn?ement (du )?loyer",
        r"\bréférence des loyers", r"loi\s+ALUR", r"loi\s+ELAN",
    ],
    "dpe-bailleur": [
        r"\bDPE\b", r"diagnostic de performance énergétique",
        r"performance énergétique", r"étiquettes? énergie",
        r"passoires? thermiques?", r"audit énergétique",
        r"rénovation\s+(énergétique|thermique)",
        r"classe[s]? énergétique[s]?",
    ],
    "aides-financieres": [
        r"certificats?\s+d'économies?\s+d'énergie",
        r"MaPrimeRén",
        r"\bFEEBAT\b", r"\bPROFEEL\b",
        r"aides?\s+(à|aux|pour)\s+la\s+rénovation",
        r"\bAPL\b", r"aide personnalisée au logement",
        r"prêt à taux zéro", r"\bPTZ\b",
        r"éco-prêt", r"éco\s*PTZ",
        r"crédit d'impôt.*transition énergétique", r"\bCITE\b",
    ],
    "preavis": [
        r"\bpréavis", r"\bbail (d'habitation|de location|locatif)",
        r"\brésiliation du contrat de location",
    ],
    "veille-reglementaire": [
        r"\blogement", r"\blocataire", r"\bbailleur",
        r"\blocation", r"copropriété",
        r"décence du logement", r"habitabilité",
        r"loi\s+(Climat|Résilience|ALUR|ELAN|Macron)",
        r"\bcommission départementale de conciliation",
    ],
    "mon-bien": [
        r"\bdéficit foncier", r"\bLMNP\b", r"\bmeublé[e]? touristique",
        r"\btaxe foncière", r"\baides? au logement",
    ],
}
COMPILED_TOPIC_KEYWORDS = {
    topic: [re.compile(p, re.IGNORECASE) for p in patterns]
    for topic, patterns in TOPIC_KEYWORDS.items()
}

# Date globale de cutoff : pas plus loin que NOW-180j même si lookback-days demandé.
HARD_CUTOFF_DAYS = 180


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def log(msg):
    sys.stdout.write(f"[{now_iso()}] {msg}\n")
    sys.stdout.flush()


def load_state():
    if not os.path.exists(STATE_FILE):
        return {"last_seen_tarballs": [], "last_run_at": None, "runs_lifetime": 0}
    try:
        with open(STATE_FILE) as f:
            return json.load(f)
    except Exception:
        return {"last_seen_tarballs": [], "last_run_at": None, "runs_lifetime": 0}


def save_state(state):
    tmp = STATE_FILE + ".tmp"
    with open(tmp, "w") as f:
        json.dump(state, f, indent=2)
    os.replace(tmp, STATE_FILE)


def load_existing_keys():
    """Retourne set((cid, nor)) déjà persistés pour dédup."""
    keys = set()
    if not os.path.exists(CHANGES_FILE):
        return keys
    with open(CHANGES_FILE) as f:
        for line in f:
            try:
                e = json.loads(line)
                keys.add((e.get("cid") or "", e.get("nor") or ""))
            except Exception:
                continue
    return keys


def append_change(entry):
    with open(CHANGES_FILE, "a") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def list_dila_tarballs(lookback_days):
    """Renvoie la liste des tarballs JORF datant des `lookback_days` derniers jours."""
    req = urllib.request.Request(DILA_INDEX, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT) as r:
        html = r.read().decode("utf-8", errors="ignore")
    # JORF_YYYYMMDD-HHMMSS.tar.gz
    pattern = re.compile(r'JORF_(\d{4})(\d{2})(\d{2})-(\d{6})\.tar\.gz')
    cutoff = datetime.now(timezone.utc) - timedelta(days=min(lookback_days, HARD_CUTOFF_DAYS))
    matches = []
    seen = set()
    for m in pattern.finditer(html):
        fname = m.group(0)
        if fname in seen:
            continue
        seen.add(fname)
        try:
            d = datetime(int(m.group(1)), int(m.group(2)), int(m.group(3)), tzinfo=timezone.utc)
        except Exception:
            continue
        if d < cutoff:
            continue
        matches.append(fname)
    matches.sort()
    return matches


def parse_section_ta_xml(xml_bytes):
    """Extrait (titre, cid, nor, nature, date_publi, date_signature, ministere, eli)
    depuis un fichier section_ta XML. Renvoie None si pas un texte standalone."""
    txt = xml_bytes.decode("utf-8", errors="ignore")
    titre_m = re.search(r'<TITRE_TXT[^>]*>(.*?)</TITRE_TXT>', txt, re.DOTALL)
    if not titre_m:
        return None
    titre = re.sub(r'\s+', ' ', titre_m.group(1)).strip()
    if not titre or len(titre) < 8:
        return None
    texte_m = re.search(r'<TEXTE\s+([^>]+)>', txt)
    attrs = {}
    if texte_m:
        for am in re.finditer(r'(\w+)="([^"]*)"', texte_m.group(1)):
            attrs[am.group(1)] = am.group(2)
    return {
        "titre": titre,
        "cid": attrs.get("cid", ""),
        "nor": attrs.get("nor", ""),
        "nature": attrs.get("nature", ""),
        "date_publi": attrs.get("date_publi", ""),
        "date_signature": attrs.get("date_signature", ""),
        "ministere": attrs.get("ministere", ""),
        "num_jo": attrs.get("num_parution_jo", ""),
    }


def classify_topics(titre):
    """Renvoie liste topics matchant. Vide si aucun."""
    topics = []
    keywords_hit = []
    for topic, patterns in COMPILED_TOPIC_KEYWORDS.items():
        for p in patterns:
            if p.search(titre):
                topics.append(topic)
                keywords_hit.append(p.pattern)
                break
    return topics, keywords_hit


def process_tarball(fname, dedup_keys, dry_run=False):
    """Télécharge + extrait + scanne un tarball. Renvoie nouvelles entrées matchées."""
    url = DILA_INDEX + fname
    log(f"FETCH {fname}")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT) as r:
            body = r.read()
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
        log(f"  ERROR fetch {fname}: {e}")
        return [], "fetch_error"

    new_entries = []
    seen_in_tarball = set()
    try:
        with tarfile.open(fileobj=__import__("io").BytesIO(body), mode="r:gz") as tar:
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
                key = (parsed["cid"], parsed["nor"])
                if key in dedup_keys or key in seen_in_tarball:
                    continue
                topics, kw_hit = classify_topics(parsed["titre"])
                if not topics:
                    continue
                # Filtre temporel : date_publi doit être dans la fenêtre lookback.
                # Évite de re-remonter des textes anciens consolidés re-inclus.
                if parsed.get("date_publi"):
                    try:
                        dpub = datetime.strptime(parsed["date_publi"], "%Y-%m-%d").replace(tzinfo=timezone.utc)
                        cutoff_pub = datetime.now(timezone.utc) - timedelta(days=180)
                        if dpub < cutoff_pub:
                            continue
                    except Exception:
                        pass
                seen_in_tarball.add(key)
                eli_url = ""
                if parsed["nature"] and parsed["date_signature"] and parsed["nor"]:
                    # Format ELI Légifrance : /eli/{nature}/{yyyy}/{m}/{d}/{nor}/jo/texte
                    try:
                        y, m, d = parsed["date_signature"].split("-")
                        nature_low = parsed["nature"].lower()
                        eli_url = f"https://www.legifrance.gouv.fr/eli/{nature_low}/{int(y)}/{int(m)}/{int(d)}/{parsed['nor']}/jo/texte"
                    except Exception:
                        pass
                entry = {
                    "ts_detected": now_iso(),
                    "topics": topics,
                    "keywords_matched": kw_hit[:6],
                    "nature": parsed["nature"],
                    "titre": parsed["titre"],
                    "cid": parsed["cid"],
                    "nor": parsed["nor"],
                    "date_publi": parsed["date_publi"],
                    "date_signature": parsed["date_signature"],
                    "ministere": parsed["ministere"],
                    "num_jo": parsed["num_jo"],
                    "source_tarball": fname,
                    "source": "DILA JORF OPENDATA",
                    "eli_url": eli_url,
                }
                new_entries.append(entry)
    except tarfile.TarError as e:
        log(f"  ERROR untar {fname}: {e}")
        return [], "tar_error"

    log(f"  scanned, matched_new={len(new_entries)}")
    if not dry_run:
        for e in new_entries:
            append_change(e)
            dedup_keys.add((e["cid"], e["nor"]))
    return new_entries, "ok"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lookback-days", type=int, default=14,
                    help="Combien de jours en arrière scanner depuis aujourd'hui.")
    ap.add_argument("--dry-run", action="store_true",
                    help="Ne pas écrire reglementation-changes.jsonl.")
    ap.add_argument("--max-tarballs", type=int, default=40,
                    help="Limite # tarballs traités en 1 run (safety).")
    args = ap.parse_args()

    state = load_state()
    dedup = load_existing_keys()
    log(f"INIT existing_changes={len(dedup)} state_runs_lifetime={state.get('runs_lifetime', 0)}")

    try:
        tarballs = list_dila_tarballs(args.lookback_days)
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
        log(f"ERROR list DILA index: {e}")
        return 2

    already = set(state.get("last_seen_tarballs", []))
    to_process = [t for t in tarballs if t not in already][: args.max_tarballs]
    log(f"DILA index tarballs={len(tarballs)} new_to_process={len(to_process)} cap={args.max_tarballs}")

    total_new = 0
    processed_ok = []
    for fname in to_process:
        new, status = process_tarball(fname, dedup, dry_run=args.dry_run)
        total_new += len(new)
        if status == "ok":
            processed_ok.append(fname)
        time.sleep(0.5)  # courtesie DILA

    if not args.dry_run:
        # On garde un sliding window des 200 derniers tarballs pour borner la taille du state.
        merged = list(set(state.get("last_seen_tarballs", []) + processed_ok))
        merged.sort()
        state["last_seen_tarballs"] = merged[-200:]
        state["last_run_at"] = now_iso()
        state["runs_lifetime"] = state.get("runs_lifetime", 0) + 1
        save_state(state)

    log(f"DONE total_new_entries={total_new} processed_tarballs_ok={len(processed_ok)} "
        f"changes_file_now={CHANGES_FILE}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
