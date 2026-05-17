#!/usr/bin/env python3
"""Audit empirique /api/scan-annonce sur 6 cas ambigus (edge cases) — run-163.

Objectif : mesurer FP/FN sur cas représentatifs réels (vs synthetic best-case run-162).
Hypothèse à tester :
- Légitime avec « urgence » justifiée juin (rush étudiants/mutations) → not flagged hopefully
- Arnaque sans paiement crypto/WU mais 3 flags faibles → catch borderline
- Légitime mention « caution avant visite » comme acompte légal de réservation → not flagged
- Légitime avec WhatsApp pour contact agence (pratique courante FR) → not flagged
- Arnaque langue mixte FR/EN avec urgence faible → catch
- Légitime mention « bailleur en mission » (expatrié réel) sans pattern arnaque → not flagged

Critère succès : ≥4/6 corrects. <4/6 = scanner trop simpliste, à raffiner.
"""
import json, urllib.request, time, sys

API = "https://bailleurverif.fr/api/scan-annonce"

# 3 arnaques ambiguës
ARNAQUES_EDGE = [
    {
        "id": "AE1_urgence_faible_telegram_bas_prix",
        "expected": "high",
        "text": """T2 36m2 quartier Lyon 7ème, refait à neuf, balcon, fibre.
Loyer 380€ charges comprises, super affaire à saisir.
Contactez moi en MP Telegram pour les détails et photos supplémentaires.
Je sélectionne sur dossier mais l'appartement part vite.""",
    },
    {
        "id": "AE2_arnaque_langue_mixte_FR_EN",
        "expected": "high",
        "text": """Beautiful T3 in Paris 15th, 65m2, fully furnished, balcony with view.
Owner currently working in London for 2 years, cannot visit in person.
Rent 1100€ all included. Send deposit (1100€) via international transfer to secure the apartment.
Bank details on request. Keys shipped FedEx after payment confirmation.
Excellent French metro, neighbors quiet, parquet floor, double glazing.""",
    },
    {
        "id": "AE3_arnaque_pas_de_crypto_juste_3_low_flags",
        "expected": "medium",
        "text": """Studio 22m2 Marseille 6ème, calme, ascenseur, lumineux.
Loyer 380€ tout compris, dépêchez-vous, je sélectionne aujourd'hui.
Pour des raisons personnelles je suis actuellement à Bruxelles, photos par email uniquement.
Pour réserver l'appartement merci de virer 380€ avant la visite.
Bail signé à mon retour mi-juin. Aucune visite physique avant paiement.""",
    },
]

# 3 légitimes ambiguës
LEGIT_EDGE = [
    {
        "id": "LE1_legit_urgence_rentree_juin",
        "expected": "safe",
        "text": """T2 40m2 Lyon 3ème, Part-Dieu, refait, calme, double vitrage.
URGENT pour rentrée septembre 2026, départ locataire actuel fin juin. À saisir rapidement.
Loyer 720€ + 60€ charges (chauffage collectif inclus, eau froide).
Dépôt 720€, bail 3 ans classique, garant ou Visale exigé.
Visites samedi 9h-12h sur RDV agence Foncia Lyon 3, 12 rue Garibaldi.""",
    },
    {
        "id": "LE2_legit_whatsapp_agence_contact",
        "expected": "safe",
        "text": """Appartement T3 55m2 Nice quartier Libération, 4ème étage avec ascenseur.
Loyer 950€ + 90€ provisions charges. Bail 3 ans non meublé.
Dépôt garantie 950€, honoraires 540€ TTC. Garant ou Visale.
Pour planifier une visite : WhatsApp agence ImmoNice 06 XX XX XX XX (numéro pro français).
Ou directement par téléphone aux horaires d'ouverture lundi-vendredi 9h-18h.""",
    },
    {
        "id": "LE3_legit_bailleur_expatrie_reel_via_gestionnaire",
        "expected": "safe",
        "text": """T2 45m2 Bordeaux centre, propriétaire actuellement expatrié au Canada (mission 3 ans).
Gestion locative confiée à Citya Bordeaux Mériadeck, 24 cours Maréchal Juin.
Loyer 780€ + 70€ charges. Bail 3 ans classique, DPE D (170 kWh/m²/an).
Dépôt 780€, état des lieux contradictoire avec agent Citya.
Toutes formalités gérées en France par l'agence, aucun paiement à l'étranger.""",
    },
]

def post(text):
    body = json.dumps({"text": text}).encode("utf-8")
    req = urllib.request.Request(API, data=body, headers={"Content-Type": "application/json", "User-Agent": "bv-audit-run163-edge"})
    with urllib.request.urlopen(req, timeout=10) as r:
        return json.loads(r.read().decode("utf-8"))

def main():
    results = []
    for ann in ARNAQUES_EDGE + LEGIT_EDGE:
        try:
            res = post(ann["text"])
            row = {"id": ann["id"], "expected": ann["expected"], "got_severity": res.get("severity"), "score": res.get("score"), "flags_count": len(res.get("flags", [])), "flags_labels": [f["label"] for f in res.get("flags", [])]}
        except Exception as e:
            row = {"id": ann["id"], "expected": ann["expected"], "error": str(e)}
        results.append(row)
        time.sleep(0.3)

    tp = fp = tn = fn = 0
    correct = 0
    for r in results:
        if "error" in r: continue
        is_arn_expected = r["expected"] in ("high", "medium")
        is_arn_predicted = r["got_severity"] in ("high", "medium")
        if is_arn_expected and is_arn_predicted:
            tp += 1; correct += 1
        elif is_arn_expected and not is_arn_predicted:
            fn += 1
        elif not is_arn_expected and is_arn_predicted:
            fp += 1
        else:
            tn += 1; correct += 1

    n = len(ARNAQUES_EDGE) + len(LEGIT_EDGE)
    out = {
        "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "scope": "edge_cases_ambiguous",
        "n_arnaque": len(ARNAQUES_EDGE),
        "n_legit": len(LEGIT_EDGE),
        "tp": tp, "tn": tn, "fp": fp, "fn": fn,
        "precision_arnaque": tp / max(1, tp + fp),
        "recall_arnaque": tp / max(1, tp + fn),
        "accuracy": correct / max(1, n),
        "verdict_success": correct >= 4,
        "results": results,
    }
    print(json.dumps(out, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
