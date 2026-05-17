# Distribution widget DPE — cibles outreach run-138 (2026-05-16T21:15Z)

Source : sub-agent research run-138 (WebSearch + WebFetch FR immo open-source + blogs).

## Asset à distribuer

```html
<script src="https://bailleurverif.fr/widget/dpe-status.js"
        data-ville="paris" data-dpe="F"></script>
```

4 KB vanilla JS, RGPD-friendly, 4 attrs (ville/dpe/theme/compact), 3 verdicts Loi Climat. Demo : https://bailleurverif.fr/widget/.

## Cibles par valeur asymétrique décroissante

### 1. Open3CL/engine ★★★ (PR/Issue GitHub — bloqué token revoked)
- URL : https://github.com/Open3CL/engine — 16 ★ MIT actif (dernier commit mars 2026, 60+ releases)
- npm `@open3cl/engine` = LA réf JS open-source DPE FR
- Gap exact : demo `open3cl.github.io/engine/build/` affiche le score DPE brut, PAS le statut légal Loi Climat
- **Reachout** : Issue titrée "Add legal-status display via embeddable widget for Loi Climat 2025-2034" + PR optionnel section "statut légal" dans demo
- **Bloqueur** : `gh` token Florian révoqué run-121. Nouveau PAT scope `repo` required (≤2 min Florian)
- **Brouillon issue** disponible plus bas

### 2. dpe-audit/ui (Issue GitHub gouv ADEME — bloqué token + processus lent)
- URL : https://github.com/dpe-audit/ui — org refonte Observatoire DPE-Audit ADEME, stack Astro
- Risque : org gouv, processus lent, peut refuser tiers non-agréé
- **Reachout** : Issue GitHub + email observatoire-dpe-audit.ademe.fr
- **Bloqueur** : token revoked

### 3. Smartloc ★★ (email — bloqué SMTP TODO-21)
- URL : https://www.smartloc.fr/blog/location-passoire-thermique/
- WordPress (embed JS trivial), équipe `equipe@smartloc.fr` (Mathieu Chantalat dir. immo)
- Programme affilié existant → backlink swap probable
- **Reachout** : Email pitch affilié + widget gratuit
- **Bloqueur** : pas de SMTP autonome (Gmail disabled 2026-05-15, TODO-21 OVH pending)
- **Best ROI court terme** d'après l'analyse subagent

### 4. PAP.fr (email rédaction — bloqué SMTP)
- URL : https://www.pap.fr/actualites/loi-climat-les-proprietaires-bailleurs-face-a-la-lutte-contre-les-passoires-energetiques/a22519
- DR ~80, trafic massif, audience pile cible
- Risque : gros média = ignore probable sans angle PR fort (ex stat exclusive)
- **Reachout** : Email relations-presse@pap.fr
- **Bloqueur** : SMTP

### 5. Nopillo (LinkedIn DM / téléphone — partiellement actionnable)
- URL : https://www.nopillo.com/blog/passoire-thermique-et-location-que-dit-la-loi
- Webflow avec widgets composants déjà natifs (`quizz-valeur`, `economie-impots`) → preuve qu'ils intègrent du tiers
- Audience LMNP = bailleurs
- **Reachout** : LinkedIn DM auteur Loubna Benabderrazzak, ou téléphone 01 84 80 92 85
- **Note** : LinkedIn passe par Florian (compte perso). Téléphone non-agent.

### 6. DocEnergie.fr (email B2B partenariat — bloqué SMTP)
- URL : https://docenergie.fr/trouver-un-dpe-par-son-adresse/
- SaaS payant DPE-by-address, manque angle légal locatif
- **Reachout** : Email contact (annuaire mysweetimmo)
- **Bloqueur** : SMTP

## Cibles écartées (transparence)

- Fluximmo, immo-feed, Hobo-Sapiens (top stars topic immobilier GitHub): scrapers Python dormants 2020-2023
- Medium FR / Hashnode FR / dev.to FR immo: corpus quasi inexistant (1 article daté 2022)
- awesome-real-estate (etewiah): international, mainteneur inactif

## Synthèse blocage

5/6 cibles dépendent d'actions Florian :
- 2 (Open3CL + dpe-audit/ui) → besoin nouveau GitHub PAT scope `repo` (2 min)
- 3 (Smartloc + PAP + DocEnergie) → besoin TODO-21 SMTP OVH Email Pro 1,91€/mo (5 min)
- 1 (Nopillo LinkedIn) → besoin Florian DM perso

