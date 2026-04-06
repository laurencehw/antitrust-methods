# Regulation and Remedies 

The preceding chapters focused on diagnosing competitive harm---identifying cartels ([Chapter 5: Cartels](05-cartels.md)), predicting merger effects ([Chapter 6: Mergers](06-mergers.md)), and establishing exclusionary conduct ([Chapter 7: Monopolization](07-monopolization.md)). But identifying harm is only half the job. This chapter addresses what comes next: designing remedies that actually work and, in some cases, ongoing regulatory frameworks that substitute for competition where markets cannot be made competitive.

Remedy design requires different skills than liability analysis. You must think dynamically about how firms will respond to constraints, whether trustees can effectively monitor behavioral commitments, and whether structural relief will create viable competitors. The economic tools are familiar---cost analysis, benchmarking, causal inference for evaluation---but the application shifts from diagnosis to prescription.

## Learning goals
Antitrust analysis often ends with a liability finding, but policy work begins there. This chapter explains how to translate theories of harm into durable remedies and how to design regulatory frameworks when competition alone cannot discipline pricing or access. You will learn to:

- Compare rate-of-return, price-cap, and incentive regulation, and pick the tool that matches industry fundamentals (cost structure, demand volatility, data availability).
- Design structural and behavioral remedies that map directly to diagnosed harms, with clear monitoring and reporting plans.
- Evaluate remedy effectiveness using retrospective econometrics---diff-in-diff and event studies, following the design principles in [Chapter 2: Research Design](02-research-design.md)---and benchmarking models.
- Integrate qualitative evidence (compliance reports, trustee memos, stakeholder hearings) with quantitative indicators.

## Why regulation and remedies matter
Competition authorities increasingly pair enforcement with sector inquiries that feed straight into regulatory design (e.g., the South African Data Services and Private Healthcare inquiries, conducted under the broad market inquiry powers of the Competition Act [@sa_competition_act_1998]). Meanwhile, merger and monopolization cases frequently conclude with behavioral obligations or divestitures that require economic monitoring. Understanding regulatory levers ensures your recommendations remain credible after the headline settlement.

## Workflow overview

{% hint style="info" %}
**Remedy Design and Evaluation Workflow**
```
DIAGNOSIS                 DESIGN                    IMPLEMENTATION
    |                        |                           |
    v                        v                           v
+-------------+        +-------------+            +-------------+
| Identify    |        | Match       |            | Specify     |
| source of   |------->| remedy to   |----------->| monitoring  |
| market      |        | theory of   |            | & compliance|
| power/harm  |        | harm        |            | framework   |
+-------------+        +-------------+            +-------------+
    |                        |                           |
    v                        v                           v
+-------------+        +-------------+            +-------------+
| Natural     |        | STRUCTURAL: |            | KPIs &      |
| monopoly?   |        | Divestiture |            | dashboards  |
| Entry       |        | Asset swap  |            |             |
| barriers?   |        +-------------+            +-------------+
| Conduct?    |               |                         |
+-------------+               v                         v
                       +-------------+            +-------------+
                       | BEHAVIORAL: |            | Trustee     |
                       | Access      |            | reports &   |
                       | MFN bans    |            | audits      |
                       | Pricing     |            +-------------+
                       | Transparency|                   |
                       +-------------+                   v
                              |                   +-------------+
                              v                   | EVALUATION  |
                       +-------------+            | DiD / Event |
                       | REGULATORY: |            | studies     |
                       | Rate-of-    |            | Benchmarks  |
                       | return      |            +-------------+
                       | Price-cap   |
                       +-------------+
```
**Key principle:** Remedies must be verifiable, enforceable, and tied directly to the diagnosed harm.
{% endhint %}

A typical engagement looks like this:

1. **Diagnose** the source of market power or harm (natural monopoly, entry barriers, conduct).
2. **Select regulatory instruments** (rate-of-return, price-cap, access pricing, incentive schemes).
3. **Design remedies** matched to the theory of harm (divestitures, access mandates, data-sharing, reporting).
4. **Specify monitoring**: KPIs, reporting cadence, trustee authority.
5. **Evaluate outcomes** periodically using benchmarking or causal inference.

## Rate-of-return vs. price-cap regulation

The economic theory of regulation is well developed [for textbook treatments, see @tirole_1988; @motta_2004]. Two dominant approaches---rate-of-return and price-cap---each present distinct trade-offs for practitioners.

### Rate-of-return (cost-plus) regime

Under rate-of-return regulation, a regulator determines the firm's allowable revenue using the basic formula: *Revenue = (Rate Base × Allowed Rate of Return) + Operating Expenses + Depreciation*. The rate base consists of the firm's prudently incurred capital investments (plant, equipment, network infrastructure), valued at either historical cost or replacement cost depending on the jurisdiction. The allowed rate of return is set to cover the firm's weighted average cost of capital, giving investors a fair return without enabling supranormal profits. This approach remains common in energy distribution, water utilities, and some telecommunications infrastructure, particularly in the United States where state public utility commissions regulate electricity and natural gas distribution using variants of this framework.

The central weakness of rate-of-return regulation is the Averch-Johnson effect, first formalized by @averch_johnson_1962. Because the firm earns a return on its rate base, it has an incentive to overinvest in capital---a phenomenon often called "gold-plating." If the allowed rate of return exceeds the true cost of capital, the firm can increase profits by expanding its asset base, even when the additional investment is socially wasteful. For example, a utility might build excess generation capacity or install unnecessarily expensive equipment because each dollar added to the rate base generates additional regulated revenue. This creates a systematic bias toward capital-intensive solutions over potentially more efficient alternatives, such as demand-side management or leasing arrangements that would not enter the rate base.

