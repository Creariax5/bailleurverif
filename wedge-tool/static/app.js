// BailleurVérif — V0 wedge tool
// Logique client : 5 questions → verdict → email gate

// ----- Encadrement loyer (V0 : barème simplifié, valeurs indicatives 2026) -----
// Sources : arrêtés préfectoraux, observatoires des loyers locaux (Paris, Plaine Commune,
// Est Ensemble, Métropole Grenobloise, MEL, Bordeaux Métropole, Montpellier 3M, etc.)
// `verified: true` = valeur observée dans un arrêté/observatoire récent
// `verified: false` = ville bien encadrée mais barème exact à confirmer (commune périmètre
//   intercommunal, secteur indéterminé) — le verdict pointe explicitement vers le simulateur
//   officiel pour les communes non-verified.
// Format : { ville_normalisée: { encadree, ref_nu, ref_meuble, verified } }
const VILLES_ENCADREES = {
  // Paris (1 commune, depuis 2019)
  "paris":           { encadree: true, ref_nu: 33.3, ref_meuble: 40.0, verified: true },
  // MEL — Lille + Hellemmes + Lomme (depuis 2020)
  "lille":           { encadree: true, ref_nu: 19.5, ref_meuble: 23.4, verified: true },
  "hellemmes":       { encadree: true, ref_nu: 19.5, ref_meuble: 23.4, verified: true },
  "lomme":           { encadree: true, ref_nu: 19.5, ref_meuble: 23.4, verified: true },
  // Métropole Lyon (Lyon + Villeurbanne, depuis 2021)
  "lyon":            { encadree: true, ref_nu: 16.8, ref_meuble: 20.2, verified: true },
  "villeurbanne":    { encadree: true, ref_nu: 16.5, ref_meuble: 19.8, verified: true },
  // Bordeaux (depuis 2022)
  "bordeaux":        { encadree: true, ref_nu: 17.4, ref_meuble: 20.9, verified: true },
  // Montpellier (depuis 2022)
  "montpellier":     { encadree: true, ref_nu: 17.0, ref_meuble: 20.4, verified: true },
  // Plaine Commune — 9 communes (depuis 2021)
  "saint-ouen":      { encadree: true, ref_nu: 25.2, ref_meuble: 30.2, verified: true },
  "aubervilliers":   { encadree: true, ref_nu: 23.4, ref_meuble: 28.1, verified: true },
  "saint-denis":     { encadree: true, ref_nu: 23.4, ref_meuble: 28.1, verified: true },
  "pierrefitte-sur-seine": { encadree: true, ref_nu: 22.1, ref_meuble: 26.5, verified: true },
  "epinay-sur-seine":{ encadree: true, ref_nu: 22.1, ref_meuble: 26.5, verified: true },
  "stains":          { encadree: true, ref_nu: 22.1, ref_meuble: 26.5, verified: true },
  "villetaneuse":    { encadree: true, ref_nu: 22.1, ref_meuble: 26.5, verified: true },
  "ile-saint-denis": { encadree: true, ref_nu: 23.4, ref_meuble: 28.1, verified: true },
  "la-courneuve":    { encadree: true, ref_nu: 22.1, ref_meuble: 26.5, verified: false },
  // Est Ensemble — 9 communes (depuis 2021)
  "bagnolet":        { encadree: true, ref_nu: 24.0, ref_meuble: 28.8, verified: true },
  "bondy":           { encadree: true, ref_nu: 22.5, ref_meuble: 27.0, verified: true },
  "bobigny":         { encadree: true, ref_nu: 22.5, ref_meuble: 27.0, verified: true },
  "le-pre-saint-gervais": { encadree: true, ref_nu: 24.0, ref_meuble: 28.8, verified: true },
  "les-lilas":       { encadree: true, ref_nu: 24.0, ref_meuble: 28.8, verified: true },
  "montreuil":       { encadree: true, ref_nu: 24.0, ref_meuble: 28.8, verified: true },
  "noisy-le-sec":    { encadree: true, ref_nu: 22.5, ref_meuble: 27.0, verified: true },
  "pantin":          { encadree: true, ref_nu: 24.0, ref_meuble: 28.8, verified: true },
  "romainville":     { encadree: true, ref_nu: 23.0, ref_meuble: 27.6, verified: true },
  // Grenoble-Alpes Métropole — extension communes (depuis 2023, secteurs OLAP)
  "grenoble":        { encadree: true, ref_nu: 14.5, ref_meuble: 17.4, verified: true },
  "echirolles":      { encadree: true, ref_nu: 13.5, ref_meuble: 16.2, verified: false },
  "eybens":          { encadree: true, ref_nu: 13.5, ref_meuble: 16.2, verified: false },
  "fontaine":        { encadree: true, ref_nu: 13.5, ref_meuble: 16.2, verified: false },
  "saint-martin-d-heres": { encadree: true, ref_nu: 13.5, ref_meuble: 16.2, verified: false }
};