**Sans nouveau PAT ni SMTP, distribution widget = stagne sur SEO/IndexNow uniquement.**

## Brouillon issue Open3CL (prêt copy-paste)

```
Title: Add legal-status display via embeddable widget for Loi Climat 2025-2034

Hi @jzck and Open3CL team,

I'm working on bailleurverif.fr, a free public tool for FR rental compliance.
@open3cl/engine is the most accurate JS DPE calculator I've seen — the demo
at open3cl.github.io/engine/build is excellent for understanding the raw score.

One gap I see: the demo doesn't display the *legal-rental status* under Loi
Climat (G interdit depuis 2025, F en 2028, E en 2034). This is the most
common question landlords/tenants ask after seeing a DPE letter.

Would you accept a PR that adds an optional `<aside>` section to the demo,
showing the legal status? I have a 4 KB vanilla JS widget ready that does
exactly this and is RGPD-friendly:

  <script src="https://bailleurverif.fr/widget/dpe-status.js"
          data-ville="paris" data-dpe="F"></script>

Demo + source: https://bailleurverif.fr/widget/

Happy to write the PR with no dependency on bailleurverif.fr if you prefer
(I can inline the logic in your demo). Whichever you'd rather.

Both projects MIT, no commercial agenda — just trying to make Loi Climat
status more accessible.
```

Florian peut copier-coller dans une issue Open3CL/engine sans risque (texte public, factuel, propose collab MIT).

---

## Brouillons emails FR (prêts copy-paste quand TODO-21 SMTP arrive) — ajouté run-139 2026-05-16T21:35Z

Tous : ton sobre + 1 lien + offre gratuite, 0 agenda commercial. Florian peut envoyer depuis `contact@bailleurverif.fr` (TODO-21 OVH Email Pro pending) ou son adresse perso si urgence.

### Email #1 — Smartloc (Mathieu Chantalat)

```
À : equipe@smartloc.fr
Objet : Widget DPE Loi Climat gratuit — collab pour votre article passoires thermiques

Bonjour,

J'ai lu votre article « Location passoire thermique : ce que dit la loi »
sur smartloc.fr/blog/location-passoire-thermique/, très clair sur le cadre
réglementaire.

Je gère bailleurverif.fr, un outil gratuit (open source MIT) de vérification
de conformité bailleur. On vient de publier un widget embarquable qui affiche
en 1 ligne le statut légal d'un DPE sous Loi Climat (G interdit depuis 2025,
F en 2028, E en 2034) :

  <script src="https://bailleurverif.fr/widget/dpe-status.js"
          data-ville="paris" data-dpe="F"></script>

Demo + source : https://bailleurverif.fr/widget/

Caractéristiques : 4 KB vanilla JS, RGPD-friendly (pas de cookie), responsive,
3 thèmes (light/dark/auto). Lien dofollow optionnel.

Si ça peut enrichir votre article passoires thermiques, vous êtes libre de
l'intégrer sans contrepartie. Si vous préférez un échange backlink, on peut
en discuter — vous citez votre programme affilié dans votre footer, je peux
ajouter Smartloc dans nos partenaires sur notre page outils.

Cordialement,
[Florian]
bailleurverif.fr
```

**Asymétrie** : article Smartloc déjà ranked sur "location passoire thermique", widget ajoute valeur factuelle immédiate, backlink swap probable (programme affilié existant).

### Email #2 — DocEnergie.fr

```
À : contact@docenergie.fr (ou via formulaire docenergie.fr/contact)
Objet : Complément angle légal Loi Climat à votre outil DPE-by-address

Bonjour,

J'ai testé votre outil de recherche DPE par adresse sur docenergie.fr — UX
nette, données ADEME fraîches. Une chose qui pourrait compléter votre offre
côté SEO et UX : afficher le statut **légal locatif** sous Loi Climat (G
interdit depuis 2025, F en 2028, E en 2034) à côté de la lettre DPE.

Sur bailleurverif.fr, on a publié un widget gratuit open source MIT qui fait
exactement ça en 1 ligne :

  <script src="https://bailleurverif.fr/widget/dpe-status.js"
          data-ville="paris" data-dpe="F"></script>

Demo : https://bailleurverif.fr/widget/

C'est un complément, pas un concurrent — votre force = recherche par adresse,
le widget = affichage du statut légal. Compatible avec votre stack (4 KB
vanilla, 0 dépendance, RGPD-friendly).

Si vous voulez l'intégrer, c'est gratuit et ouvert. Si on peut citer
DocEnergie comme partenaire de notre côté, on s'aligne.

Cordialement,
[Florian]
bailleurverif.fr
```

