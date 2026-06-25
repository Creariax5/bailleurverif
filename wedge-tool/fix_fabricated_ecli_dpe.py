#!/usr/bin/env python3
# run-655 2026-06-25 — Purge 2e vague de jurisprudence fabriquée/inexacte (suite critic-96 / run-654).
# Defects corrigés (vérifiés indépendamment Légifrance/Juricaf/courdecassation ce wake) :
#   - 22-14.121 / ECLI:FR:CCASS:2023:C300425  -> FABRIQUÉ (pourvoi absent de toutes bases). lille/nantes/toulouse/paris15e/llms
#   - 17-21.262 / ECLI:FR:CCASS:2019:C300182  -> ECLI réel MAIS = pourvoi 18-16.182 (VEFA fenêtres), hors-sujet DPE. lille
#   - 13-14.106 (21 mai 2014)                 -> NON VÉRIFIABLE (réel 21/05/2014 = 13-10.257, bail à construction). nantes/toulouse
#   - 2026:C300339 (template dpe-invalide)    -> décision RÉELLE (4 juin 2026, exéc. forcée délivrance logement décent)
#                                                mais ECLI fabriqué -> vrai pourvoi = 24-11.437 (Juricaf). On corrige l'ECLI -> pourvoi.
#   - C300983 description lille item1          -> ECLI réel mais holding mal décrit (décence au lieu de DPE/diagnostiqueur). Corrigé.
#   - liens profonds erronés C300983 (JURITEXT039442321 / courdecassation 5dd64a31) et 14-22.754 (031669108). Corrigés.
# Substituts = décisions RÉELLES vérifiées : 18-23.251/C300983 (DPE erroné), 14-22.754 (décence surface),
#   13-17.289/C300721 (décence chauffage), 24-11.437 (obligation continue délivrance).
import sys, pathlib
ROOT = pathlib.Path(__file__).parent
edits = []  # (relpath, old, new)

# ---------------- LILLE ----------------
F = "static/lille-dpe-f-g-interdit-location.html"
edits += [
 (F,
  'applique la jurisprudence Cass. civ. 3e 15 juin 2023 n° 22-14.121 (ECLI:FR:CCASS:2023:C300425).',
  'applique la jurisprudence Cass. civ. 3e 21 novembre 2019 n° 18-23.251 (ECLI:FR:CCASS:2019:C300983) sur la responsabilité du diagnostiqueur en cas de DPE erroné.'),
 (F,
  '''    <li><strong>Cass. civ. 3<sup>e</sup>, 21 novembre 2019, n° 18-23.251</strong> —
      <a href="https://www.legifrance.gouv.fr/juri/id/JURITEXT000039442321" class="text-blue-700 hover:text-blue-800 underline" rel="noopener" target="_blank">ECLI:FR:CCASS:2019:C300983</a>.
      Manquement à l'obligation de délivrance d'un logement décent : le locataire peut obtenir réduction rétroactive
      du loyer et dommages-intérêts pour préjudice de jouissance. Directement applicable à un logement G/F post-2025.</li>''',
  '''    <li><strong>Cass. civ. 3<sup>e</sup>, 21 novembre 2019, n° 18-23.251</strong> —
      <a href="https://www.legifrance.gouv.fr/juri/id/JURITEXT000039437795" class="text-blue-700 hover:text-blue-800 underline" rel="noopener" target="_blank">ECLI:FR:CCASS:2019:C300983</a>.
      DPE erroné : la responsabilité du diagnostiqueur est engagée envers l'acquéreur ou le locataire, qui subit
      une perte de chance indemnisable (négociation du prix ou du loyer). DPE opposable depuis le 1<sup>er</sup> juillet 2021.</li>'''),
 (F,
  '''    <li><strong>Cass. civ. 3<sup>e</sup>, 7 mars 2019, n° 17-21.262</strong> —
      <a href="https://www.legifrance.gouv.fr/juri/id/JURITEXT000038233812" class="text-blue-700 hover:text-blue-800 underline" rel="noopener" target="_blank">ECLI:FR:CCASS:2019:C300182</a>.
      L'inexécution durable par le bailleur de son obligation de délivrer un logement décent justifie la résolution
      du bail aux torts du bailleur (article 1719 Code civil).</li>''',
  '''    <li><strong>Cass. civ. 3<sup>e</sup>, 17 décembre 2015, n° 14-22.754</strong> (publié au bulletin) —
      <a href="https://www.legifrance.gouv.fr/juri/id/JURITEXT000031651978" class="text-blue-700 hover:text-blue-800 underline" rel="noopener" target="_blank">Légifrance</a>.
      Manquement à l'obligation de délivrance d'un logement décent (art. 6 loi 89-462) : le locataire peut obtenir
      la suspension ou la réduction du loyer. Directement applicable à un logement F/G non décent.</li>'''),
 (F,
  '''    <li><strong>Cass. civ. 3<sup>e</sup>, 15 juin 2023, n° 22-14.121</strong> —
      <a href="https://www.legifrance.gouv.fr/juri/id/JURITEXT000047732589" class="text-blue-700 hover:text-blue-800 underline" rel="noopener" target="_blank">ECLI:FR:CCASS:2023:C300425</a>.
      Caractère opposable du DPE depuis le 1<sup>er</sup> juillet 2021 : un DPE erroné engage la responsabilité
      du diagnostiqueur ET du bailleur si le classement effectif est défavorable au locataire.</li>''',
  '''    <li><strong>Cass. civ. 3<sup>e</sup>, 4 juin 2014, n° 13-17.289</strong> —
      <a href="https://www.legifrance.gouv.fr/juri/id/JURITEXT000029057014" class="text-blue-700 hover:text-blue-800 underline" rel="noopener" target="_blank">ECLI:FR:CCASS:2014:C300721</a>.
      Logement décent : la seule alimentation électrique ne vaut pas équipement de chauffage normal (décret 2002-120).
      Renforce l'exigence de décence énergétique opposable au bailleur d'un logement F/G.</li>'''),
]

