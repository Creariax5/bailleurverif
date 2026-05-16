# Call Script — 20 min entretien validation (Phase 1)

> Script de l'entretien découverte. Objectif : valider/invalider H1-H5 (cf. `hypotheses.md`) et déclencher le go/no-go (5+/10 "où je signe à 19€").
> Durée cible : 20-25 min. Tonalité : curiosité honnête, pas de pitch.

---

## Pré-call (5 min avant)

- Relire la fiche du lead (`leads.jsonl` + post qualifiant)
- Avoir sous les yeux : le pain qu'ils ont exprimé publiquement, leur persona deviné, leur ville/zone (encadrement ou pas).
- Vérifier audio/vidéo, dispo Calendly.

---

## Ouverture (2 min)

> "Merci d'avoir pris le temps. Je te rappelle le cadre : je suis en train de comprendre comment les bailleurs particuliers comme toi vivent toute la pile réglementaire qui s'est empilée — DPE, encadrement, fraude dossier, fiscalité. Je n'ai rien à te vendre aujourd'hui. L'idée c'est 20 min, je te pose 3-4 questions, je prends des notes. À la fin, je te dirai très honnêtement où j'en suis et s'il y a quelque chose qui pourrait t'aider."

→ Demander OK pour prise de notes / enregistrement (audio uniquement, supprimé après synthèse).

---

## Question 1 — Pain mapping (5 min) → H1

> "Si je te demande tes **3 plus grosses galères** en tant que bailleur en ce moment, qu'est-ce qui te vient ?"

- Laisser parler. **Ne pas suggérer.**
- Si réponses génériques ("trouver locataires", "travaux") → creuser : "OK et sur la partie paperasse / réglementaire, qu'est-ce qui te pèse ?"
- Noter mot-pour-mot les 3.

**Critère H1** : au moins 1 des 3 = conformité réglementaire (DPE, encadrement, Alur, fraude, fisc).

---

## Question 2 — Dépense & temps actuels (5 min) → H3

> "Aujourd'hui, qu'est-ce que tu **paies** ou qu'est-ce que tu **passes comme temps** sur cette partie réglementaire ? Genre, sur les 12 derniers mois, à la louche."

Sous-questions si besoin :
- Agence ? Gestion locative ? Comptable LMNP ? GLI ?
- Outils en ligne (Smartloc, Decla, autres) ?
- Heures passées (estimation) ?
- Galère vécue (litige, redressement, alerte) ?

**Critère H3** : panier total > 50€/mois ou stress quantifiable (≥4h/mois ou incident récent).

---

## Question 3 — Triggers spécifiques DPE & encadrement (3 min) → H4, H5

> "Sur ton parc, est-ce que tu as un bien classé **F ou G** ? Et tes biens, ils sont en zone d'encadrement de loyer ?"

Si oui DPE F/G :
- "Tu as un plan pour 2025/2028 ?" (interdiction location)
- "Tu as fait chiffrer la rénov ?"

Si oui encadrement :
- "Tu as déjà eu un contrôle / une plainte / un loyer recalé ?"
- "Tu vérifies comment ton loyer reste dans le plafond chaque année ?"

**Critères** : H4 = ≥3/10 ont DPE F/G + inquiétude active. H5 = ≥3/10 en zone encadrement + préoccupation réelle.

---

## Question 4 — Pitch + closing "où je signe" (5 min) → H2 ★ critique

> "Imagine un outil — 19€/mois — qui :
> - surveille pour toi les seuils DPE et te dit quand tu dois prévoir une rénov, avec quels artisans/aides
> - check à chaque renouvellement de bail que ton loyer respecte l'encadrement de ta commune
> - filtre les dossiers locataires pour repérer les faux bulletins de salaire et les fraudeurs
> - te rappelle les échéances Alur, déclaration, paperasse
>
> Et basta. Pas de gestion locative full, pas d'agence. Juste ce mille-feuille-là, en pilote automatique.
>
> Est-ce que tu **signerais aujourd'hui** à 19€/mois ? Si non, qu'est-ce qu'il manque pour que tu signes ?"

**Critère H2 ★** : "Oui, où je signe" (ou équivalent net) sans condition rédhibitoire = **+1 calls_positive**.

Variantes de réponse à noter :
- "Oui mais à 9€" → signal de non WTP, à comptabiliser comme NÉGATIF pour H2 (objectif 19€).
- "Oui mais il faut que ça inclue X" → noter X (feature must-have).
- "Non parce que je fais déjà ça avec Y" → noter Y (concurrence active).
- "Non parce que c'est pas mon problème" → H1 invalidée pour ce lead.

---

## Fermeture (2 min)

> "Merci, c'est très clair. Pour info : je suis en train de prototyper exactement ça. Tu veux que je te recontacte quand il y a un premier truc à tester ? Aucun engagement."

→ Si oui : récupérer email (à stocker chiffré, pas en clair), tag `waitlist` dans `leads.jsonl`.

> "Dernière question : tu connais 1 ou 2 bailleurs autour de toi qui pourraient avoir les mêmes galères ?"

→ Si oui : noter les noms/contacts pour sourcing futur.

---

## Post-call (10 min, juste après)

1. Mettre à jour `leads.jsonl` : status `call-done` + `positive`/`negative`/`neutral` selon H2.
2. Ajouter insights bruts dans `hypotheses.md` section "Insights bruts".
3. Cocher les hypothèses validées/invalidées pour ce lead.
4. Si insight surprenant → ligne dans `ledger.md` type INSIGHT.

---

## Compteur go/no-go

- **Go (Phase 2 débloquée)** : ≥5/10 calls_positive sur H2.
- **Pivot (vers angle A ou C)** : ≤2/10 positifs ET signal récurrent sur autre angle.
- **No-go (drop projet)** : ≤2/10 ET aucun signal alternatif sur 10 conversations.

À 5 calls : faire un **mid-point review** (entrée dédiée dans `ledger.md` type AUDIT) avant d'enchaîner les 5 suivants.

---

**Statut** : DRAFT, en attente validation Florian (sur le pitch §Q4 surtout : la formulation à 19€ est le test critique).
