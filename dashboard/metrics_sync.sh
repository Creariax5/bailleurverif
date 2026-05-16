#!/usr/bin/env bash
# metrics_sync.sh — recompte leads.jsonl + florian-todos et met à jour metrics.json
#
# Usage : bash /home/deploy/saas-florian/dashboard/metrics_sync.sh
# Idempotent : peut être lancé après chaque mutation de leads.jsonl ou de florian-todos.md.
#
# Ne touche PAS aux compteurs phase2/phase3 (ils sont gérés à part).
# Ne touche PAS au numéro de wake (l'agent l'incrémente lui-même).
# Synchronise uniquement :
#   - phase1.leads_sourced       = nb total lignes leads.jsonl
#   - phase1.leads_contacted     = nb leads avec status in (contacted, replied, call-scheduled, call-done, positive, negative)
#   - phase1.leads_replied       = nb leads avec status in (replied, call-scheduled, call-done, positive, negative)
#   - phase1.calls_scheduled     = nb leads avec status in (call-scheduled, call-done, positive, negative)
#   - phase1.calls_done          = nb leads avec status in (call-done, positive, negative)
#   - phase1.calls_positive      = nb leads avec status = positive
#   - florian_todos_open / done  = comptés via grep sur florian-todos.md
#   - leads[]                    = liste compacte (id, handle, source, status)
#   - seo_articles_stock         = nb fichiers .md dans content/ (hors README.md)
#   - wakes_total                = nb fichiers run-*.md dans runs/
#   - last_wake                  = dernier timestamp run extrait du nom de fichier
#   - generated_at               = ISO8601 maintenant

set -euo pipefail

ROOT="/home/deploy/saas-florian"
LEADS="$ROOT/leads.jsonl"
TODOS="$ROOT/florian-todos.md"
METRICS="$ROOT/dashboard/metrics.json"
TMP="$(mktemp)"

if [[ ! -f "$LEADS" ]]; then
  echo "ERR: $LEADS introuvable" >&2
  exit 1
fi
if [[ ! -f "$METRICS" ]]; then
  echo "ERR: $METRICS introuvable" >&2
  exit 1
fi

NOW="$(date -u +%Y-%m-%dT%H:%MZ)"

CONTENT_DIR="$ROOT/content"
RUNS_DIR="$ROOT/runs"
BLOG_DIR="$ROOT/dashboard/blog"

python3 - "$LEADS" "$TODOS" "$METRICS" "$NOW" "$TMP" "$CONTENT_DIR" "$RUNS_DIR" "$BLOG_DIR" <<'PY'
import json, sys, re, pathlib, urllib.request, urllib.error

leads_path, todos_path, metrics_path, now_iso, tmp_path, content_dir, runs_dir, blog_dir = sys.argv[1:9]

# --- Leads ---
leads = []
with open(leads_path) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        leads.append(json.loads(line))

def status_in(L, accepted):
    return sum(1 for x in L if x.get("status") in accepted)

contacted_set  = {"contacted", "replied", "call-scheduled", "call-done", "positive", "negative"}
replied_set    = {"replied", "call-scheduled", "call-done", "positive", "negative"}
scheduled_set  = {"call-scheduled", "call-done", "positive", "negative"}
done_set       = {"call-done", "positive", "negative"}
positive_set   = {"positive"}

leads_sourced   = len(leads)
leads_contacted = status_in(leads, contacted_set)
leads_replied   = status_in(leads, replied_set)
calls_scheduled = status_in(leads, scheduled_set)
calls_done      = status_in(leads, done_set)
calls_positive  = status_in(leads, positive_set)

leads_compact = [
    {"id": L.get("id"), "handle": L.get("handle_or_alias"), "source": L.get("source"), "status": L.get("status")}
    for L in leads
]

# --- Florian todos ---
todos_text = pathlib.Path(todos_path).read_text() if pathlib.Path(todos_path).exists() else ""
open_count    = len(re.findall(r"^\s*\*\*Statut\*\*\s*:\s*OPEN", todos_text, re.M))
done_count    = len(re.findall(r"^\s*\*\*Statut\*\*\s*:\s*DONE", todos_text, re.M))

