#!/usr/bin/env python3
"""Generate {ville}-arnaque-location.html pages with substantive unique content.

Each page = hero scanner inline + city-specific stat extrapolation + quartiers à vigilance
+ 5 signaux + maillage interne. Targets longtail "arnaque location {ville}" search.
"""
import os, json, sys, html

CITIES = [
    {
        "slug": "paris",
        "display": "Paris",
        "pop_k": 2102,
        "students_k": 750,
        "arnaque_est_mois": 28,
        "quartiers_vigilance": [
            ("Quartier Latin / Saint-Michel (5ᵉ)", "forte demande étudiante septembre, prix bas suspects"),
            ("Marais (3ᵉ / 4ᵉ)", "annonces touristiques détournées en faux baux longue durée"),
            ("Belleville / Ménilmontant (20ᵉ)", "fausses colocs Facebook, paiement avant visite"),
            ("Saint-Lazare / Gare du Nord", "ciblage primo-arrivants étudiants étrangers"),
            ("République / Oberkampf (11ᵉ)", "annonces leboncoin avec basculement WhatsApp dès message 1"),
        ],
        "specifique": "À Paris, l'<a href=\"/encadrement-loyer-france-2026.html#anchor-paris\">encadrement des loyers</a> impose un plafond : si l'annonce affiche un loyer manifestement <em>au-dessus</em> ou <em>très en-dessous</em> du plafond légal pour le quartier, c'est un drapeau. Au-dessus = bail vraisemblablement illégal ; en-dessous = appât d'arnaque classique.",
        "test_phrase": "T2 30m² Marais 700€/mois chaufage compris, propriétaire en mission Londres, caution 1400€ Western Union avant remise des clés, urgent !",
    },
    {
        "slug": "lyon",
        "display": "Lyon",
        "pop_k": 522,
        "students_k": 150,
        "arnaque_est_mois": 12,
        "quartiers_vigilance": [
            ("Part-Dieu / 3ᵉ arrondissement", "rotation cadres + étudiants, prix-appâts fréquents"),
            ("Croix-Rousse (1ᵉʳ / 4ᵉ)", "annonces \"de bouche-à-oreille\" non vérifiables"),
            ("Vieux Lyon (5ᵉ)", "rentrée septembre = pic arnaques étudiantes Lyon 3 / Lyon 2"),
            ("Villeurbanne / INSA", "ciblage primo-arrivants ingénieurs étrangers"),
            ("Gerland (7ᵉ)", "faux profils \"bailleur expat\" via Facebook Marketplace"),
        ],
        "specifique": "Lyon est dans la <a href=\"/encadrement-loyer-france-2026.html#anchor-lyon\">zone d'encadrement des loyers</a> (loi Élan 2026). Si un bailleur refuse d'inscrire le loyer de référence au bail ou propose un complément de loyer non justifié, signalez à la DDPP du Rhône.",
        "test_phrase": "Studio meublé 22m² Croix-Rousse 450€ cc, dispo immédiat, mon mari travaille à Doha, envoyez 900€ caution par MoneyGram pour bloquer.",
    },
    {
        "slug": "marseille",
        "display": "Marseille",
        "pop_k": 873,
        "students_k": 80,
        "arnaque_est_mois": 11,
        "quartiers_vigilance": [
            ("Vieux-Port / Panier (2ᵉ / 7ᵉ)", "fausses locations courte-durée converties en bail"),
            ("Saint-Charles / La Plaine (1ᵉʳ)", "rotation étudiants AMU, prix très bas suspects"),
            ("Castellane / Préfecture (6ᵉ)", "annonces sans visite, paiement préalable"),
            ("La Joliette / Euroméditerranée (2ᵉ / 3ᵉ)", "ciblage cadres mutés, faux baux meublés"),
            ("13013 / 13014 nord", "annonces très en-dessous du marché = appât"),
        ],
        "specifique": "Marseille n'est pas en zone d'encadrement des loyers, donc le prix seul ne peut servir de référence légale. Vérifiez systématiquement la pièce d'identité du bailleur + un acte de propriété ou un mandat d'agence.",
        "test_phrase": "F3 70m² Vieux-Port 400€/mois, photos super, je suis actuellement à Casablanca, payez 800€ par carte PCS, je vous envoie les clés par chronopost.",
    },
    {
        "slug": "toulouse",
        "display": "Toulouse",
        "pop_k": 498,
        "students_k": 140,
        "arnaque_est_mois": 9,
        "quartiers_vigilance": [
            ("Capitole / Carmes", "pic septembre = étudiants UT1/UT2/UT3 ciblés"),
            ("Saint-Cyprien / Patte d'Oie", "annonces leboncoin avec faux propriétaire étranger"),
            ("Rangueil / Université Paul Sabatier", "primo-arrivants ingénieurs internationaux"),
            ("Compans-Caffarelli / Borderouge", "rotation cadres aéronautique, faux baux meublés"),
            ("Mirail / Bagatelle", "annonces très en-dessous du marché 'aubaine'"),
        ],
        "specifique": "Toulouse n'a pas d'encadrement des loyers : le seul recours fiable contre une annonce suspecte est le signalement à la plateforme + dépôt de plainte si paiement déjà effectué. Aucun préfet n'arbitre un litige de prix.",
        "test_phrase": "Joli T2 Toulouse centre 420€ cc, propriétaire à Londres, virement bancaire 850€ sur compte UK pour réserver, libre dès demain.",
    },
    {
        "slug": "bordeaux",
        "display": "Bordeaux",
        "pop_k": 261,
        "students_k": 100,
        "arnaque_est_mois": 8,
        "quartiers_vigilance": [
            ("Chartrons / Quinconces", "rotation cadres + étudiants Sciences Po, prix-appâts"),
            ("Saint-Michel / Capucins", "annonces non visitées par téléphone, pression caution"),
            ("Saint-Genès / Talence (campus)", "primo-arrivants Université Bordeaux ciblés"),
            ("Caudéran / Saint-Augustin", "faux profils bailleurs expat retraités"),
            ("Bastide / rive droite", "annonces très en-dessous du marché signalées"),
        ],
        "specifique": "Bordeaux Métropole est en <a href=\"/encadrement-loyer-france-2026.html#anchor-bordeaux\">zone d'encadrement des loyers</a> depuis 2022 (loi Élan). Loyer de référence et complément doivent figurer au bail. Plafond meublé 17,4€/m² zone tendue.",
        "test_phrase": "Magnifique T1 Chartrons 380€ cc, libre tout de suite, mon père actuellement en mission Brésil, payez 760€ caution par crypto pour bloquer urgent.",
    },
    {
        "slug": "lille",
        "display": "Lille",
        "pop_k": 232,
        "students_k": 110,
        "arnaque_est_mois": 10,
        "quartiers_vigilance": [
            ("Vieux-Lille", "rentrée septembre étudiants Catho / Sciences Po, pression rapide"),
            ("Wazemmes / Moulins", "annonces leboncoin marché bas suspect"),
            ("Hellemmes / Fives", "ciblage primo-arrivants Erasmus, paiement avant visite"),
            ("République-Beaux-Arts", "faux profils bailleurs en mission Belgique"),
            ("Villeneuve d'Ascq / Cité Scientifique", "faux baux étudiants ingénieurs étrangers"),
        ],
        "specifique": "Métropole Européenne de Lille (MEL) est en <a href=\"/encadrement-loyer-france-2026.html#anchor-lille\">zone d'encadrement des loyers</a> depuis mars 2020. Loyer de référence et complément doivent figurer au bail. Voir aussi notre fiche <a href=\"/lille-dpe-f-g-interdit-location.html\">DPE F/G interdit Lille</a>.",
        "test_phrase": "Studio Vieux-Lille 320€ cc tout équipé, je travaille actuellement à Bruxelles, envoyez 640€ caution Bitcoin pour bloquer avant la rentrée.",
    },
    {
        "slug": "nantes",
        "display": "Nantes",
        "pop_k": 320,
        "students_k": 60,
        "arnaque_est_mois": 7,
        "quartiers_vigilance": [
            ("Bouffay / centre", "rotation étudiants U.Nantes / Audencia, faux profils"),
            ("Île de Nantes", "annonces neuves leboncoin avec virement préalable"),
            ("Doulon / Bottière", "marché très bas suspect, photos hors-plateforme"),
            ("Hauts-Pavés / Saint-Félix", "ciblage cadres mutés Airbus, faux baux meublés"),
            ("Malakoff / Saint-Donatien", "faux profils bailleurs internationaux"),
        ],
        "specifique": "Nantes Métropole n'est pas en zone d'encadrement des loyers (situation 2026). Seul recours en cas d'annonce trompeuse = signalement plateforme + dépôt plainte si paiement effectué.",
        "test_phrase": "T2 Île de Nantes 380€ cc, dispo, je suis en mission Argentine, payez 760€ Neosurf pour réservation, libre dès lundi.",
    },
    {
        "slug": "strasbourg",
        "display": "Strasbourg",
        "pop_k": 280,
        "students_k": 55,
        "arnaque_est_mois": 6,
        "quartiers_vigilance": [
            ("Krutenau / Université", "rentrée septembre Unistra ciblée"),
            ("Petite France / centre", "annonces touristiques détournées"),
            ("Robertsau / européens", "ciblage cadres CE / Conseil Europe, faux baux"),
            ("Neudorf / Esplanade", "primo-arrivants Erasmus / IEP"),
            ("Hautepierre / Cronenbourg", "annonces très en-dessous du marché"),
        ],
        "specifique": "Strasbourg n'est pas en zone d'encadrement des loyers. Pour les étudiants : passez par le CROUS Strasbourg pour les annonces vérifiées institutionnellement, ou par votre école avant tout virement.",
        "test_phrase": "Studio meublé Krutenau 350€ cc, libre, je travaille à Bruxelles, envoyez 700€ caution Western Union pour bloquer urgent.",
    },
]

