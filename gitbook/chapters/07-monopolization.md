# Monopolization and Exclusion

## Learning goals
- Analyze exclusionary conduct (predation, rebates, tying, MFNs, vertical restraints).
- Connect theory to measurable foreclosure and consumer harm.
- Use qualitative evidence to show strategy and intent, paired with empirical outcomes.

## Core topics
- Price-cost tests (Areeda-Turner variants), effective price with rebates/loyalty programs.
- Foreclosure metrics: share of market foreclosed, rivals' scale and entry conditions.
- Tying/bundling: uptake, defaults, switching costs, interoperability constraints.
- MFNs/parity: price dispersion effects, platform fee pass-through.
- Workflow: (1) conduct and theory of harm; (2) market power assessment; (3) mechanism (exclusion/predation/raising rivals' costs); (4) empirical effects; (5) countervailing efficiencies/justifications; (6) remedy fit.

## Introduction

Monopolization analysis sits at the intersection of conduct, market structure, and effects. Unlike merger review—which evaluates a prospective transaction—monopolization cases reconstruct historical patterns of behavior and ask whether a dominant firm has maintained or extended its position through exclusionary means rather than through competition on the merits. Section 2 of the Sherman Act in the United States and Article 102 of the Treaty on the Functioning of the European Union (TFEU) frame the legal standards, but enforcement priorities and evidentiary approaches differ substantially across jurisdictions.

This chapter provides a structured workflow for analyzing monopolization claims. We begin with market power assessment, drawing on tools from Chapter 3 (market definition) and Chapter 4 (IO toolkit). We then turn to specific conduct categories—predation, rebates and loyalty programs, tying and bundling, most-favored-nation clauses, vertical restraints, and refusal to deal. For each, we pair theoretical mechanisms with empirical measurement strategies and qualitative evidence that together build a coherent narrative. The chapter concludes with remedy design considerations and a set of case exemplars that illustrate how different jurisdictions approach the same exclusionary practices.

Throughout, we emphasize reproducibility and transparency. Code boxes demonstrate how to compute effective prices, assess foreclosure shares, and visualize event patterns around contract adoptions. Qualitative evidence boxes highlight the documentary and testimonial sources that complement quantitative analyses. Case boxes anchor abstract principles in real enforcement actions, drawing on landmark decisions from the United States, European Union, and Southern Africa.

For deeper context, consult the extensive case law on exclusionary conduct, including landmark decisions like *United States v. Microsoft* (2001) and the European Commission's decisions on abuse of dominance (EC Guidance on Article 102, 2009). For theoretical foundations, see Whinston (2006) and Salop and Scheffman (1983) on raising rivals' costs.

## Market power and the monopolization workflow

### Establishing market power

Monopolization liability begins with market power. In the United States, courts typically require monopoly power—the ability to control prices or exclude competition—which is often proxied by a sustained market share above 60–70% in a properly defined relevant market (*Grinnell*, 1966). The European Union applies a lower threshold for dominance under Article 102 TFEU, with shares as low as 40% potentially qualifying when combined with barriers to entry and expansion (*AKZO*, 1991; *United Brands*, 1978). These quantitative thresholds, however, must be buttressed by evidence of entry conditions, buyer power, and the duration of the firm's position.

**Quantitative indicators** include:

1. **Market shares**: Compute shares by revenue, volume, or capacity over multiple periods to demonstrate persistence. Use granular data (SKU-level, route-level, or platform-specific shares) when available. Cross-check shares against customer perceptions and bidding data.
2. **Entry conditions**: Examine regulatory barriers, network effects, switching costs, and capital requirements. Quantify entry attempts and failures; use survival analyses or hazard models to assess entry likelihood.
3. **Buyer power**: Assess whether large customers can sponsor entry or credibly threaten backward integration. Use procurement data and contract terms to gauge buyer negotiating leverage.

**Qualitative indicators** reinforce these metrics:

- Internal documents describing the firm as "must-have" or discussing the consequences of losing access to the product.
- Customer interviews and surveys that reveal switching frictions or lack of acceptable alternatives.
- Board materials and strategic memos that acknowledge or plan around market power (e.g., pricing flexibility, entry deterrence strategies).

Together, these elements establish the baseline condition for monopolization: a firm with durable market power and the incentive to maintain or extend it.

### Articulating the theory of harm

Once market power is established, the analysis turns to conduct. Monopolization theories fall into several categories:

1. **Predatory pricing**: pricing below cost to drive out rivals or deter entry, with a credible prospect of recouping losses through higher prices later.
2. **Exclusive dealing and loyalty rebates**: contracts or pricing structures that foreclose a substantial share of the market to rivals, raising their costs or denying them minimum efficient scale.
3. **Tying and bundling**: leveraging dominance in one market to disadvantage rivals in another, either through contractual ties or technical integration (e.g., defaults, degraded interoperability).
4. **Most-favored-nation (MFN) clauses**: contractual provisions that prevent trading partners from offering better terms elsewhere, chilling price competition and entrenching the dominant firm's position.
5. **Self-preferencing and vertical restraints**: a vertically integrated firm favoring its own downstream products over rivals' offerings on its platform or distribution network.
6. **Refusal to deal or denial of access**: withholding an essential input or interoperability without a legitimate business justification, where access is indispensable for rivals to compete.

Each theory requires alignment between the conduct, the mechanism of harm, and the expected effects. Align the data collection and empirical strategy to the specific mechanism: if the claim is that loyalty rebates foreclose rivals, measure the share of volume or capacity covered by the contracts and assess whether foreclosed volumes prevent rivals from reaching minimum efficient scale. If the claim is predatory pricing, compute effective prices net of rebates and compare to measures of avoidable or incremental cost, then model recoupment scenarios.

### Workflow summary

A complete monopolization analysis typically follows this sequence:

1. **Conduct description and theory of harm**: Document the challenged behavior (contracts, pricing, technical design) and articulate the exclusionary mechanism.
2. **Market power assessment**: Establish market shares, entry barriers, and buyer power with both quantitative and qualitative evidence.
3. **Mechanism and foreclosure**: Quantify the scope of foreclosure (volume, duration, exclusivity) and assess whether rivals are denied minimum efficient scale or face raised costs.
4. **Empirical effects**: Use natural experiments, event studies, or before/after comparisons to measure price, output, quality, or entry/exit effects attributable to the conduct.
5. **Efficiencies and justifications**: Evaluate procompetitive rationales (cost savings, quality improvements, incentive alignment) and whether less-restrictive alternatives are feasible.
6. **Remedies**: Design conduct or structural remedies that target the exclusionary mechanism without unduly chilling procompetitive conduct; specify monitoring and compliance requirements.

The remainder of this chapter elaborates on each conduct category, pairing theory with empirical methods and qualitative evidence.

## Exclusive dealing, loyalty rebates, and foreclosure

### Measuring foreclosure

Exclusive dealing and loyalty rebate programs aim to lock in a substantial share of customer demand, making it difficult or unprofitable for rivals to achieve minimum efficient scale. The central empirical question is: what share of the market is foreclosed, and for how long?

**Foreclosure metrics** include:

1. **Volume or capacity shares covered**: Sum the total volumes or capacities bound by exclusive or loyalty contracts as a percentage of total market demand. A foreclosure share above 40–50% may raise concerns, particularly if contracts are long-duration and staggered so that only a small fraction comes up for renewal in any given period.
2. **Minimum efficient scale (MES)**: Estimate the scale needed for rivals to compete effectively (e.g., plant capacity, distribution network density, platform-side critical mass). If the foreclosed share leaves rivals below MES, the conduct is more likely exclusionary.
3. **Contract duration and staggering**: Long-term contracts with staggered renewal dates can perpetuate foreclosure even if individual contracts expire. Quantify the fraction of demand available for contestation in each period.
4. **Exit and entry patterns**: Document whether rivals have exited or delayed entry coinciding with contract rollouts; use hazard models or event studies to link conduct to competitive structure.

**Effective price analysis for loyalty rebates**: Loyalty rebates condition discounts on purchasing all or a substantial share of requirements from the dominant firm. The effective price for incremental units—those that push the buyer over the loyalty threshold—can be significantly below the headline price, making it unprofitable for rivals to compete even if their costs are comparable.

To compute effective prices:

- Identify the rebate threshold (e.g., purchase 80% of requirements to qualify for a 10% rebate).
- Calculate the marginal benefit of reaching the threshold: if a buyer purchases 95 units at the list price and buying 5 more units triggers a 10% rebate on all 100 units, the effective price of those last 5 units is deeply negative.
- Compare effective prices to rivals' costs or list prices to assess whether contestation is feasible.

The European Commission's Intel decision (*Intel*, 2017) applied a version of this test, focusing on whether the rebates made it unprofitable for AMD to compete for incremental volumes even when AMD's products were technically competitive. The as-efficient competitor (AEC) test, refined post-Intel, requires showing that an equally efficient rival would be foreclosed.

#### Effective price waterfall for loyalty rebates

The following visualization demonstrates how loyalty rebates can create deeply negative effective prices for incremental units, making it unprofitable for equally efficient rivals to compete. This implements the as-efficient competitor (AEC) test framework used in EU competition enforcement.

![Effective Price Waterfall Under Retroactive Loyalty Rebate](../images/monopoly-effective-price-waterfall-1.png)

*Top panel: Waterfall showing how retroactive rebates create deeply negative effective prices for marginal units. Bottom panel: Market share evolution showing rivals losing share after loyalty contracts introduced.*

**Data replacement:** Use actual customer purchase data and contract terms from litigation discovery. Calculate effective prices per customer segment; overlay rival cost estimates from cost studies or public financial statements. For share evolution, use market monitoring data or customer panel data tracking purchases before/after contract adoption.

**As-efficient competitor (AEC) test:** The waterfall shows that even an equally efficient rival (cost = $75) cannot profitably compete for the marginal units that trigger the rebate, as the effective price faced by the customer is deeply negative. This satisfies the AEC framework established in *Intel* (2017) and subsequent EU enforcement.

### Qualitative evidence for rebates and exclusivity

Internal documents and customer testimony are critical complements to quantitative foreclosure metrics:

- **Strategy memos**: Documents revealing intent to foreclose rivals or lock in customers (e.g., "ensure [Rival] cannot reach scale," "defend our share through loyalty programs").
- **Contract negotiation histories**: Email chains and drafts showing how exclusivity or loyalty terms were introduced, customer resistance, and adjustments to overcome objections.
- **Customer interviews**: Testimony on switching costs, the importance of multi-sourcing for resilience, and coercion (explicit or implicit) to accept exclusive terms.
- **Sales force incentives**: Compensation structures that reward exclusivity or penalize customers who multi-source.

In the United States, the rule of reason standard for exclusive dealing (under Section 1 or Section 2) often weighs these qualitative factors heavily, looking for evidence that foreclosure was the purpose rather than a byproduct of legitimate incentives (*Tampa Electric*, 1961). For economic analysis of exclusive dealing, see Whinston (2006) and Ordover, Saloner, and Salop (1990) on vertical foreclosure.

### Event studies and staggered rollouts

If exclusive contracts or loyalty programs were introduced or renewed in a staggered fashion across regions, customers, or time periods, treat the rollout as a natural experiment:

1. Define treatment as the adoption of the contract or rebate program; define control customers or regions without contracts.
2. Use difference-in-differences with appropriate controls for pre-existing trends in customer purchasing patterns.
3. Examine outcomes such as rival market shares, entry/exit events, or prices paid to rivals.
4. Visualize event study coefficients to show dynamic effects before and after contract adoption.

When data are thin, simpler before/after comparisons combined with robust documentary evidence can still be persuasive. The key is transparency about identification assumptions and potential confounders.

> **Data tip:** For visuals in the roadmap (effective price waterfall, foreclosure share, rollout event analysis), start with sanitized versions of the loyalty-contract spreadsheets and rolling rollout trackers. Where you lack live case data, use synthetic templates in `data/examples/` so the Quarto build renders without confidential inputs; swap in case data during litigation prep.

#### Contract rollout event study

When exclusive contracts are adopted in staggered fashion across customers or regions, event study methods can isolate the causal effect of foreclosure on rival performance.

![Contract Rollout Event Study](../images/monopoly-contract-rollout-event-1.png)

*Top panel: Event study coefficients showing no pre-trend and sharp decline post-adoption. Bottom panel: Individual customer trajectories showing rival share drops after exclusive contracts adopted.*

**Interpretation:** The event study coefficients show no pre-trend (flat estimates in periods -11 to -1), providing support for the parallel trends assumption. Post-adoption, rival share drops by ~8 percentage points, consistent with foreclosure. The individual trajectories confirm the aggregate pattern and reveal heterogeneity in treatment effects across customers.

**Data replacement:** Use customer-level purchase data with precise contract adoption dates. Estimate event studies separately for different contract types (exclusive vs. loyalty rebates) or customer segments. If contracts are truly staggered (different customers adopt at different times), use `fixest::sunab()` for heterogeneity-robust estimation (Callaway and Sant'Anna, 2021).

## Predatory pricing

### The price-cost test

Predatory pricing claims allege that a dominant firm sets prices below an appropriate measure of cost to drive out rivals or deter entry, with the expectation of recouping losses through supracompetitive prices once competition is eliminated. The canonical legal test, articulated in *Brooke Group* (1993), requires (1) pricing below an appropriate measure of cost, and (2) a dangerous probability of recouping the investment in below-cost pricing. The foundational economic framework was established by Areeda and Turner (1975).

**Cost benchmarks** in antitrust analysis include:

1. **Average variable cost (AVC)**: Costs that vary with output in the short run (materials, direct labor). Pricing below AVC is presumptively predatory under *Areeda-Turner* logic, as no rational profit-maximizing firm would price below AVC absent an exclusionary motive.
2. **Average avoidable cost (AAC)**: Costs that could be avoided by not producing (similar to AVC but may include some fixed costs avoidable in the medium term). AAC is increasingly favored in both US and EU practice as a more accurate measure of incremental cost.
3. **Long-run incremental cost (LRIC)** or **average total cost (ATC)**: Includes allocated fixed costs. Pricing between AAC and ATC may be exclusionary if combined with evidence of predatory intent and foreclosure effects, but is less likely to satisfy the *Brooke Group* standard in the United States.

**Computing effective prices**: When rebates, bundling, or loyalty discounts are present, compute the effective price paid per unit:

- If a customer receives a retroactive rebate upon reaching a volume threshold, the effective price for marginal units near the threshold can be far below the list price.
- Allocate fixed fees, upfront payments, or bundled-product discounts transparently across the relevant units.
- Use period-level data (monthly or quarterly) to capture the timing of rebates and costs.

**Recoupment analysis**: Even if prices are below cost, predation liability in the United States requires showing a dangerous probability of recoupment—that the predator can later raise prices to recover its losses. Assess recoupment by:

- Modeling post-exit pricing power: shares, entry barriers, and coordinated interaction prospects.
- Estimating the duration and magnitude of below-cost pricing and the time needed to recoup at elevated prices.
- Examining documents that discuss post-exit pricing strategies or barriers that would prevent re-entry.

The European Union historically placed less emphasis on explicit recoupment proofs, focusing instead on the exclusionary effect and intent. However, post-*Intel*, EU enforcers increasingly apply an as-efficient competitor framework that implicitly considers recoupment by asking whether exclusion harms consumers (*Intel*, 2017; *Post Danmark*, 2012).

### Event patterns and qualitative evidence

Where price-cost tests are ambiguous—prices near AAC, cost allocation disputes, or multi-product settings—qualitative evidence and event patterns become dispositive:

- **Documents on strategy**: Emails or memos discussing "pricing [Rival] out of the market," "losing money to gain share," or "invest now, recoup later."
- **Entry and exit timing**: Did rivals exit or delay entry during the alleged predation period? Use survival analysis or simple event timelines.
- **Share and capacity shifts**: Plot market shares and capacity utilization over time; sharp increases in the alleged predator's share coinciding with rival exits support the predation narrative.
- **Subsequent price increases**: If prices rose significantly after rivals exited, recoupment is more plausible. Use difference-in-differences with unaffected markets as controls to isolate the predation effect.

In the EU *AKZO* case (1991), internal documents referencing a plan to eliminate a competitor were central to the finding of abuse, even though the price-cost analysis was contested. Similarly, in the Southern African *Media24* case (discussed earlier), predatory intent combined with below-cost pricing over an extended period led to liability.

## Tying, bundling, and technical integration

### Mechanisms and measurement

Tying occurs when a seller conditions the sale of one product (the tying product, in which the seller has market power) on the purchase of another product (the tied product). Bundling offers a package of products together, often at a discount relative to standalone prices. Both practices can be exclusionary if they leverage market power in one market to foreclose rivals in another.

**Theories of harm** include:

1. **Volume foreclosure**: If most customers buy the bundle or accept the tie, rivals in the tied market lose scale and face higher per-unit costs.
2. **Technical foreclosure**: Integration or defaults make it costly or cumbersome to use a rival's tied product (e.g., degraded APIs, interoperability limits, removal of user choice screens).
3. **Price discrimination**: Bundling can be a tool for extracting surplus from heterogeneous customers, which is not per se harmful but may facilitate exclusion if it raises rivals' costs or denies them profitable customer segments.

**Empirical assessments** should measure:

- **Take-up rates**: What share of customers buy the bundle or accept the tie? Compare take-up in settings with and without the tie/bundle (across regions, time periods, or customer segments).
- **Switching costs and defaults**: If the tied product is set as the default, measure the rate at which customers switch away. Low switching rates may indicate either high satisfaction or high frictions.
- **Rival performance**: Has the tie/bundle coincided with rival exit, reduced market shares, or diminished investment? Use event studies or difference-in-differences where tie/bundle rollouts vary across markets or time.
- **Quality and feature parity**: Has the integrated product received features, performance, or API access advantages relative to standalone rivals? Use A/B tests, user experience data, or technical benchmarks.

### Efficiencies and less-restrictive alternatives

Tying and bundling often generate legitimate efficiencies: cost savings from unified billing, improved interoperability, or enhanced user experience. The key question is whether the same efficiencies could be achieved through less-restrictive means.

For example, in *United States v. Microsoft* (2001), the court found that tying Internet Explorer to Windows foreclosed Netscape and Java, undermining the middleware threat to Microsoft's operating system monopoly. For economic analysis of tying and bundling, see Whinston (2006). While Microsoft argued integration benefits, the court found that much of the integration could have been accomplished without contractual or technical restrictions on rivals' ability to compete.

Similarly, in *Google Android* (EC, 2018), the European Commission found that Google's requirement that manufacturers pre-install Google Search and Chrome as a condition of licensing the Play Store foreclosed rivals, even though the Commission acknowledged integration efficiencies. The remedy required Google to offer Android without the mandatory pre-installation bundle, demonstrating the feasibility of less-restrictive alternatives.

### Qualitative evidence for tying and defaults

- **Product requirement documents (PRDs)**: Technical specs and design decisions that reveal whether degradation of rival interoperability was deliberate.
- **API access terms**: Restrictions on rivals' access to APIs or data compared to the firm's own integrated products.
- **User research and experiments**: A/B tests that show user preferences when given genuine choice (e.g., choice screens, default toggles).
- **Board and strategy memos**: Documents discussing leveraging market power in one product to advantage another, or concern about middleware or platform-bypass threats.

#### Tying and bundling impacts on rival market shares

When a dominant firm in one market (e.g., operating systems) bundles or ties its product with an adjacent product (e.g., browsers, media players), rivals in the tied market may lose scale and exit. The following visualization tracks bundle adoption and rival market share evolution.

![Tying and Bundling Impacts on Rival Market Shares](../images/monopoly-tying-bundling-impacts-1.png)

*Top: Bundle penetration ramps up after introduction. Bottom left: Market share evolution showing rival collapse. Bottom right: Strong negative correlation between bundle penetration and rival share.*

**Interpretation:** The bundle was introduced in Q8, and penetration ramped quickly to 80-90% by Q16 as new OS installations included the bundled media player by default. Rival A's market share dropped from ~40% to ~10% over the same period, while Rival B's share fell from ~20% to ~5%. The strong negative correlation (-0.95+) between bundle penetration and rival share supports the foreclosure theory. The stacked area chart shows the incumbent's bundled product capturing share predominantly from the leading standalone rival.

**Data replacement:** Use OS installation data (OEM shipments, enterprise deployments) to measure bundle penetration. Track media player usage via telemetry, market surveys (e.g., StatCounter, NetMarketShare), or download statistics. For technical tying (defaults, API restrictions), collect user switching data and A/B test results on choice screen interventions.

**Counterfactual analysis:** To isolate the causal effect of bundling from organic trends, estimate a difference-in-differences model comparing markets or time periods with and without the bundle. If the bundle rolled out in stages (e.g., different regions or OS versions), use the staggered rollout as a natural experiment. Document whether rival share losses coincide with reduced investment, product exits, or acquisition at distressed valuations.

**Looking ahead:** For more on defaults and choice screens in digital markets, see Chapter 9. For damages estimation in tying cases, see Chapter 12.

## Most-favored-nation clauses and parity agreements

Most-favored-nation (MFN) or parity clauses require sellers to offer the platform or buyer terms at least as favorable as those offered on any other channel. In platform settings, MFNs can chill price competition by preventing sellers from experimenting with lower prices on rival platforms or direct channels.

**Types of MFNs**:

1. **Broad/across-platform MFNs**: Seller cannot offer lower prices anywhere else (including on their own website).
2. **Narrow/platform-to-platform MFNs**: Seller cannot offer lower prices on other platforms, but can undercut on their own direct channel.

**Theories of harm**:

- **Reduced inter-platform competition**: If sellers cannot price differently across platforms, platforms cannot compete on fees (lower fees would not translate to lower retail prices if the seller must maintain parity everywhere).
- **Foreclosure of entry**: Entrant platforms cannot attract sellers with lower fees if sellers are bound by MFNs to incumbents, as fee savings cannot be passed through to consumers.
- **Coordination facilitation**: MFNs reduce price variation, increasing transparency and making tacit coordination easier.

**Empirical assessments**: Compare price dispersion before and after MFN adoption, or across platforms with and without MFNs:

- **Price dispersion tests**: If MFNs bind, within-product price dispersion (across platforms or time) should narrow.
- **Fee pass-through**: Absent MFNs, platforms that lower fees should see sellers reduce retail prices. With MFNs, pass-through is muted.
- **Entry and platform switching**: Document whether rival platforms grew or stagnated after MFN adoption; interview sellers about constraints on multi-homing strategies.

The European Commission challenged Amazon's across-platform MFN (parity requirement) in several member states, finding that it insulated Amazon from price competition and reduced sellers' incentives to join rival platforms (EC Amazon Marketplace, 2017). The UK Competition and Markets Authority similarly required removal of broad MFNs in online hotel booking following its investigation (CMA, 2014).

#### MFN effects on price dispersion and fee pass-through

Most-favored-nation clauses eliminate price variation across platforms, preventing platforms from competing on fees and insulating incumbents from entry. The following visualization shows how MFNs affect price dispersion and platform fee pass-through.

![MFN Effects on Price Dispersion and Fee Pass-Through](../images/monopoly-mfn-price-dispersion-1.png)

*Top left: Price dispersion collapses after MFN adoption. Top right: Price convergence across platforms. Bottom: Fee pass-through eliminated by MFN.*

**Interpretation:** Before the MFN, hotels priced differently across platforms, reflecting variation in platform fees (Incumbent 20%, Rival A 15%, Rival B 12%, Direct 0%). Price dispersion (coefficient of variation) averaged 0.05-0.08. After the MFN binds, prices converge across all platforms to near the Incumbent's level, collapsing dispersion to near zero. The fee pass-through test shows that pre-MFN, hotels on lower-fee platforms charged correspondingly lower prices (gap of ~$4.60), consistent with partial pass-through of fee savings. Post-MFN, the price gap shrinks to near zero, as hotels cannot undercut on rival platforms without violating parity.

**Data replacement:** Use platform transaction data with hotel-level prices across multiple channels (incumbent platform, rival platforms, hotel direct booking). Estimate pass-through regressions to quantify the relationship between platform fees and retail prices before and after MFN adoption. Interview sellers to document contractual constraints on pricing flexibility.

**Looking ahead:** For more on platform competition and two-sided markets, see Chapter 9 (Digital Markets). For MFN-related damages estimation, see Chapter 12 (Litigation Practice).

## Refusal to deal and essential facilities

Refusal to deal claims arise when a vertically integrated dominant firm denies rivals access to an input or platform that is indispensable for competition. The "essential facilities" doctrine, more accepted in the EU than the US, requires the plaintiff to show (1) indispensability of the input, (2) refusal likely to eliminate competition, (3) no objective justification, and (4) the refusal harms consumers.

### Indispensability and access terms

- **Indispensability**: Can rivals compete without access? Examine whether alternatives exist (other suppliers, substitute inputs, bypass strategies) and their economic feasibility.
- **Terms of access**: If access is provided, are the terms (price, technical specifications, service levels) equivalent to what the integrated firm provides to itself? Margin squeeze analyses compare the wholesale access price to the retail price, subtracting downstream costs to see if an equally efficient rival can break even.
- **Objective justification**: Legitimate reasons to refuse access include capacity constraints, IP protection, or safety/quality concerns. Assess whether less-restrictive conditions could address these concerns.

In *Bronner* (1998), the European Court of Justice held that a newspaper distribution network was not indispensable because the rival could develop its own network, even if at higher cost. By contrast, in *IMS Health* (2004), the court found that a unique brick structure for regional health data was indispensable, and refusal to license it eliminated competition in a derivative market.

#### Margin squeeze analysis

A margin squeeze occurs when a vertically integrated firm sets its wholesale access price so high—or its retail price so low—that an equally efficient downstream rival cannot profitably compete. The following visualization demonstrates the margin squeeze test using wholesale and retail pricing data.

![Margin Squeeze Analysis](../images/monopoly-margin-squeeze-1.png)

*Top left: Margin available to equally efficient rival over time. Top right: Waterfall showing squeeze mechanism. Bottom: Wholesale price discrimination between external and internal pricing.*

**Interpretation:** The margin squeeze test shows that an equally efficient rival—one with the same downstream costs as the incumbent—cannot break even when paying the incumbent's wholesale access price and competing at the incumbent's retail price. The waterfall reveals that the rival margin ($6) is well below the minimum required to sustain operations (~$10). The wholesale price comparison shows that the incumbent implicitly transfers wholesale access to its own retail arm at a lower price than charged to rivals, violating the non-discrimination principle.

**Data replacement:** Use regulatory cost accounting data, interconnection agreements, and retail tariff schedules. For telecommunications, water, electricity, or transport access cases, request separated accounts showing upstream and downstream cost allocations. Cross-check implicit transfer prices against actual wholesale prices charged to third parties.

**Legal framework:** Margin squeeze is recognized as abusive under Article 102 TFEU (*Deutsche Telekom*, 2010; *Telefónica*, 2014) and in Southern African competition law (Telkom SA case, 2013 settlement). In the United States, the *linkLine* decision (2009) narrowed the scope of margin squeeze claims absent an antitrust duty to deal, but margin squeeze remains relevant where regulatory obligations to provide access exist.

For FRAND-committed standard-essential patents (SEPs), the analysis shifts to whether licensing terms comply with the FRAND obligation and whether injunctions or threats thereof constitute hold-up. See Chapter 11 for detailed treatment of SEPs.

### Southern African exclusion case evidence
- **Telkom wholesale broadband (Competition Commission v. Telkom SA, 2013 settlement).** Using bitstream and IPConnect price data from 2005–2009, the Commission demonstrated that Telkom’s effective wholesale prices exceeded its retail DSL tariffs for 91% of line-speed combinations once access and backhaul costs were included, yielding a classic margin squeeze. The Tribunal-approved settlement paired a R200 million administrative penalty with mandated price cuts (down to cost-plus 8%) and functional separation of wholesale and retail reporting lines, providing a replicable margin-test template for regulated utilities.
- **Media24 community newspapers (Competition Commission v. Media24, Tribunal case 122/CR/Dec12).** Investigators constructed four-year panel data on advertising volumes, pagination, and production costs for Forum and Gold-Net News titles in Welkom. The Tribunal relied on an avoidable-cost test showing that Forum’s ad rates sat 20–30% below incremental costs for 18 consecutive months, combined with internal documents targeting rival exit, to find predatory pricing. The remedy required cost-based pricing governance and quarterly reporting on advertising discounts.
- **Polypropylene feedstock (Competition Commission v. Sasol Chemical Industries, 2014 CAC judgment).** The Commission benchmarked Sasol’s propylene prices against export parity and long-run incremental cost, revealing margins 41–47% above competitive levels despite surplus capacity. The Tribunal’s excessive-pricing ruling—upheld by the Competition Appeal Court—ordered R534 million in penalties and compelled publication of a transparent pricing formula, underlining how cost benchmarking can support exploitation and exclusion theories simultaneously.

{% hint style="info" %}
**Method box: Foreclosure share calculation**

When evaluating exclusive dealing or loyalty rebate programs, compute the share of demand or capacity that is foreclosed to rivals:

![Market Foreclosure by Exclusive/Loyalty Contracts](../images/monopoly-foreclosure-shares-1.png)

*Bar chart showing foreclosed vs. contestable volume by customer, with contract durations shown above bars.*

Interpretation: If the foreclosed share (here 58%) exceeds the threshold needed for rivals to reach minimum efficient scale, and contracts are long-duration with staggered renewals, foreclosure concerns are substantial.
{% endhint %}

{% hint style="info" %}
**Method box: Event study around contract rollout**

If exclusive or loyalty contracts were adopted in a staggered fashion, use an event-study design:

- Event/phase analysis around contract adoptions.
- Local average treatment effects from staggered contract rollouts (using `did` or `fixest` packages).
- Simple structural checks: margin squeeze sketches using internal cost data.
{% endhint %}

{% hint style="info" %}
**Method box: price-cost test sketch**

```r
contracts <- data.frame(
  customer = c("C1","C2","C3","C4"),
  list_price = c(100, 95, 90, 92),
  rebate = c(10, 5, 0, 8),
  variable_cost = c(70, 70, 70, 70)
)
contracts$effective_price <- contracts$list_price - contracts$rebate
contracts$margin_over_cost <- contracts$effective_price - contracts$variable_cost
contracts
```
Interpretation: negative margins suggest prices below variable cost; adapt to period-level data and include allocable incremental costs where relevant.
{% endhint %}

{% hint style="info" %}
**Qualitative evidence**

- Internal strategy docs and emails on exclusion goals.
- Contract clause analysis and negotiation histories.
- Customer interviews on switching frictions and coercion.
{% endhint %}

{% hint style="info" %}
**Citations and comparative note**

- Cite Section 2/FTC Act standards and leading cases (e.g., Microsoft, Qualcomm) alongside Article 102 TFEU decisions (e.g., Intel rebates, Google Shopping/Android) for contrast.
- For price-cost tests and rebates, reference agency guidance (e.g., EC Enforcement Priorities on exclusionary conduct) and economic literature on effective price tests.
- Flag jurisdiction-specific burdens on effects vs. form and intent.
{% endhint %}

{% hint style="info" %}
**Case box: Core exemplars**

- IBM (historic US monopolization framing) and Microsoft (tying/exclusion of browser/middleware).
- Google Search and Ad Tech cases (US DOJ; EC Google Shopping/Android) — defaults, self-preferencing, data advantages.
- Foreclosure and predation: United Brands (EU), Intel rebates (EU), Qualcomm (US/EU), predation tests (e.g., Brooke Group, AKZO).
- IP vs. monopoly conduct: refusal to deal/essential facilities and licensing constraints; flag tensions between IP rights and exclusion analysis.
{% endhint %}