# --- Read existing metrics, update only the keys we own ---
metrics = json.loads(pathlib.Path(metrics_path).read_text())

p1 = metrics.setdefault("phase1", {})
p1["leads_sourced"]   = leads_sourced
p1["leads_contacted"] = leads_contacted
p1["leads_replied"]   = leads_replied
p1["calls_scheduled"] = calls_scheduled
p1["calls_done"]      = calls_done
p1["calls_positive"]  = calls_positive

metrics["florian_todos_open"] = open_count
metrics["florian_todos_done"] = done_count
metrics["generated_at"]       = now_iso
metrics["leads"]              = leads_compact

# --- Stock SEO Phase 2 ---
content_path = pathlib.Path(content_dir)
if content_path.is_dir():
    articles = [p for p in content_path.glob("*.md") if p.name.lower() != "readme.md"]
    metrics["seo_articles_stock"] = len(articles)

# --- Articles publiés (HTML statiques dashboard/blog/) ---
blog_path = pathlib.Path(blog_dir)
if blog_path.is_dir():
    published = [p for p in blog_path.glob("*.html") if p.name.lower() != "index.html"]
    p2 = metrics.setdefault("phase2", {})
    p2["articles_published"] = len(published)
    metrics["blog_url"] = "http://217.182.171.135:8101/blog/"

# --- Wakes ---
runs_path = pathlib.Path(runs_dir)
if runs_path.is_dir():
    runs = sorted(p.name for p in runs_path.glob("run-*.md"))
    metrics["wakes_total"] = len(runs)
    if runs:
        # extrait le timestamp du nom de fichier "run-2026-05-13T11-00Z.md"
        last = runs[-1]
        m = re.match(r"run-(.+?)\.md$", last)
        if m:
            ts = m.group(1)
            # normalise éventuellement T11-00Z → T11:00Z
            ts_norm = re.sub(r"T(\d{2})-(\d{2})Z", r"T\1:\2Z", ts)
            ts_norm = re.sub(r"T(\d{2})(\d{2})(\d{2})Z", r"T\1:\2Z", ts_norm)
            metrics["last_wake"] = ts_norm

# --- Wedge tool stats (BailleurVérif, port 8102) ---
try:
    with urllib.request.urlopen("http://127.0.0.1:8102/api/stats", timeout=2) as r:
        wstats = json.loads(r.read().decode("utf-8"))
    metrics["wedge"] = {
        "service": "BailleurVerif",
        "url": "http://217.182.171.135:8102",
        "online": True,
        "visits_unique": wstats.get("visits_unique", 0),
        "visits_total": wstats.get("visits_total", 0),
        "results_total": wstats.get("results_total", 0),
        "captures_total": wstats.get("captures_total", 0),
        "captures_report": wstats.get("captures_report", 0),
        "captures_watch": wstats.get("captures_watch", 0),
        "conv_email_pct": wstats.get("conv_email_pct", 0),
        "shares_total": wstats.get("shares_total", 0),
        "shares_unique_sessions": wstats.get("shares_unique_sessions", 0),
        "share_rate_pct": wstats.get("share_rate_pct", 0),
        "share_channels": wstats.get("share_channels", []),
        "referrals_from_share": wstats.get("referrals_from_share", 0),
        "feedbacks_total": wstats.get("feedbacks_total", 0),
        "feedbacks_with_email": wstats.get("feedbacks_with_email", 0),
        "severity": wstats.get("severity", {"ok":0,"warn":0,"danger":0}),
        "top_villes": wstats.get("top_villes", []),
        "go_no_go_status": wstats.get("go_no_go_status", "collecting"),
        "go_no_go_threshold_pct": wstats.get("go_no_go_threshold_pct", 20)
    }
except (urllib.error.URLError, TimeoutError, ConnectionError, Exception) as e:
    metrics["wedge"] = {"service": "BailleurVerif", "url": "http://217.182.171.135:8102", "online": False, "error": str(e)[:120]}

with open(tmp_path, "w") as f:
    json.dump(metrics, f, indent=2, ensure_ascii=False)
PY

mv "$TMP" "$METRICS"
echo "[metrics_sync] OK $NOW · leads=$(wc -l < "$LEADS") · file=$METRICS"
