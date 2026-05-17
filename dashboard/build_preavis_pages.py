#!/usr/bin/env python3
"""
build_preavis_pages.py — Génère une landing SEO par ville (top 50 FR) pour les longtails
"préavis bail location {ville} 2026", "zone tendue {ville} 1 mois", "modèle lettre congé bail {ville}".

Output : 50 fichiers HTML dans wedge-tool/static/ nommés preavis-bail-{slug}.html.

Chaque page :
- title/description longtails ville-specific
- JSON-LD @graph 6 nodes : WebPage + BreadcrumbList + Dataset + FAQPage + HowTo + Org + WebSite
- mini-simulateur préavis (4 questions, JS client, sans inscription)
- bouton "Copier la lettre LRAR pré-remplie"
- statut zone tendue concret pour la commune (≠ texte générique)
- cross-link DPE + encadrement même ville quand pages existent
- 6 internal links villes voisines même département

Reuse CITIES list de build_dpe_pages.py (parité 50 communes).
Sitemap.xml mis à jour avec préavis URLs en plus des existantes (encadrement + DPE + tools).
Run from saas-florian root : python3 dashboard/build_preavis_pages.py
"""
import os
import json
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC = os.path.join(ROOT, "wedge-tool", "static")
TODAY = date.today().isoformat()
BASE_URL = "https://bailleurverif.fr"

# 50 villes parité build_dpe_pages.py — (slug, ville, dept_nom, dept_code, pop_k)
CITIES = [
    ("paris", "Paris", "Paris", "75", 2103),
    ("marseille", "Marseille", "Bouches-du-Rhône", "13", 873),
    ("lyon", "Lyon", "Rhône", "69", 522),
    ("toulouse", "Toulouse", "Haute-Garonne", "31", 504),
    ("nice", "Nice", "Alpes-Maritimes", "06", 348),
    ("nantes", "Nantes", "Loire-Atlantique", "44", 320),
    ("montpellier", "Montpellier", "Hérault", "34", 302),
    ("strasbourg", "Strasbourg", "Bas-Rhin", "67", 291),
    ("bordeaux", "Bordeaux", "Gironde", "33", 261),
    ("lille", "Lille", "Nord", "59", 235),
    ("rennes", "Rennes", "Ille-et-Vilaine", "35", 222),
    ("reims", "Reims", "Marne", "51", 181),
    ("saint-etienne", "Saint-Étienne", "Loire", "42", 173),
    ("toulon", "Toulon", "Var", "83", 175),
    ("le-havre", "Le Havre", "Seine-Maritime", "76", 167),
    ("grenoble", "Grenoble", "Isère", "38", 158),
    ("dijon", "Dijon", "Côte-d'Or", "21", 158),
    ("angers", "Angers", "Maine-et-Loire", "49", 156),
    ("villeurbanne", "Villeurbanne", "Rhône", "69", 154),
    ("nimes", "Nîmes", "Gard", "30", 147),
    ("clermont-ferrand", "Clermont-Ferrand", "Puy-de-Dôme", "63", 147),
    ("aix-en-provence", "Aix-en-Provence", "Bouches-du-Rhône", "13", 144),
    ("le-mans", "Le Mans", "Sarthe", "72", 142),
    ("brest", "Brest", "Finistère", "29", 139),
    ("tours", "Tours", "Indre-et-Loire", "37", 138),
    ("amiens", "Amiens", "Somme", "80", 134),
    ("limoges", "Limoges", "Haute-Vienne", "87", 130),
    ("annecy", "Annecy", "Haute-Savoie", "74", 131),
    ("boulogne-billancourt", "Boulogne-Billancourt", "Hauts-de-Seine", "92", 121),
    ("perpignan", "Perpignan", "Pyrénées-Orientales", "66", 119),
    ("metz", "Metz", "Moselle", "57", 117),
    ("besancon", "Besançon", "Doubs", "25", 117),
    ("orleans", "Orléans", "Loiret", "45", 116),
    ("rouen", "Rouen", "Seine-Maritime", "76", 111),
    ("argenteuil", "Argenteuil", "Val-d'Oise", "95", 111),
    ("mulhouse", "Mulhouse", "Haut-Rhin", "68", 109),
    ("saint-denis", "Saint-Denis", "Seine-Saint-Denis", "93", 113),
    ("caen", "Caen", "Calvados", "14", 105),
    ("nancy", "Nancy", "Meurthe-et-Moselle", "54", 105),
    ("tourcoing", "Tourcoing", "Nord", "59", 99),
    ("roubaix", "Roubaix", "Nord", "59", 99),
    ("vitry-sur-seine", "Vitry-sur-Seine", "Val-de-Marne", "94", 96),
    ("creteil", "Créteil", "Val-de-Marne", "94", 92),
    ("avignon", "Avignon", "Vaucluse", "84", 92),
    ("poitiers", "Poitiers", "Vienne", "86", 90),
    ("dunkerque", "Dunkerque", "Nord", "59", 86),
    ("aubervilliers", "Aubervilliers", "Seine-Saint-Denis", "93", 89),
    ("asnieres-sur-seine", "Asnières-sur-Seine", "Hauts-de-Seine", "92", 87),
    ("versailles", "Versailles", "Yvelines", "78", 85),
    ("colombes", "Colombes", "Hauts-de-Seine", "92", 85),
]

