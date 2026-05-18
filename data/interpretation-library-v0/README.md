# Interpretation Library v0 — BailleurVérif Recourse Templates

Open-data corpus of structured legal-recourse templates for French rental contentious situations (locataire ↔ bailleur).

**License**: CC-BY-4.0 (attribution: `BailleurVérif — https://bailleurverif.fr`)
**Live API**: `https://bailleurverif.fr/api/recourse` (JSON list) / `https://bailleurverif.fr/api/recourse/<tag>` (single template, ETag + 304 + Cache-Control public max-age=3600)
**Source repository**: `https://github.com/Creariax5/bailleurverif`

## Schema (v0, 23 keys)

Each template is a JSON object with:

- `tag` — short slug (`loyer-abusif`, `dpe-invalide`, `depot-garantie-non-restitue`, ...)
- `version` — semver (`v0`)
- `wave_ts` — UTC timestamp of template authoring (crypto-anchored via git history)
- `wake_id` — internal agent wake reference (`run-NNN`)
- `scope` — applicability domain (zone tendue, résidence principale, etc.)
- `legal_basis_citations` — array of 5 statutory references (Code civil, Loi 89-462, Loi Climat 2021-1104, décrets, etc.)
- `applicability_checks` — 5 binary criteria to verify the tenant qualifies
- `procedure_steps` — 5 ordered steps (proof gathering → RAR amiable → CDC → administrative regulator → judicial)
- `sample_letter_md` — markdown courrier RAR with named placeholders (`{{adresse_logement}}`, `{{date_signature}}`, etc.)
- `regulator_contacts` — 4 fiches (CDC, ADIL, TJ/juge des contentieux, préfet/DRIHL-DDETS, UFC-Que-Choisir)
- `expected_resolution_p50_days` / `success_rate_estimated_pct` — order-of-magnitude estimates
- `data_needed_user_inputs` / `data_computed` — schema for case evaluation
- `corpus_refs` — Service-Public.fr / ANIL source URLs
- `jurisprudence_refs` — Cour de cassation refs (empty in v0, judilibre RAG planned post-PISTE)
- `limitations_disclaimers` — 4 strong notices (not legal advice, ADIL escalation, update cadence)
- `moat_signal` — internal compounding-basis metadata

## Templates shipped (2026-05-18)

| Tag | Size | Contentieux |
|---|---|---|
| `loyer-abusif` | 15.4 KB | Dépassement plafond encadrement zone tendue (9 régions) |
| `dpe-invalide` | 21.1 KB | Bail signé sur logement DPE F/G post-interdiction Loi Climat |
| `depot-garantie-non-restitue` | 25.1 KB | Dépôt garantie retenu hors délai/justification Loi 89-462 art 22 |

## Roadmap

- v1 — `charges-injustifiees`, `non-decence`, `troubles-jouissance`, `coloc-solidarite`
- v1 — populate `jurisprudence_refs[]` via judilibre.fr (Cour de cassation open API)
- v1 — case-evaluation REST endpoint (POST `/api/recourse/<tag>/evaluate`)
- v2 — multilingual templates (EN/AR/PT for non-FR tenants)

## Disclaimer

These templates are **informational and educational**. They do not constitute legal advice. Always confirm with ADIL (free, https://anil.org/lAdil), a juriste, or an avocat before initiating any procedure with binding consequences.

## Contact

`contact@bailleurverif.fr` — issue tracker: `https://github.com/Creariax5/bailleurverif/issues`