Despite these well-documented inefficiencies, rate-of-return regulation persists in many jurisdictions for practical reasons. It provides regulators with detailed visibility into firm costs, which can be valuable when information asymmetries are severe or when regulated firms operate in politically sensitive sectors where price shocks are unacceptable. The approach also offers investors regulatory certainty: because costs are passed through, the firm faces less earnings volatility, which reduces the cost of capital. For antitrust practitioners, understanding rate-of-return regulation matters because remedies in regulated industries often interact with the regulatory framework. A divestiture or access mandate imposed by a competition authority must be compatible with the existing rate-setting process, and the data generated by rate cases---cost studies, asset valuations, depreciation schedules---can be valuable inputs for competition analysis.

### Price-cap (RPI-X) regime

Price-cap regulation, developed by Stephen Littlechild in the early 1980s for the privatization of British Telecom, takes a fundamentally different approach. Instead of scrutinizing costs and setting a fair return, the regulator caps the prices the firm can charge using the formula: *Price~t+1~ = Price~t~ × (1 + RPI - X)*, where RPI is the retail price index (a measure of inflation) and X is an expected productivity improvement factor. The X-factor is typically set at the beginning of a multi-year regulatory period (often four to five years) based on engineering studies, efficiency benchmarking, and consultation with the regulated firm. During the cap period, the firm retains any cost savings it achieves beyond the X-factor target, creating a powerful incentive to cut costs and innovate. At each regulatory reset, the regulator can adjust X to reflect new information about achievable efficiency gains, partially passing accumulated savings through to consumers.

The incentive properties of price-cap regulation contrast sharply with rate-of-return. Because the firm keeps the difference between its actual costs and the price cap, it has a strong incentive to minimize expenditure---the opposite of the Averch-Johnson gold-plating problem. This model was adopted across UK utility regulation, with Ofcom (telecommunications), Ofwat (water and sewerage), and Ofgem (energy networks) each operating variants of the RPI-X framework. Ofgem's RIIO model (Revenue = Incentives + Innovation + Outputs) represents a modern evolution that sets caps based on outputs (reliability, customer satisfaction, environmental targets) rather than simple cost trajectories, rewarding firms that outperform on quality as well as efficiency.

However, price-cap regulation carries its own risks. The most significant is quality degradation: a firm under a tight price cap may cut costs by reducing maintenance, delaying investment, or degrading service quality in ways that are difficult for the regulator to observe immediately. To address this, most price-cap regimes incorporate explicit quality-of-service metrics with financial penalties (or "deadbands" that define acceptable ranges). A second concern is gaming at the reset: firms may inflate costs in the years leading up to a regulatory review to secure a more favorable baseline, a problem known as the "ratchet effect." For antitrust practitioners, price-cap frameworks are relevant because they demonstrate how incentive-compatible regulation can be designed---principles that carry over directly to the design of behavioral remedies with pricing commitments, where the goal is similarly to constrain prices while preserving incentives for efficient operation.

#### Access pricing and the Efficient Component Pricing Rule (ECPR)

Essential facilities (e.g., telecom local loops, gas pipelines, rail track) often require access pricing rules that allow rivals to use the incumbent's bottleneck infrastructure at a regulated charge. The legal foundations differ across jurisdictions: the EU's essential facilities doctrine, shaped by @eu_bronner_1998 and @eu_ims_2004, imposes access obligations more readily than US law, where @us_trinko_2004 significantly narrowed the scope of forced dealing under Section 2 of the Sherman Act.

The Efficient Component Pricing Rule (ECPR), associated with the work of William Baumol and J. Gregory Sidak, provides a simple formula for setting the access charge:

> **Access Charge = Retail Price - Avoidable Downstream Costs of the Incumbent**

The logic is that the access charge should compensate the incumbent for the *opportunity cost* of providing access---that is, the profit it forgoes when an entrant serves a customer the incumbent would otherwise have served. The avoidable costs are those the incumbent no longer incurs when it loses the downstream sale (e.g., retail staff, billing, marketing).

**Worked example.** Suppose a vertically integrated telecommunications incumbent provides local loop access to a rival long-distance carrier. The incumbent's retail price for an end-to-end call is \$1.00 per minute. Its avoidable downstream costs---switching, billing, customer service, and retail marketing---amount to \$0.60 per minute. Under ECPR, the access charge for use of the local loop would be:

> Access Charge = \$1.00 - \$0.60 = **\$0.40 per minute**

At this access charge, a rival can profitably enter the downstream market only if its own downstream costs are below \$0.60---that is, only if it is at least as efficient as the incumbent in the contestable segment. If the rival's downstream costs are \$0.50, it pays \$0.40 for access and \$0.50 for its own operations, for a total cost of \$0.90, allowing it to undercut the incumbent's \$1.00 retail price while still earning a margin.

