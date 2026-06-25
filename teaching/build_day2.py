"""Day 2 — Conduct: cartels, the econometric backbone, abuse of dominance,
labour markets, and digital platforms.
Maps to book chapters 5 (cartels), 6 (econometrics), 7 (monopolization),
10 (labour), 9 (digital). SA-forward, concept-first. Corrected facts per
the audit:
Sasol excessive-pricing finding SET ASIDE by CAC (2015); Media24 finding
overturned by CAC (2019); Intel rebates/AEC finding annulled (GC 2022,
CJEU Oct 2024); Microsoft tying VACATED (liability was s2 maintenance);
Jindal acquitted on Sherman counts; DaVita acquitted (2022).
Kept in sync with slides/day2.qmd (the .qmd is authoritative)."""

from deck_builder import Deck, BLUE, GREEN, ORANGE, RED, PURPLE, CYAN, GREY, DARK

FT = "Day 2 · Conduct"
d = Deck("Day 2 — Conduct",
         "Cartels, abuse of dominance, labour markets, and digital platforms")

# ============================================================ MODULE 2.1
d.section("Module 2.1 — Cartels and collusion",
          "The clearest harm, the hardest evidence: proving an agreement.")

d.bullets("What a cartel case has to establish", [
    "An agreement (or concerted practice) among competitors to fix price, "
    "allocate markets/customers, rig bids, or restrict output — §4(1)(b) in "
    "SA, per se under Sherman §1, 'by object' under Art. 101.",
    "A 'concerted practice' reaches tacit coordination short of a formal "
    "contract: a meeting of minds inferred from contacts plus parallel "
    "conduct that has no other plausible explanation.",
    "Per se / by-object: no need to prove market power or effects — the "
    "agreement itself is the violation. The economics shifts from 'is there "
    "harm?' to screening and damages.",
    "The hard part is proving the agreement. Leniency turns insiders into "
    "witnesses; documents supply the meeting of minds; economics corroborates.",
    "Economist's two jobs: (1) screens that flag conduct, (2) quantifying the "
    "overcharge for damages.",
], footer=FT)

d.bullets("The spectrum: explicit -> tacit -> independent", [
    ("Explicit cartels (agreement on price/allocation): per se / by object. "
     "Illegal regardless of effect.", 0),
    ("Tacit coordination (conscious parallelism, no agreement): generally NOT "
     "unlawful by itself — oligopolists may rationally match prices. Needs "
     "'plus factors' (evidence of communication, actions against self-"
     "interest) to become an inferred agreement.", 0),
    ("Independent action (unilateral pricing on the merits): lawful.", 0),
    "The legal lines map to analytical standards: per se -> no defence on "
    "effects; rule of reason -> balance harm vs justification; the gap "
    "between tacit and explicit is where most litigation lives.",
    "Practical upshot: parallel prices alone never win a cartel case — you "
    "need the agreement; the screen only flags where to look.",
], footer=FT)

d.bullets("Cartel conduct types", [
    ("Price fixing — agreeing prices, margins, surcharges, discounts, or a "
     "price formula.", 0),
    ("Market / customer division — carving up geographies, customers, or "
     "product lines so each firm faces no rival in its slice.", 0),
    ("Output / capacity restriction — agreeing to cut or cap production to "
     "lift price.", 0),
    ("Bid rigging — cover bids, bid suppression, bid rotation, subcontract "
     "payoffs in procurement.", 0),
    "All are §4(1)(b) per se in SA; the detection method differs by type "
    "(price series vs bid-level data vs allocation patterns).",
], footer=FT)

d.bullets("What keeps a cartel stable", [
    ("Detection of cheating — members must observe each other's prices/sales "
     "(transparent markets collude more easily).", 0),
    ("Punishment mechanism — a credible threat (price war) to discipline a "
     "defector; without it, the agreement unravels.", 0),
    ("Entry barriers — outside entry undercuts the cartel price; high "
     "barriers protect the overcharge.", 0),
    ("Demand stability — volatile or unobservable demand makes a price cut "
     "hard to tell from cheating.", 0),
    ("Few firms / symmetry — coordination is easier with fewer, similar "
     "players; fringe firms and mavericks destabilise it.", 0),
    "Read the structure for these factors: they tell you both how likely "
    "collusion is and where the screen should bite.",
], footer=FT)

d.bullets("Cartel screens — what to compute before you have a confession", [
    ("Variance / structural-break screens.", 0),
    ("Cartels stabilise prices, then prices jump when the cartel breaks. A "
     "drop in price variance during the suspected window, then a break, is a "
     "flag.", 1),
    ("Date the breaks with Bai–Perron (multiple unknown breakpoints) or "
     "CUSUM; this is the Chow test for a structural break generalised to "
     "unknown dates (Day 1's regression machinery).", 1),
    ("Bid-rotation / market-allocation screens.", 0),
    ("Who wins in turn, suspiciously similar losing bids, spreads too tight. "
     "Needs bid-LEVEL data (every bid), not just who won.", 1),
    ("Margin / parallel-pricing screens.", 0),
    ("Prices co-moving across rivals beyond what common costs explain.", 1),
    "A screen is an investigative aid, never proof — it survives cross-"
    "examination only when tied to documents and testimony.",
], footer=FT)

