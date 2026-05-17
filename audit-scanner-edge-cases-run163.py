#!/usr/bin/env python3
"""Audit empirique scanner-arnaque sur 8 cas AMBIGUS/édge (vs run-162 cas classiques 100%/100%).

But : mesurer FP/FN sur cas représentatifs réels où la classification est ambiguë.
- 4 arnaques 'subtiles' (1-2 flags low, urgence justifiable, motif réel mais déguisé)
- 4 légitimes 'piégeux' (mentions qui pourraient déclencher faux positifs : caution Visale,
  bailleur en mission justifiée, urgence légitime juin étudiant, particulier sans agence)

Référence motifs : cybermalveillance.gouv.fr + signal-arnaques.com + ANIL faux annonces 2025.
"""
import json, urllib.request, time

API = "https://bailleurverif.fr/api/scan-annonce"

# ARNAQUES SUBTILES — déguisées, peu de flags évidents, mais sémantique d'arnaque réelle
ARNAQUES_SUBTLES = [
    {
        "id": "AS1_caution_avant_visite_sans_money_transfer_classique",
        "expected": "high",
        "comment": "Arnaque classique post-2024 : la caution avant visite EST le drapeau cardinal, mais sans WU/BTC/PCS explicite. Test sans facilitateurs paiement bizarres.",
        "text": """Loue T2 45m2 Lille Vieux-Lille, refait à neuf, parquet, fibre, cave.
Loyer 720€ + 60€ charges. Caution standard 720€.
Beaucoup de demandes : pour confirmer votre intérêt avant la visite, virement de 200€ d'arrhes sur mon RIB que je vous communique par mail.
Visite organisée uniquement après réception du virement. Disponible immédiatement.""",
    },
    {
        "id": "AS2_proprietaire_mission_japon_visite_video_only",
        "expected": "high",
        "comment": "Pas de WU/BTC. Mais combo bailleur étranger + visite vidéo only + paiement avant clés = arnaque type airbnb-scam.",
        "text": """Beau studio 30m2 Toulouse Saint-Cyprien, vue Garonne, balcon.
Je suis actuellement en mission au Japon pour 1 an, je ne peux pas faire visiter en personne.
Je propose une visite par WhatsApp Vidéo (très complète, je montre tout, vous pouvez poser des questions).
Loyer 550€ tout compris. Caution 550€ + premier mois à régler par virement avant envoi des clés par chronopost sécurisé.
Bail signé en pdf, scan envoyé par mail. Disponible immédiatement.""",
    },
    {
        "id": "AS3_etudiant_caution_visale_mais_paypal_friend",
        "expected": "high",
        "comment": "L'arnaque utilise des mots rassurants (Visale, DPE C, justificatifs) mais demande PayPal Friends&Family (irréversible) — flag à ne PAS rater.",
        "text": """Studio meublé 20m2 idéal étudiant, Grenoble centre, proche tram.
Loyer 420€ charges comprises. DPE C, double vitrage. Garant Visale accepté.
Pour me prouver votre solvabilité (j'ai eu trop de no-show), je demande un dépôt symbolique de 100€ via PayPal en mode Amis et Famille (vous me le verrez crédité avant la visite).
Ce montant sera déduit du premier loyer. Bail mobilité 9 mois.""",
    },
    {
        "id": "AS4_marchand_de_sommeil_caution_cash_pas_de_bail_ecrit",
        "expected": "high",
        "comment": "Arnaque sociale : pas d'arnaque crypto, mais bail oral, cash, pas d'état des lieux, DPE absent — marchand de sommeil classique.",
        "text": """Loue chambre 9m2 dans appartement partagé Paris 20ème métro Belleville.
350€ par mois en cash directement au propriétaire chaque début de mois.
Pas besoin de bail papier, on se met d'accord à l'oral, c'est plus simple.
Caution 350€ cash le jour de l'emménagement. Pas d'état des lieux, on se fait confiance.
Disponible tout de suite, je préfère pas de paperasse compliquée.""",
    },
]

