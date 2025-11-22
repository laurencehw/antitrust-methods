# Data folder

- `raw/`: downloads from APIs or third parties. Keep immutable; include a short `*_notes.txt` per dataset if provenance matters.
- `derived/`: cleaned/aggregated data ready for analysis.
- Prefer parquet (`arrow`) or CSV with documented schema.
- Do not commit contents to git; `.gitignore` excludes these folders.
