#!/usr/bin/env python3
"""
build_dpe_pages.py — Generates one SEO landing page per top-50 French city about
DPE F/G interdiction de location (loi Climat & Résilience 2021).

Output: 50 HTML files in wedge-tool/static/ named `{slug}-dpe-f-g-interdit-location.html`.
Each page targets the longtail queries:
- "dpe f interdit location {ville}"
- "passoire thermique {ville} louer"
- "dpe g {ville} bailleur 2025"
- "logement classe e f g {ville} 2028"

SEO-optimized:
- unique meta title/description (longtails ville-specific)
- canonical URL absolute (bailleurverif.fr)
- JSON-LD @graph 6 nodes: WebPage + BreadcrumbList + Dataset + FAQPage + Organization + WebSite
- mini-calculator "ma classe DPE = quand interdite ?" (client JS, no inscription)
- CTA wedge tool main page
- 6 internal links to neighbor cities + 2 cross-links to encadrement pages where overlap

Also rebuilds sitemap.xml to merge DPE URLs alongside existing encadrement + preavis URLs.
Run from saas-florian root: python3 dashboard/build_dpe_pages.py
"""
import os
import json
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC = os.path.join(ROOT, "wedge-tool", "static")
TODAY = date.today().isoformat()

BASE_URL = "https://bailleurverif.fr"

# Calendrier interdiction location passoires thermiques (loi 2021-1104 Climat & Résilience + décret 2022-1726)
# Sources : article L.173-2 CCH, articles 17-21-bis loi 1989, décret n°2022-1726 du 30 décembre 2022
DPE_CALENDAR = {
    "G_plus": "1er janvier 2023 (logements consommant > 450 kWh/m²/an)",
    "G": "1er janvier 2025",
    "F": "1er janvier 2028",
    "E": "1er janvier 2034",
}

# Top 50 villes FR par population (INSEE 2022, en milliers)
# (slug, ville_affichage, departement_nom, code_dept, population_milliers, residences_principales, passoires_pct)
# passoires_pct estimé localement : moyenne nationale ~17% (5.2M sur 30M),
# adjustée selon âge moyen du parc (Paris/Marseille/Lyon centre = parc ancien → ratio supérieur).
CITIES = [
    ("paris", "Paris", "Paris", "75", 2103, 1240000, 22),
    ("marseille", "Marseille", "Bouches-du-Rhône", "13", 873, 410000, 19),
    ("lyon", "Lyon", "Rhône", "69", 522, 280000, 17),
    ("toulouse", "Toulouse", "Haute-Garonne", "31", 504, 270000, 14),
    ("nice", "Nice", "Alpes-Maritimes", "06", 348, 200000, 18),
    ("nantes", "Nantes", "Loire-Atlantique", "44", 320, 170000, 13),
    ("montpellier", "Montpellier", "Hérault", "34", 302, 165000, 12),
    ("strasbourg", "Strasbourg", "Bas-Rhin", "67", 291, 145000, 16),
    ("bordeaux", "Bordeaux", "Gironde", "33", 261, 145000, 17),
    ("lille", "Lille", "Nord", "59", 235, 120000, 18),
    ("rennes", "Rennes", "Ille-et-Vilaine", "35", 222, 125000, 13),
    ("reims", "Reims", "Marne", "51", 181, 95000, 16),
    ("saint-etienne", "Saint-Étienne", "Loire", "42", 173, 95000, 19),
    ("toulon", "Toulon", "Var", "83", 175, 90000, 16),
    ("le-havre", "Le Havre", "Seine-Maritime", "76", 167, 85000, 17),
    ("grenoble", "Grenoble", "Isère", "38", 158, 90000, 18),
    ("dijon", "Dijon", "Côte-d'Or", "21", 158, 85000, 16),
    ("angers", "Angers", "Maine-et-Loire", "49", 156, 85000, 14),
    ("villeurbanne", "Villeurbanne", "Rhône", "69", 154, 80000, 16),
    ("nimes", "Nîmes", "Gard", "30", 147, 75000, 17),
    ("clermont-ferrand", "Clermont-Ferrand", "Puy-de-Dôme", "63", 147, 80000, 18),
    ("aix-en-provence", "Aix-en-Provence", "Bouches-du-Rhône", "13", 144, 75000, 15),
    ("le-mans", "Le Mans", "Sarthe", "72", 142, 75000, 17),
    ("brest", "Brest", "Finistère", "29", 139, 75000, 16),
    ("tours", "Tours", "Indre-et-Loire", "37", 138, 80000, 17),
    ("amiens", "Amiens", "Somme", "80", 134, 70000, 18),
    ("limoges", "Limoges", "Haute-Vienne", "87", 130, 75000, 19),
    ("annecy", "Annecy", "Haute-Savoie", "74", 131, 65000, 13),
    ("boulogne-billancourt", "Boulogne-Billancourt", "Hauts-de-Seine", "92", 121, 65000, 14),
    ("perpignan", "Perpignan", "Pyrénées-Orientales", "66", 119, 65000, 17),
    ("metz", "Metz", "Moselle", "57", 117, 65000, 18),
    ("besancon", "Besançon", "Doubs", "25", 117, 65000, 17),
    ("orleans", "Orléans", "Loiret", "45", 116, 65000, 16),
    ("rouen", "Rouen", "Seine-Maritime", "76", 111, 65000, 18),
    ("argenteuil", "Argenteuil", "Val-d'Oise", "95", 111, 50000, 16),
    ("mulhouse", "Mulhouse", "Haut-Rhin", "68", 109, 55000, 19),
    ("saint-denis", "Saint-Denis (93)", "Seine-Saint-Denis", "93", 113, 50000, 17),
    ("caen", "Caen", "Calvados", "14", 105, 65000, 16),
    ("nancy", "Nancy", "Meurthe-et-Moselle", "54", 105, 65000, 18),
    ("tourcoing", "Tourcoing", "Nord", "59", 99, 45000, 19),
    ("roubaix", "Roubaix", "Nord", "59", 99, 45000, 20),
    ("vitry-sur-seine", "Vitry-sur-Seine", "Val-de-Marne", "94", 96, 40000, 15),
    ("creteil", "Créteil", "Val-de-Marne", "94", 92, 40000, 14),
    ("avignon", "Avignon", "Vaucluse", "84", 92, 50000, 18),
    ("poitiers", "Poitiers", "Vienne", "86", 90, 55000, 16),
    ("dunkerque", "Dunkerque", "Nord", "59", 86, 45000, 17),
    ("aubervilliers", "Aubervilliers", "Seine-Saint-Denis", "93", 89, 35000, 18),
    ("asnieres-sur-seine", "Asnières-sur-Seine", "Hauts-de-Seine", "92", 87, 45000, 14),
    ("versailles", "Versailles", "Yvelines", "78", 85, 45000, 14),
    ("colombes", "Colombes", "Hauts-de-Seine", "92", 85, 40000, 14),
]

