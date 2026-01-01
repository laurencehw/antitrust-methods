# Market Definition and Competitive Landscape

## Learning goals
Market definition is no longer a rote SSNIP ritual, but agencies and courts still expect a disciplined articulation of product and geographic boundaries before debating competitive effects. This chapter shows you how to frame those boundaries with data and qualitative evidence, evaluate SSNIP/SSNDQ logic, and communicate results across DOJ/FTC, DG COMP, CMA, SAMR, and Competition Tribunal South Africa processes.

By the end of the chapter you should be able to:

- Frame relevant product and geographic markets using demand evidence, diversion ratios, and qualitative industry facts.
- Apply and critique SSNIP/SSNDQ reasoning, critical-loss vs. actual-loss tests, and switching-matrix screens.
- Integrate survey evidence, internal documents, and econometrics into narratives tuned to the burden of proof in each jurisdiction.
- Reference key precedents (e.g., DOJ/FTC Merger Guidelines (2010), EC Market Definition Notice (2024), CMA Merger Guidelines (2021)) and literature when defending methodological choices.

## Why market definition still matters
Even in unilateral-effects cases where agencies focus on margins, diversion, and price effects directly, courts often ask, “what is the market?” The answer shapes presumptions (HHI thresholds, dominance), jurisdictional hooks (public-interest test vs. consumer welfare), and remedy feasibility. Practitioners should treat market definition as an evidence-integration exercise: describe customer substitution paths, quantify them when possible, and tie those findings to the legal standard at issue (e.g., “reasonable interchangeability” in US case law vs. “sufficiently interchangeable” in EC practice). Keep records of how you screened candidate markets so future teams can expand or narrow scope without re-litigating data prep.

> "The 'relevant market' is not an intrinsic feature of the economy, but a tool for analyzing competitive effects... It is defined by the constraints that prevent a hypothetical monopolist from raising prices." — *United States v. Google LLC*, Memorandum Opinion (D.D.C. 2024)

## Core tools and workflow
Modern market-definition work typically cycles through four toolkits:

1. **Descriptive analytics.** Price/volume trends, seasonality, and policy shocks that reveal when products or regions move together. Use `ggplot2` quick looks before heavy modeling.
2. **Demand elasticities & diversion.** Log-log regressions, AIDS-lite models, discrete choice, or churn-based diversion ratios that quantify substitutability. Always document instruments, fixed effects, or controls used.
3. **Critical-loss vs. actual-loss.** Compare hypothetical post-SSNIP losses to observed switching, stating margin assumptions and capacity constraints. Highlight when brand repositioning or supply limits break the classic calculations.
4. **Geographic screens.** Shipment flows, travel-time analyses, or catchment-area heatmaps built from loyalty data, mobile location pings, or Stats SA transport datasets. Pair with qualitative evidence on delivery commitments or regulatory boundaries.

The workflow mirrors Chapter 02’s research design steps: scoping memo → data inventory → qualitative plan → estimation → memo/slide deck. Revisit `chapters/13-empirical-appendix.qmd` for templates.

## Core tools
Use these specific diagnostics to anchor your analysis:

- **Price/quantity dashboards.** Track cointegration, variance ratios, and shock responses to see which products move together.
- **Elasticities/diversion.** Estimate log-log or `fixest` panel regressions; or use choice data (`mlogit`, `apollo`) when products are differentiated.
- **Critical vs. actual loss.** Compare theoretical thresholds to observed share loss; revisit margin assumptions for multi-product firms.
- **Switching matrices, flows, and gravity models.** Summarize customer-level churn or shipment adjacency to motivate geographic splits.

### Critical-loss worksheet
We can calculate critical loss thresholds for various hypothetical segments (e.g., Commercial, Government, SMB) to test if a price increase would be profitable.
```r
library(dplyr)
library(ggplot2)
source("../program/R/helpers.R")

critical_loss <- function(margin, price_increase) {
  price_increase / (price_increase + margin)
}

margin <- 0.25
price_increase <- 0.05
cl_threshold <- critical_loss(margin, price_increase)

observed <- tibble::tribble(
  ~segment, ~observed_share_loss,
  "Commercial group", 0.08, # Hypothetical segments
  "Government", 0.03,
  "SMB", 0.12
) |>
  mutate(
    critical_loss = cl_threshold,
    passes_test = observed_share_loss > critical_loss
  )

knitr::kable(observed, caption="Illustrative Critical Loss by Customer Segment")
```

