# Signaux qualifiants — validation latente de l'angle A1

> Posts publics de bailleurs particuliers FR qui valident la **demande latente** pour notre offre Conformité-as-a-Service.
> Distinct de `leads.jsonl` : ici on collecte des PREUVES d'angle (utile pour landing/SEO/pitch), pas forcément des leads contactables.
> Mise à jour : 2026-05-13 run-3.

---

## Source S1 — investisseurs-heureux.fr (forum d'investisseurs particuliers, pseudos floutés non-contactables)

### SIG-001 — Diagnostic électrique : anomalies en location
- **URL** : https://www.investisseurs-heureux.fr/t33121
- **Date** : 07/05/2026
- **Pain** : bailleur incertain sur la conformité d'un diagnostic électrique défavorable avant remise en location
- **Mappe à feature** : module "diagnostic-checker" → upload du DPE/électrique, l'outil dit GO/STOP avec règle juridique référencée
- **Statut signal** : ★★★ très récent, exactement notre cœur de cible

### SIG-002 — Abandon de logement + loyers impayés
- **URL** : https://www.investisseurs-heureux.fr/t33141
- **Date** : 10/05/2026
- **Pain** : risques juridiques pour le bailleur en cas d'abandon de logement avec impayés
- **Mappe à feature** : module "procédure-impayés" (probablement v2, pas cœur conformité)
- **Statut signal** : ★★ adjacent — pas notre cœur (conformité) mais segment proche, à monitorer pour upsell GLI/recouvrement

### SIG-003 — Meublés de tourisme : restrictions copropriété
- **URL** : https://www.investisseurs-heureux.fr/t32937
- **Date** : 20/04/2026
- **Pain** : bailleurs LMNP/Airbnb touchés par les nouvelles restrictions
- **Mappe à feature** : module "veille-réglementaire" (alertes ciblées sur statut LMNP/touristique)
- **Statut signal** : ★★ segment adjacent (LMNP touristique vs LMNP longue durée), pertinent pour V2 multi-statut

### SIG-004 — Fiscalité revenus fonciers : déduction frais procédure et indemnités
- **URL** : https://www.investisseurs-heureux.fr/t32790
- **Date** : 20/04/2026
- **Pain** : complexité fiscale, peur de l'erreur déclarative
- **Mappe à feature** : module "déclaration-2044/2031 assistée"
- **Statut signal** : ★★ pertinent — la déclaration fiscale est dans le scope A1 (échéances Alur élargies)

## Source S2 — forum.quechoisir.org (handles publics → certains contactables)

### SIG-005 / LEAD-001 — EtienneGP, bailleur T3 65m² 1982 — galère diagnostic électrique
- **URL** : https://forum.quechoisir.org/diagnostic-electrique-location-anomalies-signalees-le-proprietaire-est-il-oblige-de-faire-des-travaux-t379994.html
- **Phrase qualifiante exacte (citation)** : "Je suis propriétaire bailleur d'un appartement T3 (65 m²) construit en 1982 que je loue depuis 2019. Mon locataire actuel part fin juin et avant de remettre le bien en location, j'ai fait refaire le diagnostic électrique [...] Le diagnostiqueur m'a dit que ce n'était 'pas bloquant' pour louer [...] Sauf que j'ai un doute."
- **Pain mappé** : conformité diagnostic / décret 2008 / norme NF C 16-600 — incertitude sur GO/STOP location
- **Persona** : bailleur 1 bien (au moins), T3 urbain, prudent, lit la loi mais n'est pas sûr
- **Contactable** : OUI (handle public sur forum modéré, possible réponse en commentaire au thread)
- **Statut lead** : sourced
- **Aussi loggé dans** : leads.jsonl en LEAD-001

---

## Source S6 — boursorama.com forum patrimoine immobilier (sourcing 2026-05-13 run-6)

