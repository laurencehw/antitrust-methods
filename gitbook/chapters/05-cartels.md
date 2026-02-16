# Cartels and Collusion {#sec-cartels}

Cartels represent the clearest antitrust violations---competitors agreeing to fix prices, rig bids, or allocate markets cause direct and quantifiable harm to consumers. Yet proving collusion and measuring damages requires integrating the research design, market definition, and IO tools from earlier chapters into a coherent evidentiary package.

This chapter shows how to detect collusion, measure its effects, and build cases that survive both economic and legal scrutiny. We emphasize the interplay between quantitative screens and qualitative evidence: econometric analysis can establish that prices were artificially elevated, but leniency statements and internal communications provide the smoking gun that confirms coordination. The two streams of evidence reinforce each other.

## Learning goals
Cartel enforcement hinges on weaving together quantitative screens, econometric estimates, and documentary evidence. This chapter walks through that workflow using established methodologies from the OECD and academic literature on cartel detection.

By the end you should be able to:

- Spot suspicious conduct using dashboards, variance/rotation screens, and early break tests.
- Tie raid/leniency events to structural changes in prices, margins, and quantities.
- Estimate overcharge and pass-through with transparent assumptions and uncertainty analysis.
- Triangulate econometrics with leniency statements, chats, and procurement narratives to build court-ready stories.

## Workflow roadmap

{% hint style="info" %}
**Cartel Detection and Analysis Workflow**

```
PHASE 1: DETECTION            PHASE 2: ESTIMATION          PHASE 3: LITIGATION
       |                            |                            |
       v                            v                            v
+----------------+           +----------------+           +----------------+
| Intake:        |           | Overcharge     |           | Expert report  |
| - Leniency app |           | estimation:    |           | preparation:   |
| - Complaint    |---------->| - Before/after |---------->| - Methodology  |
| - Market intel |           | - DiD          |           | - Damages      |
+----------------+           | - Yardstick    |           | - Uncertainty  |
       |                     +----------------+           +----------------+
       v                            |
+----------------+                  v
| Screening:     |           +----------------+
| - Variance     |           | Pass-through   |
| - Rotation     |           | analysis:      |
| - Correlation  |           | - Direct/      |
| - Benford      |           |   indirect     |
+----------------+           +----------------+
       |
       v
+----------------+
| Event/break    |
| analysis:      |
| - Raid dates   |
| - Leniency     |
| - Regime shift |
+----------------+
       |
       v
+----------------+
| Triangulation: |
| - Documents    |
| - Interviews   |
| - Messaging    |
+----------------+
```
**Detection triggers:** Leniency applications | Whistleblowers | Market screens | Competitor complaints
{% endhint %}

1. **Timeline & conduct map.** Build a dated chronology from complaints, internal messages, procurement milestones, and raids. Align suspected mechanisms (bid rotation, geographic allocation, price floors) with specific products and periods.
2. **Descriptive diagnostics.** Plot prices, costs, and quantities; look for unnatural stability or compression.
3. **Screens.** Run variance, digit, and rotation screens to triage markets. Treat them as prioritization tools, not dispositive proof.
4. **Event/break tests.** Evaluate how prices or spreads change around raids, leniency announcements, or policy shifts.
5. **Overcharge & pass-through.** Estimate counterfactual prices using panel regressions, yardsticks, or synthetic controls; propagate uncertainty.
6. **Triangulation.** Reconcile quantitative results with leniency statements, buyer interviews, and messaging logs.
7. **Damages & remedies.** Translate overcharge estimates into monetary relief or structural commitments, respecting jurisdictional rules (e.g., Competition Tribunal SA public-interest remedies).

## Timeline and conduct map
Document every known communication, meeting, or enforcement action in a single table (date, event, evidence source, hypothesis). Update it as new statements arrive. Every regression or screen should cite the row(s) it tests—this discipline prevents “data dredging” and makes testimony easier.

## Descriptives and screens
Start with `ggplot2` dashboards that overlay prices with cost indices, demand proxies, and competitor prices. Flag regimes where prices remain static despite volatile costs or where margins converge across firms.

- **Variance/dispersion screens:** Check price spreads, standard deviations, and coefficents of variation across firms or regions (Abrantes-Mello, 2010).  
- **Procurement rotation:** Rank bids chronologically to flag turn-taking, convenient price endings, or geographic allocations (Porter & Zona, 1993); (Conley & Decarolis, 2016).  
- **Digit/Benford checks:** Use sparingly and only when invoice conventions support the assumptions.  
- **Correlation screens:** High correlations in supposedly independent bids can justify deeper probes (Harrington, 2008).