d.formula("Detection & enforcement: leniency, sanctions, penalties",
          "The optimal fine must wipe out the expected gain, grossed up for "
          "the chance of escaping detection:",
          ["Optimal fine  >  expected gain / probability of detection"],
          ["Leniency / immunity: first-in gets immunity; a marker system "
           "holds your place. >90% of major cartel cases originate in a "
           "leniency application.",
           "The design exploits the prisoner's dilemma: once one firm can "
           "defect to the authority, every firm races to be first.",
           "Criminal sanctions: SA criminalised cartel conduct for directors; "
           "the US jails executives — the threat is what makes leniency "
           "attractive.",
           "Private damages: US allows treble damages (powers private "
           "enforcement); SA relies on follow-on civil claims."],
          footer=FT)

d.formula("Quantifying the overcharge (before/after method)",
          "Compare cartel-period prices to a competitive benchmark, then "
          "convert to damages:",
          ["Overcharge $ = (P_cartel − P_benchmark) × volume",
           "Damages = pass-through × overcharge rate × commerce"],
          ["Benchmark from a clean before/after window (validate with a "
           "structural-break test), a yardstick market, or cost-plus.",
           "Estimate in changes, control for cost drivers, and stress-test "
           "the window — the defence will attack the benchmark first.",
           "Pass-through matters when buyers are intermediaries who passed "
           "the overcharge downstream.",
           "US: treble damages (×3). SA: follow-on civil claims after a "
           "Tribunal finding."],
          footer=FT)

d.bullets("Damages estimation — three benchmark methods", [
    ("Before/after.", 0),
    ("Same market, compare the cartel window to a clean period before/after. "
     "Strength: like-for-like. Risk: the 'clean' period must really be "
     "uncontaminated (validate with a break test).", 1),
    ("Yardstick.", 0),
    ("A comparable unaffected market (another region/product) stands in for "
     "the but-for price. Strength: contemporaneous. Risk: comparability — "
     "control for the differences.", 1),
    ("Cost-plus.", 0),
    ("Build the but-for price from cost + a competitive return. Strength: no "
     "clean benchmark needed. Risk: cost data and the 'reasonable return' "
     "are contestable.", 1),
    "Pick by data availability and defensibility; triangulate across methods "
    "when you can — agreement across approaches is persuasive.",
], footer=FT)

d.bullets("Standing & the passing-on defence — know the split", [
    ("United States.", 0),
    ("Illinois Brick: only DIRECT purchasers may claim federal damages. "
     "Hanover Shoe: a defendant may NOT reduce damages by arguing the direct "
     "purchaser passed the overcharge on. (Many states differ — Illinois "
     "Brick repealers.)", 1),
    ("Together the two rules let the direct purchaser keep the full overcharge "
     "and bar indirect purchasers federally — a deliberate enforcement-"
     "incentive design.", 1),
    ("EU and South Africa.", 0),
    ("The passing-on defence IS available, and indirect purchasers can claim "
     "— so quantifying pass-through is central, not barred.", 1),
    "First thing a litigator checks — get the forum's rule right before you "
    "model, because it determines who your plaintiff is and what you must "
    "estimate.",
], footer=FT)

d.case_box("The bread cartel", "SA",
           "Leniency + documents + pricing analysis, with real victims",
           ["Premier Foods applied for leniency; implicated Tiger Brands and "
            "Pioneer in fixing the price and timing of bread-price increases "
            "(2007).",
            "Documentary and testimonial evidence established the agreement; "
            "pricing analysis sized the overcharge on a staple food.",
            "Pioneer paid penalties and made price commitments; the matter "
            "anchored SA follow-on damages and the Children's Resource Centre "
            "class action (indirect purchasers — possible in SA)."],
           "The template SA cartel matter: leniency cracks it open, economics "
           "sizes the harm, and the harm lands on poor households.",
           footer=FT)

d.case_box("The construction 'fast-track' settlement", "SA",
           "Bid rigging across an industry, resolved by settlement",
           ["The Commission's fast-track settlement (2013) covered bid rigging "
            "on major projects, including 2010 World Cup stadiums.",
            "15 firms settled for penalties totalling about R1.46 billion.",
            "Shows the bid-rotation screen logic at industry scale, resolved "
            "by a structured settlement that closed many linked bids at once."],
           "When rigging is industry-wide, a structured settlement can do what "
           "case-by-case prosecution cannot — but it depends on bid-level "
           "evidence the screen pointed to.",
           footer=FT)

