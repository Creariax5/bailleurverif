#!/usr/bin/env python3
"""
BailleurVérif — serveur HTTP V0
Port 8102. Sert /static + endpoints API /api/visit, /api/result, /api/capture, /api/stats.
Données persistées en JSONL dans data/.
"""
import hashlib
import json
import os
import re
import secrets
import smtplib
import ssl
import sys
import time
import unicodedata
import urllib.parse
import urllib.request
import urllib.error
import logging
from email.message import EmailMessage
from email.utils import formatdate, make_msgid
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(ROOT, "static")
DATA_DIR = os.path.join(ROOT, "data")
INTERPRETATION_LIB_DIR = os.path.normpath(os.path.join(ROOT, "..", "data", "interpretation-library-v0", "recourse-templates"))
os.makedirs(DATA_DIR, exist_ok=True)

VISITS_FILE = os.path.join(DATA_DIR, "visits.jsonl")
RESULTS_FILE = os.path.join(DATA_DIR, "results.jsonl")
STEPS_FILE = os.path.join(DATA_DIR, "steps.jsonl")
CAPTURES_FILE = os.path.join(DATA_DIR, "email-captures.jsonl")
SHARES_FILE = os.path.join(DATA_DIR, "shares.jsonl")
FEEDBACKS_FILE = os.path.join(DATA_DIR, "feedbacks.jsonl")
EMBED_VIEWS_FILE = os.path.join(DATA_DIR, "embed-views.jsonl")
EMBED_COPIES_FILE = os.path.join(DATA_DIR, "embed-snippet-copies.jsonl")
SUBSCRIBERS_FILE = os.path.join(DATA_DIR, "subscribers.jsonl")
CHANGES_FILE = os.path.join(DATA_DIR, "reglementation-changes.jsonl")
SIGNALEMENTS_FILE = os.path.join(DATA_DIR, "signalements-annonces.jsonl")
NOTATIONS_AGENCES_FILE = os.path.join(DATA_DIR, "notations-agences.jsonl")
OUTBOUND_EMAILS_FILE = os.path.join(DATA_DIR, "outbound-emails.jsonl")
FUNNEL_FILE = os.path.join(DATA_DIR, "funnel-events.jsonl")

# Funnel events whitelist — strategic-14 prescription run-330.
# +4 events strategic-16 run-337 : scan_url_* (zero-friction painkiller) + share_card_downloaded (viralité Pilier 1+2).
# +2 events strategic-28 run-373 : scan_url_preset_clicked + share_card_post_scan (critère T+72h 2026-05-30T22:00Z).
# +2 events strategic-29 run-376 : home_preset_click + share_card_post_home (critère T+72h 2026-05-31T10:00Z).
FUNNEL_EVENT_TYPES = {
    "home_visit",
    "wedge_q1_answered",
    "wedge_q2_answered",
    "wedge_q3_answered",
    "wedge_q4_answered",
    "wedge_q5_answered",
    "verdict_displayed",
    "email_field_focused",
    "email_submitted",
    "cta_secondary_clicked",
    "scan_url_page_visit",
    "scan_url_pasted",
    "scan_url_verdict_displayed",
    "scan_url_preset_clicked",
    "share_card_downloaded",
    "share_card_post_scan",
    "home_preset_click",
    "share_card_post_home",
}

# OVH Zimbra SMTP — provisionné Florian 2026-05-17T13:55Z, mandated patch run-205.
# Lu depuis ../.env au démarrage. Si absent, helper retombe sur fallback lien-inline.
def _load_dotenv(path):
    env = {}
    try:
        with open(path) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                v = v.strip()
                if (v.startswith("'") and v.endswith("'")) or (v.startswith('"') and v.endswith('"')):
                    v = v[1:-1]
                env[k.strip()] = v
    except FileNotFoundError:
        pass
    return env

_DOTENV = _load_dotenv(os.path.join(ROOT, "..", ".env"))
SMTP_USERNAME = _DOTENV.get("BAILLEURVERIF_SMTP_USERNAME", "")
SMTP_PASSWORD = _DOTENV.get("BAILLEURVERIF_SMTP_PASSWORD", "")
SMTP_SERVER = _DOTENV.get("BAILLEURVERIF_SMTP_SERVER", "ssl0.ovh.net")
SMTP_PORT = int(_DOTENV.get("BAILLEURVERIF_SMTP_PORT", "465"))
SMTP_USE_SSL = _DOTENV.get("BAILLEURVERIF_SMTP_USE_SSL", "true").lower() == "true"
SMTP_AVAILABLE = bool(SMTP_USERNAME and SMTP_PASSWORD)

# Préfectures / services compétents pour signalement non-conformité location (encadrement + DPE F/G).
# Source : https://www.service-public.fr (DRIHL Île-de-France ; DDETSPP en région ; Métropole de Lyon depuis 2021).
PREFECTURE_BY_DEPT = {
    "75": {"service": "DRIHL Paris", "adresse": "Direction régionale et interdépartementale de l'hébergement et du logement (DRIHL) — Unité départementale de Paris — 5 rue Leblanc, 75015 Paris", "email": "drihl-ud75-encadrement@developpement-durable.gouv.fr"},
    "92": {"service": "DRIHL Hauts-de-Seine", "adresse": "DRIHL — Unité départementale 92 — Cité administrative, 167-177 avenue Frédéric et Irène Joliot-Curie, 92000 Nanterre", "email": "drihl-ud92@developpement-durable.gouv.fr"},
    "93": {"service": "DRIHL Seine-Saint-Denis", "adresse": "DRIHL — Unité départementale 93 — Immeuble L'Européen, 5/7 promenade Jean Rostand, 93005 Bobigny", "email": "drihl-ud93@developpement-durable.gouv.fr"},
    "94": {"service": "DRIHL Val-de-Marne", "adresse": "DRIHL — Unité départementale 94 — 12-14 rue des Archives, 94000 Créteil", "email": "drihl-ud94@developpement-durable.gouv.fr"},
    "69": {"service": "DDETS du Rhône / Métropole de Lyon", "adresse": "Direction Départementale de l'Emploi, du Travail et des Solidarités du Rhône — 33 rue Moncey, 69421 Lyon Cedex 03", "email": "ddets-pole-logement@rhone.gouv.fr"},
    "59": {"service": "DDETS du Nord", "adresse": "Direction Départementale de l'Emploi, du Travail et des Solidarités du Nord — Pôle Logement — Cité administrative, 175 rue Gustave Delory, 59047 Lille Cedex", "email": "ddets-logement@nord.gouv.fr"},
    "13": {"service": "DDETS des Bouches-du-Rhône", "adresse": "DDETS 13 — Pôle Logement — 66A rue Saint-Sébastien, 13006 Marseille", "email": "ddets-logement@bouches-du-rhone.gouv.fr"},
    "44": {"service": "DDETS de Loire-Atlantique", "adresse": "DDETS 44 — Pôle Logement — 9 rue René Viviani, 44062 Nantes Cedex 1", "email": "ddets-logement@loire-atlantique.gouv.fr"},
    "31": {"service": "DDETS de Haute-Garonne", "adresse": "DDETS 31 — Pôle Logement — 1 place Saint-Étienne, 31038 Toulouse Cedex 9", "email": "ddets-logement@haute-garonne.gouv.fr"},
    "33": {"service": "DDETS de Gironde", "adresse": "DDETS 33 — Pôle Logement — 118 cours du Maréchal Juin, 33075 Bordeaux Cedex", "email": "ddets-logement@gironde.gouv.fr"},
}
# Mapping code_postal → code_dept (2 premiers chiffres pour la métropole ; arrondissements Paris/Lyon/Marseille déjà gérés).
def _dept_from_cp(cp):
    if not cp or len(str(cp).strip()) < 2:
        return ""
    cp = str(cp).strip()
    # Paris 75xxx, Marseille 13xxx, Lyon 69xxx — département = 2 premiers chiffres.
    return cp[:2]

PORT = int(os.environ.get("PORT", "8102"))

PUBLIC_BASE = "https://bailleurverif.fr"
SUBSCRIBER_TOPIC_ALLOWED = {"loyer-legal", "dpe-bailleur", "preavis", "veille-reglementaire", "deficit-foncier", "mon-bien", "aides-financieres", "arnaques-location"}
SUBSCRIBER_INTENT_ALLOWED = {"loyer-trop-cher", "arnaque-suspecte", "litige-en-cours", "curiosite", "bailleur-conformite", "bailleur-multi-bien", "bailleur-proprio-unique", "autre"}
EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")

# --- Adresse lookup (Feature B run-124) ---
BAN_BASE = "https://api-adresse.data.gouv.fr"
ADEME_DPE_DATASET = "dpe03existant"  # DPE Logements existants depuis juillet 2021 (slug actif 2026, id meg-83tjwtg8dyz4vv7h1dqe deprecated 404)
ADEME_BASE = "https://data.ademe.fr/data-fair/api/v1/datasets"
LOOKUP_UA = "BailleurVerif/1.0 (+https://bailleurverif.fr; contact@bailleurverif.fr)"
LOOKUP_TIMEOUT_BAN = 6
LOOKUP_TIMEOUT_ADEME = 9
# in-memory cache (ttl-light) keyed by lowercase normalized query — bounded and recycled
_LOOKUP_CACHE = {}  # q -> (ts_epoch, body_dict)
LOOKUP_CACHE_TTL_S = 3600
LOOKUP_CACHE_MAX = 256
# very small rate limit per ip_hash : 30 lookups / 60s
_LOOKUP_RATE = {}  # ip_hash -> [ts_epoch ...]
LOOKUP_RATE_WINDOW_S = 60
LOOKUP_RATE_MAX = 30


def _slugify_commune(s):
    """Lowercase, strip accents, hyphen-separate — must match keys in encadrement-loyer-france-2026.json slug."""
    if not s:
        return ""
    s = unicodedata.normalize("NFD", s)
    s = "".join(ch for ch in s if unicodedata.category(ch) != "Mn")
    s = s.lower().strip()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s


# Built once at import — re-keyed by both commune slug and INSEE citycode where possible.
_ENCADREMENT_MATRIX = {}      # slug -> entry
_ENCADREMENT_BY_CITY = {}     # lowercase normalized city name -> entry

# INSEE arrondissement → core commune slug : Paris/Lyon/Marseille are returned arrondissement-coded by BAN.
_INSEE_ARRONDISSEMENT_TO_COMMUNE = {}
for code in range(75101, 75121):  # Paris
    _INSEE_ARRONDISSEMENT_TO_COMMUNE[str(code)] = "paris"
for code in range(69381, 69390):  # Lyon
    _INSEE_ARRONDISSEMENT_TO_COMMUNE[str(code)] = "lyon"
for code in range(13201, 13217):  # Marseille (non-encadré mais on garde la cohérence)
    _INSEE_ARRONDISSEMENT_TO_COMMUNE[str(code)] = "marseille"

try:
    _enc_path = os.path.join(STATIC_DIR, "data", "encadrement-loyer-france-2026.json")
    with open(_enc_path, "r", encoding="utf-8") as _fp:
        _enc_data = json.load(_fp)
    for _c in _enc_data.get("communes", []):
        _slug = _c.get("slug") or _slugify_commune(_c.get("commune", ""))
        if _slug:
            _ENCADREMENT_MATRIX[_slug] = _c
            _ENCADREMENT_BY_CITY[_slugify_commune(_c.get("commune", ""))] = _c
except Exception as _e:
    sys.stdout.write(f"[ENCADREMENT] load error: {_e}\n")