Document screen logic following OECD guidance on cartel screens (OECD Cartel Screens, 2013) and note data limitations (missing bidders, net vs. list prices).

### Bid-rotation analysis
Using cement procurement data to identify potential bid rotation patterns.

```r
library(dplyr)
library(ggplot2)
source("program/R/helpers.R")

# Load cartel bid data (synthetic for illustration)
bids_df <- read.csv("data/derived/cartel_cement_bids.csv")

# Analyze win patterns by firm
rotation <- bids_df |>
  group_by(winner) |>
  summarise(
    wins = n(),
    avg_bid = mean(winning_bid, na.rm = TRUE),
    cartel_wins = sum(cartel_period),
    non_cartel_wins = sum(!cartel_period)
  ) |>
  arrange(desc(wins))

ggplot(rotation, aes(x = reorder(winner, wins), y = wins)) +
  geom_col(fill = antitrust_colors["blue"]) +
  coord_flip() +
  labs(title = "Bid wins by vendor (cement procurement)",
       subtitle = "Data: Simulated cement cartel case",
       x = NULL, y = "Contract wins") +
  theme_antitrust()
```
Pair charts with tables showing consecutive wins, geographic patterns, or unexplained bid withdrawals.

### Transition matrix for rotation detection
While bar charts show win counts, a **transition matrix** reveals systematic rotation by showing which firm wins after another firm won the previous contract. Systematic rotation produces off-diagonal clustering; competitive bidding produces diagonal concentration (repeat wins).

```r
library(dplyr)
library(tidyr)
library(ggplot2)
source("program/R/helpers.R")

# Load real cartel bid data
bids_df <- read.csv("data/derived/cartel_cement_bids.csv")

# Create lagged winner variable for transition analysis
transitions <- bids_df |>
  arrange(tender_id) |>
  mutate(
    prev_winner = lag(winner),
    period = if_else(cartel_period, "Cartel period", "Competitive period")
  ) |>
  filter(!is.na(prev_winner))

# Compute transition matrix for cartel period
cartel_transitions <- transitions |>
  filter(period == "Cartel period") |>
  count(prev_winner, winner, name = "count") |>
  group_by(prev_winner) |>
  mutate(prob = count / sum(count)) |>
  ungroup()

# Heatmap visualization
ggplot(cartel_transitions, aes(x = winner, y = prev_winner, fill = prob)) +
  geom_tile(color = "white", linewidth = 0.5) +
  geom_text(aes(label = scales::percent(prob, accuracy = 1)),
            color = "white", fontface = "bold", size = 3.5) +
  scale_fill_gradient(low = "#56B4E9", high = "#D55E00",
                      labels = scales::percent_format()) +
  labs(
    title = "Bid Rotation Transition Matrix (Cartel Period)",
    subtitle = "Probability of Firm Y winning given Firm X won previous tender",
    x = "Winner at time t",
    y = "Winner at time t-1",
    fill = "Transition\nprobability",
    caption = "Off-diagonal clustering indicates systematic rotation; diagonal dominance suggests repeat wins."
  ) +
  theme_antitrust() +
  theme(
    axis.text.x = element_text(angle = 45, hjust = 1),
    legend.position = "right",
    panel.grid = element_blank()
  )

# Rotation index: ratio of off-diagonal to diagonal transitions
diag_prob <- cartel_transitions |>
  filter(prev_winner == winner) |>
  summarise(diag = sum(prob * count) / sum(count)) |>
  pull(diag)

cat("\nRotation diagnostics:\n")
cat(paste0("Diagonal (repeat win) share: ", scales::percent(diag_prob, accuracy = 0.1), "\n"))
cat(paste0("Off-diagonal (rotation) share: ", scales::percent(1 - diag_prob, accuracy = 0.1), "\n"))
cat("Note: Competitive markets typically show >50% diagonal; rotation schemes show <30%.\n")
```

**How to interpret the transition matrix:**

- **Diagonal cells** show the probability of a firm winning consecutive contracts. In competitive markets, efficient firms often win repeatedly (high diagonal values).
- **Off-diagonal patterns** reveal rotation. If Firm A→B→C→D→A appears consistently, you'll see elevated probabilities in a cyclical off-diagonal pattern.
- **Uniform off-diagonal** suggests random or structured rotation with no repeat wins allowed.
- **Asymmetric off-diagonal** may indicate a hub-and-spoke arrangement where one firm coordinates others.

