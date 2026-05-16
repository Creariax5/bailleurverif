#!/usr/bin/env python3
"""
Builder du blog statique BailleurVérif.

Convertit content/*.md -> dashboard/blog/*.html avec :
- Frontmatter YAML extrait (title, slug, meta_description, longtails)
- Conversion markdown -> HTML (sous-set ciblé : headings, paragraphes,
  listes, gras/italique, code inline, liens, hr)
- Injection CTA wedge BailleurVérif (hero + mid + footer)
- Dark theme aligné avec dashboard live.html (Tailwind CDN)
- Génération index.html du blog

Usage : python3 dashboard/build_blog.py
"""

from __future__ import annotations

import html
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "content"
WEDGE_STATIC_DIR = ROOT / "wedge-tool" / "static"
OUT_DIR = WEDGE_STATIC_DIR / "blog"
DASHBOARD_DIR = ROOT / "dashboard"
LEGACY_BLOG_DIR = DASHBOARD_DIR / "blog"  # gardé pour compat dashboard live 8101
BASE_URL = "https://bailleurverif.fr"
WEDGE_URL = BASE_URL
BLOG_URL = f"{BASE_URL}/blog"
SITE_URL = BASE_URL

# Articles à publier (slug + accroche CTA personnalisée par sujet)
ARTICLES = {
    "dpe-f-location-2026": {
        "cta_angle": "dpe",
        "hero_kicker": "Votre logement classé F sera interdit à la location au 1ᵉʳ janvier 2028.",
        "mid_anchor_hint": "Comment décider",
        "footer_lead": "Vérifiez en 30 secondes si votre logement est conforme aux règles 2026",
    },
    "encadrement-loyer-zones-tendues-2026": {
        "cta_angle": "encadrement",
        "hero_kicker": "5 000 € d'amende possible si votre loyer dépasse le plafond légal.",
        "mid_anchor_hint": "Procédure pratique",
        "footer_lead": "Vérifiez en 30 secondes si votre loyer respecte le plafond officiel",
    },
    "verifier-dossier-locataire-fraude": {
        "cta_angle": "fraude",
        "hero_kicker": "10 à 20 % des dossiers locataires contiennent un faux document.",
        "mid_anchor_hint": "Le réflexe ultime",
        "footer_lead": "Pendant ce temps, vérifiez la conformité légale de votre bien (DPE + loyer)",
    },
    "obligations-bailleur-particulier-2026": {
        "cta_angle": "umbrella",
        "hero_kicker": "Cinq chantiers ouverts en 2026. Une seule vérification, 30 secondes.",
        "mid_anchor_hint": "Plan d'action",
        "footer_lead": "Vérifiez où votre bien se situe sur les 5 chantiers de 2026",
    },
    "dispositif-jeanbrun-2026": {
        "cta_angle": "jeanbrun",
        "hero_kicker": "LOI n° 2026-103 du 19 février 2026, art. 47 — amortissement jusqu'à 5,5 %/an.",
        "mid_anchor_hint": "Trois régimes",
        "footer_lead": "Avant de viser Jeanbrun, vérifiez les autres contraintes 2026 (DPE, encadrement, dossier)",
    },
    "guide-passoires-thermiques-rentabilite-bailleur-2026": {
        "cta_angle": "passoires-roi",
        "hero_kicker": "5,2 M de passoires thermiques en France · F interdit 1ᵉʳ janv. 2028 · 14 000 € net pour passer F→D.",
        "mid_anchor_hint": "stratégies",
        "footer_lead": "Avant tout : vérifiez les 5 chantiers réglementaires 2026 sur votre bien (30 secondes)",
    },
}


def render_cta(variant: str, lead: str, kicker: str | None = None) -> str:
    """Bloc CTA HTML inline injectable dans le flux d'article."""
    badge = {
        "hero": "Outil gratuit · 30 sec",
        "mid": "Pendant que vous lisez",
        "footer": "Et après ?",
    }.get(variant, "Outil gratuit")
    kicker_html = (
        f'<p class="text-sm text-amber-200/80 mb-2">{html.escape(kicker)}</p>'
        if kicker
        else ""
    )
    return f"""
<aside class="cta-wedge my-8 rounded-2xl border border-blue-200 bg-blue-50 p-6">
  <div class="text-[11px] uppercase tracking-widest text-blue-700 mb-2">{badge}</div>
  {kicker_html}
  <p class="text-lg md:text-xl font-semibold text-slate-900 mb-3">{html.escape(lead)}</p>
  <p class="text-sm text-slate-700 mb-4">5 questions, verdict immédiat : ✅ conforme · ⚠️ risque amende · 🚫 interdiction. Aucune création de compte.</p>
  <a href="{WEDGE_URL}" target="_blank" rel="noopener"
     class="inline-flex items-center gap-2 px-5 py-2.5 rounded-lg bg-blue-700 hover:bg-blue-800 text-slate-900 font-semibold text-sm transition">
    Vérifier mon bien sur BailleurVérif →
  </a>
  <span class="text-xs text-slate-500 ml-3">gratuit · sans inscription</span>
</aside>
""".strip()