**The critical limitation of ECPR** is that it preserves the incumbent's existing profit margin on the bottleneck facility. If the incumbent's retail price already reflects monopoly rents---that is, if \$1.00 is above the competitive level---then the ECPR access charge of \$0.40 embeds those rents. The entrant can compete on the downstream segment but cannot challenge the incumbent's upstream market power. For this reason, many regulators reject ECPR in favor of cost-based approaches such as Long-Run Incremental Cost (LRIC), which sets the access charge based on the forward-looking efficient cost of providing the bottleneck service, stripping out monopoly rents entirely. The European Commission's approach in cases like @eu_deutsche_telekom_2010 and @eu_telefonica_2014 effectively requires margin squeeze tests that go beyond ECPR by ensuring the access charge allows a reasonably efficient competitor to operate profitably downstream [contrast with the US approach in @us_linkline_2009, where the Supreme Court rejected a standalone price-squeeze claim under Section 2].

When designing access remedies in practice, the economist should document:

- The incremental cost of providing access, ideally using a bottom-up LRIC model.
- Margin squeeze tests comparing the wholesale access price to the retail price minus the downstream cost of a reasonably efficient operator.
- Capacity constraints and queue management rules, especially where the bottleneck facility has limited throughput.
- Quality and operational KPIs---fault rates, provisioning times, repair response---to ensure the incumbent does not degrade access quality as a form of non-price discrimination.

#### Access pricing in South Africa: the Telkom precedent

South Africa's Competition Tribunal has used access pricing remedies in several high-profile abuse-of-dominance cases. The **Telkom wholesale settlements** (2013) required Telkom to provide competitors with access to its local loop and wholesale broadband services at regulated prices [@sa_telkom_2013]. The Tribunal's remedy combined a margin squeeze test (ensuring the spread between wholesale and retail prices allowed efficient downstream competition) with ongoing reporting requirements on fault rates, provisioning times, and service quality. The remedy was notable for its quasi-regulatory character: rather than a one-time penalty, it established an ongoing pricing framework that functioned much like sector regulation. The Commission's monitoring team tracked six KPIs quarterly, with escalation procedures for any metric that fell below the committed threshold for two consecutive periods. This approach---using competition law remedies to create de facto regulatory oversight in the absence of a sectoral regulator---has become a distinctive feature of South African competition enforcement, particularly in sectors where ICASA's capacity is limited or where the market structure has evolved faster than the regulatory framework.

## Incentive regulation and benchmarking
Benchmarking and yardstick competition compare regulated entities to peers to set targets without micromanaging costs. Examples include Ofgem's RIIO model and the planned South African Supply-Side Regulator for Health.

#### Real utility benchmarking: South African provincial electricity and manufacturing

South Africa's electricity crisis provides a real-world benchmarking case. The decline in available generation capacity (measured in GWh) directly constrains manufacturing output across provinces. By comparing provincial manufacturing production to electricity availability, regulators can identify which provinces are most affected by supply constraints and which have managed to maintain productivity despite the crisis.

```r
library(dplyr)
library(ggplot2)
library(readr)
library(lubridate)
library(tidyr)
source("program/R/helpers.R")

# Load SA electricity data
elec <- read_csv("../the south african economy/___Contemporary/data/processed/electricity_available_gwh_sa.csv",
                 show_col_types = FALSE) |>
  mutate(date = as.Date(date))

# Load SA manufacturing production
mfg <- read_csv("../the south african economy/___Contemporary/data/processed/manufacturing_production_index.csv",
                show_col_types = FALSE) |>
  mutate(date = as.Date(date))

# Load provincial GDP by sector
pgdp <- read_csv("../the south african economy/___Contemporary/data/processed/provincial_gdp_by_sector.csv",
                 show_col_types = FALSE) |>
  filter(sector == "Manufacturing",
         region %in% c("South Africa", "Gauteng", "Western Cape", "KwaZulu-Natal",
                       "Eastern Cape", "Free State"))

# Panel A: Electricity availability over time
p1 <- ggplot(elec, aes(x = date, y = value)) +
  geom_line(color = "#D55E00", linewidth = 1) +
  geom_smooth(method = "loess", span = 0.3, color = "#0072B2", linewidth = 1.2, se = FALSE) +
  labs(
    title = "South African Electricity Availability (2000–2025)",
    subtitle = "Monthly GWh available. Blue line: loess smooth. Source: Stats SA.",
    x = NULL, y = "GWh Available"
  ) +
  theme_antitrust()

# Panel B: Provincial manufacturing GDP trends
p2 <- ggplot(pgdp, aes(x = year, y = gdp_rmillion / 1e6, color = region)) +
  geom_line(linewidth = 1) +
  scale_color_manual(values = c(
    "South Africa" = "#333333",
    "Gauteng" = "#D55E00",
    "Western Cape" = "#0072B2",
    "KwaZulu-Natal" = "#009E73",
    "Eastern Cape" = "#CC79A7",
    "Free State" = "#E69F00"
  )) +
  labs(
    title = "Provincial Manufacturing GDP (Constant 2015 Rand)",
    subtitle = "Top 5 provinces. Source: Stats SA provincial accounts.",
    x = NULL, y = "Manufacturing GDP (R billion)", color = NULL
  ) +
  theme_antitrust() +
  theme(legend.position = "bottom")

# Display both panels
if (requireNamespace("patchwork", quietly = TRUE)) {
  library(patchwork)
  p1 / p2 + plot_layout(heights = c(1, 1))
} else {
  print(p1)
  print(p2)
}

# Benchmarking table: electricity-manufacturing correlation
cat("\nElectricity-Manufacturing Correlation by Province:\n")
# Merge electricity and national manufacturing
elec_mfg <- elec |>
  mutate(year = lubridate::year(date), month = lubridate::month(date)) |>
  left_join(
    mfg |> mutate(year = lubridate::year(date), month = lubridate::month(date)),
    by = c("year", "month"),
    suffix = c("_elec", "_mfg")
  )

cat(paste0("Correlation between electricity availability and manufacturing: ",
           round(cor(elec_mfg$value_elec, elec_mfg$index, use = "complete.obs"), 3), "\n"))
```