### SIG-008 / LEAD-003 — M2244825, bailleur particulier non meublé régime réel
- **URL** : https://www.boursorama.com/patrimoine/forum/immobilier/detail/465771032/
- **Phrase qualifiante** : "ma locataire... mettre en place un prélèvement automatique... Revenus Fonciers des locations non meublées, au Régime Réel (4BA). Est-ce possible pour un particulier d'établir un mandat de prélèvement SEPA ?"
- **Pain mappé** : ergonomie opérationnelle (paiement loyer automatisé) + complexité administrative bailleur particulier. Pas directement un pain conformité mais signal qu'il **gère seul, en régime réel** = ICP solide.
- **Persona** : bailleur 1+ bien, non meublé, régime réel (4BA donc location dégage des bénéfices ou veut piloter charges). Particulier, pas pro.
- **Contactable** : OUI (commentaire dans thread) MAIS pseudo anonymisé Boursorama = pas de DM, pas d'enrichissement hors-forum
- **Statut lead** : sourced (LEAD-003), marginal (thread 5 mois - froid)
- **Aussi loggé dans** : leads.jsonl en LEAD-003

### SIG-009 — fteufce et son cercle, mentors forum (PAS un lead — observation marché)
- **URLs** : multiples (467899917, 467878807, 466519539...)
- **Profil** : bailleur 11 M€ patrimoine immo (par sa propre déclaration mai 2025), **hors cible 1-5 biens**. Multi-bien gros patrimoine.
- **Pourquoi c'est un signal** : fteufce publie régulièrement (2-3 posts/mois) des retours d'expérience sur Airbnb, copro, fiscalité. Il est l'un des rares "vétérans" du forum. Si le forum a 5-10 bailleurs réguliers actifs, c'est l'archétype de l'influenceur communautaire qu'il faudra "convaincre" pour viraliser un produit hors-cible. **Note pour Phase 3** : approche partenariat / advocacy possible si on a un produit.

### SIG-010 — Densité bailleur Boursorama immobilier estimée
- **Méthode** : qualification des 30 derniers threads (avr 2025 → avr 2026)
- **Résultat** : 5 threads BAILLEUR / 30 ≈ 17 %, plus 1 marginal (M2244825 5 mois) ≈ 20% total
- **Comparaison** : ~3x meilleur que quechoisir (5%), mais ~5x moins bon qu'invest-heureux estimé (≥80%)
- **Volume** : ~5-7 threads nouveaux / mois, ~1-2 vraiment qualifiants
- **Recommandation** : monitoring bi-mensuel pour C1, ne pas en faire S1

---

## Source S3 — forum.quechoisir.org / location-f178 (sourcing 2026-05-13 run-4)

### SIG-006 / LEAD-002 — shoes59, bailleur 1 bien insatisfait de son agence
- **URL** : https://forum.quechoisir.org/agence-de-gestion-locative-rupture-de-confiance-t379394.html
- **Phrase qualifiante** : "J'ai un appartement que j'ai mis en gestion locative dans une agence dont je ne suis pas satisfaite."
- **Pain mappé** : confiance / qualité de service de la gestion déléguée — sortie d'agence vers self-management = ICP pour notre angle
- **Persona** : bailleur 1 bien, gestion déléguée actuelle → migration potentielle vers outil + autonomie
- **Contactable** : OUI, thread actif
- **Statut lead** : sourced (LEAD-002)

### SIG-007 — Lollita132, OBSERVATEUR MARCHÉ (pas un lead, signal stratégique)
- **URL** : https://forum.quechoisir.org/comment-reduire-les-risques-d-impayes-t378678.html
- **Phrase exacte** : "Je réalise une étude anonyme auprès des propriétaires bailleurs de la région PACA sur un sujet qui nous concerne tous : la réduction des risques d'impayés."
- **Pourquoi c'est un signal** : quelqu'un d'autre fait la **même chose que nous** — une étude marché vers les bailleurs PACA, par sondage Google Forms. Cible précise : impayés (= pain anti-fraude, qui est dans notre scope A1).
- **Hypothèse** : entrepreneur en pre-validation, un peu en avance sur nous OU étudiante / acteur académique. À investiguer (mais sans paranoia : la concurrence valide la cible).
- **Action** : pas de contact direct, monitoring. Si elle publie des résultats publics, gold mine d'insights gratuits.

---

## Synthèse — ce que ces 7 signaux nous disent