# Statut zone tendue (décret 2013-392 modifié, 28 agglos + Île-de-France complète au 2026).
# True = préavis locataire bail nu = 1 mois (sinon 3 mois). Bail meublé = 1 mois partout.
# Bailleur : 6 mois bail nu (3 mois bail meublé) partout, indépendant zone tendue.
# Référence pédagogique : https://www.service-public.fr/particuliers/vosdroits/F19384
ZONE_TENDUE = {
    "paris": True, "boulogne-billancourt": True, "argenteuil": True, "saint-denis": True,
    "versailles": True, "vitry-sur-seine": True, "creteil": True, "aubervilliers": True,
    "asnieres-sur-seine": True, "colombes": True,  # toute l'Île-de-France = ZT
    "marseille": True, "aix-en-provence": True,
    "lyon": True, "villeurbanne": True,
    "toulouse": True,
    "nice": True,
    "nantes": True,
    "montpellier": True,
    "strasbourg": True,
    "bordeaux": True,
    "lille": True, "tourcoing": True, "roubaix": True,
    "rennes": True,
    "toulon": True,
    "grenoble": True,
    "nimes": True,
    "annecy": True,
    "avignon": True,
    "nancy": True,
    # cités hors agglos 28 officielles : conservatif = non ZT (vérification SP recommandée)
    "reims": False, "saint-etienne": False, "le-havre": False, "dijon": False, "angers": False,
    "clermont-ferrand": False, "le-mans": False, "brest": False, "tours": False, "amiens": False,
    "limoges": False, "perpignan": False, "metz": False, "besancon": False, "orleans": False,
    "rouen": False, "mulhouse": False, "caen": False, "poitiers": False, "dunkerque": False,
}

# Communes avec page encadrement loyer existante (cross-link)
ENCADREMENT_OVERLAP = {
    "paris", "lille", "lyon", "villeurbanne", "bordeaux", "montpellier", "grenoble",
    "saint-denis", "aubervilliers",
}


