# Sourcing Playbook — 30 premiers leads Phase 1

> Cadre méthodologique pour identifier 30 bailleurs particuliers FR (1-5 biens) à approcher en Phase 1.
> **Non exécuté tant qu'ESC-1 n'est pas validée.** Ce document est le plan, pas la liste.

---

## 1. Profil cible "qualifié" (filtres durs)

Un lead est qualifié SSI il coche **au moins 3 des 5** critères :

1. Bailleur particulier (pas SCI institutionnelle, pas pro de l'immo)
2. Détient entre 1 et 5 biens locatifs (cible cœur de l'étude)
3. Au moins un de ces signaux qualifiants exprimé publiquement :
   - parle DPE / passoire / rénovation 2025-2028
   - parle encadrement loyer (Paris/Lyon/Lille/Plaine Commune/Est Ensemble/Bordeaux/Montpellier/Grenoble + zones tendues)
   - parle galère anti-fraude dossier (faux bulletins, sélection locataire)
   - parle échéances administratives (Alur, fiscalité revenus fonciers, déclaration LMNP)
4. Actif sur la plateforme (post < 12 mois, idéalement < 3 mois)
5. Joignable proprement (handle public, profil ouvert, ou commentaire possible)

## 2. Sources prioritaires (ordre d'exploitation) — MAJ run-4 2026-05-13

### Note méthodo (révision run-4)

Sourcing test sur quechoisir.org : **5% de densité bailleur** (2/40 threads). Le bruit locataire est massif (~75%). Inversement, investisseurs-heureux.fr a montré **densité bailleur ≥80%** sur 5 threads pilotes (cf signals.md SIG-001..004). Donc : **investisseurs-heureux.fr > Finary Community > quechoisir** en rendement.

Limitation actuelle de l'agent (à débloquer via florian-todos) : `WebFetch` est bloqué par Reddit (403/cloudflare), Finary (login), LinkedIn (login), pap.fr (403), et certaines pages de investisseurs-heureux (l'index forum est 403 alors que les threads individuels passent). Les URLs de threads investisseurs-heureux doivent être trouvées via Google ou Florian.

### S1. investisseurs-heureux.fr (priorité 1 — densité bailleur particuliers FR la plus élevée mesurée)
- Threads accessibles individuellement via URL `https://www.investisseurs-heureux.fr/t{slug}/{id}`
- L'index `/c/immobilier/8` retourne 403 → besoin de **lister via Google site:investisseurs-heureux.fr** ou d'avoir un accès Florian (TODO-7 nouveau)
- Volume potentiel estimé : 10-15 leads qualifiables si on a accès aux dernières pages.

### S2. Finary Community (priorité 2 — densité haute attendue, accès bloqué)
- Sections : "Immobilier", "Fiscalité", "Investissement locatif"
- Nécessite accès Florian (cf florian-todos TODO-2)
- Mots-clés : `DPE`, `passoire`, `encadrement`, `Alur`, `loi climat`, `interdiction location`, `LMNP`, `revenus fonciers`, `bailleur`

### S3. Reddit FR (priorité 3 — bloqué WebFetch, accessible via Google)
- Subs : `r/vosfinances`, `r/immobilier`, `r/ConseilJuridique`
- Méthode : `WebSearch` ciblé "site:reddit.com/r/{sub} {mot-clé}" — donne URLs Reddit que l'on peut ensuite ouvrir via vue Google cache, ou attendre accès Florian
- Volume estimé : 6-10 leads qualifiables.

### S4. LinkedIn (priorité 4 — qualité haute, bloqué sans login)
- Recherche posts publics, mots-clés : `bailleur DPE`, `encadrement loyer galère`, `propriétaire passoire thermique`, `investisseur locatif rénovation`
- Nécessite accès Florian (TODO-3)
- Filtrer pros immo (agents, gestionnaires) pour ne garder que particuliers.

### S5. Forum quechoisir.org (priorité 5 — déprio : densité bailleur 5%)
- Garder pour les rares perles (LEAD-001 EtienneGP + LEAD-002 shoes59 viennent de là)
- Sous-forums utiles : `location-f178`, `diagnostic-immobilier-f176`, `syndic-f179`
- Méthode efficiente : lister 25 threads de la page d'index, drill-down uniquement les BAILLEUR-OP candidats (titre + auteur).

### S6. Groupes Facebook publics (priorité 6 — fallback non-testé)
- "Propriétaires bailleurs France", "Investisseurs immobiliers locatifs"
- Probable accès limité sans Florian.

### S7. Threads forum BFM/Capital/Le Revenu (priorité 7 — opt)
- Commentaires d'articles sur DPE, encadrement loyer. Signal faible, à utiliser uniquement si volume manque.

### S8 (testé et abandonné run-7). universimmo.com forum
- Réputé historiquement source haute densité bailleur. **Test run-7 : ancien forum HTTP 200 mais archive figée 2009 (dernier message juillet 2009)**. Nouvelle plateforme `/forum_universimmo/` → HTTP 500. Inexploitable. Re-tester dans 1-2 mois si la nouvelle plateforme revient en ligne, sinon source définitivement morte.

### S9 (testé run-7). leblogpatrimoine.com
- Blog patrimoine actif, HTTP 200. **Pas un forum, pas de bailleurs identifiables**. Utile pour veille marché et inspiration SEO (analyser leurs articles à fort trafic), pas pour sourcing leads.

## 3. Process de sourcing (quand ESC-1 = OK)

1. **Recherche** : utiliser les mots-clés §2 sur S1 puis S2 puis S3 (jusqu'à atteindre 30 leads).
2. **Pré-qualification** : pour chaque hit, vérifier les 5 critères §1. Si <3, drop.
3. **Enrichissement** : noter la phrase qualifiante (signal public), l'URL du post, le handle, le persona deviné (1-bien / multi-bien / LMNP / mix).
4. **Log** : ajouter une ligne dans `leads.jsonl` au format défini dans `bugs.md`.
5. **Statut initial** : `sourced`.
6. **Pas de contact** avant validation Florian de la shortlist + des templates.

## 4. Découpage thématique cible (équilibre du panel)

Pour éviter biais d'un seul pain, viser :
- 10 leads "DPE / passoire / rénovation"
- 8 leads "encadrement loyer zone tendue"
- 6 leads "anti-fraude dossier / galère sélection locataire"
- 6 leads "fiscalité / Alur / déclaration / paperasse"

(répartition indicative, à ajuster selon ce qu'on trouve)

## 5. Garde-fous RGPD / éthique

- Sourcing exclusivement à partir d'**information publique**.
- Stockage : pas d'email/tel en clair. Handle public OK.
- Si contact passe par DM/email, base légale = "intérêt légitime" + opt-out facile à fournir.
- Tracer dans `leads.jsonl` la source URL (preuve d'origine publique en cas de contestation).
- Pas de scraping massif automatisé (1 lead = 1 décision humaine de qualification).

## 6. Outils requis (à valider)

- WebSearch / WebFetch (Anthropic) — pour interroger les sources publiques sans login.
- Pour LinkedIn et Finary connectés : login Florian manuel, je travaille à partir de captures/URLs qu'il colle.
- Pas de scraper headless tant que l'autorisation outils n'est pas explicite.

## 7. Critère d'arrêt sourcing

- Stop dès 30 leads qualifiés en stock, **ou** 50 candidats examinés (signal que la cible est trop étroite et qu'il faut élargir).

---

**Statut** : DRAFT, prêt à exécuter dès validation ESC-1 (méthode B1 ou variantes).