d.code_demo("Code as demo — a before/after overcharge",
            "Book Ch. 5. Structural break dates the cartel; the gap is the "
            "overcharge.",
            ["source(\"program/R/helpers.R\")",
             "# prices: cartel window vs clean benchmark window",
             "p_cartel    <- mean(price[period == \"cartel\"])",
             "p_benchmark <- mean(price[period == \"after\"])",
             "overcharge_rate <- (p_cartel - p_benchmark) / p_benchmark",
             "damages_single  <- overcharge_rate * commerce",
             "damages_treble  <- 3 * damages_single   # US only"],
            "Validate the benchmark window with a Bai–Perron break test before "
            "you trust the gap.",
            footer=FT)

# ============================================================ MODULE 2.2
d.section("Module 2.2 — The econometric backbone",
          "The methods spine cases rely on: OLS, its failures, and the "
          "designs that survive cross-examination.")

d.bullets("Why this module sits in the middle of the course", [
    "Almost every conduct case rests on a regression: the overcharge, the "
    "foreclosure effect, the wage markdown, the ranking harm.",
    "A tribunal weighs your number by the credibility of the design, not the "
    "sophistication of the model.",
    "Today: the workhorse — OLS, its assumptions, the failures that matter, "
    "and two designs that survive cross-examination (DiD and the event "
    "study).",
    "The through-line: good design beats clever post-hoc fixes. Get the "
    "comparison right and the statistics are easy.",
], footer=FT)

d.formula("Regression basics",
          "The linear model and what each piece does:",
          ["Y = α + βX + γZ + ε"],
          ["Y = outcome (price, wage, click-through); X = the variable of "
           "interest; Z = controls; ε = everything else.",
           "β = the marginal effect of X on Y, holding Z fixed — the number "
           "the case usually turns on.",
           "Controls (Z) strip out confounders so β isolates X; the art is "
           "choosing the right ones without controlling away the effect.",
           "The error term ε holds omitted factors, measurement error, and "
           "pure noise — and it is where the trouble lives."],
          footer=FT)

d.bullets("OLS assumptions (what makes β trustworthy)", [
    "Linearity — the model is linear in parameters (transform variables if "
    "needed: logs for elasticities).",
    "Exogeneity: E[ε | X] = 0 — X is uncorrelated with the error. This is the "
    "assumption that decides cases.",
    "Homoskedasticity — constant error variance (affects SEs, not the "
    "coefficient).",
    "No autocorrelation — errors uncorrelated across observations (matters in "
    "panels / time series).",
    "Violate exogeneity and β is biased; violate the variance assumptions and "
    "β is fine but the SEs (and your significance claims) are wrong.",
], footer=FT)

d.bullets("Violations 1 — endogeneity (the central worry)", [
    ("Reverse causality / simultaneity — Y also causes X (price and quantity "
     "are set together; concentration may be the result of competition, not "
     "its cause).", 0),
    ("Omitted-variable bias — a confounder in ε that drives both X and Y "
     "(demand shocks that lift both price and quantity).", 0),
    ("Errors-in-variables — X is mismeasured, biasing β toward zero "
     "(attenuation).", 0),
    "All three break E[ε|X]=0 -> β is biased and inconsistent. No amount of "
    "data fixes it.",
    "The cure is design (a credible comparison/experiment or instrument), not "
    "a bigger model.",
], footer=FT)

d.bullets("Violations 2 — heteroskedasticity & autocorrelation", [
    "Heteroskedasticity — error variance changes with X (variance of firm "
    "prices grows with firm size). β stays unbiased; the SEs are wrong.",
    "Autocorrelation — errors correlated over time or within groups (the same "
    "firm/region across years).",
    "Fix the inference, not the estimate: robust (heteroskedasticity-"
    "consistent) SEs; clustered SEs when observations group (cluster on "
    "firm/market).",
    "These are inference repairs. They do NOT rescue an endogenous β — a "
    "precise estimate of a biased number is still wrong.",
], footer=FT)

d.bullets("When design fails — instruments, and their limits", [
    "When you cannot avoid endogeneity by design, an instrumental variable "
    "can rescue β: a variable Z that shifts X but is otherwise unrelated to Y "
    "(affects Y only through X).",
    "Example: a cost shifter (exogenous input price) instruments for price "
    "when estimating demand — it moves price but not the demand curve.",
    "Two requirements: relevance (Z strongly predicts X — beware weak "
    "instruments) and exclusion (Z affects Y ONLY through X — untestable, "
    "must be argued).",
    "IV is second-best: it trades the endogeneity problem for an exclusion "
    "assumption the other side will attack. A clean natural experiment beats "
    "a clever instrument.",
], footer=FT)

d.bullets("Reading regression output", [
    "t = coef / SE. Roughly |t| > 2 => significant at 5%.",
    "95% CI = β ± 1.96 · SE. Report the interval, not just the star — it "
    "shows the range of the effect.",
    "F-test — joint significance of several coefficients (does the model "
    "explain anything? are these dummies jointly zero?).",
    "R² / adjusted R² — share of variance explained; adjusted-R² penalises "
    "extra regressors. High R² ≠ valid causal β.",
    "RMSE — typical prediction error in the units of Y; the scale of what the "
    "model leaves unexplained.",
], footer=FT)

