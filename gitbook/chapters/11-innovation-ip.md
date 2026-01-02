# Innovation, Intellectual Property, and Antitrust

## Learning goals
Innovation cases require translating R&D pipelines, patent portfolios, and technical standards into competition narratives. This chapter shows how to:

- Evaluate SEPs/FRAND licensing, patent pools, and interoperability disputes.
- Analyze pay-for-delay/reverse-payment settlements and innovation-reducing mergers.
- Combine patent data (counts, citations, claim breadth), R&D metrics, and technical evidence (roadmaps, standards submissions).
- Integrate qualitative expert testimony with econometric and event-study evidence.

## Core topics
- SEPs/FRAND licensing economics; hold-up vs. hold-out.
- Pay-for-delay: economic characterization, entry timing, consumer harm.
- Innovation measures: patent counts/citations, R&D spend, pipeline probability.
- Interoperability and standards; access to APIs and data.
- Remedy design: FRAND commitments, compulsory licensing, data/technology access, behavioral constraints on reverse payments.

{% hint style="info" %}
**Method box**

- Event studies on patent pool or settlement announcements.
- Entry timing models for generics; hazard/survival sketches.
- R&D response to merger or remedy using panel FE.
{% endhint %}

{% hint style="info" %}
**Qualitative evidence**

- Technical expert declarations, standards body submissions, patent essentiality reviews.
- Licensing negotiations, term sheets, audit rights.
- Product roadmaps and engineering constraints.
{% endhint %}

{% hint style="info" %}
**Citations and comparative note**

- Cite FRAND/SEP cases and guidance (e.g., EU Huawei v. ZTE, US FTC/DOJ policy statements, UK FRAND rate cases).
- For pay-for-delay, reference US Supreme Court (Actavis) and EU pay-for-delay decisions.
- Include patent data sources (USPTO, EPO, JPO, CNIPA) and note differences in treatment of injunctions and remedies across jurisdictions.
{% endhint %}

## SEPs, FRAND, and standard setting

### Market power and hold-up vs. hold-out
Standard-essential patents (SEPs) can confer significant bargaining leverage once a standard is adopted. Distinguish:

- **Hold-up:** SEP holder extracts supra-FRAND royalties by threatening injunctions after firms are locked into the standard (Lemley and Shapiro, 2007).
- **Hold-out:** Implementers delay or underpay royalties despite benefiting from the standard.

For economic analysis of patent holdup and royalty stacking, see Shapiro (2001) and Farrell, Hayes, Shapiro, and Sullivan (2007).

Evidence sources:

- Standards body submissions (ETSI, IEEE, 3GPP) and FRAND commitments.
- Essentiality assessments (self-declared vs. independent).
- Licensing histories, audit trails, and comparable agreements.

**Key SEP/FRAND cases:**

- **EU *Huawei v. ZTE* (2015):** Established framework for when SEP holders may seek injunctions—requiring good-faith negotiations, FRAND offers, and willingness to license before injunctive relief is appropriate.
- **UK *Unwired Planet* (2020):** Court determined global FRAND rates across patent portfolio; established precedent for courts setting rates when parties cannot agree.
- **FTC v. Qualcomm (2019-2020):** The FTC alleged Qualcomm used its SEP position and chip monopoly to extract supracompetitive royalties through "no license, no chips" policies. The district court found antitrust violations, but the Ninth Circuit reversed, holding that Qualcomm's practices—even if anticompetitive in licensing markets—did not harm competition in chip markets. The case highlights difficulties in applying antitrust to SEP licensing and the importance of identifying the correct market for harm analysis.
- **EC Qualcomm decisions (2018-2019):** The Commission fined Qualcomm for predatory pricing to exclude Icera and for exclusivity payments to Apple, demonstrating EU willingness to pursue SEP-adjacent conduct.

