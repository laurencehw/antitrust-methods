# Full Manuscript Audit: *Antitrust Methods: Research and Practice*

Reviewed 12 June 2026. This is a second, deeper review, conducted after the
voice pass and exercise upgrades recorded in `REVIEW.md`. Where `REVIEW.md`
scored prose, structure, and pedagogy, this audit additionally verified the
substance: every formula was checked, every checkable exercise recomputed, case
holdings and statutes verified, the bibliography audited for invented entries,
and the build/reproducibility story tested end to end. The two reviews are
consistent on what they both looked at — the voice pass worked, the structure
is right — but this one reaches further down and finds problems the first one
did not.

## Score: 6 / 10

**Why lower than `REVIEW.md`'s 8.5:** that score rated the manuscript's design
and prose, which are genuinely at the 8.5 level. This score also rates its
*reliability* — and for a methods text aimed at practitioners who will be
cross-examined on what they learned from it, reliability dominates. The audit
found an inverted decision table in the market-definition chapter, four
fabricated or mangled bibliography entries, an apparently invented judicial
quotation, roughly a dozen misstated case outcomes (including two South African
appellate reversals reported as affirmances and the annulled Intel and Qualcomm
findings reported as good law), several wrong formulas with wrong printed
outputs, ~10 code chunks that error or draw the wrong picture, and a build that
cannot render from a fresh clone. None of this is visible to a casual reader;
all of it is visible to exactly the expert readers the book is for.

**What the 6 reflects on the upside:** the architecture is excellent and
distinctive (the evidence triad, the US/EU/SA frame, the box system), the voice
pass succeeded (sweeps of the STYLE.md tic patterns come back essentially
clean; several openers are genuinely strong), every one of the eleven
recomputed "Data exercise (checkable)" worked answers is arithmetically
correct, the citation-checker + gitbook-sync CI is well built, and the core
legal-economic frameworks (Brooke Group, Trinko, Amex, Bronner/IMS, Daubert,
Dukes, Comcast, logit diversion, critical loss, markdown formula) are correctly
stated. The skeleton is a 9; the flesh needs a fact-and-code pass.

### Scorecard

| Section | Sub-score | Drag |
|---|---|---|
| Front matter + Chs. 1–3 | 5.5 | Inverted critical-loss table; mislabeled "real data" figure; unverifiable Google quote; broken event-study scaffold |
| Chs. 4–7 (IO, cartels, mergers, monopolization) | 6 | Invented price-effect formula; waterfall bugs printing wrong answers; SA appellate record misstated; Intel/Google staleness |
| Chs. 8–11 (regulation, digital, labor, IP) | 5.5 | Wrong opening anecdote (Ch. 10); fabricated citation; mislabeled Nash benchmarks; badly stale digital chapter |
| Chs. 12–15 (litigation, appendix, closing, glossary) | 6 | Three broken figures; SA statute/case-number errors in glossary; capstone has no numbers |
| Reproducibility | 4 | Fresh clone cannot render; 8 reads outside the repo; no freeze cache; 12/37 packages in install script |

---

## Error catalog

File:line references are to the manuscript as of commit `b0ab74c`. Items
marked *(verify)* were flagged at medium confidence and need a human check
before correcting.

### A. Analysis errors (highest severity — the book teaches the wrong answer)

1. **Inverted critical-loss decision table** — `chapters/03-market-definition.qmd:194-198`.
   Rows with actual < critical are labeled "Market likely too narrow"; the row
   with actual > critical is labeled "too broad." Both are backwards (actual <
   critical ⇒ SSNIP profitable ⇒ market well-defined; actual > critical ⇒
   expand the candidate market). The chapter's own flowchart (lines 59–66) and
   worked answer (lines 673–676) state it correctly, so the chapter contradicts
   itself. Also rename `passes_test` (line 126) to something unambiguous.
2. **Invented "first-order price effect" formula** — `chapters/06-mergers.qmd:222-223`.
   `upp / (price * 2 * alpha * (1 - share))` is not a recognized approximation;
   it reduces to UPP×margin/2 in dollars mislabeled as a percent, printing
   26%/19%/49% "price increases" against the same chunk's +4.5% waterfall. Use
   ΔP ≈ pass-through × UPP (≈ UPP/2 under linear demand) and state the
   assumption.
