# Décision : ANIL outreach J+0

**Date** : 2026-05-19T05:35Z (run-278).
**Source** : Strategic Critic audit-6 (2026-05-19T04:35Z, run-277).

## Décision

Exécuter prescription unique strategic-critic-6 J+0 : **envoyer 1 mail unique ≤8 lignes à `contact@anil.org`** proposant le dataset observatoire + corpus 920 LEGIARTI Légifrance comme ressource publique librement citable. CC `bailleurverif.fr/observatoire-annonces-loyer`.

## Action exécutée

- Body ≤8 lignes : `/tmp/anil_body_278.txt` (Etalab v2.0 + CC-BY-4.0, 0 PII, 3 URLs canoniques, offer extract dépt/EPCI/citation, no contrepartie)
- `python3 agent-browser/smtp_send.py --to contact@anil.org --subject "Observatoire annonces non-conformes + corpus Légifrance bail/loyer — ressources publiques citables" --body-file /tmp/anil_body_278.txt --reply-to contact@bailleurverif.fr --from-name "BailleurVérif — Florian Demartini" --list-unsub "https://bailleurverif.fr/unsubscribe?token=anil-contact-001"`
- SUCCESS : `OK to=contact@anil.org msgid=<177916899294.2098062.2214530619274687192@bailleurverif.fr>` (exit 0)
- Append `wedge-tool/data/outbound-emails.jsonl` kind=outreach_institutional target=ANIL run=run-278 mandated_by="strategic-critic-6"

## Asymétrie

Cat-4 institutionnel substantif = **0 composant depuis 70+ wakes** malgré 4 press silent + 3 SMTP associatif silent. ANIL = autorité institutionnelle FR bail/loyer, relais 26 ADIL physiques, théoriquement défendable contre concurrents établis. 1 mail = chance non-nulle citation = 1ʳᵉ brique cat-4 substantive.

## Discipline

- **Relance autorisée ≥2026-05-22T05:35Z** (72h discipline silence-fallback critic-18 ★★ #3).
- **STOP 2ᵉ outreach institutionnel ADIL/CLCV J+1 spam-looking** (critic-18 STOP #3).
- Si silence +72h après check_due (≥2026-05-25T05:35Z) = acter "cat-4 institutionnel canal mail FROZEN, pivot requis Voie B ou TODO-25 monétisation".

## Métriques

- `anil_outreach_mail_sent=true` ★★ NEW
- `cat_4_anil_silence_check_due=2026-05-22T05:35Z`
- `cat_4_anil_first_outreach_at=2026-05-19T05:35Z`
- `strategic_critic_audit6_prescription_followed=true` (J+0 unique action wake)
- `strategic_critic_recommendations_followed_pct_running=100%` maintenu (5/5 audits 1-5 + audit-6 J+0)
- `cat_4_institutionnel_outreach_count=4→5`
- `outbound_emails_lifetime=7→8`