### Critical-loss vs. actual-loss curve
This visualization compares the theoretical critical loss threshold to observed share losses across different margin assumptions. It helps communicate whether a candidate market "passes" the SSNIP test.

![Critical Loss vs. Actual Loss Test](../images/critical-loss-curve-1.png)

*Points above the curve suggest the candidate market fails SSNIP (too much switching).*

**How to use this chart:** For a given margin estimate (horizontal axis), find the critical loss threshold (the curve). If your observed or estimated actual loss (from switching data, surveys, or diversion ratios) falls *above* the curve, customers switch too readily for a hypothetical monopolist to profitably raise prices by 5-10%, suggesting the candidate market is too narrow and should be expanded. Conversely, if actual loss is *below* the curve, the market definition may be defensible.

Swap `margin` and `price_increase` with matter-specific values. For theoretical derivations, see @katz_shapiro_2003. For alternatives to traditional market definition, see @farrell_shapiro_2010 and @schmalensee_2009. For quantitative techniques, consult @davis_garces_2010.

### Route-share heatmap: NYC airline concentration
This heatmap visualizes carrier concentration on specific routes, helping identify whether route-by-route markets are appropriate or whether broader origin-destination-pairs should be considered. High concentration (dark colors) on specific routes may signal competitive concerns.

![Airline Route Concentration: NYC Area](../images/nyc-route-heatmap-1.png)

*Top 20 routes by volume. HHI values indicate market concentration (>1,800 = highly concentrated per 2023 Guidelines). Source: nycflights13 package.*

**Interpretation:** Routes with HHI > 1,800 (2023 US DOJ/FTC threshold for "highly concentrated") may warrant closer scrutiny. The visualization shows that many NYC routes are served by only 1-2 carriers with dominant shares, which could support narrow route-level market definitions in merger analysis. In practice, you would supplement this with pricing data, switching patterns, and qualitative evidence about entry barriers.

Replace `nycflights13` with live data (slot allocation, loyalty records, booking data, or Stats SA shipment records) when presenting evidence in actual matters.

### Geographic market definition: Shipment flows
Understanding where products physically flow helps define geographic markets. This visualization shows the intensity of shipments between regions, which can reveal natural market boundaries, trade patterns, and whether distant regions constrain local pricing.

![Geographic Shipment Flows: Regional Trade Pattern](../images/geographic-flows-1.png)

*High diagonal values (self-shipments) suggest distinct regional markets. Illustrative data.*

**How to use this analysis:**
- **High self-sufficiency** (diagonal dominance): If 70-80%+ of shipments from a region stay within that region, it suggests the region may be a distinct geographic market.
- **Low cross-flows**: Minimal shipments between distant regions (e.g., Northeast <-> West) suggest they don't constrain each other's pricing.
- **Clustering**: Regions with high mutual flows (e.g., Northeast <-> Southeast) might constitute a single broader market.

In practice, combine this with:
- **Pricing correlation analysis**: Do prices move together across regions?
- **Delivered pricing**: What are freight costs relative to product value?
- **Qualitative evidence**: Customer testimony about willingness to source from distant suppliers, delivery time requirements, etc.

**Data sources:**
- US: Census Commodity Flow Survey (5-year intervals), BEA trade flows by state
- South Africa: Stats SA provincial trade data, National Treasury procurement records
- Company-specific: Shipping manifests, customer address clustering, delivery zone definitions

### Diversion ratios from customer switching data
Diversion ratios quantify where customers go when their first choice becomes unavailable or more expensive. They are critical for market definition, UPP calculations, and merger simulation. This example shows how to compute diversion from customer-level switching or choice data.

![Diversion Ratios: Where Do Customers Go?](../images/diversion-ratios-1.png)

*High diversion to merger partner suggests products compete closely. Source: Simulated switching data.*

**Interpretation for merger analysis:**
- **High diversion between merger parties** (e.g., 25-35% from A→B): Strong evidence products compete closely; supports narrow market definition and raises UPP concerns.
- **Low diversion to outside option**: Customers are "captive" to the industry, strengthening market power concerns.
- **Symmetric vs. asymmetric diversion**: If A→B is 30% but B→A is only 15%, Product A is a closer substitute for B than vice versa (important for UPP calculations).