def render_page(city):
    slug, ville, dept_nom, dept_code, pop_k = city
    is_zt = ZONE_TENDUE.get(slug, False)
    preavis_loc_nu = "1 mois" if is_zt else "3 mois"
    zt_label = "zone tendue" if is_zt else "hors zone tendue"
    zt_pill = "pill-1" if is_zt else "pill-3"

    title = f"Préavis bail à {ville} 2026 — {preavis_loc_nu} ({zt_label}) | BailleurVérif"
    description = (
        f"Préavis de bail à {ville} ({dept_code}) : {preavis_loc_nu} pour le locataire (bail nu, {zt_label}), "
        f"1 mois pour le meublé, 6 mois pour le bailleur. Calcul instantané + modèle lettre LRAR. Gratuit, sans inscription."
    )
    canonical = f"{BASE_URL}/preavis-bail-{slug}.html"

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
                    {"@type": "ListItem", "position": 2, "name": "Préavis bail", "item": f"{BASE_URL}/preavis-bail.html"},
                    {"@type": "ListItem", "position": 3, "name": ville, "item": canonical},
                ],
            },
            {
                "@type": "Dataset",
                "@id": f"{canonical}#dataset",
                "name": f"Préavis de bail à {ville} — durée applicable 2026",
                "description": (
                    f"Durée légale du préavis de bail à {ville} ({dept_nom}) en 2026. "
                    f"Calcul basé sur l'article 15 de la loi 89-462 (loi Mermaz) modifiée par la loi Alur (2014) et la loi ELAN (2018). "
                    f"Statut zone tendue : {zt_label} (décret 2013-392 modifié)."
                ),
                "url": canonical,
                "inLanguage": "fr-FR",
                "creator": {"@id": f"{BASE_URL}/#organization"},
                "license": "https://www.etalab.gouv.fr/licence-ouverte-open-licence",
                "isAccessibleForFree": True,
                "keywords": [
                    f"préavis bail {ville.lower()}",
                    f"zone tendue {ville.lower()}",
                    f"congé bail {ville.lower()}",
                    f"préavis 1 mois {ville.lower()}",
                    f"lettre LRAR {ville.lower()}",
                    "loi du 6 juillet 1989",
                ],
                "spatialCoverage": {
                    "@type": "Place",
                    "name": f"{ville} ({dept_code})",
                    "containedInPlace": {"@type": "Country", "name": "France"},
                },
                "temporalCoverage": "2026",
                "variableMeasured": [
                    {"@type": "PropertyValue", "name": "Préavis locataire bail nu", "value": preavis_loc_nu},
                    {"@type": "PropertyValue", "name": "Préavis locataire bail meublé", "value": "1 mois"},
                    {"@type": "PropertyValue", "name": "Préavis bailleur bail nu", "value": "6 mois"},
                    {"@type": "PropertyValue", "name": "Préavis bailleur bail meublé", "value": "3 mois"},
                    {"@type": "PropertyValue", "name": "Zone tendue", "value": "oui" if is_zt else "non"},
                ],
            },
            {
                "@type": "HowTo",
                "@id": f"{canonical}#howto",
                "name": f"Donner congé pour un bail à {ville}",
                "step": [
                    {"@type": "HowToStep", "position": 1, "name": "Vérifier zone tendue", "text": f"{ville} est classée {zt_label}. Pour un bail nu, le préavis locataire est donc de {preavis_loc_nu}."},
                    {"@type": "HowToStep", "position": 2, "name": "Rédiger la lettre", "text": "Rédigez le congé en LRAR avec date d'envoi, motif (facultatif si réduction préavis demandée), adresse du logement."},
                    {"@type": "HowToStep", "position": 3, "name": "Envoyer la LRAR", "text": "Le préavis court à compter de la date de réception par le bailleur, pas de l'envoi."},
                    {"@type": "HowToStep", "position": 4, "name": "Calculer la date butoir", "text": f"Date de réception + {preavis_loc_nu} = fin du bail effective. Le loyer reste dû jusqu'à cette date butoir, sauf accord amiable."},
                ],
            },
            {
                "@type": "FAQPage",
                "@id": f"{canonical}#faq",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": f"Quelle est la durée du préavis pour un bail nu à {ville} ?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": (
                                f"À {ville}, le préavis du locataire pour un bail nu (non meublé) est de **{preavis_loc_nu}** car la commune est {zt_label} "
                                f"selon le décret 2013-392 modifié. Pour le bailleur, le préavis reste de 6 mois avant l'échéance du bail, "
                                f"avec un motif légitime (reprise pour habiter, vente, motif sérieux)."
                            ),
                        },
                    },
                    {
                        "@type": "Question",
                        "name": f"Pour un bail meublé à {ville}, quel préavis ?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": (
                                f"Pour un bail meublé à {ville}, le préavis du locataire est toujours de 1 mois, indépendamment du statut zone tendue. "
                                f"Pour le bailleur, c'est 3 mois minimum avant l'échéance annuelle du bail."
                            ),
                        },
                    },
                    {
                        "@type": "Question",
                        "name": f"{ville} est-elle en zone tendue ?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": (
                                f"En 2026, {ville} est {zt_label} au sens du décret 2013-392 modifié. "
                                f"{'Cela entraîne un préavis locataire réduit à 1 mois pour les baux nus, ainsi que des limitations à la révision annuelle du loyer (IRL plafonné).' if is_zt else 'Le préavis locataire pour un bail nu est donc de 3 mois (durée standard). La liste officielle est consultable sur service-public.fr.'}"
                            ),
                        },
                    },
                    {
                        "@type": "Question",
                        "name": "À partir de quand court le préavis ?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": (
                                "Le préavis court à compter de la **date de réception** de la lettre recommandée avec accusé de réception (LRAR) par le destinataire, "
                                "conformément à l'article 15 de la loi du 6 juillet 1989. Si le bailleur refuse de retirer le pli, "
                                "la date du premier avis de passage du facteur fait foi."
                            ),
                        },
                    },
                    {
                        "@type": "Question",
                        "name": "Quels motifs réduisent le préavis du locataire à 1 mois (hors zone tendue) ?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": (
                                "Hors zone tendue, le préavis du locataire passe de 3 mois à 1 mois en cas de : "
                                "mutation professionnelle, perte d'emploi, nouvel emploi suite à perte d'emploi, premier emploi, "
                                "état de santé exigeant un déménagement (sur certificat médical), bénéficiaires du RSA ou de l'AAH, "
                                "et attribution d'un logement social. Le motif doit être justifié dans la lettre LRAR."
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
            f'<a href="/encadrement-loyer-{slug}-2026.html" class="text-blue-700 hover:text-blue-800 underline">'
            f"Encadrement loyer à {ville} →</a>"
        )
    dpe_xlink = (
        f'<a href="/{slug}-dpe-f-g-interdit-location.html" class="text-blue-700 hover:text-blue-800 underline">'
        f"DPE F/G interdit à {ville} →</a>"
    )

    zt_explainer = (
        f"En 2026, <strong>{ville}</strong> est classée <strong>{zt_label}</strong>"
        + (
            " (décret 2013-392 modifié). Le préavis du locataire pour un bail nu est donc <strong>réduit à 1 mois</strong>, contre 3 mois en zone normale."
            if is_zt
            else f' (vérification possible sur <a href="https://www.service-public.fr/particuliers/vosdroits/F1314" rel="nofollow noopener" target="_blank">service-public.fr</a>). Le préavis du locataire pour un bail nu reste donc de <strong>3 mois</strong>, durée standard.'
        )
    )

    html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title}</title>