def _ban_geocode(q):
    """Returns BAN feature properties dict or None."""
    url = f"{BAN_BASE}/search/?" + urllib.parse.urlencode({"q": q, "limit": 1, "autocomplete": 0})
    req = urllib.request.Request(url, headers={"User-Agent": LOOKUP_UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=LOOKUP_TIMEOUT_BAN) as r:
        data = json.loads(r.read())
    feats = data.get("features") or []
    if not feats:
        return None
    f = feats[0]
    props = f.get("properties", {}) or {}
    coords = (f.get("geometry") or {}).get("coordinates") or [None, None]
    return {
        "label": props.get("label"),
        "housenumber": props.get("housenumber"),
        "street": props.get("street") or props.get("name"),
        "postcode": props.get("postcode"),
        "city": props.get("city"),
        "citycode": props.get("citycode"),
        "depcode": props.get("depcode"),
        "district": props.get("district"),
        "context": props.get("context"),
        "lat": coords[1] if len(coords) >= 2 else None,
        "lon": coords[0] if len(coords) >= 2 else None,
        "score": props.get("score"),
        "type": props.get("type"),
    }


def _ademe_dpe_voisinage(postcode, street, citycode=None):
    """Query ADEME DPE dataset by INSEE citycode (preferred) or postcode + street fuzzy match. ADEME WAF blocks code_postal_ban so on prefere code_insee_ban quand citycode est dispo. Returns dict {fetched,total_voisinage,etiquettes,results}."""
    out = {"fetched": False, "total_voisinage": 0, "etiquettes": {}, "results": []}
    if not postcode and not citycode:
        return out
    tokens = []
    if street:
        words = re.findall(r"[A-Za-zÀ-ÿ'\-]+", street)
        for w in words:
            if len(w) >= 4 and w.lower() not in {"rue", "avenue", "boulevard", "chemin", "route", "place", "allee", "allée", "impasse", "saint", "sainte"}:
                tokens.append(w)
        if not tokens:
            tokens = [w for w in words if len(w) >= 3]
    q_street = tokens[-1] if tokens else ""
    if citycode:
        qs_filter = f"code_insee_ban:{citycode}"
    else:
        qs_filter = f"code_postal_ban:\"{postcode}\""
    params = {
        "qs": qs_filter,
        "size": 12,
        "select": "numero_voie_ban,nom_rue_ban,code_postal_ban,code_insee_ban,etiquette_dpe,etiquette_ges,surface_habitable_logement,date_etablissement_dpe,type_batiment,conso_5_usages_par_m2_ep",
        "sort": "-date_etablissement_dpe",
    }
    if q_street:
        params["q"] = q_street
        params["q_fields"] = "nom_rue_ban"
    url = f"{ADEME_BASE}/{ADEME_DPE_DATASET}/lines?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    req = urllib.request.Request(url, headers={"User-Agent": LOOKUP_UA, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=LOOKUP_TIMEOUT_ADEME) as r:
            data = json.loads(r.read())
    except Exception as e:
        out["error"] = f"ademe_unreachable: {str(e)[:120]}"
        return out
    out["fetched"] = True
    out["total_voisinage"] = int(data.get("total") or 0)
    from collections import Counter
    res = data.get("results") or []
    etiq = Counter()
    for item in res[:12]:
        et = item.get("etiquette_dpe")
        if et:
            etiq[et] += 1
        out["results"].append({
            "numero": item.get("numero_voie_ban"),
            "rue": item.get("nom_rue_ban"),
            "postcode": item.get("code_postal_ban"),
            "etiquette_dpe": et,
            "etiquette_ges": item.get("etiquette_ges"),
            "surface_m2": item.get("surface_habitable_logement"),
            "date_dpe": item.get("date_etablissement_dpe"),
            "type_batiment": item.get("type_batiment"),
            "conso_kwh_m2_an": item.get("conso_5_usages_par_m2_ep"),
        })
    out["etiquettes"] = dict(etiq)
    return out


def _commune_lookup_encadrement(address):
    """Returns the encadrement matrix entry that matches the BAN address, or None."""
    citycode = (address or {}).get("citycode") or ""
    # Arrondissement → commune
    if citycode in _INSEE_ARRONDISSEMENT_TO_COMMUNE:
        slug = _INSEE_ARRONDISSEMENT_TO_COMMUNE[citycode]
        if slug in _ENCADREMENT_MATRIX:
            return _ENCADREMENT_MATRIX[slug]
    city = (address or {}).get("city") or ""
    key = _slugify_commune(city)
    if key in _ENCADREMENT_MATRIX:
        return _ENCADREMENT_MATRIX[key]
    if key in _ENCADREMENT_BY_CITY:
        return _ENCADREMENT_BY_CITY[key]
    return None


def _build_verdicts(address, encadrement, dpe):
    """Build human-readable verdicts list from lookup data."""
    verdicts = []
    if encadrement:
        verdicts.append({
            "kind": "encadrement",
            "severity": "warn",
            "title": f"Encadrement des loyers applicable — {encadrement.get('commune')}",
            "text": (
                f"Plafond loyer nu : {encadrement.get('plafond_nu_eur_m2')} €/m². "
                f"Plafond meublé : {encadrement.get('plafond_meuble_eur_m2')} €/m². "
                f"En vigueur depuis le {encadrement.get('date_debut_encadrement')}. "
                f"Autorité : {encadrement.get('autorite_prefectorale')}."
            ),
            "source": f"{PUBLIC_BASE}/encadrement-loyer-{encadrement.get('slug')}-2026.html" if encadrement.get('slug') in _ENCADREMENT_MATRIX else f"{PUBLIC_BASE}/data/",
        })
    else:
        verdicts.append({
            "kind": "encadrement",
            "severity": "ok",
            "title": "Pas d'encadrement des loyers à cette adresse",
            "text": "Aucun arrêté préfectoral d'encadrement n'est en vigueur sur la commune (mai 2026, 31 communes couvertes).",
            "source": f"{PUBLIC_BASE}/data/",
        })
    if dpe.get("fetched"):
        et = dpe.get("etiquettes") or {}
        fg = (et.get("F") or 0) + (et.get("G") or 0)
        tot = sum(et.values()) or 0
        if tot == 0:
            verdicts.append({
                "kind": "dpe_voisinage",
                "severity": "info",
                "title": "Aucun DPE public à cette rue",
                "text": "Aucun diagnostic dans la base ADEME pour cette rue/code postal. Cela ne signifie pas l'absence de DPE — seulement qu'aucun n'est encore publié.",
                "source": "https://data.ademe.fr/datasets/dpe-v2-logements-existants",
            })
        elif fg > 0:
            verdicts.append({
                "kind": "dpe_voisinage",
                "severity": "danger",
                "title": f"{fg} logement·s classé·s F ou G dans le voisinage ({fg}/{tot} DPE relevés)",
                "text": (
                    "Calendrier d'interdiction de mise en location : "
                    "G interdit depuis le 1ᵉʳ janvier 2025, F à partir du 1ᵉʳ janvier 2028, E à partir du 1ᵉʳ janvier 2034. "
                    "Si votre bien est dans le même immeuble, il est probable qu'il soit également F ou G."
                ),
                "source": f"{PUBLIC_BASE}/blog/guide-passoires-thermiques-rentabilite-bailleur-2026.html",
            })
        else:
            verdicts.append({
                "kind": "dpe_voisinage",
                "severity": "ok",
                "title": f"Voisinage majoritairement performant ({tot} DPE relevés)",
                "text": "Aucun logement F ou G dans les DPE publics du voisinage. Bonne base de comparaison.",
                "source": "https://data.ademe.fr/datasets/dpe-v2-logements-existants",
            })
    else:
        verdicts.append({
            "kind": "dpe_voisinage",
            "severity": "info",
            "title": "DPE voisinage non récupéré",
            "text": dpe.get("error") or "Pas de connexion à la base ADEME ce moment-ci. Réessayez dans quelques minutes.",
            "source": "https://data.ademe.fr/datasets/dpe-v2-logements-existants",
        })
    return verdicts

MIME = {
    ".html": "text/html; charset=utf-8",
    ".js": "application/javascript; charset=utf-8",
    ".css": "text/css; charset=utf-8",
    ".json": "application/json; charset=utf-8",
    ".xml": "application/xml; charset=utf-8",
    ".svg": "image/svg+xml",
    ".png": "image/png",
    ".ico": "image/x-icon",
    ".txt": "text/plain; charset=utf-8",
    ".csv": "text/csv; charset=utf-8",
    ".md": "text/markdown; charset=utf-8",
    ".cff": "text/yaml; charset=utf-8",
}

def send_signup_confirmation(email, confirm_url, unsub_url, topic):
    """Send confirmation email via OVH SMTP. Return (ok, error_or_msgid).
    Florian-mandated patch run-205. Graceful degradation if SMTP down."""
    if not SMTP_AVAILABLE:
        return False, "smtp_unconfigured"
    topic_label = {
        "loyer-legal": "encadrement loyer",
        "dpe-bailleur": "DPE bailleur",
        "preavis": "préavis",
        "veille-reglementaire": "veille réglementaire",
        "deficit-foncier": "déficit foncier",
        "mon-bien": "mon bien",
        "aides-financieres": "aides financières",
        "arnaques-location": "arnaques location",
    }.get(topic, topic)
    body = (
        "Bonjour,\n\n"
        f"Vous venez de demander l'inscription à BailleurVérif (sujet : {topic_label}).\n\n"
        "Pour confirmer votre inscription, cliquez sur ce lien (ou copiez-le dans votre navigateur) :\n\n"
        f"{confirm_url}\n\n"
        "Ce lien expire dans 7 jours. Si vous n'êtes pas à l'origine de cette demande, ignorez ce message — "
        "aucun email supplémentaire ne vous sera envoyé.\n\n"
        "Pour vous désinscrire à tout moment, utilisez ce lien (un clic suffit, RGPD art. 17) :\n"
        f"{unsub_url}\n\n"
        "— L'équipe BailleurVérif\n"
        "https://bailleurverif.fr — observatoire ouvert des annonces non-conformes\n"
        "contact@bailleurverif.fr\n"
    )
    msg = EmailMessage()
    msg["From"] = f"BailleurVérif <{SMTP_USERNAME}>"
    msg["To"] = email
    msg["Reply-To"] = SMTP_USERNAME
    msg["Subject"] = f"Confirmez votre inscription BailleurVérif ({topic_label})"
    msg["Date"] = formatdate(localtime=False)
    msg["Message-ID"] = make_msgid(domain="bailleurverif.fr")
    msg["List-Unsubscribe"] = f"<{unsub_url}>"
    msg["List-Unsubscribe-Post"] = "List-Unsubscribe=One-Click"
    msg["X-Mailer"] = "BailleurVerif-server/run-205"
    msg.set_content(body)
    try:
        if SMTP_USE_SSL:
            ctx = ssl.create_default_context()
            with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=ctx, timeout=15) as smtp:
                smtp.login(SMTP_USERNAME, SMTP_PASSWORD)
                smtp.send_message(msg)
        else:
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=15) as smtp:
                smtp.starttls(context=ssl.create_default_context())
                smtp.login(SMTP_USERNAME, SMTP_PASSWORD)
                smtp.send_message(msg)
        return True, msg["Message-ID"]
    except Exception as exc:
        return False, f"{type(exc).__name__}: {exc}"


def now_iso():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")

def append_jsonl(path, record):
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")

def read_jsonl(path):
    if not os.path.exists(path):
        return []
    out = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return out

def compute_subscriber_state(events):
    """Replay event stream → dict[token] = {email, topic, source, status, ts_*, referrer_token, referrals}.

    `referrals` = count of CONFIRMED downstream subscribers whose `referrer_token` == this token.
    """
    state = {}
    referred_by = {}
    for ev in events:
        tok = ev.get("token")
        if not tok:
            continue
        t = ev.get("type")
        if t == "subscribe":
            state.setdefault(tok, {
                "email": ev.get("email"),
                "topic": ev.get("topic"),
                "source": ev.get("source"),
                "status": "pending",
                "ts_subscribe": ev.get("ts"),
                "ts_confirm": None,
                "ts_unsubscribe": None,
                "referrer_token": ev.get("referrer_token") or None,
                "referrals": 0,
                "intent_signal": ev.get("intent_signal") or None,
            })
            rt = ev.get("referrer_token")
            if rt:
                referred_by[tok] = rt
        elif t == "confirm" and tok in state:
            if state[tok]["status"] == "pending":
                state[tok]["status"] = "confirmed"
                state[tok]["ts_confirm"] = ev.get("ts")
        elif t == "unsubscribe" and tok in state:
            state[tok]["status"] = "unsubscribed"
            state[tok]["ts_unsubscribe"] = ev.get("ts")
    for child, parent in referred_by.items():
        if child in state and state[child]["status"] == "confirmed" and parent in state:
            state[parent]["referrals"] += 1
    return state


SUBSCRIBE_PAGE_CSS = """body{font-family:system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;background:#f8fafc;color:#0f172a;margin:0;padding:48px 24px;line-height:1.5}.card{max-width:560px;margin:0 auto;background:#fff;border:1px solid #e2e8f0;border-radius:16px;padding:32px;box-shadow:0 1px 2px rgba(15,23,42,.04)}h1{font-size:22px;margin:0 0 12px;color:#0f172a}p{margin:8px 0;color:#334155}.ok{color:#15803d}.warn{color:#b45309}.bad{color:#b91c1c}.muted{font-size:13px;color:#64748b}a{color:#1d4ed8;text-decoration:underline}.brand{font-size:12px;text-transform:uppercase;letter-spacing:.15em;color:#1d4ed8;margin-bottom:8px}"""


def _referral_block_html(ref_url, ref_count):
    """Bloc HTML inline pour le hub partage personnel (referral)."""
    return (
        "<div style=\"margin:18px 0;padding:14px 16px;background:#f1f5f9;border:1px solid #cbd5e1;border-radius:10px\">"
        "<p style=\"margin:0 0 6px;font-weight:600;color:#0f172a\">Parrainez d'autres bailleurs ou locataires</p>"
        f"<p style=\"margin:0 0 8px;color:#334155;font-size:14px\">Partagez ce lien : chaque inscription confirmée est créditée à votre compte. Compteur actuel : <strong>{ref_count}</strong>.</p>"
        f"<input id=\"bv-ref-url\" type=\"text\" readonly value=\"{ref_url}\" "
        "style=\"width:100%;box-sizing:border-box;padding:8px 10px;border:1px solid #cbd5e1;border-radius:6px;font-family:ui-monospace,Menlo,monospace;font-size:13px;background:#fff;color:#0f172a\">"
        "<div style=\"margin-top:8px;display:flex;gap:8px;flex-wrap:wrap\">"
        f"<a href=\"https://wa.me/?text={_url_encode(ref_url)}\" target=\"_blank\" rel=\"noopener\" style=\"font-size:13px;padding:6px 10px;background:#25d366;color:#fff;border-radius:6px;text-decoration:none\">WhatsApp</a>"
        f"<a href=\"mailto:?subject=BailleurVerif%20%E2%80%94%20alertes%20r%C3%A9glementaires&body={_url_encode(ref_url)}\" style=\"font-size:13px;padding:6px 10px;background:#1d4ed8;color:#fff;border-radius:6px;text-decoration:none\">Email</a>"
        "<button type=\"button\" id=\"bv-ref-copy\" style=\"font-size:13px;padding:6px 10px;background:#0f172a;color:#fff;border:0;border-radius:6px;cursor:pointer\">Copier le lien</button>"
        "</div>"
        "<script>(function(){var b=document.getElementById('bv-ref-copy');var i=document.getElementById('bv-ref-url');"
        "if(!b||!i)return;b.addEventListener('click',function(){try{i.select();navigator.clipboard.writeText(i.value);b.textContent='Copié \\u2713';}catch(e){i.select();document.execCommand('copy');b.textContent='Copié \\u2713';}});})();</script>"
        "</div>"
    )


