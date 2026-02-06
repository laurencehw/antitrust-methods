# Industrial Organization Toolkit

The previous chapters showed how to define markets and conduct causal research. This chapter introduces the industrial organization (IO) toolkit---the analytical machinery that powers much of modern antitrust analysis. These methods allow us to model how firms compete, estimate parameters like marginal costs and demand elasticities, and simulate the effects of mergers or conduct before they occur.

The demand models, cost estimates, and bargaining frameworks introduced here feed directly into the merger simulations in Chapter 6, the exclusionary conduct analysis in Chapter 7, and the digital markets analysis in Chapter 9.

## Learning goals

This chapter sits between descriptive evidence and full merger simulations. You will learn when to deploy lightweight demand or supply models, how to explain their assumptions to agencies and courts, and how to integrate qualitative evidence (contracts, governance documents, interviews) so the results stay connected to observable market behavior.

By the end you should be able to:

- Use IO models to link conduct to outcomes: demand estimation, cost modeling, bargaining, and equilibrium effects.
- Choose between structural and reduced-form evidence depending on data, timing, and tribunal expectations.
- Capture platform-specific dynamics (multi-homing, indirect network effects, parity clauses).
- Explain each model’s intuition, diagnostics, and jurisdictional track record.

## Core components
1. **Demand estimation.** Start with logit/BLP-lite intuition (shares vs. prices and characteristics) (Nevo, 2000); (Berry, Levinsohn & Pakes, 1995). Add nested logit or random coefficients when differentiation is material, and report diversion matrices.  
2. **Supply modeling & pass-through.** Recover marginal costs via first-order conditions (FOCs) or reduced-form models, and estimate pass-through elasticities (see code below).  
3. **Bargaining frameworks.** Nash-in-Nash approximations for platform or healthcare negotiations. For theoretical foundations, see (Tirole, 1988) and (Motta, 2004).  
4. **Multi-sided interactions.** Incorporate indirect network effects, multi-homing rates, and platform policies (MFNs, parity clauses) as either covariates or structural parameters (Rochet & Tirole, 2003).  
5. **Diagnostics & validation.** Cross-check simulated price effects against historical shocks, third-party benchmarks (Ashenfelter & Hosken, 2010), or rival stock reactions.

## Structural vs. Reduced Form Approaches

Antitrust economics relies on two distinct methodological traditions. Knowing when to use each is central to designing an effective expert report.

### The Contrast

*   **Structural Modeling (Simulation):**
    *   **Definition:** Estimates "deep parameters" (primitives like utility weights and marginal costs) that are assumed to remain stable even when the market changes. It imposes a specific theoretical framework (e.g., Bertrand-Nash competition with Logit demand) to link these parameters to outcomes.
    *   **Primary Use:** **Merger Simulation**. Because the post-merger world does not yet exist, we cannot measure it directly. We must *simulate* the new equilibrium by feeding the estimated parameters into a model of the merged firm.
    *   **Pros/Cons:** It is the only way to predict the future (prospective analysis), but the results are only as good as the model's assumptions (functional form, conduct).

*   **Reduced Form (Causal Inference):**
    *   **Definition:** Estimates the relationship between observable variables (e.g., price and a policy dummy) without recovering the underlying primitives or imposing a full model of competition. It focuses on identifying a causal effect from historical variation.
    *   **Primary Use:** **Retrospectives and Damages**. Used to answer "what happened?" (e.g., "Did the cartel raise prices?" or "Did the 2018 merger harm consumers?"). Common tools include Difference-in-Differences (DiD) and instrumental variables (IV) regressions.
    *   **Pros/Cons:** Relies on fewer assumptions about market conduct, but cannot typically predict the effect of a *new* policy or merger (the Lucas Critique).

### Complementarity in Practice

{% hint style="success" %}
**Best practice: Combine both approaches.** Use a **reduced-form** event study to show that a past merger in the same industry raised prices by 5%. Then calibrate a **structural** simulation model to reproduce that 5% increase. Once the model is "validated" by the historical data, you can confidently use it to predict the effects of the *current* merger.
{% endhint %}

