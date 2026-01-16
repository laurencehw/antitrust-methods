# Preface and How to Use This Book {.unnumbered}

## Audience and approach
- Upper-undergraduates, early graduate students, and practitioners needing applied antitrust methods.
- Each chapter pairs empirical tools with qualitative evidence guidance and litigation context.
- Code boxes use R; figures are reproducible from public or licensed data.

## How to read
- Skim the case boxes first to anchor theory.
- Run the R chunks; every figure is meant to be regenerated locally.
- Method boxes flag assumptions, diagnostics, and common failure modes.
- Debate callouts mark unsettled areas where multiple approaches coexist.

## Data and reproducibility
- Keys live in `.Renviron`; data are cached in `data/raw` and `data/derived`.
- Render with `quarto render`; set `execute: freeze: auto` to cache slow chunks.
- Use `renv` to lock package versions for teaching and litigation consistency.

## Evidence triad
- Empirics: estimation and inference with transparent code.
- Documentary: facts from discovery and public sources woven into case boxes.
- Expert judgment: where and how to exercise professional judgment, including survey design and qualitative interviews.

## Citations and jurisdictions
- Cite claims and data with `[@key]` inline; include papers, books, agency actions, and case law (US focus with EU/UK/Japan/China notes where relevant).
- All references live in `references/references.bib`; add `note = {Last accessed: YYYY-MM-DD}` for web/agency sources.
- When a claim hinges on jurisdictional nuance, flag it explicitly (e.g., `{US}`, `{EU}`) and note divergences in standards or burdens.