3. **Q-learning benchmarks mislabeled** — `chapters/09-digital-markets.qmd:424,495-503,522`.
   With demand q = 100 − 2p_i + p_j and c = 5, the price labeled "Nash
   equilibrium" (8) is not an equilibrium and the price labeled "Collusive"
   (16) is approximately the stage-game Nash on the grid — the simulation
   "demonstrates" collusion that is actually competitive play. Recalibrate
   demand so the labels are true. Also: agents share one Q-matrix despite the
   prose claiming independent learners (lines 435–479), and
   `mean(collusion_data[1:500])` (lines 517, 520) subsets columns, not rows —
   runtime error.
4. **Critical-loss fallacy never stated** — `chapters/03-market-definition.qmd:66`
   asserts high margins make narrow markets easier to sustain; without the
   O'Brien–Wickelgren/Katz–Shapiro caveat (high margins also imply low *actual*
   loss) this teaches the textbook fallacy. Both papers are already in the bib.
   Also distinguish breakeven vs. profit-maximizing critical loss.
5. **Pass-through estimated on index levels** — `chapters/04-io-toolkit.qmd:369-413`.
   CPI-on-PPI levels regression is the spurious-regression trap; the chunk even
   computes the changes (lines 342–343) and never uses them. Estimate in
   log-differences with lags, as Ch. 5's own method box (line 791) prescribes.

### B. Fabricated or unverifiable material (purge entirely)

6. **`calvano_vijay_2023`** — `references/references.bib:1607-1616`, cited at
   `09-digital-markets.qmd:399,532` and `14-closing.qmd`. "Calvano, Emilio and
   Vijay, Vijay" (JEP 2023) does not exist. The real paper is Calvano,
   Calzolari, Denicolò & Pastorello, "Artificial Intelligence, Algorithmic
   Pricing, and Collusion," *AER* 2020.
7. **`crawford_etal_2022`** (`references.bib:1585`) and **`johnson_etal_2023`**
   (`references.bib:1596`) — neither matches a real publication *(verify, then
   replace or cut)*.
8. **`azab_etal_2024`** (`references.bib:1618`) — misspells Azar, misdates the
   Azar–Marinescu–Steinbaum–Taska job-postings paper (2020, *Labour
   Economics*), and `14-closing.qmd:38` mischaracterizes it as a survey.
9. **Epigraph quote attributed to *US v. Google*** —
   `chapters/03-market-definition.qmd:69`. The quoted sentence cannot be found
   in or about the 2024 memorandum opinion. Quote the real opinion or
   paraphrase without quotation marks. A fabricated quote from a live case is
   the most damaging single artifact a hostile reader could find.
10. **Unsourced quantitative specifics presented as findings** *(source or
    soften each)*: Grocery Retail Market Inquiry SSNIP/critical-loss numbers
    (`03:612`); Healthcare Market Inquiry credited with COVID-era agency-nurse
    findings although it closed in 2019 (`10:567`); OIPMI driver-earnings
    dashboard remedies on e-hailing the same paragraph says was out of scope
    (`10:571`); identical "six KPIs… two consecutive quarters" detail attached
    to both Telkom 2013 and the Data Services Inquiry (`08:114,247,254`);
    bread-cartel damages-model and "Tribunal-supervised trustee" details
    (`12:214`); DaVita "$53.6 million" settlement figure (`10:495`).

### C. Misstated case outcomes and law

11. **Sasol** — `07:976`: the CAC *set aside* the Tribunal's excessive-pricing
    finding (June 2015); the text says "upheld."
12. **Media24** — `07:464,975`: the Tribunal's 2015 finding (ATC-plus-intent,
    not avoidable-cost) was overturned by the CAC in 2019; the text reports
    final liability with remedies.
13. **Intel** — `07:144,286,1078`: 2009 decision conflated with the 2017 CJEU
    judgment; the rebates/AEC finding was annulled (GC 2022, affirmed CJEU Oct
    2024), so "satisfies the AEC framework established in *Intel*" is no longer
    good law.
14. **Qualcomm** — `11:61,64-65,858`: the €997M exclusivity fine was annulled
    by the General Court (T-235/18, 2022); Exercise 3's premise "fines upheld"
    is wrong.
15. **Microsoft** — `07:489`: the D.C. Circuit *vacated* the tying ruling; the
    affirmed liability was §2 monopoly maintenance.
16. **Evanston Northwestern** — `08:296`: cited as structural relief; it is the
    canonical *behavioral* hospital remedy.
17. **Pilgrim's Pride opener** — `10:44`: the 2021 indictments were for broiler
    price-fixing, not wage-fixing. Retell *US v. Jindal* (Dec 2020, physical
    therapists) or the 2022 civil poultry wage-information consent decree.