def _url_encode(s):
    """Encodage URL-percent simple pour les liens de partage (helper local pour éviter import sur la chaîne chaude)."""
    from urllib.parse import quote
    return quote(s, safe="")


def html_subscribe_page(title, status_class, h1, body_html):
    return (
        "<!doctype html><html lang=\"fr\"><head><meta charset=\"utf-8\">"
        "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"
        "<meta name=\"robots\" content=\"noindex,nofollow\">"
        f"<title>{title} — BailleurVérif</title>"
        f"<style>{SUBSCRIBE_PAGE_CSS}</style></head>"
        "<body><main class=\"card\">"
        "<div class=\"brand\">BailleurVérif</div>"
        f"<h1 class=\"{status_class}\">{h1}</h1>"
        f"{body_html}"
        "<p class=\"muted\">RGPD : vos données ne sont jamais partagées. Aucun cookie tiers. "
        "<a href=\"/politique-confidentialite.html\">Politique de confidentialité</a>.</p>"
        "<p class=\"muted\"><a href=\"/\">← Retour à BailleurVérif</a></p>"
        "</main></body></html>"
    )


def safe_static(path):
    """Resolve a static path under STATIC_DIR safely."""
    rel = path.lstrip("/").replace("static/", "", 1) if path.startswith("/static/") else path.lstrip("/")
    abs_path = os.path.realpath(os.path.join(STATIC_DIR, rel))
    if not abs_path.startswith(STATIC_DIR):
        return None
    if os.path.isdir(abs_path):
        abs_path = os.path.join(abs_path, "index.html")
    if not os.path.isfile(abs_path):
        return None
    return abs_path

