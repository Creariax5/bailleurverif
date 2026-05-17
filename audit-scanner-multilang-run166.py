#!/usr/bin/env python3
"""Audit scanner V1.2 sur cas multi-langue : it / es / pt / ar.

But : verifier que V1.2 (regex EN+FR + agence detection + disclaimer window + booleen pressure)
detecte les arnaques redigees principalement dans une autre langue (DOM-TOM, Maghreb,
diaspora portugaise/espagnole). Si V1.2 rate ces cas = spec V1.3 (i18n keywords).

Hypothese H : V1.2 rate les langues non-FR/EN car aucun regex it/es/pt/ar present.
Pour qu'un scanner V1.x serve les francophones diaspora et DOM-TOM, il faut au moins
detecter `Western Union / Bitcoin / Telegram / WhatsApp / virement` dans ces langues.
"""
import json, urllib.request, time

API = "https://bailleurverif.fr/api/scan-annonce"

CASES_ML = [
    {
        "id": "ML1_it_scam_WU_telegram",
        "expected": "high",
        "lang": "it",
        "comment": "Annonce italophone arnaque WU classique. V1.2 doit attraper 'Western Union' meme dans phrase italienne.",
        "text": """Affittasi T2 Marsiglia 13013, 45mq, recentemente ristrutturato.
Affitto 580€/mese tutto incluso. Cauzione 580€.
Attualmente all'estero per lavoro, non posso mostrare di persona.
Pagamento solo via Western Union o Bitcoin sul mio account. Chiavi spedite DHL dopo conferma pagamento.
Contattatemi solo via Telegram per dettagli rapidi.""",
    },
    {
        "id": "ML2_es_scam_giro_btc_anticipo",
        "expected": "high",
        "lang": "es",
        "comment": "Espagnol Andalou - virement + bitcoin + arrhe + pas visite. WU/BTC mots-cles latins reperables.",
        "text": """Alquilo estudio Toulouse Centro 25m2, recien renovado, fibra optica.
Renta 450€/mes con gastos. Fianza 450€.
Soy expat en Madrid, propiedad heredada. No puedo viajar antes del 1 de septiembre.
Para reservar pido 300€ de senal por transferencia Western Union o pago en Bitcoin.
Llaves enviadas FedEx tras confirmacion. Contacto preferido por WhatsApp.""",
    },
    {
        "id": "ML3_pt_scam_transferencia_chaves",
        "expected": "high",
        "lang": "pt",
        "comment": "Portugais Bresil - propriete Lisbonne falsifiee, virement etranger, FedEx cles.",
        "text": """Aluga-se T1 Bordeaux Saint-Michel 28m2, calmo, todo equipado.
Renda 520€/mes tudo incluso. Caucao 520€.
Estou actualmente em Lisboa, propriedade gerida a distancia.
Pagamento por transferencia Western Union OU Bitcoin (BTC) para conta portuguesa.
Chaves enviadas via FedEx 48h apos confirmacao do pagamento.
Contacto exclusivo Telegram para rapidez.""",
    },
    {
        "id": "ML4_ar_translit_scam_hawala_btc",
        "expected": "high",
        "lang": "ar-translit",
        "comment": "Arabe translittere (Maghreb diaspora) - hawala mention + telegram + paiement avant visite.",
        "text": """Krayet shaqqa Marseille 14eme, 50m2, mojahaza bil meuble.
Lkraa 600€/chhar. Daman 600€.
Ana fi Tunis daba, makanchi nedjbed l Marseille qbel septembre.
Khalas par Western Union wla Bitcoin (BTC). Hawala system kayna had9oula.
Telegram kayn pour les details. Chaves yaslo b FedEx mor lakhlas.""",
    },
    {
        "id": "ML5_it_legit_no_keywords",
        "expected": "safe",
        "lang": "it",
        "comment": "Annonce italophone legitime. Foncia agence FR mention. Doit etre safe meme si scanner connait pas l'italien.",
        "text": """Affitto T2 Nizza Vieux Nice 40mq, ristrutturato 2024, terrazzo.
Affitto 720€/mese + 50€ spese. Cauzione 720€ oppure Visale.
Visite tramite l'agenzia Foncia Nice (12 avenue Jean Medecin, 06000 Nice).
Documenti richiesti : 3 buste paga, contratto, RIB. Firma del contratto in agenzia.
DPE classe C. Disponibile dal 1° agosto 2026.""",
    },
    {
        "id": "ML6_es_legit_agency_visale",
        "expected": "safe",
        "lang": "es",
        "comment": "Espagnol mais agence Century21 + Visale + visite obligatoire. Safe.",
        "text": """Alquilo T3 Montpellier Antigone 70m2, terraza, parking.
Alquiler 980€ + 80€ gastos. Fianza 980€ o garantia Visale.
Visita unicamente con agencia Century 21 Antigone (3 place Vauban, 34000 Montpellier).
Documentos : 3 nominas, contrato, RIB. Firma del contrato en agencia despues del expediente completo.
DPE D. Disponible 15 agosto 2026.""",
    },
]


def post(text):
    body = json.dumps({"text": text}).encode("utf-8")
    req = urllib.request.Request(API, data=body, headers={"Content-Type": "application/json", "User-Agent": "bv-audit-multilang-run166"})
    with urllib.request.urlopen(req, timeout=10) as r:
        return json.loads(r.read().decode("utf-8"))


def main():
    results = []
    for ann in CASES_ML:
        try:
            res = post(ann["text"])
            row = {
                "id": ann["id"],
                "lang": ann["lang"],
                "expected": ann["expected"],
                "got_severity": res.get("severity"),
                "score": res.get("score"),
                "flags_count": len(res.get("flags", [])),
                "flags_labels": [f.get("label") for f in res.get("flags", [])],
                "comment": ann["comment"],
            }
        except Exception as e:
            row = {"id": ann["id"], "lang": ann["lang"], "expected": ann["expected"], "error": str(e)}
        results.append(row)
        time.sleep(0.3)

    tp = fp = tn = fn = 0
    for r in results:
        if "error" in r:
            continue
        is_arn_expected = r["expected"] in ("high", "medium")
        is_arn_predicted = r["got_severity"] in ("high", "medium")
        if is_arn_expected and is_arn_predicted:
            tp += 1
        elif is_arn_expected and not is_arn_predicted:
            fn += 1
        elif not is_arn_expected and is_arn_predicted:
            fp += 1
        else:
            tn += 1

    out = {
        "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "audit_type": "multilang_run166",
        "scanner_version_under_test": "V1.2",
        "n_arnaque": sum(1 for a in CASES_ML if a["expected"] in ("high", "medium")),
        "n_legit": sum(1 for a in CASES_ML if a["expected"] == "safe"),
        "tp": tp, "tn": tn, "fp": fp, "fn": fn,
        "precision_arnaque": round(tp / max(1, tp + fp), 3),
        "recall_arnaque": round(tp / max(1, tp + fn), 3),
        "accuracy": round((tp + tn) / max(1, tp + tn + fp + fn), 3),
        "results": results,
    }
    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
