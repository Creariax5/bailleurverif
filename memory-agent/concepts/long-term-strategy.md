# Long-term strategy — Phase 1 utility → Phase 2 SaaS scalable conditionnel

> **Source décisive** : Florian brief inbox.md 2026-06-03T17:00Z (autonomie totale auto-PATCH prompts, stratégie séquentielle binding).
> **Statut** : Phase 1 EN COURS. Phase 2 = ENGAGÉE EN PRÉPARATION (rails techniques + capture signal persona), NON-déclenchée.
> **Owner** : Builder Agent (autonome). Florian = veto + arbitrages.

## Vision (12-18 mois)

Vrai SaaS scalable récurrent (€10-50k€/mois) construit sur un persona vertical dominant — probablement **bailleur multi-bien** (alertes JORF + IRL/DPE/conformité continue) OU pivot **B2B agences/syndics** selon signal user mesuré Phase 1.

## Phase 1 (M0-M9 estimé) — Utility free + acquisition + brand

**Mission alignée** : `concepts/mission.md` RE-RECALIBRÉE 2026-06-01T14:30Z (P1 PRODUIT-EXCELLENCE + P2 SEO COMPOUNDING + P3 MESURE).

**Ship gate "would they pay €X"** (binding ≥06-03T16:30Z) : chaque NEW page / NEW feature passe le filtre *"un utilisateur paierait-il €5-50 pour ça si payant ?"* AVANT ship. Sinon, défer ou pivote.

**Métriques cibles** :
- `humans_engaged_lifetime ≥ 100` (North Star)
- `gsc_indexed_pages ≥ 50` @ M3 (vs ~8 actuel)
- `produit_excellence_signal = verdict_displayed / q1_answered ≥ 70%` @ M3
- `subscribers_lifetime ≥ 20` avec breakdown `intent_signal` qualifié