| Criterion | Structural (Simulation) | Reduced-Form (Causal) |
|:----------|:------------------------|:---------------------|
| **Question** | "What will happen?" | "What did happen?" |
| **Data needs** | Prices, shares, characteristics | Treatment/control, panel |
| **Assumptions** | Equilibrium model, functional form | Parallel trends, exogeneity |
| **Output** | Predicted price changes | Estimated effects |
| **Robustness** | Sensitivity to model choice | Placebo tests, pre-trends |
| **Agency preference** | Mergers (prospective) | Retrospectives, damages |
| **Key packages** | `BLPestimatoR`, custom code | `fixest`, `did`, `synthdid` |

{% hint style="danger" %}
**Key IO Formulas**

| Formula | Definition | Use Case |
|:--------|:-----------|:---------|
| **UPP** = Diversion x Margin - Efficiency | Upward Pricing Pressure | Merger screening |
| **GUPPI** = Diversion x Margin | Gross UPP (no efficiencies) | Agency benchmarks |
| **Lerner Index** = (P - MC) / P | Price-cost margin | Market power proxy |
| **Pass-through** = dP/dC | Price response to cost | Damages, EDM |
| **Critical Loss** = SSNIP / (SSNIP + Margin) | Break-even loss for SSNIP | Market definition |
| **HHI** = Sum of squared shares | Concentration index | Structural presumption |
| **Delta HHI** = 2 x Share1 x Share2 | Merger-induced HHI change | Screening threshold |
{% endhint %}

{% hint style="info" %}
**Method box**

**UPP/GUPPI.** Use diversion ratios and margins to compute Upward Pricing Pressure (UPP) or Gross Upward Pricing Pressure Index (GUPPI). See Farrell & Shapiro (2010) "Antitrust Evaluation of Horizontal Mergers: An Economic Alternative to Market Definition" for the theoretical foundation.  
**Pass-through regressions.** Run `feols(price ~ cost_shifter | product + time)` with clustered standard errors to get empirical pass-through before turning to structural models.  
**Simulation scaffolds.** When time is short, build a logit demand system with constant marginal costs to approximate unilateral effects, then refine later.
{% endhint %}

{% hint style="info" %}
**Qualitative evidence**

**Contracts & governance.** MFNs, parity clauses, data-sharing obligations, and service-level agreements indicate how flexible margins are; tie them to modeling assumptions.  
**Design choices.** Product defaults, API throttling, or app-store ranking algorithms signal platform steering and inform multi-sided parameters.  
**Field interviews.** Operations or procurement leads can explain capacity constraints, switching costs, or negotiation cycles—use these insights to set priors for bargaining power or cost recovery.
{% endhint %}

{% hint style="info" %}
**Citations and comparative note**

- Cite foundational IO models and their antitrust applications (e.g., diversion/UPP notes in merger guidelines (DOJ/FTC Horizontal Merger Guidelines, 2010); (EC Horizontal Merger Guidelines, 2004)).
- Note jurisdictional differences in treatment of MFNs/parity clauses (e.g., EU/UK platform cases vs. US approach).
- Attribute platform multi-sided modeling references (e.g., Rochet-Tirole style papers) and cite any A/B evidence or agency decisions when used.
{% endhint %}

---

## Demand skeleton: simple logit example

```r
library(dplyr)
library(tibble)
source("program/R/helpers.R")

products <- tribble(
  ~product, ~price, ~share, ~feature_score,
  "A", 12, 0.25, 0.6,
  "B", 10, 0.20, 0.5,
  "C", 9,  0.15, 0.4,
  "Outside", 0, 0.40, 0
)

logit_data <- products |>
  mutate(
    share_ratio = share / share[product == "Outside"],
    logit_dep = log(share_ratio)
  ) |>
  filter(product != "Outside")

logit_model <- lm(logit_dep ~ price + feature_score, data = logit_data)
coef(logit_model)
```
Document instruments (cost shifters) if price endogeneity is a concern. Expand to nested logit or BLP as needed.

## UPP/GUPPI calculation and sensitivity analysis

Upward Pricing Pressure (UPP) is a quick screen to assess whether a merger creates incentives to raise prices. It combines diversion ratios (where do customers go?) and margins (how profitable are those diverted sales?). High UPP suggests competitive concerns; low or negative UPP (when efficiencies exceed pricing pressure) suggests the merger may be benign.