**Data sources:**
- **Loyalty/transaction data**: Track customer purchases before/after product unavailability or price changes
- **Surveys**: "If Product A were unavailable, what would you buy instead?" (watch for hypothetical bias)
- **Natural experiments**: Stockouts, temporary exits, localized price shocks
- **Discrete choice experiments**: Show customers product bundles and estimate substitution patterns

{% hint style="info" %}
**Method box**

- **Computing diversion from panel data.** Use customer-level purchase histories to track switches after price changes, stockouts, or exits: `dplyr::group_by(customer) |> arrange(date) |> lag(product)` to identify transitions.

- **Survey-based diversion.** Ask "next best" questions but weight by purchase likelihood; validate against revealed switching where possible. Document screening (exclude inattentive respondents) and show robustness to alternative weighting schemes.

- **Entry/exit event studies.** When competitors enter or exit (Lyft entering a city, clinic closure), run high-frequency event studies on prices/volumes to see whether products constrain each other.

- **Cross-price elasticities with uncertainty.** Pair point estimates with bootstrapped intervals (or Bayesian draws) and present them in `gt` (the R “grammar of tables” package, which produces formatted tables) so tribunals can see both the estimates and their precision.

- **Discrete choice models.** For differentiated products, estimate multinomial logit or nested logit models (`mlogit`, `apollo` packages) to recover full substitution matrices and test market definitions.
{% endhint %}

{% hint style="info" %}
**Qualitative evidence**

**Product positioning.** Sales playbooks, win/loss reports, and marketing decks often list "closest competitor" products—quote them and tie to diversion ratios.  
**Customer evidence.** Structured interviews and surveys reveal practical switching hurdles, procurement timelines, and multi-homing behavior. Document sampling rigor following established survey research standards.  
**RFP and contract language.** Bid specs, exclusivity clauses, and default settings (especially on platforms) show whether customers view products as substitutes.
{% endhint %}

{% hint style="info" %}
**Case box: Market definition in practice**

**Hospitals & insurers (US).** In FTC v. Advocate Health Care (7th Cir. 2017), the court examined whether a hospital merger would harm commercially insured patients in the Chicago North Shore area. The FTC presented patient origin data showing that 80% of patients traveled less than 15 miles, commercial insurer testimony about limited bargaining leverage with "must-have" hospitals, and survey evidence on patient switching. Defendants countered with broader geographic market definitions based on physician referral patterns and specialty care availability. The court sided with the FTC's narrower market, emphasizing that commercial insurers—not patients—were the direct customers, and their testimony about competitive dynamics was dispositive. **Lesson:** In two-sided markets, identify the relevant customer for market definition purposes and weight their testimony heavily.

**Grocery retail (South Africa).** The 2015-2019 Grocery Retail Market Inquiry combined loyalty-card transaction data from Pick n Pay and Shoprite covering millions of baskets, mall lease registers showing exclusive clauses, and micro-level CPI data by product and township. Investigators used the loyalty data to map customer catchment areas, finding that 70-80% of shoppers traveled less than 5 kilometers. They simulated a 5% SSNIP on a basket of staples and estimated that only 15-20% of customers would switch to more distant stores, well below the critical loss threshold for margins of 25-30%. The inquiry documented how long-term exclusive leases between national chains and mall developers foreclosed entry by discounters in townships, effectively segmenting markets by neighborhood. **Lesson:** Granular transaction data can overcome theoretical debates about SSNIP tests; pair with qualitative evidence (lease contracts) to show barriers to expansion.

**Tech platforms: Google Search (US/EU).** In US v. Google (2020) and European Commission decisions, market definition turned on whether general search, specialized search (maps, shopping, travel), and social media search were in the same market. Google argued for a broad "online advertising" or "digital information" market. Agencies presented telemetry showing users rarely substitute between general search and social platforms for commercial queries, default contract terms showing Google paid billions to remain the default on Safari/Chrome (revealing high diversion), and advertiser testimony that search ads have unique intent-based targeting. The narrow "general search" market was upheld. **Lesson:** In zero-price markets, use revealed preference (default payments, multi-homing rates) rather than stated willingness to pay; SSNDQ (Small but Significant Non-transitory Decrease in Quality) can substitute for SSNIP.