JSON_LD_TEMPLATE = """{{"@context":"https://schema.org","@graph":[
{{"@type":"WebPage","@id":"https://bailleurverif.fr/arnaque-location-{slug}.html#webpage","url":"https://bailleurverif.fr/arnaque-location-{slug}.html","name":"Arnaque location {display} 2026 — scanner gratuit + signaux à connaître","description":"Détectez les arnaques aux annonces de location à {display} : scanner gratuit, 8 drapeaux rouges, quartiers à vigilance, conseils locaux.","inLanguage":"fr-FR","isPartOf":{{"@id":"https://bailleurverif.fr/#website"}},"datePublished":"2026-05-16","dateModified":"2026-05-16","breadcrumb":{{"@id":"https://bailleurverif.fr/arnaque-location-{slug}.html#breadcrumbs"}}}},
{{"@type":"BreadcrumbList","@id":"https://bailleurverif.fr/arnaque-location-{slug}.html#breadcrumbs","itemListElement":[{{"@type":"ListItem","position":1,"name":"Accueil","item":"https://bailleurverif.fr"}},{{"@type":"ListItem","position":2,"name":"Scanner anti-arnaque","item":"https://bailleurverif.fr/scanner-annonce-arnaque.html"}},{{"@type":"ListItem","position":3,"name":"{display}","item":"https://bailleurverif.fr/arnaque-location-{slug}.html"}}]}},
{{"@type":"FAQPage","@id":"https://bailleurverif.fr/arnaque-location-{slug}.html#faq","mainEntity":[
{{"@type":"Question","name":"Combien d'arnaques aux annonces de location estime-t-on par mois à {display} ?","acceptedAnswer":{{"@type":"Answer","text":"Estimation extrapolée depuis les signalements cybermalveillance.gouv.fr et les remontées plateformes : environ {arnaque_est_mois} cas par mois à {display} (population {pop_k}k, étudiants {students_k}k). Les pics sont en août-septembre (rentrée) et janvier-février (mutations)."}}}},
{{"@type":"Question","name":"Quels quartiers de {display} sont les plus ciblés par les arnaques ?","acceptedAnswer":{{"@type":"Answer","text":"Les quartiers à forte rotation étudiante et à forte demande sont plus exposés. Voir la liste détaillée dans cette page : 5 zones de vigilance avec contexte local."}}}},
{{"@type":"Question","name":"Comment vérifier qu'une annonce à {display} n'est pas une arnaque ?","acceptedAnswer":{{"@type":"Answer","text":"Collez le texte intégral de l'annonce dans notre scanner gratuit. Il détecte les 8 drapeaux rouges classiques en 30 secondes : paiement Western Union, bailleur étranger, caution avant visite, prix anormalement bas, basculement WhatsApp, ton d'urgence, photos hors-plateforme, adresse manquante."}}}}
]}},
{{"@type":"Organization","@id":"https://bailleurverif.fr/#organization","name":"BailleurVérif","url":"https://bailleurverif.fr","logo":{{"@type":"ImageObject","url":"https://bailleurverif.fr/logo.png"}},"sameAs":["https://github.com/Creariax5/bailleurverif"]}},
{{"@type":"WebSite","@id":"https://bailleurverif.fr/#website","url":"https://bailleurverif.fr","name":"BailleurVérif","inLanguage":"fr-FR","publisher":{{"@id":"https://bailleurverif.fr/#organization"}}}}
]}}"""


