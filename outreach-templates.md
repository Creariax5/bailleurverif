# Templates d'approche — DRAFT (à valider par Florian)

> 2 templates : T1 = réponse publique à un post (méthode B1/C1 recommandée), T2 = DM/email cold (fallback).
> **Aucun envoi tant que Florian n'a pas validé.** Pour les 5 premiers leads, validation lead-par-lead obligatoire (cf. runbook §6).

---

## T1 — Réponse publique à un post Finary/Reddit/LinkedIn

**Contexte d'usage** : un bailleur a publié un post qualifiant (galère DPE / encadrement / fraude / Alur). Je réponds en commentaire public, avec une valeur réelle d'abord, sans pitcher. Si traction → DM.

**Variables** : `{PRENOM}`, `{PAIN_CITÉ}` (ex : "le DPE F sur ton T3 à Lyon"), `{ELEMENT_DE_VALEUR_CONCRET}` (1-2 lignes utiles : date limite, montant amende, lien officiel, retour terrain).

### Version A — "Apport de valeur + curiosité"

```
Salut {PRENOM},

Je suis tombé sur ton post sur {PAIN_CITÉ}. Petit retour qui peut aider :
{ELEMENT_DE_VALEUR_CONCRET}.

De mon côté je discute en ce moment avec une dizaine de bailleurs particuliers
pour comprendre comment vous gérez tout le mille-feuille réglementaire
(DPE, encadrement, dossiers, échéances). Si tu as 15-20 min cette semaine ou
la prochaine pour me raconter ton expérience, je suis preneur — sans rien à
te vendre, je suis en phase d'écoute.

Tu peux me MP si ça t'intéresse.
```

**Notes Florian** :
- Ton volontairement bas, pas de produit mentionné (cohérent avec D1).
- Le "rien à te vendre" est vrai à ce stade et lève une partie de la garde.
- Variante possible si Florian veut signaler qu'un outil est en préparation (D2).

### Version A' — Variante "D2" (mention discrète qu'on prépare quelque chose)

Identique sauf dernière phrase :
```
...je suis en train de préparer un outil pour aider sur ce type de galère,
mais aujourd'hui je veux d'abord comprendre les vôtres avant de coder quoi
que ce soit.
```

→ À choisir selon directive Florian (D1 ou D2).

---

## T2 — DM/email cold (fallback uniquement)

**Contexte d'usage** : pas de post public récent, mais profil qualifié identifié.
**Précaution** : RGPD plus risqué, à n'utiliser que si Florian valide B2 ou B3.

```
Bonjour {PRENOM},

Petit message direct, je vais à l'essentiel : je discute en ce moment
avec ~10 propriétaires bailleurs particuliers (1-5 biens) pour comprendre
comment vous vivez la pile réglementaire qui s'empile depuis 2 ans —
DPE, encadrement des loyers, vérification dossier locataire, échéances
administratives.

Je ne vends rien à ce stade, je suis en phase d'écoute.

Est-ce que vous auriez 15-20 min cette semaine ou la prochaine pour échanger ?
Je m'adapte à votre dispo. Si le sujet ne vous parle pas du tout, dites-le
moi simplement et je ne reviens pas.

Bien à vous,
Florian
```

**Notes Florian** :
- Phrase "si ça ne parle pas, dites-le" = facilite l'opt-out + diminue intrusivité perçue.
- Pas de lien, pas de logo, pas de prétention de marque (D1).

---

## Règles communes

1. **Pas de mensonge** : ne jamais dire "j'ai déjà X clients" ou "produit dispo" tant que faux.
2. **Pas de scarcity fake** ("seulement 3 places dispos") — gold standard d'authenticité.
3. **Personnalisation obligatoire** : `{PAIN_CITÉ}` doit être ce que la personne a réellement écrit, pas générique.
4. **Tracking** : chaque envoi → mise à jour `leads.jsonl` (status `contacted`, notes = template utilisé + date).
5. **Pas de relance** avant J+5. Une seule relance max, puis abandon courtois.

---

## Process validation Florian (5 premiers leads)

Pour chaque lead 1 à 5 :
1. Je propose le lead (URL + handle + persona) + le template ciblé pré-rempli avec `{variables}` résolues.
2. Florian dit GO / NO-GO / éditer.
3. Envoi seulement après GO.
4. Log dans `leads.jsonl`.

À partir du lead 6, je peux envoyer les variantes validées sans approbation lead-par-lead, en loggant simplement.

---

**Statut** : DRAFT, en attente validation Florian (texte + choix D1/D2).