### Bid-rotation network graph
Network graphs help visualize suspected coordination patterns by showing which bidders consistently "yield" to others. This is particularly useful for identifying systematic rotation schemes or hub-and-spoke arrangements.

```r
library(dplyr)
library(tidyr)
library(ggplot2)
library(igraph)
library(ggraph)

# Simulated bid data: tender_id, bidder, rank, bid_amount
# In practice, replace with actual procurement data
set.seed(123)
n_tenders <- 50
bidders <- c("Firm A", "Firm B", "Firm C", "Firm D", "Firm E")

bids <- expand.grid(
  tender_id = 1:n_tenders,
  bidder = bidders
) |>
  group_by(tender_id) |>
  mutate(
    # Simulate rotation: certain patterns are more likely
    base_bid = runif(n(), 100, 200),
    rotation_boost = case_when(
      tender_id %% 5 == 0 & bidder == "Firm A" ~ -20,
      tender_id %% 5 == 1 & bidder == "Firm B" ~ -20,
      tender_id %% 5 == 2 & bidder == "Firm C" ~ -20,
      tender_id %% 5 == 3 & bidder == "Firm D" ~ -20,
      tender_id %% 5 == 4 & bidder == "Firm E" ~ -20,
      TRUE ~ 0
    ),
    bid = base_bid + rotation_boost,
    rank = rank(bid)
  ) |>
  ungroup()

# Identify winners and runner-ups
winners <- bids |>
  filter(rank == 1) |>
  select(tender_id, winner = bidder)

runner_ups <- bids |>
  filter(rank == 2) |>
  select(tender_id, runner_up = bidder)

# Create edge list: who "yielded" to whom (runner-up -> winner)
edges <- inner_join(winners, runner_ups, by = "tender_id") |>
  count(runner_up, winner, name = "weight") |>
  filter(runner_up != winner)

# Create network graph
g <- graph_from_data_frame(edges, directed = TRUE)

# Plot using ggraph
ggraph(g, layout = "fr") +
  geom_edge_link(aes(width = weight, alpha = weight),
                 arrow = arrow(length = unit(4, 'mm'), type = "closed"),
                 end_cap = circle(3, 'mm'),
                 color = "#666666") +
  geom_node_point(size = 12, color = "#0072B2", alpha = 0.8) +
  geom_node_text(
    aes(label = name),
    color = "white",
    fontface = "bold",
    size = 4,
    family = "Arial"
  ) +
  scale_edge_width(range = c(0.5, 3)) +
  scale_edge_alpha(range = c(0.3, 0.9)) +
  labs(
    title = "Bid Rotation Network Graph",
    subtitle = "Arrows show which firms consistently submit 2nd-place 'cover bids' when others win",
    caption = "Edge width = frequency of runner-up pattern. Systematic rotation creates hub-spoke or circular patterns."
  ) +
  theme_graph() +
  theme(
    text = element_text(family = "Arial"),
    plot.title = element_text(size = 14, face = "bold"),
    plot.subtitle = element_text(size = 11),
    legend.position = "none"
  )

# Supplementary table: win rates and rotation metrics
rotation_metrics <- bids |>
  group_by(bidder) |>
  summarise(
    wins = sum(rank == 1),
    second_place = sum(rank == 2),
    avg_rank = mean(rank),
    rotation_index = wins / n_tenders
  ) |>
  arrange(desc(wins))

cat("\nRotation metrics by bidder:\n")
print(rotation_metrics, n = Inf)

# Centrality metrics to identify hub firms
cat("\n--- NETWORK CENTRALITY ANALYSIS ---\n")

# Eigenvector centrality: identifies influential nodes
eigen_scores <- eigen_centrality(g)$vector
cat("\nEigenvector centrality (hub influence):\n")
print(sort(eigen_scores, decreasing = TRUE))

# In-degree: who receives the most "yielding" from others
in_deg <- degree(g, mode = "in")
cat("\nIn-degree (frequency of winning when others yield):\n")
print(sort(in_deg, decreasing = TRUE))

# Out-degree: who yields most often to others
out_deg <- degree(g, mode = "out")
cat("\nOut-degree (frequency of yielding to others):\n")
print(sort(out_deg, decreasing = TRUE))

# Betweenness: who bridges different parts of the network
between_scores <- betweenness(g, directed = TRUE)
cat("\nBetweenness centrality (coordination role):\n")
print(sort(between_scores, decreasing = TRUE))

# Summary interpretation
cat("\n--- INTERPRETATION ---\n")
hub_firm <- names(which.max(eigen_scores))
cat(paste0("Likely hub/ringleader: ", hub_firm,
           " (highest eigenvector centrality)\n"))
cat("High eigenvector + high in-degree = receives wins from many firms\n")
cat("High betweenness = potential coordinator bridging subgroups\n")
```

