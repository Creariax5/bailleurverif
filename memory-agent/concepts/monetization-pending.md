# Concept : Monétisation Pending

**État** : OFF pour mission 5000 users 90j. Activation Phase 2 post-TODO-25 Florian-action ~3-5h.

## Pourquoi off Phase 1

- Mission B2C focus = croissance users gratuit
- Monétisation ajoute friction conversion + KYC charge cognitive Florian
- BailleurVérif crédibilité = "outil gratuit informatif" (positionnement ANIL-like)

## Plan Phase 2 (TODO-25, 5 actions Florian-action)

### 25.1 Compte paiement (1h)

**Reco : Stripe** (FR standard, intégration simple, micro-volume <35k€ pas de TVA).
- https://dashboard.stripe.com/register
- Sign up `florian.demartini.dev@gmail.com`
- KYC + RIB + CB perso virements ≤ 2-3j
- Clé restreinte : `customers:write`, `payment_intents:create`, `subscriptions:write`
- Alt : Lemon Squeezy (Merchant of Record, 5% vs Stripe 1.4%+0.25€, gère TVA EU auto)

### 25.2 3 SKUs payants (30 min)

| SKU | Prix | Public | Pitch |
|---|---|---|---|
| Premium Bailleur | €5/mois | bailleurs | Watch-list 10 biens + alertes JORF + courriers auto |
| API Access Pro | €19/mois | devs / agents immo | 100 calls `/api/lookup-adresse` + watch-list pro + export CSV/JSON |
| Pack courrier RAR | €2/unité | tous | Génération + envoi RAR via La Poste/Maileva |

A/B test pricing par agent post-activation.

### 25.3 Partenariats affiliés (1-2h)

**Voie A bailleur** :
- Lovys (GLI) : €30-50/contrat → https://lovys.fr/partenaires
- Hemea (travaux) : 5-15% commission → https://hemea.com/affiliation
- MaPrimeRénov démarcheur (Effy/MGE) : €50-150/demande

**Voie B locataire** (priorité actuelle post pivot run-210) :
- Visale (garantie locataire gratuit) — pas d'affiliation directe mais signup utile
- Castorama / Leroy Merlin : 2-5% commission
- DossierFacile (gov) : pas d'affiliation directe

### 25.4-25.5

Non finalisés. À documenter post-Florian-confirmation.

## Espérance revenue

- P50 sans Florian-action : ~150€/mois (zéro, plafonné par défaut)
- P50 avec TODO-25 actions : **500-3000€/mois**
- Asymétrie max : ~3-5h Florian une seule fois → cash récurrent

## Agent prep work (autonome avant TODO-25 done)

- Coder intégration Stripe BLANK (test mode opérationnel sans clés live)
- 3 brouillons partenaires affiliés copy (Lovys/Hemea/Castorama)
- CGU monétisation draft `/cgu-monetisation.html`
- Paywall pattern Vanilla JS pour SKU `/api/lookup-adresse` (rate-limit IP gratuit → email-gate → premium)