# ---------- Frontmatter & markdown ----------

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.DOTALL)


def parse_frontmatter(raw: str) -> tuple[dict[str, str | list[str]], str]:
    m = FRONTMATTER_RE.match(raw)
    if not m:
        return {}, raw
    fm_block, body = m.group(1), m.group(2)
    meta: dict[str, str | list[str]] = {}
    current_list_key: str | None = None
    for line in fm_block.splitlines():
        if not line.strip():
            current_list_key = None
            continue
        if line.startswith("  - "):
            if current_list_key:
                val = line[4:].strip().strip('"')
                lst = meta.setdefault(current_list_key, [])
                if isinstance(lst, list):
                    lst.append(val)
            continue
        if ":" in line:
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip()
            if not val:
                current_list_key = key
                meta[key] = []
            else:
                current_list_key = None
                meta[key] = val.strip('"')
    return meta, body


def _inline(text: str) -> str:
    """Transforme inline markdown -> HTML. Préserve l'échappement."""
    # Échappement HTML d'abord
    text = html.escape(text, quote=False)
    # Code inline `...`
    text = re.sub(
        r"`([^`]+)`",
        lambda m: f'<code class="bg-white/80 px-1.5 py-0.5 rounded text-emerald-300 text-[0.92em]">{m.group(1)}</code>',
        text,
    )
    # Liens [text](url)
    text = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda m: f'<a href="{m.group(2)}" class="text-blue-700 hover:text-blue-800 underline decoration-blue-300" target="_blank" rel="noopener">{m.group(1)}</a>',
        text,
    )
    # Bold **
    text = re.sub(r"\*\*([^*]+)\*\*", r'<strong class="text-slate-900">\1</strong>', text)
    # Italic * (basique, après bold)
    text = re.sub(r"(?<![\*])\*([^*]+)\*(?![\*])", r"<em>\1</em>", text)
    return text


INTERNAL_MARKERS = (
    "Notes pour révision",
    "Notes pour publication",
    "Note interne",
)


def md_to_html(body: str, mid_cta_html: str, mid_anchor_hint: str) -> tuple[str, str]:
    """
    Convertit le markdown en HTML structurel. Retourne (intro_html, body_html).
    L'intro_html = paragraphes avant la première section `##` ou première ligne `---`.
    Injecte mid_cta_html avant la première section H2 dont le titre contient mid_anchor_hint.
    Coupe le body si un marqueur interne (Notes pour révision, etc.) apparait.
    """
    # Coupure préalable des sections internes éditoriales
    for marker in INTERNAL_MARKERS:
        idx = body.find(marker)
        if idx >= 0:
            # Remonter jusqu'au début du paragraphe contenant le marqueur
            cut = body.rfind("\n\n", 0, idx)
            if cut < 0:
                cut = body.rfind("\n", 0, idx)
            if cut < 0:
                cut = idx
            body = body[:cut].rstrip() + "\n"
            break

    lines = body.splitlines()
    out: list[str] = []
    intro_parts: list[str] = []
    intro_done = False
    para_buffer: list[str] = []
    list_buffer: list[str] = []
    list_type: str | None = None  # 'ul' | 'ol'
    mid_injected = False

    def flush_para():
        nonlocal para_buffer
        if not para_buffer:
            return
        text = " ".join(para_buffer).strip()
        para_buffer = []
        if not text:
            return
        target = out if intro_done else intro_parts
        target.append(f'<p class="text-slate-700 leading-relaxed my-4">{_inline(text)}</p>')

    def flush_list():
        nonlocal list_buffer, list_type
        if not list_buffer or list_type is None:
            list_buffer, list_type = [], None
            return
        tag = list_type
        items = "".join(f'<li class="my-1">{_inline(it)}</li>' for it in list_buffer)
        cls = "list-disc" if tag == "ul" else "list-decimal"
        target = out if intro_done else intro_parts
        target.append(
            f'<{tag} class="{cls} pl-6 text-slate-700 leading-relaxed my-3 space-y-1">{items}</{tag}>'
        )
        list_buffer, list_type = [], None

    def maybe_mid_inject(heading_text: str):
        nonlocal mid_injected
        if mid_injected:
            return
        if mid_anchor_hint and mid_anchor_hint.lower() in heading_text.lower():
            out.append(mid_cta_html)
            mid_injected = True

    # Skip the leading H1 (the title is already rendered in the article header)
    h1_skipped = False

    for raw in lines:
        line = raw.rstrip()

        # Headings
        if line.startswith("# ") and not h1_skipped:
            h1_skipped = True
            continue
        if line.startswith("## "):
            flush_para()
            flush_list()
            intro_done = True
            heading = line[3:].strip()
            maybe_mid_inject(heading)
            out.append(
                f'<h2 class="text-2xl font-bold text-slate-900 mt-10 mb-3 leading-tight">{_inline(heading)}</h2>'
            )
            continue
        if line.startswith("### "):
            flush_para()
            flush_list()
            heading = line[4:].strip()
            target = out if intro_done else intro_parts
            target.append(
                f'<h3 class="text-lg font-semibold text-blue-700 mt-6 mb-2">{_inline(heading)}</h3>'
            )
            continue

        # Horizontal rule
        if line.strip() in ("---", "***"):
            flush_para()
            flush_list()
            # Skip first --- if it would be at top (after frontmatter strip, none)
            target = out if intro_done else intro_parts
            target.append('<hr class="my-8 border-slate-200" />')
            continue

        # Lists
        ul_match = re.match(r"^[-*]\s+(.*)$", line)
        ol_match = re.match(r"^(\d+)\.\s+(.*)$", line)
        if ul_match:
            flush_para()
            if list_type and list_type != "ul":
                flush_list()
            list_type = "ul"
            list_buffer.append(ul_match.group(1))
            continue
        if ol_match:
            flush_para()
            if list_type and list_type != "ol":
                flush_list()
            list_type = "ol"
            list_buffer.append(ol_match.group(2))
            continue

        # Blank line = paragraph break
        if not line.strip():
            flush_para()
            flush_list()
            continue

        # Default : paragraph line (concat avec espace)
        flush_list()
        para_buffer.append(line.strip())

    flush_para()
    flush_list()

    # Remove the {{CTA}} placeholder if it ended up in output as raw text
    body_html = "\n".join(out)
    body_html = re.sub(r"<p[^>]*>\{\{CTA\}\}</p>\s*", "", body_html)

    intro_html = "\n".join(intro_parts)
    intro_html = re.sub(r"<p[^>]*>\{\{CTA\}\}</p>\s*", "", intro_html)
    return intro_html, body_html


