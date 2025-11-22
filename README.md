# Antitrust Methods Book

Working directory for a Quarto book that turns lecture notes and slides into a practitioner-focused text on antitrust research methods. Chapters weave empirical and qualitative methods, with code boxes and case boxes throughout.

## Structure
- `chapters/`: Chapter `.qmd` files (see `_quarto.yml` for order).
- `data/raw`: Downloaded source data (ignored).
- `data/derived`: Clean/processed data (ignored).
- `R/`: Shared R helpers (themes, API helpers).
- `scripts/`: One-off scripts or pipelines.
- `figures/`: Generated figures (ignored; referenced from chapters).
- `_literature/`: Existing readings and references (kept separate from git).
- `references/`: `references.bib` for citations (papers, cases, agency materials) and optional CSL style.

## Keys and setup
1. Copy `.Renviron.example` to `.Renviron` and fill your keys (`FRED_API_KEY`, `BLS_KEY`, `BEA_KEY`, `CENSUS_API_KEY`, `COMTRADE_KEY`).
2. Install R packages with `renv::init()` (optional but recommended), then `renv::install(c("tidyverse","fixest","did","bacondecomp","gsynth","sandwich","clubSandwich","broom","ggplot2","ggthemes","hrbrthemes","patchwork","cowplot","plotly","fredr","blsAPI","bea.R","censusapi","jsonlite","arrow","targets","strucchange"))`.
3. Render HTML with `quarto render`. (PDF output requires LaTeX/Perl; install TinyTeX/MiKTeX with Perl if you need PDF.)

## Next steps
- Drop your existing notes/slides into the relevant chapter files and replace placeholders.
- Add real data pulls and figures to each chapter using the helper functions in `R/helpers.R`.
- Keep case boxes and method boxes tight and actionable; pair empirical strategies with qualitative evidence guidance.
- Populate `references/references.bib` (papers, books, cases, agency decisions); set `csl:` in `_quarto.yml` if you prefer a specific style.