18. **Jindal mischaracterized twice** — `02:121` (called poultry) and `10:482`
    (called nurses + market-allocation count; jury acquitted on the Sherman
    Act counts, convicted only on obstruction). The book's own bib note has it
    right.
19. **AA/US Airways remedy doubled** — `06:301`: "104 slot pairs… 34 slot
    pairs" should be 104 slots (52 pairs) at DCA and 34 slots (17 pairs) at
    LGA. Also `03:327`: DOJ pleaded *city pairs*, not airport pairs *(verify
    against the complaint)*; and `04:292`: DCA–LGA was a US Airways–Delta
    shuttle market, not an AA overlap *(verify)*.
20. **Advocate Health Care** — `03:610` and `06:463`: the Seventh Circuit
    decision is 2016, not 2017; and hospital–insurer competition is two-stage
    bargaining, not a "two-sided market" — the term will be flagged post-*Amex*.
21. **Google default payments** — `03:614`: payments were to Apple/Mozilla/
    OEMs; Chrome is Google's own browser.
22. **Amazon MFNs** — `07:662-663`: the price-parity actions were national
    (Bundeskartellamt, OFT), not EC; the CMA hotel-booking investigation closed
    without the remedy described.
23. **Apple e-books** — `05:809`: SSNDQ has no role in that case; it turned on
    agency + retail MFN.
24. **SA statutory errors** — `01:40` (vertical restraints mapped to §4(1)(b),
    the per se *horizontal* provision; should be §5/§8(1)(d));
    `15-glossary.qmd:110` (per se prohibition attributed to §4(1)(a); it is
    §4(1)(b)); `15:57` (Act chapter numbers wrong: abuse of dominance is Ch. 2
    Part B, mergers Ch. 3); `01:48` (SA dominance thresholds are statutory —
    ≥45% presumed, 35–45% rebuttable, <35% only with proven power — not
    "40–50%"); `03:620` (Healthcare Market Inquiry panel was
    Commission-appointed, not Tribunal-appointed).
25. **SA case citations** — `15:82,84`: Walmart/Massmart and Heineken/Distell
    given complaint-referral (/CR/) codes; merger cases carry /LM/ codes
    (Walmart/Massmart was 73/LM/Nov10; Heineken/Distell approved 2023).
    `15:80`: Sasol case number contradicts the book's own bib entry — neither
    matches the reported citations *(verify all SA case numbers)*.
26. **JetBlue/Spirit** — `15:69` + bib: case was No. 1:23-cv-10511 (D. Mass.),
    not 1:22-cv-02439 (D.D.C.).
27. **Misc.** — `01:49` (Art. 101 object restrictions are not "per se illegal";
    101(3) remains available); `01:174` (the 2004 timeline entry conflates Reg.
    1/2003 with the EUMR recast); `15:70` (DaVita listed as criminal no-poach
    conviction without noting the acquittal); `06:616` (2020 Vertical Merger
    Guidelines cited as live; withdrawn 2021); `09:1023` (DeepMind, wholly
    owned since 2014, listed among quasi-merger AI partnerships); `09:273`
    ("CTRs 35 times higher" conflates the ~35%-of-clicks finding the chapter
    itself uses correctly at line 1073).

### D. Staleness as of mid-2026 (the digital and labor chapters read as 2023)

28. **Ch. 7 and Ch. 9 must incorporate**: *US v. Google* search — liability
    Aug 2024, remedies Sept 2025 (no Chrome divestiture; default-exclusivity
    bans; data syndication); *US v. Google* ad tech — liability Apr 2025;
    *FTC v. Meta* — judgment for Meta Nov 2025; *Epic v. Apple* contempt ruling
    Apr 2025; CJEU affirmance of Google Shopping Sept 2024; DMA non-compliance
    fines (Apple €500M, Meta €200M, Apr 2025); UK DMCCA 2024 / SMS regime
    (replacing the "digital markets unit" framing at `09:25,273,392,532,
    1019-1057`); rescission of the 2023 AI Executive Order (`09:1045`). A 2026
    monopolization chapter whose newest US case is Microsoft (2001) will read
    as dated to every practitioner.