# ---------------- NANTES + TOULOUSE (blocs identiques) ----------------
for F in ("static/nantes-dpe-f-g-interdit-location.html",
          "static/toulouse-dpe-f-g-interdit-location.html"):
    edits += [
     (F,
      'applique la jurisprudence Cass. civ. 3e 15 juin 2023 n° 22-14.121 (ECLI:FR:CCASS:2023:C300425) qui confirme le caractère opposable du DPE et la possibilité de réduction du loyer en cas d\'écart manifeste de classe.',
      'applique la jurisprudence Cass. civ. 3e 21 novembre 2019 n° 18-23.251 (ECLI:FR:CCASS:2019:C300983) qui retient la responsabilité du diagnostiqueur en cas de DPE erroné : le locataire ou l\'acquéreur subit une perte de chance indemnisable.'),
     (F,
      '''    <li><strong class="text-slate-900">Cass. civ. 3<sup>e</sup>, 15 juin 2023, n° 22-14.121</strong>
      (<a href="https://www.legifrance.gouv.fr/juri/id/JURITEXT000047754097" rel="noopener" target="_blank" class="text-blue-700 hover:text-blue-800 underline">ECLI:FR:CCASS:2023:C300425</a>) —
      Confirme le caractère <strong>opposable du DPE</strong> et la possibilité, pour le locataire, de demander la
      <strong>réduction du loyer</strong> en cas d'écart manifeste entre la classe affichée et la performance réelle du logement.</li>''',
      '''    <li><strong class="text-slate-900">Cass. civ. 3<sup>e</sup>, 21 novembre 2019, n° 18-23.251</strong>
      (<a href="https://www.legifrance.gouv.fr/juri/id/JURITEXT000039437795" rel="noopener" target="_blank" class="text-blue-700 hover:text-blue-800 underline">ECLI:FR:CCASS:2019:C300983</a>) —
      <strong>DPE erroné</strong> : la responsabilité du diagnostiqueur est engagée ; l'acquéreur ou le locataire subit une
      <strong>perte de chance</strong> indemnisable (négociation du prix ou du loyer). DPE opposable depuis le 1<sup>er</sup> juillet 2021.</li>'''),
     (F,
      'https://www.legifrance.gouv.fr/juri/id/JURITEXT000031669108',
      'https://www.legifrance.gouv.fr/juri/id/JURITEXT000031651978'),
     (F,
      '''    <li><strong class="text-slate-900">Cass. civ. 3<sup>e</sup>, 21 mai 2014, n° 13-14.106</strong>
      (<a href="https://www.legifrance.gouv.fr/juri/id/JURITEXT000028964447" rel="noopener" target="_blank" class="text-blue-700 hover:text-blue-800 underline">recherche Légifrance</a>) —
      Confirme la possibilité pour le locataire d'exiger des <strong>travaux à la charge du bailleur</strong> pour rendre
      le logement décent, sous astreinte si nécessaire.</li>''',
      '''    <li><strong class="text-slate-900">Cass. civ. 3<sup>e</sup>, 4 juin 2014, n° 13-17.289</strong>
      (<a href="https://www.legifrance.gouv.fr/juri/id/JURITEXT000029057014" rel="noopener" target="_blank" class="text-blue-700 hover:text-blue-800 underline">ECLI:FR:CCASS:2014:C300721</a>) —
      Logement décent : la seule <strong>alimentation électrique</strong> ne vaut pas équipement de chauffage normal (décret 2002-120).
      Le locataire peut exiger des <strong>travaux à la charge du bailleur</strong>, au besoin sous astreinte.</li>'''),
    ]