These cases illustrate jurisdictional divergence: EU authorities more readily pursue SEP-related antitrust claims, while US courts after *Qualcomm* require clearer links between licensing conduct and competitive harm.

### Royalty stack analysis
```r
library(dplyr)
library(ggplot2)
source("../program/R/helpers.R")

stack <- tibble::tribble(
  ~component, ~royalty_percent,
  "Baseband", 1.5,
  "Display", 0.8,
  "Camera", 0.5,
  "OS/API", 0.7,
  "Other SEPs", 1.0
)

ggplot(stack, aes(x = "", y = royalty_percent, fill = component)) +
  geom_col(width = 0.5) +
  coord_polar("y") +
  labs(
    title = "Illustrative royalty stack",
    subtitle = "Replace with FRAND negotiation data when available",
    y = "Royalty (% of device price)",
    x = NULL,
    fill = NULL
  ) +
  theme_void()
```
Replace the illustrative stack with licensing data (often produced during litigation) or sanitized aggregates from public FRAND rate determinations. Cite FRAND rate determinations (e.g., UK Unwired Planet, Optis) for benchmarking, which are available through court records.

### Event study for injunction announcements
```r
library(tidyquant)
library(dplyr)
library(ggplot2)

# Use tidyquant to pull SEP-holder and implementer stocks; measure CAR around injunction or settlement announcements
# event_date <- as.Date("2021-08-27")
# tickers <- c("QCOM","AAPL","SSNLF","SPY")
# prices <- tq_get(tickers, from = event_date - 120, to = event_date + 60) |> ...
```
Use `tidyquant` with actual ticker lists; cite the docket (e.g., “Optis v. Apple FRAND decision”) in the narrative.

## Pay-for-delay and reverse payments

### Entry timing and hazard models
Reverse-payment settlements can delay generic entry and harm consumers (*FTC v. Actavis*, 2013). Analyze:

- **Payment size:** Compare settlement payment to expected litigation costs and projected profits (Edlin and Hemphill, 2013).
- **Entry timing:** Use survival models or diff-in-diff to estimate delay relative to counterfactuals.
- **Price effects:** Simulate price paths with and without generic entry (Scott Morton, 2000; Hemphill and Sampat, 2012).

```r
library(survival)

# synthetic example
data <- tibble::tribble(
  ~drug, ~entry_year, ~settlement, ~status,
  "DrugA", 2020, 1, 1,
  "DrugB", 2018, 0, 1,
  "DrugC", 2022, 1, 0
)

# survival::survfit(Surv(entry_year, status) ~ settlement, data = data)
```
Replace with real pay-for-delay cases (Actavis-style) or EU decisions (Servier, Lundbeck). Use FDA Orange Book, EMA data, or South African SAMRC filings for entry timelines.

### Diff-in-diff for price effects
```r
library(fixest)

# panel columns: market, year, treated (1 if affected by settlement), price_index
# did_model <- feols(price_index ~ treated | market + year, data = panel)
# summary(did_model)
```
Data sources: IQVIA (if available), CMS reimbursement data, Stats SA medicine price data, or public price registries.

## Innovation effects of mergers or conduct

- **Patent/R&D panels:** Compile patent counts (PatentsView, EPO PATSTAT), citation-weighted measures, and R&D spending to evaluate innovation incentives pre/post merger or remedy.  
- **Pipeline probability models:** For pharmaceuticals, use clinical trial progression rates.  
- **Product roadmaps:** Qualitative review of technical plans to confirm or rebut innovation harm narratives.

### Panel FE scaffold
```r
library(fixest)

# panel columns: firm, year, rd_spend, merger_dummy, controls
# rd_model <- feols(log(rd_spend) ~ merger_dummy + controls | firm + year, data = panel)
# summary(rd_model)
```

### Killer acquisitions

"Killer acquisitions" occur when an incumbent acquires a nascent competitor specifically to discontinue its innovation pipeline, eliminating a competitive threat rather than realizing synergies (Cunningham, Ederer, and Ma, 2021). These transactions often fall below merger notification thresholds, allowing them to proceed without antitrust review.