**Bans Phase 1** :
- Monétisation toute forme (paywall, Stripe, freemium) tant que `humans_engaged < 100`
- Push viralité Reddit/HN/X/TikTok dépriorisé (Florian 06-01 jusqu'humans>50)
- Vanity SEO (pages_total brut, IndexNow rounds spam)

## Switch triggers Phase 1 → Phase 2

**Ne PAS pivoter sur N<10.** Itérer Phase 1 sur N≥10 humains target.

**Conditions cumulatives** pour engager Phase 2 SaaS payant :
1. `humans_engaged_lifetime ≥ 100` ET `subscribers_lifetime ≥ 20` (preuve d'usage réel)
2. **Persona dominant identifié** : ≥ 40% des subscribers ou humains qualifiés sur un même `intent_signal` (signal capture API run-433 + UI run-439)
3. **GSC traction** : ≥ 30 pages indexées + ≥ 100 imp/jour cumul
4. **Validation Florian explicite** sur le pivot (engagement temps + budget marketing)

Si 1-3 atteints, Builder escalade inbox.md HEAD pour 4. **Pas d'auto-pivot Phase 2.**

## Phase 2 (M9-M12+ conditionnel) — SaaS scalable récurrent

**Modèle candidat A — Bailleur multi-bien** (signal le plus fort à date) :
- Alertes JORF + jurisprudence DPE/IRL temps réel par bien (push email/SMS)
- Tableau de bord conformité multi-bien (DPE, encadrement, indexation IRL, jurisprudence applicable)
- Templates LRAR pré-remplis (régularisation charges, mise en demeure travaux, etc.)
- **Pricing pressenti** : €15-29/mois jusqu'à 5 biens, €49/mois 5-20 biens, sur-mesure 20+.
- Signal d'appui : GSC #2 (aides bailleur 7imp) + #5 (DRIHL) + subscriber `sogibim` dpe-bailleur (NEW Phase 2 persona).

**Modèle candidat B — B2B agences/syndics** :
- API conformité (input adresse + DPE + loyer → verdict structuré)
- White-label de l'outil verdict pour intégration site agence
- **Pricing pressenti** : €99-499/mois selon volume.
- Trigger : ≥ 3 agences identifiées en inbound spontané (forms + LinkedIn DM).

**Modèle candidat C — Locataire-victime premium** (probabilité basse) :
- Service "monter mon dossier" (LRAR + saisine ADIL + jurisprudence + simulation indemnités)
- One-shot €39-99 par dossier
- Trigger : ≥ 10 sessions complètes wedge → CTA "j'ai besoin d'aide" cliqué.

**Modèle dominant = choisi sur DATA Phase 1**, pas opinion ex-ante.

## Rails Phase 2 déjà construits (préparation passive Phase 1)

1. **Capture signal user** :
   - `intent_signal` enum API `/api/subscribe` (server run-433) + UI `/dpe-fiabilite.html` dropdown 6 options (run-439). À étendre 2-3 pages additionnelles (locataire + bailleur).
   - Mini-feedback widget post-verdict (brief A.1) : PENDING ship.
2. **Funnel observability** (run-330) : 7 events + agg sessions_reaching_step → mesure conversion par persona.
3. **Bot detection cross-ref UA** (critic-42+49) : filtre `direct_humans_after_ua_filter_lifetime` pour ne pas se mentir sur le N.
4. **GSC weekly monitoring** : tracker queries émergentes (cf `concepts/seo-keyword-intelligence.md`).
5. **Cat-3 jurisprudence-backed templates** (loyer-abusif + dpe-invalide + depot-garantie + 9 ECLI Cass.) : briques réutilisables Phase 2 "monter mon dossier".
6. **Observatoire N=232 + chain 11 vagues** (cat-1) : moat data réutilisable Phase 2 pricing data (heatmap conformité par ville → upsell agences).

## Discipline 11 (build-vs-escalate) appliquée à Phase 2 prep

- **Build par défaut** sur tout rail technique non-bloqué (capture signal, observabilité, templates).
- **Escalade Florian UNIQUEMENT** sur :
  - Choix modèle A/B/C définitif (data Phase 1 requise + arbitrage humain)
  - Engagement Stripe / cadre légal SaaS payant
  - Pivot complet (abandon BailleurVérif brand, etc.)
  - Budget marketing > 100€/mois récurrent

## Risques Phase 2

1. **Persona-fit jamais trouvé** : Phase 1 plafonne humans<50 → mission re-recalibrée vers cat-3 LLM-bait densification (canal pull-LLM seul validé, Bouygues+Applebot).
2. **Concurrence ANIL/SP-fr surclasse SEO** : Phase 2 doit avoir feature defendable pure (alertes temps réel, dashboard multi-bien) que ANIL ne fera jamais.
3. **Florian capacity** : Phase 2 = engagement temps Florian (SAV, kyc, comptabilité). Vérifier appétence AVANT switch.

## Décisions ouvertes (à trancher Phase 2 entry)

- Brand : conserver "BailleurVérif" OR rebrand neutre (bailleur-side aurait friction "vérif" qui sonne locataire-side) ?
- Stack : conserver Python stdlib server.py OR migrer FastAPI/PostgreSQL pour scaling subscribers + paiements ?
- Statut juridique : auto-entreprise → SASU à quel seuil revenus ?
- Acquisition payante Phase 2 : Google Ads bailleurs OR LinkedIn agences OR organique pur ?

## Méta — pourquoi ce concept existe

Florian 06-03T17:00Z verbatim : *"Dis à l'agent de faire tout ça lui-même, même modif son prompt et les critic et strategy si besoin."* Phase 2 prep = NEW responsabilité Builder (autonomie élargie). Ce fichier = source of truth Phase 2 thinking, lu par Strategic Critic pour audit cohérence + par futur Builder PATCH prompt.

**À mettre à jour** : à chaque NEW data Phase 1 qui change le ranking modèle A/B/C OU à chaque ship d'un rail Phase 2.
