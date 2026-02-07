# Manuscript Review: Antitrust Methods — Research and Practice

**Reviewer:** Claude (automated deep review)
**Date:** 2026-02-07
**Scope:** All 14 chapters, bibliography, helpers, Quarto configuration

---

## Overall Score: 3.4 / 5

| Dimension | Score | Weight | Notes |
|---|---|---|---|
| Content & topical coverage | 4.0 / 5 | 25% | Ambitious scope, genuinely distinctive framing |
| Writing quality & exposition | 3.5 / 5 | 20% | Strong in best chapters, outline-level in weakest |
| Code & reproducibility | 3.5 / 5 | 15% | Good scaffolds; many non-functional placeholders |
| Citations & bibliography | 2.5 / 5 | 15% | Uneven; several chapters have zero formal cites |
| Structural consistency | 3.0 / 5 | 10% | Inconsistent box formatting, internal notes leak through |
| Data integration | 2.5 / 5 | 10% | All visualizations use synthetic data |
| Publication readiness | 3.0 / 5 | 5% | Config issues, runtime errors, internal planning text visible |

---

## Chapter-by-Chapter Assessment

### Ch 00 — Preface (Score: 4.5/5)
- **Strengths:** Polished, concise, well-structured. The "evidence triad" (empirical analysis, documentary evidence, expert judgment) is a compelling and distinctive organizing framework. Three navigation paths (classroom, practitioner, self-study) are practical. The reproducibility callout is useful.
- **Issues:** Uses editorial "we" throughout a single-authored book — minor style point. Does not signal the heavy South African content that appears from Ch 01 onward; the preface says "primary focus is United States antitrust law" but Chapters 01–02 give roughly equal weight to US, EU, and South Africa.

### Ch 01 — Orientation (Score: 3.5/5)
- **Strengths:** Comparative statute mapping table (US/EU/SA) is genuinely useful. ASCII workflow diagram is effective. Google Search vignette is well-chosen. The timeline and bank HHI visualizations are polished.
- **Issues:** **Zero formal `@key` citations** despite referencing dozens of cases and guidelines by name. The learning goals explicitly reference "practitioners in South Africa" and "SADC matters," contradicting the preface's US-primary framing. The FRED series ID `HHMSDODNS` for the bank HHI chart may not actually be a bank concentration index — needs verification.

