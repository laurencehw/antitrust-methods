# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Quarto book: "Antitrust Methods: Research and Practice" — a practitioner-focused text weaving empirical and qualitative methods with code boxes and case boxes throughout. Author: Laurence Wilse-Samson (NYU Wagner).

## Build Commands

```bash
# Render full book (HTML output to _book/)
quarto render

# Render single chapter
quarto render chapters/05-cartels.qmd

# Preview with live reload
quarto preview
```

PDF requires XeLaTeX (MiKTeX with Perl). Uses Palatino Linotype + Consolas fonts.

## Data Pipeline

### Data collection scripts (run in order):
```bash
Rscript program/scripts/00_run_all.R           # Runs all scripts below
Rscript program/scripts/01_fred_extended.R     # FRED economic series
Rscript program/scripts/02_finance_extended.R  # Stock prices (tidyquant)
Rscript program/scripts/03_bls_labor.R         # BLS wage/employment
Rscript program/scripts/05_flights_extended.R  # Airline route shares
Rscript program/scripts/06_procurement_cartels.R  # Cartel screening data
Rscript program/scripts/07_digital_platforms.R    # Platform market shares
Rscript program/scripts/08_regulation_benchmarks.R # Utility benchmarking
```

### API keys
Copy `.Renviron.example` to `.Renviron` and populate:
- `FRED_API_KEY` — register at fred.stlouisfed.org
- `BLS_KEY` — register at bls.gov/developers

### Data locations
- `data/raw/` — immutable API downloads (gitignored)
- `data/derived/` — cleaned analysis-ready files (gitignored)
- Each dataset has `*_metadata.csv` documenting provenance

## Architecture

### Chapter structure
14 chapters in `chapters/` (00-preface through 13-empirical-appendix). Chapter order defined in `_quarto.yml`. Each `.qmd` contains:
- Prose with case boxes and method boxes
- R code chunks using real or synthetic data from `data/`
- Citations via `@key` referencing `references/references.bib`

### Shared R code
`program/R/helpers.R` provides:
- `theme_antitrust()` — ggplot2 theme for PDF figures
- `scale_color_antitrust()`, `scale_fill_antitrust()` — colorblind-friendly palette
- `fetch_fred()`, `fetch_bls()`, `fetch_census()` — API wrappers
- `run_logit_sim()` — differentiated products merger simulation
- `plot_timeline()`, `plot_tornado()`, `plot_sankey()` — specialized visualizations
- `theme_antitrust_minimal()` — minimal variant of the ggplot2 theme for busy plots
- `plot_waterfall()` — waterfall chart for price/cost decompositions and HHI changes
- `calc_hhi_change()` — compute HHI and delta-HHI from market shares

### Quarto execution
Code executes from project root (`execute-dir: project` in `_quarto.yml`), so relative paths like `data/derived/file.csv` work from any chapter.

### Caching
Use chunk options for API-dependent code:
```r
#| cache: true
#| cache.extra: !expr file.mtime("data/raw/fred_combined.csv")
```

## Key Files

| File | Purpose |
|------|---------|
| `_quarto.yml` | Book metadata, chapter order, PDF/HTML settings |
| `references/references.bib` | Bibliography (papers, cases, agency materials) |
| `references/CITATION_QUICK_REFERENCE.md` | Common citation keys by topic |
| `planning/DATA_INTEGRATION_GUIDE.md` | How to replace synthetic scaffolds with real data |
| `planning/visualization-roadmap.md` | Chapter-by-chapter visualization status |

## Data Status

Real data collected: FRED (HHI, prices, wages), stock prices (airlines, tech, healthcare), airline route shares.

Real-data ingestion wired (run locally to populate): `03_bls_labor.R` pulls BLS QCEW county employment (`data/raw/qcew_county_employment.csv`, feeds Ch.10 HHI proxy) + CES employment; `06_procurement_cartels.R` pulls World Bank contract awards and derives a supplier award-concentration HHI screen. Both fall back to a schema-matched, clearly labelled synthetic file when offline.

Still synthetic (no open source): cartel bid-rotation data (needs every bidder's bid, not just awards), platform usage, patent/FDA data.

Manual downloads required (APIs deprecated): PatentsView bulk files, FDA Orange Book, BLS QCEW county data. See `planning/API_KEYS_SETUP.md`.

## Citation Format

Pandoc-style citations in text: `@author_year` or `[@author_year]`. Bibliography entries use BibTeX keys like `@areeda_turner_1975`, `@us_microsoft_2001`, `@doj_ftc_hmg_2023`. See `references/CITATION_QUICK_REFERENCE.md` for common keys.

## Conventions

- Figures: 6" wide, PDF vector format, minimal gridlines
- Tables: booktabs style, SEs in parentheses, stars (* p<0.10, ** p<0.05, *** p<0.01)
- Monetary values: constant 2020 USD unless specified
- R paths: always relative from project root (`data/derived/file.csv`, not absolute)