# ---------- Page template ----------

PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<meta name="referrer" content="no-referrer-when-downgrade" />
<title>{title} — BailleurVérif</title>
<meta name="description" content="{meta_description}" />
<link rel="canonical" href="{canonical_url}" />
<link rel="alternate" type="application/atom+xml" title="BailleurVérif — Articles" href="/atom.xml" />
<link rel="alternate" type="application/feed+json" title="BailleurVérif — Articles" href="/feed.json" />
<meta property="og:title" content="{title}" />
<meta property="og:description" content="{meta_description}" />
<meta property="og:type" content="article" />
<meta property="og:url" content="{canonical_url}" />
<meta property="og:site_name" content="BailleurVérif" />
<meta property="og:locale" content="fr_FR" />
<meta name="twitter:card" content="summary" />
<meta name="twitter:title" content="{title}" />
<meta name="twitter:description" content="{meta_description}" />
<link rel="icon" type="image/svg+xml" href="/favicon.svg" />
<meta name="theme-color" content="#ffffff" />
<script type="application/ld+json">{jsonld}</script>
<link rel="stylesheet" href="/css/main.css" />
<script src="https://cdn.tailwindcss.com"></script>
<style>
  .article-body p strong, .article-body li strong {{ color: var(--text-primary); }}
  .article-body a {{ word-break: break-word; }}
</style>
</head>
<body>
<header class="bv-header">
  <div class="max-w-3xl mx-auto px-6 py-4 flex items-center justify-between flex-wrap gap-2">
    <a href="/" class="bv-logo">
      <span class="bv-logo-mark">✓</span>
      <span>BailleurVérif</span>
    </a>
    <nav class="flex items-center gap-4 text-sm">
      <a href="./" style="color:var(--text-secondary)">Tous les guides</a>
      <a href="{wedge_url}" target="_blank" rel="noopener" class="bv-btn-secondary" style="padding:0.4rem 0.9rem;font-size:0.8rem">Outil gratuit →</a>
    </nav>
  </div>
</header>

<main class="max-w-3xl mx-auto px-6 py-10 article-body">
  <div class="text-xs uppercase tracking-widest text-blue-700 mb-2">{kicker_top}</div>
  <h1 class="text-3xl md:text-4xl font-bold leading-tight mb-4"><span>{title}</span></h1>
  <div class="text-xs mb-4" style="color:var(--text-muted)"><span class="bv-update-pill">Publié le {pub_date}</span> · Lecture ~{minutes} min · BailleurVérif</div>

  <aside class="bv-trust-bar mb-8" aria-label="Sources officielles">
    <span><strong>Sources :</strong> <a href="https://www.legifrance.gouv.fr" target="_blank" rel="noopener">Légifrance</a> · <a href="https://www.service-public.fr" target="_blank" rel="noopener">Service-Public.fr</a> · <a href="https://www.ademe.fr" target="_blank" rel="noopener">ADEME</a></span>
    <span class="bv-lock">🔒 Aucun compte · Aucun cookie tiers · RGPD</span>
  </aside>

  {intro_html}

  {hero_cta}

  {body_html}

  {footer_cta}

  <div class="mt-12 pt-6 text-xs" style="border-top:1px solid var(--border); color:var(--text-secondary)">
    <div>BailleurVérif — outil gratuit de conformité pour bailleurs particuliers en France.</div>
    <div class="mt-1">Cet article a une vocation informative et ne constitue pas un conseil juridique.</div>
  </div>
