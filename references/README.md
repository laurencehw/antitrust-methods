# References workflow

- Maintain all citations in `references/references.bib`. Use a reference manager (e.g., Zotero + Better BibTeX) to sync exports here.
- Use pandoc citation keys in text (`[@authorYear]`). For cases/decisions, create keys like `[@us_supreme_court_microsoft_2001]` or `[@ec_commission_google_shopping_2017]`.
- For multi-jurisdiction coverage, include tags in the bib entry keywords (e.g., `keywords = {US, DOJ, merger}`) to aid searching.
- If you prefer a specific citation style, add the CSL file (e.g., `chicago-author-date.csl`) under `references/` and set `csl: references/chicago-author-date.csl` in `_quarto.yml`.
- Keep case law and agency materials (complaints, decisions, guidelines) with stable URLs or docket numbers; add `note = {Last accessed: YYYY-MM-DD}`.