29. **Ch. 10 must incorporate**: the January 2025 DOJ/FTC *Antitrust Guidelines
    for Business Activities Affecting Workers* superseding the 2016 HR guidance
    (`10:48,486-488`); 2023 Merger Guidelines Guideline 10; the FTC's Sept 2025
    dismissal of the *Ryan* noncompete appeal (`10:451,476` says "pending
    appellate review").

### E. Formula and arithmetic errors

30. `06:104-108` — UPP function documented with the wrong product's
    price/margin (UPP_A needs the *partner's* margin, P_B − C_B). Harmonize
    with Ch. 4's index form and state UPP-vs-GUPPI units once.
31. `06:538-547` — vUPP opportunity-cost term (`upstream_margin_on_rivals *
    downstream_price`) dimensionally wrong; cf. Moresi–Salop vGUPPI.
32. `06:237-250,937-957,1011-1022` — waterfall "total" rows included in
    `cumsum`, so the chart and printed summary report a $21.50 post-merger
    price (+115%) for a $10.75 (+7.5%) simulation. Same defect at
    `07:185-217` (effective-price waterfall ends at $0; correct answer −$100,
    which the method box at `07:1037-1066` gets right).
33. `07:1026` — "foreclosed share (here 58%)" vs. the chunk's own printed
    47.1%.
34. `07:893-924,965` — margin-squeeze waterfall hardcodes wholesale $47/$6
    margin; the simulated data and the chapter's own exercise use $45/$8.
35. `04:486-520` — Nash-in-Nash example: post-merger rate equals Hospital A's
    pre-merger rate; the claimed price rise comes from an assumed
    bargaining-weight jump and an average-vs-average comparison. Hold the
    weight fixed and let the superadditive disagreement payoff drive it.
36. `04:292-298` — airline GUPPI box uses 10–15% *operating* margins where
    incremental margins (high for airlines) belong; inconsistent with the
    40–55% in the adjacent box.
37. `10:445` — "elasticity of 10 ⇒ a 10% wage cut loses half the workforce" —
    it loses ~100%; elasticity 5 loses half.
38. `15:21` — glossary GUPPI omits the price-ratio term (D₁₂ × M₂ × P₂/P₁).
39. `03:286,309-311,355` — structural presumption stated as HHI > 1,800 alone;
    requires ΔHHI > 100 too (Ch. 1's exercise has it right); line 355's prose
    doesn't match the code filter at 351.

### F. HHI-threshold contradiction (book-wide; pick 2023 and sweep)

40. 2023 thresholds (1,800/Δ100) used correctly: `03:320`, `06:843-916`,
    `06:1062,1077`, Ch. 1 exercise. 2010 thresholds (1,500/2,500) presented as
    current: `06:1039` ("HHI > 2,500 with delta > 200 … under current
    guidelines"), `06:299` (fine if flagged as the 2013-era standard — say so),
    `14-closing.qmd:9`, `15-glossary.qmd:23`, `program/R/helpers.R:409-413`
    (docstring labels 2010 bands "2023 Merger Guidelines thresholds"),
    `10:626-627,659,738` vs. `10:46,866-871` (1,800 vs. 2,500 within one
    chapter).

### G. Code that errors or draws the wrong picture

41. `13-empirical-appendix.qmd:277` — event-study coefficient regex leaves
    `"1:treated"`, `as.numeric()` → all-NA → the centerpiece pre-trends figure
    renders empty. Same regex class of bug at `07:366-370`. Also remove the
    literal placeholder printed into the book at `13:320`.
42. `12-litigation-practice.qmd:548` — Lorenz curve x-axis ranks by member-id
    values, not row position; the plot is a scribble.
43. `12:137-138` — `rep(each=)`/`rep(times=)` swapped relative to
    `expand.grid` ordering; member and period fixed effects are scrambled.
44. `13:569-573` — treatment indicator perfectly collinear with firm FE;
    fixest silently drops the variable of interest.
45. `13:743-771` — `ranger()` lacks `importance=`, so `importance()` errors;
    the per-project bid-CV feature engineering uses `winning_bid` where a
    `bid` column is needed. `13:112` — `plot_balance()` does not exist and the
    path is wrong.
46. `10:437-438` — `log(log_employment) ~ log(log_wage)` double-logs
    already-logged variables; cannot recover the built-in elasticity.
47. `10:165` — `p1 | p2 + plot_layout(...)`: `+` binds tighter than `|`;
    parenthesize.
48. `11:98` — named `antitrust_colors` vector against unmatched levels sends
    all bars to gray; use `unname()`.
49. `05:710` — "common cost shock" computed on the ungrouped frame, so the two
    products get different cost paths; the placebo design's premise is false
    in the code.
50. `02:142-148` + `06:643-699` + `program/scripts/02_finance_extended.R:16` —
    the AA/US event study pulls AAL (no trading history before Dec 2013) and
    never pulls LCC, so *neither merging party appears* in figures whose
    captions and exercises discuss the merging parties. Use AAMRQ/LCC, switch
    mergers (e.g., Alaska/Virgin 2016), or reframe as rivals-only and say so.
    `06:671` also omits JBLU/ALK labels → NA legend entries.
51. `09:933-936` — unguarded read of an absent file (render-fatal), plus schema
    mismatch with `07_digital_platforms.R` (`case` vs `case_name`,
    `year/standard_rate` vs `date/commission_rate`, "Amazon Appstore" vs
    "Amazon", an "Uber Eats" series the script never writes).
52. `12:159` — comment references `permute_plm()`, defined nowhere.
    `06:731-733` — references `sim$summary` and a nest column that
    `run_logit_sim()` does not return. `08:532` — Exercise 2 references "the
    benchmarking scatter code in this chapter," which does not exist.
    `04:534` — Exercise 1 references a 3-product skeleton replaced by a
    10-product one.
53. `13:686,709-714` — power-analysis filter `power >= .79 & power <= .81`
    silently drops the d=0.8 row from the "minimum n" table.
54. `helpers.R` latent bugs (functions currently uncalled but documented):
    `plot_waterfall` zeroes the NA total row its own example uses (317–333);
    `plot_timeline` puts every third event at y=0 and hardcodes `nudge_x = 5`
    days (147,152); `calc_hhi_change` breaks on inputs with extra columns
    (438–446).

### H. Reproducibility (fresh clone cannot render)

55. **No committed `_freeze/` cache** and `data/` ships only a README, so with
    `freeze: auto` every chunk executes — and ~17 chunks hard-fail. **Fix with
    one change: render locally, commit `_freeze/`.**
56. **Eight reads outside the repository** — `"../the south african
    economy/___Contemporary/..."` at `05:198,216,221`, `08:137,142,147`,
    `10:112,124`. Copy the processed aggregates into `data/` with metadata, or
    guard them.
57. **Unguarded missing-file reads**: `03:337`, `05:98-110,308,346`, `06:643`,
    `09:933,936`. **Live API calls at render**: `02:145` (tq_get), `04:320-330`
    and `05:835-836` (fredr). Apply the exemplary tryCatch +
    synthetic-fallback-caption pattern already used at `01:274` and `05:571`.
58. **Dependency manifest**: chapters require ~37 packages;
    `09_install_packages.R` installs 12; `ggsankey` is GitHub-only and can
    never come from `install.packages()`. Add `renv.lock` or complete the
    script.
59. **Broken crossrefs**: `06:467` (`@sec-regulation-remedies-remedies`) and
    `08:12` (em-dash glued into `@sec-research-design---and`). CI's grep
    doesn't catch "Unable to resolve crossref" — extend the pattern.
    Additionally, ten `@sec-empirical-appendix` references target an
    `{.unnumbered}` chapter and will likely render as "Section ??" — move the
    appendix and glossary under Quarto's `appendices:` key (which also fixes
    the lettering) and rename `13-/14-` files to match render order.
60. **Over-claiming captions**: `09:952-954` ("Real platform market share
    data…") and `11:234` ("PatentsView… Real data") describe data the pipeline
    cannot deliver; `01:286-287` labels FRED HHMSDODNS (household mortgage
    liabilities) as a bank-deposit HHI "Real data" figure — and
    `01_fred_extended.R:23-27` mislabels the World Bank bank-concentration
    series as retail/manufacturing HHIs. `05:346` comments "Load real cartel
    bid data" on a file the chapter itself calls synthetic.
61. **CLAUDE.md points at four gitignored, absent files** (`planning/DATA_
    INTEGRATION_GUIDE.md`, `planning/visualization-roadmap.md`,
    `references/CITATION_QUICK_REFERENCE.md`, `planning/API_KEYS_SETUP.md`).
    Commit them or stop referencing them.
62. Minor: 29 orphaned bib entries (harmless); no chapter uses the
    `cache.extra: file.mtime(...)` guard CLAUDE.md mandates; `check_citations.py`
    lives in `program/scripts/`, not `scripts/` as CLAUDE.md says.

### I. Coverage gaps an expert reviewer will name

63. **Ch. 3**: Cellophane fallacy (essential given the book's Art. 102/§8
    framing), smallest-market principle, *Brown Shoe* practical indicia
    (glossary-only today), aggregate diversion.
64. **Ch. 5**: *Hanover Shoe*/*Illinois Brick* vs. the EU passing-on defense —
    the first thing a litigator looks for in a pass-through discussion
    (`05:677,877`).
65. **Ch. 12**: concurrent expert evidence ("hot tubbing") — standard in
    Australia, used in the UK CAT and before the SA Tribunal; glaring absence
    for a comparative text. Natural home after `12:204`.
66. **Ch. 14 capstone has no numbers** (`14:112-126`) — a step list with
    nothing to compute, unlike every methods chapter. Supply a small
    patient-flow/share table so HHI, diversion, and GUPPI are computable.
67. **Glossary gaps** vs. chapter usage: FRAND, treble damages, leniency,
    but-for world, Lerner index, predominance, Daubert.
68. **"Evidence triad" claim** — `14:54` says it "has run through every
    chapter"; the term appears only in 00, 01, 08, 14, 15. Seed it through the
    methods chapters or soften the claim.

### J. Prose/structure residue (small; the voice pass mostly held)

69. Back halves of Chs. 9–11 ("Enhanced Visualizations") read as exported
    notebooks — "Key insights:" / "How to use this analysis:" / "Replace with
    actual data" bullet stacks in a register far below the front-half prose.
    Integrate or cut.
70. Duplicates: Ch. 8 Data Services case box appears twice (`08:249-257` vs
    `08:291-293`); Ch. 3 says its core-tools list twice (`03:73-89`) and tells
    the Grocery Retail story twice (`03:612` vs `03:621`).
71. "Key Takeaways" listicles (`03:640-652`, `05:870`, `06:1038`) are the
    pattern STYLE.md bans; Ch. 1–2 bodies are ~70% boxes/tables with thin
    connective prose; Title Case headers at `02:22-39` against sentence case
    elsewhere.
72. Typos: "a 'umbrella effect'" (`06:701`), "coefficents" (`05:74`),
    "interference" for "inference" (`02:100`); plain-text citations at
    `06:461` against the `@key` convention.

---

## Path to 9.75, in order

The ceiling of this manuscript is high — the design, pedagogy, and SA material
are already top-of-market. Getting there is almost entirely a verification and
engineering exercise, not a writing one.

1. **Truth pass (≈ +1.5).** Fix every item in §§A–C and E–F above. Then adopt
   the rule that closes the class of error, not just the instances: *every
   direct quote, case outcome, statute section, docket number, and specific
   number attached to a named case or inquiry gets a pinned primary source, or
   it comes out.* The fabricated bib entries and the Google quote show the
   failure mode is systematic, so the fix must be too. Finish with the human
   legal read-through `REVIEW.md` already flags as open — and given §§24–25,
   specifically a South African practitioner.

2. **Currency pass (≈ +0.75).** Items in §D. Chs. 7 and 9 need the 2024–2026
   Google/Meta/Epic/DMA record; Ch. 10 needs the 2025 labor guidelines and the
   noncompete-rule endgame. Consider a short "as of mid-2026" enforcement-status
   box pattern so future updates are localized.

3. **Build pass (≈ +0.75).** Items in §§G–H. The one-line summary: a fresh
   clone must render. Commit `_freeze/`, eliminate the out-of-repo reads, guard
   every file read with the existing tryCatch pattern, fix the ~10 broken
   chunks, complete the dependency manifest, fix the crossrefs and move the
   back matter under `appendices:`. Then add a CI job that actually executes
   the render (the current CI is structurally blind to all of this) — that
   locks the gains in.

4. **Honest-data pass (≈ +0.4).** Run the wired ingestion scripts locally with
   keys (the open item from `REVIEW.md`), fix the two FRED-series mislabelings,
   and make every caption's real/synthetic claim true. Where data must stay
   synthetic, the existing `05:571` caption pattern is the model.

5. **Substance pass (≈ +0.25).** Items in §I: Cellophane and critical-loss
   fallacies, Illinois Brick/passing-on, hot tubbing, numbers for the capstone,
   glossary gaps.

6. **Final polish (≈ +0.1).** Items in §J, plus one continuity read for the
   $6-vs-$8 / 58%-vs-47% class of figure-text mismatch — cheapest found by
   rendering and reading the printed outputs against the prose.

Items 1–3 are the score. A methods book earns trust by being *checkable*, and
the book's own best feature — exercises a reader can recompute — sets exactly
the standard the rest of the text now has to meet.
