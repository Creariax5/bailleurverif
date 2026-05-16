#!/usr/bin/env python3
"""
BailleurVérif — serveur HTTP V0
Port 8102. Sert /static + endpoints API /api/visit, /api/result, /api/capture, /api/stats.
Données persistées en JSONL dans data/.
"""
import json
import os
import re
import secrets
import sys
import time
import logging
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(ROOT, "static")
DATA_DIR = os.path.join(ROOT, "data")
os.makedirs(DATA_DIR, exist_ok=True)

VISITS_FILE = os.path.join(DATA_DIR, "visits.jsonl")
RESULTS_FILE = os.path.join(DATA_DIR, "results.jsonl")
CAPTURES_FILE = os.path.join(DATA_DIR, "email-captures.jsonl")
SHARES_FILE = os.path.join(DATA_DIR, "shares.jsonl")
FEEDBACKS_FILE = os.path.join(DATA_DIR, "feedbacks.jsonl")
EMBED_VIEWS_FILE = os.path.join(DATA_DIR, "embed-views.jsonl")
EMBED_COPIES_FILE = os.path.join(DATA_DIR, "embed-snippet-copies.jsonl")
SUBSCRIBERS_FILE = os.path.join(DATA_DIR, "subscribers.jsonl")

PORT = int(os.environ.get("PORT", "8102"))

PUBLIC_BASE = "https://bailleurverif.fr"
SUBSCRIBER_TOPIC_ALLOWED = {"loyer-legal", "dpe-bailleur", "preavis", "veille-reglementaire"}
EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")

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
        sys.stdout.write("[%s] %s - %s\n" % (now_iso(), self.client_address[0], fmt % args))
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

        if path in ("/", "/index.html"):
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
                # subscribers double-opt-in
                sub_events = read_jsonl(SUBSCRIBERS_FILE)
                sub_state = compute_subscriber_state(sub_events)
                subscribers_pending = sum(1 for e in sub_state.values() if e["status"] == "pending")
                subscribers_confirmed = sum(1 for e in sub_state.values() if e["status"] == "confirmed")
                subscribers_unsubscribed = sum(1 for e in sub_state.values() if e["status"] == "unsubscribed")
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
                    "signups_24h": signups_24h,
                    "referrals_total": referrals_total,
                    "referrers_count": referrals_top,
                    "severity": sev,
                    "top_villes": top_villes,
                    "go_no_go_threshold_pct": 20,
                    "go_no_go_status": "go" if conv_email_pct >= 20 and visits_unique >= 100 else ("pivot" if conv_email_pct < 5 and visits_unique >= 100 else "collecting"),
                    "updated_at": now_iso()
                })
            except Exception as e:
                self._send(500, {"ok": False, "error": str(e)})
            return

        if path == "/healthz":
            self._send(200, {"ok": True, "service": "BailleurVerif", "time": now_iso()})
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

        # Servir directement depuis STATIC_DIR : robots.txt, sitemap.xml, /blog/...,
        # /embed/..., et tout fichier de vérification (google*.html, BingSiteAuth.xml, etc.).
        if (
            path == "/robots.txt"
            or path == "/sitemap.xml"
            or path.startswith("/blog/")
            or path == "/blog"
            or path.startswith("/embed/")
            or path == "/embed"
            or path.startswith("/css/")
            or path.startswith("/js/")
            or path.startswith("/img/")
            or path.startswith("/data/")
            or (path.startswith("/") and "/" not in path[1:] and path.endswith((".html", ".xml", ".txt", ".json", ".png", ".ico", ".svg", ".csv", ".md")))
            or path.startswith("/.well-known/")
        ):
            target = path
            if path == "/blog":
                target = "/blog/"
            if path == "/embed":
                target = "/embed/widget.html"
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
            raw = self.rfile.read(length) if length else b"{}"
            data = json.loads(raw.decode("utf-8")) if raw else {}
        except Exception:
            self._send(400, {"ok": False, "error": "bad json"})
            return

        ip = self._client_ip()
        ua = self.headers.get("User-Agent", "")

        if path == "/api/visit":
            rec = {
                "ts": now_iso(),
                "sessionId": data.get("sessionId"),
                "referrer": (data.get("referrer") or "")[:300],
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
            if not consent:
                self._send(400, {"ok": False, "error": "consent required"})
                return
            if not EMAIL_RE.match(email) or len(email) > 200:
                self._send(400, {"ok": False, "error": "invalid email"})
                return
            if topic not in SUBSCRIBER_TOPIC_ALLOWED:
                self._send(400, {"ok": False, "error": "invalid topic"})
                return
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
            }
            append_jsonl(SUBSCRIBERS_FILE, rec)
            confirm_url = f"{PUBLIC_BASE}/api/confirm?token={token}"
            unsub_url = f"{PUBLIC_BASE}/api/unsubscribe?token={token}"
            sys.stdout.write("[%s] SUBSCRIBE_PENDING topic=%s email=%s confirm=%s\n"
                             % (now_iso(), topic, email[:3] + "***", confirm_url))
            sys.stdout.flush()
            self._send(200, {
                "ok": True,
                "pending": True,
                "confirm_url": confirm_url,
                "unsubscribe_url": unsub_url,
                "message": "Cliquez sur le lien de confirmation pour valider votre inscription."
            })
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
                "ip_hash": str(abs(hash(ip)) % (10**10))
            }
            append_jsonl(CAPTURES_FILE, rec)
            sys.stdout.write("[%s] EMAIL_CAPTURED kind=%s sev=%s\n" % (now_iso(), rec["kind"], rec["severity"]))
            sys.stdout.flush()
            self._send(200, {"ok": True})
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