</main>

<footer class="bv-footer mt-8 py-8">
  <div class="max-w-3xl mx-auto px-6">
    <div class="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-4">
      <div>
        <div><strong>BailleurVérif</strong> — Outil gratuit · Mis à jour le {pub_date}</div>
        <div class="text-xs mt-1" style="color:var(--text-muted)">Informatif — ne se substitue pas à un conseil juridique.</div>
      </div>
      <nav class="flex flex-wrap gap-x-4 gap-y-1 text-xs">
        <a href="/">Accueil</a>
        <a href="./">Tous les guides</a>
        <a href="/preavis-bail.html">Préavis</a>
        <a href="/mentions-legales.html">Mentions légales</a>
        <a href="/politique-confidentialite.html">Confidentialité</a>
        <a href="/cgu.html">CGU</a>
      </nav>
    </div>
    <div class="text-xs mt-4 pt-4" style="border-top:1px solid var(--border); color:var(--text-muted)">© {year} BailleurVérif</div>
  </div>
</footer>
</body>
</html>
"""

INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Blog BailleurVérif — conformité bailleur 2026</title>
<meta name="description" content="Guides pratiques pour propriétaires bailleurs particuliers : DPE, encadrement des loyers, anti-fraude dossier. Mis à jour en 2026." />
<link rel="canonical" href="{blog_url}/" />
<link rel="alternate" type="application/atom+xml" title="BailleurVérif — Articles" href="/atom.xml" />
<link rel="alternate" type="application/feed+json" title="BailleurVérif — Articles" href="/feed.json" />
<meta property="og:title" content="Blog BailleurVérif — conformité bailleur 2026" />
<meta property="og:description" content="Guides pratiques pour propriétaires bailleurs particuliers : DPE, encadrement des loyers, anti-fraude dossier. Mis à jour en 2026." />
<meta property="og:type" content="website" />
<meta property="og:url" content="{blog_url}/" />
<meta property="og:site_name" content="BailleurVérif" />
<meta property="og:locale" content="fr_FR" />
<meta name="twitter:card" content="summary" />
<meta name="twitter:title" content="Blog BailleurVérif — conformité bailleur 2026" />
<meta name="twitter:description" content="Guides pratiques pour bailleurs particuliers : DPE, encadrement, anti-fraude. À jour 2026." />
<link rel="icon" type="image/svg+xml" href="/favicon.svg" />
<meta name="theme-color" content="#ffffff" />
<script type="application/ld+json">{jsonld}</script>
<link rel="stylesheet" href="/css/main.css" />
<script src="https://cdn.tailwindcss.com"></script>
<style>
  .card:hover {{ background: var(--bg-secondary); border-color: var(--accent); }}
</style>
</head>
<body>
<header class="bv-header">
  <div class="max-w-3xl mx-auto px-6 py-4 flex items-center justify-between flex-wrap gap-2">
    <a href="/" class="bv-logo">
      <span class="bv-logo-mark">✓</span>
      <span>BailleurVérif</span>
    </a>
    <nav class="flex items-center gap-4 text-sm">
      <a href="{wedge_url}" style="color:var(--text-secondary)">Outil</a>
      <a href="{wedge_url}" target="_blank" rel="noopener" class="bv-btn-secondary" style="padding:0.4rem 0.9rem;font-size:0.8rem">Diagnostic gratuit →</a>
    </nav>
  </div>
</header>

<main class="max-w-3xl mx-auto px-6 py-10">
  <div class="text-xs uppercase tracking-widest text-blue-700 mb-2">Blog BailleurVérif</div>
  <h1 class="text-3xl md:text-4xl font-bold leading-tight mb-4"><span>Conformité bailleur particulier — 2026</span></h1>
  <p class="mb-4" style="color:var(--text-secondary);line-height:1.6">Guides pratiques, à jour des textes de 2026, pour propriétaires bailleurs particuliers en France. Pas de jargon, pas de paywall. Chaque article s'appuie sur des sources légales citées.</p>

  <aside class="bv-trust-bar mb-8" aria-label="Sources officielles">
    <span><strong>Sources :</strong> <a href="https://www.legifrance.gouv.fr" target="_blank" rel="noopener">Légifrance</a> · <a href="https://www.service-public.fr" target="_blank" rel="noopener">Service-Public.fr</a> · <a href="https://www.ademe.fr" target="_blank" rel="noopener">ADEME</a></span>
    <span class="bv-lock">🔒 Aucun compte · Aucun cookie tiers · RGPD</span>
  </aside>

  <div class="space-y-4 mb-10">
    {cards_html}
  </div>

  <div class="glass rounded-xl p-5 mb-8">
    <div class="text-xs uppercase tracking-widest text-blue-700 mb-2">L'outil</div>
    <p style="color:var(--text-secondary)" class="mb-3">Vérifiez en 30 secondes si votre logement est conforme à la loi 2026 (DPE, encadrement loyer, anti-fraude). Verdict immédiat, sans inscription.</p>
    <a href="{wedge_url}" target="_blank" rel="noopener" class="bv-btn">
      Vérifier mon bien →
    </a>
  </div>
</main>

<footer class="bv-footer py-8">
  <div class="max-w-3xl mx-auto px-6">
    <div class="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-4">
      <div>
        <div><strong>BailleurVérif</strong> — Outil gratuit · Blog 2026</div>
        <div class="text-xs mt-1" style="color:var(--text-muted)">Informatif — ne se substitue pas à un conseil juridique.</div>
      </div>
      <nav class="flex flex-wrap gap-x-4 gap-y-1 text-xs">
        <a href="/">Accueil</a>
        <a href="/preavis-bail.html">Préavis</a>
        <a href="/mentions-legales.html">Mentions légales</a>
        <a href="/politique-confidentialite.html">Confidentialité</a>
        <a href="/cgu.html">CGU</a>
      </nav>
    </div>
    <div class="text-xs mt-4 pt-4" style="border-top:1px solid var(--border); color:var(--text-muted)">© {year} BailleurVérif</div>
  </div>
</footer>
</body>
</html>
"""

