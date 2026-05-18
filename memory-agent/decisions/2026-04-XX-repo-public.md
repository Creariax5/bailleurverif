# Décision : Repo GitHub public MIT

**Date** : ~2026-04-XX (avant pivot B2C run-95, date exacte à clarifier git log)
**Status** : DONE

## Décision

Repo `Creariax5/bailleurverif` rendu public sous licence MIT.

## Pourquoi

- Crédibilité technique externe (DR 90 GitHub naturellement)
- Crypto-timestamp commits publics = antériorité observable rétroactivement (cat-1 moat support)
- Open-source attrait dev FR proptech (cf. visiteur Open3CL #160 2026-05-18)
- Pas de secret commercial à protéger (calculs encadrement = règles publiques)

## Risque géré

Concurrent peut fork → mais série temporelle horodatée par commit = non-rejouable rétroactivement. Le code est copyable, **l'historique cryptographique ne l'est pas**.

## Files associés

- `LICENSE` (MIT)
- `README.md` (présentation projet)
- `.github/` workflows CI
- `/llms.txt` (LLM-friendly summary)

## URL canonique

`https://github.com/Creariax5/bailleurverif`

## Commits cryptographiques notables

- `cf51c00` 1ʳᵉ vague observatoire
- `075b344` 9ᵉ vague observatoire (run-XXX)
- `8840c77` crypto-timestamp run-XXX