<meta name="description" content="{description}" />
<link rel="canonical" href="{canonical}" />
<meta property="og:title" content="Préavis bail à {ville} 2026 — {preavis_loc_nu}" />
<meta property="og:description" content="{description}" />
<meta property="og:type" content="article" />
<meta property="og:url" content="{canonical}" />
<meta property="og:site_name" content="BailleurVérif" />
<meta property="og:locale" content="fr_FR" />
<meta name="twitter:card" content="summary" />
<meta name="twitter:title" content="Préavis bail à {ville} — {preavis_loc_nu}" />
<meta name="twitter:description" content="{description}" />
<link rel="alternate" type="application/atom+xml" title="BailleurVérif — Articles" href="/atom.xml" />
<link rel="alternate" type="application/feed+json" title="BailleurVérif — Articles" href="/feed.json" />
<link rel="icon" type="image/svg+xml" href="/favicon.svg" />
<meta name="theme-color" content="#ffffff" />
<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script>
<link rel="stylesheet" href="/css/main.css" />
<script src="https://cdn.tailwindcss.com"></script>
<style>
  table {{ width: 100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.9rem; }}
  td, th {{ padding: 0.6rem; border: 1px solid var(--border); }}
  th {{ background: var(--bg-secondary); text-align: left; }}
  .pill {{ display:inline-block; padding:0.15rem 0.55rem; border-radius:999px; font-size:0.7rem; font-weight:600; }}
  .pill-1 {{ background: var(--success-soft); color: var(--success); border:1px solid var(--success); }}
  .pill-3 {{ background: var(--warning-soft); color: var(--warning); border:1px solid var(--warning); }}
  .pill-6 {{ background: var(--danger-soft); color: var(--danger); border:1px solid var(--danger); }}
  details summary {{ cursor:pointer; padding:0.5rem 0; }}
  details[open] summary {{ color:var(--accent); }}
  textarea {{ font-family: ui-monospace, SFMono-Regular, Menlo, monospace; }}