**Ride-hailing (Asia/Africa).** Japan's JFTC and South Africa's Competition Commission both investigated ride-hailing platforms. JFTC examined whether taxi services and ride-hailing were in the same market, analyzing driver multi-homing (many drivers used both Uber and local apps), rider app-switching behavior via surveys, and pricing correlation. High multi-homing suggested low switching costs, supporting a broader market. In South Africa, the Commission's digital platform inquiry examined Uber, Bolt, and local competitors, finding that commission caps and driver exclusivity clauses fragmented the market geographically (Gauteng vs. Western Cape) and by vehicle class (metered taxis vs. e-hailing). **Lesson:** Multi-sided platform markets require separate analysis of each side (riders, drivers) and attention to contractual terms that may segment otherwise integrated markets.
{% endhint %}

### Southern African market evidence
- **Private Healthcare Market Inquiry (Competition Commission, 2014–2019).** Tribunal-appointed panel reviewed six years of patient-level claims covering roughly 70% of the 8.8 million beneficiaries in South Africa’s private schemes, combining them with supplier cost data to test alternative geographic definitions for specialist care. The inquiry found Herfindahl indices above 4,000 in several provinces and documented limited patient switching despite tariff differentials, motivating recommendations on supply-side licensing reform and transparency.
- **Grocery Retail Market Inquiry (2015–2019).** Investigators merged retailer loyalty data, mall lease registers, and micro-CPI data to map catchment areas for supermarkets versus spaza shops. By simulating 5% SSNIP-style shocks with actual basket-level switching elasticities, the Commission showed how long-term exclusive leases between national chains and landlords constrained entry by discounters in townships and secondary towns.
- **Data Services Market Inquiry (2017–2019).** The Competition Commission benchmarked prepaid mobile data prices (30-day 1GB basket) against a peer group of African and BRICS comparators, documenting South African prices that were roughly 20–40% above the median even after controlling for spectrum cost proxies and GDP per capita. Subscriber-level usage data from MTN and Vodacom revealed steep price discrimination by income segment, which fed into the Tribunal-endorsed commitments to cut headline prepaid rates by 30–50% and expand zero-rated educational content.

{% hint style="info" %}
**Debate: Is market definition still necessary?**

A lively debate centers on whether formal market definition remains essential in unilateral effects analysis. **The traditional view** (agencies, most courts) holds that market definition disciplines the analysis: it forces practitioners to articulate which products/regions constrain pricing, establishes evidentiary presumptions (HHI thresholds), and provides a common language across jurisdictions. Without it, arguments risk becoming untethered from competitive reality.

**The reform view** (some economists, recent US guidelines commentary) argues that diversion ratios, margins, and UPP/GUPPI directly answer the relevant question—"will this merger raise prices?"—without the need for binary in/out market distinctions. Forcing a SSNIP test can be arbitrary (the 5-10% threshold is a convention, not economics), and critical-loss analysis is sensitive to margin measurement. Modern tools (merger simulation, natural experiments) can estimate price effects directly. See Katz & Shapiro (2003), Farrell & Shapiro (2010), and Werden (2012) for the evolution of this debate.

**Practical middle ground:** Most practitioners define a candidate market to anchor share calculations and HHI, but also present direct evidence (diversion, UPP, simulation) to avoid getting bogged down in SSNIP debates. Courts still expect market definition—especially in monopolization and vertical cases where structural presumptions remain central—so skip it at your peril. Document the market definition exercise even if your ultimate analysis relies on direct effects modeling.

**Jurisdictional variation:** DG COMP and the CMA increasingly accept "direct effects" arguments in merger reviews but still require formal market definition in abuse-of-dominance cases. The US has moved toward pragmatism: the 2023 Merger Guidelines retain market definition but emphasize it's not always necessary when direct evidence of competitive effects is available. South African practice follows this middle path: the Competition Act requires market definition for some statutory tests (dominance, public interest), but practitioners routinely supplement with direct diversion and simulation evidence.
{% endhint %}

{% hint style="info" %}
**Citations and comparative note**

- Cite market definition sources such as US Merger Guidelines SSNIP discussion (DOJ/FTC, 2010) and EC Notice on market definition (2024); add CMA cases for UK context.
- When using surveys or switching analyses, reference standards on survey reliability (e.g., reference guides, cases admitting/excluding surveys).
- Flag jurisdictional differences explicitly when SSNDQ or platform-centric approaches apply more than SSNIP (e.g., EU digital contexts).
{% endhint %}

## Looking ahead
Export cleaned switching matrices, elasticity estimates, and qualitative chronologies to the shared appendix so the IO, merger, and cartels chapters can reuse them. Before moving to Chapter 04, confirm that your demand estimates include the product/segment labels used in the IO models and that any survey instruments or interviews are logged in the qualitative template.