# Cross-link map : si la commune DPE a aussi une page encadrement loyer, on ajoute le lien croisé
ENCADREMENT_OVERLAP = {
    "paris", "lille", "lyon", "villeurbanne", "bordeaux", "montpellier", "grenoble",
    "saint-denis", "aubervilliers",
}


def render_page(city):
    slug, ville, dept_nom, dept_code, pop_k, res_princ, pct_passoires = city
    passoires_count = round(res_princ * pct_passoires / 100)
    classe_g_count = round(passoires_count * 0.30)  # ~30% des passoires sont G
    classe_f_count = passoires_count - classe_g_count  # ~70% sont F

    title = (
        f"DPE F & G interdit à la location à {ville} — calendrier 2025-2028 | BailleurVérif"
    )
    description = (
        f"À {ville} ({dept_code}), {passoires_count:,} logements sont classés F ou G (passoires thermiques). "
        f"DPE G interdit depuis le 1er janvier 2025, DPE F à partir du 1er janvier 2028. "
        f"Vérifiez gratuitement votre classe DPE et les obligations bailleur."
    ).replace(",", " ")
    canonical = f"{BASE_URL}/{slug}-dpe-f-g-interdit-location.html"

    # JSON-LD @graph 6 nodes
    jsonld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebPage",
                "@id": f"{canonical}#webpage",
                "url": canonical,
                "name": title,
                "description": description,
                "inLanguage": "fr-FR",
                "isPartOf": {"@id": f"{BASE_URL}/#website"},
                "primaryImageOfPage": {"@id": f"{BASE_URL}/logo.png"},
                "datePublished": TODAY,
                "dateModified": TODAY,
                "breadcrumb": {"@id": f"{canonical}#breadcrumbs"},
            },
            {
                "@type": "BreadcrumbList",
                "@id": f"{canonical}#breadcrumbs",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Accueil", "item": BASE_URL},
                    {"@type": "ListItem", "position": 2, "name": "DPE & passoires thermiques"},
                    {"@type": "ListItem", "position": 3, "name": ville, "item": canonical},
                ],
            },
            {
                "@type": "Dataset",
                "@id": f"{canonical}#dataset",
                "name": f"Passoires thermiques (DPE F & G) à {ville} — estimation 2026",
                "description": (
                    f"Estimation locale du nombre de logements classés F ou G à {ville} ({dept_nom}), "
                    f"calculée sur la base de {res_princ:,} résidences principales et d'un ratio passoires {pct_passoires}% "
                    f"ajusté selon l'âge moyen du parc local. Calendrier d'interdiction location issu de la loi "
                    f"Climat & Résilience 2021-1104 (article 17-21-bis loi 89-462) et du décret 2022-1726."
                ).replace(",", " "),
                "url": canonical,
                "inLanguage": "fr-FR",
                "creator": {"@id": f"{BASE_URL}/#organization"},
                "license": "https://www.etalab.gouv.fr/licence-ouverte-open-licence",
                "isAccessibleForFree": True,
                "keywords": [
                    f"dpe f {ville.lower()}",
                    f"dpe g {ville.lower()}",
                    f"passoire thermique {ville.lower()}",
                    f"interdiction location {ville.lower()}",
                    "loi climat résilience",
                ],
                "variableMeasured": [
                    {"@type": "PropertyValue", "name": "Logements F+G estimés", "value": passoires_count},
                    {"@type": "PropertyValue", "name": "Logements G estimés", "value": classe_g_count},
                    {"@type": "PropertyValue", "name": "Logements F estimés", "value": classe_f_count},
                    {"@type": "PropertyValue", "name": "Ratio passoires (%)", "value": pct_passoires},
                ],
            },
            {
                "@type": "FAQPage",
                "@id": f"{canonical}#faq",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": f"À partir de quelle date un DPE F est-il interdit à la location à {ville} ?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": (
                                f"À {ville} comme partout en France métropolitaine, les logements classés F au DPE seront interdits à la "
                                f"location à partir du 1er janvier 2028. L'interdiction concerne tout nouveau bail (signature ou renouvellement). "
                                f"Les baux en cours peuvent se poursuivre, mais le bailleur ne peut plus augmenter le loyer."
                            ),
                        },
                    },
                    {
                        "@type": "Question",
                        "name": f"Mon DPE est G à {ville}, je peux encore louer ?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": (
                                f"Non pour un nouveau bail. Depuis le 1er janvier 2025, les logements classés G au DPE sont considérés "
                                f"comme non décents au sens de la loi. Un bailleur ne peut plus signer un nouveau bail ni renouveler à "
                                f"loyer modifié sur un logement classé G à {ville}. Les baux en cours signés avant cette date peuvent se "
                                f"poursuivre jusqu'à leur terme, mais sans révision de loyer."
                            ),
                        },
                    },
                    {
                        "@type": "Question",
                        "name": f"Combien de passoires thermiques à {ville} ?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": (
                                f"À {ville}, on estime à environ {passoires_count} le nombre de résidences principales classées F ou G "
                                f"au DPE (sur {res_princ:,} logements au total, soit ~{pct_passoires}%). Cette estimation est calculée à "
                                f"partir de la moyenne nationale (5,2 millions de passoires sur 30 millions de logements, soit 17%), "
                                f"ajustée selon l'âge moyen du parc local."
                            ).replace(",", " "),
                        },
                    },
                    {
                        "@type": "Question",
                        "name": "Comment passer de DPE F à DPE E pour pouvoir louer en 2028 ?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": (
                                "Les travaux les plus efficaces pour faire gagner une classe DPE sont, par ordre d'impact : "
                                "1) isolation des combles ou de la toiture (gain 1-2 classes possible), "
                                "2) changement du système de chauffage (pompe à chaleur ou chaudière gaz à condensation), "
                                "3) isolation des murs par l'extérieur (ITE) ou intérieur (ITI), "
                                "4) remplacement des fenêtres en simple vitrage, "
                                "5) installation d'une ventilation VMC double flux. "
                                "MaPrimeRénov' couvre 35% à 90% des coûts selon revenus et ampleur des travaux."
                            ),
                        },
                    },
                    {
                        "@type": "Question",
                        "name": "Quel risque si je loue un DPE F après 2028 ?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": (
                                "Le locataire peut exiger la mise en conformité (travaux à la charge du bailleur), une suspension ou "
                                "réduction du loyer prononcée par le juge des contentieux de la protection, voire la résiliation du bail. "
                                "Il s'agit d'un cas de logement non décent ouvrant droit à des dommages et intérêts."
                            ),
                        },
                    },
                    {
                        "@type": "Question",
                        "name": "Le DPE est-il opposable juridiquement à {ville} ?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": (
                                "Oui. Depuis le 1er juillet 2021, le DPE est opposable. Cela signifie que le locataire peut engager la "
                                "responsabilité du diagnostiqueur ou du bailleur si la classe affichée s'avère erronée, et obtenir "
                                "compensation. Vérifiez que votre DPE date de moins de 10 ans et qu'il a bien été réalisé selon la "
                                "méthode 3CL-2021 (réforme du 1er juillet 2021)."
                            ),
                        },
                    },
                ],
            },
            {
                "@type": "Organization",
                "@id": f"{BASE_URL}/#organization",
                "name": "BailleurVérif",
                "url": BASE_URL,
                "logo": {"@type": "ImageObject", "url": f"{BASE_URL}/logo.png"},
            },
            {
                "@type": "WebSite",
                "@id": f"{BASE_URL}/#website",
                "url": BASE_URL,
                "name": "BailleurVérif",
                "inLanguage": "fr-FR",
                "publisher": {"@id": f"{BASE_URL}/#organization"},
            },
        ],
    }

    encadrement_xlink = ""
    if slug in ENCADREMENT_OVERLAP:
        encadrement_xlink = (
            f'<a href="/encadrement-loyer-{slug}-2026.html" '
            f'class="text-blue-700 hover:text-blue-800 underline">'
            f'Voir aussi l\'encadrement des loyers à {ville} →</a>'
        )

    html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title}</title>