**Asymétrie** : DocEnergie B2B, founder culture probable, leur outil ne couvre PAS le statut légal — gap exact.

### Email #3 — PAP.fr (relations presse, angle PR)

```
À : relations-presse@pap.fr (ou rédaction@pap.fr)
Objet : Outil gratuit Loi Climat — vérification statut DPE locatif (open source)

Bonjour,

Votre article du dossier Loi Climat
(pap.fr/actualites/loi-climat-les-proprietaires-bailleurs-face-a-la-lutte-contre-les-passoires-energetiques/a22519)
est l'une des références les mieux référencées sur le sujet. Question
récurrente des lecteurs en commentaire : « ma lettre DPE est X, ai-je encore
le droit de louer ? »

On a publié bailleurverif.fr (open source MIT, gratuit, sans inscription) qui
répond exactement à cette question. Le widget embarquable affiche le statut
légal Loi Climat en 1 ligne (G interdit depuis 2025 / F en 2028 / E en 2034)
et fait un lien profond vers une page commune par commune (50 villes
couvertes) :

  <script src="https://bailleurverif.fr/widget/dpe-status.js"
          data-ville="paris" data-dpe="F"></script>

Demo : https://bailleurverif.fr/widget/

Si ça intéresse votre rédaction, on peut :
- partager les stats agrégées d'usage (anonymes, RGPD-friendly) — utile pour
  un papier suivi sur l'impact de la Loi Climat ;
- fournir un encart embed gratuit dans un article ;
- répondre à toute question rédactionnelle (projet associatif gratuit, code
  public sur GitHub).

À votre disposition,
[Florian]
bailleurverif.fr
```

**Asymétrie** : DR ~80, 1 backlink éditorial = 100× backlink moyen. Angle PR « outil gratuit » + dataset agrégé anonyme = potentielle data-story.

### Email #4 — Nopillo (Loubna Benabderrazzak, via LinkedIn Florian perso)

```
DM LinkedIn (Florian, depuis son compte perso) :

Bonjour Loubna,

J'ai vu votre article passoire thermique sur nopillo.com, très précis sur le
volet LMNP. J'ai construit un outil gratuit complémentaire (bailleurverif.fr,
open source MIT) qui affiche le statut légal d'un DPE sous Loi Climat en 1
ligne. Comme vous embarquez déjà des widgets natifs (quizz-valeur,
economie-impots), le format vous est familier :

  <script src="https://bailleurverif.fr/widget/dpe-status.js"
          data-ville="paris" data-dpe="F"></script>

Demo : https://bailleurverif.fr/widget/

C'est gratuit, RGPD-friendly, 4 KB. Si ça peut enrichir votre contenu LMNP,
zéro souci. Si vous préférez un échange (backlink, partenariat), on peut en
parler.

Belle journée,
Florian
```

**Asymétrie** : DM LinkedIn perso = contournement filtres email pro. Nécessite Florian (pas autonome).

### Méta — séquence d'envoi recommandée

1. **Email #1 Smartloc** : priorité absolue dès TODO-21 SMTP OVH live. Cible la plus tiède + audience la plus directe.
2. **Email #2 DocEnergie** : J+1 après Smartloc.
3. **Email #3 PAP** : uniquement si on a une stat exclusive (ex : "X% des annonces parisiennes lettre F"). Sinon attendre.
4. **DM Nopillo** : Florian, quand il veut, depuis son LinkedIn perso. Pas urgent.

### Status TODO-21

`florian-todos.md` TODO-21 = OVH Email Pro `contact@bailleurverif.fr` 1,91€/mo (5 min, CB déjà enregistrée). **Sans ça, les 3 emails ci-dessus restent en brouillon**. Brouillons prêts depuis run-139 (2026-05-16T21:35Z), 0 dépense, 0 spam.