d.formula("Difference-in-differences — the workhorse design",
          "Compare the change in a treated group to the change in an untreated "
          "control over the same period; the control differences out anything "
          "common to both:",
          ["DiD = (Y_treat,after − Y_treat,before)",
           "        − (Y_ctrl,after − Y_ctrl,before)"],
          ["Parallel-trends assumption: absent treatment, treated and control "
           "would have moved together — check pre-trends.",
           "Cluster the SEs on the treatment unit; with few clusters, use "
           "randomisation / permutation inference.",
           "Why tribunals like it: the comparison is transparent and "
           "falsifiable — you can see the control and test the trends."],
          footer=FT)

d.case_box("Ashenfelter in US v. Apple (e-books)", "US",
           "A textbook DiD expert report — assume liability, find a control, "
           "quantify, stress-test",
           ["Setup: assume the alleged conspiracy; compare the 6 months either "
            "side of the agency-model switch.",
            "Control: Random House did not join initially -> a clean control "
            "publisher inside the same market.",
            "DiD = change in conspiring-publisher e-book prices minus change "
            "in Random House prices.",
            "Result: roughly a 16.8% price increase and about 14.5% fewer "
            "books sold for the conspiring publishers.",
            "Robustness: re-run across windows, retailers, and datasets — a "
            "finding that moves with the window is one the defence will "
            "break."],
           "A textbook DiD expert report: assume liability, find a credible "
           "control inside the market, quantify, then stress-test.",
           footer=FT)

d.formula("Event studies / the market model",
          "Isolate the effect of an event (merger announcement, agency "
          "action, stock-drop) on returns, netting out the market:",
          ["R_it = α + β · R_mt + ε     (estimate on a clean window)",
           "AR = actual − predicted; CAR = ΣAR; t = CAR / σ"],
          ["Estimation window fits α, β before the event; the event window "
           "measures the abnormal return (AR) the event caused.",
           "CAR cumulates ARs over the event window; the t-stat tests whether "
           "it differs from zero.",
           "Uses: merger announcements (does the market expect higher "
           "prices?), agency actions, and securities stock-drop cases."],
          footer=FT)

d.code_demo("Code as demo — the market model",
            "Book Ch. 6. Fit on the estimation window, predict the event "
            "window, read the abnormal return.",
            ["source(\"program/R/helpers.R\")",
             "# estimation window: fit the market model on pre-event returns",
             "m  <- lm(r_firm ~ r_mkt, data = est_window)",
             "# event window: predicted 'normal' return, then abnormal return",
             "pred <- predict(m, newdata = event_window)",
             "ar   <- event_window$r_firm - pred        # abnormal returns",
             "car  <- sum(ar)                           # cumulative AR",
             "tval <- car / (sd(residuals(m)) * sqrt(length(ar)))"],
            "The abnormal return is what the model did NOT expect — the "
            "market's read on the event, net of the market move.",
            footer=FT)

d.case_box("Kamita — airline antitrust immunity (JOLE 2010)", "US",
           "An exogenous legal change as a natural experiment",
           ["Natural experiment: the DOT granted Hawaii interisland carriers "
            "temporary antitrust immunity, Dec 2002 – Oct 2003, letting them "
            "coordinate openly.",
            "Treat immunity as the treatment; compare immunised routes to "
            "interisland control routes (DiD).",
            "Finding: prices rose under immunity and stayed elevated ~2.5 "
            "years after it ended — coordination outlived the legal shelter.",
            "Lesson: a policy switch is a free experiment; control routes make "
            "the counterfactual credible, and persistence after removal is "
            "itself evidence of coordination."],
           "Shows how an exogenous legal change becomes a clean identification "
           "strategy — exactly what a tribunal can follow.",
           footer=FT)

# ============================================================ MODULE 2.3
d.section("Module 2.3 — Abuse of dominance",
          "§8 / Art. 102 / Sherman §2. First dominance, then the abuse, then "
          "(sometimes) the justification.")

d.bullets("The structure of an abuse case", [
    "Step 1 — Dominance. SA §7 thresholds (Day 1): ≥45% presumed dominant; "
    "35–45% dominant unless it disproves market power; <35% only if proven. "
    "EU ~40%+ with barriers, AKZO presumption at 50%; US §2 ~70%+.",
    "Step 2 — Abusive conduct. Exclusionary (foreclosing rivals) or "
    "exploitative (excessive pricing — live in SA/EU, largely not in the US).",
    "Step 3 — Effects & justification. Anticompetitive effect vs objective "
    "justification / efficiency; SA §8 distinguishes per se-type and "
    "rule-of-reason abuses.",
    "The economist supplies the foreclosure measure, the cost benchmark, or "
    "the price-vs-competitive-level comparison.",
], footer=FT)

d.bullets("Proving dominance — the evidence", [
    "Market shares first: SA's §7 thresholds make the share number do legal "
    "work directly (≥45% / 35–45% / <35%).",
    "But share is a proxy — corroborate with entry barriers (sunk costs, "
    "regulation, network effects), buyer power, and the durability of the "
    "position over time.",
    "Watch market definition: define too narrowly and everyone is dominant; "
    "too broadly and no one is. The dominance finding lives or dies on Day "
    "1's market definition.",
    "Dynamic check: a high share with easy entry and contestation is weaker "
    "evidence of power than a stable share behind barriers.",
], footer=FT)