**How to interpret this graph:**
- **Hub-spoke patterns**: If one firm is at the center with many arrows pointing to it, that firm may be the "ringleader" coordinating bids.
- **Circular patterns**: Arrows forming a circle (A→B→C→D→A) suggest systematic rotation where firms take turns winning.
- **Asymmetric flows**: If Firm A frequently comes second when Firm B wins, but not vice versa, this may indicate a hierarchical arrangement.
- **Edge weights**: Thicker arrows indicate more frequent patterns, which are more suspicious than occasional occurrences.

**Practical applications:**
- Combine with document evidence (emails, meeting logs) to validate rotation schemes.
- Compare network patterns across product lines or regions to identify geographic allocation.
- Use as demonstrative exhibit in tribunal presentations or expert reports.

Replace simulated data with actual procurement records (World Bank, TED, US DOT, Stats SA infrastructure tenders). Document bid amounts, dates, and project characteristics in `data/raw/procurement/` with provenance notes.

## Event and break tests
When raids or leniency filings occur, run event studies on prices, spreads, or quantities. Check both cartel participants and outsiders; in public procurement you can also evaluate engineers’ estimates or cost indices.

Structural break tests (Bai–Perron, CUSUM) highlight regime shifts. Always incorporate costs so you do not misattribute cost-driven changes to conduct. Present break plots next to relevant timeline entries (e.g., WhatsApp thread confirming a January 2019 meeting).

{% hint style="info" %}
**Code box: raid event study scaffold**

```r
# df must include date, price, cost, treated (0/1), firm, product
# library(fixest)
# df <- df |> mutate(post = date >= as.Date("YYYY-MM-DD"))
# feols(log(price) ~ post * treated + cost + month(date) | firm + product + year(date),
#       cluster = ~firm, data = df)
```
{% endhint %}

## Overcharge and pass-through
Pick a counterfactual that matches data availability:

- **Before/after:** Include product, customer, and time fixed effects plus cost controls.  
- **Difference-in-differences:** Compare cartel markets to unaffected regions or product classes; test pre-trends.  
- **Yardsticks:** Use similar markets (neighboring countries, regulated benchmarks) when local data are thin.  
- **Synthetic controls:** Helpful for single-market cartels; combine unaffected markets into a donor pool.

Robustness: alternative functional forms (log vs. level), trimming outliers, placebo periods, heteroskedasticity checks, and randomization inference when N is small. For pass-through, regress downstream prices on upstream costs with lags to quantify harm on intermediaries vs. end-users.

### Placebo tests for causal validation

Placebo tests strengthen causal claims by showing that the estimated effect disappears when applied to situations where no effect should exist. Two common approaches:

1. **Product placebo**: Run the same regression on a product NOT involved in the cartel. If you find a similar "effect," your identification is suspect.
2. **Timing placebo**: Use a fake raid/leniency date. If structural breaks appear at arbitrary dates, the true break may be spurious.