**Empirical identification:**

1. **Pipeline discontinuation rates:** Compare probability that acquired projects are discontinued vs. comparable projects at independent firms. Cunningham et al. (2021) find 5-7% of pharma acquisitions are "killer" in this sense.
2. **Overlap analysis:** Higher discontinuation rates for targets whose pipelines overlap with acquirer's marketed products suggest elimination of competition.
3. **Post-acquisition R&D:** Track whether acquirer shifts resources away from the target's development programs.

**Key metrics:**

| Indicator | Measurement | Data source |
|:----------|:------------|:------------|
| Pipeline overlap | % therapeutic areas in common | Clinical trials databases, patent filings |
| Discontinuation rate | % acquired projects discontinued | FDA/EMA filings, company announcements |
| Development timeline | Delay in milestone achievement | Clinical trial phase transitions |
| R&D reallocation | Post-acquisition spending shifts | SEC filings, segment disclosures |

**Remedies and policy responses:**

- **Expanded notification thresholds:** Several jurisdictions now require notification based on transaction value (not just target revenue), capturing high-value acquisitions of pre-revenue startups.
- **Continuation requirements:** Behavioral remedies may require the acquirer to continue development of acquired pipeline assets for a specified period.
- **Periodic reporting:** Monitor development milestones post-acquisition to detect strategic discontinuation.

For pharmaceutical and biotech markets, cross-reference FDA and EMA clinical trial databases with acquisition announcements. For technology markets, track product launches, API deprecations, and talent retention post-acquisition.

## Interoperability and data access

Analyze API access restrictions, data sharing, and interoperability constraints:

- **API logs:** Compare response times, rate limits, and feature parity between internal and external developers.  
- **Data portability metrics:** Evaluate export completeness, frequency, and latency.  
- **Technical documentation:** PRDs and engineering tickets often show intent to foreclose or degrade rivals.

## Southern African innovation/IP examples
- **Telkom vs. Internet Solutions (broadband IP).** Access to APIs and OSS/BSS systems under FRAND-like commitments; margin squeeze tests combined with technical audits.  
- **Vodacom Zero-Rating commitments (data services inquiry).** Interoperability obligations for educational content, showing how innovation incentives can align with public-interest remedies.  
- **Pharma patent settlements (Competition Commission investigations into ARV markets).** Settlement analysis combining SAMRC price data, patent landscapes, and clinical trial timelines to assess delay and innovation impact.

## Enhanced Visualizations

### Enhanced royalty stack waterfall
A more detailed royalty stack showing how cumulative royalties build up across different technology components. This helps demonstrate potential royalty stack concerns in FRAND disputes.

![Royalty Stack Waterfall: Smartphone Example](../images/innovation-royalty-waterfall-1.png)

*Waterfall showing cumulative royalty burden from device price (100%) down to net manufacturer margin. Color indicates royalty type (SEP, patent pool, non-SEP, license).*

**Key concerns:**
- **Royalty stacking**: Multiple SEP holders each claiming a "reasonable" royalty can collectively make manufacturing unprofitable.
- **Double marginalization**: Each layer adds its markup, raising final prices.
- **Hold-up**: Once committed to a standard, manufacturers face switching costs that weaken bargaining position.

**Benchmarking:**
Compare against FRAND rate determinations:
- UK Unwired Planet v. Huawei (2017)
- UK Optis v. Apple (2023)
- US Ericsson v. Samsung arbitration

### Generic entry survival curve
Analyze the timing of generic pharmaceutical entry, with and without reverse payment settlements. Survival analysis shows whether settlements delay entry.

![Generic Entry Timing: Impact of Reverse Payment Settlements](../images/innovation-generic-entry-1.png)

*Kaplan-Meier survival curves showing probability of no generic entry over time. Drugs with reverse payment settlements show systematically delayed entry.*