### Basic UPP calculation
```r
library(dplyr)
library(ggplot2)

upp <- function(diversion, margin, efficiency = 0) {
  (diversion * margin) - efficiency
}

upp_results <- tibble::tribble(
  ~pair, ~diversion, ~margin, ~efficiency,
  "Product A -> B", 0.35, 0.45, 0.05,
  "Product B -> A", 0.28, 0.40, 0.02
) |>
  mutate(
    upp = upp(diversion, margin, efficiency),
    guppi = diversion * margin,  # Gross UPP (before efficiencies)
    interpretation = case_when(
      upp > 0.10 ~ "High pricing pressure",
      upp > 0.05 ~ "Moderate pricing pressure",
      upp > 0 ~ "Low pricing pressure",
      TRUE ~ "No pricing pressure (efficiencies dominate)"
    )
  )

upp_results
```

### UPP/GUPPI sensitivity tornado chart
A tornado chart shows how UPP changes as we vary key inputs (diversion, margin, efficiencies) one at a time. This helps communicate uncertainty and identify which parameters matter most for the competitive assessment.

```r
library(dplyr)
library(ggplot2)
library(tidyr)
source("program/R/helpers.R")

# Base case parameters (Product A -> Product B merger)
base_diversion <- 0.30
base_margin <- 0.40
base_efficiency <- 0.03

base_upp <- (base_diversion * base_margin) - base_efficiency

# Sensitivity ranges: vary each parameter ±30% while holding others constant
sensitivity <- tibble::tribble(
  ~parameter,            ~low_value, ~high_value,
  "Diversion ratio",     base_diversion * 0.7,  base_diversion * 1.3,
  "Margin (B)",          base_margin * 0.7,     base_margin * 1.3,
  "Efficiency credit",   base_efficiency * 0.5, base_efficiency * 1.5
) |>
  rowwise() |>
  mutate(
    upp_low = case_when(
      parameter == "Diversion ratio" ~ (low_value * base_margin) - base_efficiency,
      parameter == "Margin (B)" ~ (base_diversion * low_value) - base_efficiency,
      parameter == "Efficiency credit" ~ (base_diversion * base_margin) - low_value,
      TRUE ~ NA_real_
    ),
    upp_high = case_when(
      parameter == "Diversion ratio" ~ (high_value * base_margin) - base_efficiency,
      parameter == "Margin (B)" ~ (base_diversion * high_value) - base_efficiency,
      parameter == "Efficiency credit" ~ (base_diversion * base_margin) - high_value,
      TRUE ~ NA_real_
    ),
    range = abs(upp_high - upp_low)
  ) |>
  ungroup() |>
  arrange(desc(range))

# Create ordered factor for tornado plot
sensitivity <- sensitivity |>
  mutate(parameter = factor(parameter, levels = rev(parameter)))

# Tornado chart
ggplot(sensitivity) +
  geom_segment(aes(x = upp_low, xend = upp_high,
                   y = parameter, yend = parameter),
               linewidth = 8, color = "#0072B2", alpha = 0.7) +
  geom_vline(xintercept = base_upp, linetype = "dashed",
             color = "#D55E00", linewidth = 1) +
  geom_vline(xintercept = 0, linetype = "solid",
             color = "black", linewidth = 0.5) +
  annotate("text", x = base_upp, y = 3.5,
           label = paste0("Base case UPP: ", round(base_upp, 3)),
           hjust = -0.1, vjust = -0.5, size = 4, fontface = "bold", color = "#D55E00") +
  annotate("rect", xmin = 0.05, xmax = 0.15, ymin = -Inf, ymax = Inf,
           fill = "red", alpha = 0.1) +
  annotate("text", x = 0.10, y = 0.5,
           label = "Likely concern zone\n(UPP > 5%)",
           size = 3, color = "darkred", fontface = "italic") +
  scale_x_continuous(labels = scales::percent_format(),
                     breaks = seq(-0.05, 0.20, by = 0.05)) +
  labs(
    title = "UPP Sensitivity Analysis (Tornado Chart)",
    subtitle = "How does UPP change as we vary key inputs? Longer bars = more sensitive parameters",
    x = "Upward Pricing Pressure (UPP)",
    y = NULL,
    caption = paste0("Base case: Diversion = ", round(base_diversion, 2),
                    ", Margin = ", round(base_margin, 2),
                    ", Efficiency = ", round(base_efficiency, 2))
  ) +
  theme_antitrust() +
  theme(
    plot.title.position = "plot",
    panel.grid.major.y = element_blank()
  )

# Summary table
cat("\nSensitivity analysis summary:\n")
sensitivity |>
  mutate(
    across(c(low_value, high_value, upp_low, upp_high),
           ~round(., 4)),
    range = round(range, 4),
    impact = case_when(
      range > 0.04 ~ "HIGH impact on UPP",
      range > 0.02 ~ "MODERATE impact",
      TRUE ~ "LOW impact"
    )
  ) |>
  select(parameter, low_value, high_value, upp_low, upp_high, range, impact) |>
  print(n = Inf)
```