### Ch 02 — Research Design (Score: 4.0/5)
- **Strengths:** The strongest pedagogical chapter. The method selection decision tree is outstanding. The TWFE/staggered-adoption discussion is timely and identifies it as a "litigation vulnerability." The scoping memo and data pipeline sections contain practical wisdom absent from standard textbooks. The qualitative methods box is unusually thorough.
- **Issues:** The DiD code box is entirely commented out (`eval: false`), so the chapter has no interactive code example beyond the auto-generated event study. Some citations are inline text rather than `@key` format (Angrist & Pischke, Callaway & Sant'Anna). Cross-references use plain "Chapter 4" rather than Quarto `@sec-` syntax.

### Ch 03 — Market Definition (Score: 4.0/5)
- **Strengths:** Most polished of the substantive chapters. Five functional code chunks with real data (nycflights13) and well-labeled synthetic data. Every visualization includes "How to use this," "Interpretation," and "Data sources" guidance. The debate box on whether market definition is still necessary is well-executed. Citations properly use `@key` format.
- **Issues:** Minor overlap between "Core tools and workflow" and "Core diagnostic tools" sections. Geographic flows and diversion ratio data are simulated (appropriately labeled).

### Ch 04 — IO Toolkit (Score: 3.0/5)
- **Strengths:** The structural vs. reduced-form comparison table is one of the best pedagogical elements in the book. The key IO formulas reference table is useful. The cost pass-through analysis using FRED data is strong.
- **Issues:** **Thinnest chapter in the book.** The logit demand example fits a regression on only 3 observations with 2 predictors (zero degrees of freedom) — misleading for students. The bargaining section is only two bullet points. The "Looking ahead" section contains internal project-management language ("Push generic templates...into `chapters/13-empirical-appendix.qmd`", "Update the visualization tracker"). This must be removed before publication.

### Ch 05 — Cartels and Collusion (Score: 3.5/5)
- **Strengths:** The 7-step workflow roadmap is an effective structural device. The network graph with centrality metrics is analytically rich. The placebo test visualization is a strong addition. South African enforcement highlights with specific penalty figures are distinctive.
- **Issues:** The overcharge and pass-through section — arguably the most important quantitative output of cartel analysis — is only bullet points with no code demonstration. The raid event study is entirely commented out. Case boxes are abbreviated compared to Ch 03. Internal project-management language in "Looking ahead." Some citations are inline prose rather than `@key` format.

### Ch 06 — Mergers (Score: 4.0/5)
- **Strengths:** Most comprehensive chapter. Ten code chunks, all functional. The UPP formula walkthrough is one of the best accessible explanations available. The vUPP section uses an effective Netflix/content studio motivating example. The stock-event study uses real ticker data. Southern African case examples are detailed and specific.
- **Issues:** The **Gemini review identified a UPP formula error** (`diversion * price * (1 - margin)` should be `diversion * price * margin`) — this must be verified and fixed. The coordinated effects section is thin (only bullet points + maverick detection). Some redundancy with Ch 04 on UPP/GUPPI. The HHI dashboard hardcodes `share + 0.22` rather than dynamically computing post-merger shares.

### Ch 07 — Monopolization and Exclusion (Score: 4.0/5)
- **Strengths:** The most polished and complete chapter. Deep treatment of each conduct category (predation, rebates, tying, MFNs, refusal to deal) with a consistent pattern: theory → measurement → qualitative evidence → case references. Seven functional code chunks. The effective price waterfall correctly models retroactive rebate mechanics. Extensive and well-integrated citations.
- **Issues:** The callout boxes at the end of the chapter (lines 1079–1091) read like **authoring notes** — stub outlines rather than finished content. The "Case box: Core exemplars" is a bare outline that should be developed or removed. No dedicated Remedies section despite the workflow promising one.

### Ch 08 — Regulation and Remedies (Score: 2.5/5)
- **Strengths:** Sound conceptual structure. The "diagnosis vs. prescription" framing is effective. The benchmarking scatter and remedy timeline visualizations are reasonable starting points.
- **Issues:** **Zero formal citations.** The prose is thin — topics like rate-of-return regulation, price-cap regulation, and ECPR get only a few bullet points each. Multiple sections are explicitly labeled "scaffold." The "Data and visualization plan" section is internal planning text that should not appear in the published book. No formal case boxes despite rich South African material. This chapter reads as a detailed outline, not a finished chapter.

### Ch 09 — Digital Markets (Score: 3.5/5)
- **Strengths:** The theory-to-metric mapping table (10 theories of harm → metrics → tests → data sources) is excellent reference material. The platform fee structure visualization uses real publicly available data. The generative AI section is timely. The Southern African digital enforcement examples are distinctive.
- **Issues:** **Duplicate callout boxes** — the method box, qualitative evidence box, and citations box each appear twice with near-identical content (drafting artifact). The `ggalluvial` library is loaded but never used. Citations are sparse — many important references (Epic v. Apple, DOJ Google, FTC Amazon, DMA) are mentioned by name but not formally cited. The two-sided demand scaffold runs `feols()` on only 12 observations.

### Ch 10 — Labor Markets (Score: 2.5/5)
- **Strengths:** Clear framing of labor antitrust as the mirror image of product market analysis. The statutory labor exemption callout is a valuable addition. The choropleth and occupation concentration visualizations are well-designed.
- **Issues:** **Significantly underdeveloped.** Multiple sections are bullet-point outlines with no prose elaboration (wage posting, mobility analytics, franchise no-poach). Two of seven code chunks are non-functional placeholders. Missing substantive treatment of criminal wage-fixing cases (DOJ v. Jindal, DaVita), the FTC noncompete rule, gig economy classification, and worker damages estimation. Roughly half the length and depth of the monopolization chapter.

### Ch 11 — Innovation, IP, and Antitrust (Score: 3.5/5)
- **Strengths:** The SEP/FRAND cases section is strong with clear jurisdictional comparisons. The killer acquisitions framework is well-developed. The royalty waterfall, survival analysis, patent citation network, and R&D event study are ambitious and well-designed code chunks. Best citation practice of the later chapters.
- **Issues:** Variable depth — some sections are richly developed while others (interoperability, Southern African examples) are stubs. The "Enhanced Visualizations" section (~450 lines) feels like a separate appendix grafted onto the chapter. Four code chunks are `eval: false` scaffolds with sparse pseudocode.

### Ch 12 — Litigation Practice (Score: 2.5/5)
- **Strengths:** Good conceptual structure covering the full expert lifecycle from engagement through trial testimony. The evidence provenance network and individual damages visualizations are impressive.
- **Issues:** **Heavily code-weighted with thin prose** (~60-70% code by line count). Two of the core analytical chunks are commented-out placeholders. Only 4 citations, all in one section. Line 98 contains garbled text ("Document random sampling pr OCED images?") — an editing artifact visible in output. No case boxes. No substantive discussion of class certification law, deposition/testimony guidance, or damages calculation methodology. The callout boxes read as authorial reminders, not reader-facing content.

### Ch 13 — Empirical Appendix (Score: 3.0/5)
- **Strengths:** Well-conceived as a practical reference. The diagnostic gallery (pre-trends, balance plots, specification curves, residual diagnostics, power analysis) is impressive in scope and would be genuinely valuable to practitioners. The data inventory and chronology templates are useful.
- **Issues:** Two **likely runtime errors**: (1) `se()` from `fixest` called on an `lm` object in the spec curve chunk, and (2) `pwr.t.test()` is not vectorized but is called with vector arguments in `mutate()`. The prose is extremely terse throughout. The survey kit and coding lexicon sections are underdeveloped. Only 6 citations total.

---

## Cross-Cutting Findings

### 1. Audience / Jurisdictional Scope Mismatch (High Priority)
The preface states "primary focus is United States antitrust law" with EU/UK comparisons, but from Ch 01 onward the book gives roughly equal weight to **US, EU, and South Africa**. Chapter 01's learning goals explicitly reference "practitioners in South Africa" and "SADC matters." This needs reconciliation: either update the preface to acknowledge the tri-jurisdictional scope, or reduce the South African emphasis.

### 2. Citation Coverage Is Severely Uneven (High Priority)
| Chapter | Formal `@key` citations |
|---|---|
| 00 Preface | 0 (acceptable) |
| 01 Orientation | **0** (not acceptable) |
| 02 Research Design | ~5 |
| 03 Market Definition | ~7+ |
| 04 IO Toolkit | ~8 |
| 05 Cartels | ~6 |
| 06 Mergers | ~13+ |
| 07 Monopolization | ~20+ |
| 08 Regulation | **0** (not acceptable) |
| 09 Digital Markets | ~5 (low for chapter length) |
| 10 Labor Markets | ~7 |
| 11 Innovation/IP | ~8 |
| 12 Litigation | **4** (all in one section) |
| 13 Appendix | 6 |

Chapters 01, 08, and 12 need immediate citation work. Chapters 09 and 05 need significant additions.

### 3. Internal Planning Text Leaks Into Chapters (High Priority)
Several chapters contain text intended for authors, not readers:
- Ch 04, 05: "Push generic templates...into `chapters/13-empirical-appendix.qmd`"
- Ch 04: "Update the visualization tracker if you add new figures"
- Ch 08: "Data and visualization plan" section, "Checklist for fill with real data"
- Ch 09: "When we 'fill with real data,' replace the synthetic CSVs..."
- Ch 12: Line 98 garbled text, "Checklist for fill with real data" section
- Multiple chapters: "Visualizations and data sourcing" sections read as internal notes

### 4. Box Formatting Inconsistency (Medium Priority)
The book promises "case boxes and method boxes throughout," but:
- Case boxes appear in some chapters (03, 05, 06, 07) but not others (08, 09, 10, 11, 12)
- Method boxes use uniform `callout-note` styling everywhere — no visual distinction between method boxes, case boxes, and debate boxes
- Several callout boxes are stub outlines rather than developed content (07 end, 08, 12)
- Ch 09 has duplicate callout boxes (drafting artifact)

### 5. Synthetic Data Throughout (Medium Priority)
Every visualization in the book uses synthetic or simulated data, with the partial exceptions of:
- `nycflights13` package data (Ch 03)
- FRED API data (Ch 01, 02, 04, 05)
- `tidyquant` stock prices (Ch 02, 06)

All other charts — including the core analytical demonstrations in mergers, cartels, monopolization, digital markets, labor, innovation, and litigation — use `set.seed()` + `rnorm()`/`runif()` generated data. This is clearly flagged throughout, but it means the book currently cannot demonstrate that its methods work on real problems.

### 6. Non-Functional Code Scaffolds (Medium Priority)
Multiple chapters contain `eval: false` or fully commented-out code chunks:
- Ch 02: DiD code box (commented out)
- Ch 05: Raid event study (commented out)
- Ch 09: Default-choice event study (`eval: false`)
- Ch 10: Labor elasticity (commented out), synthetic control (`eval: false` with `...` placeholders)
- Ch 11: Four chunks `eval: false`
- Ch 12: Two core chunks commented out
- Ch 13: Survey weighting (`eval: false`)

These scaffolds need to either be fleshed out with synthetic data that actually runs, or replaced with prose explaining the method.

### 7. Bibliography Issues (Medium Priority)
- **118 entries** — adequate but not comprehensive for a 14-chapter practitioner text
- **10 BibTeX type mismatches** (books declared as `@article`): `davis_garces_2010`, `whinston_2006`, `manning_2003`, `posner_1976`, `bork_1978`, `hovenkamp_2005`, `harrington_2008`, `werden_froeb_2008`, `rubinfeld_2010`, `baker_salop_2015`
- **3 citation key/year mismatches**: `abrantes_mello_2010` (actually 2006), `edlin_hemphill_2012` (actually 2013), `rubinfeld_2010` (actually 2011)
- **Missing seminal references**: Landes & Posner (1981), Werden (2003), US v. Alcoa (1945), Ohio v. American Express (2018), Verizon v. Trinko (2004), Brown Shoe v. US (1962), Khan (2017) "Amazon's Antitrust Paradox," Stigler Committee (2019), Goodman-Bacon (2021), Sun & Abraham (2021)

### 8. Code / Configuration Issues (Low-Medium Priority)
- **UPP formula potentially wrong in Ch 06** (flagged by prior Gemini review): `diversion * price * (1 - margin)` should be `diversion * price * margin`
- **Ch 13 runtime errors**: `se()` on `lm` object; `pwr.t.test()` not vectorized
- **helpers.R**: `fetch_fred()`/`fetch_bls()` promise caching but don't implement it; `plot_tornado()` has undeclared `tidyr` dependency; `plot_waterfall()` doesn't handle NA
- **_quarto.yml**: No `message: false` in execute options; no CSL file; figure numbering disabled; conflicting `tidy: false` with `tidy.opts`

---

## Paths to 5/5

### Path 1: Citation and Bibliography Overhaul (Impact: +0.4)

**Current gap:** Three chapters have zero citations; others cite sporadically.

Actions:
1. **Add missing seminal references** to `references.bib` (~15 entries): Landes & Posner, Werden (2003), Alcoa, Amex, Trinko, Brown Shoe, Khan (2017), Stigler Committee, Goodman-Bacon, Sun & Abraham, Werden & Froeb (1994), Simonsohn et al. (spec curves), Austin (2009, balance diagnostics)
2. **Fix 10 BibTeX type mismatches** (change `@article` to `@book` or `@incollection`)
3. **Fix 3 key/year mismatches**
4. **Systematic citation pass on Ch 01** — every named case, guideline, and statute needs a `@key` reference
5. **Systematic citation pass on Ch 08** — add citations for Kahn, Vogelsang, OECD, DOJ/FTC remedy manuals
6. **Add citations to Ch 12** — damages methodology literature, class certification case law
7. **Formalize inline references in Ch 05, 09** — convert "Connor 2007," "Luca et al., 2016" to proper `@key` format

### Path 2: Develop Underdeveloped Chapters (Impact: +0.5)

**Current gap:** Chapters 04, 08, 10, and 12 are substantially thinner than the rest.

Actions:
1. **Ch 04 (IO Toolkit):** Expand bargaining section from 2 bullet points to a proper subsection with a Nash-in-Nash worked example. Replace the 3-observation logit with a ~20-product example. Add at least one case box.
2. **Ch 08 (Regulation & Remedies):** Expand rate-of-return and price-cap sections with worked numerical examples. Add proper case boxes for the South African market inquiry examples. Develop the consent decree / remedy negotiation discussion. Add ECPR worked example.
3. **Ch 10 (Labor Markets):** Develop the wage posting, mobility analytics, and franchise no-poach sections from bullet points to full prose. Add treatment of criminal wage-fixing cases (DOJ v. Jindal, DaVita), the FTC noncompete rule, and gig economy classification. Make the elasticity and synthetic control code chunks functional.
4. **Ch 12 (Litigation Practice):** Expand prose significantly — each section (damages modeling, class certification, Daubert readiness, presentation) needs 2-3 paragraphs of developed exposition. Add class certification law discussion (Comcast v. Behrend, Wal-Mart v. Dukes). Make the common impact and randomization inference code chunks functional. Fix the garbled text on line 98.

### Path 3: Scrub Internal Planning Text (Impact: +0.2)

**Current gap:** Authorial notes visible in rendered output.

Actions:
1. Remove "Push generic templates..." language from Ch 04, 05 "Looking ahead" sections
2. Remove "Update the visualization tracker" from Ch 04
3. Remove "Data and visualization plan" and "Checklist for fill with real data" sections from Ch 08, 09, 12
4. Remove "Visualizations and data sourcing" internal notes from Ch 09, 10
5. Remove garbled text from Ch 12 line 98
6. Convert authorial-reminder callout boxes in Ch 07 (end), 08, 12 into either finished content or delete them
7. Remove the duplicate callout boxes in Ch 09

### Path 4: Standardize Box Formatting (Impact: +0.15)

**Current gap:** Inconsistent use of case boxes and method boxes across chapters.

Actions:
1. Define a consistent callout type mapping: e.g., `callout-tip` for case boxes, `callout-note` for method boxes, `callout-warning` for debate boxes, `callout-important` for practitioner tips
2. Add case boxes to chapters that lack them (08, 09, 10, 12) — each chapter should have at least one detailed case box
3. Develop stub callout boxes into full content or remove them
4. Ensure consistent labeling ("Case box: [Title]", "Method box: [Title]")

### Path 5: Activate Code Scaffolds (Impact: +0.15)

**Current gap:** ~15 code chunks across the book are non-functional.

Actions:
1. Convert `eval: false` scaffolds to running examples with synthetic data where possible (priority: Ch 10 elasticity + synthetic control, Ch 11 pay-for-delay survival, Ch 12 common impact)
2. For scaffolds that genuinely need real data, add a brief prose explanation of the method above the scaffold so readers still learn from it
3. Fix the two runtime errors in Ch 13 (spec curve `se()` on `lm`; power analysis `pwr.t.test()` vectorization)
4. Verify and fix the UPP formula in Ch 06

### Path 6: Real Data Integration (Impact: +0.2)

**Current gap:** Core analytical demonstrations all use simulated data.

Actions (prioritized by feasibility):
1. **Already collected, just needs integration:** FRED HHI/price data → Ch 01, 03, 04, 05 visualizations; airline route shares → Ch 03, 06; stock prices → Ch 02, 06
2. **Publicly available, needs collection:** BLS QCEW for labor market HHI → Ch 10; FDA Orange Book for generic entry → Ch 11; FCC broadband data → Ch 08
3. **Requires synthesis from public sources:** Platform market shares from SEC filings / Statista → Ch 09; App store fee schedules → Ch 09
4. **Lowest priority (may remain synthetic):** Cartel bid data (Ch 05), patent citation networks (Ch 11), litigation damages (Ch 12) — these may legitimately need to remain illustrative

### Path 7: Resolve the Audience / Scope Question (Impact: +0.15)

**Current gap:** Preface says "US primary" but content is tri-jurisdictional.

Actions (choose one):
- **Option A:** Update the preface to explicitly acknowledge the tri-jurisdictional scope (US, EU, South Africa) as a distinctive feature. Add a sentence explaining the South African focus serves practitioners in developing/emerging economy competition regimes.
- **Option B:** Reduce South African content to brief comparative notes (like the EU/UK treatment) and remove the Ch 01 learning goal about "practitioners in South Africa."

Option A is recommended — the South African content is a genuine differentiator.

### Path 8: Configuration and Infrastructure Fixes (Impact: +0.05)

Actions:
1. Add `message: false` to `_quarto.yml` execute options
2. Add a CSL file (Chicago author-date or a law-economics hybrid)
3. Add `lang: en` to `_quarto.yml`
4. Remove conflicting `tidy.opts` (since `tidy: false`)
5. Re-enable figure numbering or document why it is disabled
6. Fix `helpers.R`: add disk caching to `fetch_fred()`/`fetch_bls()`; declare `tidyr` dependency in `plot_tornado()`; handle NA in `plot_waterfall()`
7. Update CLAUDE.md to document `theme_antitrust_minimal()`, `plot_waterfall()`, and `calc_hhi_change()`

---

## Priority Ranking for Maximum Impact

| Priority | Path | Effort | Impact |
|---|---|---|---|
| 1 | Path 2: Develop underdeveloped chapters | High | +0.5 |
| 2 | Path 1: Citation & bibliography overhaul | Medium | +0.4 |
| 3 | Path 3: Scrub internal planning text | Low | +0.2 |
| 4 | Path 6: Real data integration | High | +0.2 |
| 5 | Path 4: Standardize box formatting | Medium | +0.15 |
| 6 | Path 7: Resolve audience/scope | Low | +0.15 |
| 7 | Path 5: Activate code scaffolds | Medium | +0.15 |
| 8 | Path 8: Configuration fixes | Low | +0.05 |

**Achieving 5/5 requires completing Paths 1–7.** Path 8 is polish. The single highest-impact action is developing the four weakest chapters (04, 08, 10, 12) to match the quality of the four strongest (03, 06, 07, 02).

---

## What the Book Does Well

It is worth noting what is already strong, since the paths above focus on gaps:

1. **Distinctive framing.** The "evidence triad" and the consistent integration of empirical, documentary, and qualitative evidence sets this apart from both pure economics texts (Motta, Davis & Garces) and pure law texts (Hovenkamp).
2. **Practitioner orientation.** Workflow diagrams, scoping memo guidance, "how to use this" annotations on visualizations — this is written for people who will actually do antitrust work, not just study it.
3. **Code quality in best chapters.** The R code in chapters 03, 06, and 07 is clean, well-commented, and pedagogically effective. The helper infrastructure (theme, palette, API wrappers) is thoughtful.
4. **South African comparative content.** This is a genuine differentiator. No comparable English-language textbook integrates developing-economy competition enforcement at this level.
5. **Modern methods coverage.** The staggered DiD / TWFE discussion, specification curves, synthetic control, and network analysis reflect the current state of applied economics rather than legacy methods.
6. **Ambitious scope.** Covering market definition through digital platforms through labor through litigation in a single integrated text is a significant undertaking, and the conceptual architecture holds together well.