**Interpretation:**
- **Separation of curves**: If settlement drugs show consistently lower entry hazard, this suggests anticompetitive delay.
- **Median delay**: Calculate months of delay attributable to settlements.
- **Consumer harm**: Combine with price differentials (branded vs. generic) to estimate consumer losses.

**Data sources:**
- **FDA Orange Book**: [fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files](https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files)
- **EMA**: European Medicines Agency public assessment reports
- **SAHPRA**: South African Health Products Regulatory Authority
- **FTC settlements**: Public records of reverse payment cases

### Patent citation network
Visualize how key patents cite each other to show technological relationships and potential blocking positions.

![Patent Citation Network](../images/innovation-patent-network-1.png)

*Network graph showing patent citations. Node size = citation count (in-degree); color = patent holder; shape = SEP vs. non-SEP.*

**Key insights:**
- **Central patents**: High betweenness centrality indicates "bottleneck" patents that many others depend on.
- **Patent thickets**: Dense clusters suggest overlapping IP that may impede innovation.
- **Holder concentration**: If one firm controls many central patents, it may have market power.

### R&D spending event study around merger
Evaluate whether mergers affect innovation incentives by tracking R&D spending before and after the transaction.

![R&D Spending Around Merger Event](../images/innovation-rd-event-1.png)

*Time series showing R&D spending indexed to 100 at merger announcement. Merged firms show decline relative to non-merged rivals post-merger.*

**Interpretation:**
- **Pre-trends**: Parallel trends before merger support DiD identification.
- **Treatment effect**: Negative coefficient suggests merger reduced R&D.
- **Innovation harm**: Combine with patent output, clinical trials, or product launches to assess real-world impact.

**Alternative specifications:**
- Event study with leads/lags
- Synthetic control for single-firm mergers
- Stacked DiD for multiple mergers

### Clinical trial pipeline visualization (pharmaceuticals)
Track clinical trial progress for pharmaceutical innovation assessments.

![Clinical Trial Pipeline Comparison](../images/innovation-clinical-pipeline-1.png)

*Bar chart showing number of compounds by development stage (preclinical through approved) for three firms.*

**Applications:**
- **Merger review**: Compare pipeline depth before/after transaction.
- **Pay-for-delay**: Estimate lost innovation from delayed generic competition.
- **Market foreclosure**: Show whether conduct reduces rivals' pipeline.

**Data sources:**
- **ClinicalTrials.gov**: US clinical trial registry
- **EU Clinical Trials Register**: European trials
- **WHO ICTRP**: International registry
- **Company pipelines**: Annual reports and R&D presentations

## Visualizations and data sourcing
- **Royalty stack:** Use licensing disclosures from litigation or FRAND rate decisions. If unavailable, maintain illustrative stack in `data/examples/royalty_stack.csv`.
- **Entry timing survival curves:** [FDA Orange Book](https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files), EMA, SAHPRA, or competition-inquiry appendices.
- **FRAND injunction event plots:** `tidyquant` stock data; ensure tickers are mapped to key SEP holders and implementers.
- **Patent pipeline ridge plot:** Pull [PatentsView](https://patentsview.org/) or [EPO PATSTAT](https://www.epo.org/searching-for-patents/business/patstat.html) data; store sanitized extracts and scripts in `data/derived/innovation/`.

Document data provenance and confidentiality in `data/README.md`, noting which visuals can ship publicly and which require synthetic placeholders until case data is approved for release.

## Looking ahead
Archive all innovation analyses in `data/derived/innovation/` with clear metadata. When PatentsView bulk downloads or FDA Orange Book data become available, replace synthetic patent networks and entry curves with actual data. Cross-reference R&D event studies with Chapter 06 (mergers) and Chapter 08 (remedies) for remedy design templates. Document technical expert declarations and standards body submissions in case chronologies for litigation support.