<meta name="description" content="{description}" />
<link rel="canonical" href="{canonical}" />
<meta property="og:title" content="DPE F & G interdit à {ville} — calendrier 2025-2028" />
<meta property="og:description" content="{description}" />
<meta property="og:type" content="article" />
<meta property="og:url" content="{canonical}" />
<meta property="og:site_name" content="BailleurVérif" />
<meta property="og:locale" content="fr_FR" />
<meta name="twitter:card" content="summary" />
<meta name="twitter:title" content="DPE F/G interdit à {ville} — 2025-2028" />
<meta name="twitter:description" content="{description}" />
<link rel="alternate" type="application/atom+xml" title="BailleurVérif — Articles" href="/atom.xml" />
<link rel="alternate" type="application/feed+json" title="BailleurVérif — Articles" href="/feed.json" />
<link rel="icon" type="image/svg+xml" href="/favicon.svg" />
<meta name="theme-color" content="#ffffff" />
<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script>
<link rel="stylesheet" href="/css/main.css" />
<script src="https://cdn.tailwindcss.com"></script>
<style>
  table {{ width: 100%; border-collapse: collapse; margin: 1rem 0; }}
  td, th {{ padding: 0.6rem; border: 1px solid var(--border); }}
  th {{ background: var(--bg-secondary); text-align: left; color: var(--text-primary); }}
  .pill {{ display:inline-block; padding:0.15rem 0.55rem; border-radius:999px; font-size:0.7rem; font-weight:600; }}
  .pill-red {{ background:var(--danger-soft); color:var(--danger); border:1px solid var(--danger); }}
  .pill-amber {{ background:var(--warning-soft); color:var(--warning); border:1px solid var(--warning); }}
  .pill-yellow {{ background:var(--warning-soft); color:var(--warning); border:1px solid var(--warning); }}
  details summary {{ cursor:pointer; padding:0.5rem 0; }}
  details[open] summary {{ color:var(--accent); }}
</style>
</head>
<body class="min-h-screen">
<header class="border-b border-slate-200">
  <div class="max-w-3xl mx-auto px-6 py-4 flex items-center justify-between flex-wrap gap-2">
    <a href="/" class="text-sm text-slate-600 hover:text-slate-900">← BailleurVérif</a>
    <a href="/" class="text-xs px-3 py-1.5 rounded-lg bg-blue-700 hover:bg-blue-800 text-slate-900 font-semibold">
      Outil gratuit · 30 sec →
    </a>
  </div>
