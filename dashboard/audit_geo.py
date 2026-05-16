#!/usr/bin/env python3
"""
Audit GEO content sur les 4 articles markdown.

Mesure 3 dimensions (cible >=3/3/3 par article, source: étude Princeton/GeorgiaTech/IIT/AI2):
 - stats chiffrees    : pourcentages, montants en €, dates/annees, surfaces, durees
 - citations sources  : urls .gouv.fr / ademe.fr / anil.org + mentions textuelles
 - quotations / lois  : loi nommee, decret n°, article L./R./D., guillemets « »

Sortie: tableau markdown sur stdout. Pas de patch automatique (humain dans la boucle).

Usage:
    python3 dashboard/audit_geo.py                # tous les articles content/*.md
    python3 dashboard/audit_geo.py path1 path2    # subset
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CONTENT_DIR = REPO / "content"

FRONTMATTER_RE = re.compile(r"^---\n.*?\n---\n", re.DOTALL)

# 1. Stats chiffrees (compte les MATCHES uniques cumules, pas les lignes)
STAT_PATTERNS = [
    r"\b\d+(?:[.,]\d+)?\s*%",                       # 18 %, 0,78%
    r"\b\d{1,3}(?:[\s ]\d{3})*\s*€",            # 5 000 €
    r"\b\d+(?:[.,]\d+)?\s*€",                        # 250€
    r"\b\d+(?:[.,]\d+)?\s*(?:kWh|m²|m2)\b",          # 50 kWh, 30 m²
    r"\b\d{4}\b(?!\s*€)",                           # annee 2025 (mais pas 5000 €)
    r"\b\d+\s*(?:à|et)\s*\d+\s*€",                  # 8 000 à 15 000 €
]

# 2. Citations sources officielles (urls + mentions textuelles distinctes)
OFFICIAL_DOMAINS = [
    r"service-public\.fr/\S+",
    r"legifrance\.gouv\.fr/\S+",
    r"impots\.gouv\.fr/\S+",
    r"ademe\.fr/\S+",
    r"anil\.org/\S+",
    r"insee\.fr/\S+",
    r"ecologie\.gouv\.fr/\S+",
    r"economie\.gouv\.fr/\S+",
    r"hatvp\.fr/\S+",
    r"diagnostiqueurs-immobiliers\.com",
    r"encadrementdesloyers\.gouv\.fr",
    r"cohesion-territoires\.gouv\.fr/\S+",
]
TEXTUAL_SOURCES = [
    r"\bservice-public\.fr\b",
    r"\bADEME\b",
    r"\bANIL\b",
    r"\bINSEE\b",
    r"\bLegifrance\b",
    r"\bDGCCRF\b",
    r"\bONIAM\b",
    # run-45 fix : Observatoire {Local,Locaux,Régional,des} des Loyers — singulier+pluriel
    r"\bobservatoires?\s+(?:locaux|local|r[ée]gional|r[ée]gionaux)?\s*(?:des\s+)?loyers\b",
    r"\bpréfectures?\b",   # run-45 fix : préfecture(s)
    r"\bDRIHL\b",          # run-45 add : Direction Régionale Habitat Logement IDF
    r"\bDREAL\b",          # run-45 add : Direction Régionale Environnement
    r"\bOLAP\b",           # run-45 add : Observatoire Loyers Agglo Parisienne
    r"\barrêté\s+préfectoral\b",  # run-45 add : forme légale courante
]

# 3. Quotations / textes de loi (nommage explicite)
LAW_PATTERNS = [
    r"\bLoi\s+(?:Climat\s+et\s+Résilience|ALUR|ELAN|Pinel|Cosse|Aurillac|n°\s*\d+[-\d]*)",
    r"\bloi\s+du\s+\d+\s+[a-zûéèêâîôç]+\s+\d{4}",
    r"\bDécret\s+n°\s*\d+[-\d]*",
    r"\barticle\s+[LRD]\.?\s*\d+[-\d]*(?:[.,]\d+)?",
    r"\barticle\s+\d+(?:-\d+)?\s+de\s+la\s+loi",
    r"«\s*[^»]{12,}»",                              # citation entre guillemets francais
    r"\"[^\"]{20,}\"",                              # citation entre guillemets droits
]


def strip_frontmatter(text: str) -> str:
    m = FRONTMATTER_RE.match(text)
    return text[m.end():] if m else text


def count_matches(text: str, patterns: list[str]) -> tuple[int, list[str]]:
    """Retourne (nb_matches_total, sample max 3 distincts)."""
    found: list[str] = []
    for pat in patterns:
        for m in re.finditer(pat, text, flags=re.IGNORECASE):
            found.append(m.group(0).strip())
    distinct = []
    seen = set()
    for x in found:
        k = x.lower()
        if k not in seen:
            seen.add(k)
            distinct.append(x)
    return len(distinct), distinct[:3]


def audit_article(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8")
    body = strip_frontmatter(raw)
    n_stat, s_stat = count_matches(body, STAT_PATTERNS)
    n_src, s_src = count_matches(body, OFFICIAL_DOMAINS + TEXTUAL_SOURCES)
    n_law, s_law = count_matches(body, LAW_PATTERNS)
    score = sum(1 for v in (n_stat, n_src, n_law) if v >= 3)
    return {
        "file": path.name,
        "stats": n_stat, "stats_sample": s_stat,
        "sources": n_src, "sources_sample": s_src,
        "laws": n_law, "laws_sample": s_law,
        "score_3of3": score,
    }


def render_markdown(results: list[dict]) -> str:
    lines = []
    lines.append("# Audit GEO content — résumé")
    lines.append("")
    lines.append("Cible (étude Princeton/GeorgiaTech/IIT/AI2) : ≥3 stats + ≥3 sources + ≥3 lois par article = score 3/3.")
    lines.append("")
    lines.append("| Article | stats | sources | lois | score |")
    lines.append("|---|---:|---:|---:|---:|")
    for r in results:
        flag = " ✅" if r["score_3of3"] == 3 else (" ⚠️" if r["score_3of3"] == 2 else " ❌")
        lines.append(
            f"| `{r['file']}` | {r['stats']} | {r['sources']} | {r['laws']} | "
            f"{r['score_3of3']}/3{flag} |"
        )
    lines.append("")
    lines.append("## Détail par article (3 samples max par dimension)")
    for r in results:
        lines.append("")
        lines.append(f"### {r['file']}  →  {r['score_3of3']}/3")
        lines.append(f"- stats ({r['stats']}) : {r['stats_sample']}")
        lines.append(f"- sources ({r['sources']}) : {r['sources_sample']}")
        lines.append(f"- lois ({r['laws']}) : {r['laws_sample']}")
    return "\n".join(lines) + "\n"


def main(argv: list[str]) -> int:
    if len(argv) > 1:
        paths = [Path(p) for p in argv[1:]]
    else:
        paths = sorted(p for p in CONTENT_DIR.glob("*.md") if p.name != "README.md")
    if not paths:
        print("Aucun article trouvé.", file=sys.stderr)
        return 2
    results = [audit_article(p) for p in paths]
    print(render_markdown(results))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
