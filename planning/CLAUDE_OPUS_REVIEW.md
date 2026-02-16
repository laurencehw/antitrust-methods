# Manuscript Review: Antitrust Methods — Research and Practice

**Reviewer:** Claude Opus 4.6 (independent deep review)
**Date:** 2026-02-16
**Scope:** All 14 chapters, bibliography, helpers, data pipeline, Quarto configuration, prior reviews

---

## Overall Score: 7.5 / 10

| Dimension | Score | Notes |
|---|---|---|
| Conceptual architecture & scope | 9.0 | Distinctive framing; tri-jurisdictional coverage is a genuine differentiator |
| Content & topical coverage | 8.0 | Ambitious and largely delivered; two chapters remain thin |
| Writing quality & exposition | 7.5 | Best chapters are publishable; weakest chapter (Labor) needs prose development |
| Code & reproducibility | 7.5 | 98.8% of code chunks execute; helper infrastructure is well-designed |
| Citations & bibliography | 6.5 | 251 total citations, but distribution is uneven; some chapters are under-cited |
| Data integration | 6.0 | Smart use of synthetic data for pedagogy, but core demonstrations lack real-data credibility |
| Structural consistency | 7.5 | Callout boxes are more consistent than prior reviews suggest; minor polish needed |
| Publication readiness | 7.0 | Close to publishable; needs one editorial pass to reach final form |

---

## What This Book Does Exceptionally Well

### 1. The Evidence Triad Is a Genuinely Novel Organizing Framework
The book's insistence that antitrust analysis rests on three legs — empirical analysis, documentary evidence, and expert judgment — is not just a framing device. It structures every chapter. Method boxes teach econometrics, qualitative evidence boxes teach document analysis, and case boxes show how they combine in real investigations. No competing textbook (Motta, Davis & Garcés, Hovenkamp) does this.

### 2. The Tri-Jurisdictional Approach Is a Major Selling Point
Every substantive chapter integrates US, EU, and South African enforcement. The South African content is not tokenistic — it includes specific Competition Tribunal decisions (Netcare, Sasol, Telkom, Mediclinic), the OIPMI digital platforms inquiry, bread and construction cartels, and the public interest test. This positions the book uniquely for practitioners in emerging competition regimes, where the existing English-language literature is US/EU-centric.

### 3. Workflow Diagrams Create Genuine Practitioner Value
Each chapter opens with a workflow diagram showing the investigation arc for that topic — from intake through analysis to remedy. These are absent from academic textbooks and represent the kind of tacit knowledge that junior practitioners need but rarely receive.

### 4. Modern Econometric Methods Are Correctly Taught
The treatment of staggered DiD/TWFE (Chapter 2), specification curves (Chapter 13), and synthetic control (Chapter 10) reflects the post-credibility-revolution state of applied economics. The identification of TWFE as a "litigation vulnerability" is particularly valuable for practitioners.

### 5. The Helper Infrastructure Is Thoughtfully Designed
`theme_antitrust()`, the colorblind-friendly palette, API wrappers, `calc_hhi_change()`, and `plot_waterfall()` create a coherent analytical toolkit. The execution-from-root configuration (`execute-dir: project`) means code paths work from any chapter. This is production-quality infrastructure for a textbook.

---

## Chapter-by-Chapter Assessment

### Ch 00 — Preface (8.5/10)
Polished and effective. The three navigation paths (classroom, practitioner, self-study) are practical. One issue: the preface frames the book as US-primary with EU/UK comparisons, but the actual content gives roughly equal weight to South Africa. This should be updated to explicitly frame the tri-jurisdictional scope.

### Ch 01 — Orientation (7.5/10)
Strong institutional mapping with a useful comparative statute table (US/EU/SA). The Google Search vignette is well-chosen. The timeline and bank HHI visualizations are polished. Citation count (14) is adequate but could be denser given the breadth of institutional material covered.

### Ch 02 — Research Design (8.0/10)
The strongest pedagogical chapter. The method selection decision tree is outstanding. The staggered-adoption discussion is timely. The scoping memo and data pipeline sections contain practical wisdom absent from standard textbooks. The one eval:false DiD scaffold is appropriately marked as a template for customization.