```r
library(dplyr)
library(fixest)
library(ggplot2)
source("program/R/helpers.R")

# Simulate panel data for cartel and control products
set.seed(456)
n_periods <- 60
raid_date <- 36  # Raid occurs at period 36

panel <- expand.grid(
 period = 1:n_periods,
 product = c("Cement (cartel)", "Gravel (control)")
) |>
 mutate(
   post_raid = period >= raid_date,
   cartel_product = product == "Cement (cartel)",
   cost = 50 + cumsum(rnorm(n(), 0, 1)),  # Common cost shock
   # Cartel product has elevated prices pre-raid, drops after
   price = case_when(
     cartel_product & !post_raid ~ 100 + 0.8 * cost + 15 + rnorm(n(), 0, 3),
     cartel_product & post_raid ~ 100 + 0.8 * cost + rnorm(n(), 0, 3),
     TRUE ~ 95 + 0.85 * cost + rnorm(n(), 0, 3)  # Control product
   )
 )

# Main regression: cartel product
main_model <- feols(
 log(price) ~ post_raid + cost | product,
 data = filter(panel, cartel_product),
 cluster = ~product
)

# Placebo 1: Control product (should show NO effect)
placebo_product <- feols(
 log(price) ~ post_raid + cost | product,
 data = filter(panel, !cartel_product),
 cluster = ~product
)

# Placebo 2: Fake raid date (period 20 instead of 36)
panel_fake <- panel |>
 mutate(post_fake_raid = period >= 20)

placebo_timing <- feols(
 log(price) ~ post_fake_raid + cost | product,
 data = filter(panel_fake, cartel_product),
 cluster = ~product
)

# Display results
cat("=== MAIN RESULT: Cartel Product ===\n")
cat(paste0("Post-raid effect: ", round(coef(main_model)["post_raidTRUE"], 4),
          " (expect negative = price drop)\n\n"))

cat("=== PLACEBO 1: Control Product ===\n")
cat(paste0("Post-raid effect: ", round(coef(placebo_product)["post_raidTRUE"], 4),
          " (should be ~0 if identification valid)\n\n"))

cat("=== PLACEBO 2: Fake Raid Date ===\n")
cat(paste0("Post-fake-raid effect: ", round(coef(placebo_timing)["post_fake_raidTRUE"], 4),
          " (should be ~0 if true break is at raid date)\n"))

# Visualization
ggplot(panel, aes(x = period, y = price, color = product)) +
 geom_vline(xintercept = raid_date, linetype = "dashed", color = "darkred", linewidth = 1) +
 geom_line(linewidth = 0.8, alpha = 0.8) +
 annotate("text", x = raid_date + 1, y = max(panel$price) - 5,
          label = "Raid date", color = "darkred", hjust = 0, fontface = "italic") +
 scale_color_manual(values = c("Cement (cartel)" = "#D55E00", "Gravel (control)" = "#0072B2")) +
 labs(
   title = "Placebo Test: Cartel vs. Control Product",
   subtitle = "Control product shows no structural break at raid date",
   x = "Period", y = "Price", color = NULL
 ) +
 theme_antitrust() +
 theme(legend.position = "bottom")
```

**Interpreting placebo results:**

- **Product placebo fails** (control shows effect): Consider whether the "control" product is actually affected, or whether your specification captures market-wide shocks rather than cartel conduct.
- **Timing placebo fails** (fake date shows effect): Your data may have multiple structural breaks, or the cartel period definition is imprecise. Cross-check with documentary evidence.
- **Both placebos pass**: Strengthens the causal interpretation that the raid/leniency event caused the observed price change.

## Leniency, documents, and triangulation
Leniency statements, chats, and board minutes pin down conduct mechanisms (rotation order, price floors, trigger strategies). Use them to:

- Set regression windows and sample selections.  
- Validate that estimated start/stop dates match qualitative evidence.  
- Explain residuals—if econometrics show little effect where documents admit coordination, revisit product mapping or data coverage.  
- Clarify what is fact (documented) vs. inference (econometric patterns), citing (OECD Leniency Programmes, 2015) or agency policies.

{% hint style="info" %}
**Method box: econometric toolkit**

**Event studies:** Evaluate raid/leniency impact on prices or spreads.  
**Overcharge regressions:** `feols(log(price) ~ cartel_period + cost + demand | product + customer + time)` with clustered SEs and placebo checks.  
**Pass-through:** Dynamic regressions or VECMs linking upstream and downstream prices to trace harm along the chain.
{% endhint %}

{% hint style="info" %}
**Method box: screens & variance**

**Distribution screens:** Variance compression, digit spikes, Benford where appropriate.  
**Rotation checks:** Consecutive wins, geographic allocation, or sequential ordering.  
**Cost-pass-through diagnostics:** Compare pass-through before/during suspected collusion; suppressed pass-through can corroborate coordination.
{% endhint %}

{% hint style="info" %}
**Qualitative evidence**

Treat qualitative materials as structured data:

- **Bid sheets & messaging apps:** Extract explicit allocation rules or fallback prices.  
- **Buyer interviews:** Document procurement timelines, awareness of cover bids, or complaints.  
- **Expert narratives:** Craft timelines tying every empirical result to specific documents.
{% endhint %}

{% hint style="info" %}
**Case box: Illustrative matters**