d.formula("Predatory pricing — the cost-benchmark logic",
          "Pricing below cost to exclude. The Areeda–Turner benchmarks:",
          ["Price < AVC            -> presumptively predatory",
           "AVC ≤ Price < ATC      -> ambiguous (predatory if exclusion plan)",
           "Price ≥ ATC            -> legal"],
          ["LRAIC (long-run average incremental cost) is the modern benchmark "
           "for multi-product firms; AAC (average avoidable cost) the "
           "short-run one.",
           "The test embodies the AEC ('as-efficient-competitor') logic: "
           "would a rival as efficient as the dominant firm survive these "
           "prices?",
           "Practical pitfall: which cost concept, and whose accounts — the "
           "case often turns on cost allocation."],
          footer=FT)

d.formula("Predatory pricing — the recoupment leg",
          "Below-cost pricing only harms competition if the predator can get "
          "the money back:",
          ["Leg 1: Price below the cost benchmark (above)",
           "Leg 2 (US): recoupment must be plausible"],
          ["US Brooke Group: no recoupment, no claim — below-cost pricing that "
           "can never be recouped just benefits consumers.",
           "Recoupment needs post-exit market power: barriers high enough that "
           "the predator can later raise price and recover the losses.",
           "EU / SA do not impose a strict recoupment gate — below-cost "
           "pricing by a dominant firm can be abuse on the cost test plus an "
           "exclusionary plan.",
           "Same conduct, different test: always anchor predation in the "
           "forum's recoupment posture."],
          footer=FT)

d.formula("Margin squeeze (vertically integrated dominant firm)",
          "A firm dominant in an input squeezes downstream rivals who must "
          "buy that input from it:",
          ["Squeeze if:  P_retail − P_wholesale < downstream cost",
           "i.e. the firm's own retail arm couldn't profit at its own "
           "wholesale price"],
          ["This is the AEC test applied to a two-level structure — no need "
           "to show below-cost retail pricing in the absolute.",
           "Classic in telecoms (access to the local loop / wholesale "
           "broadband). SA: the Telkom matters.",
           "ECPR (efficient component pricing rule) is the benchmark for the "
           "access price — we return to it on Day 3 (remedies).",
           "Data you need: the wholesale price, the retail price, and the "
           "downstream cost of an efficient entrant."],
          footer=FT)

d.bullets("Exclusion: dealing, tying, and refusal to supply", [
    ("Exclusive dealing / loyalty rebates.", 0),
    ("Foreclose rivals' access to customers/distribution; assessed on the "
     "share foreclosed plus the AEC test for the rebate's effective price.", 1),
    ("Tying / bundling.", 0),
    ("Leverage power in one product to a second — but tying can be efficient, "
     "so effects matter.", 1),
    ("Refusal to deal / essential facilities.", 0),
    ("Narrow in the US after Trinko; EU Bronner / IMS conditions: "
     "indispensability, elimination of competition, no objective "
     "justification; SA uses §8 essential-facility provisions more readily "
     "than US law.", 1),
    "The common thread: measure foreclosure (how much of the market is closed "
    "to an efficient rival), then weigh justifications.",
], footer=FT)

d.bullets("Excessive pricing (the exploitative abuse)", [
    "Exploitative, not exclusionary: charging a price that bears no "
    "reasonable relation to economic value — harm to customers directly, no "
    "rival need be excluded.",
    "Live in SA (§8(1)(a)) and the EU; largely not actionable in the US "
    "(which polices structure/conduct, not price levels).",
    "The hard part is the benchmark for 'economic value': cost-plus-"
    "reasonable-return, comparable markets, or price over time — each "
    "contestable.",
    "This is why excessive-pricing findings are fragile on appeal — the next "
    "two SA cases show exactly that.",
], footer=FT)

d.case_box("Sasol — excessive pricing", "SA",
           "Tribunal found excessive pricing; the CAC SET IT ASIDE (2015)",
           ["Sasol Chemical Industries was found by the Tribunal to have "
            "charged excessive prices for polymers (propylene/polypropylene) "
            "to local converters.",
            "On appeal the Competition Appeal Court SET ASIDE the finding "
            "(2015), faulting the economic-value / cost benchmark used.",
            "Excessive pricing (§8(1)(a)) requires a price that bears no "
            "reasonable relation to economic value — notoriously hard to "
            "prove."],
           "Teach it as good law on the TEST, not standing liability — SA "
           "appellate courts have set findings aside on exactly the benchmark "
           "question.",
           footer=FT)

