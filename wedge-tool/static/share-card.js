// share-card.js — Pillar 1 PRIO ABSOLU mission recalibrée 2026-05-21
//
// Génère un PNG share-friendly (1200×630, OG-image format) à partir du verdict utilisateur.
// 0 dépendance externe (SVG → Canvas → PNG). Anonymisé : pas d'adresse, juste ville + chiffres.
// Intégration future (anti-touch ban audit-14 actif jusqu'à audit-15) : button "Partager" sur
// verdict-card homepage post-funnel data T+24h décision pivot/sharpen.

(function (window) {
  "use strict";

  // Palette par sévérité (cohérent verdict-{danger,warn,ok} CSS classes app.js)
  const PALETTE = {
    danger: { bg: "#7f1d1d", accent: "#fca5a5", emoji: "🚨", label: "VIOLATION DÉTECTÉE" },
    warn:   { bg: "#78350f", accent: "#fcd34d", emoji: "⚠️", label: "À VÉRIFIER" },
    ok:     { bg: "#14532d", accent: "#86efac", emoji: "✅", label: "LOYER CONFORME" },
  };

  // Format français pour montants
  function fmtEur(n) { return Math.round(n).toLocaleString("fr-FR") + " €"; }

  // Échappe XML/SVG-unsafe chars dans valeurs user-injected
  function esc(s) {
    return String(s).replace(/[<>&"']/g, c => ({ "<": "&lt;", ">": "&gt;", "&": "&amp;", '"': "&quot;", "'": "&apos;" }[c]));
  }

  // WebKit/iOS Safari ne rend pas <foreignObject> via drawImage→canvas — wrap natif <text>+<tspan>
  function wrapAt(s, maxChars) {
    s = String(s);
    if (s.length <= maxChars) return [s];
    let i = maxChars;
    while (i > 0 && s[i] !== " ") i--;
    if (i === 0) i = maxChars;
    return [s.slice(0, i).trim(), s.slice(i).trim()];
  }

  // Construit le SVG verdict-card (1200×630)
  function buildSvg(verdict) {
    const sev = verdict.severity || "warn";
    const pal = PALETTE[sev] || PALETTE.warn;
    const ville = esc(verdict.ville || "Ma ville");
    const depMois = verdict.depassement || 0;
    const depAn = depMois * 12;
    const loyerM2 = verdict.loyerM2 ? verdict.loyerM2.toFixed(2) : null;

    // Headline + sous-titre selon sévérité
    let headline, subline;
    if (sev === "danger") {
      headline = `${fmtEur(depMois)}/mois au-dessus du plafond légal`;
      subline = `Encadrement ${ville} • Soit ${fmtEur(depAn)}/an récupérables (rétroactif 3 ans max)`;
    } else if (sev === "warn") {
      headline = `Loyer ${ville} — vérification recommandée`;
      subline = loyerM2 ? `${loyerM2} €/m² (secteur indéterminé, simulateur officiel à consulter)` : "Secteur à confirmer";
    } else {
      headline = `Loyer ${ville} — pas d'infraction d'encadrement`;
      subline = loyerM2 ? `${loyerM2} €/m² • Vérifié sur barème 2026` : "Vérifié sur barème 2026";
    }

    // SVG inline, autonome, fonts système pour éviter dep externe
    return `<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
  <rect width="1200" height="630" fill="${pal.bg}"/>
  <rect x="0" y="0" width="1200" height="8" fill="${pal.accent}"/>
  <text x="60" y="120" font-family="system-ui,-apple-system,sans-serif" font-size="28" font-weight="700" fill="${pal.accent}" letter-spacing="2">${pal.emoji}  ${pal.label}</text>
  <text x="60" y="240" font-family="system-ui,-apple-system,sans-serif" font-size="64" font-weight="800" fill="#fff" text-rendering="optimizeLegibility">${esc(headline)}</text>
  <text x="60" y="340" font-family="system-ui,-apple-system,sans-serif" font-size="32" font-weight="400" fill="#fff" opacity="0.92">${wrapAt(subline, 46).map((line, idx) => `<tspan x="60" dy="${idx === 0 ? 0 : 42}">${esc(line)}</tspan>`).join("")}</text>
  <line x1="60" y1="510" x2="1140" y2="510" stroke="${pal.accent}" stroke-opacity=".3" stroke-width="1"/>
  <text x="60" y="570" font-family="system-ui,-apple-system,sans-serif" font-size="22" font-weight="600" fill="${pal.accent}">bailleurverif.fr</text>
  <text x="60" y="600" font-family="system-ui,-apple-system,sans-serif" font-size="18" font-weight="400" fill="#fff" opacity=".7">Vérification gratuite • Sources : INSEE OLAP + DILA + ADEME</text>
  <text x="1140" y="600" font-family="system-ui,-apple-system,sans-serif" font-size="14" font-weight="400" fill="#fff" opacity=".55" text-anchor="end">Observatoire 232+ annonces non-conformes</text>
</svg>`;
  }

  // Convertit le SVG en PNG via canvas (renvoie blob URL)
  // Retourne une Promise<string> (objectURL prêt pour <a download>)
  function generateShareCardPng(verdict) {
    return new Promise(function (resolve, reject) {
      try {
        const svg = buildSvg(verdict);
        const blob = new Blob([svg], { type: "image/svg+xml;charset=utf-8" });
        const url = URL.createObjectURL(blob);
        const img = new Image();
        img.onload = function () {
          const canvas = document.createElement("canvas");
          canvas.width = 1200;
          canvas.height = 630;
          const ctx = canvas.getContext("2d");
          ctx.fillStyle = PALETTE[verdict.severity || "warn"].bg;
          ctx.fillRect(0, 0, 1200, 630);
          ctx.drawImage(img, 0, 0);
          URL.revokeObjectURL(url);
          canvas.toBlob(function (pngBlob) {
            if (!pngBlob) { reject(new Error("toBlob failed")); return; }
            resolve(URL.createObjectURL(pngBlob));
          }, "image/png", 0.95);
        };
        img.onerror = function (e) { URL.revokeObjectURL(url); reject(e); };
        img.src = url;
      } catch (e) { reject(e); }
    });
  }

  // Déclenche le download direct
  function downloadShareCard(verdict, filename) {
    return generateShareCardPng(verdict).then(function (pngUrl) {
      const a = document.createElement("a");
      a.href = pngUrl;
      a.download = filename || ("bailleurverif-verdict-" + Date.now() + ".png");
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      // libère le blob URL après 30s (laisse temps au download)
      setTimeout(function () { URL.revokeObjectURL(pngUrl); }, 30000);
      // Track event funnel (opt-in via trackFunnel global app.js)
      if (typeof window.trackFunnel === "function") {
        window.trackFunnel("share_card_downloaded", { sev: verdict.severity });
      }
      return pngUrl;
    });
  }

  // Exporte API publique
  window.ShareCard = {
    buildSvg: buildSvg,
    generatePng: generateShareCardPng,
    download: downloadShareCard,
  };
})(window);
