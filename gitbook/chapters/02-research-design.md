# Research Design: Quantitative and Qualitative 

The previous chapter oriented you to the institutions and legal standards that shape antitrust work. With that foundation in place, we now turn to methodology. How do you design research that will persuade regulators, courts, and opposing experts? This chapter introduces the core principles of research design---both quantitative and qualitative---that underpin the specific applications in later chapters.

The goal is not just to learn techniques, but to develop the judgment to choose among them. Different questions call for different methods, and the choice depends as much on available data and institutional constraints as on statistical properties. We emphasize the "credibility revolution" in applied economics while recognizing that qualitative evidence often plays an equally important role in antitrust matters.

## Learning goals
The goal of this chapter is to help you translate messy case facts into evidence that withstands scrutiny from opposing experts, agency staff, and judges. You will learn how to articulate research questions that map directly to legal theories of harm and to choose empirical strategies—diff-in-diff, event study, instrumental variables (IV), regression discontinuity (RDD), matching, or structural models—that are feasible with available data. Equally important, you will practice designing qualitative instruments (surveys, interviews, document coding schemes) that align with those empirical tests so each stream of evidence reinforces the others.

Because antitrust matters often unfold across jurisdictions, we emphasize how to document design choices so they travel: a memorandum prepared for the US DOJ should be intelligible to DG COMP economists or the South African Competition Tribunal. That means explicit statements about identifying assumptions, robustness diagnostics, and data provenance. Throughout the chapter we draw on recent matters such as US hospital merger retrospectives, EU telecom remedies, and South African ride-hailing and grocery market inquiries.

## Workflow
### Scoping memo
Every matter should begin with a scoping memo linking the narrative theory of harm to measurable outcomes. Specify the primary question (“Did the 2018 hospital merger in Texas raise commercial insurance prices?”), outline plausible channels (unilateral effects vs. coordination), and list essential datasets with owners, legal process required, and likely cleaning steps. Capture timing constraints—the DOJ’s Second Request clock, the CMA’s Phase I deadlines, or the Competition Commission South Africa’s 60-business-day merger review period—and highlight non-negotiable assumptions (e.g., availability of claims-level data or ability to survey procurement managers). Include citations to precedent such as merger retrospectives [@ashenfelter_hosken_2010]---the methodology we apply in [Chapter 6: Mergers](06-mergers.md)---or class-certification common-impact decisions [@dickey_rubinfeld_2014] so legal teams can anticipate how courts reacted to similar designs.

### Data pipeline architecture
Treat the data pipeline as infrastructure. Raw productions, public datasets, and hand-entered chronologies should land in `data/raw`, with documented schemas and hashing to ensure integrity. Cleaning scripts housed in `scripts/` or `R/` should emit analytic files to `data/derived`, complete with README files explaining variable creation, filtering rules, and version numbers. Cloud-based teams should use reproducible environments (Renv, Conda, Docker) so every regression or visualization is rerunnable months later when litigation heats up. For South African matters, plan for hybrid data sources—local procurement records may arrive as PDFs, while US financials might come via SEC APIs—so build ingestion scripts that normalize currencies, indexation, and time zones.

### Pre-analysis and litigation deliverables
Before estimating anything, write a pre-analysis plan that documents main outcomes, treatment definitions, control groups, identifying assumptions, and robustness checks. This discipline is not just for academics: DOJ and FTC staff frequently ask for pre-specified models, DG COMP expects methodological appendices, and South African tribunals often require plain-language summaries usable in simultaneous interpretation. Include sensitivity tests (e.g., alternative market definitions, exclusion of outlier distributors, placebo periods) and specify the qualitative evidence that will contextualize results. As you progress, convert technical memos into courtroom-ready outputs—slide decks, white papers, expert declarations—without sacrificing reproducibility.

## The Modern Causal Toolkit: The Credibility Revolution

Modern antitrust economics increasingly relies on the "credibility revolution" in applied microeconomics—a shift from complex structural adjustments to transparent research designs that mimic randomized experiments. As championed by @angrist_pischke_2009 and popularized in *Causal Inference: The Mixtape* [@cunningham_2021], the goal is to identify a "natural experiment" where treatment (e.g., a merger, a cartel breakdown, or a regulation) is as good as randomly assigned.