class Handler(BaseHTTPRequestHandler):
    server_version = "BailleurVerif/0.1"

    def log_message(self, fmt, *args):
        try:
            xff = self.headers.get("X-Forwarded-For", "") if getattr(self, "headers", None) else ""
            client_ip = xff.split(",")[0].strip() if xff else self.client_address[0]
            ua = (self.headers.get("User-Agent", "") if getattr(self, "headers", None) else "")[:120]
        except Exception:
            client_ip = self.client_address[0]
            ua = ""
        sys.stdout.write("[%s] %s - %s ua=%r\n" % (now_iso(), client_ip, fmt % args, ua))
        sys.stdout.flush()

    def _send(self, status, body, ctype="application/json; charset=utf-8", extra_headers=None):
        if isinstance(body, (dict, list)):
            body = json.dumps(body, ensure_ascii=False).encode("utf-8")
        elif isinstance(body, str):
            body = body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store" if ctype.startswith("application/json") else "public, max-age=300")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "strict-origin-when-cross-origin")
        if extra_headers:
            for k, v in extra_headers.items():
                self.send_header(k, v)
        self.end_headers()
        if not getattr(self, "_head_only", False):
            self.wfile.write(body)

    def do_HEAD(self):
        self._head_only = True
        try:
            self.do_GET()
        finally:
            self._head_only = False

    def _client_ip(self):
        return self.headers.get("X-Forwarded-For", self.client_address[0]).split(",")[0].strip()

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path

        if path == "/index.html":
            self.send_response(301)
            self.send_header("Location", "/")
            self.send_header("Cache-Control", "public, max-age=86400")
            self.end_headers()
            return

        if path == "/":
            f = safe_static("/index.html")
            if f:
                with open(f, "rb") as fp:
                    self._send(200, fp.read(), ctype=MIME[".html"])
                return
            self._send(404, "not found", ctype="text/plain; charset=utf-8")
            return

        if path.startswith("/static/"):
            f = safe_static(path)
            if f:
                ext = os.path.splitext(f)[1]
                with open(f, "rb") as fp:
                    self._send(200, fp.read(), ctype=MIME.get(ext, "application/octet-stream"))
                return
            self._send(404, "not found", ctype="text/plain; charset=utf-8")
            return

        if path == "/api/stats":
            try:
                visits = read_jsonl(VISITS_FILE)
                results = read_jsonl(RESULTS_FILE)
                captures = read_jsonl(CAPTURES_FILE)
                shares = read_jsonl(SHARES_FILE)
                feedbacks = read_jsonl(FEEDBACKS_FILE)
                visits_total = len(visits)
                # unique by sessionId
                visits_unique = len({v.get("sessionId") for v in visits if v.get("sessionId")})
                results_total = len(results)
                captures_total = len(captures)
                captures_report = sum(1 for c in captures if c.get("kind") == "report")
                captures_watch = sum(1 for c in captures if c.get("kind") == "watch")
                conv_email_pct = round(100 * captures_total / max(visits_unique, 1), 1)
                shares_total = len(shares)
                shares_unique_sessions = len({s.get("sessionId") for s in shares if s.get("sessionId")})
                share_rate_pct = round(100 * shares_unique_sessions / max(visits_unique, 1), 1)
                # severity breakdown
                sev = {"ok": 0, "warn": 0, "danger": 0}
                for r in results:
                    s = r.get("severity")
                    if s in sev:
                        sev[s] += 1
                # top cities
                from collections import Counter
                villes = Counter([r.get("answers", {}).get("ville", "") for r in results if r.get("answers", {}).get("ville")])
                top_villes = villes.most_common(5)
                # share channels
                channels = Counter([s.get("channel", "") for s in shares if s.get("channel")])
                share_channels = channels.most_common(5)
                # referrals (visits with referrer = wedge share marker)
                referrals_from_share = sum(1 for v in visits if "src=share" in (v.get("referrer") or ""))
                feedbacks_total = len(feedbacks)
                feedbacks_with_email = sum(1 for fb in feedbacks if fb.get("email"))
                # signalements observatoire (V1 run-196)
                signalements = read_jsonl(SIGNALEMENTS_FILE)
                signalements_total = len(signalements)
                _now = datetime.now(timezone.utc)
                signalements_30d = 0
                signalements_by_dept = {}
                for s in signalements:
                    try:
                        ts = datetime.fromisoformat(s.get("ts", "").replace("Z", "+00:00"))
                        if (_now - ts).total_seconds() < 30 * 86400:
                            signalements_30d += 1
                    except Exception:
                        pass
                    d = s.get("dept") or "??"
                    signalements_by_dept[d] = signalements_by_dept.get(d, 0) + 1
                # subscribers double-opt-in
                sub_events = read_jsonl(SUBSCRIBERS_FILE)
                sub_state = compute_subscriber_state(sub_events)
                subscribers_pending = sum(1 for e in sub_state.values() if e["status"] == "pending")
                subscribers_confirmed = sum(1 for e in sub_state.values() if e["status"] == "confirmed")
                subscribers_unsubscribed = sum(1 for e in sub_state.values() if e["status"] == "unsubscribed")
                subscribers_by_intent = {}
                for e in sub_state.values():
                    if e["status"] == "unsubscribed":
                        continue
                    isig = e.get("intent_signal") or "unset"
                    subscribers_by_intent[isig] = subscribers_by_intent.get(isig, 0) + 1
                referrals_total = sum(e.get("referrals", 0) for e in sub_state.values())
                referrals_top = sum(1 for e in sub_state.values() if e.get("referrals", 0) > 0)
                # signups_24h = confirmed events whose ts_confirm is within 24h
                now_dt = datetime.now(timezone.utc)
                signups_24h = 0
                for e in sub_state.values():
                    if e["status"] == "confirmed" and e.get("ts_confirm"):
                        try:
                            ts = datetime.fromisoformat(e["ts_confirm"].replace("Z", "+00:00"))
                            if (now_dt - ts).total_seconds() < 86400:
                                signups_24h += 1
                        except Exception:
                            pass
                self._send(200, {
                    "visits_total": visits_total,
                    "visits_unique": visits_unique,
                    "results_total": results_total,
                    "captures_total": captures_total,
                    "captures_report": captures_report,
                    "captures_watch": captures_watch,
                    "conv_email_pct": conv_email_pct,
                    "shares_total": shares_total,
                    "shares_unique_sessions": shares_unique_sessions,
                    "share_rate_pct": share_rate_pct,
                    "share_channels": share_channels,
                    "referrals_from_share": referrals_from_share,
                    "feedbacks_total": feedbacks_total,
                    "feedbacks_with_email": feedbacks_with_email,
                    "subscribers_pending": subscribers_pending,
                    "subscribers_confirmed": subscribers_confirmed,
                    "subscribers_unsubscribed": subscribers_unsubscribed,
                    "subscribers_by_intent": subscribers_by_intent,
                    "signups_24h": signups_24h,
                    "referrals_total": referrals_total,
                    "referrers_count": referrals_top,
                    "severity": sev,
                    "top_villes": top_villes,
                    "go_no_go_threshold_pct": 20,
                    "go_no_go_status": "go" if conv_email_pct >= 20 and visits_unique >= 100 else ("pivot" if conv_email_pct < 5 and visits_unique >= 100 else "collecting"),
                    "signalements_total": signalements_total,
                    "signalements_30d": signalements_30d,
                    "signalements_by_dept": signalements_by_dept,
                    "updated_at": now_iso()
                })
            except Exception as e:
                self._send(500, {"ok": False, "error": str(e)})
            return

        if path == "/healthz":
            self._send(200, {"ok": True, "service": "BailleurVerif", "time": now_iso()})
            return

        if path == "/api/funnel/agg":
            try:
                events = read_jsonl(FUNNEL_FILE)
            except Exception:
                events = []
            now_dt = datetime.now(timezone.utc)
            h24_ago = now_dt.timestamp() - 86400
            by_type_24h = {}
            by_type_lifetime = {}
            sessions_24h = set()
            sessions_lifetime = set()
            session_max_event = {}
            for e in events:
                et = e.get("event_type")
                if not et:
                    continue
                sid = e.get("sessionId") or ""
                by_type_lifetime[et] = by_type_lifetime.get(et, 0) + 1
                sessions_lifetime.add(sid)
                try:
                    ts_str = (e.get("ts") or "").replace("Z", "+00:00")
                    ts = datetime.fromisoformat(ts_str).timestamp()
                except Exception:
                    ts = 0
                if ts >= h24_ago:
                    by_type_24h[et] = by_type_24h.get(et, 0) + 1
                    sessions_24h.add(sid)
                session_max_event.setdefault(sid, set()).add(et)
            funnel_order = [
                "home_visit", "wedge_q1_answered", "wedge_q2_answered",
                "wedge_q3_answered", "wedge_q4_answered", "wedge_q5_answered",
                "verdict_displayed", "email_field_focused", "email_submitted",
            ]
            sessions_reaching = {}
            for et in funnel_order:
                count = sum(1 for sid, evs in session_max_event.items() if et in evs)
                sessions_reaching[et] = count
            by_utm_source_lifetime = {}
            for e in events:
                src = str((e.get("meta") or {}).get("utm_source") or "direct").lower()[:32]
                if "chatgpt" in src or src == "gpt": bucket = "chatgpt"
                elif "perplexity" in src: bucket = "perplexity"
                elif "claude" in src: bucket = "claude"
                elif "gemini" in src or "google" in src: bucket = "google"
                elif "linkedin" in src: bucket = "linkedin"
                else: bucket = src or "direct"
                by_utm_source_lifetime[bucket] = by_utm_source_lifetime.get(bucket, 0) + 1
            self._send(200, {
                "ok": True,
                "events_total_lifetime": len(events),
                "sessions_lifetime": len(sessions_lifetime),
                "sessions_24h": len(sessions_24h),
                "by_type_24h": by_type_24h,
                "by_type_lifetime": by_type_lifetime,
                "sessions_reaching_step_lifetime": sessions_reaching,
                "by_utm_source_lifetime": by_utm_source_lifetime,
                "updated_at": now_iso(),
            })
            return

        if path == "/api/embed/view":
            qs = parse_qs(parsed.query or "")
            tool = (qs.get("w", [""])[0] or "").strip().lower()[:32]
            ville = (qs.get("v", [""])[0] or "").strip().lower()[:64]
            dpe = (qs.get("d", [""])[0] or "").strip().upper()[:4]
            ref = self.headers.get("Referer", "")[:300]
            ua = self.headers.get("User-Agent", "")[:200]
            ip = self.client_address[0]
            rec = {
                "ts": now_iso(),
                "tool": tool,
                "ville": ville,
                "dpe": dpe,
                "referrer": ref,
                "ip_hash": str(abs(hash(ip)) % (10**10)),
                "ua": ua
            }
            try:
                append_jsonl(EMBED_VIEWS_FILE, rec)
            except Exception:
                pass
            gif = b"GIF89a\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00!\xf9\x04\x01\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;"
            self._send(200, gif, ctype="image/gif")
            return

        if path == "/api/changelog":
            qs = parse_qs(parsed.query or "")
            topic_filter = (qs.get("topic", [""])[0] or "").strip().lower()
            try:
                limit = max(1, min(200, int(qs.get("limit", ["50"])[0])))
            except (TypeError, ValueError):
                limit = 50
            entries = read_jsonl(CHANGES_FILE)
            # Tri descendant par date_publi (lexicographique YYYY-MM-DD safe), fallback ts_detected.
            entries.sort(key=lambda e: (e.get("date_publi") or "", e.get("ts_detected") or ""), reverse=True)
            if topic_filter and topic_filter != "all":
                if topic_filter not in SUBSCRIBER_TOPIC_ALLOWED:
                    self._send(400, {"ok": False, "error": "unknown topic"})
                    return
                entries = [e for e in entries if topic_filter in (e.get("topics") or [])]
            try:
                state_path = os.path.join(DATA_DIR, "jorf_poll_state.json")
                poll_state = json.load(open(state_path)) if os.path.exists(state_path) else {}
            except Exception:
                poll_state = {}
            self._send(200, {
                "ok": True,
                "topic": topic_filter or "all",
                "count": len(entries[:limit]),
                "total_matching": len(entries),
                "entries": entries[:limit],
                "poll_state": {
                    "last_run_at": poll_state.get("last_run_at"),
                    "runs_lifetime": poll_state.get("runs_lifetime"),
                    "tarballs_seen_lifetime": len(poll_state.get("last_seen_tarballs", [])),
                },
                "source": "Journal Officiel — DILA OPENDATA (Etalab gouv.fr)",
                "fetched_at": now_iso(),
            })
            return

        if path == "/api/observatoire-dpe-fg":
            qs = parse_qs(parsed.query or "")
            insee_f = (qs.get("insee", [""])[0] or "").strip()
            try:
                limit = max(1, min(200, int(qs.get("limit", ["50"])[0])))
            except (TypeError, ValueError):
                limit = 50
            rollup_path = os.path.join(DATA_DIR, "dpe-fg-rollup.json")
            state_path = os.path.join(DATA_DIR, "dpe_fg_poll_state.json")
            stream_path = os.path.join(DATA_DIR, "dpe-fg-stream.jsonl")
            try:
                rollup = json.load(open(rollup_path)) if os.path.exists(rollup_path) else {"total": 0, "by_commune": {}, "by_etiquette": {}}
            except Exception:
                rollup = {"total": 0, "by_commune": {}, "by_etiquette": {}}
            try:
                state = json.load(open(state_path)) if os.path.exists(state_path) else {}
            except Exception:
                state = {}
            latest = []
            if os.path.exists(stream_path):
                try:
                    with open(stream_path, "r", encoding="utf-8") as f:
                        lines = f.readlines()
                except Exception:
                    lines = []
                pool = []
                tail = lines[-2000:] if len(lines) > 2000 else lines
                for line in tail:
                    try:
                        rec = json.loads(line)
                    except Exception:
                        continue
                    if insee_f and (rec.get("code_insee_ban") or "") != insee_f:
                        continue
                    pool.append(rec)
                pool.sort(key=lambda r: (r.get("date_etablissement_dpe") or "", r.get("_seen_at") or ""), reverse=True)
                latest = pool[:limit]
            commune_items = []
            for ins, row in (rollup.get("by_commune") or {}).items():
                f = int(row.get("F", 0) or 0)
                g = int(row.get("G", 0) or 0)
                commune_items.append({
                    "insee": ins,
                    "commune": row.get("commune"),
                    "F": f,
                    "G": g,
                    "total": f + g,
                    "last_seen": row.get("last_seen"),
                })
            commune_items.sort(key=lambda x: -x["total"])
            self._send(200, {
                "ok": True,
                "rollup": {
                    "total": rollup.get("total"),
                    "by_etiquette": rollup.get("by_etiquette"),
                    "generated_at": rollup.get("generated_at"),
                    "commune_count": len(rollup.get("by_commune") or {}),
                    "by_commune_top": commune_items[:20],
                },
                "poll_state": {
                    "first_run_at": state.get("first_run_at"),
                    "last_run_at": state.get("last_run_at"),
                    "runs_lifetime": state.get("runs_lifetime"),
                },
                "filter_insee": insee_f or None,
                "count": len(latest),
                "latest": latest,
                "source": "ADEME — data.ademe.fr/datasets/dpe03existant (Licence Ouverte Etalab 2.0)",
                "fetched_at": now_iso(),
            })
            return

        if path == "/api/lookup-adresse":
            qs = parse_qs(parsed.query or "")
            q = (qs.get("q", [""])[0] or "").strip()
            if not q or len(q) < 4 or len(q) > 200:
                self._send(400, {"ok": False, "error": "query length must be 4..200"})
                return
            ip_hash = str(abs(hash(self._client_ip())) % (10**10))
            now_ts = time.time()
            bucket = _LOOKUP_RATE.setdefault(ip_hash, [])
            bucket[:] = [t for t in bucket if t > now_ts - LOOKUP_RATE_WINDOW_S]
            if len(bucket) >= LOOKUP_RATE_MAX:
                self._send(429, {"ok": False, "error": "rate limited"})
                return
            bucket.append(now_ts)
            cache_key = q.lower()
            cached = _LOOKUP_CACHE.get(cache_key)
            if cached and (now_ts - cached[0]) < LOOKUP_CACHE_TTL_S:
                self._send(200, dict(cached[1], cache_hit=True))
                return
            try:
                address = _ban_geocode(q)
            except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
                self._send(502, {"ok": False, "error": f"ban_unreachable: {str(e)[:120]}"})
                return
            except Exception as e:
                self._send(500, {"ok": False, "error": f"ban_error: {str(e)[:120]}"})
                return
            if not address:
                self._send(404, {"ok": False, "error": "address not found", "q": q})
                return
            encadrement = _commune_lookup_encadrement(address)
            dpe = _ademe_dpe_voisinage(address.get("postcode"), address.get("street"), citycode=address.get("citycode"))
            verdicts = _build_verdicts(address, encadrement, dpe)
            body = {
                "ok": True,
                "address": address,
                "encadrement_loyer": (
                    {
                        "applicable": True,
                        "commune": encadrement.get("commune"),
                        "slug": encadrement.get("slug"),
                        "plafond_nu_eur_m2": encadrement.get("plafond_nu_eur_m2"),
                        "plafond_meuble_eur_m2": encadrement.get("plafond_meuble_eur_m2"),
                        "perimetre": encadrement.get("perimetre"),
                        "date_debut": encadrement.get("date_debut_encadrement"),
                        "autorite": encadrement.get("autorite_prefectorale"),
                        "intercommunalite": encadrement.get("intercommunalite"),
                    } if encadrement else {"applicable": False}
                ),
                "dpe_voisinage": dpe,
                "verdicts": verdicts,
                "sources": {
                    "geocoding": "BAN — api-adresse.data.gouv.fr (Etalab gouv.fr)",
                    "dpe": "ADEME — data.ademe.fr (dpe-v2-logements-existants, depuis juillet 2021)",
                    "encadrement_loyer": "Arrêtés préfectoraux 2026 — bailleurverif.fr/data (CC-BY-4.0)",
                },
                "fetched_at": now_iso(),
                "cache_hit": False,
            }
            # bounded cache write
            if len(_LOOKUP_CACHE) >= LOOKUP_CACHE_MAX:
                # evict oldest 25%
                stale = sorted(_LOOKUP_CACHE.items(), key=lambda kv: kv[1][0])[: LOOKUP_CACHE_MAX // 4]
                for k, _ in stale:
                    _LOOKUP_CACHE.pop(k, None)
            _LOOKUP_CACHE[cache_key] = (now_ts, body)
            sys.stdout.write("[%s] LOOKUP_ADRESSE q=%s city=%s enc=%s dpe_n=%d\n" %
                             (now_iso(), q[:40], (address.get("city") or "")[:30],
                              "yes" if encadrement else "no", len(dpe.get("results", []))))
            sys.stdout.flush()
            self._send(200, body)
            return

        if path == "/api/confirm":
            qs = parse_qs(parsed.query or "")
            token = (qs.get("token", [""])[0] or "").strip()
            if not token or len(token) > 96 or not re.match(r"^[A-Za-z0-9_-]+$", token):
                body = html_subscribe_page("Lien invalide", "bad", "Lien invalide",
                    "<p>Ce lien de confirmation n'est pas valide. Vérifiez l'URL ou ré-inscrivez-vous depuis la page d'origine.</p>")
                self._send(400, body, ctype="text/html; charset=utf-8")
                return
            events = read_jsonl(SUBSCRIBERS_FILE)
            state = compute_subscriber_state(events)
            entry = state.get(token)
            if not entry:
                body = html_subscribe_page("Lien introuvable", "bad", "Lien introuvable",
                    "<p>Aucune inscription ne correspond à ce lien.</p>")
                self._send(404, body, ctype="text/html; charset=utf-8")
                return
            if entry["status"] == "confirmed":
                unsub_url = f"{PUBLIC_BASE}/api/unsubscribe?token={token}"
                ref_url = f"{PUBLIC_BASE}/?ref={token}"
                ref_count = entry.get("referrals", 0)
                body = html_subscribe_page("Déjà confirmé", "ok", "Inscription déjà confirmée ✓",
                    f"<p>L'adresse <strong>{entry['email']}</strong> est déjà inscrite aux alertes <em>{entry['topic']}</em>.</p>"
                    + _referral_block_html(ref_url, ref_count)
                    + f"<p class=\"muted\">Pour vous désinscrire : <a href=\"{unsub_url}\">cliquez ici</a>.</p>")
                self._send(200, body, ctype="text/html; charset=utf-8")
                return
            if entry["status"] == "unsubscribed":
                body = html_subscribe_page("Désinscrit", "warn", "Vous êtes désinscrit",
                    f"<p>L'adresse <strong>{entry['email']}</strong> a été désinscrite. Ré-inscrivez-vous depuis la page d'origine si besoin.</p>")
                self._send(200, body, ctype="text/html; charset=utf-8")
                return
            append_jsonl(SUBSCRIBERS_FILE, {"ts": now_iso(), "type": "confirm", "token": token})
            unsub_url = f"{PUBLIC_BASE}/api/unsubscribe?token={token}"
            ref_url = f"{PUBLIC_BASE}/?ref={token}"
            # Comptage referrals après l'event confirm (juste écrit) — recompute state.
            fresh_state = compute_subscriber_state(read_jsonl(SUBSCRIBERS_FILE))
            ref_count = fresh_state.get(token, {}).get("referrals", 0)
            body = html_subscribe_page("Inscription confirmée", "ok", "Inscription confirmée ✓",
                f"<p>Merci. L'adresse <strong>{entry['email']}</strong> est désormais inscrite aux alertes <em>{entry['topic']}</em>.</p>"
                "<p>Vous recevrez un email à chaque mise à jour réglementaire significative (loi, décret, arrêté, jurisprudence).</p>"
                + _referral_block_html(ref_url, ref_count)
                + f"<p class=\"muted\">Pour vous désinscrire à tout moment : <a href=\"{unsub_url}\">cliquez ici</a>.</p>")
            sys.stdout.write("[%s] SUBSCRIBE_CONFIRMED token=%s topic=%s\n" % (now_iso(), token[:8], entry["topic"]))
            sys.stdout.flush()
            self._send(200, body, ctype="text/html; charset=utf-8")
            return

        if path == "/api/me":
            qs = parse_qs(parsed.query or "")
            token = (qs.get("token", [""])[0] or "").strip()
            if not token or len(token) > 96 or not re.match(r"^[A-Za-z0-9_-]+$", token):
                self._send(400, {"ok": False, "error": "invalid token"})
                return
            events = read_jsonl(SUBSCRIBERS_FILE)
            state = compute_subscriber_state(events)
            entry = state.get(token)
            if not entry:
                self._send(404, {"ok": False, "error": "not found"})
                return
            email = entry["email"] or ""
            masked = email[:2] + "***" + email[email.find("@"):] if "@" in email else email
            self._send(200, {
                "ok": True,
                "email_masked": masked,
                "topic": entry["topic"],
                "status": entry["status"],
                "referral_url": f"{PUBLIC_BASE}/?ref={token}",
                "referrals": entry.get("referrals", 0),
            })
            return

        if path == "/api/unsubscribe":
            qs = parse_qs(parsed.query or "")
            token = (qs.get("token", [""])[0] or "").strip()
            if not token or len(token) > 96 or not re.match(r"^[A-Za-z0-9_-]+$", token):
                body = html_subscribe_page("Lien invalide", "bad", "Lien invalide",
                    "<p>Ce lien de désinscription n'est pas valide.</p>")
                self._send(400, body, ctype="text/html; charset=utf-8")
                return
            events = read_jsonl(SUBSCRIBERS_FILE)
            state = compute_subscriber_state(events)
            entry = state.get(token)
            if not entry:
                body = html_subscribe_page("Lien introuvable", "bad", "Lien introuvable",
                    "<p>Aucune inscription ne correspond à ce lien.</p>")
                self._send(404, body, ctype="text/html; charset=utf-8")
                return
            if entry["status"] == "unsubscribed":
                body = html_subscribe_page("Déjà désinscrit", "warn", "Vous êtes déjà désinscrit",
                    f"<p>L'adresse <strong>{entry['email']}</strong> a déjà été désinscrite.</p>")
                self._send(200, body, ctype="text/html; charset=utf-8")
                return
            append_jsonl(SUBSCRIBERS_FILE, {"ts": now_iso(), "type": "unsubscribe", "token": token})
            body = html_subscribe_page("Désinscription confirmée", "ok", "Désinscription confirmée ✓",
                f"<p>L'adresse <strong>{entry['email']}</strong> n'est plus inscrite aux alertes. Plus aucun email ne vous sera envoyé.</p>"
                "<p class=\"muted\">Droit à l'oubli RGPD : vos données seront purgées sous 30 jours.</p>")
            sys.stdout.write("[%s] SUBSCRIBE_UNSUBSCRIBED token=%s\n" % (now_iso(), token[:8]))
            sys.stdout.flush()
            self._send(200, body, ctype="text/html; charset=utf-8")
            return

        if path == "/api/recourse" or path.startswith("/api/recourse/"):
            tag = path[len("/api/recourse"):].lstrip("/")
            want_md = False
            if tag.endswith(".md"):
                want_md = True
                tag = tag[:-3]
            if not os.path.isdir(INTERPRETATION_LIB_DIR):
                self._send(503, {"ok": False, "error": "library not available"})
                return
            if not tag:
                tags = []
                for fn in sorted(os.listdir(INTERPRETATION_LIB_DIR)):
                    if not fn.endswith(".json"):
                        continue
                    base = fn[:-5]
                    tname = base.rsplit(".", 1)[0] if "." in base else base
                    fpath = os.path.join(INTERPRETATION_LIB_DIR, fn)
                    try:
                        with open(fpath, "rb") as fp:
                            data = json.loads(fp.read().decode("utf-8"))
                        tags.append({
                            "tag": data.get("tag", tname),
                            "version": data.get("version"),
                            "wave_ts": data.get("wave_ts"),
                            "scope": data.get("scope"),
                            "url": f"/api/recourse/{data.get('tag', tname)}",
                            "size_bytes": os.path.getsize(fpath),
                        })
                    except Exception:
                        continue
                self._send(200, {
                    "ok": True,
                    "library": "interpretation-library-v0/recourse-templates",
                    "description": "Templates de recours juridiques pour locataires FR (cat-3 interpretation moat). Citations légales croisées + procédures + courriers RAR + régulateurs.",
                    "license": "CC-BY-4.0",
                    "source": "BailleurVérif open-data",
                    "count": len(tags),
                    "templates": tags,
                    "fetched_at": now_iso(),
                }, extra_headers={"Cache-Control": "public, max-age=300"})
                return
            safe_tag = "".join(c for c in tag if c.isalnum() or c in "-_")[:64]
            if not safe_tag or safe_tag != tag:
                self._send(400, {"ok": False, "error": "invalid tag"})
                return
            candidates = [fn for fn in os.listdir(INTERPRETATION_LIB_DIR)
                          if fn.startswith(safe_tag + ".") and fn.endswith(".json")]
            if not candidates:
                self._send(404, {"ok": False, "error": "tag not found"})
                return
            fpath = os.path.join(INTERPRETATION_LIB_DIR, sorted(candidates)[-1])
            if want_md:
                md_cache_path = os.path.join(STATIC_DIR, "api-recourse-md-cache", safe_tag + ".md")
                if os.path.isfile(md_cache_path):
                    try:
                        with open(md_cache_path, "rb") as fp:
                            raw = fp.read()
                    except Exception as e:
                        self._send(500, {"ok": False, "error": str(e)})
                        return
                    etag = '"' + hashlib.sha1(raw).hexdigest()[:16] + '"'
                    inm = self.headers.get("If-None-Match", "")
                    if inm and inm == etag:
                        self.send_response(304)
                        self.send_header("ETag", etag)
                        self.send_header("Cache-Control", "public, max-age=3600")
                        self.end_headers()
                        return
                    self._send(200, raw, ctype="text/markdown; charset=utf-8",
                               extra_headers={"ETag": etag, "Cache-Control": "public, max-age=3600"})
                    return
                self._send(404, {"ok": False, "error": "markdown alternate not available"})
                return
            try:
                with open(fpath, "rb") as fp:
                    raw = fp.read()
            except Exception as e:
                self._send(500, {"ok": False, "error": str(e)})
                return
            etag = '"' + hashlib.sha1(raw).hexdigest()[:16] + '"'
            inm = self.headers.get("If-None-Match", "")
            if inm and inm == etag:
                self.send_response(304)
                self.send_header("ETag", etag)
                self.send_header("Cache-Control", "public, max-age=3600")
                self.end_headers()
                return
            self._send(200, raw, ctype="application/json; charset=utf-8",
                       extra_headers={"ETag": etag, "Cache-Control": "public, max-age=3600"})
            return

        if path == "/api/dvf-stats" or path.startswith("/api/dvf-stats/"):
            dvf_path = os.path.join(STATIC_DIR, "data", "observatoire-prix-vente-vs-loyer.json")
            if not os.path.isfile(dvf_path):
                self._send(503, {"ok": False, "error": "dataset not available"})
                return
            try:
                with open(dvf_path, "rb") as fp:
                    dataset = json.loads(fp.read().decode("utf-8"))
            except Exception as e:
                self._send(500, {"ok": False, "error": str(e)[:160]})
                return
            insee = path[len("/api/dvf-stats"):].lstrip("/")
            if not insee:
                self._send(200, {
                    "ok": True,
                    "license": dataset.get("license"),
                    "source_loyer": dataset.get("source_loyer"),
                    "source_prix_vente": dataset.get("source_prix_vente"),
                    "n_communes": dataset.get("n_communes_cross"),
                    "communes": [
                        {"insee": c["insee"], "libelle": c["libelle"],
                         "url": f"/api/dvf-stats/{c['insee']}"}
                        for c in dataset.get("communes", [])
                    ],
                    "fetched_at": now_iso(),
                }, extra_headers={"Cache-Control": "public, max-age=300"})
                return
            safe_insee = "".join(c for c in insee if c.isalnum())[:6]
            if not safe_insee or safe_insee != insee:
                self._send(400, {"ok": False, "error": "invalid insee"})
                return
            for c in dataset.get("communes", []):
                if c.get("insee") == safe_insee:
                    self._send(200, {
                        "ok": True,
                        "insee": c["insee"],
                        "libelle": c["libelle"],
                        "loyer_eur_m2_median": c["loyer_eur_m2_median"],
                        "loyer_n_annonces": c["loyer_n_annonces"],
                        "prix_vente_eur_m2_median_24_25": c["prix_vente_eur_m2_median_24_25"],
                        "nb_ventes_apt_24m": c["nb_ventes_apt_24m"],
                        "rendement_brut_pct_annuel": c["rendement_brut_pct_annuel"],
                        "period_loyer": dataset.get("period_loyer"),
                        "period_prix_vente": dataset.get("period_prix_vente"),
                        "license": dataset.get("license"),
                        "fetched_at": now_iso(),
                    }, extra_headers={"Cache-Control": "public, max-age=3600"})
                    return
            self._send(404, {"ok": False, "error": "insee not found", "insee": safe_insee,
                             "hint": "see /api/dvf-stats for full list"})
            return

        # Servir directement depuis STATIC_DIR : robots.txt, sitemap.xml, /blog/...,
        # /embed/..., et tout fichier de vérification (google*.html, BingSiteAuth.xml, etc.).
        if (
            path == "/robots.txt"
            or path == "/sitemap.xml"
            or path.startswith("/blog/")
            or path == "/blog"
            or path.startswith("/embed/")
            or path == "/embed"
            or path.startswith("/widget/")
            or path == "/widget"
            or path.startswith("/css/")
            or path.startswith("/js/")
            or path.startswith("/img/")
            or path.startswith("/data/")
            or path.startswith("/share/")
            or (path.startswith("/") and "/" not in path[1:] and path.endswith((".html", ".xml", ".txt", ".json", ".png", ".ico", ".svg", ".csv", ".md")))
            or path.startswith("/.well-known/")
        ):
            target = path
            if path == "/blog":
                target = "/blog/"
            if path == "/embed":
                target = "/embed/widget.html"
            if path == "/widget":
                target = "/widget/"
            f = safe_static(target)
            if f:
                ext = os.path.splitext(f)[1]
                with open(f, "rb") as fp:
                    self._send(200, fp.read(), ctype=MIME.get(ext, "application/octet-stream"))
                return
            # robots.txt fallback minimal si le fichier n'existe pas encore
            if path == "/robots.txt":
                self._send(200, "User-agent: *\nAllow: /\n", ctype=MIME[".txt"])
                return
            self._send(404, "not found", ctype="text/plain; charset=utf-8")
            return

        self._send(404, "not found", ctype="text/plain; charset=utf-8")

    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path
        try:
            length = int(self.headers.get("Content-Length", "0"))
            raw = self.rfile.read(length) if length else b""
            ctype = (self.headers.get("Content-Type", "") or "").split(";")[0].strip().lower()
            if not raw:
                data = {}
            elif ctype == "application/x-www-form-urlencoded":
                # Bug #14 fix : forms HTML submit as form-encoded, server now accepts both JSON and form-encoded.
                pairs = parse_qs(raw.decode("utf-8"), keep_blank_values=True)
                data = {k: (v[0] if isinstance(v, list) and v else v) for k, v in pairs.items()}
                if data.get("consent") in ("on", "true", "1", "yes"):
                    data["consent"] = True
                elif "consent" in data and data["consent"] not in (True, False):
                    data["consent"] = False
            else:
                data = json.loads(raw.decode("utf-8"))
        except Exception:
            self._send(400, {"ok": False, "error": "bad body"})
            return

        ip = self._client_ip()
        ua = self.headers.get("User-Agent", "")

        if path == "/api/visit":
            rec = {
                "ts": now_iso(),
                "sessionId": data.get("sessionId"),
                "referrer": (data.get("referrer") or "")[:300],
                "path": (data.get("path") or "")[:200],
                "source": (data.get("source") or "")[:80],
                "ip_hash": str(abs(hash(ip)) % (10**10)),  # pseudonymisé
                "ua": ua[:200]
            }
            append_jsonl(VISITS_FILE, rec)
            self._send(200, {"ok": True})
            return

        if path == "/api/result":
            rec = {
                "ts": now_iso(),
                "sessionId": data.get("sessionId"),
                "answers": data.get("answers", {}),
                "severity": data.get("severity"),
                "timeToCompleteMs": data.get("timeToCompleteMs")
            }
            append_jsonl(RESULTS_FILE, rec)
            self._send(200, {"ok": True})
            return

        if path == "/api/scan-url":
            # Strategic-16 prescription run-337 — zero-friction painkiller.
            # Input : URL annonce Locservice → fetch + parse → score conformité → verdict pour share-card.
            url = (data.get("url") or "").strip()
            if not isinstance(url, str) or len(url) < 20 or len(url) > 500:
                self._send(400, {"ok": False, "error": "url invalide (20-500 chars)"})
                return
            if not url.startswith("https://www.locservice.fr/"):
                self._send(400, {"ok": False, "error": "v0 supporte uniquement locservice.fr (PAP/SeLoger JS-rendered, prévus v1)"})
                return
            try:
                from crawler.locservice_v0 import fetch as _ls_fetch, parse_detail_dpe, parse_detail_jsonld
                from scoring.conformity_score import score_record, load_reference
            except Exception as e:
                self._send(500, {"ok": False, "error": f"import error: {e}"})
                return
            try:
                html = _ls_fetch(url)
            except Exception as e:
                self._send(502, {"ok": False, "error": f"fetch failed: {e}"})
                return
            dpe, ges = parse_detail_dpe(html)
            ld = parse_detail_jsonld(html)
            cp = ld.get("cp_jsonld")
            surface = ld.get("surface_jsonld")
            title_m = re.search(r"<title>([^<]+)</title>", html)
            title = (title_m.group(1).strip()[:200] if title_m else "")
            loyer = None
            for pat in (
                r'class="[^"]*price[^"]*"[^>]*>\s*([\d\s ]{3,8})\s*€',
                r"<title>[^<]*?\b(\d[\d\s ]{2,5})\s*€",
                r"loyer[^<]{0,30}?(\d[\d\s ]{2,5})\s*€",
                r">(\d[\d\s ]{2,5})\s*€\s*/\s*mois<",
            ):
                m = re.search(pat, html, re.IGNORECASE)
                if m:
                    digits = "".join(ch for ch in m.group(1) if ch.isdigit())
                    if digits and 100 <= int(digits) <= 20000:
                        loyer = int(digits)
                        break
            if not (cp and surface and loyer):
                self._send(200, {
                    "ok": True,
                    "extracted": False,
                    "verdict": {"severity": "warn", "ville": "annonce", "depassement": 0, "loyerM2": None},
                    "raw": {"cp": cp, "surface": surface, "loyer": loyer, "dpe": dpe, "ges": ges, "title": title},
                    "explain": "Extraction partielle — JSON-LD ou prix manquant sur cette URL.",
                })
                return
            ref = load_reference()
            rec = {
                "code_postal": cp,
                "surface_m2": surface,
                "loyer_eur_total": loyer,
                "dpe_letter": dpe,
                "ges_letter": ges,
                "title": title,
            }
            scored = score_record(rec, ref)
            vscore = scored.get("violation_score", 0)
            severity = "danger" if vscore >= 2 else ("warn" if vscore >= 1 else "ok")
            excess = scored.get("encadrement_excess_eur_m2") or 0
            depassement = round(excess * surface) if excess else 0
            ville_slug = scored.get("commune_slug") or "votre ville"
            ville = ville_slug.replace("-", " ").title() if ville_slug else "votre ville"
            sys.stdout.write(f"[scan-url] {url[:80]} cp={cp} surf={surface}m2 loyer={loyer}EUR dpe={dpe} → {severity}\n")
            sys.stdout.flush()
            self._send(200, {
                "ok": True,
                "extracted": True,
                "verdict": {"severity": severity, "ville": ville, "depassement": depassement, "loyerM2": scored.get("eur_per_m2")},
                "raw": {"cp": cp, "surface": surface, "loyer": loyer, "dpe": dpe, "ges": ges, "title": title, "violation_score": vscore, "violation_type": scored.get("violation_type")},
            })
            return

        if path == "/api/funnel/event":
            event_type = (data.get("event_type") or "").strip()[:48]
            if event_type not in FUNNEL_EVENT_TYPES:
                self._send(400, {"ok": False, "error": "invalid event_type"})
                return
            meta = data.get("meta") or {}
            if not isinstance(meta, dict):
                meta = {}
            meta_clean = {}
            for k, v in list(meta.items())[:8]:
                if isinstance(k, str) and len(k) <= 32 and isinstance(v, (str, int, float, bool)):
                    meta_clean[k[:32]] = v if not isinstance(v, str) else v[:120]
            rec = {
                "ts": now_iso(),
                "sessionId": data.get("sessionId"),
                "event_type": event_type,
                "path": (data.get("path") or "")[:200],
                "meta": meta_clean,
                "ip_hash": str(abs(hash(ip)) % (10**10)),
            }
            append_jsonl(FUNNEL_FILE, rec)
            self._send(200, {"ok": True})
            return

        if path == "/api/step":
            try:
                from_step = int(data.get("from_step", 0))
                to_step_raw = data.get("to_step")
                to_step = "result" if to_step_raw == "result" else int(to_step_raw)
                ms_on_step = int(data.get("ms_on_step", 0))
            except (TypeError, ValueError):
                self._send(400, {"ok": False, "error": "bad step"})
                return
            if from_step not in (1, 2, 3, 4, 5):
                self._send(400, {"ok": False, "error": "invalid from_step"})
                return
            if to_step != "result" and to_step not in (1, 2, 3, 4, 5):
                self._send(400, {"ok": False, "error": "invalid to_step"})
                return
            rec = {
                "ts": now_iso(),
                "sessionId": data.get("sessionId"),
                "from_step": from_step,
                "to_step": to_step,
                "ms_on_step": max(0, min(ms_on_step, 3600000)),
                "path": (data.get("path") or "")[:200],
                "ip_hash": str(abs(hash(ip)) % (10**10))
            }
            append_jsonl(STEPS_FILE, rec)
            self._send(200, {"ok": True})
            return

        if path == "/api/share":
            channel = (data.get("channel") or "").strip().lower()
            allowed_channels = {"whatsapp", "email", "copy", "sms", "telegram", "messenger", "linkedin", "twitter"}
            if channel not in allowed_channels:
                self._send(400, {"ok": False, "error": "invalid channel"})
                return
            rec = {
                "ts": now_iso(),
                "sessionId": data.get("sessionId"),
                "channel": channel,
                "severity": data.get("severity"),
                "answers_ville": (data.get("answers") or {}).get("ville", ""),
                "ip_hash": str(abs(hash(ip)) % (10**10))
            }
            append_jsonl(SHARES_FILE, rec)
            sys.stdout.write("[%s] SHARE_CLICK channel=%s sev=%s\n" % (now_iso(), channel, rec["severity"]))
            sys.stdout.flush()
            self._send(200, {"ok": True})
            return

        if path == "/api/feedback":
            message = (data.get("message") or "").strip()
            if not message or len(message) > 1500:
                self._send(400, {"ok": False, "error": "invalid message length"})
                return
            email = (data.get("email") or "").strip().lower()
            if email and ("@" not in email or "." not in email or len(email) > 200):
                email = ""  # silently drop invalid email but keep feedback
            rec = {
                "ts": now_iso(),
                "sessionId": data.get("sessionId"),
                "message": message[:1500],
                "email": email or None,
                "severity": data.get("severity"),
                "answers_ville": (data.get("answers") or {}).get("ville", ""),
                "ip_hash": str(abs(hash(ip)) % (10**10))
            }
            append_jsonl(FEEDBACKS_FILE, rec)
            sys.stdout.write("[%s] FEEDBACK len=%d email=%s sev=%s\n" % (now_iso(), len(message), bool(email), rec["severity"]))
            sys.stdout.flush()
            self._send(200, {"ok": True})
            return

        if path == "/api/embed/view":
            tool = (data.get("tool") or "").strip().lower()[:32]
            ville = (data.get("ville") or "").strip().lower()[:64]
            ref = (data.get("referrer") or "")[:300]
            rec = {
                "ts": now_iso(),
                "tool": tool,
                "ville": ville,
                "referrer": ref,
                "ip_hash": str(abs(hash(ip)) % (10**10)),
                "ua": ua[:200]
            }
            append_jsonl(EMBED_VIEWS_FILE, rec)
            self._send(200, {"ok": True})
            return

        if path == "/api/embed/snippet-copied":
            tool = (data.get("tool") or "").strip().lower()[:32]
            ville = (data.get("ville") or "").strip().lower()[:64]
            rec = {
                "ts": now_iso(),
                "tool": tool,
                "ville": ville,
                "ip_hash": str(abs(hash(ip)) % (10**10)),
                "ua": ua[:200]
            }
            append_jsonl(EMBED_COPIES_FILE, rec)
            sys.stdout.write("[%s] EMBED_SNIPPET_COPIED tool=%s ville=%s\n" % (now_iso(), tool, ville))
            sys.stdout.flush()
            self._send(200, {"ok": True})
            return

        if path == "/api/subscribe":
            email = (data.get("email") or "").strip().lower()
            topic = (data.get("topic") or "").strip().lower()
            source = (data.get("source") or "")[:200]
            consent = bool(data.get("consent"))
            referrer_token = (data.get("referrer_token") or "").strip()
            intent_signal = (data.get("intent_signal") or "").strip().lower()
            if not consent:
                self._send(400, {"ok": False, "error": "consent required"})
                return
            if not EMAIL_RE.match(email) or len(email) > 200:
                self._send(400, {"ok": False, "error": "invalid email"})
                return
            if topic not in SUBSCRIBER_TOPIC_ALLOWED:
                self._send(400, {"ok": False, "error": "invalid topic"})
                return
            if intent_signal and intent_signal not in SUBSCRIBER_INTENT_ALLOWED:
                intent_signal = ""
            if referrer_token and (len(referrer_token) > 96 or not re.match(r"^[A-Za-z0-9_-]+$", referrer_token)):
                referrer_token = ""
            ip_hash = str(abs(hash(ip)) % (10**10))
            # Anti-abuse léger : max 5 subscribe events / 60s par ip_hash
            events_all = read_jsonl(SUBSCRIBERS_FILE)
            recent = 0
            cutoff = time.time() - 60
            for ev in events_all[-200:]:
                if ev.get("type") != "subscribe" or ev.get("ip_hash") != ip_hash:
                    continue
                try:
                    ts_dt = datetime.fromisoformat(ev["ts"].replace("Z", "+00:00"))
                    if ts_dt.timestamp() >= cutoff:
                        recent += 1
                except Exception:
                    pass
            if recent >= 5:
                self._send(429, {"ok": False, "error": "rate limited"})
                return
            # Idempotence : si le couple (email, topic) est déjà confirmé, retourne le token existant.
            state = compute_subscriber_state(events_all)
            for tok, entry in state.items():
                if entry["email"] == email and entry["topic"] == topic and entry["status"] == "confirmed":
                    self._send(200, {"ok": True, "already_confirmed": True})
                    return
            # Valider referrer_token : doit pointer vers un subscriber CONFIRMED (anti-self-referral, anti-pending).
            valid_referrer = ""
            if referrer_token and referrer_token in state and state[referrer_token]["status"] == "confirmed":
                # Anti-self-referral : email du parrain != email du nouveau.
                if state[referrer_token]["email"] != email:
                    valid_referrer = referrer_token
            token = secrets.token_urlsafe(24)
            rec = {
                "ts": now_iso(),
                "type": "subscribe",
                "token": token,
                "email": email,
                "topic": topic,
                "source": source,
                "ip_hash": ip_hash,
                "ua": ua[:200],
                "referrer_token": valid_referrer or None,
                "intent_signal": intent_signal or None,
            }
            append_jsonl(SUBSCRIBERS_FILE, rec)
            confirm_url = f"{PUBLIC_BASE}/api/confirm?token={token}"
            unsub_url = f"{PUBLIC_BASE}/api/unsubscribe?token={token}"
            email_sent_ok, email_info = send_signup_confirmation(email, confirm_url, unsub_url, topic)
            append_jsonl(OUTBOUND_EMAILS_FILE, {
                "ts": now_iso(),
                "kind": "signup_confirm",
                "to_hash": str(abs(hash(email)) % (10**10)),
                "topic": topic,
                "token": token,
                "ok": email_sent_ok,
                "info": email_info if not email_sent_ok else "sent",
                "msgid": email_info if email_sent_ok else None,
            })
            sys.stdout.write("[%s] SUBSCRIBE_PENDING topic=%s email=%s email_sent=%s\n"
                             % (now_iso(), topic, email[:3] + "***", email_sent_ok))
            sys.stdout.flush()
            resp = {
                "ok": True,
                "pending": True,
                "unsubscribe_url": unsub_url,
                "email_sent": email_sent_ok,
            }
            if email_sent_ok:
                resp["message"] = "Un email de confirmation vient de vous être envoyé. Cliquez sur le lien pour valider votre inscription."
            else:
                # Fallback inline-link si SMTP indisponible (degradation gracieuse Florian-mandated)
                resp["confirm_url"] = confirm_url
                resp["message"] = "Cliquez sur le lien de confirmation pour valider votre inscription."
            self._send(200, resp)
            return

        if path == "/api/capture":
            email = (data.get("email") or "").strip().lower()
            if "@" not in email or "." not in email or len(email) > 200:
                self._send(400, {"ok": False, "error": "invalid email"})
                return
            rec = {
                "ts": now_iso(),
                "sessionId": data.get("sessionId"),
                "email": email,
                "kind": data.get("kind", "report"),
                "answers": data.get("answers", {}),
                "severity": data.get("severity"),
                "depassement_eur_mois": data.get("depassement"),
                "ip_hash": str(abs(hash(ip)) % (10**10))
            }
            append_jsonl(CAPTURES_FILE, rec)
            sys.stdout.write("[%s] EMAIL_CAPTURED kind=%s sev=%s\n" % (now_iso(), rec["kind"], rec["severity"]))
            sys.stdout.flush()
            self._send(200, {"ok": True})
            return

        if path == "/api/scan-annonce":
            text = (data.get("text") or "")
            if not isinstance(text, str) or len(text.strip()) < 20:
                self._send(400, {"ok": False, "error": "text too short (min 20 chars)"})
                return
            text = text[:8000]
            text_l = text.lower()
            flags = []
            advice = []
            score = 0
            wu_match = re.search(r'\bwestern\s*union\b|\bmoneygram\b|\bbitcoin\b|\bbtc\b|\bcrypto(?:monnaie|s)?\b|\bpcs\b|\bneosurf\b|\btransfert\s*cash\b|\binternational\s+(?:bank\s+|wire\s+)?transfer\b|\b(?:wire|bank)\s+transfer\s+(?:to|abroad)\b', text_l)
            if wu_match:
                # V1.2 (run-164) : detection contexte anti-arnaque (disclaimer "JAMAIS" / "attention arnaques" / "anti-arnaque" / "never")
                ctx_start = max(0, wu_match.start() - 90)
                ctx_window = text_l[ctx_start:wu_match.end() + 30]
                is_disclaimer = bool(re.search(r'\bjamais\b|\battention\s+arnaque|\banti[\s\-]?arnaque|ne\s+(?:demande|accepte|veux)\s+(?:pas\s+)?(?:de\s+)?(?:virement|paiement)|\bm[ée]fiance\b|\bm[ée]fiez[\s\-]vous\b|\bwarning\b|\bnever\b|\bdisclaimer\b|\bne\s+jamais\s+(?:envoyer|virer|payer)\b', ctx_window))
                if not is_disclaimer:
                    flags.append({"severity": "high", "label": "Demande de paiement non-tracable (Western Union, MoneyGram, Bitcoin, PCS, Neosurf, international transfer)"})
                    score += 50
                    advice.append("Refusez catégoriquement tout paiement via Western Union, MoneyGram, Bitcoin, cartes PCS/Neosurf ou \"international transfer\". Ces moyens ne sont ni traçables ni remboursables.")
                else:
                    flags.append({"severity": "low", "label": "Mention WU/Bitcoin en contexte disclaimer anti-arnaque (legitime probable)"})
                    score += 3
            has_fr_agency = bool(re.search(r'\b(?:foncia|citya|orpi|century\s*21|laforet|guy\s*hoquet|nestenn|stephane\s*plaza|era\s*immobilier|imm[oôb]\s*de\s*france|notaire|huissier|cl[ée]s\s+(?:du\s+)?gestionnaire|gestion\s+locative\s+confi[ée]e?|mandataire\s+immobilier|(?:via|par|chez)\s+(?:l[\'’])?agence|en\s+agence|agence\s+(?:immobili[èe]re\s+)?[a-zé][a-zé\-]{2,})\b', text_l))
            etranger_match = re.search(r'(?:je\s+suis|propri[ée]taire|bailleur|owner)\s+(?:currently\s+|actuellement\s+)?(?:[àa]\s+l[\'’]?[ée]tranger|expatri[ée]|en\s+mission|en\s+voyage|abroad|working\s+(?:in|abroad)|au\s+royaume[\s-]?uni|aux\s+[ée]tats[\s-]?unis|en\s+afrique|en\s+australie|au\s+canada|en\s+su[èe]de|in\s+london|in\s+new\s+york|in\s+dubai)', text_l)
            if etranger_match and not has_fr_agency:
                flags.append({"severity": "high", "label": "Bailleur declare a l'etranger / en mission"})
                score += 35
                advice.append("Méfiance : un bailleur \"à l'étranger\" qui ne peut pas faire visiter est un schéma d'arnaque classique. Exigez une visite physique avec un mandataire identifié (notaire, agence).")
            elif etranger_match and has_fr_agency:
                flags.append({"severity": "low", "label": "Bailleur a l'etranger MAIS mandataire FR identifie (legitime probable)"})
                score += 5
            if re.search(r'(?:caution|d[ée]p[ôo]t\s*(?:de\s*garantie)?|loyer|frais\s*d[\'’]?agence)\s+(?:avant|d[èe]s)\s+(?:la\s+)?(?:visite|envoi|cl[ée]s)|envoy(?:ez|er)\s+(?:la\s+)?(?:caution|argent|d[ée]p[ôo]t|paiement)\s+(?:avant|pour\s+r[ée]server)|\bsend\s+(?:the\s+)?deposit\s+(?:to\s+)?(?:secure|reserve|book|lock)\b|\b(?:keys?\s+(?:shipped|sent|delivered))\s+(?:by\s+)?(?:fedex|dhl|ups|tnt|post)\b|\bpayment\s+(?:before|prior\s+to)\s+(?:the\s+)?(?:visit|viewing|meeting)\b|\bvirer?\s+\d+\s*[€e]?\s*(?:avant|pour\s+r[ée]server)', text_l):
                flags.append({"severity": "high", "label": "Demande de caution / loyer AVANT visite"})
                score += 40
                advice.append("Aucun bailleur sérieux ne demande d'argent avant la visite et la signature du bail. C'est interdit par l'article 22 de la loi du 6 juillet 1989.")
            price_match = re.search(r'(\d{2,4})\s*(?:€|euros?|eur)\b', text_l)
            surface_match = re.search(r'(\d{2,3})\s*m[²2]\b', text_l)
            if price_match and surface_match:
                try:
                    price = int(price_match.group(1))
                    surface = int(surface_match.group(1))
                    if 15 <= surface <= 250 and 100 <= price <= 20000:
                        eur_m2 = price / surface
                        if eur_m2 < 5:
                            flags.append({"severity": "medium", "label": "Prix anormalement bas : %.1f euros/m2 (mediane FR ~14 euros/m2)" % eur_m2})
                            score += 25
                            advice.append("Un loyer à %.1f€/m² est très en dessous du marché français. Soit le logement est insalubre, soit c'est une arnaque appât. Visitez systématiquement avant tout engagement." % eur_m2)
                except Exception:
                    pass
            if re.search(r'\b(?:urgent|imm[ée]diat|tr[èe]s\s*rapide|aujourd[\'’]?hui|d[èe]s\s+(?:demain|maintenant|ce\s*soir)|tr[èe]s\s+vite|d[ée]p[ée]chez)\b', text_l):
                flags.append({"severity": "medium", "label": "Ton d'urgence injustifie"})
                score += 15
                advice.append("L'urgence est un levier psychologique classique d'arnaque pour vous empêcher de réfléchir. Prenez le temps de vérifier.")
            telegram_signal = re.search(r'\.(?:ru|cn|tk|ml|ga|cf)(?:\b|/)|wa\.me/|t\.me/|whatsapp\s*[:\-]\s*\+?\d|telegram\s*[:\-]\s*@|\b(?:contact(?:ez)?(?:\s+moi)?|joindre|messagerie?\s*priv[ée]e?)\s+(?:par|sur|via|en)\s+(?:mp\s+)?(?:whatsapp|telegram)\b|\bmp\s+telegram\b|\b(?:par|sur|via)\s+telegram\s+(?:pour|uniquement|seulement)\b|\bje\s+(?:ne\s+r[ée]ponds|r[ée]ponds\s+pas)\s+(?:que\s+)?(?:par|sur|via)\s+(?:whatsapp|telegram)\b', text_l)
            if telegram_signal and not has_fr_agency:
                flags.append({"severity": "high", "label": "Basculement WhatsApp / Telegram / TLD inhabituel"})
                score += 30
                advice.append("Les arnaques basculent vite hors plateforme (WhatsApp, Telegram) pour échapper à la modération. Restez sur la messagerie de Leboncoin / SeLoger / PAP.")
            elif telegram_signal and has_fr_agency:
                flags.append({"severity": "low", "label": "Mention WhatsApp/Telegram (contact agence FR identifiee)"})
                score += 5
            has_address = bool(re.search(r'\b(?:rue|avenue|boulevard|place|all[ée]e|impasse|chemin|route|cours|quai)\s+[a-zà-ÿ]', text_l))
            if not has_address and len(text) > 200:
                flags.append({"severity": "low", "label": "Aucune adresse precise mentionnee"})
                score += 10
                advice.append("Demandez l'adresse exacte avant tout déplacement. Vérifiez sur Google Street View que le bâtiment existe.")
            if re.search(r'(?:photos?|images?)\s+(?:disponibles?\s+)?(?:par\s+(?:email|mail|sms|whatsapp|telegram)|sur\s+demande|en\s+pi[èe]ce\s+jointe|hors\s+annonce)|\b(?:photos?|pictures?)\s+(?:available\s+)?(?:on\s+request|by\s+(?:email|whatsapp|telegram))\b', text_l):
                flags.append({"severity": "medium", "label": "Photos envoyees hors plateforme"})
                score += 15
                advice.append("Les photos doivent figurer DANS l'annonce. \"Photos par email/WhatsApp\" = drapeau rouge. Faites une recherche Google Image inversée pour vérifier qu'elles ne sont pas volées.")
            if re.search(r'paypal\s+(?:en\s+)?(?:mode\s+)?(?:amis?\s*(?:et|&)\s*famille|friends?\s*(?:and|&)\s*family|f(?:&|\s*et\s*)f|personnel|priv[ée])', text_l):
                flags.append({"severity": "high", "label": "Demande PayPal Amis & Famille (paiement irreversible)"})
                score += 40
                advice.append("PayPal \"Amis & Famille\" supprime toute protection acheteur : c'est strictement equivalent a un transfert cash irreversible. Aucun bailleur honnete ne demande ce mode de paiement.")
            if re.search(r'(?:arrhes|acompte|virement|paiement|caution)\s+(?:de\s+)?\d+\s*(?:€|euros?|eur)?\s+(?:d[\'’]arrhes\s+)?(?:avant|pour\s+(?:r[ée]server|bloquer|confirmer))|(?:pour|afin\s+de)\s+(?:r[ée]server|bloquer|confirmer)\s+(?:le\s+(?:bien|logement|studio|appartement|appart)|votre\s+(?:int[ée]r[êe]t|place))[^.!?]*(?:virement|arrhes|acompte|rib)', text_l):
                flags.append({"severity": "high", "label": "Demande d'arrhes / acompte AVANT visite pour 'reserver'"})
                score += 35
                advice.append("La loi du 6 juillet 1989 (art. 22) interdit tout versement avant la signature du bail. Aucun bailleur serieux ne demande d'arrhes ou d'acompte pour \"reserver\" un logement avant visite.")
            if re.search(r'(?:loyer|caution|d[ée]p[ôo]t)\s+(?:en\s+)?cash\b|(?:pas\s+de\s+|sans\s+)bail\s+(?:papier|[ée]crit|formel)|bail\s+oral|(?:on\s+se\s+(?:met\s+d[\'’]accord|fait\s+confiance|arrange)\s+(?:[àa]\s+l[\'’]oral|sans\s+papier))|(?:pas\s+(?:besoin|d[\'’]obligation)\s+(?:de\s+)?(?:bail|paperasse|contrat))', text_l):
                flags.append({"severity": "high", "label": "Bail oral / cash / pas de contrat ecrit (marchand de sommeil)"})
                score += 35
                advice.append("L'absence de bail ecrit est ILLEGALE (loi 1989 art. 3). Cash sans recu = aucune preuve. Pattern classique de marchand de sommeil : exigez bail ecrit, etat des lieux contradictoire, paiement par virement nominatif.")
            # V1.2 (run-164) : demande virement pour "etre selectionne" / pre-bail / "integre dans premier loyer"
            if re.search(r'(?:vir(?:er|ement)|payer|verser|envoy(?:er|ez))\s+\d{2,4}\s*[€e]?\s*(?:pour|afin\s+de)\s+(?:[êe]tre\s+(?:s[ée]lectionn[ée]|retenu|pris\s+en\s+compte)|figurer\s+dans\s+la\s+s[ée]lection|valider\s+(?:le\s+)?dossier)|(?:vir(?:er|ement)|payer|verser)\s+\d{2,4}\s*[€e]?\s*[àa]\s+la\s+(?:signature\s+)?pre[\s\-]?bail|d[ée]p[ôo]t\s+(?:de\s+)?\d{2,4}\s*[€e]?\s+pour\s+(?:bloquer|figurer\s+dans\s+la\s+s[ée]lection)|ces?\s+\d{2,4}\s*[€e]?\s+(?:sera|seront)\s+(?:integr[ée]s?|d[ée]duits?|r[ée]embours[ée]s?)\s+(?:dans|du)\s+(?:le\s+)?premier\s+loyer', text_l):
                flags.append({"severity": "high", "label": "Demande virement pour 'etre selectionne' / 'pre-bail' / 'integre dans premier loyer'"})
                score += 35
                advice.append("Aucun bailleur honnete ne demande de virement pour 'etre selectionne' ou en 'pre-bail'. La promesse 'sera integre dans le premier loyer' est un piege : une fois l'argent envoye, l'arnaqueur disparait. Loi du 6 juillet 1989 art. 22 interdit tout versement avant la signature.")
            # V1.2 (run-164) : pression selection (N candidats + deadline serree + pas de visite physique)
            n_candidats_match = bool(re.search(r'\bj[\'’]?\s*ai\s+(?:actuellement\s+)?\d{1,2}\s+(?:dossiers?|candidats?|demandes?|personnes?)\s+s[ée]rieu(?:x|ses)\b', text_l))
            deadline_match = bool(re.search(r'\b(?:je\s+(?:clos|cl[ôo]ture)|cl[ôo]ture|deadline|jusqu[\'’]?\s*[àa])\s+(?:les?\s+)?(?:candidatures?\s+)?(?:lundi|mardi|mercredi|jeudi|vendredi|samedi|dimanche|demain|ce\s+soir|\d{1,2}h)\b|d[ée]lai\s+(?:de\s+)?\d{1,3}\s*h', text_l))
            no_visit_match = bool(re.search(r'\bpas\s+de\s+visite(?:\s+(?:organis[ée]e?|physique))?\b|\bsans\s+visite(?:\s+physique)?\b|\bdossier\s+(?:sur|via)\s+(?:photos?|email|mail)\s+suffit\b|\bbail\s+(?:sign[ée]\s+)?scann[ée]\s+envoy[ée]', text_l))
            if (n_candidats_match and (deadline_match or no_visit_match)) or (deadline_match and no_visit_match):
                flags.append({"severity": "medium", "label": "Pression selection : N candidats + deadline serree OU absence visite physique"})
                score += 20
                advice.append("Le combo 'plusieurs dossiers serieux' + 'deadline serree' + 'pas de visite physique' est un schema d'arnaque a la pression sociale. Un bailleur honnete prend le temps de visiter avec chaque candidat retenu.")
            score = min(score, 100)
            if score >= 60:
                severity = "high"
                verdict = "Tres probablement une arnaque"
            elif score >= 30:
                severity = "medium"
                verdict = "Plusieurs signaux suspects - vigilance accrue"
            elif score >= 10:
                severity = "low"
                verdict = "Quelques points d'attention, sans gravite majeure"
            else:
                severity = "safe"
                verdict = "Aucun signal d'arnaque detecte (mais restez vigilant)"
            rec = {
                "ts": now_iso(),
                "score": score,
                "severity": severity,
                "flags_count": len(flags),
                "text_len": len(text),
                "ip_hash": str(abs(hash(ip)) % (10**10)),
            }
            append_jsonl(os.path.join(DATA_DIR, "scans-annonces.jsonl"), rec)
            sys.stdout.write("[%s] SCAN_ANNONCE score=%d sev=%s flags=%d len=%d\n" % (now_iso(), score, severity, len(flags), len(text)))
            sys.stdout.flush()
            self._send(200, {
                "ok": True,
                "score": score,
                "severity": severity,
                "verdict": verdict,
                "flags": flags,
                "advice": advice,
                "disclaimer": "Outil heuristique gratuit. Aucun remplacement d'un avis juridique ou d'une verification terrain."
            })
            return

        if path == "/api/signaler-annonce":
            try:
                ville = str(data.get("ville") or "").strip()[:80]
                code_postal = str(data.get("code_postal") or "").strip()[:6]
                violation_type = str(data.get("violation_type") or "").strip().lower()
                loyer_eur = data.get("loyer_eur")
                surface_m2 = data.get("surface_m2")
                dpe_letter = str(data.get("dpe_letter") or "").strip().upper()[:1]
                annonce_ref = str(data.get("annonce_ref") or "").strip()[:300]
                plafond_eur_m2 = data.get("plafond_eur_m2")
                eur_per_m2 = data.get("eur_per_m2")
                meuble = bool(data.get("meuble"))
            except Exception:
                self._send(400, {"ok": False, "error": "bad fields"})
                return

            if violation_type not in ("encadrement", "dpe", "both"):
                self._send(400, {"ok": False, "error": "violation_type must be encadrement|dpe|both"})
                return
            try:
                loyer = float(loyer_eur) if loyer_eur is not None else 0.0
                surf = float(surface_m2) if surface_m2 is not None else 0.0
            except (TypeError, ValueError):
                self._send(400, {"ok": False, "error": "loyer/surface must be numeric"})
                return
            if loyer <= 0 or loyer > 50000:
                self._send(400, {"ok": False, "error": "loyer out of range"})
                return
            if surf <= 0 or surf > 1000:
                self._send(400, {"ok": False, "error": "surface out of range"})
                return
            if violation_type in ("dpe", "both") and dpe_letter not in ("F", "G"):
                self._send(400, {"ok": False, "error": "dpe_letter must be F or G for DPE violation"})
                return

            dept = _dept_from_cp(code_postal)
            pref = PREFECTURE_BY_DEPT.get(dept) or {
                "service": "Préfecture du département " + (dept or "[à compléter]"),
                "adresse": "Préfecture du département " + (dept or "[à compléter]") + " — Service Logement / DDETS",
                "email": "(à compléter — voir préfecture du département sur service-public.fr)"
            }
            eur_m2 = (loyer / surf) if surf > 0 else 0.0

            # Compose le brouillon de courrier. Texte plain — l'utilisateur copy-paste dans son client mail ou imprime.
            today = datetime.now(timezone.utc).strftime("%d/%m/%Y")
            type_bail = "meublée" if meuble else "vide"
            lines = []
            lines.append("[Vos nom et prénom]")
            lines.append("[Votre adresse postale]")
            lines.append("[Votre email]")
            lines.append("")
            lines.append(pref["service"])
            lines.append(pref["adresse"])
            lines.append("")
            lines.append("Fait à [Votre ville], le " + today)
            lines.append("")
            if violation_type == "encadrement":
                lines.append("Objet : Signalement d'une annonce de location en zone d'encadrement des loyers — loyer manifestement supérieur au plafond réglementaire")
            elif violation_type == "dpe":
                lines.append("Objet : Signalement d'une annonce de location d'un logement classé " + dpe_letter + " au DPE — interdiction de mise en location (loi Climat & Résilience)")
            else:
                lines.append("Objet : Signalement d'une annonce de location cumulant dépassement d'encadrement et classement DPE " + dpe_letter + " interdit")
            lines.append("")
            lines.append("Madame, Monsieur,")
            lines.append("")
            lines.append("Je porte à votre connaissance une annonce de location à " + (ville or "[ville]") + " (" + (code_postal or "[CP]") + ") présentant une non-conformité présumée au regard de la réglementation locative en vigueur :")
            lines.append("")
            lines.append("• Type de bail : location " + type_bail)
            lines.append("• Loyer mensuel hors charges : " + ("%.0f" % loyer) + " €")
            lines.append("• Surface habitable : " + ("%.1f" % surf).rstrip("0").rstrip(".") + " m²")
            lines.append("• Loyer rapporté à la surface : " + ("%.2f" % eur_m2) + " €/m²")
            if violation_type in ("encadrement", "both"):
                if plafond_eur_m2:
                    try:
                        pl = float(plafond_eur_m2)
                        excess_pct = 100.0 * (eur_m2 - pl) / pl if pl > 0 else 0.0
                        lines.append("• Plafond majoré applicable (arrêté préfectoral) : " + ("%.2f" % pl) + " €/m²")
                        lines.append("• Dépassement présumé : " + ("+%.1f" % excess_pct) + " % au-delà du plafond")
                    except (TypeError, ValueError):
                        pass
            if violation_type in ("dpe", "both"):
                lines.append("• Classe énergétique DPE annoncée : " + dpe_letter + " — classée parmi les « passoires thermiques » dont la mise en location est progressivement interdite")
            if annonce_ref:
                lines.append("• Référence de l'annonce (hash anonymisé) : " + annonce_ref)
            lines.append("")
            lines.append("Fondements juridiques invoqués :")
            if violation_type in ("encadrement", "both"):
                lines.append("• Article 17 de la loi n° 89-462 du 6 juillet 1989 modifiée par la loi ELAN (n° 2018-1021) — encadrement des loyers dans les zones tendues.")
                lines.append("• Arrêté préfectoral fixant les loyers de référence majorés en vigueur dans la commune concernée.")
                lines.append("• Article 198 de la loi ELAN — sanction administrative jusqu'à 5 000 € (personne physique) / 15 000 € (personne morale) en cas de loyer supérieur au plafond.")
            if violation_type in ("dpe", "both"):
                lines.append("• Article L. 173-2 du Code de la construction et de l'habitation, modifié par la loi Climat & Résilience (loi n° 2021-1104 du 22 août 2021).")
                lines.append("• Décret n° 2021-19 — Calendrier d'interdiction progressive : classe G interdite depuis le 1ᵉʳ janvier 2025 ; classe F à compter du 1ᵉʳ janvier 2028 ; classe E à compter du 1ᵉʳ janvier 2034.")
            lines.append("")
            lines.append("En conséquence, je sollicite l'engagement par votre service des contrôles utiles et, le cas échéant, des suites administratives prévues à l'encontre du bailleur concerné.")
            lines.append("")
            lines.append("Je me tiens à votre disposition pour tout complément d'information.")
            lines.append("")
            lines.append("Je vous prie d'agréer, Madame, Monsieur, l'expression de mes salutations distinguées.")
            lines.append("")
            lines.append("[Votre signature]")
            lines.append("")
            lines.append("---")
            lines.append("Pièces utiles à joindre si vous les possédez : capture d'écran de l'annonce datée, copie du bail, dernier diagnostic de performance énergétique (DPE), quittances de loyer, échanges écrits avec le bailleur.")
            lines.append("")
            lines.append("Modèle généré gratuitement par BailleurVérif (https://bailleurverif.fr) à partir des données publiques observatoire-annonces-loyer. À adapter à votre situation personnelle avant envoi. L'ADIL de votre département peut vous accompagner (numéro vert national 0 805 16 00 75).")

            courrier = "\n".join(lines)

            rec = {
                "ts": now_iso(),
                "dept": dept,
                "ville_slug": _slugify_commune(ville)[:80],
                "violation_type": violation_type,
                "dpe_letter": dpe_letter if violation_type in ("dpe", "both") else "",
                "meuble": meuble,
                "loyer_bucket": int(loyer // 100) * 100,
                "surface_bucket": int(surf // 5) * 5,
                "eur_m2_round": round(eur_m2, 1),
                "annonce_ref": annonce_ref[:64],
                "ip_hash": str(abs(hash(ip)) % (10**10)),
                "ua_short": ua[:80]
            }
            append_jsonl(SIGNALEMENTS_FILE, rec)
            sys.stdout.write("[%s] SIGNALEMENT dept=%s violation=%s dpe=%s eur_m2=%.1f\n" % (now_iso(), dept, violation_type, rec["dpe_letter"], eur_m2))
            sys.stdout.flush()
            self._send(200, {
                "ok": True,
                "courrier": courrier,
                "service_competent": pref["service"],
                "adresse_postale": pref["adresse"],
                "email_optionnel": pref["email"],
                "disclaimer": "Brouillon généré automatiquement à partir des éléments saisis. À relire et adapter avant envoi. BailleurVérif n'envoie aucun courrier à votre place et ne stocke aucune donnée nominative sur le bailleur signalé. Source : observatoire-annonces-loyer.html (licence Etalab 2.0)."
            })
            return

        if path == "/api/notation-agence":
            # V1 run-236 — moat cat-2 effets réseau : notation publique anonyme agences immo FR (entités morales).
            # Validation stricte : agence_nom normalisé, note 1-5, tags allowlist 7 valeurs, commentaire ≤280, ville/CP optionnels.
            ALLOWED_TAGS = {"loyer-abusif", "dpe-invalide", "depot-non-rendu", "etat-lieux-abusif", "charges-injustifiees", "reactivite-faible", "autre"}
            try:
                agence_raw = str(data.get("agence_nom") or "").strip()
                note = int(data.get("note") or 0)
                tags_raw = data.get("tags") or []
                if isinstance(tags_raw, str):
                    tags_raw = [t.strip() for t in tags_raw.split(",") if t.strip()]
                commentaire = str(data.get("commentaire") or "").strip()[:280]
                ville = str(data.get("ville") or "").strip()[:80]
                code_postal = str(data.get("code_postal") or "").strip()[:6]
                agence_type = str(data.get("agence_type") or "agence").strip().lower()
            except Exception:
                self._send(400, {"ok": False, "error": "bad fields"})
                return

            if len(agence_raw) < 2 or len(agence_raw) > 120:
                self._send(400, {"ok": False, "error": "agence_nom length must be 2-120 chars"})
                return
            if note < 1 or note > 5:
                self._send(400, {"ok": False, "error": "note must be integer 1-5"})
                return
            if agence_type not in ("agence", "bailleur-pro", "syndic"):
                self._send(400, {"ok": False, "error": "agence_type must be agence|bailleur-pro|syndic"})
                return
            tags_clean = [t for t in tags_raw if t in ALLOWED_TAGS][:7]
            # Normalisation pour aggregation (lower + strip accents + simple slug-like).
            agence_normalized = _slugify_commune(agence_raw)[:120]
            if len(agence_normalized) < 2:
                self._send(400, {"ok": False, "error": "agence_nom invalid after normalization"})
                return

            rec = {
                "ts": now_iso(),
                "agence_nom_raw": agence_raw[:120],
                "agence_normalized": agence_normalized,
                "agence_type": agence_type,
                "note": note,
                "tags": tags_clean,
                "commentaire": commentaire,
                "ville_slug": _slugify_commune(ville)[:80] if ville else "",
                "code_postal": code_postal,
                "ip_hash": str(abs(hash(ip)) % (10**10)),
                "ua_short": ua[:80]
            }
            append_jsonl(NOTATIONS_AGENCES_FILE, rec)
            sys.stdout.write("[%s] NOTATION agence=%s type=%s note=%d tags=%s\n" % (now_iso(), agence_normalized, agence_type, note, ",".join(tags_clean)))
            sys.stdout.flush()
            self._send(200, {
                "ok": True,
                "agence_normalized": agence_normalized,
                "note": note,
                "disclaimer": "Avis anonyme déposé. Source : déclarations utilisateurs anonymes. BailleurVérif modère a posteriori les avis manifestement abusifs (insultes, données nominatives individus, fausses agences). Le présent avis exprime l'opinion subjective de son auteur."
            })
            return

        self._send(404, {"ok": False, "error": "not found"})


def main():
    print(f"[{now_iso()}] BailleurVérif starting on :{PORT}", flush=True)
    print(f"[{now_iso()}] STATIC_DIR={STATIC_DIR}", flush=True)
    print(f"[{now_iso()}] DATA_DIR={DATA_DIR}", flush=True)
    server = HTTPServer(("0.0.0.0", PORT), Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print(f"[{now_iso()}] shutting down", flush=True)
        server.server_close()

if __name__ == "__main__":
    main()