d.case_box("Media24 — exclusionary (predatory) pricing", "SA",
           "Tribunal finding (2015) later OVERTURNED by the CAC (2019)",
           ["Media24's Forum community newspaper was alleged to have priced to "
            "drive out the rival Gold–Net News in Welkom, then closed Forum "
            "once the rival exited.",
            "The Tribunal found abuse in 2015 on a recoupment-flavoured "
            "theory; on appeal the CAC overturned the finding in 2019.",
            "The litigation refined the SA cost benchmark for predation "
            "(average avoidable cost vs average total cost)."],
           "A second SA appellate reversal — carry the appellate history; the "
           "audience will know it.",
           footer=FT)

d.bullets("Comparative note: the AEC framework is contested abroad", [
    "EU Intel: the 2009 rebates decision and its AEC analysis were annulled "
    "(General Court 2022, affirmed CJEU Oct 2024). Do NOT call the AEC "
    "framework 'settled via Intel' — it was unwound.",
    "US Microsoft (2001): the D.C. Circuit VACATED the tying ruling; the "
    "liability that stood was §2 monopoly maintenance. Cite it for "
    "maintenance, not tying.",
    "Lesson: exclusion tests (AEC, foreclosure shares) are live and "
    "jurisdiction-specific. Anchor your method in the forum's current law, "
    "not a famous old headline.",
], footer=FT)

d.case_box("US v. Microsoft — the conduct (Fisher's analysis)", "US",
           "The canonical §2 monopoly-maintenance case",
           ["Monopoly power: ~95% of Intel-compatible PC operating systems; "
            "sustained high margins; the 'applications barrier to entry' "
            "(developers write for Windows because users are on Windows) "
            "protects the position — MIT's Franklin Fisher for the DOJ.",
            "The browser threat: Netscape + Java threatened a cross-platform "
            "layer that would erode the applications barrier — so Microsoft "
            "moved to foreclose it.",
            "The conduct: bundling IE into Windows at zero marginal price; OEM "
            "restrictions (no removing IE / promoting rivals); exclusive ISP & "
            "content deals; technical integration — 'embrace, extend, "
            "extinguish'."],
           "The harm was to the competitive process and innovation (maintaining "
           "the OS monopoly), not a simple price rise — the template for "
           "platform-monopoly theory.",
           footer=FT)

d.case_box("US v. Microsoft — findings, remedy, legacy", "US",
           "A won §2 case that ended in a behavioural remedy",
           ["Findings of fact (Jackson J., Nov 1999): monopoly power established; "
            "exclusionary conduct harmed consumers, degraded quality, stifled "
            "innovation.",
            "Remedy whiplash: a 2000 order to break Microsoft in two (OS vs. "
            "applications) was reversed on appeal (D.C. Cir. 2001) — which also "
            "vacated the tying ruling but upheld §2 maintenance — and remanded.",
            "2001 settlement: behavioural only (API disclosure, OEM freedom, "
            "uniform licensing, anti-retaliation; 10-year consent decree).",
            "Legacy: the structural-vs-behavioural remedy debate; the line from "
            "Microsoft to Google (search/ad-tech) to Apple/Amazon app-store and "
            "self-preferencing."],
           "Even a won §2 case can end in a behavioural remedy a court can "
           "administer — and the appellate record, not the headline, is what "
           "you cite.",
           footer=FT)

# ============================================================ MODULE 2.4
d.section("Module 2.4 — Antitrust and labour markets",
          "Buyer power over workers: monopsony is the mirror image of "
          "monopoly.")

d.bullets("Employer market power — the spectrum", [
    ("Competitive — many employers; a worker who quits is instantly rehired "
     "at the same wage; firms are wage-takers.", 0),
    ("Oligopsony — a few large employers in a local market; some wage-setting "
     "power, strategic interaction.", 0),
    ("Monopsony — a dominant buyer of labour faces the whole upward-sloping "
     "supply curve and sets the wage.", 0),
    "The mirror of product-market power: monopoly raises price by restricting "
    "output; monopsony lowers the wage by restricting hiring.",
    "Geography is decisive: labour markets are local and occupation-specific, "
    "so power concentrates far more than product-market shares suggest.",
], footer=FT)

d.formula("Monopsony and the wage markdown",
          "A dominant employer faces an upward-sloping labour supply curve, so "
          "it holds wages below the value workers add:",
          ["wage / MRPL = η / (1 + η)",
           "η = firm-level labour-supply elasticity"],
          ["MRPL = marginal revenue product of labour (what the worker adds).",
           "η = 2 → wage = 2/3 of MRPL → a 33% markdown. As η → ∞ "
           "(competitive), wage → MRPL.",
           "A firm can be tiny in its product market yet dominant as a BUYER "
           "of local labour — the only large hospital in a rural commuting "
           "zone.",
           "The markdown is the labour analogue of the Lerner index (Day 1): "
           "less elastic supply => bigger wedge."],
          footer=FT)

d.formula("Labour-market concentration (labour HHI)",
          "Define the market as occupation × commuting zone, then apply the "
          "same HHI:",
          ["Labour HHI = Σ (employment share_i)²"],
          ["2023 Merger Guidelines flag concentration at HHI 1,800 (the 2010 "
           "figure was 2,500).",
           "Many US local labour markets exceed 3,000 — highly concentrated "
           "(Azar–Marinescu–Steinbaum).",
           "Same arithmetic as product-market HHI; the work is defining the "
           "geography (commute) and the occupation correctly.",
           "A merger can be benign in the product market but anticompetitive "
           "in the labour market — review both."],
          footer=FT)

