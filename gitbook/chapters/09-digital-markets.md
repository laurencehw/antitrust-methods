# Digital Markets and Platforms

The tools and frameworks from the preceding chapters---market definition, IO modeling, merger analysis, and monopolization doctrine---apply to digital markets, but with distinctive challenges. Multi-sided platforms, network effects, zero-price business models, and rapid technological change all complicate traditional antitrust analysis. This chapter shows how to adapt the general toolkit to these specific features.

We also introduce new evidence types that matter especially in digital markets: telemetry data, clickstream analysis, API documentation, and product requirements documents. The intersection of technical product knowledge and economic reasoning defines much of the frontier in digital platform enforcement, from the US cases against Google and Meta to the EU's Digital Markets Act and South Africa's Online Intermediation Platforms Market Inquiry.

## Learning goals

Digital markets combine traditional IO concepts with product design, governance, and behavioral nudges. Drawing on DMA/Digital Markets Unit briefings and recent enforcement actions, this chapter helps you:

- Analyze multi-sided participation, indirect network effects, and multi-homing incentives.
- Quantify self-preferencing, ranking changes, and default effects on user/merchant behavior.
- Evaluate data advantages, access restrictions, and algorithmic pricing risks.
- Integrate product requirement documents (PRDs), API policies, and telemetry with econometric evidence for global enforcement settings.

Expect to combine telemetry, clickstream data, partner contracts, and qualitative product documentation with econometric tests and simulation scaffolds.

{% hint style="info" %}
**Key acronyms**

**OIPMI** = Online Intermediation Platforms Market Inquiry (South African Competition Commission, 2020–2023). A comprehensive investigation into digital platform competition covering marketplaces, app stores, food delivery, travel booking, and software platforms. Provides detailed transaction data, commission structures, and market share analyses referenced throughout this chapter.
{% endhint %}

## Core topics

**Multi-sided markets** connect different user groups (buyers/sellers, users/advertisers, drivers/riders) who value each other's participation:

- **Participation and multi-homing**: How do users on each side respond to fees, quality, and participation on other sides?
- **Network effects**: Do more users on one side attract more users on other sides? How strong is the feedback loop?
- **Switching costs and lock-in**: What prevents users from moving to rival platforms?

**Platform conduct concerns** include:

- **Self-preferencing**: Does the platform favor its own products in search rankings or recommendations?
- **Ranking manipulation**: Do algorithm changes benefit the platform at users' expense?
- **Default tying**: Are defaults structured to foreclose rivals?
- **Data leverage**: Does the platform use seller/developer data to compete against them?

**The platform case workflow** proceeds through five stages:

1. Define sides and metrics (MAU, GMV, multi-homing rates)
2. Map fees and monetization (commissions, ad loads, data collection)
3. Identify theory of harm (self-preferencing, foreclosure, data leverage)
4. Measure mechanisms (ranking impacts, default effects, fee pass-through)
5. Assess effects and design remedies (choice screens, access mandates, portability)

## Platform workflow overview

{% hint style="info" %}
**Platform Competition Analysis Workflow**

```
SCOPING                   ANALYSIS                  REMEDIES
   |                          |                         |
   v                          v                         v
+--------------+        +--------------+        +--------------+
| Define       |        | Quantify     |        | Design       |
| sides &      |------->| mechanisms:  |------->| remedies:    |
| metrics      |        | - Ranking    |        | - Choice     |
|              |        | - Defaults   |        |   screens    |
+--------------+        | - Fees       |        | - API access |
   |                    +--------------+        | - Fair       |
   v                          |                |   ranking    |
+--------------+              v                +--------------+
| Map          |        +--------------+
| monetization:|        | Test         |
| - Commissions|        | theories:    |
| - Ad loads   |        | - DiD/Event  |
| - Data       |        | - A/B logs   |
+--------------+        | - Telemetry  |
   |                    +--------------+
   v
+--------------+
| Identify     |
| theory of    |
| harm:        |
| - Self-pref  |
| - Foreclosure|
| - Data lever.|
+--------------+
```

**Data sources:** Platform telemetry | DMA compliance | OIPMI surveys | Partner contracts | API documentation
{% endhint %}

1. **Define sides and metrics.** Identify user, merchant, advertiser, developer, courier, or publisher sides. Track MAU/DAU, GMV, multi-homing rates, engagement depth, and conversion metrics.
2. **Map fees and monetization.** Build ladders for commissions, subscriptions, ad loads, and data monetization; compute pass-through and elasticity. For two-sided market theory, see (Rochet & Tirole, 2003) and (Armstrong, 2006).
3. **Theory of harm.** Common mechanisms include self-preferencing, default tying, MFN/parity clauses, data leveraging, interoperability restrictions, algorithmic ranking biases, and algorithmic collusion.
4. **Mechanism measurement.** Quantify ranking impacts, default effects, fee changes, and data advantages; document multi-homing constraints and API access terms.
5. **Effects & remedies.** Measure partner churn, user switching, price/fee changes, and innovation impacts. Propose remedies (choice screens, fair-ranking reports, API access rules, data portability, structural separation) tied to measured harms.

## Theory-to-metric mapping

The table below maps common platform theories of harm to measurable metrics and appropriate empirical tests. Use this as a checklist when scoping digital market investigations.

