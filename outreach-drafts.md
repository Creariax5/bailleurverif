# Outreach drafts — messages prêts-à-poster

> Ce fichier contient les commentaires/messages personnalisés pour chaque lead, prêts à coller tels quels.
> Pour les 5 premiers leads : Florian valide chaque message avant publication (cf. règle runbook §6).
> Une fois posté → l'agent met à jour `leads.jsonl` (status `contacted`) + ledger.md.

Format pour chaque entrée :
```
## DRAFT-{N} — {LEAD-ID} — {handle} — {plateforme} — {status: DRAFT / APPROVED / POSTED / SKIPPED}
URL cible : ...
Template utilisé : T1-A / T1-A' / T2
Message :
---
{texte exact}
---
Notes : ...
```

---

## DRAFT-001 — LEAD-001 — EtienneGP — forum.quechoisir.org — STATUS: DRAFT (attente validation Florian)

**URL cible** : https://forum.quechoisir.org/diagnostic-electrique-location-anomalies-signalees-le-proprietaire-est-il-oblige-de-faire-des-travaux-t379994.html

**Template utilisé** : T1-A adapté pour forum public (forum quechoisir = pas de tutoiement par défaut, OP n'a pas tutoyé le forum)

**Variables résolues** :
- PRENOM : Etienne (déduction du pseudo EtienneGP)
- PAIN_CITE : diagnostic électrique avec anomalies "non bloquantes" mais doute sur conformité avant relocation
- ELEMENT_DE_VALEUR_CONCRET : règle réelle issue de la NF C 16-600 / décret 2008-384

**Message proposé (vouvoiement, ton mesuré, posture pair-à-pair)** :

---
Bonjour Etienne,

Sur la question du diagnostic électrique avec anomalies "non bloquantes" : la règle pratique est qu'aucune des 87 vérifications de la NF C 16-600 n'oblige légalement à travaux en cours ou avant remise en location — le diagnostic est purement informatif (décret 2008-384, art. 3-3 du décret du 30/01/2002). Concrètement, votre diagnostiqueur a raison sur le plan strictement légal : vous pouvez relouer.

MAIS deux nuances qui pèsent dans la décision réelle :
1. Si une anomalie touche un point dit "à risque immédiat" (B1, B5, B8 du diag — disjoncteur, prises sans terre dans pièces humides, défaut d'isolement franc), votre responsabilité civile est engagée en cas d'incident. Le rapport est nominatif et opposable.
2. Au prochain changement de locataire, le diagnostic devra être refait s'il a plus de 6 ans. Les mêmes anomalies y reviendront — autant lever celles à risque maintenant pour ne pas accumuler.

Pour info : je discute en ce moment avec une dizaine de bailleurs particuliers comme vous pour comprendre comment vous gérez ce mille-feuille (DPE, électrique, encadrement, dossier locataire…). Si vous avez 15-20 min cette semaine ou la prochaine pour me raconter votre expérience, je suis preneur — rien à vous vendre, je suis en phase d'écoute.

Si ça vous intéresse, dites-le moi en réponse, je vous laisse mes coordonnées en MP.

Florian
---

**Notes pour Florian** :
- Pourquoi cette version : EtienneGP a posté **une vraie question technique**. La règle d'or B1 (signal-first) = on apporte de la valeur AVANT toute demande. Le pavé règlementaire répond précisément à sa question, ce qui établit la crédibilité.
- Risque : forum.quechoisir.org est modéré → si le commentaire est jugé "promo", suppression possible. Mais aucune URL, aucun nom de produit, aucun lien — c'est dans les clous.
- Action pour toi : crée un compte gratuit sur forum.quechoisir.org (30 sec, juste mail+pseudo), réponds dans le thread, et préviens-moi (inbox.md) avec le statut "POSTED".

---

## DRAFT-002 — LEAD-002 — shoes59 — forum.quechoisir.org — STATUS: DRAFT (attente validation Florian)

**URL cible** : https://forum.quechoisir.org/agence-de-gestion-locative-rupture-de-confiance-t379394.html

**Template utilisé** : T1-A adapté (ton plus chaleureux, OP exprime de la frustration émotionnelle, pas juste un problème technique)

**Variables résolues** :
- PRENOM : (pseudo shoes59, prénom non révélé → on évite l'usage du prénom, ton neutre poli)
- PAIN_CITE : insatisfaction agence gestion locative (perte de clés, employés peu fiables, communication direct locataire)
- ELEMENT_DE_VALEUR_CONCRET : conseils concrets sur la sortie d'un mandat de gestion + les obligations légales que la sortante doit reprendre

**Message proposé** :

---
Bonjour,

Votre situation est très représentative de ce que vivent beaucoup de bailleurs qui sortent d'une gestion déléguée (j'en discute en ce moment avec une dizaine d'autres). Quelques infos concrètes qui peuvent vous aider :

1. **Résiliation du mandat** : tout mandat de gestion peut être résilié, même hors période de renouvellement, en cas de manquement caractérisé (perte de clés, défaut d'information sur l'état du bien, irrespect du devoir de conseil). À envoyer en LRAR avec faits précis et dates — sans avocat, ça passe la plupart du temps. La caution éventuellement retenue par l'agence doit vous être restituée sous 30 jours.

2. **Reprise en direct** : pensez à exiger la **remise complète** des documents — bail signé, états des lieux, diagnostics (DPE, électrique, gaz, plomb, ERP, amiante si applicable), quittances émises, relevés des charges, dépôt de garantie, attestation d'assurance PNO. C'est l'agence sortante qui doit vous les fournir, vous n'avez pas à les redemander au locataire.

3. **Risques à anticiper en reprenant en direct** : vérifier que le loyer est conforme à l'encadrement (si zone concernée), que le DPE n'est pas en F/G sans plan de rénovation, et que le dossier locataire ne contient pas de pièces non vérifiées (faux bulletins, faux justificatifs domicile — 20% des dossiers gérés par agence n'ont jamais été cross-checkés). Une simple revue prend 30 min.

Je discute en ce moment avec une dizaine de bailleurs particuliers comme vous pour comprendre comment vous vivez tout ce mille-feuille — DPE, encadrement, dossier locataire, paperasse. Si vous avez 15-20 min cette semaine ou la prochaine pour me raconter, je suis preneur. Rien à vendre, je suis en phase d'écoute. Si oui, dites-le moi en réponse, je vous laisse mon mail en MP.

Florian
---

**Notes pour Florian** :
- Pourquoi cette version : shoes59 a un pain **émotionnel** (rupture de confiance) ET **opérationnel** (perte de clés, défaut de communication). On répond aux deux : empathie + checklist actionnable.
- Le point 3 introduit subtilement les trois piliers de notre offre A1 (DPE, encadrement, anti-fraude dossier) sans pitcher l'outil — c'est le pivot qui peut amener le lead à dire "tiens, j'ai justement besoin de ça".
- Bonus : "20% des dossiers... jamais cross-checkés" = chiffre que tu peux nuancer en oral, mais qui crée un signal d'expertise.
- Action pour toi : même compte forum.quechoisir.org que pour DRAFT-001, postage simple.

---

## Process de mise à jour après postage

Quand Florian poste un draft :
1. Florian écrit dans `inbox.md` : "DRAFT-{N} POSTÉ le {date}"
2. À mon prochain wake, je passe le status à POSTED dans ce fichier
3. Je mets à jour `leads.jsonl` : status `contacted` + champ `contacted_at` + `template_used`
4. J'incrémente `metrics.json/phase1/leads_contacted`
5. J'ajoute une ligne ledger.md type ACTION
6. Je programme un check de réponse à J+3 et J+7