This real-data benchmarking exercise reveals the structural relationship between electricity supply and manufacturing output. The correlation between available GWh and the manufacturing production index quantifies the extent to which load-shedding constrains industrial activity---a critical input for regulatory remedy design. When the Supply-Side Regulator for Health is established, similar benchmarking methods will compare hospital costs and quality outcomes across provinces, using the same yardstick competition framework that Ofgem applies to UK energy networks.

## Remedy design after antitrust findings

### Structural vs. behavioral

Merger guidelines in major jurisdictions discuss both structural and behavioral remedies [@doj_ftc_hmg_2023; @cma_merger_assessment_2021; @ec_hmg_2004]; the horizontal merger framework in [Chapter 6: Mergers](06-mergers.md) provides the diagnostic tools that inform remedy selection. Vertical mergers, covered separately by @doj_ftc_vmg_2020, often raise remedy design questions involving access and non-discrimination commitments rather than divestitures. The choice between structural and behavioral remedies depends on the diagnosed harm, the feasibility of monitoring, and the institutional capacity of the enforcing agency.

**Structural remedies**---divestitures, ownership separation, and asset swaps---are generally preferred by competition authorities when the competitive concern is horizontal overlap. The logic is straightforward: by transferring assets to a new or existing competitor, a divestiture creates a self-enforcing remedy that does not require ongoing regulatory oversight. Once the divested business is operating independently, market forces discipline pricing and innovation without the need for a compliance trustee or periodic review. For this reason, both the DOJ and the European Commission have expressed a strong preference for structural relief in horizontal merger cases. The DOJ's merger remedies guidance states that structural remedies are "preferred to conduct remedies" because they are "clean and certain" and avoid the costs of ongoing supervision. However, structural remedies carry their own risks: the divested assets must be viable as a standalone business, the buyer must have the capability and incentive to compete effectively, and the divestiture process itself---which may take 6--12 months---can create transitional disruptions that erode the value of the divested business.

**Behavioral (or conduct) remedies**---access commitments, most-favored-nation (MFN) bans, parity obligations, algorithm transparency requirements, firewall provisions, and anti-retaliation clauses---are more common in vertical merger cases and in abuse-of-dominance proceedings where the competitive concern relates to foreclosure or discrimination rather than the elimination of a direct rival. The consent decree in @us_microsoft_2001 is a canonical example: rather than breaking up Microsoft, the final judgment imposed interoperability and non-discrimination obligations that required sustained monitoring over a decade-long compliance period---the underlying monopolization theory is analyzed in [Chapter 7: Monopolization](07-monopolization.md). Behavioral remedies offer flexibility---they can be tailored to address specific theories of harm without the disruption of asset sales---but they impose significant monitoring costs on the enforcing agency. The compliance trustee must verify adherence, interpret ambiguous provisions, and respond to complaints from rivals who may have incentives to game the process. These challenges have led the FTC's Bureau of Competition to express skepticism about behavioral remedies in several retrospective studies, finding that conduct conditions in merger settlements have a mixed track record: some succeed in preserving competition, while others are evaded through creative compliance or become obsolete as market conditions evolve.

The empirical evidence on remedy effectiveness reinforces the importance of matching the remedy to the theory of harm. FTC retrospective studies of merger remedies have found that divestitures are more likely to maintain competition when the buyer is an existing market participant with operational expertise, and less likely to succeed when the divested assets require ongoing transitional services from the merged firm. Behavioral remedies, meanwhile, tend to work best when the obligations are specific, measurable, and time-limited, and when the enforcing agency has sufficient resources to monitor compliance. In the South African context, the Competition Tribunal frequently attaches public interest conditions to merger approvals---employment guarantees, local procurement requirements, and commitments to maintain operations in underserved areas---alongside conventional competition conditions. These hybrid remedy packages reflect the broader mandate of the South African competition framework, which explicitly incorporates public interest factors into merger review [@sa_competition_act_1998]. For the practitioner, the lesson is that remedy design must account for the institutional environment: a remedy that works well in a jurisdiction with a well-resourced monitoring agency may fail where enforcement capacity is limited.

When drafting behavioral remedies, specify:

1. **Scope and metrics** (e.g., access price formula, quality KPIs).  
2. **Reporting cadence** (quarterly dashboards, API feeds).  
3. **Trustee authority** (independent monitor credentials, escalation paths).  
4. **Sunset or reassessment triggers.**