// Villes connues mais non-encadrées (autocomplete + clarification)
const VILLES_NON_ENCADREES = [
  "marseille","nice","nantes","strasbourg","toulouse","rennes","reims","saint-etienne","toulon",
  "le havre","dijon","angers","nimes","aix-en-provence","brest","limoges","tours",
  "amiens","perpignan","metz","besancon","orleans","mulhouse","rouen","caen","nancy","argenteuil",
  "saint-paul","clermont-ferrand","la rochelle","poitiers","versailles","colombes",
  "asnieres-sur-seine","aulnay-sous-bois","rueil-malmaison","creteil","champigny-sur-marne",
  "saint-maur-des-fosses","calais","beziers","cannes","cholet","colmar","ajaccio","quimper",
  "boulogne-billancourt","courbevoie","nanterre"
];

// Echeances DPE (loi Climat & Résilience)
const DPE_RULES = {
  "A": { interdit: false, message: "DPE excellent — aucune restriction." },
  "B": { interdit: false, message: "DPE très performant — aucune restriction." },
  "C": { interdit: false, message: "DPE conforme — aucune restriction." },
  "D": { interdit: false, message: "DPE conforme — aucune restriction." },
  "E": { interdit_date: "2034-01-01", message: "DPE E : interdiction de location à partir du 1er janvier 2034 (loi Climat & Résilience)." },
  "F": { interdit_date: "2028-01-01", message: "DPE F : interdiction de mettre en location à partir du 1er janvier 2028." },
  "G": { interdit_date: "2025-01-01", message: "DPE G : interdiction de mettre en location depuis le 1er janvier 2025 (logement classé passoire thermique)." }
};

// ----- État -----
const state = {
  step: 1,
  answers: { ville: "", type: "", surface: null, loyer: null, dpe: "" },
  sessionId: null,
  startTime: Date.now(),
  stepStartTime: Date.now()
};

// Init autocomplete villes
window.addEventListener("DOMContentLoaded", () => {
  const dl = document.getElementById("villes-list");
  const all = [...Object.keys(VILLES_ENCADREES), ...VILLES_NON_ENCADREES].sort();
  all.forEach(v => {
    const opt = document.createElement("option");
    opt.value = v.replace(/-/g," ").replace(/\b\w/g, l=>l.toUpperCase());
    dl.appendChild(opt);
  });
  state.sessionId = "s-" + Date.now().toString(36) + "-" + Math.random().toString(36).slice(2,7);
  fetch("/api/visit", { method:"POST", headers:{"Content-Type":"application/json"}, body: JSON.stringify({ sessionId: state.sessionId, referrer: document.referrer || "direct", path: location.pathname, source: "home" })}).catch(()=>{});
});

function normalizeVille(s) {
  return s.toLowerCase().trim()
    .normalize("NFD").replace(/[̀-ͯ]/g,"")
    .replace(/\s+/g,"-").replace(/[^a-z0-9-]/g,"");
}

function selectChoice(btn, key) {
  const parent = btn.parentElement;
  parent.querySelectorAll(".choice").forEach(b => b.classList.remove("selected"));
  btn.classList.add("selected");
  if (key === "q-type") state.answers.type = btn.dataset.val;
  if (key === "q-dpe") state.answers.dpe = btn.dataset.val;
  const stepNum = state.step;
  const btnNext = document.getElementById("btn-" + stepNum);
  if (btnNext) { btnNext.disabled = false; btnNext.classList.remove("opacity-50","cursor-not-allowed"); }
}