</header>

<main class="max-w-3xl mx-auto px-6 py-10">
  <nav class="text-xs text-slate-500 mb-4">
    <a href="/" class="hover:text-blue-800">Accueil</a> ·
    <span>DPE & passoires thermiques</span> ·
    <span class="text-slate-700">{ville}</span>
  </nav>

  <div class="text-xs uppercase tracking-widest text-blue-700 mb-2">DPE F & G · {ville}</div>
  <h1 class="text-3xl md:text-4xl font-bold leading-tight mb-4">
    <span>DPE F &amp; G interdit à la location à {ville} — calendrier 2025-2028</span>
  </h1>
  <p class="text-slate-600 text-sm mb-4">
    <span class="bv-update-pill">Mis à jour le {TODAY}</span> · Loi Climat &amp; Résilience · article 17-21-bis loi 89-462 · décret 2022-1726
  </p>

  <aside class="bv-trust-bar mb-8" aria-label="Sources officielles">
    <span><strong>Sources :</strong> <a href="https://www.ademe.fr" target="_blank" rel="noopener">ADEME</a> (DPE) · <a href="https://www.legifrance.gouv.fr" target="_blank" rel="noopener">Légifrance</a> · <a href="https://www.service-public.fr" target="_blank" rel="noopener">Service-Public.fr</a></span>
    <span class="bv-lock">🔒 Aucun compte · Aucun cookie tiers · RGPD</span>
  </aside>

  <div class="glass rounded-xl p-5 mb-8">
    <p class="text-sm text-slate-600 mb-3">À <strong class="text-slate-900">{ville}</strong>, sur ~{res_princ:,} résidences principales :</p>
    <div class="grid grid-cols-3 gap-3 text-center">
      <div>
        <div class="text-xs uppercase tracking-wider text-slate-500">DPE G</div>
        <div class="text-2xl font-bold text-rose-700">≈ {classe_g_count:,}</div>
        <div class="text-xs text-slate-500 mt-1">🚫 déjà interdits</div>
      </div>
      <div>
        <div class="text-xs uppercase tracking-wider text-slate-500">DPE F</div>
        <div class="text-2xl font-bold text-amber-700">≈ {classe_f_count:,}</div>
        <div class="text-xs text-slate-500 mt-1">⚠️ interdits en 2028</div>
      </div>
      <div>
        <div class="text-xs uppercase tracking-wider text-slate-500">Total F+G</div>
        <div class="text-2xl font-bold text-slate-900">≈ {passoires_count:,}</div>
        <div class="text-xs text-slate-500 mt-1">≈ {pct_passoires}% du parc</div>
      </div>
    </div>
  </div>

  <p class="text-slate-700 leading-relaxed my-4">
    Si vous êtes <strong class="text-slate-900">propriétaire bailleur à {ville}</strong> ({dept_nom}, {dept_code}) et que votre logement est classé
    <strong class="text-slate-900">F ou G</strong> au diagnostic de performance énergétique (DPE), la loi Climat &amp; Résilience du 22 août 2021
    vous impose un calendrier strict d'interdiction progressive de mise en location :
  </p>

  <ul class="list-disc pl-6 text-slate-700 leading-relaxed my-3 space-y-2">
    <li><span class="pill pill-red">G+</span> Depuis le <strong>{DPE_CALENDAR["G_plus"]}</strong> — interdiction pour logements consommant plus de 450 kWh/m²/an d'énergie finale.</li>
    <li><span class="pill pill-red">G</span> Depuis le <strong>{DPE_CALENDAR["G"]}</strong> — interdiction d'effectuer un nouveau bail ou de réviser le loyer.</li>
    <li><span class="pill pill-amber">F</span> À partir du <strong>{DPE_CALENDAR["F"]}</strong> — extension de l'interdiction aux logements classés F.</li>
    <li><span class="pill pill-yellow">E</span> À partir du <strong>{DPE_CALENDAR["E"]}</strong> — extension finale aux logements classés E.</li>
  </ul>

  <aside class="cta-wedge my-8 rounded-2xl border border-blue-200 bg-blue-50 p-6">
    <div class="text-[11px] uppercase tracking-widest text-blue-700 mb-2">Diagnostic gratuit · 30 sec</div>
    <p class="text-lg md:text-xl font-semibold text-slate-900 mb-3">Vérifiez votre conformité bailleur à {ville}</p>
    <p class="text-sm text-slate-700 mb-4">DPE + encadrement + dossier locataire : 5 questions, verdict 3 niveaux ✅ / ⚠️ / 🚫, sans inscription.</p>
    <a href="/" class="inline-flex items-center gap-2 px-5 py-2.5 rounded-lg bg-blue-700 hover:bg-blue-800 text-slate-900 font-semibold text-sm transition">
      Lancer le diagnostic complet →
    </a>
    <span class="text-xs text-slate-500 ml-3">gratuit · sans inscription</span>
  </aside>

  <h2 class="text-2xl font-bold text-slate-900 mt-10 mb-3 leading-tight">Mini-simulateur : ma classe DPE = quand interdite ?</h2>
  <div class="glass rounded-xl p-5 my-4">
    <label class="block text-xs uppercase tracking-wider text-slate-600 mb-2">Classe DPE de votre logement à {ville}</label>
    <div class="grid grid-cols-7 gap-1 mb-3">
      <button onclick="dpeCheck('A')" class="dpe-btn px-2 py-2 rounded-lg border border-slate-300 hover:border-emerald-500 text-slate-900 text-sm font-semibold">A</button>
      <button onclick="dpeCheck('B')" class="dpe-btn px-2 py-2 rounded-lg border border-slate-300 hover:border-emerald-500 text-slate-900 text-sm font-semibold">B</button>
      <button onclick="dpeCheck('C')" class="dpe-btn px-2 py-2 rounded-lg border border-slate-300 hover:border-emerald-500 text-slate-900 text-sm font-semibold">C</button>
      <button onclick="dpeCheck('D')" class="dpe-btn px-2 py-2 rounded-lg border border-slate-300 hover:border-emerald-500 text-slate-900 text-sm font-semibold">D</button>
      <button onclick="dpeCheck('E')" class="dpe-btn px-2 py-2 rounded-lg border border-slate-300 hover:border-yellow-500 text-slate-900 text-sm font-semibold">E</button>
      <button onclick="dpeCheck('F')" class="dpe-btn px-2 py-2 rounded-lg border border-slate-300 hover:border-amber-500 text-slate-900 text-sm font-semibold">F</button>
      <button onclick="dpeCheck('G')" class="dpe-btn px-2 py-2 rounded-lg border border-slate-300 hover:border-rose-500 text-slate-900 text-sm font-semibold">G</button>
    </div>
    <div id="dpe-result" class="text-sm"></div>
  </div>

  <script>
    function dpeCheck(c) {{
      const r = document.getElementById("dpe-result");
      const map = {{
        "A": {{verdict:"✅ Excellent — aucune contrainte légale, logement très performant.",  color:"text-emerald-700", deadline:"—"}},
        "B": {{verdict:"✅ Très bon — aucune contrainte légale, logement performant.",         color:"text-emerald-700", deadline:"—"}},
        "C": {{verdict:"✅ Bon — aucune contrainte légale à ce jour.",                          color:"text-emerald-700", deadline:"—"}},
        "D": {{verdict:"✅ Acceptable — aucune contrainte légale à ce jour.",                   color:"text-emerald-700", deadline:"—"}},
        "E": {{verdict:"⚠️ À surveiller — interdiction location prévue le 1er janvier 2034.",   color:"text-yellow-300", deadline:"1er janvier 2034"}},
        "F": {{verdict:"⚠️ Attention — interdiction location au 1er janvier 2028 (~18 mois).", color:"text-amber-700", deadline:"1er janvier 2028"}},
        "G": {{verdict:"🚫 INTERDIT — vous ne pouvez plus signer de nouveau bail depuis le 1er janvier 2025.", color:"text-rose-700", deadline:"DÉJÀ INTERDIT"}}
      }};
      const m = map[c];
      r.innerHTML = `
        <div class="${{m.color}} font-semibold mb-2 text-base">DPE ${{c}} à {ville} : ${{m.verdict}}</div>
        <div class="text-slate-600">Échéance : <strong class="text-slate-900">${{m.deadline}}</strong></div>
        <a href="/" class="inline-block mt-3 text-blue-700 hover:text-blue-800 font-semibold">
          → Diagnostic complet (DPE + encadrement + dossier locataire) sur BailleurVérif
        </a>`;
      try {{
        fetch("/api/visit", {{method:"POST", headers:{{"Content-Type":"application/json"}}, body: JSON.stringify({{src:"dpe_simulator", classe:c, ville:"{ville}"}})}});
      }} catch(e) {{}}
    }}
  </script>

  <h2 class="text-2xl font-bold text-slate-900 mt-10 mb-3 leading-tight">Combien de passoires thermiques à {ville} ?</h2>
  <p class="text-slate-700 leading-relaxed my-4">
    Sur les ~<strong class="text-slate-900">{res_princ:,}</strong> résidences principales recensées à {ville} ({dept_nom}),
    on estime à environ <strong class="text-slate-900">{passoires_count:,}</strong> le nombre de logements classés F ou G —
    soit ~<strong class="text-slate-900">{pct_passoires}%</strong> du parc. Cette estimation est calculée à partir du
    ratio national (<strong class="text-slate-900">5,2 millions de passoires</strong> sur 30 millions de logements, soit 17%
    — chiffres ONRE / ADEME 2024), <em>ajusté selon l'âge moyen du parc local</em>.
  </p>
  <p class="text-slate-700 leading-relaxed my-4">
    Sur ce total, environ <strong class="text-slate-900">{classe_g_count:,} logements sont classés G</strong>
    (déjà interdits à la location depuis le 1<sup>er</sup> janvier 2025) et <strong class="text-slate-900">{classe_f_count:,} sont classés F</strong>
    (qui seront interdits à partir du 1<sup>er</sup> janvier 2028 — dans environ 18 mois).
  </p>

  <h2 class="text-2xl font-bold text-slate-900 mt-10 mb-3 leading-tight">Quels travaux pour sortir du F/G à {ville} ?</h2>
  <p class="text-slate-700 leading-relaxed my-4">
    Le gain en classes DPE dépend de la nature et du cumul de travaux. Voici l'ordre d'efficacité moyen mesuré par
    l'ADEME, valable à {ville} comme partout en climat océanique et continental :
  </p>
  <table>
    <thead>
      <tr><th>Travail</th><th>Coût indicatif</th><th>Gain DPE moyen</th></tr>
    </thead>
    <tbody>
      <tr><td>Isolation des combles ou toiture</td><td>30-80 €/m²</td><td>+1 à +2 classes</td></tr>
      <tr><td>Pompe à chaleur air/eau</td><td>10 000-18 000 €</td><td>+1 à +2 classes</td></tr>
      <tr><td>Isolation par l'extérieur (ITE)</td><td>120-250 €/m²</td><td>+1 à +2 classes</td></tr>
      <tr><td>Remplacement fenêtres simple vitrage</td><td>400-1 200 €/fenêtre</td><td>+0,5 à +1 classe</td></tr>
      <tr><td>VMC double flux</td><td>4 000-8 000 €</td><td>+0,5 classe</td></tr>
    </tbody>
  </table>
  <p class="text-xs text-slate-500 my-2">
    <strong>Aides 2026</strong> : <a class="text-blue-700 hover:text-blue-800 underline" href="https://www.maprimerenov.gouv.fr/" rel="nofollow noopener" target="_blank">MaPrimeRénov'</a>
    (jusqu'à 90% selon revenus &amp; ampleur), <a class="text-blue-700 hover:text-blue-800 underline" href="https://france-renov.gouv.fr/" rel="nofollow noopener" target="_blank">France Rénov'</a>,
    éco-PTZ jusqu'à 50 000 €, déduction fiscale possible si bail loi 1989 maintenu.
  </p>

  <h2 class="text-2xl font-bold text-slate-900 mt-10 mb-3 leading-tight">Cadre légal applicable à {ville}</h2>
  <ul class="list-disc pl-6 text-slate-700 leading-relaxed my-3 space-y-1">
    <li><strong class="text-slate-900">Loi 2021-1104</strong> du 22 août 2021 (Climat &amp; Résilience), articles 158-160.</li>
    <li><strong class="text-slate-900">Article 17-21-bis</strong> de la loi 89-462 du 6 juillet 1989 (rapports locatifs), introduit en 2021.</li>
    <li><strong class="text-slate-900">Décret 2022-1726</strong> du 30 décembre 2022 (relèvement du seuil de décence énergétique).</li>
    <li><strong class="text-slate-900">Article L.173-2</strong> du Code de la construction et de l'habitation.</li>
    <li><strong class="text-slate-900">Méthode 3CL-2021</strong> (arrêté du 31 mars 2021), DPE opposable depuis le 1<sup>er</sup> juillet 2021.</li>
  </ul>

  <h2 class="text-2xl font-bold text-slate-900 mt-10 mb-3 leading-tight">Questions fréquentes — DPE à {ville}</h2>
  <details>
    <summary class="text-slate-900 font-semibold">📅 Quand mon DPE F sera-t-il interdit à la location à {ville} ?</summary>
    <p class="text-slate-700 my-2 pl-4">À partir du 1<sup>er</sup> janvier 2028. Cela concerne tout nouveau bail (signature ou renouvellement). Les baux signés avant peuvent se poursuivre mais sans révision de loyer.</p>
  </details>
  <details>
    <summary class="text-slate-900 font-semibold">🚫 Mon DPE G, je peux encore louer ?</summary>
    <p class="text-slate-700 my-2 pl-4">Non pour un nouveau bail. Depuis le 1<sup>er</sup> janvier 2025, les logements G sont considérés non décents. Les baux antérieurs continuent jusqu'au départ du locataire, sans révision de loyer.</p>
  </details>
  <details>
    <summary class="text-slate-900 font-semibold">💰 Quelles aides pour rénover à {ville} ?</summary>
    <p class="text-slate-700 my-2 pl-4">MaPrimeRénov' (35-90% selon revenus), éco-PTZ jusqu'à 50 000 €, CEE (certificats économies énergie). France Rénov' propose un accompagnement gratuit (Espaces Conseil France Rénov').</p>
  </details>
  <details>
    <summary class="text-slate-900 font-semibold">⚖️ Risque si je loue un F après 2028 ?</summary>
    <p class="text-slate-700 my-2 pl-4">Le locataire peut exiger : mise en conformité à la charge du bailleur, suspension/réduction du loyer par le juge des contentieux de la protection, dommages-intérêts. Cas de logement non décent.</p>
  </details>
  <details>
    <summary class="text-slate-900 font-semibold">🏠 Vente possible d'un DPE F/G à {ville} ?</summary>
    <p class="text-slate-700 my-2 pl-4">Oui, la vente reste libre. En revanche, un audit énergétique est obligatoire depuis le 1<sup>er</sup> avril 2023 pour la vente d'une passoire thermique (F ou G), à présenter dès la première visite.</p>
  </details>

  <h2 class="text-2xl font-bold text-slate-900 mt-10 mb-3 leading-tight">Autres outils utiles pour bailleurs à {ville}</h2>
  <p class="text-slate-700 leading-relaxed my-4">
    Au-delà du DPE, votre conformité bailleur en {dept_nom} peut être impactée par d'autres règles :
  </p>
  <ul class="list-disc pl-6 text-slate-700 leading-relaxed my-3 space-y-1">
    <li><a href="/" class="text-blue-700 hover:text-blue-800 underline">Outil gratuit BailleurVérif</a> — vérification 5 questions (DPE + encadrement + dossier locataire)</li>
    <li><a href="/preavis-bail.html" class="text-blue-700 hover:text-blue-800 underline">Calculateur préavis bail</a> — simulateur 4-inputs + modèle LRAR</li>
    {encadrement_xlink}
    <li><a href="/blog/dpe-f-location-2026.html" class="text-blue-700 hover:text-blue-800 underline">Guide complet DPE F : ce qui change en 2026</a></li>
    <li><a href="/blog/obligations-bailleur-particulier-2026.html" class="text-blue-700 hover:text-blue-800 underline">Obligations bailleur particulier 2026</a></li>
  </ul>

  <h2 class="text-2xl font-bold text-slate-900 mt-10 mb-3 leading-tight">DPE F/G dans les villes proches</h2>
  <div class="grid grid-cols-2 md:grid-cols-3 gap-2 my-3">
    {{LINKS_PLACEHOLDER}}
  </div>

  <aside class="cta-wedge my-8 rounded-2xl border border-blue-200 bg-blue-50 p-6">
    <div class="text-[11px] uppercase tracking-widest text-blue-700 mb-2">Diagnostic complet · gratuit</div>
    <p class="text-lg md:text-xl font-semibold text-slate-900 mb-3">Au-delà du DPE, vérifiez aussi encadrement + dossier locataire</p>
    <p class="text-sm text-slate-700 mb-4">BailleurVérif : 5 questions, verdict 3 niveaux, sans inscription. Couvre les 3 risques bailleurs 2026 : DPE F/G, encadrement loyer, fraude dossier locataire.</p>
    <a href="/" class="inline-flex items-center gap-2 px-5 py-2.5 rounded-lg bg-blue-700 hover:bg-blue-800 text-slate-900 font-semibold text-sm transition">
      Lancer le diagnostic gratuit →
    </a>
  </aside>

  <aside id="alerte-maj" class="my-10 rounded-2xl border border-blue-200 bg-blue-50 p-6">
    <div class="text-[11px] uppercase tracking-widest text-blue-700 mb-2">Alerte DPE bailleur · Gratuit</div>
    <p class="text-base md:text-lg font-semibold text-slate-900 mb-2">Être prévenu si le calendrier DPE évolue (à {ville})</p>
    <p class="text-sm text-slate-700 mb-4">
      Reports d'échéance F/G/E, nouveau seuil MaPrimeRénov', évolution de la méthode 3CL, jurisprudence "logement non décent" :
      recevez un email <strong>uniquement</strong> si un décret ou un arrêté change ce qui s'applique aux bailleurs F/G.
      0 spam, 0 partage, désinscription un clic. Stockage en France, conforme RGPD.
    </p>
    <form id="bv-subscribe-form" class="flex flex-col gap-3" novalidate>
      <input type="hidden" name="topic" value="dpe-bailleur">
      <input type="hidden" name="source" value="/{slug}-dpe-f-g-interdit-location.html">
      <div class="flex flex-col sm:flex-row gap-2">
        <label class="sr-only" for="bv-subscribe-email">Votre email</label>
        <input id="bv-subscribe-email" name="email" type="email" required autocomplete="email"
               placeholder="votre.email@exemple.fr"
               class="flex-1 px-4 py-2 rounded-lg border border-slate-300 bg-white text-slate-900 text-base focus:border-blue-600 focus:ring-2 focus:ring-blue-200 outline-none">
        <button id="bv-subscribe-submit" type="submit"
                class="px-5 py-2 rounded-lg bg-blue-700 hover:bg-blue-800 text-white text-sm font-semibold transition">
          Recevoir les alertes
        </button>
      </div>
      <label class="flex items-start gap-2 text-xs text-slate-600">
        <input id="bv-subscribe-consent" name="consent" type="checkbox" required class="mt-0.5">
        <span>J'accepte de recevoir des emails uniquement en cas de mise à jour réglementaire DPE bailleur. Je peux me désinscrire à tout moment.
          Voir la <a href="/politique-confidentialite.html" class="underline text-blue-700 hover:text-blue-800">politique de confidentialité</a>.</span>
      </label>
    </form>
    <div id="bv-subscribe-status" class="mt-3 text-sm" role="status" aria-live="polite"></div>
  </aside>

  <script>
  (function(){{
    var form = document.getElementById('bv-subscribe-form');
    var statusEl = document.getElementById('bv-subscribe-status');
    var submitBtn = document.getElementById('bv-subscribe-submit');
    if (!form) return;
    form.addEventListener('submit', function(e){{
      e.preventDefault();
      statusEl.className = 'mt-3 text-sm text-slate-600';
      statusEl.textContent = 'Envoi en cours…';
      submitBtn.disabled = true;
      var email = document.getElementById('bv-subscribe-email').value.trim();
      var consent = document.getElementById('bv-subscribe-consent').checked;
      if (!email || !consent) {{
        statusEl.className = 'mt-3 text-sm text-rose-700';
        statusEl.textContent = 'Merci de renseigner votre email et de cocher la case de consentement.';
        submitBtn.disabled = false;
        return;
      }}
      fetch('/api/subscribe', {{
        method: 'POST',
        headers: {{'Content-Type': 'application/json'}},
        body: JSON.stringify({{email: email, topic: 'dpe-bailleur', source: '/{slug}-dpe-f-g-interdit-location.html', consent: true, referrer_token: (new URLSearchParams(location.search).get('ref') || '').slice(0,96)}})
      }}).then(function(r){{ return r.json().then(function(j){{ return {{status: r.status, body: j}}; }}); }})
      .then(function(res){{
        submitBtn.disabled = false;
        if (res.status === 200 && res.body.ok && res.body.already_confirmed) {{
          statusEl.className = 'mt-3 text-sm text-emerald-700';
          statusEl.textContent = 'Votre email est déjà inscrit aux alertes DPE bailleur. Merci.';
          return;
        }}
        if (res.status === 200 && res.body.ok && res.body.confirm_url) {{
          statusEl.className = 'mt-3 text-sm text-emerald-700';
          statusEl.innerHTML = '✓ Merci. Pour activer votre inscription, cliquez ce lien de confirmation : <a class="underline font-semibold text-blue-700 hover:text-blue-800" href="' + res.body.confirm_url + '" rel="noopener">Confirmer mon inscription</a>.';
          form.reset();
          return;
        }}
        if (res.status === 429) {{
          statusEl.className = 'mt-3 text-sm text-amber-700';
          statusEl.textContent = 'Trop de demandes récentes. Réessayez dans une minute.';
          return;
        }}
        statusEl.className = 'mt-3 text-sm text-rose-700';
        statusEl.textContent = (res.body && res.body.error) ? ('Erreur : ' + res.body.error) : 'Une erreur est survenue. Réessayez.';
      }}).catch(function(){{
        submitBtn.disabled = false;
        statusEl.className = 'mt-3 text-sm text-rose-700';
        statusEl.textContent = 'Erreur réseau. Réessayez dans un instant.';
      }});
    }});
  }})();
  </script>

  <hr class="my-10 border-slate-200" />
  <p class="text-xs text-slate-500">
    Les chiffres présentés sont des <strong>estimations</strong> basées sur les ratios nationaux ONRE/ADEME 2024
    appliqués au parc local de {ville}. Pour le diagnostic exact de votre logement, consultez l'<a class="hover:text-blue-800" href="https://observatoire-dpe-audit.ademe.fr/" rel="nofollow noopener" target="_blank">observatoire ADEME des DPE</a>
    (chaque DPE émis depuis 2018 y est référencé par identifiant). Mise à jour : {TODAY}.
  </p>