# LÉGITIMES PIÉGEUSES — vocabulaire ou contexte qui POURRAIT déclencher des flags
LEGIT_TRICKY = [
    {
        "id": "LT1_legitime_urgent_juin_etudiant_bail_mobilite",
        "expected": "safe",
        "comment": "Mot 'urgent' présent mais contexte légitime (rentrée septembre, bail mobilité juin). Visale + agence + RDV physiques.",
        "text": """URGENT — Studio meublé 22m2 Nantes Hauts-Pavés, libre 15 juin pour bail mobilité ou bail meublé 1 an.
Loyer 520€ charges comprises, DPE D, fibre, parquet, kitchenette équipée (frigo, plaque, micro-ondes).
Idéal étudiant rentrée septembre ou stagiaire. Caution 1040€ (2 mois meublé) ou Visale.
Dossier complet exigé : 3 derniers bulletins de salaire OU attestation scolarité + justificatif garant.
Visite agence Square Habitat sur RDV uniquement, du mardi au samedi 10h-18h. Bail signé en agence.""",
    },
    {
        "id": "LT2_legitime_bailleur_a_letranger_via_agence_mandataire",
        "expected": "safe",
        "comment": "Bailleur étranger MAIS agence locale mandataire et toutes les opérations sur place. Doit être classé safe.",
        "text": """Bailleur expatrié au Luxembourg, gestion locative confiée à l'agence Foncia Lyon 6ème.
T3 70m2 quartier Brotteaux, balcon, ascenseur, 4ème étage. Loyer 1280€ + 110€ charges.
Toutes les visites sont organisées par l'agence Foncia (45 cours Vitton, 69006 Lyon, 04 78 XX XX XX).
Caution 1280€ versée à l'agence, état des lieux contradictoire avec l'agent, bail signé en agence.
DPE classe C, double vitrage récent, chauffage collectif. Disponible 1er juillet.""",
    },
    {
        "id": "LT3_particulier_caution_visale_pas_de_telephone_visible",
        "expected": "safe",
        "comment": "Annonce particulier sans tél visible (RGPD) ni adresse précise, contact via messagerie plateforme — légitime.",
        "text": """Particulier loue T2 38m2 lumineux à Rennes quartier Sainte-Anne (proche métro Sainte-Anne).
Loyer 620€ + 50€ charges. DPE E (logement ancien, travaux d'isolation prévus 2027 dans le cadre du calendrier Loi Climat).
Caution 1240€ classique ou Visale. Dépôt de garantie réglé par virement à la signature du bail.
Bail meublé 1 an renouvelable. Préférence locataire stable, en CDI ou fonctionnaire, avec garant solide.
Pour planifier une visite et recevoir l'adresse exacte, contactez-moi via la messagerie du site.""",
    },
    {
        "id": "LT4_legit_meuble_appartement_paris_dispo_immediat_dossier_lourd",
        "expected": "safe",
        "comment": "Dispo immédiate (mot pouvant être suspect) MAIS dossier locataire structuré, agence, visite physique.",
        "text": """Appartement T1 24m2 meublé, 17 rue de la Pompe, Paris 16ème, 5ème étage avec ascenseur.
Disponible immédiatement suite départ précédent locataire (mutation professionnelle).
Loyer 1150€ + 90€ charges. Honoraires agence 480€ TTC. Caution 1150€ + 1150€ (2 mois meublé).
Dossier locataire : pièce d'identité, 3 derniers bulletins de salaire, contrat de travail (CDI confirmé) OU 2 derniers avis d'imposition pour profession libérale, RIB, justificatif domicile.
Garant solidaire exigé (parents ou Visale). Visite uniquement sur RDV avec l'agence Lodgis, 4 rue de la Pompe.""",
    },
]

def post(text):
    body = json.dumps({"text": text}).encode("utf-8")
    req = urllib.request.Request(API, data=body, headers={"Content-Type": "application/json", "User-Agent": "bv-audit-run163"})
    with urllib.request.urlopen(req, timeout=10) as r:
        return json.loads(r.read().decode("utf-8"))

def main():
    results = []
    for ann in ARNAQUES_SUBTLES + LEGIT_TRICKY:
        try:
            res = post(ann["text"])
            row = {
                "id": ann["id"],
                "expected": ann["expected"],
                "got_severity": res.get("severity"),
                "score": res.get("score"),
                "flags_count": len(res.get("flags", [])),
                "flags_labels": [f.get("label") for f in res.get("flags", [])],
                "comment": ann["comment"],
            }
        except Exception as e:
            row = {"id": ann["id"], "expected": ann["expected"], "error": str(e)}
        results.append(row)
        time.sleep(0.3)

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
        "audit_type": "edge_cases_run163",
        "n_arnaque_subtle": len(ARNAQUES_SUBTLES),
        "n_legit_tricky": len(LEGIT_TRICKY),
        "tp": tp, "tn": tn, "fp": fp, "fn": fn,
        "precision_arnaque": round(tp / max(1, tp + fp), 3),
        "recall_arnaque": round(tp / max(1, tp + fn), 3),
        "accuracy": round((tp + tn) / max(1, tp + tn + fp + fn), 3),
        "results": results,
    }
    print(json.dumps(out, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