function next(fromStep) {
  if (fromStep === 1) {
    const v = document.getElementById("q-ville").value.trim();
    if (!v) { alert("Indiquez une ville."); return; }
    state.answers.ville = normalizeVille(v);
  }
  if (fromStep === 2 && !state.answers.type) { alert("Choisissez nu ou meublé."); return; }
  if (fromStep === 3) {
    const s = parseFloat(document.getElementById("q-surface").value);
    if (!s || s < 5 || s > 500) { alert("Surface entre 5 et 500 m²."); return; }
    state.answers.surface = s;
  }
  if (fromStep === 4) {
    const l = parseFloat(document.getElementById("q-loyer").value);
    if (!l || l < 100 || l > 20000) { alert("Loyer entre 100 et 20 000 €."); return; }
    state.answers.loyer = l;
  }
  if (fromStep === 5 && !state.answers.dpe) { alert("Choisissez le DPE ou cliquez sur 'continuer sans le DPE'."); return; }

  document.querySelectorAll(".step").forEach(s => s.classList.remove("active"));

  const toStep = fromStep < 5 ? fromStep + 1 : "result";
  const msOnStep = Date.now() - state.stepStartTime;
  fetch("/api/step", { method:"POST", headers:{"Content-Type":"application/json"}, body: JSON.stringify({
    sessionId: state.sessionId,
    from_step: fromStep,
    to_step: toStep,
    ms_on_step: msOnStep,
    path: location.pathname
  })}).catch(()=>{});
  state.stepStartTime = Date.now();

  if (fromStep < 5) {
    state.step = fromStep + 1;
    document.querySelector(`[data-step="${state.step}"]`).classList.add("active");
    document.getElementById("step-counter").textContent = `Question ${state.step} / 5`;
    document.getElementById("progress").style.width = (state.step * 20) + "%";
  } else {
    showResult();
  }
}

function prev() {
  if (state.step <= 1) return;
  document.querySelectorAll(".step").forEach(s => s.classList.remove("active"));
  state.step -= 1;
  document.querySelector(`[data-step="${state.step}"]`).classList.add("active");
  document.getElementById("step-counter").textContent = `Question ${state.step} / 5`;
  document.getElementById("progress").style.width = (state.step * 20) + "%";
}