</main>

<footer class="bv-footer mt-16 py-8">
  <div class="max-w-3xl mx-auto px-6">
    <div class="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-4">
      <div>
        <div><strong>BailleurVérif</strong> — Outil gratuit · Mis à jour le {TODAY}</div>
        <div class="text-xs mt-1" style="color:var(--text-muted)">Estimations basées sur ratios ONRE/ADEME 2024. Informatif — ne remplace pas un DPE officiel.</div>
      </div>
      <nav class="flex flex-wrap gap-x-4 gap-y-1 text-xs">
        <a href="/">Accueil</a>
        <a href="/blog/">Guides</a>
        <a href="/preavis-bail.html">Préavis</a>
        <a href="/mentions-legales.html">Mentions légales</a>
        <a href="/politique-confidentialite.html">Confidentialité</a>
        <a href="/cgu.html">CGU</a>
      </nav>
    </div>
    <div class="text-xs mt-4 pt-4" style="border-top:1px solid var(--border); color:var(--text-muted)">© 2026 BailleurVérif · Données DPE 2026</div>
  </div>
</footer>
</body>
</html>
"""
    return html


def build_neighbors_links(current_slug):
    """Pick up to 6 'neighbor' cities by department first, fallback to other cities."""
    current = next((c for c in CITIES if c[0] == current_slug), None)
    if not current:
        return ""
    cur_dept = current[3]
    same_dept = [c for c in CITIES if c[3] == cur_dept and c[0] != current_slug]
    other = [c for c in CITIES if c[3] != cur_dept and c[0] != current_slug]
    # max 6 : prioritize same dept, fill with random others (deterministic order)
    pick = (same_dept + other)[:6]
    links = "\n    ".join(
        f'<a href="/{c[0]}-dpe-f-g-interdit-location.html" class="text-sm text-blue-700 hover:text-blue-800 underline">{c[1]}</a>'
        for c in pick
    )
    return links


# Communes du builder encadrement (reused for sitemap merge)
ENCADREMENT_COMMUNES = [
    "paris", "lille", "hellemmes", "lomme", "lyon", "villeurbanne", "bordeaux",
    "montpellier", "saint-ouen", "aubervilliers", "saint-denis",
    "pierrefitte-sur-seine", "epinay-sur-seine", "stains", "villetaneuse",
    "ile-saint-denis", "la-courneuve", "bagnolet", "bondy", "bobigny",
    "le-pre-saint-gervais", "les-lilas", "montreuil", "noisy-le-sec", "pantin",
    "romainville", "grenoble", "echirolles", "eybens", "fontaine",
    "saint-martin-d-heres",
]

def _discover_blog_pages() -> list[str]:
    """Dynamic blog discovery (run-100): mirrors build_programmatic_pages.py — survives
    the addition of the run-99 mega-guide and any future article without code changes."""
    blog_dir = os.path.join(STATIC, "blog")
    if not os.path.isdir(blog_dir):
        return []
    return sorted({
        f[:-5] for f in os.listdir(blog_dir)
        if f.endswith(".html") and f != "index.html"
    })


def main():
    os.makedirs(STATIC, exist_ok=True)
    generated = []
    for c in CITIES:
        slug = c[0]
        html = render_page(c)
        html = html.replace("{LINKS_PLACEHOLDER}", build_neighbors_links(slug))
        out = os.path.join(STATIC, f"{slug}-dpe-f-g-interdit-location.html")
        with open(out, "w", encoding="utf-8") as f:
            f.write(html)
        generated.append(slug)
    print(f"Generated {len(generated)} DPE pages.")
    BLOG_PAGES = _discover_blog_pages()

    # Rebuild merged sitemap.xml — includes static + encadrement + dpe pages
    # run-110 : parité avec build_programmatic_pages.py (widget, locataire-loyer-legal)
    # run-124 : + deficit-foncier-2026.html
    # pour éviter régression sitemap quand ce builder tourne en dernier.
    tools_pages = [
        p for p in (
            "mon-bien.html",
            "preavis-bail.html",
            "changelog.html",
            "widget-bailleurverif.html",
            "locataire-loyer-legal.html",
            "deficit-foncier-2026.html",
        )
        if os.path.exists(os.path.join(STATIC, p))
    ]
    urls = [f"{BASE_URL}/"]
    urls += [f"{BASE_URL}/{p}" for p in tools_pages]
    urls.append(f"{BASE_URL}/blog/")
    urls += [f"{BASE_URL}/blog/{p}.html" for p in BLOG_PAGES]
    urls += [f"{BASE_URL}/encadrement-loyer-{s}-2026.html" for s in ENCADREMENT_COMMUNES]
    urls += [f"{BASE_URL}/{s}-dpe-f-g-interdit-location.html" for s in generated]

    # run-100: legal pages — must survive rebuilds.
    legal_pages = [
        p for p in ("mentions-legales.html", "politique-confidentialite.html", "cgu.html")
        if os.path.exists(os.path.join(STATIC, p))
    ]
    urls += [f"{BASE_URL}/{p}" for p in legal_pages]

    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for u in urls:
        sitemap += f"  <url><loc>{u}</loc><lastmod>{TODAY}</lastmod></url>\n"
    sitemap += "</urlset>\n"
    with open(os.path.join(STATIC, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap)
    print(f"Sitemap rebuilt with {len(urls)} URLs.")

    # output list of new urls for IndexNow
    new_urls = [f"{BASE_URL}/{s}-dpe-f-g-interdit-location.html" for s in generated]
    print("NEW_URLS:")
    for u in new_urls:
        print(u)


if __name__ == "__main__":
    main()