**How to use this chart:**
- **Longest bars** = most sensitive parameters. Focus data collection and robustness checks on these.
- **Base case** (dashed orange line): Your central UPP estimate.
- **Zero line**: UPP < 0 suggests efficiencies outweigh pricing pressure.
- **Concern threshold** (shaded region): Many agencies use 5% as a rule of thumb; higher UPP warrants closer scrutiny.

**Practical insights:**
- If **diversion** creates the widest swing, invest in better switching data (surveys, natural experiments, loyalty panels).
- If **margin** is most sensitive, request detailed cost accounting or validate with third-party benchmarks.
- If **efficiencies** have large impact, document synergy claims rigorously (pre/post integration plans, expert affidavits).

**GUPPI variant:** To calculate GUPPI instead of UPP, simply omit the efficiency credit: `GUPPI = diversion × margin`. Some agencies prefer GUPPI because it isolates the gross pricing pressure before offsetting efficiencies.

Tie the efficiency term to documented synergies or cost savings (procurement economies, network effects, R&D cost sharing). For cross-border mergers, adjust for currency and local cost differences.

## Visualizations

### Pass-through diagnostic using public price indices
Pass-through analysis estimates how much of a cost change flows through to consumer prices. It matters for cartel damages (upstream overcharge flowing to downstream harm), merger analysis (whether cost savings benefit consumers), and vertical restraints. This example uses real FRED data for gasoline prices.

```r
library(fredr)
library(dplyr)
library(tidyr)
library(ggplot2)
library(patchwork)
source("program/R/helpers.R")

fredr_set_key(Sys.getenv("FRED_API_KEY"))

# Producer Price Index: Petroleum refining
ppi <- fredr(
  series_id = "PCU324110324110",
  observation_start = as.Date("2015-01-01")
) |>
  transmute(date, ppi = value)

# Consumer Price Index: Gasoline (all types)
cpi <- fredr(
  series_id = "CUSR0000SETB01",
  observation_start = as.Date("2015-01-01")
) |>
  transmute(date, cpi = value)

pass_df <- inner_join(ppi, cpi, by = "date") |>
  arrange(date) |>
  mutate(
    ppi_index = ppi / first(ppi) * 100,
    cpi_index = cpi / first(cpi) * 100,
    # Calculate changes for pass-through regression
    ppi_change = (ppi - lag(ppi)) / lag(ppi),
    cpi_change = (cpi - lag(cpi)) / lag(cpi)
  ) |>
  drop_na()

# Time series plot
pass_long <- pass_df |>
  select(date, Producer = ppi_index, Consumer = cpi_index) |>
  pivot_longer(-date, names_to = "series", values_to = "index")

p1 <- ggplot(pass_long, aes(x = date, y = index, color = series)) +
  geom_line(linewidth = 1.1) +
  scale_color_manual(values = c("Producer" = "#D55E00", "Consumer" = "#0072B2")) +
  labs(
    title = "Producer vs. Consumer Gasoline Price Indices",
    subtitle = "Tracking cost pass-through from refineries to retail",
    x = NULL,
    y = "Index (Jan 2015 = 100)",
    color = NULL
  ) +
  theme_antitrust() +
  theme(
    legend.position = "bottom",
    plot.title.position = "plot"
  )

# Scatter plot with regression line
pass_model <- lm(cpi_index ~ ppi_index, data = pass_df)
pass_coef <- coef(pass_model)[["ppi_index"]]
pass_r2 <- summary(pass_model)$r.squared

p2 <- ggplot(pass_df, aes(x = ppi_index, y = cpi_index)) +
  geom_point(alpha = 0.5, color = "#0072B2") +
  geom_smooth(method = "lm", se = TRUE, color = "#D55E00", linewidth = 1.2) +
  annotate("text", x = min(pass_df$ppi_index) + 5, y = max(pass_df$cpi_index) - 5,
           label = paste0("Pass-through rate: ", round(pass_coef, 3),
                         "\nR² = ", round(pass_r2, 3)),
           hjust = 0, size = 4, fontface = "bold") +
  labs(
    title = "Pass-Through Regression",
    subtitle = "1 unit increase in PPI → ? unit increase in CPI",
    x = "Producer Price Index",
    y = "Consumer Price Index"
  ) +
  theme_antitrust() +
  theme(plot.title.position = "plot")

# Combined plot
p1 / p2 + plot_annotation(
  caption = "Data: FRED series PCU324110324110 (PPI: Petroleum Refining) and CUSR0000SETB01 (CPI: Gasoline)"
)

# Summary statistics
pass_summary <- tibble::tibble(
  metric = c("Pass-through coefficient", "R-squared", "Observations", "Interpretation"),
  value = c(
    round(pass_coef, 3),
    round(pass_r2, 3),
    nrow(pass_df),
    ifelse(pass_coef < 0.5, "Incomplete pass-through",
           ifelse(pass_coef < 1.0, "Substantial pass-through",
                  "Over-shifting (pass-through > 100%)"))
  )
)

cat("\nPass-through analysis summary:\n")
knitr::kable(pass_summary, digits=3, caption="Pass-Through Analysis Results")
```