function computeVerdict() {
  const { ville, type, surface, loyer, dpe } = state.answers;
  const items = [];
  let severity = "ok";

  // DPE check
  if (dpe && dpe !== "unknown") {
    const rule = DPE_RULES[dpe];
    if (dpe === "G") {
      severity = "danger";
      items.push({ level: "danger", icon: "🚫", title: "DPE G — INTERDICTION DE LOCATION", body: rule.message + " Si le bail est déjà en cours il continue, mais aucun nouveau bail/renouvellement n'est légal. Sanction : impossibilité de relouer + risque action locataire en réduction de loyer." });
    } else if (dpe === "F") {
      if (severity !== "danger") severity = "warn";
      items.push({ level: "warn", icon: "⚠️", title: "DPE F — Interdiction au 1er janvier 2028", body: rule.message + " Vous avez environ 2 ans pour engager des travaux ou changer de stratégie (vente, rénovation, vacance). Le gel des loyers en zone tendue s'applique déjà depuis août 2022." });
    } else if (dpe === "E") {
      items.push({ level: "info", icon: "🕒", title: "DPE E — Conforme jusqu'en 2034", body: rule.message + " Pas d'urgence mais à anticiper si vous conservez le bien long terme." });
    } else {
      items.push({ level: "ok", icon: "✅", title: `DPE ${dpe} — Conforme`, body: rule.message });
    }
  } else {
    items.push({ level: "info", icon: "❔", title: "DPE non renseigné", body: "Faites établir un DPE si ce n'est pas déjà fait : il est obligatoire pour toute mise en location et a une validité de 10 ans. Coût indicatif : 100-250 €." });
  }

  // Encadrement loyer check
  const villeData = VILLES_ENCADREES[ville];
  if (villeData) {
    const refMaj = type === "meuble" ? villeData.ref_meuble : villeData.ref_nu;
    const loyerM2 = loyer / surface;
    const verifNote = villeData.verified
      ? `Le plafond exact dépend du secteur géographique et de l'année de construction : à confirmer via le <a href="https://www.service-public.fr/particuliers/vosdroits/F33880" target="_blank" rel="noopener" class="underline">simulateur officiel</a>.`
      : `<strong>Barème indicatif</strong> : ${capitalize(ville)} est dans le périmètre d'encadrement mais le plafond exact varie par secteur. À confirmer sur le <a href="https://www.service-public.fr/particuliers/vosdroits/F33880" target="_blank" rel="noopener" class="underline">simulateur officiel</a> ou auprès de votre observatoire local des loyers.`;
    if (loyerM2 > refMaj) {
      if (severity !== "danger") severity = "warn";
      const depassement = Math.round((loyerM2 - refMaj) * surface);
      items.push({
        level: "warn",
        icon: "💶",
        title: `Loyer probablement au-dessus du plafond (encadrement ${capitalize(ville)})`,
        body: `Votre loyer est de <strong>${loyerM2.toFixed(2)} €/m²</strong>, soit <strong>~${depassement} €/mois</strong> au-dessus du plafond indicatif (${refMaj.toFixed(1)} €/m² pour ${type === "meuble" ? "meublé" : "nu"} dans cette zone). Sanction : amende administrative jusqu'à <strong>5 000 € (15 000 € en personne morale)</strong> + restitution du trop-perçu au locataire. <em>${verifNote}</em>`
      });
    } else {
      items.push({
        level: "ok",
        icon: "✅",
        title: `Loyer dans la fourchette d'encadrement (${capitalize(ville)})`,
        body: `Votre loyer est de <strong>${loyerM2.toFixed(2)} €/m²</strong>, sous le plafond indicatif de ${refMaj.toFixed(1)} €/m². <em>${verifNote}</em>`
      });
    }
  } else {
    items.push({ level: "ok", icon: "✅", title: "Pas d'encadrement de loyer dans cette commune", body: "Cette ville n'est pas (ou plus) soumise à l'encadrement des loyers. Vous restez libre du montant — sauf relocation rapide d'un même bail, où des règles de variation s'appliquent." });
  }

  // Anti-fraude — V0 placeholder
  items.push({
    level: "info",
    icon: "🛡️",
    title: "Anti-fraude dossier locataire",
    body: "Vérification non incluse dans cette V0. Recevez la <strong>checklist 15 minutes</strong> pour détecter un faux bulletin de salaire / avis d'imposition (en cas de selection de locataire en cours). Inclus dans le rapport détaillé."
  });

  return { items, severity };
}

function capitalize(s) {
  return s.replace(/-/g," ").replace(/\b\w/g, l => l.toUpperCase());
}

function showResult() {
  state.step = "result";
  document.querySelector(`[data-step="result"]`).classList.add("active");
  document.getElementById("step-counter").textContent = `Résultat`;
  document.getElementById("progress").style.width = `100%`;

  const { items, severity } = computeVerdict();
  const card = document.getElementById("verdict-card");
  const cls = severity === "danger" ? "verdict-danger" : severity === "warn" ? "verdict-warn" : "verdict-ok";
  card.className = "rounded-2xl p-5 sm:p-6 mb-5 fade-in " + cls;
  const verdictTitles = {
    "ok": ["✅", "Votre bien semble conforme"],
    "warn": ["⚠️", "Risque de non-conformité détecté"],
    "danger": ["🚫", "Interdiction de location applicable"]
  };
  const [icon, title] = verdictTitles[severity];
  card.innerHTML = `
    <div class="flex items-start gap-3">
      <div class="text-3xl">${icon}</div>
      <div>
        <h2 class="text-xl sm:text-2xl font-bold mb-1">${title}</h2>
        <p class="text-sm text-[color:var(--text-dim)]">Verdict basé sur les barèmes officiels 2026. Vérification indicative.</p>
      </div>
    </div>
  `;

  const det = document.getElementById("details");
  det.innerHTML = "";
  items.forEach(item => {
    const div = document.createElement("div");
    div.className = "glass rounded-xl p-4 sm:p-5";
    div.innerHTML = `
      <div class="flex gap-3">
        <div class="text-xl shrink-0">${item.icon}</div>
        <div class="flex-1">
          <div class="font-semibold mb-1">${item.title}</div>
          <div class="text-sm text-[color:var(--text-dim)] leading-relaxed">${item.body}</div>
        </div>
      </div>
    `;
    det.appendChild(div);
  });

  // Log result
  fetch("/api/result", { method:"POST", headers:{"Content-Type":"application/json"}, body: JSON.stringify({
    sessionId: state.sessionId,
    answers: state.answers,
    severity,
    timeToCompleteMs: Date.now() - state.startTime
  })}).catch(()=>{});
}