# ---------------- PARIS 15e FAQ ----------------
F = "static/encadrement-loyer-paris-15eme-2026-faq-complete.html"
edits += [
 (F,
  'Cass. civ. 3ᵉ ECLI:FR:CCASS:2019:C300983 (21 novembre 2019) et ECLI:FR:CCASS:2023:C300425 (15 juin 2023) précisent les conditions d\'engagement de la responsabilité du diagnostiqueur.',
  'Cass. civ. 3ᵉ ECLI:FR:CCASS:2019:C300983 (21 novembre 2019, pourvoi n° 18-23.251) précise les conditions d\'engagement de la responsabilité du diagnostiqueur en cas de DPE erroné.'),
 (F,
  '<a href="https://www.courdecassation.fr/decision/5dd64a31a06595abc879a4f8" target="_blank" rel="noopener">Cass. civ. 3ᵉ ECLI:FR:CCASS:2019:C300983</a> + <a href="https://www.courdecassation.fr/decision/648b6e76a9c8d7000730e1cd" target="_blank" rel="noopener">ECLI:FR:CCASS:2023:C300425</a> (15 juin 2023) éclairent la responsabilité du diagnostiqueur.',
  '<a href="https://www.legifrance.gouv.fr/juri/id/JURITEXT000039437795" target="_blank" rel="noopener">Cass. civ. 3ᵉ ECLI:FR:CCASS:2019:C300983</a> (21 nov. 2019, pourvoi n° 18-23.251) éclaire la responsabilité du diagnostiqueur en cas de DPE erroné.'),
 (F,
  '<a href="https://www.courdecassation.fr/decision/5dd64a31a06595abc879a4f8" target="_blank" rel="noopener">Cass. civ. 3ᵉ ECLI:FR:CCASS:2019:C300983</a> (21 nov. 2019)',
  '<a href="https://www.legifrance.gouv.fr/juri/id/JURITEXT000039437795" target="_blank" rel="noopener">Cass. civ. 3ᵉ ECLI:FR:CCASS:2019:C300983</a> (21 nov. 2019, pourvoi n° 18-23.251)'),
]

# ---------------- TEMPLATE cat-3 dpe-invalide (moat) ----------------
F = "static/api-recourse-md-cache/dpe-invalide.md"
edits += [
 (F,
  '- Le locataire d\'un local à usage d\'habitation est recevable, d\'une part, à poursuivre l\'exécution forcée en nature de l\'obligation de délivrance d\'un logement décent tant que le manquement perdure, d\'autre part à obtenir la réparation des conséquences de ce manquement. _( ECLI ECLI:FR:CCASS:2026:C300339 · Troisième chambre civile · 2026-06-04 )_',
  '- Le locataire d\'un local à usage d\'habitation est recevable, d\'une part, à poursuivre l\'exécution forcée en nature de l\'obligation de délivrance d\'un logement décent tant que le manquement perdure, d\'autre part à obtenir la réparation des conséquences de ce manquement (dans la limite de la prescription triennale, art. 7-1 loi 89-462). _( Cour de cassation, 3ᵉ chambre civile, 4 juin 2026, pourvoi n° 24-11.437 · Publié au bulletin )_'),
]

# ---------------- llms-full.txt ----------------
F = "static/llms-full.txt"
edits += [
 (F,
  '- **Template `dpe-invalide`** : Cass. civ. 3ᵉ `ECLI:FR:CCASS:2024:C300983` (responsabilité du bailleur en cas de DPE erroné fourni en location), Cass. civ. 3ᵉ `ECLI:FR:CCASS:2024:C300182` (interdiction effective de location DPE G depuis 2025 — bail postérieur réputé non écrit sur la mise en location), Cass. civ. 3ᵉ `ECLI:FR:CCASS:2024:C300425` (étendue des travaux opposables au bailleur DPE F en vue de l\'échéance 2028).',
  '- **Template `dpe-invalide`** : Cass. civ. 3ᵉ `ECLI:FR:CCASS:2019:C300983` (DPE erroné — responsabilité du diagnostiqueur, perte de chance indemnisable, pourvoi 18-23.251), Cass. civ. 3ᵉ `ECLI:FR:CCASS:2014:C300721` (logement décent — la seule alimentation électrique ne vaut pas chauffage normal, pourvoi 13-17.289), Cass. civ. 3ᵉ 4 juin 2026 pourvoi n° 24-11.437 (obligation continue de délivrance d\'un logement décent — exécution forcée en nature tant que le manquement perdure).'),
]

# ---------------- APPLY ----------------
errors, applied = [], 0
files = {}
for rel, old, new in edits:
    files.setdefault(rel, None)
for rel in files:
    p = ROOT / rel
    files[rel] = p.read_text(encoding="utf-8")
for rel, old, new in edits:
    txt = files[rel]
    n = txt.count(old)
    if n != 1:
        errors.append(f"{rel}: expected 1 occurrence, found {n}: {old[:70]!r}")
        continue
    files[rel] = txt.replace(old, new)
    applied += 1
if errors:
    print("ABORT — unmatched OLD strings:")
    for e in errors: print("  ", e)
    sys.exit(1)
for rel, txt in files.items():
    (ROOT / rel).write_text(txt, encoding="utf-8")
print(f"OK — {applied} replacements across {len(files)} files.")
