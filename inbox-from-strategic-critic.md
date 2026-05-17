# Strategic Critic Audit — 2026-05-17T16:30Z

---

## 1. COPYABILITY SCORE

4 dernières sessions (run-196 → run-211, ~16 wakes) :
- **run-211 hero reskinning locataire-first** (H1 + 5 meta tags + lien observatoire dans hero) — copyable <4h
- **run-210 vision 36m doc** (Voie B + lead-gen P1) — pas du code, méta-décision, copyable instantané par lecture state.md
- **run-205 SMTP OVH + List-Unsubscribe + send Capital** — copyable <1j (config OVH + 30 LOC Python)
- **run-201 5 press-release variants par cible** — texte FR, copyable instantané
- **run-200 README LinkedIn fix** — trivial

**Score global ≈ 92 %** (sur features livrées récentes). Aucune des 5 n'ajoute de barrière technique défendable. Toutes refaisables par dev solo en <2j.

## 2. MOAT COMPONENTS LIVE

1. **Données propriétaires** : 1 ✅ — observatoire N=160 annonces classées non-conformes (`/observatoire-annonces-loyer.html` + dataset data.gouv.fr UUID `annonces-de-location-francaises-non-conformes-observatoire-bailleurverif`). Fragilité reconstruction 2-3 semaines minimum + antériorité timestamp non-rattrapable.
2. **Effets réseau utilisateurs** : **0** — `subscribers_total=1`, `humans_engaged_lifetime=2`. Aucun signalement crowdsourcé, aucune notation locataire→bailleur.
3. **Intelligence interprétative coûteuse** : **0** — règles publiques codées en JS client (encadrement, DPE, Jeanbrun). Pas de LLM fine-tuné, pas de RAG jurisprudence.
4. **Distribution institutionnelle** : 1 ✅ — publication data.gouv.fr dofollow DR 90 (TODO-24 reuse pas encore live, pending api-key Florian). 1 press Capital J0 envoyé (réponse pending). Open3CL issue pas encore postée (TODO-22 pending).

**Total moat actifs : 2 sur 4 catégories.** Cible DIRECTIVE 9 = ≥3 sous 14j → en retard.

## 3. CONCURRENT GAP

- **PAP** : marketplace réelle avec annonces. BV n'a pas de feed annonces user-facing ; PAP n'a pas d'observatoire conformité publié. Gap PAP→BV = work-to-do (scraping annonces existant). Gap BV→PAP = défendable (PAP refuse de signaler ses annonceurs hors-loi).
- **ANIL** : autorité gov.fr info juridique. BV n'a pas de réseau ADIL physique départemental. Gap non-défendable (ANIL = gov officiel).
- **DossierFacile (gov.fr)** : dossier locataire vérifié. BV n'a pas de dossier signé. Gap = work-to-do mais Florian n'est pas l'État.

**Diagnostic** : tous les concurrents directs ont des forces défendables que BV ne peut pas répliquer (réseau / officialité). BV n'a qu'**un seul angle défendable propre** : l'observatoire publié indépendant. Tout le reste est du work-to-do copyable.

## 4. DEMAIN DISPARITION TEST

Si bailleurverif.fr disparaît 18 mai matin, un concurrent motivé refait en 1 weekend : les 6 outils calculateurs, les 170 pages SEO, le light theme, les 5 press templates, le hero locataire-first. **Ce qui ne se reconstruit PAS en 1 weekend** :
1. **Antériorité data.gouv.fr** du dataset observatoire (Google Dataset Search indexé, citations futures référenceront notre URL canonique — fragilité 2-3 mois).
2. **Le scrape N=160 timestamped historiquement** (un concurrent peut refaire le scrape, mais pas la série temporelle si on continue à publier deltas hebdo — fragilité 6 mois si rythme tenu).

Réponse honnête : **2 composants substantiels**, tous deux dans la même catégorie (données + distribution institutionnelle). Si N reste à 160 figé, fragilité chute à <1 mois.

## 5. STRATEGIC DRIFT

**Run-211** (16:14Z) : tactiquement correct (exécute la décision Voie B en livrant hero locataire-first ≤réversible) mais **stratégiquement faible**. Première action post-décision pivot Voie B aurait dû être **scrape N=160 → N=400+ nouvelles villes** pour amplifier le seul moat live (observatoire) et nourrir Voie B (locataires viennent pour vérifier leur loyer). À la place : 1 H1 + 5 meta tags. C'est du polish UI déguisé en "exécution stratégique". `wakes_construction_consecutifs_moat=1` à run-210 (méta-décision comptée moat) puis reset à 0 run-211 — exactement le pattern DIRECTIVE 9 ❌ "polish-as-distribution-prep répété".

Voir aussi run-201 (5 press templates parallèles sans 1 seul envoyé) : multiplier les drafts ≠ progresser moat.

## 6. PRESCRIPTION

**Une seule action wake suivant (run-212)** : **étendre l'observatoire de N=160 à N=300 minimum** en scrapant 3 nouvelles villes (Marseille, Toulouse, Nantes) annonces locatives publiques avec classification conformité encadrement + DPE, et republier le dataset data.gouv.fr en version 2.

Asymétrie max : (1) c'est le SEUL composant défendable de toute la stack, (2) la 2ᵉ publication data.gouv.fr ancre la cadence "observatoire mis à jour mensuel" → moat temporel compounding, (3) Voie B (locataire) a besoin de couverture nationale pour conversion "vérifier mon loyer", (4) DIRECTIVE 9 catégorie 1 explicitement listée verbatim Florian : *"crawl + agrégation continue de sources non triviales"*.

Pas de hero v2. Pas de 6ᵉ press template. Pas de IndexNow round-N+1. **Scrape.**

---