### The "Design-Based" Philosophy
Instead of asking "what controls do I need to fix my model?", design-based thinking asks "where does the variation come from?" If you cannot draw a Directed Acyclic Graph (DAG) showing how the treatment was assigned independent of the outcome, no amount of regression control will save the analysis [@pearl_2009]. This "reduced form" approach contrasts with the "structural" methods used in merger simulation (see [Chapter 4: IO Toolkit](04-io-toolkit.md)), which rely on theoretical models to estimate "deep parameters".

This approach prioritizes:
1.  **Clean Identification:** Finding shocks (institutional details, policy boundaries, timing quirks) that separate treated and control groups.
2.  **Transparency:** Presenting raw data visuals (like the event study plots below) before showing regression tables.
3.  **Falsification:** Rigorously testing "placebos" (e.g., testing for effects before the merger happened, showing no effects in a time period where the treatment is not expected to have an effect) to prove the design is valid.

### Core Causal Toolkit
While the toolkit is vast, antitrust practitioners lean heavily on a few workhorses:
-   **Difference-in-Differences (DiD):** The gold standard for retrospective merger analysis.
-   **Synthetic Control:** Crucial for "N=1" cases (e.g., a single national merger) where no single control unit exists.
-   **Instrumental Variables (IV):** Used when prices are endogenous; we look for "shifters" (like tax changes or weather) that move supply but not demand.
-   **Regression Discontinuity (RDD):** Exploits arbitrary cutoffs (e.g., population thresholds for regulation) to compare similar firms on either side of the line.

{% hint style="info" %}
**Method Selection Guide**
```
                            WHAT IS YOUR QUESTION?
                                     |
          +--------------------------+---------------------------+
          |                          |                           |
          v                          v                           v
   RETROSPECTIVE              PROSPECTIVE                 DAMAGES
   "Did X cause Y?"           "Will X cause Y?"           "How much harm?"
          |                          |                           |
          v                          v                           v
   Do you have a             Use STRUCTURAL               Calculate
   control group?            SIMULATION                   overcharge or
          |                  (Chapter 4, 6)               lost profits
    +-----+-----+                                         (Chapter 12)
    |           |
    v           v
   YES          NO
    |           |
    v           v
   DiD or    Synthetic
   Event     Control or
   Study     Before/After
    |
    v
   Is treatment
   timing staggered?
    |
    +-----+-----+
    |           |
    v           v
   YES          NO
    |           |
    v           v
   Callaway-  Standard
   Sant'Anna  TWFE
   or Sun-    (with
   Abraham    pre-trends)
```
**Key diagnostic:** Always plot raw data before and after treatment. If parallel trends fail visually, no estimator will save you.
{% endhint %}

| Method | When to Use | Key Assumption | Antitrust Application |
|:-------|:------------|:---------------|:---------------------|
| **DiD** | Policy/merger with clear timing, parallel control group | Parallel trends | Merger retrospectives ([Chapter 6: Mergers](06-mergers.md)), cartel breakdowns ([Chapter 5: Cartels](05-cartels.md)) |
| **Synthetic Control** | Single treated unit, multiple potential controls | Weights construct valid counterfactual | National mergers, single-market interventions |
| **IV** | Endogenous treatment/price, valid instrument available | Relevance + exclusion | Demand estimation, price-fixing damages |
| **RDD** | Sharp cutoff determines treatment | Continuity at threshold | Regulatory thresholds, antitrust exemptions |
| **Structural** | Forward-looking prediction needed | Model correctly specified | Merger simulation, counterfactual pricing |

### The Evolution of DiD
A critical development in recent years is the realization that the standard Two-Way Fixed Effects (TWFE) estimator can be biased when treatment timing varies (staggered adoption). If you are analyzing a rollup strategy where a firm buys competitors in 2018, 2019, and 2020, standard regressions might compare early-treated units to late-treated units in ways that invert the sign of the effect.

Modern estimators like @callaway_santanna_2021 or @sun_abraham_2021 (implemented in R packages `did` and `fixest`) explicitly handle this heterogeneity. In litigation, relying on "old" TWFE without robustness checks is now a vulnerability.