{% endhint %}{.callout-note title="Case box: AT&T/Time Warner --- The limits of behavioral remedies in vertical mergers"}
In 2018, AT&T acquired Time Warner (owner of HBO, CNN, and Warner Bros.) for \$85 billion, creating a vertically integrated firm controlling both content production and distribution infrastructure. The DOJ challenged the merger, arguing that AT&T would have the incentive and ability to raise the price of Time Warner content to rival distributors (such as Dish Network and cable companies), or to withhold it entirely, thereby harming competition in the pay-television market. The district court rejected the DOJ's challenge, and the merger proceeded without structural or behavioral conditions. Judge Leon found that the government's bargaining-model evidence was insufficient to establish likely competitive harm. Critics of the decision argued that the court underweighted the dynamic effects of vertical integration, including the risk that AT&T would use Time Warner content to favor its own streaming platform (which later launched as HBO Max) at the expense of rival distributors. Within three years, AT&T unwound the acquisition, spinning off WarnerMedia to merge with Discovery---suggesting that the anticipated vertical synergies failed to materialize. The case is widely cited as illustrating the difficulty of predicting vertical merger effects and the limitations of relying on court-imposed behavioral remedies (or, in this case, no remedy at all) when vertical integration creates ongoing incentives for foreclosure.
{% endhint %}

### Monitoring and compliance
Create compliance scorecards that align with the remedy's logic. For example, if the remedy ensures rival access to APIs, track uptime, latency, and parity between internal and external developers. Use qualitative sources---monitor reports, public hearings, stakeholder interviews---to contextualize metrics.

#### Remedy monitoring KPIs

Effective remedy monitoring requires a dashboard of key performance indicators that map directly to the theory of harm. The choice of KPIs depends on the remedy type:

| Remedy Type | Core KPIs | Monitoring Frequency | Red Flag Thresholds |
|-------------|-----------|---------------------|---------------------|
| Access commitment | API uptime, latency, feature parity | Monthly | >5% degradation vs. internal access |
| Non-discrimination | Price parity, quality parity, ranking position | Quarterly | >10% price differential |
| Divestiture | Buyer viability, market share trajectory | Semi-annual | Declining market share post-divestiture |
| Price cap | Tariff compliance, cost pass-through | Quarterly | Price exceeds cap by >2% |
| Data sharing | Data completeness, timeliness, format parity | Monthly | >15% data fields missing |

The South African Data Services Market Inquiry provides a model for remedy monitoring: the Commission required Vodacom and MTN to report quarterly on prepaid data prices, zero-rated services, and MVNO access terms, with an independent monitoring trustee verifying compliance. The Commission's monitoring dashboard tracked six KPIs over a two-year period, with escalation procedures for any KPI that fell below the committed threshold for two consecutive quarters.

{% hint style="info" %}
**Case box: South Africa's Data Services Market Inquiry --- Remedy Design and Monitoring**
In 2017, the South African Competition Commission launched a market inquiry into data services, responding to public concern that mobile data prices were unaffordable for low-income consumers. The Commission's approach combined multiple analytical methods: (1) international price benchmarking across 70+ countries, controlling for income levels and network costs; (2) profitability analysis using publicly reported financials to show that Vodacom and MTN earned returns on capital significantly above their weighted average cost of capital; and (3) cost modeling to determine the efficient cost of providing data services.

The inquiry's final report (December 2019) recommended that both operators reduce the headline price of sub-1GB prepaid data bundles---the packages most used by low-income consumers---within defined timeframes. Both operators agreed to price reductions, with Vodacom cutting its 500MB bundle price by over 30%. The Commission also mandated open-access APN regulations to lower barriers for MVNOs and required zero-rating of essential public websites.

The remedial framework is notable for its monitoring architecture. The Commission established a compliance dashboard tracking six KPIs: (1) prepaid data prices for bundles under 1GB, (2) per-MB out-of-bundle rates, (3) zero-rated website availability, (4) MVNO access terms, (5) network quality metrics, and (6) complaint resolution times. Vodacom and MTN reported quarterly, with an independent monitoring trustee verifying the data. Any KPI that fell below the committed threshold for two consecutive quarters triggered an escalation procedure, including public hearings and potential referral to the Competition Tribunal for enforcement.

This inquiry demonstrates how competition authorities can use benchmarking and profitability analysis to design targeted, consumer-facing remedies without resorting to full-scale price regulation. The monitoring framework---with its specific KPIs, reporting cadence, and escalation procedures---provides a model for remedy design in other concentrated sectors.
{% endhint %}

#### Retrospective diff-in-diff scaffold
```r
library(dplyr)
library(fixest)

# data columns: region, period, treated (1 if subject to remedy), outcome
# Example uses synthetic data
set.seed(123)
panel <- expand.grid(region = LETTERS[1:6], period = 2016:2022) |>
  mutate(
    treated = if_else(region %in% c("A","B","C"), 1, 0),
    post = if_else(period >= 2019, 1, 0),
    outcome = 100 + rnorm(n(), 0, 2) - 2 * (treated * post) + 0.5 * period
  )

did_model <- feols(outcome ~ treated:post | region + period, data = panel)
summary(did_model)
```
Swap the synthetic data with actual KPI panels (e.g., mobile data prices before/after the Data Services commitments, hospital tariffs after remedy adoption). Store sanitized versions in `data/derived/regulation/` with README files tracking provenance.

## Southern African market inquiries and remedy design

South Africa's Competition Act [@sa_competition_act_1998] grants the Competition Commission broad market inquiry powers that sit between traditional antitrust enforcement and sector regulation. These inquiries allow the Commission to investigate the general state of competition in a market without requiring evidence of a specific contravention, producing recommendations that can range from voluntary commitments to binding orders. Several landmark inquiries illustrate how empirical methods translate into remedy design.

