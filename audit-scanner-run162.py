#!/usr/bin/env python3
"""Audit empirique /api/scan-annonce sur 8 annonces (4 arnaques + 4 légitimes)."""
import json, urllib.request, urllib.parse, time, sys

API = "https://bailleurverif.fr/api/scan-annonce"

# 4 arnaques (motifs réels documentés cybermalveillance.gouv.fr / signal-arnaques.com)
ARNAQUES = [
    {
        "id": "A1_bailleur_etranger_western_union",
        "expected": "high",
        "text": """Loue beau T3 60m2 dans le centre de Paris, refait à neuf, balcon, calme.
Je suis actuellement à l'étranger pour mon travail (Royaume-Uni), je ne peux donc pas faire visiter.
Pour réserver l'appartement, merci de m'envoyer la caution de 1500€ via Western Union à mon nom.
Je vous enverrai les clés par DHL dès réception du paiement. Loyer 800€ + 100€ charges.
Contactez moi par WhatsApp +44 7XXX XXXXXX, je ne réponds pas sur la messagerie Leboncoin.""",
    },
    {
        "id": "A2_prix_trop_bas_telegram",
        "expected": "high",
        "text": """T2 35m2 Paris 11ème, lumineux, parquet, cuisine équipée, métro Charonne.
Loyer 250€ tout compris, urgent il faut signer aujourd'hui, plusieurs personnes intéressées.
Photos disponibles par email sur demande. Pour les détails, contactez moi par Telegram @prop_paris_11.
Caution 250€ à envoyer en Bitcoin (BTC) avant la visite pour bloquer le bien.""",
    },
    {
        "id": "A3_studio_caution_avant_visite",
        "expected": "high",
        "text": """Studio 22m2 Lyon 3ème quartier Part-Dieu, rénové, cuisine américaine, fibre.
Loyer 480€ charges comprises. Plusieurs demandes, je sélectionne par ordre de paiement caution.
Envoyez la caution (480€) par PCS Neosurf avant la visite pour confirmer votre intérêt.
Visite programmée uniquement après réception du paiement. Disponible immédiat.""",
    },
    {
        "id": "A4_propriétaire_mission_photos_email",
        "expected": "high",
        "text": """T1 28m2 Marseille 7ème, vue mer, balcon, calme, proche métro.
Propriétaire actuellement en mission au Canada, photos disponibles par WhatsApp uniquement.
Pour réserver, transfert cash de 600€ par MoneyGram à mon nom, je vous envoie ensuite le bail signé.
Dépêchez-vous, très rapide, plusieurs candidats sérieux.""",
    },
]

# 4 annonces légitimes (typiques agence ou particulier respectant les règles)
LEGIT = [
    {
        "id": "L1_appart_agence_paris_normal",
        "expected": "safe",
        "text": """Appartement T2 de 42m2 situé 24 rue de la Roquette, Paris 11ème.
Au 3ème étage avec ascenseur, lumineux double exposition sud-ouest, parquet point de Hongrie d'origine.
Cuisine équipée (plaque vitro, four, hotte, lave-vaisselle), salle d'eau avec douche italienne.
Loyer 1380€ hors charges + 120€ provisions charges (chauffage collectif inclus).
Dépôt de garantie 1380€, honoraires agence 600€ TTC. Visite sur RDV agence du lundi au vendredi 9h-18h.""",
    },
    {
        "id": "L2_studio_etudiant_lyon",
        "expected": "safe",
        "text": """Studio meublé de 25m2 au 12 avenue Berthelot, Lyon 7ème, proche métro Jean Macé.
Idéal étudiant ou jeune actif, 4ème étage sans ascenseur, calme côté cour, fibre internet.
Loyer 580€ charges comprises (eau, électricité, chauffage individuel gaz, taxe ordures).
Bail mobilité 9 mois ou bail meublé classique 1 an renouvelable. Garant exigé ou caution Visale.
Visites programmées le samedi matin. Bail signé devant notaire ou en agence.""",
    },
    {
        "id": "L3_t3_particulier_bordeaux",
        "expected": "safe",
        "text": """Particulier loue T3 65m2 au 8 cours de la Marne, Bordeaux quartier Saint-Michel.
2 chambres, séjour avec balcon, cuisine séparée équipée, salle de bain avec baignoire, WC séparés.
Chauffage gaz individuel, double vitrage récent, DPE classe D (consommation 180 kWh/m²/an).
Loyer 1050€ + 80€ charges (entretien parties communes, eau froide).
Caution 1050€, état des lieux contradictoire. Visites sur RDV mardi et jeudi 17h-19h.""",
    },
    {
        "id": "L4_t1_marseille_meuble",
        "expected": "safe",
        "text": """Loue T1 30m2 meublé refait à neuf, 45 boulevard Chave, Marseille 5ème.
Quartier La Plaine, proche métro Notre-Dame du Mont, fibre, double vitrage, parquet stratifié.
Cuisine équipée (frigo, plaque induction, micro-ondes), lit double, bureau, rangements.
Loyer 620€ + 50€ charges forfaitaires. Caution 1240€ (2 mois), bail meublé 1 an.
Visites sur RDV en présence du propriétaire. Dossier locataire complet exigé (3 derniers bulletins, garant).""",
    },
]

def post(text):
    body = json.dumps({"text": text}).encode("utf-8")
    req = urllib.request.Request(API, data=body, headers={"Content-Type": "application/json", "User-Agent": "bv-audit-run162"})
    with urllib.request.urlopen(req, timeout=10) as r:
        return json.loads(r.read().decode("utf-8"))

def main():
    results = []
    for ann in ARNAQUES + LEGIT:
        try:
            res = post(ann["text"])
            row = {"id": ann["id"], "expected": ann["expected"], "got_severity": res.get("severity"), "score": res.get("score"), "flags_count": len(res.get("flags", [])), "flags_labels": [f["label"] for f in res.get("flags", [])]}
        except Exception as e:
            row = {"id": ann["id"], "expected": ann["expected"], "error": str(e)}
        results.append(row)
        time.sleep(0.3)

    # Compute confusion matrix
    tp = fp = tn = fn = 0
    for r in results:
        if "error" in r: continue
        is_arn_expected = r["expected"] in ("high", "medium")
        is_arn_predicted = r["got_severity"] in ("high", "medium")
        if is_arn_expected and is_arn_predicted: tp += 1
        elif is_arn_expected and not is_arn_predicted: fn += 1
        elif not is_arn_expected and is_arn_predicted: fp += 1
        else: tn += 1

    out = {
        "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "n_arnaque": len(ARNAQUES),
        "n_legit": len(LEGIT),
        "tp": tp, "tn": tn, "fp": fp, "fn": fn,
        "precision_arnaque": tp / max(1, tp + fp),
        "recall_arnaque": tp / max(1, tp + fn),
        "accuracy": (tp + tn) / max(1, tp + tn + fp + fn),
        "results": results,
    }
    print(json.dumps(out, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