**Apple eBooks (US).** Hub-and-spoke coordination with agency-model contracts and SSNDQ logic (*United States v. Apple Inc.*, 2013).
**Lysine & DRAM (US/EU).** Classic dawn-raid analyses with overcharge estimates of 17--20% (lysine) and 10--15% (DRAM), illustrating how leniency programs can expose sophisticated international price-fixing. These cases anchor the empirical literature on cartel overcharges.
**Construction bid-rigging (EU, SA, JFTC).** Rotation matrices and dawn raids aligned with procurement archives.
**Digital advertising (SAMR).** Algorithms and platform policies as qualitative evidence.
{% endhint %}

{% hint style="info" %}
**Case box: South African enforcement highlights**

- **Bread cartel (Tribunal case 15/CR/Feb07).** Stats SA CPI data plus mill-level costs revealed synchronized 30–40 cent jumps; overcharge estimated at 7–10% with R250 million penalties and consumer relief funds.  
- **Construction fast-track settlement (2013).** Self-reported matrices across 300 tenders showed rotation; event windows around raids captured 8–12% price drops relative to engineers’ estimates.  
- **Fertilizer/ammonia (Sasol/Yara/Omnia).** Export-parity benchmarks and plant-level variable-cost data showed 25–30% overcharges despite spare capacity, leading to penalties and divestitures.
{% endhint %}

## Code box: structural break illustration
```r
library(fredr)
library(dplyr)
library(strucchange)
library(ggplot2)
source("program/R/helpers.R")

fredr_set_key(Sys.getenv("FRED_API_KEY"))
gas <- fredr(series_id = "GASREGW", observation_start = as.Date("2015-01-01")) |>
  rename(price = value) |>
  mutate(week = row_number())

bp <- breakpoints(price ~ week, data = gas, h = 26)
gas$regime <- factor(cut(gas$week, c(0, bp$breakpoints, Inf)))

ggplot(gas, aes(date, price, color = regime)) +
  geom_line(linewidth = 0.8) +
  labs(
    title = "Regular Gasoline Prices: Structural Break Illustration",
    subtitle = "FRED series GASREGW (weekly, US average)",
    x = NULL,
    y = "USD per gallon",
    color = "Regime"
  ) +
  scale_color_viridis_d() +
  theme_antitrust() +
  guides(color = guide_legend(nrow = 1))
```
Replace the public FRED data with product-level transactions to present in litigation.

{% hint style="info" %}
**Citations and comparative note**

- Cite OECD screen guidance, FTC/DOJ econometrics speeches, and EC/JFTC leniency notices when defending methodology.
- Reference cases (lysine, DRAM, auto parts, LIBOR) with docket numbers.
- Flag jurisdictional differences: e.g., SAMR often requires data-driven screens, while US courts scrutinize documentary corroboration.
{% endhint %}

{% hint style="success" %}
**Key Takeaways**

1. **Screens are triage tools, not proof.** Variance screens, rotation patterns, and price correlations identify suspicious markets worth investigating. They rarely prove collusion alone.

2. **Leniency evidence anchors timelines.** The strongest cartel cases combine econometric analysis with documentary evidence from leniency applicants. Build your analysis around known communication dates.

3. **Overcharge estimation requires a credible counterfactual.** Whether using before-after, yardstick, or difference-in-differences, clearly articulate what prices would have been absent the cartel.

4. **Pass-through matters for damages.** If overcharges were passed through to downstream customers, direct purchasers may not bear the full harm. Document pass-through assumptions.

5. **Structural breaks are not self-interpreting.** A price drop after a raid is consistent with cartel breakdown---but also with demand shocks, cost changes, or confounding events. Triangulate with qualitative evidence.

6. **Document everything.** Cartel analysis often leads to litigation. Keep code reproducible, data hashed, and methodology memos contemporaneous.
{% endhint %}

## Looking ahead
The detection screens, overcharge regressions, and pass-through analyses developed here carry forward throughout the book. **[Chapter 6](chapters/06-mergers.md)** builds on the same demand estimates and diversion ratios---post-cartel mergers frequently face heightened scrutiny, and the diagnostic tools overlap substantially. **[Chapter 12](chapters/12-litigation-practice.md)** revisits damages modeling and expert report preparation, showing how to package cartel evidence for courtroom presentation. The rotation indices, structural break plots, and overcharge tables introduced here will serve as templates you can adapt to new cases and jurisdictions.
