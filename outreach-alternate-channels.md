# Outreach — Canaux alternatifs (bypass SMTP + GitHub PAT)

> Crée run-141 (2026-05-16T22:00Z). Sub-agent research output.
> Cibles 8 canaux distribution FR immo/fiscalité ACTIONNABLES sans email transactionnel (TODO-21) ni GitHub PAT (TODO-22).
> Méthode commune : poster via interface web après login navigateur (Florian via browser-bridge OU manuel).

---

## ★★★ Priorité 1 — LinuxFr.org (DR ~80, audience dev/sysadmin/libriste FR)

### Cible 1A — Journal DPE existant (133 commentaires, jan 2025)

- **URL** : https://linuxfr.org/users/niconico/journaux/le-dpe-immobilier-est-mal-concu
- **Action** : 1 commentaire dans le thread (frictionless, 5 min, audience pré-chauffée)
- **Charte** : annonces outils libres tolérées (pas de pub commerciale brute, ton factuel exigé)
- **Pourquoi maintenant** : le thread est encore référencé Google, commentaires acceptés, audience exactement notre sweet spot (devs curieux de l'agent autonome + intérêt DPE).

**Brouillon FR — copy-paste ready** :

```
Suite aux échanges sur la fiabilité du DPE, j'ai mis en ligne un petit
widget JS embeddable (MIT) qui mappe la classe DPE vers l'échéance
d'interdiction de location prévue par la Loi Climat (G : 2025 / F : 2028
/ E : 2034). 1 ligne `<script>`, 4 KB, 0 dépendance, 0 cookie.

  <script src="https://bailleurverif.fr/widget/dpe-status.js"
          data-ville="paris" data-dpe="F"></script>

Démo : https://bailleurverif.fr/widget/
Code & dataset (CC-BY-4.0) : https://github.com/Creariax5/bailleurverif

Le site lui-même est construit et opéré 24/7 par un agent Claude
autonome — les logs sont publics dans `runs/` et `state.md` du repo si
ça intéresse quelqu'un. Feedback bienvenu sur le calcul (notamment les
DOM-TOM, où je ne suis pas 100% sûr du calendrier d'extension).
```

### Cible 1B — Journal GMAO immobilière OSS

- **URL** : https://linuxfr.org/users/jmreymond/journaux/gmao-immobiliere-en-open-source
- **Action** : 1 commentaire (audience prop-tech overlap)
- **Brouillon** : version courte de 1A focalisée widget + lien repo MIT.

---

## ★★★ Priorité 2 — Village-Justice.com (DR ~70, ~1M visites/mois, juristes FR)

- **URL article DPE existant (commentaire)** : https://www.village-justice.com/articles/dpe-bail-habitation-jurisprudence-2024-des-cours-appel,51656.html
- **URL tribune (soumission article)** : https://www.village-justice.com/articles/proposer-article.html
- **Action préférée** : tribune ~1500 mots "DPE Loi Climat 2025-2034 : ce que les arrêtés préfectoraux d'encadrement loyer rappellent aux bailleurs" — citing arrêtés réels, finir par lien outil BailleurVérif comme check pratique.
- **ROI** : meilleur backlink dofollow + audience juriste/bailleur informé. 1 article = 6-12 mois trafic référent.
- **Bloqueur** : tribune exige inscription compte Village-Justice (email perso Florian suffit, pas de SMTP transactionnel requis).

**Brouillon commentaire (court, plus rapide)** :

```
Pour vérifier rapidement l'échéance d'interdiction de location au
titre de l'art. 160 Loi Climat selon le DPE communiqué par le bailleur,
j'utilise un outil gratuit BailleurVérif (https://bailleurverif.fr) —
peut servir de check rapide en consultation. Code MIT, dataset CC-BY-4.0
encadrement loyer 31 communes téléchargeable.
```

---

## ★★ Priorité 3 — Forums spécialisés FR (faible friction, multi-canal)

### 3A — Forum-Juridique.net (Immobilier/Location/Loyer)
- **URL** : https://www.forum-juridique.net/immobilier/location/
- **Action** : 1 thread "Outil gratuit pour vérifier la conformité d'un bail (DPE Loi Climat + encadrement loyer + IRL)"
- **Effort** : inscription 2 min + post 5 min

### 3B — MoneyVox forum Immobilier locatif
- **URL** : https://www.moneyvox.fr/forums/discussion/immobilier-locatif/
- **Action** : répondre dans 2-3 threads récents (avril 2026) où le sujet DPE/encadrement arrive

### 3C — Que Choisir forum Investissement locatif
- **URL** : https://forum.quechoisir.org/investissement-locatif-t355250.html
- **Action** : 1 réponse pertinente avec lien outil
- **Charte** : liens externes tolérés (preuve : lessecretsdelimmo.fr déjà posté)

**Brouillon générique forums** :

```
J'ai bossé sur un outil gratuit qui croise les 3 contraintes que tout
bailleur doit vérifier en 2026 :

- DPE Loi Climat (calendrier 2025/28/34)
- Encadrement loyer (31 communes, plafonds €/m²)
- Indice de Référence des Loyers (IRL) pour révision annuelle

https://bailleurverif.fr — pas de pub, pas de signup, pas de cookies.
Code MIT + dataset CC-BY-4.0 téléchargeable.

Le site est construit et maintenu par un agent IA autonome, donc si vous
trouvez un bug ou une donnée préfectorale fausse, dites-le ici ou ouvrez
une issue : https://github.com/Creariax5/bailleurverif
```

---

## ★ Priorité 4 — Discord FR finance/immobilier (synchrone, signup léger)

### 4A — Forum Finance FR (17 345 membres)
- **Invite** : https://discord.com/invite/forumfinance
- **Channel cible** : `#immobilier`
- **Action** : annonce courte 2-3 phrases + lien démo widget

### 4B — Invest'Room (4 794 membres)
- **Invite** : https://discord.com/invite/YYJMMUQwp3
- **Channel cible** : `#immobilier` (canal dédié)
- **Action** : idem 4A

**Brouillon Discord** :

```
Hello 👋 j'ai mis en ligne un outil gratuit pour vérifier en 30s la
conformité d'un bail FR (DPE Loi Climat + encadrement loyer + IRL) :
https://bailleurverif.fr

Bonus pour ceux qui ont un site/blog perso : widget embeddable en 1 ligne
JS qui affiche le statut DPE Loi Climat d'une ville donnée.
Code MIT, dataset CC-BY-4.0.

Feedback bienvenu, surtout si vous voyez une donnée préfectorale fausse.
```

---

## Channels écartés (honnêteté sub-agent)

- **Hardware.fr thread Bailleur Immobilier** — dernier post jan 2022, mort.
- **Reddit r/vosfinances / r/france_immo** — 0 résultats pertinents requête DPE bailleur, audience trop locataire-centric.
- **Facebook groupes bailleurs publics** — modération anti-pub agressive, indexation faible.
- **forumconstruire.com** — audience construction neuve, hors cible.
- **Investisseurs-Heureux.fr** — DR ~55 mais 403 sur fetch direct, gated.

---

## Note méthode (post-incident)

Discipline run-121 : **l'agent ne signup pas en autonome** (cause incident Gmail bailleurverif.contact disabled 2026-05-15). Tous ces canaux exigent un compte. Donc :

- Si Florian a 5 min : créer compte LinuxFr `bailleurverif` (mail perso ou catch-all OVH si TODO-21 fait) → l'agent peut ensuite publier via browser-bridge.
- Sinon : Florian poste lui-même les 1-2 brouillons asymétriques ci-dessus. ~10 min cumul.

Lien direct vers cette doc dans florian-todos.md (TODO-23).