CARD_TEMPLATE = """<a href="{slug}.html" class="card glass rounded-xl p-5 block transition">
  <div class="text-xs uppercase tracking-widest text-blue-700 mb-1">{kicker}</div>
  <div class="text-lg md:text-xl font-bold mb-1" style="color:var(--text-primary)">{title}</div>
  <div class="text-sm" style="color:var(--text-secondary)">{meta}</div>
</a>"""


# ---------- Build ----------

def estimate_minutes(text: str) -> int:
    words = len(re.findall(r"\w+", text))
    return max(1, round(words / 220))


def organization_node() -> dict:
    return {
        "@type": "Organization",
        "@id": f"{BASE_URL}/#organization",
        "name": "BailleurVérif",
        "url": BASE_URL,
        "logo": {
            "@type": "ImageObject",
            "url": f"{BASE_URL}/logo.png",
            "width": 400,
            "height": 400,
        },
        "description": "Vérification de conformité bailleur 2026 : DPE, encadrement loyer, anti-fraude dossier locataire.",
        "sameAs": ["https://piaille.fr/@bailleurverif"],
    }


def website_node() -> dict:
    return {
        "@type": "WebSite",
        "@id": f"{BASE_URL}/#website",
        "url": BASE_URL,
        "name": "BailleurVérif",
        "inLanguage": "fr-FR",
        "publisher": {"@id": f"{BASE_URL}/#organization"},
    }


def software_application_node() -> dict:
    return {
        "@type": "SoftwareApplication",
        "@id": f"{BASE_URL}/#softwareapplication",
        "name": "BailleurVérif",
        "url": BASE_URL,
        "description": (
            "Diagnostic gratuit de conformité bailleur 2026 : DPE (interdictions "
            "F 2028 / G 2025), encadrement loyer 31 communes, anti-fraude dossier. "
            "Verdict instantané sans inscription."
        ),
        "applicationCategory": "BusinessApplication",
        "applicationSubCategory": "PropertyManagement",
        "operatingSystem": "Web",
        "inLanguage": "fr-FR",
        "audience": {
            "@type": "Audience",
            "audienceType": "Propriétaires bailleurs particuliers",
        },
        "offers": {
            "@type": "Offer",
            "price": "0",
            "priceCurrency": "EUR",
            "availability": "https://schema.org/InStock",
            "description": "Diagnostic V0 gratuit, sans inscription",
        },
        "featureList": [
            "Vérification DPE (interdictions location 2025-2034)",
            "Plafond loyer encadré (31 communes zone tendue)",
            "Check anti-fraude dossier locataire",
            "Verdict 3 niveaux : conforme / risque amende / interdiction",
        ],
        "provider": {"@id": f"{BASE_URL}/#organization"},
    }


FAQ_QA_RE = re.compile(
    r"^\*\*\d+\.\s+(?P<q>[^*]+?\?)\*\*\s*\n(?P<a>(?:(?!^\*\*\d+\.)[^\n]*\n?)+)",
    re.MULTILINE,
)