function captureEmail(ev, kind) {
  ev.preventDefault();
  const form = ev.target;
  const email = form.querySelector("input[type=email]").value.trim();
  const msgId = kind === "watch" ? "watch-form-msg" : "email-form-msg";
  const msg = document.getElementById(msgId);
  if (!email.includes("@") || !email.includes(".")) { msg.textContent = "Email invalide."; msg.style.color = "var(--danger)"; return; }
  msg.textContent = "Envoi…";
  msg.style.color = "var(--text-dim)";
  fetch("/api/capture", { method:"POST", headers:{"Content-Type":"application/json"}, body: JSON.stringify({
    sessionId: state.sessionId,
    email,
    kind, // "report" ou "watch"
    answers: state.answers,
    severity: computeVerdict().severity
  })}).then(r => r.json()).then(data => {
    if (data.ok) {
      msg.textContent = kind === "watch" ? "✓ Inscrit. On vous prévient au lancement." : "✓ Reçu — votre rapport arrive sous 24h.";
      msg.style.color = "var(--accent)";
      form.querySelector("input").value = "";
      form.querySelector("button").disabled = true;
      form.querySelector("button").style.opacity = "0.5";
    } else {
      msg.textContent = "Erreur — réessayez dans quelques minutes.";
      msg.style.color = "var(--danger)";
    }
  }).catch(() => {
    msg.textContent = "Erreur réseau — réessayez.";
    msg.style.color = "var(--danger)";
  });
}

// ----- Partage social (viralité intrinsèque) -----
function share(channel) {
  const baseUrl = window.location.origin + "/";
  const sharedUrl = baseUrl + "?src=share&via=" + encodeURIComponent(channel);
  const verdict = computeVerdict();
  const severity = verdict.severity;
  const ville = state.answers.ville || "";
  const villeFriendly = ville ? capitalize(ville) : "";

  // Texte adapté à la sévérité du verdict de l'utilisateur (si fait), sinon générique
  let intro;
  if (severity === "danger") {
    intro = "Je viens de vérifier en 30 sec si ma loc est conforme à la loi 2026 — gros pain découvert. Si tu loues un bien, fais-le aussi :";
  } else if (severity === "warn") {
    intro = "J'ai testé un outil qui vérifie en 30 sec si une loc respecte la loi 2026 (DPE, encadrement, amendes 5 000 €). Pour bailleurs particuliers, à essayer :";
  } else {
    intro = "Outil utile pour bailleurs particuliers : vérifier en 30 sec si une loc est conforme à la loi 2026 (DPE, encadrement loyer, amende 5 000 €).";
  }
  if (villeFriendly && severity !== "ok") {
    intro = intro.replace("ma loc", `ma loc à ${villeFriendly}`);
  }
  const fullMsg = intro + " " + sharedUrl;

  const msgEl = document.getElementById("share-msg");
  const setMsg = (txt, color) => { msgEl.textContent = txt; msgEl.style.color = color || "var(--accent)"; };

  // Fire-and-forget tracking
  fetch("/api/share", { method: "POST", headers: {"Content-Type":"application/json"}, body: JSON.stringify({
    sessionId: state.sessionId,
    channel,
    severity,
    answers: state.answers
  })}).catch(()=>{});

  if (channel === "whatsapp") {
    const url = "https://wa.me/?text=" + encodeURIComponent(fullMsg);
    window.open(url, "_blank", "noopener,noreferrer");
    setMsg("✓ WhatsApp ouvert");
  } else if (channel === "email") {
    const subject = encodeURIComponent("Vérifie en 30 sec si ta loc est conforme à la loi 2026");
    const body = encodeURIComponent(fullMsg);
    window.location.href = "mailto:?subject=" + subject + "&body=" + body;
    setMsg("✓ Email ouvert");
  } else if (channel === "sms") {
    // sms: scheme, body param works on iOS/Android moderne
    const url = "sms:?&body=" + encodeURIComponent(fullMsg);
    window.location.href = url;
    setMsg("✓ SMS ouvert");
  } else if (channel === "copy") {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(fullMsg).then(() => {
        setMsg("✓ Lien + message copié dans le presse-papiers");
        const icon = document.getElementById("copy-icon");
        const label = document.getElementById("copy-label");
        if (icon) icon.textContent = "✅";
        if (label) label.textContent = "Copié !";
        setTimeout(() => {
          if (icon) icon.textContent = "🔗";
          if (label) label.textContent = "Copier le lien";
        }, 2500);
      }).catch(() => {
        // fallback: textarea
        fallbackCopy(fullMsg);
        setMsg("✓ Lien copié (méthode fallback)");
      });
    } else {
      fallbackCopy(fullMsg);
      setMsg("✓ Lien copié (méthode fallback)");
    }
  }
}