{% hint style="success" %}
**Getting Up to Speed**
For a practical guide to these methods, we recommend three complementary resources:
1.  **"Causal Inference: The Mixtape"** [@cunningham_2021]: Excellent for intuition and history. [mixtape.scunning.com](https://mixtape.scunning.com/)
2.  **"The Effect"** [@huntington_klein_2021]: A highly accessible introduction to design-based thinking. [theeffectbook.net](https://theeffectbook.net/)
3.  **"Causal Inference for the Brave and True"** [@alves_2022]: Covers intermediate topics including machine-learning approaches to interference. [matheusfacure.github.io/python-causality-handbook](https://matheusfacure.github.io/python-causality-handbook/)

For the academic foundations, see @angrist_pischke_2009 and their companion *Mastering 'Metrics* [@angrist_pischke_2015].
{% endhint %}

{% hint style="info" %}
**Method box: Causal tools**
**Diff-in-diff and event studies**: Always test for pre-trend equivalence using graphical diagnostics and formal tests. Dynamic specifications (leads/lags) are persuasive in telecom or energy cases where policy shocks phase in, and in remedy evaluations as we show in [Chapter 8: Regulation & Remedies](08-regulation-remedies.md). The DOJ used this approach in Spirit/JetBlue analyses [@us_spirit_jetblue_2023], while South African regulators applied similar diagnostics to evaluate grocery supplier rebates.  
**Instrumental variables**: When supply or demand shocks are endogenous—think of hospital mergers with network design responses—search for plausibly exogenous instruments, such as regulatory bed caps or travel-time thresholds. Document relevance and exclusion explicitly; DG COMP is unforgiving when those steps are skipped.  
**Panel estimators**: Fixed-effects (FE) or two-way FE models remain workhorses but require caution under staggered adoption. Use estimators like `did::att_gt` or `fixest`’s Sun-Abraham implementation, and explain weighting schemes in your declarations.  
**Synthetic control / matrix completion**: For markets with single treated units (e.g., the CMA’s analysis of a UK airport slot divestiture), synthetic control and ridge-regularized matrix completion provide transparent counterfactuals. Include donor-pool rationale and placebo reassignments.  
**Inference**: With few clusters (common in mining or port cases), complement cluster-robust standard errors with wild bootstrap or randomization inference to avoid overconfident p-values.
{% endhint %}

{% hint style="info" %}
**Qualitative methods box**
**Surveys and diversion studies**: Define the decision-maker (consumer vs. procurement lead), sampling frame, and recall period before crafting questions. The FTC’s Staples/Essendant review [@ftc_staples_essendant_2019] and the Competition Commission South Africa’s ride-hailing inquiry both relied on carefully screened respondents to estimate diversion ratios---a key input for market definition as discussed in [Chapter 3: Market Definition](03-market-definition.md). Pre-test instruments to detect anchoring or order effects, and document weighting schemes.  
**Structured case studies**: Build matrices that compare conduct across firms, time, and geographies—e.g., analyzing fertilizer cartels in the US, EU, and South Africa to see whether “industry meetings” align with price spikes. Use the same template so qualitative coders can draw parallels to econometric findings.  
**Document coding**: Create controlled vocabularies for internal emails, board decks, and pricing memos. Tag each excerpt with custodian, date, and issue code; this facilitates linking to regression covariates (e.g., a “capacity discipline” tag aligned with utilization metrics).  
**Expert elicitation**: When engaging industry experts (engineers, procurement veterans), capture their priors, data references, and compensation structures. Tribunals increasingly ask for transparency, especially in South African public-interest hearings.
{% endhint %}

{% hint style="info" %}
**Debate**
Three debates recur in nearly every case. First, **stated vs. revealed preferences**: surveys can illuminate multi-sided platforms where transaction data are limited (app stores, adtech), but agencies often prefer revealed behavior. One compromise is to calibrate survey responses against observable churn or clickstream metrics, as seen in the DOJ’s ad-tech inquiries [@us_google_search_2023]. Second, **parallel trends under innovation**: in markets with rapid product cycles (semiconductors, fintech), clean control groups may not exist. Explain how you use feature-adjusted indices, synthetic controls, or machine-learning prognostics to approximate counterfactuals, and disclose residual risk. Third, **placebo tests**: courts increasingly expect falsification exercises. In wage-fixing litigation (e.g., poultry processors [@us_jindal_2021], US tech no-poach cases [@us_high_tech_nopoach_2015]), teams ran placebo periods and alternative employee groups to show effects were specific to collusive periods rather than macro shocks---labor market concentration analysis is developed in [Chapter 10: Labor Markets](10-labor-markets.md).
{% endhint %}

## Visualizations

### Event study around a merger announcement
This figure uses publicly available equity data to demonstrate how to structure an event-study diagnostic for merger retrospectives or policy shocks. Replace tickers and the `event_date` to align with a specific matter; the scaffold keeps everything tidy for quick reporting.

```r
library(tidyquant)
library(dplyr)
library(ggplot2)
source("program/R/helpers.R")

event_date <- as.Date("2013-02-14") # American Airlines/US Airways announcement
tickers <- c("AAL", "DAL", "LUV", "SPY") # SPY proxy for market return

prices <- tq_get(
  tickers,
  from = event_date - lubridate::days(180),
  to   = event_date + lubridate::days(180)
) |>
  dplyr::group_by(symbol) |>
  dplyr::arrange(date) |>
  dplyr::mutate(ret = log(adjusted) - log(dplyr::lag(adjusted))) |>
  dplyr::ungroup()

market <- prices |>
  dplyr::filter(symbol == "SPY") |>
  dplyr::select(date, mkt_ret = ret)

cars <- prices |>
  dplyr::filter(symbol != "SPY") |>
  dplyr::left_join(market, by = "date") |>
  dplyr::mutate(
    abnormal_ret = ret - mkt_ret,
    rel_day = as.integer(date - event_date)
  ) |>
  dplyr::filter(rel_day >= -30, rel_day <= 30, !is.na(abnormal_ret)) |>
  dplyr::group_by(symbol) |>
  dplyr::arrange(rel_day) |>
  dplyr::mutate(car = cumsum(abnormal_ret))

ggplot(cars, aes(x = rel_day, y = car, color = symbol)) +
  geom_hline(yintercept = 0, linewidth = 0.3, color = "gray65") +
  geom_line(linewidth = 0.9) +
  labs(
    title = "Cumulative Abnormal Returns Around Merger Announcement",
    subtitle = "Airline equities vs. SPY benchmark (±30 trading days)",
    x = "Event time (days relative to 2013-02-14)",
    y = "Cumulative abnormal return",
    color = NULL
  ) +
  theme_antitrust() +
  theme(legend.position = "bottom")
```

## Exercises

1. **Conceptual.** Draw a DAG for a hospital merger analysis where the treatment is the merger, the outcome is price, and potential confounders include local demand shocks and insurer network changes. Identify at least one valid instrument and explain why it satisfies the exclusion restriction.

2. **Data/code.** Using the event study code scaffold in this chapter, modify the tickers to analyze the cumulative abnormal returns around a different merger announcement of your choosing. Compare the pattern for the merging parties vs. rivals vs. the market index.

3. **Conceptual.** Explain why standard two-way fixed effects (TWFE) can produce biased estimates under staggered treatment timing. Sketch a scenario in antitrust (e.g., a serial acquirer buying firms in 2018, 2019, 2020) where this bias would be particularly severe.

4. **Case discussion.** The DOJ's Google Search case relied on both quantitative evidence (auction data, default share calculations) and qualitative evidence (executive testimony, internal documents). How would you structure a pre-analysis plan that integrates both streams? What would you specify ex ante?

5. **Conceptual.** A South African Competition Commission investigation has access to 18 months of transaction data from two grocery chains but no natural experiment or policy shock. What research design options are available? Discuss the tradeoffs between before/after, cross-sectional, and structural approaches.

## Looking ahead
Document every decision from scoping memo to estimation so later chapters can layer on industry-specific models. Begin compiling a reusable appendix that includes sample interview protocols, diversion survey templates, and code snippets for data validation. We will lean on these assets when we turn to market definition, industrial-organization toolkits, and merger simulation, so note any gaps (e.g., need a telecom-grade cost index or South African procurement benchmark) while the evidence record is still flexible.

## Code box: diff-in-diff scaffold
```r
# In a typical DD setup:
# library(fixest)
library(did)

# expected columns:
# - id: firm, product, or region
# - time: monthly/quarterly period (Date or numeric)
# - treat: 0/1 indicator
# - outcome: price, margin, volume, quality score, etc.
# - controls: cost indices, demand shifters, policy dummies

# panel_data <- panel_data %>%
#   filter(between(time, as.Date("2016-01-01"), as.Date("2023-12-31"))) %>%
#   mutate(post = if_else(time >= treat_date[id], 1, 0))

# att_gt <- att_gt(yname = "outcome", tname = "time", idname = "id",
#                  gname = "treat_time", data = panel_data, panel = TRUE,
#                  xformla = ~ controls, clustervars = "id")
# summary(att_gt)

# Sun & Abraham style with fixest, clustered at market level:
# feols(outcome ~ i(time, treat, ref = REF_PERIOD) + controls | id + time,
#       data = panel_data, cluster = ~market_id)
```