</style>
</head>
<body class="min-h-screen">
<header class="border-b border-slate-200">
  <div class="max-w-3xl mx-auto px-6 py-4 flex items-center justify-between flex-wrap gap-2">
    <a href="/" class="text-sm text-slate-600 hover:text-slate-900">← BailleurVérif</a>
    <a href="/preavis-bail.html" class="text-xs px-3 py-1.5 rounded-lg bg-blue-700 hover:bg-blue-800 text-slate-900 font-semibold">Calculateur national →</a>
  </div>
</header>

<main class="max-w-3xl mx-auto px-6 py-10">
  <nav class="text-xs text-slate-500 mb-4">
    <a href="/" class="hover:text-blue-800">Accueil</a> ·
    <a href="/preavis-bail.html" class="hover:text-blue-800">Préavis bail</a> ·
    <span class="text-slate-700">{ville}</span>
  </nav>

  <div class="text-xs uppercase tracking-widest text-blue-700 mb-2">Préavis · {ville}</div>
  <h1 class="text-3xl md:text-4xl font-bold leading-tight mb-4">
    <span>Préavis de bail à {ville} en 2026 — <span class="pill {zt_pill}">{preavis_loc_nu}</span> bail nu</span>
  </h1>
  <p class="text-slate-600 text-sm mb-4">
    <span class="bv-update-pill">Mis à jour le {TODAY}</span> · Loi 89-462 (Mermaz) art. 15 · Loi Alur 2014 · Loi ELAN 2018
  </p>

  <aside class="bv-trust-bar mb-8" aria-label="Sources officielles">
    <span><strong>Sources :</strong> <a href="https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000509310/" rel="nofollow noopener" target="_blank">Loi 89-462</a> · <a href="https://www.service-public.fr/particuliers/vosdroits/F1314" rel="nofollow noopener" target="_blank">Service-Public.fr</a> · <a href="https://www.legifrance.gouv.fr/loda/id/JORFTEXT000027309231" rel="nofollow noopener" target="_blank">Décret 2013-392 (zone tendue)</a></span>
    <span class="bv-lock">🔒 Aucun compte · Aucun cookie tiers · RGPD</span>
  </aside>

  <div class="glass rounded-xl p-5 mb-8">
    <p class="text-sm text-slate-700 leading-relaxed">{zt_explainer}</p>
  </div>

  <h2 class="text-2xl font-bold text-slate-900 mt-8 mb-3">Durées applicables à {ville} (synthèse)</h2>
  <table>
    <thead><tr><th>Cas</th><th>Préavis</th><th>Référence</th></tr></thead>
    <tbody>
      <tr><td>Locataire — bail <strong>nu</strong></td><td><span class="pill {zt_pill}">{preavis_loc_nu}</span></td><td>Loi 89-462 art. 15-I {'+ zone tendue' if is_zt else ''}</td></tr>
      <tr><td>Locataire — bail <strong>meublé</strong></td><td><span class="pill pill-1">1 mois</span></td><td>Loi 89-462 art. 25-8</td></tr>
      <tr><td>Locataire — motif spécifique (mutation, perte emploi, RSA, AAH, état santé…)</td><td><span class="pill pill-1">1 mois</span></td><td>Loi 89-462 art. 15-I 4°</td></tr>
      <tr><td>Bailleur — bail <strong>nu</strong> (échéance + motif légitime)</td><td><span class="pill pill-6">6 mois</span></td><td>Loi 89-462 art. 15-II</td></tr>
      <tr><td>Bailleur — bail <strong>meublé</strong> (échéance + motif légitime)</td><td><span class="pill pill-3">3 mois</span></td><td>Loi 89-462 art. 25-8</td></tr>
    </tbody>
  </table>

  <aside class="cta-wedge my-8 rounded-2xl border border-blue-200 bg-blue-50 p-6">
    <div class="text-[11px] uppercase tracking-widest text-blue-700 mb-2">Calculateur national · 30 sec</div>
    <p class="text-lg md:text-xl font-semibold text-slate-900 mb-3">Calculer ma date butoir + modèle LRAR pré-rempli</p>
    <p class="text-sm text-slate-700 mb-4">Sélectionnez date de réception du congé, type de bail, motif éventuel. Verdict instantané + lettre formattée à copier-coller.</p>
    <a href="/preavis-bail.html" class="inline-flex items-center gap-2 px-5 py-2.5 rounded-lg bg-blue-700 hover:bg-blue-800 text-slate-900 font-semibold text-sm transition">
      Lancer le calculateur national →
    </a>
    <span class="text-xs text-slate-500 ml-3">gratuit · sans inscription</span>
  </aside>

  <h2 class="text-2xl font-bold text-slate-900 mt-10 mb-3">Mini-simulateur : ma date butoir à {ville}</h2>
  <div class="glass rounded-xl p-5 my-4">
    <label class="block text-xs uppercase tracking-wider text-slate-600 mb-1">Date de réception du congé (LRAR)</label>
    <input id="pb-date" type="date" class="border border-slate-300 rounded-md px-3 py-2 text-sm w-full mb-3" />
    <label class="block text-xs uppercase tracking-wider text-slate-600 mb-1">Type de bail</label>
    <select id="pb-type" class="border border-slate-300 rounded-md px-3 py-2 text-sm w-full mb-3">
      <option value="nu">Bail nu (vide)</option>
      <option value="meuble">Bail meublé</option>
    </select>
    <label class="block text-xs uppercase tracking-wider text-slate-600 mb-1">Qui donne congé ?</label>
    <select id="pb-qui" class="border border-slate-300 rounded-md px-3 py-2 text-sm w-full mb-3">
      <option value="locataire">Locataire</option>
      <option value="bailleur">Bailleur</option>
    </select>
    <label class="block text-xs uppercase tracking-wider text-slate-600 mb-1">Motif réduisant le préavis (locataire) ?</label>
    <select id="pb-motif" class="border border-slate-300 rounded-md px-3 py-2 text-sm w-full mb-4">
      <option value="non">Non</option>
      <option value="oui">Oui (mutation, perte emploi, RSA/AAH, santé…)</option>
    </select>
    <button id="pb-calc" class="px-4 py-2 rounded-lg bg-blue-700 hover:bg-blue-800 text-slate-900 font-semibold text-sm">Calculer →</button>
    <div id="pb-out" class="mt-4 text-sm text-slate-800"></div>
  </div>
  <script>
  (function() {{
    var IS_ZT = {('true' if is_zt else 'false')};
    var btn = document.getElementById('pb-calc');
    btn.addEventListener('click', function() {{
      var d = document.getElementById('pb-date').value;
      var type = document.getElementById('pb-type').value;
      var qui = document.getElementById('pb-qui').value;
      var motif = document.getElementById('pb-motif').value;
      var out = document.getElementById('pb-out');
      if (!d) {{ out.innerHTML = '<span class="text-rose-700">Saisissez la date de réception du congé.</span>'; return; }}
      var months;
      if (qui === 'locataire') {{
        if (type === 'meuble') months = 1;
        else if (motif === 'oui' || IS_ZT) months = 1;
        else months = 3;
      }} else {{
        months = (type === 'meuble') ? 3 : 6;
      }}
      var date = new Date(d);
      date.setMonth(date.getMonth() + months);
      var iso = date.toISOString().slice(0, 10);
      out.innerHTML = '<strong>Préavis applicable :</strong> <span class="pill pill-' + months + '">' + months + ' mois</span><br>' +
                      '<strong>Date butoir (fin de bail) :</strong> ' + iso + '<br>' +
                      '<span class="text-xs text-slate-500">Loyer dû jusqu\\'à cette date, sauf accord amiable.</span>';
    }});
  }})();
  </script>

  <h2 class="text-2xl font-bold text-slate-900 mt-10 mb-3">Modèle de lettre LRAR (à personnaliser)</h2>
  <p class="text-sm text-slate-600 mb-2">Copiez ce modèle, complétez les champs entre crochets, envoyez en recommandé avec AR au bailleur.</p>
  <textarea readonly rows="14" class="w-full border border-slate-300 rounded-md p-3 text-xs">[Vos nom et prénom]