The **Private Healthcare Market Inquiry (2014--2019)** used case-mix adjusted benchmarking across eight hospital groups to demonstrate significant price variation that could not be explained by patient acuity or facility quality alone. Its central recommendation---the creation of a Supply-Side Regulator for Health---represents a shift from one-off enforcement to ongoing regulatory oversight, drawing on the benchmarking and yardstick competition principles discussed above.

The **Data Services Market Inquiry (2017--2019)** combined international price benchmarking with profitability analysis to show that South African prepaid mobile data prices were high relative to comparable markets. The resulting commitments from Vodacom and MTN included mandatory reductions in sub-1GB prepaid data prices, open-access APN rules, and zero-rating of public benefit websites. The **Public Passenger Transport Inquiry (2017--2020)** used route maps, tender records, and e-hailing platform data to design subsidy formulas and fare transparency rules for both formal and informal operators. Meanwhile, the **Sasol Gas and Telkom wholesale settlements** illustrate how antitrust remedies can morph into quasi-regulatory regimes: margin-squeeze tests combined with cost-plus access obligations created ongoing pricing frameworks that function much like sector regulation [@sa_sasol_2014; @sa_telkom_2013].

{% endhint %}{.callout-note title="Case box: South Africa's Data Services Market Inquiry (2017--2019)"}
In 2017, the South African Competition Commission launched a market inquiry into the cost of data services, responding to public concern that mobile data prices were unaffordable for low-income consumers. The Commission's economic team assembled international price benchmarks covering over 70 countries, controlling for income levels, network costs, and market structure. Profitability analysis using publicly reported financials showed that Vodacom and MTN earned returns on capital significantly above their weighted average cost of capital, consistent with the exercise of market power in a concentrated duopoly. The inquiry's final report (December 2019) recommended that both operators reduce the headline price of sub-1GB prepaid data bundles---the packages most used by low-income consumers---within defined timeframes. Both operators agreed to price reductions, with Vodacom cutting its 500MB bundle price by over 30 percent. The Commission also mandated open-access APN regulations to lower barriers for MVNOs and required zero-rating of essential public websites (e.g., government services, job portals). This inquiry demonstrates how competition authorities can use benchmarking and profitability analysis to design targeted, consumer-facing remedies without resorting to full-scale price regulation.
{% endhint %}

{% hint style="success" %}
**Extended example: Evaluating healthcare competition remedies**
Hospital merger remedies range from full divestitures---requiring the merged system to sell a hospital or campus---to behavioral commitments such as rate caps, quality guarantees, and network access obligations. The FTC generally prefers structural remedies, but hospital divestitures are uniquely complex: the buyer must be capable of operating a full-service hospital, maintaining physician relationships, and investing in capital equipment. Failed divestitures---where the buyer cannot sustain competitive operations and the divested facility deteriorates or closes---have undermined several past merger remedies. The Evanston Northwestern case (2007) and the ProMedica/St. Luke's divestiture illustrate both the promise and the pitfalls: structural relief works only when the divested hospital emerges as a viable, independently competitive institution.

Evaluating hospital merger remedies requires comparing post-merger prices and quality at the merged system against a credible counterfactual. Difference-in-differences designs using comparable hospitals in unaffected markets are the standard approach, following the methodology established in the merger retrospective literature [@ashenfelter_hosken_2010]. Key outcomes to track include commercial insurance negotiated rates, patient volume, quality metrics (readmission rates, patient safety indicators from CMS Hospital Compare), and physician staffing levels. The challenge is that post-merger integration effects take two to three years to materialize fully, as the merged system renegotiates insurer contracts, consolidates service lines, and adjusts staffing. This lag requires patience in evaluation design---studies conducted too early will underestimate the merger's price effects, while studies conducted too late may confound the merger effect with other market changes. Researchers should pre-register their evaluation design and control group selection to avoid ex post specification searching.

South Africa's proposed Supply-Side Regulator for Health takes a fundamentally different approach to the hospital market power problem: instead of case-by-case merger review, it would impose ongoing benchmarking and price regulation across the private hospital sector. The analytical tools from this chapter---cost benchmarking, yardstick competition, incentive regulation---would be directly applicable to such a regulator's operations. The critical question is whether a developing country's regulatory apparatus can sustain the data collection, technical capacity, and institutional independence that effective health sector regulation demands. International experience from the NHS in the UK (Monitor/NHS Improvement) and the German hospital planning system suggests that health sector regulation requires substantial investment in data infrastructure and clinical expertise within the regulatory body. Cross-reference [Chapter 10: Labor Markets](10-labor-markets.md) for related concerns about healthcare labor market concentration, which compounds the product-market power issues discussed here.

For practitioners, hospital mergers illustrate the full evidence triad in action. Quantitative WTP models and retrospective price studies provide the empirical backbone, establishing whether and by how much the merger increased prices. Insurer and physician testimony provides the qualitative dimension, explaining how bargaining dynamics actually work and whether the merged system leveraged its "must-have" status in contract negotiations. And internal strategy documents---particularly those discussing network essentiality, rate negotiation targets, and competitive positioning relative to rival systems---provide the documentary evidence that ties the quantitative and qualitative strands together. No single evidence stream is sufficient on its own; the strength of hospital merger cases lies in their convergence across all three.
{% endhint %}

## Callouts and qualitative evidence

{% hint style="info" %}
**Method box**
- Benchmarking models and productivity comparisons.
- Remedy simulations (cost/pass-through projections); see @davis_garces_2010 for quantitative implementation.
- Retrospective diff-in-diff and event studies on post-remedy outcomes [@angrist_pischke_2009; @cunningham_2021].
{% endhint %}