def extract_faq(body: str) -> list[tuple[str, str]]:
    """Extract FAQ Q/A pairs from a markdown article body.

    Garde : ne parse que la section qui suit un heading contenant "FAQ"
    (insensible à la casse). Évite faux-positifs sur arbres de décision
    formattés en `**N. Question ?**` (cf article DPE-F).

    Pattern matché : `**N. Question ?**` suivi de paragraphe(s) jusqu'à la
    prochaine occurrence du même pattern ou heading.
    Retourne [(question, answer_plaintext), ...]. Answer plaintext = markdown
    inline simplifié (gras/italique conservés en texte, liens transformés en
    "label (url)").
    """
    faq_heading = re.search(r"^#{1,6}\s+[^\n]*FAQ\b", body, re.MULTILINE | re.IGNORECASE)
    if not faq_heading:
        return []
    faq_section = body[faq_heading.end():]
    # Stop at next H2 (--- or ## without FAQ in it).
    next_h2 = re.search(r"\n##\s", faq_section)
    if next_h2:
        faq_section = faq_section[: next_h2.start()]
    out: list[tuple[str, str]] = []
    for m in FAQ_QA_RE.finditer(faq_section):
        q = m.group("q").strip()
        a_raw = m.group("a").strip()
        # Stop at next heading marker (## or ###) if matched too greedy
        a_raw = re.split(r"\n(?:#{1,6}\s|---\s*$)", a_raw)[0].strip()
        # Strip markdown emphasis markers, normalize newlines, decode links
        a = re.sub(r"\*\*(.+?)\*\*", r"\1", a_raw)
        a = re.sub(r"\*(.+?)\*", r"\1", a)
        a = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1 (\2)", a)
        a = re.sub(r"\s+", " ", a).strip()
        if q and a:
            out.append((q, a))
    return out


def faq_node(canonical_url: str, qa: list[tuple[str, str]]) -> dict:
    return {
        "@type": "FAQPage",
        "@id": f"{canonical_url}#faq",
        "isPartOf": {"@id": f"{BASE_URL}/#website"},
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in qa
        ],
    }


def article_jsonld(
    title: str,
    description: str,
    canonical_url: str,
    iso_date: str,
    faq_qa: list[tuple[str, str]] | None = None,
) -> str:
    article = {
        "@type": "Article",
        "@id": f"{canonical_url}#article",
        "headline": title,
        "description": description,
        "datePublished": iso_date,
        "dateModified": iso_date,
        "inLanguage": "fr-FR",
        "author": {"@id": f"{BASE_URL}/#organization"},
        "publisher": {"@id": f"{BASE_URL}/#organization"},
        "mainEntityOfPage": {"@type": "WebPage", "@id": canonical_url},
        "isPartOf": {"@id": f"{BASE_URL}/#website"},
    }
    graph: list[dict] = [
        article,
        organization_node(),
        website_node(),
        software_application_node(),
    ]
    if faq_qa:
        graph.append(faq_node(canonical_url, faq_qa))
    data = {
        "@context": "https://schema.org",
        "@graph": graph,
    }
    return json.dumps(data, ensure_ascii=False)


def collection_jsonld(items: list[tuple[str, str, str]]) -> str:
    """items: list of (url, title, description)"""
    collection = {
        "@type": "CollectionPage",
        "@id": f"{BLOG_URL}/#collection",
        "name": "Blog BailleurVérif — conformité bailleur 2026",
        "url": f"{BLOG_URL}/",
        "inLanguage": "fr-FR",
        "isPartOf": {"@id": f"{BASE_URL}/#website"},
        "publisher": {"@id": f"{BASE_URL}/#organization"},
        "mainEntity": {
            "@type": "ItemList",
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": i + 1,
                    "url": url,
                    "name": title,
                }
                for i, (url, title, _desc) in enumerate(items)
            ],
        },
    }
    data = {
        "@context": "https://schema.org",
        "@graph": [
            collection,
            organization_node(),
            website_node(),
            software_application_node(),
        ],
    }
    return json.dumps(data, ensure_ascii=False)


AI_BOTS_ALLOW = [
    "GPTBot",
    "OAI-SearchBot",
    "ChatGPT-User",
    "ClaudeBot",
    "Claude-SearchBot",
    "PerplexityBot",
    "Perplexity-User",
    "Google-Extended",
    "Bytespider",
    "CCBot",
]