function fallbackCopy(text) {
  const ta = document.createElement("textarea");
  ta.value = text;
  ta.style.position = "fixed";
  ta.style.left = "-9999px";
  document.body.appendChild(ta);
  ta.select();
  try { document.execCommand("copy"); } catch (e) {}
  document.body.removeChild(ta);
}

// ----- Feedback qualitatif (capture intention/objection libre) -----
function submitFeedback(e) {
  e.preventDefault();
  const msgEl = document.getElementById("fb-message");
  const emailEl = document.getElementById("fb-email");
  const out = document.getElementById("fb-msg");
  const message = (msgEl.value || "").trim();
  const email = (emailEl.value || "").trim();
  if (message.length < 3) {
    out.textContent = "Message trop court.";
    out.style.color = "var(--warn)";
    return;
  }
  const verdict = computeVerdict();
  fetch("/api/feedback", {
    method: "POST",
    headers: {"Content-Type":"application/json"},
    body: JSON.stringify({
      sessionId: state.sessionId,
      message,
      email: email || null,
      severity: verdict.severity,
      answers: state.answers
    })
  }).then(r => r.json()).then(j => {
    if (j.ok) {
      out.textContent = "✓ Merci, ton retour est bien arrivé.";
      out.style.color = "var(--accent)";
      msgEl.value = "";
      emailEl.value = "";
      const submitBtn = document.querySelector("#feedback-form button[type=submit]");
      if (submitBtn) { submitBtn.disabled = true; submitBtn.textContent = "Envoyé"; }
    } else {
      out.textContent = "Erreur — réessayez.";
      out.style.color = "var(--danger)";
    }
  }).catch(() => {
    out.textContent = "Erreur réseau — réessayez.";
    out.style.color = "var(--danger)";
  });
}

function restart() {
  state.step = 1;
  state.answers = { ville: "", type: "", surface: null, loyer: null, dpe: "" };
  state.startTime = Date.now();
  state.stepStartTime = Date.now();
  document.querySelectorAll(".step").forEach(s => s.classList.remove("active"));
  document.querySelector(`[data-step="1"]`).classList.add("active");
  document.getElementById("step-counter").textContent = "Question 1 / 5";
  document.getElementById("progress").style.width = "20%";
  document.getElementById("q-ville").value = "";
  document.getElementById("q-surface").value = "";
  document.getElementById("q-loyer").value = "";
  document.querySelectorAll(".choice").forEach(b => b.classList.remove("selected"));
  ["btn-2","btn-5"].forEach(id => {
    const b = document.getElementById(id);
    if (b) { b.disabled = true; b.classList.add("opacity-50","cursor-not-allowed"); }
  });
}