{% hint style="info" %}
**Qualitative evidence**
- Implementation plans, trustee reports, stakeholder workshops.  
- Regulator-stakeholder hearings and public comment summaries.  
- Operational feasibility memos from engineering or procurement teams.
{% endhint %}

{% hint style="info" %}
**Citations and comparative note**
- **Sector-specific regulators:** FCC/Ofcom (telecom), FERC/Ofgem (energy), NERSA/ICASA (South Africa). The South African regulatory framework operates under the Competition Act [@sa_competition_act_1998].
- **Theoretical foundations:** @tirole_1988 provides the industrial organization theory underlying regulation; @motta_2004 bridges theory and competition policy practice. Classic practitioner references include Kahn's *Economics of Regulation* and Vogelsang's work on price-cap design.
- **Merger remedy frameworks:** The US merger guidelines [@doj_ftc_hmg_2023; @doj_ftc_hmg_2010] and vertical merger guidelines [@doj_ftc_vmg_2020] discuss remedy design. The CMA's merger assessment guidelines [@cma_merger_assessment_2021] and EC horizontal merger guidelines [@ec_hmg_2004] provide the UK and EU frameworks, respectively.
- **Abuse-of-dominance guidance:** The EC's Article 102 enforcement priorities guidance [@ec_article102_guidance_2009] is relevant to access and pricing remedies.
{% endhint %}

## Visualizations

### Remedy compliance timeline
A timeline visualization helps communicate key milestones, deadlines, and compliance events for complex remedy packages. This is particularly useful for trustee reports, agency presentations, and public communications.

```r
source("program/R/helpers.R")
library(dplyr)
library(ggplot2)
library(lubridate)

# Example remedy timeline from a merger case
# Replace with actual compliance events from trustee reports
remedy_events <- tibble::tribble(
  ~date,              ~event,                               ~category,
  "2021-03-15",       "Merger approved w/ conditions",      "Decision",
  "2021-04-01",       "Trustee appointed",                  "Monitoring",
  "2021-07-01",       "Access API go-live",                 "Technical",
  "2021-09-30",       "Q1 compliance report",               "Reporting",
  "2021-12-01",       "Data sharing portal launched",       "Technical",
  "2021-12-31",       "Q2 compliance report",               "Reporting",
  "2022-03-15",       "First annual review",                "Review",
  "2022-06-30",       "Q3 compliance report",               "Reporting",
  "2022-09-01",       "Pricing parity audit",               "Monitoring",
  "2022-12-31",       "Q4 compliance report",               "Reporting",
  "2023-03-15",       "Second annual review",               "Review",
  "2023-06-01",       "Remedy modification hearing",        "Decision",
  "2024-03-15",       "Final compliance assessment",        "Review",
  "2024-06-30",       "Sunset date (remedy expires)",       "Termination"
) |>
  mutate(
    date = as.Date(date),
    category = factor(category,
                     levels = c("Decision", "Technical", "Monitoring",
                               "Reporting", "Review", "Termination"))
  )

# Create timeline plot with categorical coloring
ggplot(remedy_events, aes(x = date, y = 0)) +
  # Baseline
  geom_hline(yintercept = 0, color = "gray70", linewidth = 1) +
  # Event points
  geom_point(aes(color = category), size = 4) +
  # Event labels
  geom_text(aes(label = event, angle = 45),
            hjust = -0.1, vjust = -0.5, size = 3) +
  # Category coloring
  scale_color_manual(
    values = c(
      "Decision" = "#0072B2",
      "Technical" = "#009E73",
      "Monitoring" = "#F0E442",
      "Reporting" = "#999999",
      "Review" = "#D55E00",
      "Termination" = "#CC79A7"
    )
  ) +
  scale_x_date(date_breaks = "6 months", date_labels = "%b %Y",
               expand = expansion(mult = c(0.05, 0.05))) +
  labs(
    title = "Remedy Compliance Timeline",
    subtitle = "Tracking key milestones and reporting obligations",
    x = NULL,
    y = NULL,
    color = "Event Type",
    caption = "Example from merger conditional approval. Replace with actual compliance data."
  ) +
  theme_antitrust() +
  theme(
    axis.text.y = element_blank(),
    axis.ticks.y = element_blank(),
    panel.grid = element_blank(),
    plot.title.position = "plot",
    axis.text.x = element_text(angle = 45, hjust = 1),
    legend.position = "bottom"
  ) +
  coord_cartesian(ylim = c(-0.5, 1.5))

# Summary table
cat("\nCompliance milestone summary:\n")
remedy_summary <- remedy_events |>
  group_by(category) |>
  summarise(count = n(), .groups = "drop") |>
  arrange(desc(count))
print(remedy_summary, n = Inf)
```

**How to use this timeline:**
- **Decision events** (blue): Key regulatory or tribunal decisions establishing or modifying remedies.
- **Technical milestones** (green): System launches, API deployments, portal go-lives.
- **Monitoring events** (yellow): Audits, investigations, compliance checks.
- **Reporting obligations** (gray): Regular quarterly or annual reports.
- **Review points** (orange): Scheduled assessments where remedies may be modified or extended.
- **Termination** (purple): Sunset date when behavioral remedies expire.