d.bullets("Conduct: no-poach, wage-fixing, non-competes", [
    "No-poach agreements between employers (incl. across franchisees) and "
    "wage-fixing — the US DOJ treats naked versions as per se criminal, like "
    "price-fixing.",
    "Reality check: Jindal (physical therapists) — jury ACQUITTED on the "
    "Sherman counts; DaVita — defendants ACQUITTED (2022). Hard to win "
    "criminally, but the cases reshaped compliance.",
    "Non-competes bind workers post-employment (~18% of US workers); they cut "
    "mobility and shave wages. The FTC's 2024 ban was SET ASIDE (Ryan v. "
    "FTC); the appeal was dropped (2025) -> back to case-by-case enforcement.",
    "Information sharing on pay (benchmarking surveys, algorithms) can "
    "facilitate coordination short of an explicit agreement.",
], footer=FT)

d.bullets("SA hook & the monopsony evidence", [
    "Healthcare Market Inquiry: a few hospital groups hold >80% of private "
    "beds -> a structural monopsony over nurses and clinical labour in many "
    "regions.",
    "The same concentration that raises prices to patients also depresses "
    "wages to clinical staff — one structure, two harms.",
    "SA tools reach this through market inquiries and §8 dominance in the "
    "buying market — the buyer-power case is statutorily available.",
    "For the expert: build the labour HHI by occupation × region, then "
    "connect concentration to the wage markdown implied by the supply "
    "elasticity.",
], footer=FT)

d.code_demo("Code as demo — labour HHI and the markdown",
            "Book Ch. 10. Same helper as product markets.",
            ["source(\"program/R/helpers.R\")",
             "shares   <- c(50, 30, 20)        # hiring shares, %",
             "hhi      <- sum(shares^2)        # 3800  -> concentrated",
             "eta      <- 2                    # labour-supply elasticity",
             "markdown <- 1 - eta/(1+eta)      # 0.333 -> 33% below MRPL"],
            "HHI 3,800 (> 1,800) and a 33% markdown: concentration and the "
            "wage gap tell the same story.",
            footer=FT)

# ============================================================ MODULE 2.5
d.section("Module 2.5 — Digital markets and platforms",
          "Multi-sided, data-rich, fast-moving. New measurement problems, "
          "familiar theories of harm.")

d.bullets("What makes platforms different", [
    "Multi-sided: value on one side depends on the other (buyers/sellers, "
    "users/advertisers, riders/drivers).",
    ("Network effects — direct (more users -> more value to users), indirect "
     "(more users -> more sellers), and data network effects (more use -> "
     "better product).", 0),
    "Switching costs and lock-in keep users put even when a rival is better.",
    "Together these tip markets toward winner-take-all and durable, "
    "hard-to-contest positions ('gatekeeper' power).",
    "Implication: a high share can be both a sign of quality AND a barrier — "
    "the analysis has to separate the two.",
], footer=FT)

d.bullets("...and what doesn't (familiar theories of harm)", [
    "The conduct is old friends in new clothes: self-preferencing "
    "(leverage/discrimination), exclusion via defaults, tying/bundling, "
    "refusal to interoperate.",
    "Zero price on one side breaks the SSNIP — use SSNDQ (small but "
    "significant DECREASE in quality: ad load, data extraction, degraded "
    "service) and watch the OTHER side's price.",
    "Defaults move behaviour even when switching is nominally free — the "
    "central empirical fact of the search cases.",
    "So the toolkit transfers: define the market (carefully, around zero "
    "prices), measure foreclosure / favouritism, weigh justifications.",
], footer=FT)

d.bullets("Market power at a zero price", [
    "A free service can still wield power — over the paying side "
    "(advertisers) and over quality to users.",
    "SSNDQ replaces SSNIP: would a hypothetical monopolist profitably impose "
    "a small but significant decrease in quality (more ads, more data "
    "extraction, worse defaults)?",
    "Gatekeeper power: the platform controls a bottleneck between two sides — "
    "users can't reach sellers, or sellers can't reach users, except through "
    "it.",
    "Measure power by the other side's terms (commission rates, ad load) and "
    "by dependence (what share of a seller's sales runs through the "
    "platform) — not by the user-side price of zero.",
], footer=FT)

d.formula("Measuring self-preferencing and default effects",
          "Two workhorse measurements:",
          ["Ranking harm:  Δclicks = (CTR_top − CTR_demoted) × queries",
           "Default effect: event-study / DiD around a choice-screen change"],
          ["Top organic result captures ~25–35% of clicks; demotion to "
           "position ~4 is a large traffic loss even at equal quality.",
           "Self-preferencing test: regress rank (or visibility) on quality "
           "AND an own-product dummy — the dummy coefficient is the "
           "favouritism, net of quality.",
           "Defaults: a DiD around the introduction/removal of a choice "
           "screen isolates how much share moves when the default changes.",
           "These are the same regression and DiD tools from Module 2.2, "
           "pointed at clicks and shares."],
          footer=FT)