1. **L'angle A1 (Conformité-as-a-Service) est validé par demande latente** : 5 threads forum publics actifs sur conformité/gestion location en 30 jours, plus 2 leads directs identifiables.
2. **Le pain de qualif n°1 est l'incertitude juridique** (suis-je dans la norme ? puis-je louer ?) > le pain calcul économique.
3. **Le diagnostic (électrique, DPE) revient deux fois** sur 7 — segment "checker conformité avant relocation" est porteur.
4. **La fiscalité, les impayés, la frustration agence** sont des pains adjacents — l'angle "gérez vous-même + sécurité conformité" peut attirer les sortants d'agence (LEAD-002 type shoes59).
5. **Au moins 1 concurrent latent** (Lollita132) fait une étude similaire en PACA — la cible est suffisamment évidente pour attirer d'autres regards. Avantage à celui qui exécute le plus vite.

## Hypothèses à raffiner suite à ces signaux (cf hypotheses.md)

- H1 (bailleurs cherchent un assistant conformité unique) — renforcée
- H2 (prêts à 19€/mois) — non testée encore
- H3 (segment cœur = 1-bien T2/T3) — confirmée sur 3 signaux directs (EtienneGP + shoes59 + Antodiag)
- À tester : "module checker diagnostic" comme feature wedge plutôt que "module DPE F-G".
- Nouvelle H9 : "Les bailleurs qui SORTENT de gestion déléguée (frustrés agence) sont un sous-segment à conversion haute" — à valider via shoes59 et autres.

## Insight méthodo — sources S1 du playbook à réviser

Sourcing run-4 (40 threads parcourus sur forum.quechoisir.org/location + diagnostic) : **2 leads BAILLEUR-OP / 40 threads ≈ 5%** de densité. Le forum est dominé par les locataires (~75%) et acheteurs (~10%). À DÉPRIORISER comme source S1.

→ Voir mise à jour `sourcing-playbook.md` §2.

## Insight run-6 — paysage sources autonomes

Après tests parallèles run-6 :
- **Boursorama forum immobilier** → nouvelle source S6 ouverte, densité bailleur 17-20%, mais pseudos anonymisés (limite outreach à C1 in-forum)
- **old.reddit.com** → bloqué côté agent ("unable to fetch") — pas un workaround pour reddit.com
- **forum.hardware.fr/immobilier** → 404 sur la page testée, à explorer mieux
- **forum-juridique.net-iris.fr** → ECONNREFUSED, hôte down
- **quechoisir slugs alternatifs** (/location, /immobilier-f12) → 404, le forum a été restructuré, drill-down uniquement via Google site:

Verdict global : 1 nouvelle source autonome trouvée mais d'un rendement modeste (1-2 leads qualifiants/mois). Le mur web reste réel. Le ROI le plus haut maintenant n'est pas de chercher d'autres forums mais (a) débloquer Florian sur TODO-1/7/8 (b) produire du contenu SEO en stock pour Phase 2 (c) monitoring bi-mensuel Boursorama + quechoisir.

## Insight run-7 — universimmo écarté, carte sources consolidée

Test run-7 sur 8 nouvelles sources candidates :
- **universimmo.com/forum/** → HTTP 200 mais archive figée juillet 2009 (forum migré, 4 264 sujets dans la section "Appel à expériences similaires bailleurs" tous antérieurs à 2010). Inexploitable.
- **universimmo.com/forum_universimmo/** (nouvelle plateforme) → HTTP 500. Cassée.
- **leblogpatrimoine.com/immobilier** → HTTP 200 mais c'est un blog, pas un forum. Pas de leads. Utile veille SEO/inspiration uniquement.
- **immobilier-danger.com, jurifiable, documentissime, village-justice, lecoinduproprietaire, particulier-bailleur** → 404 / 301 / DNS not found.
- **forum.cms-bp.com, proprietaires-actifs.fr** → DNS not found.

Verdict consolidé Phase 1 résiduelle : aucune nouvelle source autonome scalable n'est trouvable. La carte des sources est figée à :
- S1 invest-heureux (bloqué Cloudflare, débloquable via TODO-7 Florian)
- S2 Finary (bloqué login, TODO-2)
- S3 Reddit (bloqué Cloudflare, TODO-3)
- S4 LinkedIn (bloqué login, TODO-3)
- S5 quechoisir (densité 5%, drill via Google site:)
- **S6 Boursorama** (active, rendement ~1-2 leads/mois — la seule vivante autonome)
- S7-S9 abandonnés (BFM/Capital, universimmo, leblogpatrimoine)

L'effort de prospection de nouvelles sources n'a plus de ROI. Décision : arrêter la chasse aux forums, scaler le stock SEO et attendre les TODO Florian.