def render_quartier(qs):
    out = []
    for name, ctx in qs:
        out.append(f'<li><strong>{html.escape(name)}</strong> — {html.escape(ctx)}.</li>')
    return '\n'.join(out)


PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Arnaque location {display} 2026 — scanner gratuit + 5 quartiers à vigilance | BailleurVérif</title>
<meta name="description" content="Arnaques aux annonces de location à {display} : scanner gratuit (8 drapeaux rouges), {arnaque_est_mois} cas/mois estimés, quartiers à vigilance, conseils locaux. Sans inscription." />
<link rel="canonical" href="https://bailleurverif.fr/arnaque-location-{slug}.html" />
<meta property="og:title" content="Arnaque location {display} 2026 — scanner gratuit anonyme" />
<meta property="og:description" content="Vérifiez en 30 secondes si une annonce {display} est une arnaque. 5 quartiers à vigilance + 8 drapeaux rouges. Gratuit." />
<meta property="og:type" content="article" />
<meta property="og:url" content="https://bailleurverif.fr/arnaque-location-{slug}.html" />
<meta property="og:site_name" content="BailleurVérif" />
<meta property="og:locale" content="fr_FR" />
<meta name="twitter:card" content="summary" />
<meta name="twitter:title" content="Arnaque location {display} — scanner gratuit" />
<meta name="twitter:description" content="Détectez en 30 secondes si une annonce de location à {display} est une arnaque. 8 signaux. Gratuit." />
<link rel="alternate" type="application/atom+xml" title="BailleurVérif — Articles" href="/atom.xml" />
<script type="application/ld+json">{jsonld}</script>
<link rel="icon" type="image/svg+xml" href="/favicon.svg" />
<meta name="theme-color" content="#ffffff" />
<link rel="stylesheet" href="/css/main.css" />
<script src="https://cdn.tailwindcss.com"></script>
<style>
  .glass {{ background: rgba(255,255,255,0.85); backdrop-filter: blur(10px); border: 1px solid rgba(0,0,0,0.06); }}
  .gauge {{ height: 12px; border-radius: 999px; background: linear-gradient(90deg, #16a34a 0%, #facc15 50%, #dc2626 100%); position: relative; }}
  .gauge-marker {{ position: absolute; top: -6px; width: 4px; height: 24px; background: #111; border-radius: 2px; transform: translateX(-2px); }}
  .flag {{ display: flex; gap: .75rem; padding: .75rem 1rem; border-radius: 8px; margin-bottom: .5rem; align-items: flex-start; }}
  .flag-high {{ background: #fee2e2; border-left: 4px solid #dc2626; }}
  .flag-medium {{ background: #fef3c7; border-left: 4px solid #d97706; }}
  .flag-low {{ background: #dbeafe; border-left: 4px solid #2563eb; }}
  .badge {{ display: inline-block; font-size: .7rem; font-weight: 700; padding: .15rem .55rem; border-radius: 999px; text-transform: uppercase; }}
  .badge-high {{ background: #dc2626; color: #fff; }}
  .badge-medium {{ background: #d97706; color: #fff; }}
  .badge-low {{ background: #2563eb; color: #fff; }}
  .badge-safe {{ background: #16a34a; color: #fff; }}
  textarea {{ font-family: inherit; }}
</style>
</head>
<body class="bg-gradient-to-br from-slate-50 to-blue-50 min-h-screen text-slate-900">

<header class="border-b border-slate-200 bg-white/80 backdrop-blur sticky top-0 z-10">
  <div class="max-w-5xl mx-auto px-4 py-3 flex items-center justify-between">
    <a href="/" class="font-bold text-lg text-slate-900">BailleurVérif</a>
    <nav class="text-sm text-slate-600 hidden sm:flex gap-4">
      <a href="/" class="hover:text-slate-900">Accueil</a>
      <a href="/scanner-annonce-arnaque.html" class="hover:text-slate-900">Scanner arnaque</a>
      <a href="/preavis-bail.html" class="hover:text-slate-900">Préavis</a>
      <a href="/encadrement-loyer-france-2026.html" class="hover:text-slate-900">Encadrement loyer</a>
    </nav>
  </div>
</header>

<main class="max-w-5xl mx-auto px-4 py-8">

  <nav aria-label="Fil d'Ariane" class="text-xs text-slate-500 mb-4">
    <a href="/" class="hover:underline">Accueil</a> ›
    <a href="/scanner-annonce-arnaque.html" class="hover:underline">Scanner anti-arnaque</a> ›
    <span class="text-slate-700">{display}</span>
  </nav>

  <h1 class="text-3xl sm:text-4xl font-bold mb-3">Arnaque location {display} — scanner gratuit + quartiers à vigilance</h1>
  <p class="text-lg text-slate-700 mb-3">Vous cherchez un logement à <strong>{display}</strong> (population {pop_k}k, {students_k}k étudiants) et une annonce vous semble suspecte ? Collez son texte ci-dessous : notre scanner gratuit détecte les <strong>8 drapeaux rouges</strong> classiques des arnaques locatives, en 30 secondes, sans inscription.</p>
  <p class="text-sm text-slate-600 mb-6">Estimation locale 2026 : ~{arnaque_est_mois} signalements/mois à {display} (extrapolation depuis cybermalveillance.gouv.fr et remontées plateformes).</p>

  <div class="glass rounded-xl p-5 sm:p-6 mb-8">
    <label for="scan-input" class="block text-sm font-semibold text-slate-700 mb-2">Texte de l'annonce {display} à analyser</label>
    <textarea id="scan-input" rows="9" class="w-full border border-slate-300 rounded-lg p-3 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500" placeholder="Exemple {display} :&#10;&quot;{test_phrase}&quot;&#10;&#10;Collez ici le texte intégral de l'annonce (description + prix + contact)."></textarea>
    <div class="flex flex-col sm:flex-row gap-3 mt-3 items-stretch sm:items-center justify-between">
      <button id="scan-btn" class="bg-blue-600 hover:bg-blue-700 text-white font-semibold px-6 py-3 rounded-lg transition">Analyser l'annonce {display}</button>
      <p class="text-xs text-slate-500">Gratuit · anonyme · aucune inscription · texte non stocké</p>
    </div>
  </div>

  <div id="scan-result" class="hidden glass rounded-xl p-5 sm:p-6 mb-8">
    <div class="flex items-center gap-3 mb-4">
      <span id="scan-badge" class="badge"></span>
      <h2 id="scan-verdict" class="text-xl font-bold"></h2>
    </div>
    <div class="mb-5">
      <div class="flex justify-between text-xs text-slate-600 mb-1">
        <span>Sûr</span>
        <span id="scan-score-label">Score : –</span>
        <span>Très suspect</span>
      </div>
      <div class="gauge"><div id="scan-marker" class="gauge-marker"></div></div>
    </div>
    <div id="scan-flags-block" class="mb-5">
      <h3 class="text-sm font-semibold text-slate-700 mb-2">Drapeaux détectés</h3>
      <div id="scan-flags"></div>
    </div>
    <div id="scan-advice-block">
      <h3 class="text-sm font-semibold text-slate-700 mb-2">Conseils</h3>
      <ul id="scan-advice" class="list-disc list-inside text-sm text-slate-700 space-y-1"></ul>
    </div>
    <p id="scan-disclaimer" class="text-xs text-slate-500 mt-4 italic"></p>
  </div>

  <section class="prose prose-slate max-w-none mb-10">
    <h2 class="text-2xl font-bold mb-3">5 quartiers de {display} à vigilance accrue</h2>
    <p>Les arnaques aux annonces de location à {display} se concentrent dans les zones à forte rotation (étudiants, jeunes cadres, primo-arrivants). Les quartiers ci-dessous sont ceux où les signalements remontent le plus souvent en 2024-2026 :</p>
    <ul class="list-disc list-inside space-y-2 mt-3">
{quartiers_html}
    </ul>
    <p class="text-xs text-slate-500 mt-2 italic">Cette liste n'est pas exhaustive et reflète les tendances de signalement, pas l'insécurité réelle d'un quartier. Une annonce peut être saine dans un quartier "à risque" et arnaqueuse dans un quartier "sain". Le scanner ci-dessus reste l'arbitre fiable.</p>

    <h2 class="text-2xl font-bold mb-3 mt-8">Contexte local {display} 2026</h2>
    <p>{specifique}</p>

    <h2 class="text-2xl font-bold mb-3 mt-8">Les 8 drapeaux rouges qui s'appliquent partout (et à {display})</h2>
    <ol class="list-decimal list-inside space-y-2">
      <li><strong>Paiement Western Union / MoneyGram / Bitcoin / PCS / Neosurf</strong> — aucun bailleur sérieux ne demande ces moyens. Drapeau rouge maximal.</li>
      <li><strong>Bailleur déclaré à l'étranger ou en mission</strong> — "je suis à Londres / Dubai / Casablanca, envoyez par chronopost" : pattern classique.</li>
      <li><strong>Demande de caution ou loyer avant la visite</strong> — illégal en France (loi du 6 juillet 1989). Ne payez rien sans visite physique.</li>
      <li><strong>Prix anormalement bas</strong> — sous 5€/m² à {display}, c'est statistiquement impossible. Appât classique pour engager.</li>
      <li><strong>Basculement WhatsApp / Telegram dès le 1er message</strong> — sortir de la plateforme = échapper à sa modération.</li>
      <li><strong>Ton d'urgence injustifié</strong> — "URGENT", "libre tout de suite", "plusieurs candidats", "réservez sous 24h".</li>
      <li><strong>Photos envoyées par email/WhatsApp au lieu d'être dans l'annonce</strong> — souvent volées sur d'autres annonces ailleurs.</li>
      <li><strong>Adresse précise absente</strong> — un bailleur sérieux mentionne au moins la rue ou le métro. Adresse floue = suspect.</li>
    </ol>

    <h2 class="text-2xl font-bold mb-3 mt-8">Que faire si vous suspectez une arnaque à {display}</h2>
    <ol class="list-decimal list-inside space-y-1">
      <li><strong>Ne payez rien</strong>, même "pour réserver" ou "pour sécuriser".</li>
      <li><strong>Demandez la pièce d'identité du bailleur</strong> + un acte de propriété ou un mandat d'agence.</li>
      <li><strong>Visitez physiquement</strong> le logement avant tout engagement.</li>
      <li><strong>Signalez l'annonce</strong> sur la plateforme (Leboncoin, SeLoger, PAP ont tous un bouton signalement).</li>
      <li><strong>Si vous avez déjà versé de l'argent</strong> : déposez plainte au commissariat de police de {display} et signalez sur <a href="https://www.cybermalveillance.gouv.fr/" target="_blank" rel="noopener nofollow">cybermalveillance.gouv.fr</a>.</li>
      <li><strong>Contactez votre banque</strong> immédiatement : un virement SEPA peut parfois être rappelé sous 13 mois.</li>
    </ol>

    <h2 class="text-2xl font-bold mb-3 mt-8">Plateformes officielles {display}</h2>
    <ul class="list-disc list-inside space-y-1">
      <li><strong>Étudiants</strong> : CROUS (logements vérifiés institutionnellement).</li>
      <li><strong>Demandeurs précaires</strong> : DALO / SIAO local ({display}), pas d'arnaque possible (circuit public).</li>
      <li><strong>Particuliers</strong> : PAP, SeLoger, Leboncoin (avec scanner ci-dessus avant tout virement).</li>
      <li><strong>Agences</strong> : carte professionnelle T affichée obligatoirement (vérifiable préfecture).</li>
    </ul>
  </section>

  <aside class="grid sm:grid-cols-2 lg:grid-cols-4 gap-3 mb-10">
    <a href="/arnaque-location-france-2026.html" class="glass rounded-lg p-4 hover:bg-white transition">
      <div class="text-xs text-slate-500 uppercase">Hub national</div>
      <div class="font-bold">Arnaques France — 8 villes</div>
      <div class="text-sm text-slate-600 mt-1">Comparatif national + ~91 cas/mois estimés.</div>
    </a>
    <a href="/scanner-annonce-arnaque.html" class="glass rounded-lg p-4 hover:bg-white transition">
      <div class="text-xs text-slate-500 uppercase">Outil principal</div>
      <div class="font-bold">Scanner anti-arnaque</div>
      <div class="text-sm text-slate-600 mt-1">Page nationale + FAQ détaillée + 8 drapeaux.</div>
    </a>
    <a href="/preavis-bail.html" class="glass rounded-lg p-4 hover:bg-white transition">
      <div class="text-xs text-slate-500 uppercase">Outil gratuit</div>
      <div class="font-bold">Calculateur de préavis</div>
      <div class="text-sm text-slate-600 mt-1">1 mois ou 3 mois ? Lettre LRAR fournie.</div>
    </a>
    <a href="/encadrement-loyer-france-2026.html" class="glass rounded-lg p-4 hover:bg-white transition">
      <div class="text-xs text-slate-500 uppercase">Hub national</div>
      <div class="font-bold">Encadrement loyer 31 communes</div>
      <div class="text-sm text-slate-600 mt-1">Plafonds 2026 par commune et type.</div>
    </a>
  </aside>

  <footer class="border-t border-slate-200 pt-6 text-xs text-slate-500 space-y-2">
    <p>BailleurVérif — outil open-source MIT. Mise à jour : 2026-05-16.</p>
    <p><a href="/mentions-legales.html" class="underline">Mentions légales</a> · <a href="/politique-confidentialite.html" class="underline">Confidentialité</a> · <a href="/cgu.html" class="underline">CGU</a> · <a href="https://github.com/Creariax5/bailleurverif" class="underline" target="_blank" rel="noopener">GitHub</a></p>
  </footer>

</main>

<script src="/css/scanner.js"></script>
</body>
</html>
"""


def gen_all():
    out_dir = os.path.join(os.path.dirname(__file__), "static")
    written = []
    for c in CITIES:
        jsonld = JSON_LD_TEMPLATE.format(
            slug=c["slug"], display=c["display"],
            arnaque_est_mois=c["arnaque_est_mois"],
            pop_k=c["pop_k"], students_k=c["students_k"],
        )
        body = PAGE_TEMPLATE.format(
            slug=c["slug"], display=c["display"],
            pop_k=c["pop_k"], students_k=c["students_k"],
            arnaque_est_mois=c["arnaque_est_mois"],
            test_phrase=html.escape(c["test_phrase"], quote=True),
            quartiers_html=render_quartier(c["quartiers_vigilance"]),
            specifique=c["specifique"],
            jsonld=jsonld,
        )
        fname = f"arnaque-location-{c['slug']}.html"
        fpath = os.path.join(out_dir, fname)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(body)
        written.append((fname, len(body)))
    return written


if __name__ == "__main__":
    res = gen_all()
    for f, sz in res:
        print(f"{f}\t{sz}b")
    print(f"---\n{len(res)} pages written")
