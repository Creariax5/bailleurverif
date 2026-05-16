#!/usr/bin/env python3
"""
build_programmatic_pages.py — Generates one SEO landing page per encadrement-loyer commune.

Output: 31 HTML files in wedge-tool/static/ named `encadrement-loyer-{slug}-2026.html`.
Each page is SEO-optimized for the longtail query "encadrement loyer {ville} 2026" with:
- unique meta title/description
- canonical URL
- JSON-LD WebPage + Dataset + BreadcrumbList
- mini-calculator (client JS, no inscription)
- CTA towards wedge tool main page
- official preficture references

Also rebuilds sitemap.xml to include the new URLs.
Run from saas-florian root: python3 dashboard/build_programmatic_pages.py
"""
import os
import json
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC = os.path.join(ROOT, "wedge-tool", "static")
TODAY = date.today().isoformat()

# (slug, ville_affichage, ref_nu, ref_meuble, scope, depuis, prefecture, intercommunalite)
COMMUNES = [
    ("paris", "Paris", 33.3, 40.0, "20 arrondissements", "1er juillet 2019", "Préfecture de Paris (DRIHL)", "Paris intra-muros"),
    ("lille", "Lille", 19.5, 23.4, "Lille + Hellemmes + Lomme", "1er mars 2020", "Préfecture du Nord (DDETS)", "Métropole Européenne de Lille (MEL)"),
    ("hellemmes", "Hellemmes", 19.5, 23.4, "commune associée à Lille", "1er mars 2020", "Préfecture du Nord (DDETS)", "Métropole Européenne de Lille (MEL)"),
    ("lomme", "Lomme", 19.5, 23.4, "commune associée à Lille", "1er mars 2020", "Préfecture du Nord (DDETS)", "Métropole Européenne de Lille (MEL)"),
    ("lyon", "Lyon", 16.8, 20.2, "9 arrondissements lyonnais", "1er novembre 2021", "Préfecture du Rhône (DDETS)", "Métropole de Lyon"),
    ("villeurbanne", "Villeurbanne", 16.5, 19.8, "ensemble du territoire communal", "1er novembre 2021", "Préfecture du Rhône (DDETS)", "Métropole de Lyon"),
    ("bordeaux", "Bordeaux", 17.4, 20.9, "ensemble de la commune", "15 juillet 2022", "Préfecture de la Gironde (DDTM)", "Bordeaux Métropole"),
    ("montpellier", "Montpellier", 17.0, 20.4, "ensemble de la commune", "1er juillet 2022", "Préfecture de l'Hérault (DDTM)", "Montpellier Méditerranée Métropole (3M)"),
    ("saint-ouen", "Saint-Ouen-sur-Seine", 25.2, 30.2, "ensemble du territoire", "1er juin 2021", "Préfecture de Seine-Saint-Denis (DDETS 93)", "EPT Plaine Commune"),
    ("aubervilliers", "Aubervilliers", 23.4, 28.1, "ensemble du territoire", "1er juin 2021", "Préfecture de Seine-Saint-Denis (DDETS 93)", "EPT Plaine Commune"),
    ("saint-denis", "Saint-Denis", 23.4, 28.1, "ensemble du territoire", "1er juin 2021", "Préfecture de Seine-Saint-Denis (DDETS 93)", "EPT Plaine Commune"),
    ("pierrefitte-sur-seine", "Pierrefitte-sur-Seine", 22.1, 26.5, "ensemble du territoire", "1er juin 2021", "Préfecture de Seine-Saint-Denis (DDETS 93)", "EPT Plaine Commune"),
    ("epinay-sur-seine", "Épinay-sur-Seine", 22.1, 26.5, "ensemble du territoire", "1er juin 2021", "Préfecture de Seine-Saint-Denis (DDETS 93)", "EPT Plaine Commune"),
    ("stains", "Stains", 22.1, 26.5, "ensemble du territoire", "1er juin 2021", "Préfecture de Seine-Saint-Denis (DDETS 93)", "EPT Plaine Commune"),
    ("villetaneuse", "Villetaneuse", 22.1, 26.5, "ensemble du territoire", "1er juin 2021", "Préfecture de Seine-Saint-Denis (DDETS 93)", "EPT Plaine Commune"),
    ("ile-saint-denis", "L'Île-Saint-Denis", 23.4, 28.1, "ensemble du territoire", "1er juin 2021", "Préfecture de Seine-Saint-Denis (DDETS 93)", "EPT Plaine Commune"),
    ("la-courneuve", "La Courneuve", 22.1, 26.5, "ensemble du territoire", "1er juin 2021", "Préfecture de Seine-Saint-Denis (DDETS 93)", "EPT Plaine Commune"),
    ("bagnolet", "Bagnolet", 24.0, 28.8, "ensemble du territoire", "1er décembre 2021", "Préfecture de Seine-Saint-Denis (DDETS 93)", "EPT Est Ensemble"),
    ("bondy", "Bondy", 22.5, 27.0, "ensemble du territoire", "1er décembre 2021", "Préfecture de Seine-Saint-Denis (DDETS 93)", "EPT Est Ensemble"),
    ("bobigny", "Bobigny", 22.5, 27.0, "ensemble du territoire", "1er décembre 2021", "Préfecture de Seine-Saint-Denis (DDETS 93)", "EPT Est Ensemble"),
    ("le-pre-saint-gervais", "Le Pré-Saint-Gervais", 24.0, 28.8, "ensemble du territoire", "1er décembre 2021", "Préfecture de Seine-Saint-Denis (DDETS 93)", "EPT Est Ensemble"),
    ("les-lilas", "Les Lilas", 24.0, 28.8, "ensemble du territoire", "1er décembre 2021", "Préfecture de Seine-Saint-Denis (DDETS 93)", "EPT Est Ensemble"),
    ("montreuil", "Montreuil", 24.0, 28.8, "ensemble du territoire", "1er décembre 2021", "Préfecture de Seine-Saint-Denis (DDETS 93)", "EPT Est Ensemble"),
    ("noisy-le-sec", "Noisy-le-Sec", 22.5, 27.0, "ensemble du territoire", "1er décembre 2021", "Préfecture de Seine-Saint-Denis (DDETS 93)", "EPT Est Ensemble"),
    ("pantin", "Pantin", 24.0, 28.8, "ensemble du territoire", "1er décembre 2021", "Préfecture de Seine-Saint-Denis (DDETS 93)", "EPT Est Ensemble"),
    ("romainville", "Romainville", 23.0, 27.6, "ensemble du territoire", "1er décembre 2021", "Préfecture de Seine-Saint-Denis (DDETS 93)", "EPT Est Ensemble"),
    ("grenoble", "Grenoble", 14.5, 17.4, "ensemble de la commune", "1er septembre 2023", "Préfecture de l'Isère (DDETS)", "Grenoble-Alpes Métropole"),
    ("echirolles", "Échirolles", 13.5, 16.2, "secteurs OLAP", "1er septembre 2023", "Préfecture de l'Isère (DDETS)", "Grenoble-Alpes Métropole"),
    ("eybens", "Eybens", 13.5, 16.2, "secteurs OLAP", "1er septembre 2023", "Préfecture de l'Isère (DDETS)", "Grenoble-Alpes Métropole"),
    ("fontaine", "Fontaine", 13.5, 16.2, "secteurs OLAP", "1er septembre 2023", "Préfecture de l'Isère (DDETS)", "Grenoble-Alpes Métropole"),
    ("saint-martin-d-heres", "Saint-Martin-d'Hères", 13.5, 16.2, "secteurs OLAP", "1er septembre 2023", "Préfecture de l'Isère (DDETS)", "Grenoble-Alpes Métropole"),
]