**Interpretation:**
- **Pass-through coefficient**: Measures how much a 1% increase in producer prices flows through to consumer prices. Values < 1 indicate incomplete pass-through (firms absorb some cost increases); values > 1 indicate over-shifting (firms amplify cost increases, possibly due to market power).
- **R-squared**: Indicates how well producer prices explain consumer price variation. High R² suggests tight cost-price linkage.
- **Incomplete pass-through**: Common in competitive markets where firms absorb cost shocks to retain customers. Can also occur with sticky prices or menu costs.
- **Over-shifting**: May signal market power (firms use cost increases as "focal points" to raise prices beyond the cost change) or complementarities/network effects.

{% hint style="success" %}
**Applications in antitrust:**

- **Cartel damages**: If pass-through is 80%, a $10 upstream overcharge causes an $8 downstream price increase.
- **Merger efficiencies**: If parties claim $5M in cost savings but pass-through is only 30%, consumers benefit by only $1.5M.
- **Vertical mergers**: Estimate pass-through separately for upstream and downstream stages to predict EDM (Elimination of Double Marginalization) benefits.
{% endhint %}

Swap series IDs for your industry (e.g., `WPUSI012011` for steel PPI, `CPIAUCSL` for overall CPI) or use firm-specific cost and price data when available.

## Bargaining sketches
When platforms or healthcare networks negotiate contracts, full structural models may be infeasible. Use Nash-in-Nash approximations or reduced-form proxies:

- **Regression-based bargaining shares.** Estimate how much of a wholesale cost shock flows into downstream prices for different bargaining parties (e.g., pharmacy benefit managers vs. hospitals).  
- **Qualitative overlays.** Pair negotiation timelines, renewal clauses, and concession histories with the empirical results.

## Looking ahead
Store demand estimates, diversion matrices, and pass-through/bargaining diagnostics in `data/derived` with READMEs so the mergers and monopolization chapters can reuse them in simulations. **Chapter 5** (Cartels) will use the pass-through analysis introduced here to trace overcharge harm along the supply chain, while **Chapter 6** (Mergers) deploys the UPP/GUPPI and logit simulation frameworks for prospective merger assessment. Note which datasets or code paths (e.g., `io-logit`, `upp-gup` templates) should be generalized in the Empirical Appendix (Chapter 13), and update the visualization tracker when adding new figures.