### Ch 03 — Market Definition (8.5/10)
The most technically polished chapter. Five functional code chunks with real data (nycflights13). Every visualization includes interpretation guidance. The debate box on whether market definition is still necessary is well-executed. The SSNIP flowchart is a standout pedagogical element.

### Ch 04 — IO Toolkit (7.0/10)
The structural vs. reduced-form comparison table is one of the best pedagogical elements in the book. The key IO formulas reference table is useful. However, this chapter is more code-heavy and less prose-rich than the best chapters. The bargaining section, while present, could benefit from a more developed Nash-in-Nash worked example.

### Ch 05 — Cartels and Collusion (7.5/10)
The 7-step workflow is an effective structural device. The network analysis with centrality metrics and the placebo test are analytically rich. South African enforcement highlights (bread cartel, construction fast-track, Sasol) are distinctive. Citation count (7) is low for a chapter covering this much ground.

### Ch 06 — Mergers (8.5/10)
The most comprehensive chapter. The UPP formula is correctly implemented (contrary to the Gemini review's claim — see assessment of prior feedback below). The vUPP section, the stock event study using real ticker data, and the logit merger simulation are all well-executed. The HHI thresholds correctly reference the 2023 Guidelines (1,800).

### Ch 07 — Monopolization (8.5/10)
The most polished substantive chapter. Deep, consistent treatment of each conduct category with a reliable pattern: theory → measurement → qualitative evidence → case references. The effective price waterfall correctly models retroactive rebate mechanics. The most heavily cited chapter (39 citations).

### Ch 08 — Regulation and Remedies (7.5/10)
Stronger than prior reviews suggest. Contains 33 citations (tied for second-highest), substantive prose on rate-of-return vs. price-cap regulation, a worked ECPR access pricing example, and a detailed AT&T/Time Warner case box. Not an outline. Could benefit from additional numerical worked examples and South African market inquiry case boxes.

### Ch 09 — Digital Markets (7.5/10)
The theory-to-metric mapping table (10 theories of harm) is excellent reference material. The platform fee visualization uses real data. The generative AI section is timely. The OIPMI coverage is a genuine contribution.

### Ch 10 — Labor Markets (6.0/10)
The weakest chapter. While it covers the right topics (monopsony, HHI, noncompetes, no-poach, gig economy), several sections compress complex material into code scaffolds with minimal prose. The "Southern African enforcement snapshots" section reads as bulleted notes rather than developed analysis. Two eval:false chunks and only 9 citations. This chapter needs the most development work.

### Ch 11 — Innovation, IP, and Antitrust (7.5/10)
The SEP/FRAND section is strong with clear jurisdictional comparisons. The killer acquisitions framework is well-developed. The royalty waterfall and patent citation network are ambitious visualizations. Some unevenness in depth across sections.

### Ch 12 — Litigation Practice (7.5/10)
Better than the prior automated review scored it. Contains 33 citations, substantive sections on evidence mapping, class certification, damages modeling, Daubert readiness, and expert presentation. The DOJ v. Google Search case box is detailed. Not an outline — this is developed prose with practical guidance.

### Ch 13 — Empirical Appendix (7.0/10)
Well-conceived as a practitioner's reference toolkit. The diagnostic gallery (pre-trends, balance plots, specification curves, residual diagnostics, power analysis) is genuinely valuable. The data inventory and chronology templates are useful. Terse prose is appropriate for a reference appendix.

---

## Suggestions for Improvement

### High Priority

**1. Develop Chapter 10 (Labor Markets) into full prose.**
This is the single highest-impact improvement. The chapter covers the right topics but delivers them as compressed scaffolds rather than developed exposition. Specifically:
- Expand the monopsony and labor supply elasticity sections with prose explaining the economic intuition, not just the code
- Develop the noncompete and no-poach sections into full narrative — the FTC rule, the DaVita prosecution, and franchise no-poach agreements each deserve a paragraph or two of context
- Convert the Southern African enforcement snapshots from bullet points to a proper case box
- Add 5-10 more citations (Azar et al., Manning, Benmelech et al. are in the bibliography but under-referenced in the text)

**2. Citation pass on low-citation chapters.**
Chapters 02 (5 citations), 05 (7 citations), 03 (9 citations), and 10 (9 citations) are under-cited relative to their content. Named cases, guidelines, and seminal papers mentioned in prose should be converted to formal `@key` references. This is largely mechanical work — the bibliography already contains most of the needed entries.

**3. Update the Preface to acknowledge the tri-jurisdictional scope.**
The preface says "primary focus is United States antitrust law" but the book's actual content — and genuine competitive advantage — is its tri-jurisdictional coverage (US, EU, South Africa). Update the preface to explicitly frame this as a feature. One paragraph explaining that the South African content serves practitioners in developing-economy competition regimes would suffice.

### Medium Priority

**4. Integrate collected real data into core demonstrations.**
The data pipeline scripts have already collected FRED, airline, and stock price data. Integrating these into the visualizations in Chapters 01, 03, and 04 would demonstrate that the methods work on actual economic data. The infrastructure (helpers.R, API wrappers) is already built — this is a wiring task.

**5. Strengthen Chapter 04 (IO Toolkit) prose.**
The chapter's code-to-prose ratio is higher than ideal. The bargaining section and the logit demand walkthrough would benefit from additional explanatory text. A more detailed Nash-in-Nash worked example would strengthen the chapter significantly.

**6. Add cross-chapter references using Quarto `@sec-` syntax.**
Several chapters reference other chapters by name ("see Chapter 4") rather than using Quarto's cross-reference system. Converting these to `@sec-` references would make the HTML and PDF output more navigable.

### Lower Priority

**7. Expand the bibliography with ~15 additional entries.**
Seminal references that would strengthen the book: Landes & Posner (1981) on market power, Werden (2003) on market definition, Brown Shoe (1962), Ohio v. American Express (2018), Goodman-Bacon (2021) on DiD decomposition, Sun & Abraham (2021) on event studies, and the Stigler Committee (2019) on digital platforms.

**8. Minor code fixes.**
- Chapter 13: The `se()` call on an `lm` object and the `pwr.t.test()` vectorization issue flagged in the prior review should be verified and fixed
- `helpers.R`: `plot_tornado()` has an undeclared `tidyr` dependency; `fetch_fred()`/`fetch_bls()` promise caching but don't implement it

**9. Develop one additional case box for Chapter 10.**
The labor chapter lacks the case box depth of other chapters. A developed case box on DaVita (criminal no-poach prosecution) or the FTC noncompete rule would bring it closer to parity.

---

## Assessment of Prior Feedback (7.0/10 Review)

The prior review you shared scores the manuscript at 7.0/10. I largely agree with the spirit of that assessment but have significant corrections on specific factual claims and some disagreements on severity.

### Where the Prior Review Is Correct

**1. Chapter 10 (Labor Markets) is underdeveloped.** This is the single most accurate observation in the review. The chapter genuinely reads more as a working scaffold than finished prose, and it is the clear weakest link in the manuscript. The suggestion to expand it with prose on the FTC noncompete rule and gig economy classification is sound.

**2. The Preface should be updated to frame the tri-jurisdictional scope.** The mismatch between the US-primary framing and the actual tri-jurisdictional content is real. The reviewer's suggestion to "highlight rather than hide" this as a selling point is exactly right.

**3. A citation pass is needed on under-cited chapters.** The observation about uneven citation coverage is accurate, though the specific chapters identified as problematic are partially wrong (see below).

**4. Real data integration would strengthen the book.** The suggestion to integrate already-collected FRED and BLS data into core chapters is practical and high-impact.

### Where the Prior Review Is Factually Wrong

**1. The UPP formula is CORRECT — there is no error in Chapter 6.**
The review states: "There is a critical error in the current code for the Upward Pricing Pressure (UPP) calculation. Ensure the formula is updated from `diversion * price * (1 - margin)` to the correct `diversion * price * margin`."

This claim originates from the Gemini review (January 2026) but **does not reflect the current state of the manuscript**. The Chapter 6 code (line 107) reads:

```r
upp <- function(diversion, price, margin, efficiency = 0) {
  diversion * price * margin - efficiency
}
```

The prose formula (line 89) reads: `UPP = Diversion × Price × Margin − Efficiency`. A comment on line 106 explicitly explains: "margin = (P-MC)/P, so price * margin = P - MC = profit per unit." This is correct. The `(1 - margin)` error either existed in an earlier draft and was already fixed, or was a misreading by the Gemini reviewer.

**2. The HHI thresholds are ALREADY updated to 2023 Guidelines.**
The review states: "The manuscript still references 2010 thresholds (1,500/2,500), but the 2023 DOJ/FTC Guidelines have shifted the 'highly concentrated' threshold to 1,800."

This is false. The manuscript consistently uses 1,800 as the "highly concentrated" threshold. Chapter 6 (line 794) explicitly labels it "1,800 (2023 Guidelines)." The code in Chapters 3, 6, and 10 all use `hhi < 1800` as the classification boundary. This fix was likely already applied before the review was written, or the reviewer was working from an outdated version.

**3. Chapters 08 and 12 are NOT "outline" chapters.**
The review claims Chapters 04, 08, 10, and 12 are "much thinner than the rest" and "currently read as detailed outlines or code scaffolds rather than finished prose." This is true for Chapter 10 and partially true for Chapter 04, but **false for Chapters 08 and 12**:

- **Chapter 08 (Regulation and Remedies)** contains 33 formal citations, substantive prose on rate-of-return vs. price-cap regulation, a worked ECPR access pricing example ($1.00/minute illustration), and a developed AT&T/Time Warner case box. It is not an outline.

- **Chapter 12 (Litigation Practice)** also contains 33 citations, with developed sections on evidence mapping, class certification, damages modeling (before/after, yardstick, DiD, hedonic), Daubert readiness checklists, and expert presentation guidance. The DOJ v. Google Search case box is detailed and instructive.

The review appears to have relied on the earlier automated review (which scored these chapters at 2.5/5) without independently verifying the current content.

**4. The claim that Chapters 01, 08, and 12 have "almost zero formal citations" is wrong.**
Chapter 01 has 14 citations, Chapter 08 has 33, and Chapter 12 has 33. These are not citation deserts. The chapters that are genuinely under-cited are 02 (5 citations), 05 (7 citations), and 13 (7 citations) — but these were not flagged by the prior review.

### Where the Prior Review Overstates Severity

**1. "Scrub Author Notes and Roadmaps" is less severe than described.**
The review states: "Several chapters currently leak internal project-management language." My thorough search found that the current manuscript is largely clean of author-facing notes. There are no visible "TODO", "FIXME", or "Roadmap X.X" references in the reader-facing prose. Some chapters include "scaffold" and "Replace with actual data" comments within code blocks, but these are intentional pedagogical markers guiding practitioners to customize examples — standard practice in applied methods textbooks. The extensive cleanup described in the prior automated review (Path 3) appears to have already been performed.

**2. "Standardize Callout Box Styles" overstates the inconsistency.**
The review suggests using different callout types (tip, note, warning) for different content types. In practice, the current mapping is internally consistent: `callout-note` for all pedagogical content (method boxes, case boxes, workflows, evidence protocols), `callout-tip` for key takeaways and practical guidance, `callout-important` for critical formulas and statutory frameworks. This is a defensible design choice — using the title prefix ("Case box:", "Method box:", "Debate:") to distinguish content types while maintaining visual uniformity. Whether to change this is a design preference, not a correction of an error.

**3. "Activate Code Scaffolds" overstates the problem.**
The review implies there are many non-functional code chunks. In reality, only 4 out of 329 code chunks (1.2%) are `eval: false`, and all four are intentional templates (DiD scaffold in Ch 2, synthetic control in Ch 10, BLS API template in Ch 10, survey weighting in Ch 13) clearly marked for practitioner customization. This is not a significant deficiency.

### Where the Prior Review Undersells the Manuscript

**1. The score of 7.0 undervalues the conceptual architecture.**
The evidence triad framework, the workflow diagrams, and the consistent theory-measurement-evidence-case pattern across chapters represent genuine pedagogical innovation in the antitrust methods space. No competing textbook integrates qualitative and quantitative evidence this way.

**2. The South African content is a bigger differentiator than acknowledged.**
The review mentions it in passing ("a major selling point for practitioners in emerging competition regimes") but doesn't adequately weight it. This book may be the only English-language practitioner text that treats South African competition enforcement at this depth. For a book targeting an international audience, this is not a minor feature.

**3. The code infrastructure is underappreciated.**
The helper functions, the project-root execution, the colorblind-friendly palette, and the API wrapper architecture create a genuine analytical toolkit that practitioners can reuse. The 98.8% execution rate across 329 code chunks is strong for a textbook in active development.

### Summary of Agreement / Disagreement

| Claim in Prior Review | My Assessment |
|---|---|
| Score: 7.0/10 | **Agree directionally** — I score it 7.5/10, reflecting recent improvements |
| UPP formula error in Ch 6 | **Wrong** — formula is correct in current manuscript |
| Outdated HHI thresholds | **Wrong** — already uses 2023 Guidelines (1,800) |
| Ch 04, 08, 10, 12 are "outline" chapters | **Partially wrong** — true for Ch 10, partially for Ch 04; false for Ch 08 and 12 |
| Ch 01, 08, 12 have "almost zero citations" | **Wrong** — Ch 08 and 12 have 33 citations each; Ch 01 has 14 |
| Scrub author notes and roadmaps | **Overstated** — manuscript is largely clean |
| Standardize callout box styles | **Matter of preference** — current system is internally consistent |
| Flesh out Labor Markets chapter | **Strongly agree** — single highest-impact improvement |
| Update Preface for tri-jurisdictional scope | **Strongly agree** |
| Comprehensive citation pass needed | **Agree** — but on different chapters than identified (Ch 02, 05, 13 need it most) |
| Activate code scaffolds | **Overstated** — only 4 out of 329 chunks are eval:false |
| Integrate real data | **Agree** — practical and high-impact |
| "Easily a 9.5+ manuscript" with improvements | **Agree** — the architecture is there; execution gaps are addressable |

---

## My Path to 9.5/10

The gap between 7.5 and 9.5 is addressable through focused work on a small number of areas:

| Action | Impact | Current State |
|---|---|---|
| Develop Chapter 10 (Labor) into full prose | +0.5 | Weakest chapter; needs narrative expansion |
| Citation pass on Ch 02, 05, 10, 13 | +0.4 | Mechanical work; bib entries mostly exist |
| Update Preface for tri-jurisdictional framing | +0.2 | One paragraph change |
| Integrate FRED/airline real data into Ch 01, 03, 04 | +0.3 | Data collected; needs wiring |
| Strengthen Ch 04 prose (bargaining, logit walkthrough) | +0.2 | Good structure; needs more text |
| Add ~15 bibliography entries for seminal references | +0.1 | Straightforward additions |
| Minor code fixes (Ch 13 runtime errors, helpers.R) | +0.1 | Small targeted fixes |
| Cross-chapter `@sec-` references | +0.05 | Polish item |
| Additional case box for Ch 10 | +0.05 | DaVita or FTC noncompete |

**The single highest-return action is developing Chapter 10.** Everything else is incremental polish on what is already a strong manuscript.

---

## Final Assessment

This is a serious, well-architected practitioner textbook that fills a genuine gap in the antitrust methods literature. The evidence triad framework, the tri-jurisdictional coverage, and the integration of code with legal and economic analysis represent real contributions. The strongest chapters (03, 06, 07) are publishable now. The weakest chapter (10) needs prose development but not reconceptualization — the structure is sound.

The prior reviews (both automated and the 7.0/10 feedback) were written against earlier drafts and contain several factual claims that no longer hold. The manuscript has improved since those reviews were written. The remaining work is concentrated, not diffuse — develop one chapter, add citations to four chapters, update the preface, wire in real data — and the result would be a distinctive and valuable addition to the field.