def write_atom_feed(items: list[tuple[str, str, str]], iso_datetime: str) -> None:
    """Atom 1.0 feed — consommé par Feedly/Inoreader/agrégateurs + crawlers LLM (Perplexity index Feedly)."""
    parts = [
        '<?xml version="1.0" encoding="utf-8"?>',
        '<feed xmlns="http://www.w3.org/2005/Atom" xml:lang="fr">',
        f'  <title>BailleurVérif — Conformité bailleur 2026</title>',
        f'  <subtitle>Guides pratiques pour propriétaires bailleurs particuliers : DPE, encadrement, anti-fraude, Alur.</subtitle>',
        f'  <link href="{BLOG_URL}/" />',
        f'  <link rel="self" type="application/atom+xml" href="{SITE_URL}/atom.xml" />',
        f'  <link rel="hub" href="https://pubsubhubbub.appspot.com/" />',
        f'  <link rel="hub" href="https://pubsubhubbub.superfeedr.com/" />',
        f'  <id>{SITE_URL}/</id>',
        f'  <updated>{iso_datetime}</updated>',
        f'  <author><name>BailleurVérif</name></author>',
        f'  <rights>© BailleurVérif</rights>',
    ]
    for url, title, summary in items:
        parts.extend([
            '  <entry>',
            f'    <title>{html.escape(title)}</title>',
            f'    <link href="{html.escape(url)}" />',
            f'    <id>{html.escape(url)}</id>',
            f'    <updated>{iso_datetime}</updated>',
            f'    <published>{iso_datetime}</published>',
            f'    <summary>{html.escape(summary)}</summary>',
            '  </entry>',
        ])
    parts.append('</feed>')
    content = "\n".join(parts) + "\n"
    (WEDGE_STATIC_DIR / "atom.xml").write_text(content, encoding="utf-8")