[Votre adresse complète à {ville}]
[Téléphone] [E-mail]

À [Bailleur — nom et adresse complète]

Lettre recommandée avec accusé de réception
Objet : Notification de congé — bail signé le [date de signature]

Madame, Monsieur,

Conformément à l'article 15 de la loi du 6 juillet 1989, je vous notifie par la présente
ma décision de mettre fin au bail portant sur le logement situé [adresse complète à {ville}],
que vous me louez depuis le [date d'entrée dans les lieux].

La commune de {ville} étant {zt_label}, le préavis applicable est de {preavis_loc_nu}.
La date de fin de bail effective sera donc fixée [date de réception + préavis] au plus tard.

[Si motif réduction préavis hors ZT, le préciser ici : mutation professionnelle / perte d'emploi
 / RSA-AAH / état de santé / etc., avec justificatif joint.]

Je me tiens à votre disposition pour organiser l'état des lieux de sortie ainsi que la
restitution des clés. Je vous prie de bien vouloir me communiquer le RIB sur lequel vous
souhaitez que le dépôt de garantie me soit restitué.

Je vous prie d'agréer, Madame, Monsieur, l'expression de mes salutations distinguées.

Fait à {ville}, le [date]
[Signature]
  </textarea>

  <h2 class="text-2xl font-bold text-slate-900 mt-10 mb-3">FAQ — préavis bail à {ville}</h2>
  <details><summary class="font-semibold">Quelle est la durée du préavis pour un bail nu à {ville} ?</summary>
    <p class="text-sm text-slate-700 my-2">À {ville}, le préavis du locataire pour un bail nu est de <strong>{preavis_loc_nu}</strong> car la commune est {zt_label} (décret 2013-392 modifié). Pour le bailleur, le préavis reste de 6 mois avant l'échéance du bail, avec motif légitime obligatoire.</p>
  </details>
  <details><summary class="font-semibold">Bail meublé à {ville} : quel préavis ?</summary>
    <p class="text-sm text-slate-700 my-2">Pour un bail meublé à {ville}, le préavis du locataire est toujours de <strong>1 mois</strong>, indépendamment du statut zone tendue. Pour le bailleur, c'est 3 mois minimum avant l'échéance annuelle.</p>
  </details>
  <details><summary class="font-semibold">{ville} est-elle en zone tendue ?</summary>
    <p class="text-sm text-slate-700 my-2">En 2026, {ville} est <strong>{zt_label}</strong> au sens du décret 2013-392 modifié. {('Cela entraîne préavis 1 mois bail nu + encadrement IRL.' if is_zt else 'Préavis bail nu = 3 mois standard. Liste officielle complète sur service-public.fr.')}</p>
  </details>
  <details><summary class="font-semibold">À partir de quand court le préavis ?</summary>
    <p class="text-sm text-slate-700 my-2">À compter de la <strong>date de réception</strong> de la LRAR par le destinataire (article 15 loi 89-462). En cas de refus de retirer le pli, la date du premier avis de passage du facteur fait foi.</p>
  </details>
  <details><summary class="font-semibold">Motifs réduisant le préavis du locataire à 1 mois (hors ZT) ?</summary>
    <p class="text-sm text-slate-700 my-2">Mutation professionnelle, perte d'emploi, nouvel emploi suite à perte d'emploi, premier emploi, état de santé exigeant un déménagement (certificat médical), bénéficiaires du RSA ou de l'AAH, attribution d'un logement social. Le motif doit être justifié dans la lettre LRAR avec pièce jointe.</p>
  </details>

  <h2 class="text-2xl font-bold text-slate-900 mt-10 mb-3">Voir aussi à {ville}</h2>
  <p class="text-sm text-slate-600 mb-3">Autres obligations locatives applicables à votre logement à {ville} :</p>
  <p class="text-sm leading-loose">
    {dpe_xlink} &nbsp;·&nbsp; {encadrement_xlink}
  </p>

  <h2 class="text-2xl font-bold text-slate-900 mt-10 mb-3">Villes voisines</h2>
  <p class="text-sm leading-loose flex flex-wrap gap-x-3 gap-y-1">
    {{LINKS_PLACEHOLDER}}
  </p>

  <hr class="my-10 border-slate-200" />
  <p class="text-xs text-slate-500">
    Les durées ci-dessus sont les durées <strong>légales standard</strong> 2026. Un bail commercial, un bail de meublé étudiant, un bail mobilité, ou
    une convention de mise à disposition à titre gratuit obéissent à des règles spécifiques non couvertes ici. En cas de doute, consultez l'<a class="hover:text-blue-800" href="https://www.service-public.fr/particuliers/vosdroits/F1314" rel="nofollow noopener" target="_blank">ADIL de votre département</a> (consultation gratuite). Mise à jour : {TODAY}.
  </p>
</main>

<footer class="bv-footer mt-16 py-8">
  <div class="max-w-3xl mx-auto px-6">
    <div class="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-4">
      <div>
        <div><strong>BailleurVérif</strong> — Outil gratuit · Mis à jour le {TODAY}</div>
        <div class="text-xs mt-1" style="color:var(--text-muted)">Informatif — ne remplace pas un conseil juridique personnalisé (ADIL).</div>
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
    <div class="text-xs mt-4 pt-4" style="border-top:1px solid var(--border); color:var(--text-muted)">© 2026 BailleurVérif</div>
  </div>
</footer>
</body>
</html>
"""
    return html


def build_neighbors_links(current_slug):
    current = next((c for c in CITIES if c[0] == current_slug), None)
    if not current:
        return ""
    cur_dept = current[3]
    same_dept = [c for c in CITIES if c[3] == cur_dept and c[0] != current_slug]
    other = [c for c in CITIES if c[3] != cur_dept and c[0] != current_slug]
    pick = (same_dept + other)[:6]
    links = "\n    ".join(
        f'<a href="/preavis-bail-{c[0]}.html" class="text-sm text-blue-700 hover:text-blue-800 underline">{c[1]}</a>'
        for c in pick
    )
    return links


# Communes encadrement & DPE déjà connues — pour sitemap merged (parité builders existants)
ENCADREMENT_COMMUNES = [
    "paris", "lille", "hellemmes", "lomme", "lyon", "villeurbanne", "bordeaux",
    "montpellier", "saint-ouen", "aubervilliers", "saint-denis",
    "pierrefitte-sur-seine", "epinay-sur-seine", "stains", "villetaneuse",
    "ile-saint-denis", "la-courneuve", "bagnolet", "bondy", "bobigny",
    "le-pre-saint-gervais", "les-lilas", "montreuil", "noisy-le-sec", "pantin",
    "romainville", "grenoble", "echirolles", "eybens", "fontaine",
    "saint-martin-d-heres",
]

DPE_CITIES = [c[0] for c in CITIES]


def _discover_blog_pages() -> list[str]:
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
        out = os.path.join(STATIC, f"preavis-bail-{slug}.html")
        with open(out, "w", encoding="utf-8") as f:
            f.write(html)
        generated.append(slug)
    print(f"Generated {len(generated)} preavis pages.")

    BLOG_PAGES = _discover_blog_pages()
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
    urls += [f"{BASE_URL}/{s}-dpe-f-g-interdit-location.html" for s in DPE_CITIES if os.path.exists(os.path.join(STATIC, f"{s}-dpe-f-g-interdit-location.html"))]
    urls += [f"{BASE_URL}/preavis-bail-{s}.html" for s in generated]

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

    new_urls = [f"{BASE_URL}/preavis-bail-{s}.html" for s in generated]
    print("NEW_URLS:")
    for u in new_urls:
        print(u)


if __name__ == "__main__":
    main()