| Theory of Harm | Key Metric | Empirical Test | Data Sources |
|:---------------|:-----------|:---------------|:-------------|
| **Self-preferencing** | Downstream traffic share; CTR by listing type | DiD around algorithm changes; A/B test analysis | Platform telemetry, OIPMI audits, CMA studies |
| **Ranking manipulation** | Position-adjusted CTR; conversion by slot | Regression of outcomes on ranking position × first-party indicator | Clickstream logs, buy-box audits |
| **Default tying** | Rival market share pre/post choice screen | Event study around remedy implementation | DMA compliance reports, browser/search share data |
| **Foreclosure (input denial)** | API latency; error rates; access denial frequency | Regression of 3rd-party performance on access restrictions | API logs, developer complaints, uptime monitoring |
| **Foreclosure (raising rivals' costs)** | Fee differential; cost-to-serve by channel | Comparison of platform vs. direct channel costs | Fee schedules, merchant P&L data |
| **Data leverage** | Copycat product launch timing; feature matching | Survival analysis of 3rd-party products post-data access | Product launch dates, feature audits, internal documents |
| **MFN/parity clauses** | Price dispersion across platforms | Variance analysis; price comparison pre/post MFN removal | Price scraping, platform listings, DMA studies |
| **Algorithmic collusion** | Price correlation; response times; convergence patterns | Granger causality; structural break tests; simulation | Transaction-level pricing data, algorithm audits |
| **Switching costs/lock-in** | Multi-homing rates; churn by tenure | Duration models; switching cost estimation | Survey data, telemetry, DMA surveys |
| **Network effects exploitation** | Participation elasticity; tipping point dynamics | Two-sided demand estimation; natural experiments | Platform growth data, entry/exit events |

**How to use this table:**

1. **Scoping phase:** Identify which theories of harm are plausible given the market context and available complaints.
2. **Data requests:** Use the "Data Sources" column to structure information requests to platforms and third parties.
3. **Analysis design:** Match empirical tests to available data; prioritize tests with strongest identification.
4. **Triangulation:** Combine quantitative evidence with qualitative sources (internal documents, partner interviews, PRDs).

{% hint style="info" %}
**Adapting to zero-price markets**

When users pay with attention rather than money, adapt metrics accordingly:

- Replace `fees_users` with **ad load** (ads per session, ad-to-content ratio)
- Use **time spent** or **engagement depth** as the "price" users pay
- Apply SSNDQ framework: would a hypothetical monopolist profitably degrade **quality** by 5-10%?
- Track quality metrics: load times, relevance scores, content diversity, privacy erosion
{% endhint %}

## Participation, multi-homing, and network effects

- **Participation curves:** Model each side's activity as a function of fees, quality, and participation on the other side. Use logit, linear, or Poisson models with cross-side terms (Evans & Schmalensee, 2007); (Hagiu & Wright, 2015).  
- **Multi-homing rates:** Estimate the share of users or merchants active on rival platforms. OIPMI surveys and EU DMA filings include methodologies you can reuse (Parker & Van Alstyne, 2005).  
- **Match quality:** Track conversion rates, completion times, or satisfaction metrics per platform side to show how conduct affects outcomes.  
- **Elasticities:** Two-sided elasticities inform fee caps and remedy design (e.g., how merchant participation responds to lower commissions or improved ranking fairness).

### Two-sided demand scaffold
```r
library(dplyr)
library(fixest)
source("program/R/helpers.R")

# Synthetic example; replace with platform telemetry
set.seed(42)
panel <- expand.grid(platform = c("Alpha","Beta"), period = 2018:2023) |>
  mutate(
    fees_users = runif(n(), 0, 4),
    fees_merchants = runif(n(), 15, 30),
    quality = runif(n(), 0.5, 1),
    users = exp(5 - 0.25 * fees_users + 0.4 * quality + rnorm(n(), 0, 0.2)),
    merchants = exp(4 - 0.12 * fees_merchants + 0.3 * users / 1e5 + rnorm(n(), 0, 0.2))
  )

user_model <- feols(log(users) ~ fees_users + quality + log(merchants) | platform + period, data = panel)
merchant_model <- feols(log(merchants) ~ fees_merchants + log(users) | platform + period, data = panel)
summary(user_model)
summary(merchant_model)
```
Replace the synthetic `panel` with sanitized telemetry (monthly active users/merchants) or aggregated OIPMI data stored in `data/examples/digital-two-sided.csv`. Document the estimated cross-side elasticities in your memo.

### Zero-price demand model (attention markets)

Many platforms charge users nothing in money terms---instead, users pay with attention (watching ads) and data (surrendering personal information). Standard price-based demand models do not directly apply. The fix is to replace monetary fees with **attention costs**: ad load, time spent, or quality degradation, then estimate how sensitive users are to non-price dimensions of competition. This maps onto the SSNDQ (Small but Significant Non-transitory Decrease in Quality) framework competition authorities use for zero-price markets.

The model below estimates how user engagement (daily active users) responds to attention costs (ad load, data collection) and quality metrics (load time, content relevance), then simulates whether a hypothetical monopolist could profitably degrade quality.

```r
library(dplyr)
library(fixest)
source("program/R/helpers.R")

# Zero-price platform: users "pay" with attention (ad exposure)
# Synthetic example; replace with platform telemetry
set.seed(789)
attention_panel <- expand.grid(
  platform = c("Alpha", "Beta"),
  period = 2018:2023
) |>
  mutate(
    # Attention costs (ads per session, data collection intensity)
    ad_load = runif(n(), 3, 12),        # Ads per session
    data_collection = runif(n(), 0, 1), # Privacy cost index (0-1)

    # Quality metrics
    load_time_ms = runif(n(), 500, 3000),   # Page load time
    relevance_score = runif(n(), 0.5, 0.95), # Content relevance

    # User engagement (dependent variable)
    # Users respond negatively to ads/data collection, positively to quality
    daily_active_users = exp(
      12 - 0.08 * ad_load - 0.5 * data_collection -
      0.0003 * load_time_ms + 2 * relevance_score +
      rnorm(n(), 0, 0.15)
    ),

    # Advertiser side responds to user base
    advertiser_spend = exp(
      8 + 0.6 * log(daily_active_users) + 0.1 * ad_load +
      rnorm(n(), 0, 0.1)
    )
  )

# User-side model: attention cost elasticity
user_model <- feols(
  log(daily_active_users) ~ ad_load + data_collection +
    load_time_ms + relevance_score | platform + period,
  data = attention_panel
)

# Advertiser-side model: cross-side effects
advertiser_model <- feols(
  log(advertiser_spend) ~ log(daily_active_users) + ad_load | platform + period,
  data = attention_panel
)

cat("=== ZERO-PRICE DEMAND MODEL ===\n\n")
cat("User-side (attention cost) elasticities:\n")
cat(paste0("  Ad load effect: ", round(coef(user_model)["ad_load"], 4),
           " (1 more ad/session → ",
           round(coef(user_model)["ad_load"] * 100, 1), "% DAU change)\n"))
cat(paste0("  Data collection effect: ", round(coef(user_model)["data_collection"], 4),
           " (privacy cost)\n"))
cat(paste0("  Load time effect: ", round(coef(user_model)["load_time_ms"], 6),
           " (per ms)\n"))
cat(paste0("  Relevance effect: ", round(coef(user_model)["relevance_score"], 4),
           " (quality boost)\n\n"))

cat("Advertiser-side elasticities:\n")
cat(paste0("  User base elasticity: ", round(coef(advertiser_model)["log(daily_active_users)"], 3),
           " (cross-side network effect)\n"))
cat(paste0("  Ad inventory value: ", round(coef(advertiser_model)["ad_load"], 4),
           " (more slots → more spend)\n"))

# SSNDQ analysis: what if quality degrades 5-10%?
cat("\n=== SSNDQ SIMULATION ===\n")
baseline_dau <- mean(attention_panel$daily_active_users)
# 10% quality degradation = 10% more ads + 10% worse relevance
degraded_dau <- baseline_dau * exp(
  coef(user_model)["ad_load"] * 0.8 +      # 10% more ads (e.g., 8 → 8.8)
  coef(user_model)["relevance_score"] * -0.08  # 10% worse relevance
)
dau_loss <- (baseline_dau - degraded_dau) / baseline_dau

cat(paste0("Baseline DAU: ", format(round(baseline_dau), big.mark = ","), "\n"))
cat(paste0("After 10% quality degradation: ", format(round(degraded_dau), big.mark = ","), "\n"))
cat(paste0("Predicted user loss: ", scales::percent(dau_loss, accuracy = 0.1), "\n"))
cat(paste0("Would monopolist profit? Depends on ad revenue vs. user loss tradeoff.\n"))
```

**Key adaptations for zero-price markets:**

| Traditional Market | Zero-Price Market | Measurement |
|:-------------------|:------------------|:------------|
| Price | Ad load (ads/session) | Platform telemetry |
| Price | Time cost (session duration) | Engagement metrics |
| Price | Privacy cost (data collection) | Privacy policy scoring |
| Quality | Relevance, load time, UX | A/B tests, user surveys |
| Quantity | DAU, MAU, sessions | Platform analytics |

**SSNDQ framework application:**

1. Define quality metrics relevant to users (speed, relevance, privacy, content diversity)
2. Estimate user sensitivity to each quality dimension
3. Simulate: would a hypothetical monopolist profitably degrade quality by 5-10%?
4. If users wouldn't switch despite degradation → market power concern

## Ranking, self-preferencing, and defaults

### Ranking impact visualization
```r
library(dplyr)
library(tidyr)
library(ggplot2)
source("program/R/helpers.R")

ranking <- tibble::tribble(
  ~slot, ~first_party_ctr, ~third_party_ctr,
  1, 0.16, 0.08,
  2, 0.13, 0.06,
  3, 0.11, 0.05,
  4, 0.08, 0.04,
  5, 0.06, 0.03
) |>
  pivot_longer(-slot, names_to = "listing", values_to = "ctr")

ggplot(ranking, aes(slot, ctr, color = listing)) +
  geom_line(linewidth = 1) +
  geom_point(size = 2) +
  scale_color_manual(values = c("#1b9e77", "#d95f02"), labels = c("First-party", "Third-party")) +
  labs(
    title = "Conversion by ranking slot",
    subtitle = "Illustrative data; use OIPMI or platform A/B metrics when available",
    x = "Slot (1 = top)",
    y = "Conversion rate",
    color = NULL
  ) +
  theme_antitrust() +
  theme(legend.position = "bottom")
```
Populate the tibble with actual ranking data (e.g., OIPMI buy-box audits, CMA Amazon Marketplace analysis) or maintain sanitized values in `data/examples/digital-ranking.csv`. The CMA's market studies are publicly available at [gov.uk/cma](https://www.gov.uk/government/organisations/competition-and-markets-authority).

### Default-choice event study scaffold
```r
library(fixest)

# df requires: device_id, week, default_event (event date), share_rival
# event_model <- feols(share_rival ~ i(week, default_event, ref = -1) | device_id + week, data = df)
# etable(event_model)
```
Use telemetry from choice screens (EU Android choice screen, DMA compliance reports) or partner-provided logs. If live data are unavailable, build synthetic event panels mirroring DMA summary stats (store in `data/examples/digital-default.csv`).

## Methodologies

{% hint style="info" %}
**Method box**

- Platform fee/price pass-through across sides.  
- Event studies on ranking/default changes; DMA/DMA-style interventions.  
- Two-sided logit or bargaining sketches to test fee caps and interoperability remedies.
{% endhint %}

{% hint style="info" %}
**Qualitative evidence**

- Product requirement documents, experiment summaries, and governance memos.  
- Partner contracts (parity/MFN, exclusivity), API access terms, data-sharing policies.  
- User research/surveys capturing multi-homing, switching costs, and friction sources.
{% endhint %}

{% hint style="info" %}
**Citations and comparative note**

- US cases (Epic v. Apple, DOJ Google Search and Ad Tech, FTC Amazon Marketplace), EU/DMA (Google Shopping/Android, DMA obligations), UK (CMA digital market studies), KFTC/JFTC app store cases, SAMR digital enforcement.  
- Empirical studies on defaults, ranking effects, and multi-homing (e.g., Luca et al., 2016, "Does Google Content Degrade Google Search?," Harvard Business School Working Paper; Edelman & Lai, 2016, "Design of Search Engine Services," *Journal of Economics & Management Strategy* 25(1): 187-218).  
- Flag differences in parity/MFN treatment and remedy preferences (EU fair-ranking obligations vs. US injunctive relief).
{% endhint %}

## Visualizations and data sourcing
- **Default impact chart:** Source DMA compliance reports (available at [ec.europa.eu/dma](https://ec.europa.eu/)), CMA choice-screen experiments, or sanitized telemetry. If unavailable, simulate from DMA summary stats.
- **Multi-homing Sankey:** Use OIPMI survey microdata or replicate with local surveys; store in `data/examples/digital-sankey.csv` until live data arrive.
- **Ranking change event analysis:** Combine OIPMI buy-box audits or platform-provided logs with the ranking scaffold above.
- **Fee ladder diagrams:** Pull commission schedules from OIPMI appendices or global public filings (App Store, Play Store, Amazon Marketplace).

Document each dataset in `data/README.md` with provenance, confidentiality notes, and instructions for swapping synthetic vs. production data. When we "fill with real data," replace the synthetic CSVs, re-render figures, and cache sanitized outputs for publication builds.

### Southern African digital enforcement snapshots
- **Online Intermediation Platforms Market Inquiry (OIPMI, 2020–2023).** The Competition Commission collected transaction-level data from e-commerce marketplaces, app stores, food delivery apps, and travel platforms. Findings highlighted Google Search’s >90% share of general search queries, food-delivery commissions clustering at 25–30%, and marketplace buy-box algorithms that favored first-party listings (e.g., Takealot Retail) over third-party sellers with identical fulfillment metrics. Final remedies require fair-ranking reports, caps on marketplace storage/fulfillment fees for SMEs, and anti-steering relief that lets restaurants promote direct-order channels inside aggregator apps.
- **Advertising and digital news media (Media and Digital Platforms Market Inquiry, 2023–ongoing).** Building on OIPMI data, the Commission is ingesting impression-level logs from Meta, Google, and local publishers to quantify revenue imbalances in display advertising. The interim statement reports that Google commands roughly 65% of display ad spend routed through programmatic channels, while local publishers face average take-rates below 30% after demand-side/platform fees—data points that frame prospective bargaining remedies for news publishers across Southern Africa.
- **GovChat/Meta interim relief (Competition Commission v. Meta Platforms, 2021).** The Commission used WhatsApp Business API telemetry to demonstrate GovChat’s role in reaching 8+ million South African users for public-service messaging, and it showed how Meta’s proposed off-boarding would foreclose a civic-use case despite negligible incremental infrastructure cost. Interim relief preserved access while the Tribunal weighed the exclusion case, offering a blueprint for combining platform-side telemetry with public-interest arguments in developing markets.

{% hint style="info" %}
**Method box**

- Platform price/fee pass-through; elasticity across sides.
- Event studies on default changes or ranking tweaks.
- Simple two-sided logit/bargaining sketches; diversion across sides.
{% endhint %}

{% hint style="info" %}
**Qualitative evidence**

- Product requirement docs and experiments; governance and content policies.
- Partner contracts (parity/MFN, exclusivity), API access terms.
- User research surveys on multi-homing and switching.
{% endhint %}

{% hint style="info" %}
**Citations and comparative note**

- Cite platform cases and regulations: US (e.g., Epic v. Apple, DOJ Google Search/Ad Tech), EU (Google Shopping/Android, [DMA](https://ec.europa.eu/info/strategy/priorities-2019-2024/europe-fit-digital-age/digital-markets-act-ensuring-fair-and-open-digital-markets_en)), UK ([CMA market investigations](https://www.gov.uk/cma-cases)), and other jurisdictions (e.g., Korea KFTC app stores where relevant).
- Reference empirical studies on defaults and ranking effects, and any A/B or natural experiment evidence from platforms.
- Note differences in treatment of MFNs/parity and self-preferencing across jurisdictions.
{% endhint %}

## Enhanced Visualizations

### Multi-homing patterns
Multi-homing patterns reveal competitive constraints and switching costs. The distribution of users across platform combinations indicates whether platforms compete head-to-head or serve distinct niches.

```r
library(dplyr)
library(ggplot2)
library(ggalluvial)
source("program/R/helpers.R")

# Simulated multi-homing survey data
# Replace with OIPMI survey data or DMA compliance reports
set.seed(234)
n_users <- 1000

multihoming <- tibble(
  user_id = 1:n_users,
  platform_a = sample(c("Active", "Inactive"), n_users, replace = TRUE,
                     prob = c(0.7, 0.3)),
  platform_b = sample(c("Active", "Inactive"), n_users, replace = TRUE,
                     prob = c(0.5, 0.5)),
  platform_c = sample(c("Active", "Inactive"), n_users, replace = TRUE,
                     prob = c(0.3, 0.7))
) |>
  mutate(
    pattern = case_when(
      platform_a == "Active" & platform_b == "Active" & platform_c == "Active" ~ "All three",
      platform_a == "Active" & platform_b == "Active" ~ "A + B",
      platform_a == "Active" & platform_c == "Active" ~ "A + C",
      platform_b == "Active" & platform_c == "Active" ~ "B + C",
      platform_a == "Active" ~ "A only",
      platform_b == "Active" ~ "B only",
      platform_c == "Active" ~ "C only",
      TRUE ~ "None"
    )
  )

# Aggregate flows
flows <- multihoming |>
  count(pattern) |>
  mutate(
    pct = n / sum(n),
    pattern = factor(pattern,
                    levels = c("A only", "B only", "C only",
                              "A + B", "A + C", "B + C", "All three", "None"))
  ) |>
  arrange(pattern)

# Bar chart showing multi-homing patterns
p1 <- ggplot(flows, aes(x = pattern, y = pct, fill = pattern)) +
  geom_col(width = 0.7) +
  geom_text(aes(label = scales::percent(pct, accuracy = 0.1)),
            vjust = -0.5, size = 3.5) +
  scale_y_continuous(labels = scales::percent_format(),
                     expand = expansion(mult = c(0, 0.1))) +
  scale_fill_brewer(palette = "Set2") +
  labs(
    title = "Multi-homing Patterns Across Platforms",
    subtitle = "User activity across Platform A, B, and C",
    x = NULL,
    y = "Share of Users",
    caption = "Illustrative data. Replace with OIPMI survey or DMA compliance reports."
  ) +
  theme_antitrust() +
  theme(
    axis.text.x = element_text(angle = 45, hjust = 1),
    legend.position = "none",
    plot.title.position = "plot"
  )

p1

# Summary statistics
cat("\nMulti-homing summary:\n")
cat(paste0("Single-homing (one platform only): ",
          scales::percent(sum(flows$pct[flows$pattern %in%
                              c("A only", "B only", "C only")]),
                         accuracy = 0.1), "\n"))
cat(paste0("Multi-homing (2+ platforms): ",
          scales::percent(sum(flows$pct[grepl("\\+|three", flows$pattern)]),
                         accuracy = 0.1), "\n"))
```

**Interpretation:**
-   **High single-homing**: Suggests strong lock-in, switching costs, or network effects. Platforms may have market power.
-   **High multi-homing**: Indicates competitive pressure; users actively compare options. But check if multi-homing is symmetric or if one platform dominates usage.
-   **Asymmetric patterns**: If Platform A appears in most combinations, it may be a "must-have" platform with gatekeeping power.

**Data sources:**
-   OIPMI survey microdata (South Africa)
-   DMA compliance reports (EU)
-   CMA market studies (UK)
-   Platform-provided telemetry (subject to confidentiality)

### Choice screen / default effect visualization
Quantify how defaults affect market shares using difference-in-differences or event studies around choice screen implementations.

```r
library(fixest)
library(dplyr)
library(ggplot2)
library(patchwork)
source("program/R/helpers.R")

# Simulated data: Android choice screen impact (EU DMA context)
# Replace with actual DMA compliance data or CMA experiments
set.seed(345)
weeks <- -24:24
countries <- c("Control (no choice screen)", "Treatment (choice screen)")

default_data <- expand.grid(
  week = weeks,
  country = countries
) |>
  mutate(
    # Pre-intervention: both countries similar
    # Post-intervention: treatment shows rival gain
    rival_share = case_when(
      country == "Control (no choice screen)" ~ 0.05 + 0.0005 * week + rnorm(n(), 0, 0.01),
      week < 0 ~ 0.05 + 0.0005 * week + rnorm(n(), 0, 0.01),
      TRUE ~ 0.05 + 0.0005 * week + 0.08 + rnorm(n(), 0, 0.01)
    ),
    rival_share = pmax(0.01, pmin(0.25, rival_share))
  )

# Time series plot
p1 <- ggplot(default_data, aes(x = week, y = rival_share,
                                color = country, linetype = country)) +
  geom_vline(xintercept = 0, linetype = "dashed", color = "gray40",
             linewidth = 1) +
  stat_summary(fun = mean, geom = "line", linewidth = 1.2) +
  annotate("text", x = 0, y = 0.22, label = "Choice screen\nintroduced",
           hjust = -0.1, size = 3.5, fontface = "italic") +
  scale_color_manual(values = c("Control (no choice screen)" = "#999999",
                                 "Treatment (choice screen)" = "#0072B2")) +
  scale_linetype_manual(values = c("Control (no choice screen)" = "dashed",
                                   "Treatment (choice screen)" = "solid")) +
  scale_y_continuous(labels = scales::percent_format()) +
  labs(
    title = "Impact of Choice Screen on Rival Search Engine Share",
    subtitle = "Difference-in-Differences: Treatment vs. Control Countries",
    x = "Weeks relative to choice screen introduction",
    y = "Rival search engine share",
    color = NULL,
    linetype = NULL
  ) +
  theme_antitrust() +
  theme(
    legend.position = "bottom",
    plot.title.position = "plot"
  )

# Coefficient plot (event study coefficients)
# Simulated DiD estimates
did_coefs <- tibble(
  week = weeks[weeks != -1]  # reference period
) |>
  mutate(
    estimate = 0.08 * as.numeric(week >= 0) + rnorm(n(), 0, 0.01),
    ci_lower = estimate - 1.96 * 0.01,
    ci_upper = estimate + 1.96 * 0.01
  )

p2 <- ggplot(did_coefs, aes(x = week, y = estimate)) +
  geom_hline(yintercept = 0, linetype = "solid", color = "gray40") +
  geom_vline(xintercept = 0, linetype = "dashed", color = "gray40",
             linewidth = 1) +
  geom_ribbon(aes(ymin = ci_lower, ymax = ci_upper),
              alpha = 0.2, fill = "#0072B2") +
  geom_line(color = "#0072B2", linewidth = 1) +
  geom_point(color = "#0072B2", size = 2) +
  scale_y_continuous(labels = scales::percent_format()) +
  labs(
    title = "Event Study Coefficients",
    subtitle = "Treatment effect by week (relative to week -1)",
    x = "Weeks relative to choice screen",
    y = "Effect on rival share (percentage points)",
    caption = "Illustrative data. Replace with DMA compliance reports or CMA experiments."
  ) +
  theme_antitrust() +
  theme(plot.title.position = "plot")

# Combined plot
p1 / p2

# Summary statistics
pre_treatment <- mean(default_data$rival_share[
  default_data$country == "Treatment (choice screen)" & default_data$week < 0])
post_treatment <- mean(default_data$rival_share[
  default_data$country == "Treatment (choice screen)" & default_data$week >= 0])
effect <- post_treatment - pre_treatment

cat("\nChoice screen impact summary:\n")
tibble::tibble(
  metric = c("Pre-treatment share", "Post-treatment share", "Treatment Effect"),
  value = c(pre_treatment, post_treatment, effect)
) |>
  knitr::kable(digits = 3, caption = "Impact of Choice Screen")
```

**How to use this analysis:**
- **Pre-trends**: Check parallel trends before intervention to validate DiD assumptions.
- **Treatment effect**: Quantify how much rival share increased after choice screen.
- **Heterogeneity**: Analyze by device type, user demographics, or country.
- **Persistence**: Track whether effects sustain over time or decay.

**DMA context:**
The EU Digital Markets Act requires designated gatekeepers to offer choice screens for browsers, search engines, and other services. This analysis framework can evaluate compliance and effectiveness.

### Platform fee structure visualization
Commission and fee structures are critical evidence in platform cases. Show how fees vary by seller tier, product category, or fulfillment method.

```r
library(dplyr)
library(ggplot2)
library(tidyr)
source("program/R/helpers.R")

# Fee structures from major platforms (public sources)
# App Store, Play Store, Amazon Marketplace, food delivery
fees <- tibble::tribble(
  ~platform,            ~category,          ~base_commission, ~fulfillment_fee, ~payment_fee,
  "App Store",          "Apps",             0.30,             0.00,              0.00,
  "App Store",          "Apps (< $1M)",     0.15,             0.00,              0.00,
  "Play Store",         "Apps",             0.30,             0.00,              0.00,
  "Play Store",         "Apps (< $1M)",     0.15,             0.00,              0.00,
  "Amazon Marketplace", "FBM (self-fulfill)", 0.15,          0.00,              0.03,
  "Amazon Marketplace", "FBA (Amazon fulfill)", 0.15,        0.20,              0.03,
  "Food Delivery A",    "Restaurant",       0.28,             0.00,              0.02,
  "Food Delivery B",    "Restaurant",       0.32,             0.00,              0.02
) |>
  mutate(
    total_fee = base_commission + fulfillment_fee + payment_fee,
    total_fee_pct = scales::percent(total_fee, accuracy = 0.1)
  )

# Stacked bar chart
fees_long <- fees |>
  pivot_longer(cols = c(base_commission, fulfillment_fee, payment_fee),
               names_to = "fee_type", values_to = "rate") |>
  mutate(
    fee_type = factor(fee_type,
                     levels = c("payment_fee", "fulfillment_fee", "base_commission"),
                     labels = c("Payment Processing", "Fulfillment", "Base Commission"))
  )

ggplot(fees_long, aes(x = paste(platform, category, sep = "\n"),
                      y = rate, fill = fee_type)) +
  geom_col(width = 0.7) +
  geom_text(data = fees,
            aes(x = paste(platform, category, sep = "\n"),
                y = total_fee, label = total_fee_pct, fill = NULL),
            vjust = -0.5, size = 3.5, fontface = "bold") +
  scale_y_continuous(labels = scales::percent_format(),
                     expand = expansion(mult = c(0, 0.1))) +
  scale_fill_manual(
    values = c("Base Commission" = "#D55E00",
               "Fulfillment" = "#0072B2",
               "Payment Processing" = "#009E73")
  ) +
  labs(
    title = "Platform Fee Structures by Category",
    subtitle = "Total take rate shown at top of each bar",
    x = NULL,
    y = "Fee Rate",
    fill = "Fee Component",
    caption = "Data from public platform documentation (2024). FBM = Fulfilled by Merchant; FBA = Fulfilled by Amazon."
  ) +
  theme_antitrust() +
  theme(
    axis.text.x = element_text(angle = 45, hjust = 1, size = 9),
    legend.position = "bottom",
    plot.title.position = "plot"
  )

# Summary table
cat("\nFee structure summary:\n")
fees |>
  select(platform, category, total_fee) |>
  mutate(total_fee = scales::percent(total_fee, accuracy = 0.1)) |>
  print(n = Inf)
```

**Key insights:**
- **App stores**: 30% standard (15% for small developers under $1M revenue).
- **E-commerce marketplaces**: 15-18% base + 15-25% fulfillment (if using platform logistics).
- **Food delivery**: 28-32% commission + 2-3% payment processing.
- **Bundling**: Platforms often bundle services (payment, fulfillment, advertising) making switching costly.

**Competitive assessment:**
- Compare fees across platforms to evaluate competitive pressure.
- Assess whether high fees reflect service value or market power.
- Evaluate whether fee structures create barriers to multi-homing.

### Market share evolution for digital platforms
Track platform market share over time to identify tipping points and competitive dynamics.

```r
library(dplyr)
library(ggplot2)
library(lubridate)
source("program/R/helpers.R")

# Market share evolution from public sources and regulatory filings
# Illustrative data for search engines, social media, or e-commerce
market_evolution <- tibble::tribble(
  ~date,         ~platform,      ~share,
  "2015-01-01",  "Platform A",   0.88,
  "2016-01-01",  "Platform A",   0.90,
  "2017-01-01",  "Platform A",   0.91,
  "2018-01-01",  "Platform A",   0.92,
  "2019-01-01",  "Platform A",   0.91,
  "2020-01-01",  "Platform A",   0.90,
  "2021-01-01",  "Platform A",   0.89,
  "2022-01-01",  "Platform A",   0.88,
  "2023-01-01",  "Platform A",   0.87,
  "2015-01-01",  "Platform B",   0.08,
  "2016-01-01",  "Platform B",   0.07,
  "2017-01-01",  "Platform B",   0.06,
  "2018-01-01",  "Platform B",   0.05,
  "2019-01-01",  "Platform B",   0.06,
  "2020-01-01",  "Platform B",   0.07,
  "2021-01-01",  "Platform B",   0.08,
  "2022-01-01",  "Platform B",   0.09,
  "2023-01-01",  "Platform B",   0.10,
  "2015-01-01",  "Others",       0.04,
  "2016-01-01",  "Others",       0.03,
  "2017-01-01",  "Others",       0.03,
  "2018-01-01",  "Others",       0.03,
  "2019-01-01",  "Others",       0.03,
  "2020-01-01",  "Others",       0.03,
  "2021-01-01",  "Others",       0.03,
  "2022-01-01",  "Others",       0.03,
  "2023-01-01",  "Others",       0.03
) |>
  mutate(date = as.Date(date))

# Area chart
ggplot(market_evolution, aes(x = date, y = share, fill = platform)) +
  geom_area(alpha = 0.8) +
  scale_y_continuous(labels = scales::percent_format()) +
  scale_x_date(date_breaks = "1 year", date_labels = "%Y") +
  scale_fill_manual(
    values = c("Platform A" = "#0072B2",
               "Platform B" = "#009E73",
               "Others" = "#999999")
  ) +
  labs(
    title = "Digital Platform Market Share Evolution",
    subtitle = "Example: Search engine market shares 2015-2023",
    x = NULL,
    y = "Market Share",
    fill = "Platform",
    caption = "Illustrative data. Replace with StatCounter, SimilarWeb, or regulatory filings."
  ) +
  theme_antitrust() +
  theme(
    legend.position = "bottom",
    plot.title.position = "plot"
  )

# Summary statistics
cat("\nMarket concentration trends:\n")
cat(paste0("2015 HHI: ", round(sum((market_evolution$share[
  market_evolution$date == "2015-01-01"] * 100)^2), 0), "\n"))
cat(paste0("2023 HHI: ", round(sum((market_evolution$share[
  market_evolution$date == "2023-01-01"] * 100)^2), 0), "\n"))
cat(paste0("\nPlatform A share trend: ",
          scales::percent(market_evolution$share[
            market_evolution$date == "2015-01-01" &
            market_evolution$platform == "Platform A"], accuracy = 0.1),
          " (2015) → ",
          scales::percent(market_evolution$share[
            market_evolution$date == "2023-01-01" &
            market_evolution$platform == "Platform A"], accuracy = 0.1),
          " (2023)\n"))
```

**Data sources:**
- **StatCounter**: Global browser, OS, search engine stats
- **SimilarWeb**: Website and app traffic data
- **Sensor Tower / App Annie**: Mobile app market intelligence
- **Regulatory filings**: EC, CMA, FTC, DMA compliance reports
- **OIPMI**: South African platform market shares

**Use cases:**
- Demonstrate sustained dominance or competitive entry
- Identify tipping points or competitive interventions
- Support market definition and dominance assessments

---

## Generative AI and foundation models

{% hint style="warning" %}
**Rapidly evolving area.** AI market competition is subject to fast-moving developments in both technology and regulation. The frameworks below provide a starting point, but practitioners should monitor agency guidance closely for updates.
{% endhint %}

The platform competition framework developed above---multi-sided markets, network effects, data as a competitive moat---applies to AI markets, but foundation models raise distinct concerns: compute concentration, partnership structures that may confer control without acquisition, and rapidly evolving capabilities that resist static market share analysis. Enforcement agencies in multiple jurisdictions began examining these issues in 2024--2025.

### Market structure concerns

**Vertical integration and compute access:** A small number of cloud providers (AWS, Azure, Google Cloud) control the compute infrastructure essential for training frontier models. Vertical integration between cloud providers and AI model developers (Microsoft/OpenAI, Google/DeepMind, Amazon/Anthropic) creates potential foreclosure concerns similar to traditional media/distribution cases.

**Data moats:** Training data advantages may create barriers to entry that are difficult to replicate. Key questions include:
- Whether data access is essential for competitive AI development
- Whether exclusive data arrangements foreclose rivals
- The role of synthetic data in reducing data barriers

**Partnerships vs. acquisitions:** The Microsoft/OpenAI and Amazon/Anthropic partnership structures may achieve control similar to acquisitions without triggering merger notification. Agencies are scrutinizing whether these arrangements confer de facto control.

### Theory of harm framework

| Concern | Mechanism | Measurement approach |
|:--------|:----------|:--------------------|
| **Compute foreclosure** | Integrated cloud provider degrades rivals' access | API latency/uptime for affiliated vs. unaffiliated models |
| **Training data exclusivity** | Exclusive licensing of high-quality datasets | Document analysis; entry barrier assessment |
| **API pricing squeeze** | Below-cost API pricing to foreclose rivals | Margin analysis; comparison to standalone costs |
| **Distribution bundling** | Tying AI features to dominant platforms | Default/pre-installation analysis (cf. browser cases) |
| **Talent concentration** | Acqui-hires and non-competes limiting rival innovation | Labor market analysis (see Chapter 10) |

### Emerging regulatory frameworks

- **EU AI Act (2024):** Establishes tiered obligations based on risk level; interacts with DMA gatekeeper obligations for AI-integrated platforms.
- **US Executive Order on AI (2023):** Directs agencies to monitor competitive dynamics; potential FTC Section 5 authority for unfair methods.
- **CMA AI Foundation Models review (2023-ongoing):** Examines compute concentration, partnerships, and potential competition concerns.

### Practical implications

When analyzing AI market competition:

1. **Define the relevant market carefully:** Is it foundation models, fine-tuned applications, API access, or end-user AI features? Market boundaries are fluid and contested.
2. **Assess partnership structures:** Evaluate whether minority investments, commercial agreements, and board seats confer control absent formal acquisition.
3. **Consider dynamic competition:** AI capabilities evolve rapidly; static market shares may understate competitive dynamics or overstate durability of positions.
4. **Examine data and compute access:** These inputs may function as essential facilities; apply raising rivals' costs and foreclosure frameworks.

For the latest agency guidance, monitor CMA's AI Foundation Models work and FTC/DOJ statements on AI competition.

## Looking ahead

Store digital platform analyses in `data/derived/digital/` with clear provenance notes (data source, extraction date, confidentiality status). When DMA compliance data become available, replace synthetic choice-screen impacts with actual telemetry; document API access restrictions and data-sharing agreements in `data/README.md`.

**Chapter 10** (Labor Markets) applies related monopsony frameworks to employer-side platform power---gig economy classification, wage-fixing algorithms, and no-poach agreements---extending the platform analysis to the labor side. **Chapter 11** (Innovation and IP) addresses interoperability mandates and API access disputes that parallel the data-leverage and foreclosure concerns analyzed here. **Chapter 12** (Litigation Practice) provides expert report templates for platform litigation, and the **Empirical Appendix (Chapter 13)** covers the diagnostic checklists (event studies, DiD) that apply equally to platform remedy evaluation and merger retrospectives. The remedy design principles from **Chapter 8** are essential when crafting platform-specific relief such as choice screens, interoperability mandates, and data portability requirements.