def write_json_feed(items: list[tuple[str, str, str]], iso_datetime: str) -> None:
    """JSON Feed 1.1 — format moderne, consommé par NetNewsWire/Inoreader/agrégateurs récents."""
    feed = {
        "version": "https://jsonfeed.org/version/1.1",
        "title": "BailleurVérif — Conformité bailleur 2026",
        "description": "Guides pratiques pour propriétaires bailleurs particuliers : DPE, encadrement, anti-fraude, Alur.",
        "home_page_url": f"{BLOG_URL}/",
        "feed_url": f"{SITE_URL}/feed.json",
        "language": "fr",
        "authors": [{"name": "BailleurVérif"}],
        "items": [
            {
                "id": url,
                "url": url,
                "title": title,
                "summary": summary,
                "date_published": iso_datetime,
                "date_modified": iso_datetime,
            }
            for url, title, summary in items
        ],
    }
    (WEDGE_STATIC_DIR / "feed.json").write_text(
        json.dumps(feed, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def write_sitemap_and_robots(article_urls: list[str], iso_date: str) -> None:
    # Idempotence : merge des pages programmatiques scannées depuis /static/
    # pour ne plus écraser les 50 DPE + 31 encadrement + tools dédiés à
    # chaque rebuild blog (bug latent fixé run-99, miroir patch run-98).
    static_files = []
    if WEDGE_STATIC_DIR.exists():
        static_files = [p.name for p in WEDGE_STATIC_DIR.iterdir() if p.is_file()]
    enc_slugs = sorted({
        f[:-5] for f in static_files
        if f.startswith("encadrement-loyer-") and f.endswith(".html")
    })
    dpe_slugs = sorted({
        f[:-5] for f in static_files
        if f.endswith("-dpe-f-g-interdit-location.html")
    })
    tool_pages = [f for f in ("preavis-bail.html", "widget-bailleurverif.html") if f in static_files]
    legal_pages = [
        f for f in ("mentions-legales.html", "politique-confidentialite.html", "cgu.html")
        if f in static_files
    ]

    urls = [f"{SITE_URL}/"] + [f"{SITE_URL}/{p}" for p in tool_pages] + [f"{BLOG_URL}/"] + article_urls
    urls += [f"{SITE_URL}/{s}.html" for s in enc_slugs]
    urls += [f"{SITE_URL}/{s}.html" for s in dpe_slugs]
    urls += [f"{SITE_URL}/{p}" for p in legal_pages]
    # Dedup en préservant ordre
    seen: set[str] = set()
    deduped: list[str] = []
    for u in urls:
        if u not in seen:
            seen.add(u)
            deduped.append(u)
    urls = deduped

    parts = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        parts.append(f"  <url><loc>{html.escape(u)}</loc><lastmod>{iso_date}</lastmod></url>")
    parts.append("</urlset>")
    sitemap_content = "\n".join(parts) + "\n"

    robots_lines = ["User-agent: *", "Allow: /", ""]
    for bot in AI_BOTS_ALLOW:
        robots_lines.append(f"User-agent: {bot}")
        robots_lines.append("Allow: /")
        robots_lines.append("")
    robots_lines.append(f"Sitemap: {SITE_URL}/sitemap.xml")
    robots_content = "\n".join(robots_lines) + "\n"

    # Cible canonique : sert via https://bailleurverif.fr (port 8102).
    WEDGE_STATIC_DIR.mkdir(parents=True, exist_ok=True)
    (WEDGE_STATIC_DIR / "sitemap.xml").write_text(sitemap_content, encoding="utf-8")
    (WEDGE_STATIC_DIR / "robots.txt").write_text(robots_content, encoding="utf-8")

    # Compat : dashboard 8101 reste accessible interne, on garde un miroir.
    (DASHBOARD_DIR / "sitemap.xml").write_text(sitemap_content, encoding="utf-8")
    (DASHBOARD_DIR / "robots.txt").write_text(robots_content, encoding="utf-8")


def build():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    cards: list[tuple[str, str, str, str]] = []  # (slug, title, meta, kicker)
    pub_date = datetime.now(timezone.utc).strftime("%d %B %Y")
    iso_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    year = datetime.now(timezone.utc).year
    article_urls: list[str] = []
    index_items: list[tuple[str, str, str]] = []

    for slug, cta_cfg in ARTICLES.items():
        md_path = CONTENT_DIR / f"{slug}.md"
        if not md_path.exists():
            print(f"SKIP {slug} (no source markdown)")
            continue
        raw = md_path.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(raw)
        title = str(meta.get("title", slug))
        meta_desc = str(meta.get("meta_description", ""))

        mid_cta_html = render_cta(
            "mid",
            cta_cfg["footer_lead"],
            kicker=None,
        )
        intro_html, body_html = md_to_html(
            body, mid_cta_html, cta_cfg["mid_anchor_hint"]
        )

        hero_cta = render_cta(
            "hero",
            cta_cfg["footer_lead"],
            kicker=cta_cfg["hero_kicker"],
        )
        footer_cta = render_cta(
            "footer",
            cta_cfg["footer_lead"],
            kicker="Vous venez de lire un guide. Le reste, on l'a outillé.",
        )

        minutes = estimate_minutes(body)
        canonical_url = f"{BLOG_URL}/{slug}.html"
        faq_qa = extract_faq(body)
        jsonld = article_jsonld(title, meta_desc, canonical_url, iso_date, faq_qa)
        page = PAGE_TEMPLATE.format(
            title=html.escape(title),
            meta_description=html.escape(meta_desc),
            wedge_url=WEDGE_URL,
            canonical_url=canonical_url,
            kicker_top="Guide conformité 2026",
            pub_date=pub_date,
            minutes=minutes,
            intro_html=intro_html,
            hero_cta=hero_cta,
            body_html=body_html,
            footer_cta=footer_cta,
            year=year,
            jsonld=jsonld,
        )
        out_path = OUT_DIR / f"{slug}.html"
        out_path.write_text(page, encoding="utf-8")
        print(f"OK   {out_path.relative_to(ROOT)} ({minutes} min)")

        cards.append((slug, title, meta_desc, "Guide conformité 2026"))
        article_urls.append(canonical_url)
        index_items.append((canonical_url, title, meta_desc))

    cards_html = "\n".join(
        CARD_TEMPLATE.format(
            slug=html.escape(s),
            title=html.escape(t),
            meta=html.escape(m),
            kicker=html.escape(k),
        )
        for s, t, m, k in cards
    )
    index_jsonld = collection_jsonld(index_items)
    index_html = INDEX_TEMPLATE.format(
        wedge_url=WEDGE_URL,
        blog_url=BLOG_URL,
        cards_html=cards_html,
        year=year,
        jsonld=index_jsonld,
    )
    (OUT_DIR / "index.html").write_text(index_html, encoding="utf-8")
    print(f"OK   {(OUT_DIR / 'index.html').relative_to(ROOT)} (index)")

    # Miroir legacy dashboard/blog/ (rétro-compat dashboard 8101).
    LEGACY_BLOG_DIR.mkdir(parents=True, exist_ok=True)
    for src in OUT_DIR.iterdir():
        if src.is_file():
            (LEGACY_BLOG_DIR / src.name).write_bytes(src.read_bytes())
    print(f"OK   mirror -> {LEGACY_BLOG_DIR.relative_to(ROOT)}")

    write_sitemap_and_robots(article_urls, iso_date)
    # Re-count after merge (programmatic pages merged inside write_sitemap_and_robots)
    sitemap_total = (WEDGE_STATIC_DIR / "sitemap.xml").read_text(encoding="utf-8").count("<loc>")
    print(f"OK   {(WEDGE_STATIC_DIR / 'sitemap.xml').relative_to(ROOT)} ({sitemap_total} urls, blog {len(article_urls)} + merge prog)")
    print(f"OK   {(WEDGE_STATIC_DIR / 'robots.txt').relative_to(ROOT)}")

    iso_datetime = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    write_atom_feed(index_items, iso_datetime)
    write_json_feed(index_items, iso_datetime)
    print(f"OK   {(WEDGE_STATIC_DIR / 'atom.xml').relative_to(ROOT)} ({len(index_items)} entries)")
    print(f"OK   {(WEDGE_STATIC_DIR / 'feed.json').relative_to(ROOT)} ({len(index_items)} items)")


if __name__ == "__main__":
    build()