d.bullets("The enforcement record is now 2024–2026 — US", [
    "US v. Google (search): liability Aug 2024; remedies Sept 2025 — "
    "default-exclusivity bans and data-sharing, NO Chrome divestiture.",
    "US v. Google (ad tech): §2 liability (2025) — publisher ad server + ad "
    "exchange.",
    "Epic v. Apple: 2025 contempt ruling barred Apple's 27% off-app surcharge "
    "and anti-steering 'scare screens'.",
    "The US model is case-by-case litigation — slow, fact-intensive, remedy "
    "fights that run for years after liability.",
], footer=FT)

d.bullets("The enforcement record — EU & SA", [
    "EU Google Shopping: self-preferencing finding affirmed (CJEU 2024) — "
    "the European anchor for ranking-discrimination harm.",
    "DMA (ex ante gatekeeper rules): non-compliance fines — Apple €500M, "
    "Meta €200M (Apr 2025). Rules apply before harm is proven.",
    "SA — OIPMI final report (2023): Takealot marketplace ranking vs its own "
    "retail arm, food-delivery commissions ~25–30%, Google >90% SA search "
    "share.",
    "OIPMI remedies: fair-ranking reporting, anti-steering relief, "
    "data/visibility transparency — a forward-looking remedy package, not a "
    "litigated abuse finding.",
], footer=FT)

d.bullets("Three models, side by side", [
    ("SA — market inquiries: investigative, forward-looking remedies, fast "
     "for moving markets; reaches harms without a contested abuse finding.", 0),
    ("EU — DMA: ex ante obligations on designated gatekeepers; harm presumed "
     "from the structure, enforced by fines.", 0),
    ("US — litigation: ex post case-by-case under Sherman §2; high proof "
     "burden, long remedy phase.", 0),
    "For the expert: the measurement is the same (ranking, defaults, "
    "foreclosure); what differs is what you must prove and when — frame your "
    "number to the forum.",
], footer=FT)

d.case_box("Online Intermediation Platforms Market Inquiry (OIPMI)", "SA",
           "Self-preferencing and platform dependence, SA-style remedies",
           ["Final report (2023): e-commerce (Takealot marketplace ranking "
            "vs. its own retail arm), food delivery (commissions ~25–30%), "
            "online travel, and Google's >90% SA search share.",
            "Remedies: fair-ranking reporting, anti-steering relief for "
            "restaurants, and data/visibility transparency.",
            "A market-inquiry remedy package, not a litigated abuse finding — "
            "the SA tool of choice for fast-moving digital markets."],
           "SA reaches platform harms through market inquiries with "
           "forward-looking remedies, in parallel with the EU's ex ante DMA — "
           "both contrast with US case-by-case litigation.",
           footer=FT)

# ============================================================ CLOSE
d.takeaways("Day 2 — what you should now be able to do", [
    "Lay out a cartel case: per se status, a screen to run, and a "
    "before/after overcharge — and state whether passing-on is available in "
    "the forum.",
    "Use the econometric backbone: read an OLS output, spot endogeneity, and "
    "run a DiD or event study a tribunal can follow.",
    "Structure an abuse case (dominance -> conduct -> justification) and apply "
    "the cost/AEC test to predation and margin squeeze.",
    "Carry the SA appellate history: Sasol set aside (2015), Media24 "
    "overturned (2019); treat Intel's AEC analysis as unwound and Microsoft "
    "as §2 maintenance.",
    "Compute a labour HHI and a wage markdown; apply old theories of harm to "
    "platforms with SSNDQ and ranking/default measurement, framed to the "
    "forum (SA inquiry vs EU DMA vs US litigation).",
], footer=FT)

d.exercise("Day 2 — exercises (worked answers in the key)", [
    "1.  Overcharge & damages: commerce R200m, overcharge rate 15%. Single "
    "damages? US treble exposure? Why might the SA number differ?",
    "2.  Read a DiD: treated prices 100->120, control 100->105. What is the "
    "DiD estimate, and what assumption lets you call it causal?",
    "3.  Wage markdown: hiring shares 50/30/20. Compute the labour HHI. With "
    "η = 2, what is the markdown vs MRPL?",
    "4.  Ranking harm: CTR 35% at position 1, 8% at position 4; a rival "
    "demoted 1->4 on 1,000,000 queries. Lost clicks?",
    "5.  Margin-squeeze strategy: a vertically integrated SA telco is accused "
    "of margin squeeze. State the test, the two prices you need, and one "
    "objective justification the firm might raise.",
], deliverable="Exercises 1–4 are checkable arithmetic; 5 is a one-paragraph "
   "strategy note. Key provided.", footer=FT)

out = d.save("slides/day2_conduct.pptx")
print("saved", out, "slides:", len(d.prs.slides._sldIdLst))
