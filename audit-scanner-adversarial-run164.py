#!/usr/bin/env python3
"""Audit adversarial scanner V1.1 sur 6 cas (vs run-163 edge cases 6/6 V1.1=1.00).

But : trouver les FP/FN sur cas vraiment HOSTILES :
- AV1 : obfuscation typographique (leet, accents, "W3st3rn Un10n", "B!tcoin")
- AV2 : ASCII spacing ("W e s t e r n  U n i o n", "B i t c o i n")
- AV3 : code-switching FR/EN/DE pour eviter regex monolingue
- AV4 : pressure sociale pure SANS mots-cles (no "urgent", no WU, multi-bidders deadline)
- AL1 : legit avec "wire" / "transfer" en contexte non-paiement
- AL2 : legit qui CITE des mots arnaque pour les denoncer (anti-pattern texte preventif)

Si V1.1 rate ces cas = on a deja la spec V1.2.
"""
import json, urllib.request, time

API = "https://bailleurverif.fr/api/scan-annonce"

ADVERSARIAL_ARNAQUES = [
    {
        "id": "AV1_leet_obfuscation_W3st3rn_B!tcoin",
        "expected": "high",
        "comment": "Arnaqueur sophistique remplace lettres par chiffres/symboles. V1.1 utilise regex litteral, va probablement RATER.",
        "text": """Loue T2 40m2 Paris 18eme, refait neuf, fibre.
Loyer 580€/mois charges comprises. Caution 580€.
Beaucoup de demandes, je demande 200€ d'arrhes pour bloquer.
Paiement uniquement par W3st3rn Un10n ou B!tcoin (BTC), je suis a l'etranger pour 6 mois.
Cle envoyee par DHL apres reception du virement.""",
    },
    {
        "id": "AV2_ascii_spacing_obfuscation",
        "expected": "high",
        "comment": "Espaces inseres entre lettres pour casser le tokenization regex. \\b...\\b fails.",
        "text": """Beautiful studio Lyon Croix-Rousse, 25m2, balcony.
Rent 480€/month all-inclusive. Deposit 480€.
Owner currently traveling abroad. Send the deposit via W e s t e r n   U n i o n
or as B i t c o i n (faster). Photos by email upon request.
Keys shipped FedEx 24h after payment received.""",
    },
    {
        "id": "AV3_codeswitch_DE_EN_FR",
        "expected": "high",
        "comment": "Annonce trilingue. Bailleur a Berlin, Kaution en EN. V1.1 EN partiel mais DE 0 patterns.",
        "text": """Schones Apartment in Marseille Vieux-Port, 35qm, voll moebliert.
Owner is currently in Berlin for work, kann nicht persoenlich zeigen.
Loyer 650€/mois. Kaution 650€ + erste Miete par bank transfer to my German account before keys delivery.
Visite uniquement par WhatsApp Video, sehr ausfuehrlich.
Ich akzeptiere auch Bitcoin payment if faster.""",
    },
    {
        "id": "AV4_pressure_no_keywords_deadline_bidders",
        "expected": "medium",
        "comment": "Pure social engineering. Pas de WU, pas de telegram, pas d'urgent. Mais : 7 candidats, deadline 24h, paiement RIB avant visite. Doit lever AU MOINS medium.",
        "text": """T3 65m2 Bordeaux Chartrons, parquet, balcon, ascenseur, refait 2024.
Loyer 980€ + 80€ charges. Caution 980€.
J'ai actuellement 7 dossiers serieux pour ce bien. Je clos les candidatures vendredi 23h.
Pour etre pris en compte dans la selection, merci de virer 250€ a la signature pre-bail
sur mon RIB que je transmets par mail. Ces 250€ seront integres dans le premier loyer.
Bail signe scanne, envoye en RAR au lauréat. Pas de visite organisee, dossier sur photos suffit.""",
    },
]

ADVERSARIAL_LEGIT = [
    {
        "id": "AL1_legit_wire_in_neutral_sense",
        "expected": "safe",
        "comment": "Mot 'wire' present mais contexte cablage electrique. Pas un faux positif legitime.",
        "text": """T2 48m2 Strasbourg Krutenau, renove 2025, fibre optique, parquet chene.
Loyer 720€ + 60€ charges. Caution 720€ ou Visale.
Logement entierement rewired (mise aux normes electriques NF C 15-100), nouvelle wire box.
Visite uniquement sur RDV avec l'agence Foncia Strasbourg (8 rue de la Mesange, 67000).
Bail signe en agence apres reception complete du dossier locataire (3 bulletins, contrat, RIB).""",
    },
    {
        "id": "AL2_legit_anti_arnaque_warning_in_description",
        "expected": "safe",
        "comment": "Bailleur experimente mentionne 'methode anti-arnaque' avec les termes Western Union/Bitcoin dans un disclaimer. Faut PAS le flagger high.",
        "text": """T1 22m2 Toulouse Capitole, meuble, calme, lumineux. Bail mobilite 9 mois.
Loyer 480€ tout compris. Caution 480€ ou Visale.
ATTENTION arnaques : je ne demande JAMAIS de virement Western Union, MoneyGram, Bitcoin, PCS ou Neosurf.
Tout paiement uniquement par virement SEPA nominatif sur RIB officiel apres signature en agence.
Visite physique obligatoire avec l'agence Century 21 Capitole (5 rue Lafayette, 31000 Toulouse).
DPE classe D. Disponible 1er aout 2026.""",
    },
]

def post(text):
    body = json.dumps({"text": text}).encode("utf-8")
    req = urllib.request.Request(API, data=body, headers={"Content-Type": "application/json", "User-Agent": "bv-audit-adversarial-run164"})
    with urllib.request.urlopen(req, timeout=10) as r:
        return json.loads(r.read().decode("utf-8"))

def main():
    results = []
    for ann in ADVERSARIAL_ARNAQUES + ADVERSARIAL_LEGIT:
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
        "audit_type": "adversarial_run164",
        "scanner_version_under_test": "V1.1",
        "n_arnaque_adversarial": len(ADVERSARIAL_ARNAQUES),
        "n_legit_adversarial": len(ADVERSARIAL_LEGIT),
        "tp": tp, "tn": tn, "fp": fp, "fn": fn,
        "precision_arnaque": round(tp / max(1, tp + fp), 3),
        "recall_arnaque": round(tp / max(1, tp + fn), 3),
        "accuracy": round((tp + tn) / max(1, tp + tn + fp + fn), 3),
        "results": results,
    }
    print(json.dumps(out, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