BASE_URL = "https://bailleurverif.fr"


def render_page(slug, ville, ref_nu, ref_meuble, scope, depuis, prefecture, intercommunalite):
    title = f"Encadrement loyer {ville} 2026 — Plafond légal {ref_nu}€/m² (nu) · {ref_meuble}€/m² (meublé) | BailleurVérif"
    description = (
        f"Loyer plafond à {ville} en 2026 : {ref_nu}€/m² (nu) et {ref_meuble}€/m² (meublé). "
        f"Encadrement légal depuis le {depuis}. Vérification gratuite en 30 secondes, sans inscription."
    )
    canonical = f"{BASE_URL}/encadrement-loyer-{slug}-2026.html"

    # JSON-LD : WebPage + Dataset + BreadcrumbList + Organization
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
                    {"@type": "ListItem", "position": 2, "name": "Encadrement des loyers"},
                    {"@type": "ListItem", "position": 3, "name": ville, "item": canonical},
                ],
            },
            {
                "@type": "Dataset",
                "@id": f"{canonical}#dataset",
                "name": f"Loyers de référence encadrés à {ville} (2026)",
                "description": (
                    f"Loyers de référence majorés à {ville} pour l'année 2026 : "
                    f"plafond légal nu {ref_nu}€/m²/mois et plafond légal meublé {ref_meuble}€/m²/mois "
                    f"hors charges, applicable à toute nouvelle location ou renouvellement. "
                    f"Source : arrêté préfectoral, {prefecture}."
                ),
                "url": canonical,
                "inLanguage": "fr-FR",
                "creator": {"@id": f"{BASE_URL}/#organization"},
                "license": "https://www.etalab.gouv.fr/licence-ouverte-open-licence",
                "isAccessibleForFree": True,
                "keywords": [
                    f"encadrement loyer {ville.lower()}",
                    f"plafond loyer {ville.lower()}",
                    "loyer référence majoré",
                    "loi ELAN",
                    "zone tendue",
                ],
                "variableMeasured": [
                    {
                        "@type": "PropertyValue",
                        "name": "Loyer de référence majoré (nu)",
                        "value": ref_nu,
                        "unitText": "EUR par mètre carré par mois",
                    },
                    {
                        "@type": "PropertyValue",
                        "name": "Loyer de référence majoré (meublé)",
                        "value": ref_meuble,
                        "unitText": "EUR par mètre carré par mois",
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

    # exemples de calcul (T1 25m², T2 40m², T3 60m²)
    ex_t1_nu = round(ref_nu * 25)
    ex_t2_nu = round(ref_nu * 40)
    ex_t3_nu = round(ref_nu * 60)
    ex_t2_meuble = round(ref_meuble * 40)

    html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title}</title>
<meta name="description" content="{description}" />
<link rel="canonical" href="{canonical}" />
<meta property="og:title" content="Encadrement loyer {ville} 2026 — plafond légal {ref_nu}€/m²" />
<meta property="og:description" content="{description}" />
<meta property="og:type" content="article" />
<meta property="og:url" content="{canonical}" />
<meta property="og:site_name" content="BailleurVérif" />
<meta property="og:locale" content="fr_FR" />
<meta name="twitter:card" content="summary" />
<meta name="twitter:title" content="Encadrement loyer {ville} 2026 — plafond {ref_nu}€/m²" />
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
    <span>Encadrement des loyers</span> ·
    <span class="text-slate-700">{ville}</span>
  </nav>

  <div class="text-xs uppercase tracking-widest text-blue-700 mb-2">Encadrement des loyers · {ville}</div>
  <h1 class="text-3xl md:text-4xl font-bold leading-tight mb-4">
    <span>Encadrement des loyers à {ville} en 2026 — plafond légal et calcul</span>
  </h1>
  <p class="text-slate-600 text-sm mb-4"><span class="bv-update-pill">Mis à jour le {TODAY}</span> · Source officielle : {prefecture}</p>

  <aside class="bv-trust-bar mb-8" aria-label="Sources officielles">
    <span><strong>Sources :</strong> Arrêté préfectoral 2026 · <a href="https://www.legifrance.gouv.fr" target="_blank" rel="noopener">Légifrance</a> (loi ELAN, loi 89-462) · <a href="https://www.service-public.fr" target="_blank" rel="noopener">Service-Public.fr</a></span>
    <span class="bv-lock">🔒 Aucun compte · Aucun cookie tiers · RGPD</span>
  </aside>

  <div class="glass rounded-xl p-5 mb-8">
    <p class="text-sm text-slate-600 mb-1">Plafond légal à <strong class="text-slate-900">{ville}</strong> en 2026</p>
    <div class="grid grid-cols-2 gap-4 mt-3">
      <div>
        <div class="text-xs uppercase tracking-wider text-slate-500">Location nue</div>
        <div class="text-2xl font-bold text-slate-900">{ref_nu} €/m²/mois</div>
        <div class="text-xs text-slate-500">loyer de référence majoré (+20%)</div>
      </div>
      <div>
        <div class="text-xs uppercase tracking-wider text-slate-500">Location meublée</div>
        <div class="text-2xl font-bold text-slate-900">{ref_meuble} €/m²/mois</div>
        <div class="text-xs text-slate-500">loyer de référence majoré (+20%)</div>
      </div>
    </div>
  </div>

  <p class="text-slate-700 leading-relaxed my-4">
    Si vous louez un logement à <strong class="text-slate-900">{ville}</strong>, votre loyer est soumis à l'<strong class="text-slate-900">encadrement légal des loyers</strong>
    depuis le {depuis}. Le périmètre couvre <strong class="text-slate-900">{scope}</strong>, dans le cadre de l'expérimentation prévue par la loi ELAN du 23 novembre 2018
    (prolongée jusqu'au 23 novembre 2026 par la loi du 27 juillet 2023). L'autorité de contrôle est la <strong class="text-slate-900">{prefecture}</strong>.
  </p>

  <p class="text-slate-700 leading-relaxed my-4">
    Le plafond légal applicable à {ville} en 2026 est de <strong class="text-slate-900">{ref_nu} €/m²/mois pour une location nue</strong>,
    et <strong class="text-slate-900">{ref_meuble} €/m²/mois pour une location meublée</strong>, hors charges. Ces valeurs correspondent au
    <em>loyer de référence majoré</em> tel que défini par l'arrêté préfectoral en vigueur. Tout dépassement, sauf complément de loyer
    justifié et formalisé dans le bail, expose le bailleur à une <strong class="text-slate-900">amende administrative de 5 000 €</strong> (15 000 €
    pour une SCI) cumulable avec la restitution du trop-perçu.
  </p>

  <aside class="cta-wedge my-8 rounded-2xl border border-blue-200 bg-blue-50 p-6">
    <div class="text-[11px] uppercase tracking-widest text-blue-700 mb-2">Outil gratuit · 30 sec</div>
    <p class="text-lg md:text-xl font-semibold text-slate-900 mb-3">Vérifiez votre loyer à {ville} en 30 secondes</p>
    <p class="text-sm text-slate-700 mb-4">5 questions, verdict immédiat : ✅ conforme · ⚠️ risque amende · 🚫 interdiction. Aucune création de compte.</p>
    <a href="/" class="inline-flex items-center gap-2 px-5 py-2.5 rounded-lg bg-blue-700 hover:bg-blue-800 text-slate-900 font-semibold text-sm transition">
      Vérifier mon loyer à {ville} →
    </a>
    <span class="text-xs text-slate-500 ml-3">gratuit · sans inscription</span>
  </aside>

  <h2 class="text-2xl font-bold text-slate-900 mt-10 mb-3 leading-tight">Calcul rapide pour {ville}</h2>
  <p class="text-slate-700 leading-relaxed my-4">
    Le plafond varie en fonction de la surface du logement. Voici trois ordres de grandeur :
  </p>
  <table>
    <thead>
      <tr><th>Typologie</th><th>Surface</th><th>Plafond légal (nu)</th></tr>
    </thead>
    <tbody>
      <tr><td>Studio / T1</td><td>25 m²</td><td><strong class="text-slate-900">{ex_t1_nu} €</strong> hors charges</td></tr>
      <tr><td>T2</td><td>40 m²</td><td><strong class="text-slate-900">{ex_t2_nu} €</strong> hors charges (meublé : {ex_t2_meuble} €)</td></tr>
      <tr><td>T3</td><td>60 m²</td><td><strong class="text-slate-900">{ex_t3_nu} €</strong> hors charges</td></tr>
    </tbody>
  </table>
  <p class="text-xs text-slate-500 my-2">Ces valeurs sont indicatives et basées sur le loyer de référence majoré global pour {ville}.
    Le plafond exact dépend du <strong class="text-slate-600">secteur géographique précis</strong>, du <strong class="text-slate-600">nombre de pièces</strong>,
    de <strong class="text-slate-600">l'époque de construction</strong> et du <strong class="text-slate-600">type de location</strong>. Utilisez le simulateur officiel
    de la {prefecture} ou notre outil de vérification gratuit pour le calcul personnalisé.</p>

  <h2 class="text-2xl font-bold text-slate-900 mt-10 mb-3 leading-tight">Simulateur intégré — votre loyer est-il conforme ?</h2>
  <div class="glass rounded-xl p-5 my-4">
    <label class="block text-xs uppercase tracking-wider text-slate-600 mb-1">Surface habitable (m²)</label>
    <input id="pp-surface" type="number" min="5" max="500" placeholder="ex : 35"
           class="w-full bg-white border border-slate-300 rounded-lg px-3 py-2 text-slate-900 mb-3" />
    <label class="block text-xs uppercase tracking-wider text-slate-600 mb-1">Loyer hors charges (€/mois)</label>
    <input id="pp-loyer" type="number" min="100" max="20000" placeholder="ex : 850"
           class="w-full bg-white border border-slate-300 rounded-lg px-3 py-2 text-slate-900 mb-3" />
    <label class="block text-xs uppercase tracking-wider text-slate-600 mb-1">Type de location</label>
    <div class="flex gap-2 mb-3">
      <button onclick="ppSetType('nu')" id="pp-nu"
              class="flex-1 px-3 py-2 rounded-lg border border-slate-300 hover:border-blue-700 text-slate-900 text-sm">Nu</button>
      <button onclick="ppSetType('meuble')" id="pp-meuble"
              class="flex-1 px-3 py-2 rounded-lg border border-slate-300 hover:border-blue-700 text-slate-900 text-sm">Meublé</button>
    </div>
    <button onclick="ppCheck()" class="w-full bg-blue-700 hover:bg-blue-800 text-slate-900 font-semibold py-2.5 rounded-lg">
      Vérifier le plafond
    </button>
    <div id="pp-result" class="mt-4"></div>
  </div>

  <script>
    const PP = {{ ville: "{ville}", ref_nu: {ref_nu}, ref_meuble: {ref_meuble}, type: null }};
    function ppSetType(t) {{
      PP.type = t;
      document.getElementById("pp-nu").classList.toggle("border-blue-700", t==="nu");
      document.getElementById("pp-meuble").classList.toggle("border-blue-700", t==="meuble");
    }}
    function ppCheck() {{
      const s = parseFloat(document.getElementById("pp-surface").value);
      const l = parseFloat(document.getElementById("pp-loyer").value);
      const r = document.getElementById("pp-result");
      if (!s || !l || !PP.type) {{ r.innerHTML = '<div class="text-amber-700 text-sm">Remplissez surface, loyer et type.</div>'; return; }}
      const ref = PP.type === "nu" ? PP.ref_nu : PP.ref_meuble;
      const plafond = ref * s;
      const m2 = l / s;
      let verdict, color;
      if (m2 <= ref * 0.95) {{ verdict = "✅ Conforme — votre loyer respecte le plafond légal."; color = "text-emerald-700"; }}
      else if (m2 <= ref * 1.05) {{ verdict = "⚠️ Limite — vous êtes proche du plafond, marge faible en cas de complément contesté."; color = "text-amber-700"; }}
      else {{ verdict = "🚫 Dépassement — risque d'amende préfectorale et restitution du trop-perçu."; color = "text-rose-700"; }}
      r.innerHTML = `
        <div class="${{color}} font-semibold mb-2">${{verdict}}</div>
        <div class="text-sm text-slate-600">
          Plafond légal estimé : <strong class="text-slate-900">${{plafond.toFixed(0)}} € hors charges</strong> (${{ref}} €/m² × ${{s}} m²).
          <br/>Votre loyer au m² : <strong class="text-slate-900">${{m2.toFixed(2)}} €/m²/mois</strong>.
        </div>
        <a href="/" class="inline-block mt-3 text-blue-700 hover:text-blue-800 text-sm font-semibold">
          → Diagnostic complet (DPE + encadrement + fraude dossier) sur BailleurVérif
        </a>`;
    }}
  </script>

  <h2 class="text-2xl font-bold text-slate-900 mt-10 mb-3 leading-tight">Cadre légal applicable à {ville}</h2>
  <ul class="list-disc pl-6 text-slate-700 leading-relaxed my-3 space-y-1">
    <li><strong class="text-slate-900">Loi ELAN</strong> du 23 novembre 2018, article 140, créant le cadre expérimental.</li>
    <li><strong class="text-slate-900">Loi 89-462</strong> du 6 juillet 1989, articles 17 et 17-2, fixant les règles d'encadrement.</li>
    <li><strong class="text-slate-900">Loi 3DS</strong> du 21 février 2022, instituant l'amende administrative préfectorale (5 000 € / 15 000 €).</li>
    <li><strong class="text-slate-900">Loi du 27 juillet 2023</strong>, prolongeant l'expérimentation jusqu'au 23 novembre 2026.</li>
    <li><strong class="text-slate-900">Arrêté préfectoral 2025</strong> ({prefecture}), fixant les valeurs de référence pour l'année en cours.</li>
  </ul>

  <h2 class="text-2xl font-bold text-slate-900 mt-10 mb-3 leading-tight">Que faire si votre loyer dépasse le plafond à {ville} ?</h2>
  <p class="text-slate-700 leading-relaxed my-4">
    Si le diagnostic ci-dessus indique un dépassement, plusieurs options s'offrent à vous selon votre situation :
  </p>
  <ol class="list-decimal pl-6 text-slate-700 leading-relaxed my-3 space-y-1">
    <li><strong class="text-slate-900">Bail en cours</strong> : régularisez à l'amiable en envoyant un avenant au locataire ramenant le loyer au plafond, avec restitution
      éventuelle des sommes versées en trop. La prescription civile permet au locataire de réclamer jusqu'à 3 ans en arrière.</li>
    <li><strong class="text-slate-900">Renouvellement</strong> (article 17-2 loi 89-462) : si le loyer en cours est sous le loyer de référence minoré, vous pouvez proposer
      une réévaluation, mais uniquement dans la limite du loyer de référence (pas le majoré) et avec un préavis de 6 mois formalisé.</li>
    <li><strong class="text-slate-900">Nouvelle mise en location</strong> : fixez le loyer initial dans la fourchette légale ; si vous souhaitez appliquer un complément
      de loyer, mentionnez-le explicitement dans le bail avec justification écrite (article 4 du décret du 10 juin 2015).</li>
  </ol>

  <p class="text-slate-700 leading-relaxed my-4">
    L'<strong class="text-slate-900">absence de mention du loyer de référence dans le bail</strong> est en elle-même une cause de nullité de la clause loyer
    et peut entraîner le retour au loyer de référence par défaut. Ne signez jamais un bail à {ville} sans y inscrire les trois valeurs (minoré / référence / majoré).
  </p>

  <h2 class="text-2xl font-bold text-slate-900 mt-10 mb-3 leading-tight">Communes voisines de {ville}</h2>
  <p class="text-slate-700 leading-relaxed my-4">
    Pour aller plus loin, consultez aussi les communes voisines sous encadrement :
  </p>
  <div class="grid grid-cols-2 md:grid-cols-3 gap-2 my-3">
    {{LINKS_PLACEHOLDER}}
  </div>

  <aside class="cta-wedge my-8 rounded-2xl border border-blue-200 bg-blue-50 p-6">
    <div class="text-[11px] uppercase tracking-widest text-blue-700 mb-2">Diagnostic complet · gratuit</div>
    <p class="text-lg md:text-xl font-semibold text-slate-900 mb-3">Au-delà du plafond, vérifiez aussi DPE + dossier locataire</p>
    <p class="text-sm text-slate-700 mb-4">BailleurVérif : 5 questions, verdict 3 niveaux, sans inscription. Couvre les 3 risques bailleurs de 2026 : DPE F (interdiction 2028), encadrement loyer, fraude dossier locataire.</p>
    <a href="/" class="inline-flex items-center gap-2 px-5 py-2.5 rounded-lg bg-blue-700 hover:bg-blue-800 text-slate-900 font-semibold text-sm transition">
      Lancer le diagnostic complet →
    </a>
  </aside>

  <hr class="my-10 border-slate-200" />
  <p class="text-xs text-slate-500">
    Cette page est mise à jour à chaque publication d'un nouvel arrêté préfectoral. Les valeurs présentées
    sont indicatives ; consultez systématiquement le simulateur officiel de la {prefecture} pour le calcul exact applicable à votre logement.
    Mise à jour : {TODAY}.
  </p>
</main>

<footer class="bv-footer mt-16 py-8">
  <div class="max-w-3xl mx-auto px-6">
    <div class="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-4">
      <div>
        <div><strong>BailleurVérif</strong> — Outil gratuit · Mis à jour le {TODAY}</div>
        <div class="text-xs mt-1" style="color:var(--text-muted)">Informatif — ne remplace pas un conseil juridique. Source : {prefecture}.</div>
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
    <div class="text-xs mt-4 pt-4" style="border-top:1px solid var(--border); color:var(--text-muted)">© 2026 BailleurVérif · Données réglementaires 2026</div>
  </div>
</footer>
</body>
</html>
"""
    return html


def build_neighbors_links(current_slug):
    """Pick up to 6 'neighbor' communes by sharing the same intercommunalite."""
    current = next((c for c in COMMUNES if c[0] == current_slug), None)
    if not current:
        return ""
    same_inter = [c for c in COMMUNES if c[7] == current[7] and c[0] != current_slug]
    if len(same_inter) < 3:
        # fall back to random other communes
        same_inter = [c for c in COMMUNES if c[0] != current_slug]
    pick = same_inter[:6]
    links = "\n    ".join(
        f'<a href="/encadrement-loyer-{c[0]}-2026.html" class="text-sm text-blue-700 hover:text-blue-800 underline">{c[1]}</a>'
        for c in pick
    )
    return links


def main():
    os.makedirs(STATIC, exist_ok=True)
    generated = []
    for c in COMMUNES:
        slug = c[0]
        html = render_page(*c)
        html = html.replace("{LINKS_PLACEHOLDER}", build_neighbors_links(slug))
        out = os.path.join(STATIC, f"encadrement-loyer-{slug}-2026.html")
        with open(out, "w", encoding="utf-8") as f:
            f.write(html)
        generated.append(slug)
    print(f"Generated {len(generated)} pages.")

    # rebuild sitemap.xml — scan dynamique des articles blog (idempotence run-99)
    blog_dir = os.path.join(STATIC, "blog")
    if os.path.isdir(blog_dir):
        blog_pages = sorted({
            f[:-5] for f in os.listdir(blog_dir)
            if f.endswith(".html") and f != "index.html"
        })
    else:
        blog_pages = []
    tools_pages = [
        p for p in (
            "preavis-bail.html",
            "widget-bailleurverif.html",
            "locataire-loyer-legal.html",
        )
        if os.path.exists(os.path.join(STATIC, p))
    ]
    urls = [f"{BASE_URL}/"]
    urls += [f"{BASE_URL}/{p}" for p in tools_pages]
    urls.append(f"{BASE_URL}/blog/")
    urls += [f"{BASE_URL}/blog/{p}.html" for p in blog_pages]
    urls += [f"{BASE_URL}/encadrement-loyer-{c[0]}-2026.html" for c in COMMUNES]

    # Idempotence : merge with existing DPE pages from /static/ (run-98) so this
    # builder no longer wipes them when re-run standalone.
    dpe_slugs = sorted({
        f.replace("-dpe-f-g-interdit-location.html", "")
        for f in os.listdir(STATIC)
        if f.endswith("-dpe-f-g-interdit-location.html")
    })
    urls += [f"{BASE_URL}/{s}-dpe-f-g-interdit-location.html" for s in dpe_slugs]

    # Idempotence : legal pages added run-100 — must also survive rebuilds.
    legal_pages = [
        p for p in ("mentions-legales.html", "politique-confidentialite.html", "cgu.html")
        if os.path.exists(os.path.join(STATIC, p))
    ]
    urls += [f"{BASE_URL}/{p}" for p in legal_pages]

    # Idempotence : open-data assets added run-118 — CC-BY-4.0 release.
    # run-119 : also include the /data/ hub page (schema.org/Dataset markup
    # for Google Dataset Search).
    data_dir = os.path.join(STATIC, "data")
    if os.path.isdir(data_dir):
        data_files = sorted(
            f for f in os.listdir(data_dir)
            if f.endswith((".csv", ".json", ".md", ".html", ".xml", ".cff"))
            and f != "index.html"
        )
        urls += [f"{BASE_URL}/data/{f}" for f in data_files]
        if os.path.exists(os.path.join(data_dir, "index.html")):
            urls.append(f"{BASE_URL}/data/")

    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for u in urls:
        sitemap += f"  <url><loc>{u}</loc><lastmod>{TODAY}</lastmod></url>\n"
    sitemap += "</urlset>\n"
    with open(os.path.join(STATIC, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap)
    print(f"Sitemap rebuilt with {len(urls)} URLs.")

    # output list of new urls for IndexNow
    new_urls = [f"{BASE_URL}/encadrement-loyer-{c[0]}-2026.html" for c in COMMUNES]
    print("NEW_URLS:")
    for u in new_urls:
        print(u)


if __name__ == "__main__":
    main()