**Practical applications:**
- Include in trustee reports to show progress against mandated milestones.
- Present in annual compliance reviews to agency staff.
- Use in public communications to demonstrate transparency.
- Adapt for different remedy types: structural (divestitures), behavioral (access, pricing), or hybrid packages.

Replace with actual dates from:
- Consent decrees and settlement agreements (DOJ/FTC, DG COMP, CMA)
- Trustee reports and compliance dashboards
- Agency monitoring databases
- Tribunal orders (South African Competition Tribunal)

### Enhanced timeline with swimlanes
For complex remedies involving multiple workstreams (technical, legal, operational), use a swimlane variant:

```r
library(ggplot2)
library(dplyr)

# Add swimlane assignments
remedy_events_swim <- remedy_events |>
  mutate(
    swimlane = case_when(
      category %in% c("Decision", "Termination") ~ "Legal/Regulatory",
      category %in% c("Technical") ~ "Technical Implementation",
      category %in% c("Monitoring", "Review") ~ "Compliance & Audit",
      category == "Reporting" ~ "Reporting & Documentation"
    ),
    swimlane = factor(swimlane,
                     levels = c("Legal/Regulatory",
                               "Technical Implementation",
                               "Compliance & Audit",
                               "Reporting & Documentation"))
  )

ggplot(remedy_events_swim, aes(x = date, y = as.numeric(swimlane))) +
  # Swimlane backgrounds
  geom_rect(aes(fill = swimlane),
            xmin = min(remedy_events_swim$date) - days(30),
            xmax = max(remedy_events_swim$date) + days(30),
            ymin = as.numeric(remedy_events_swim$swimlane) - 0.4,
            ymax = as.numeric(remedy_events_swim$swimlane) + 0.4,
            alpha = 0.1) +
  # Event points
  geom_point(aes(color = category), size = 4) +
  # Event labels
  geom_text(aes(label = format(date, "%b %y")),
            nudge_y = 0.15, size = 2.5, fontface = "bold") +
  geom_text(aes(label = event),
            nudge_y = -0.15, size = 2.5, hjust = 0.5) +
  scale_color_manual(
    values = c(
      "Decision" = "#0072B2",
      "Technical" = "#009E73",
      "Monitoring" = "#F0E442",
      "Reporting" = "#999999",
      "Review" = "#D55E00",
      "Termination" = "#CC79A7"
    )
  ) +
  scale_fill_manual(
    values = c(
      "Legal/Regulatory" = "#0072B2",
      "Technical Implementation" = "#009E73",
      "Compliance & Audit" = "#D55E00",
      "Reporting & Documentation" = "#999999"
    )
  ) +
  scale_y_continuous(
    breaks = 1:4,
    labels = levels(remedy_events_swim$swimlane)
  ) +
  scale_x_date(date_breaks = "6 months", date_labels = "%b %Y") +
  labs(
    title = "Remedy Compliance Timeline (Swimlane View)",
    subtitle = "Organized by workstream to track parallel activities",
    x = NULL,
    y = NULL,
    color = "Event Type",
    fill = "Workstream"
  ) +
  theme_antitrust() +
  theme(
    plot.title.position = "plot",
    axis.text.x = element_text(angle = 45, hjust = 1),
    legend.position = "bottom",
    panel.grid.minor = element_blank(),
    panel.grid.major.x = element_line(color = "#e0e0e0", linewidth = 0.3)
  ) +
  guides(fill = "none")
```

**Swimlane benefits:**
- Separates legal, technical, and operational workstreams for clarity.
- Shows dependencies and sequencing across different teams.
- Useful for program management and stakeholder coordination.

## Exercises

1. **Conceptual.** Explain the Averch-Johnson effect. A regulated electric utility proposes a $500 million capital investment in smart grid technology. What questions should the regulator ask to determine whether the investment is prudent or gold-plating?

2. **Data/code.** Using the benchmarking scatter code in this chapter, add 5 more hypothetical utilities with varying opex and quality scores. Fit a frontier (linear regression) and identify which utilities are "above the line" (efficient) vs. "below the line" (inefficient). How could a regulator use this information to set X-factors?

3. **Case discussion.** The South African Data Services Market Inquiry resulted in voluntary price commitments rather than binding regulation. What are the advantages and disadvantages of voluntary commitments vs. formal price-cap regulation? Under what conditions might commitments be more effective?

4. **Conceptual.** Design a compliance scorecard for a behavioral remedy requiring a dominant platform to provide API access to third-party developers on non-discriminatory terms. Specify: 4 KPIs, reporting frequency, escalation triggers, and sunset conditions.

5. **Conceptual.** Compare structural vs. behavioral remedies for a horizontal hospital merger that would create a must-have system in a metropolitan area. What are the key considerations for each approach, and which would you recommend? Justify your answer.

## Looking ahead
The remedy design and evaluation tools developed here connect directly to the chapters ahead. [Chapter 9: Digital Markets](09-digital-markets.md) applies access mandates, fair-ranking obligations, and interoperability remedies to platform markets---obligations codified in instruments such as the EU Digital Markets Act [@eu_dma_2022]---contexts where behavioral remedies and ongoing monitoring are especially important. [Chapter 12: Litigation Practice](12-litigation-practice.md) covers how to present remedy compliance evidence in expert reports and how retrospective evaluations feed into damages proceedings. As you encounter new cases, consider which remedy type---structural, behavioral, or hybrid---best matches the diagnosed harm, and how the benchmarking and diff-in-diff frameworks from this chapter can assess whether the remedy is working.
