"""Day 1 — Foundations: institutions, evidence, markets, and power.
Maps to book chapters 1 (orientation), 2 (research design),
3 (market definition), 4 (IO toolkit). SA-forward, concept-first.

Mirrors slides/day1.qmd slide-for-slide, in the same order. The .qmd is
authoritative; keep this file in sync with it."""

from deck_builder import Deck, BLUE, GREEN, ORANGE, RED, PURPLE, GREY, DARK

FT = "Day 1 · Foundations"
d = Deck("Day 1 — Foundations",
         "Institutions, evidence, market definition, and market power")

# ============================================================ MODULE 1.1
d.section("Module 1.1 — The competition-law landscape",
          "Institutions first, methods second. We start from South Africa.")

d.bullets("Why institutions come before methods", [
    "Economic analysis answers to legal standards, agency priorities, and "
    "procedural rules — and all three vary by jurisdiction.",
    "Get the frame right and your analysis speaks to the questions that decide "
    "a matter, not the ones that are merely interesting.",
    ("Three questions to ask of any matter:", 0),
    ("Who enforces the law here?", 1),
    ("What must they prove (the legal elements)?", 1),
    ("Where does the economics enter (which element does my number go to)?", 1),
    "Same number, different jobs: a 48% share is presumed dominance in SA, "
    "probably dominant in the EU, not yet monopoly power in the US.",
    "The economist who skips this step produces beautiful estimates that "
    "answer the wrong legal question.",
], footer=FT)

d.bullets("South Africa: the institutions", [
    "Competition Act 89 of 1998 (as amended, incl. 2019 Amendment Act).",
    ("Competition Commission — investigates, screens mergers, refers cases, "
     "runs market inquiries.", 0),
    ("Competition Tribunal — adjudicates (Pretoria); decides large mergers and "
     "prohibited-practice referrals.", 0),
    ("Competition Appeal Court (CAC) — hears appeals; several headline economic "
     "findings have been set aside on appeal (Sasol, Media24).", 0),
    "Distinctive features: a statutory public-interest test in merger review, "
    "and market inquiries as a standing tool.",
    "Regional reach: conduct affecting SADC markets is squarely in scope.",
], footer=FT)

d.table("The Competition Act, by conduct type",
        ["Conduct", "South Africa", "United States", "EU"],
        [["Cartels / horizontal", "§4 (per se: §4(1)(b))", "Sherman §1", "Art. 101"],
         ["Abuse of dominance", "§8", "Sherman §2", "Art. 102"],
         ["Vertical restraints", "§5; §8(1)(d) if dominant", "Sherman §1 (RoR)", "Art. 101 + VBER"],
         ["Mergers", "§12, §12A (+ public interest §12A(3))", "Clayton §7", "EUMR 139/2004"],
         ["Price discrimination", "§9 (by dominant firm)", "Robinson-Patman", "Art. 102(c)"]],
        col_widths=[2.6, 3.9, 2.9, 2.9],
        note="Note: vertical restraints fall under §5 (and §8(1)(d) for a "
             "dominant firm), NOT the per se horizontal provision §4(1)(b).",
        footer=FT)

d.formula("Dominance thresholds are statutory in South Africa (§7)",
          "Unlike the US 'monopoly power' inference or the EU's practice-based "
          "approach, SA fixes the thresholds in the statute:",
          ["≥ 45%  → presumed dominant",
           "35–45%  → dominant UNLESS it shows it lacks market power",
           "< 35%  → dominant only if market power is proven"],
          ["The thresholds shift the burden of proof, not just the label.",
           "At ≥45% the firm must disprove dominance; in the 35–45% band it "
           "must disprove market power; below 35% the complainant must prove it.",
           "Why it matters: in SA the share number does legal work directly — "
           "the economist's market-share estimate can decide who carries the "
           "burden."],
          footer=FT)

d.two_col("Dominance abroad: a comparison",
          "United States (Sherman §2)",
          ["'Monopoly power' — power to control price or exclude competition.",
           "No statutory number; courts infer it, in practice above ~70% share.",
           "Alcoa (90% = monopoly; 60–64% doubtful; 33% no).",
           "Always paired with durable entry barriers."],
          "EU (Art. 102)",
          ["'Dominance' — to behave independently of competitors and customers.",
           "In practice from ~40% with entry barriers.",
           "AKZO: a 50% share is a rebuttable presumption of dominance.",
           "Structure plus barriers, not share alone."],
          lcolor=BLUE, rcolor=ORANGE, footer=FT)

d.bullets("Object vs. effects — the deep structure", [
    "EU Art. 101: 'object' restrictions (price-fixing, market-sharing) are "
    "presumptively restrictive — no effects proof needed, though 101(3) "
    "exemption is formally available.",
    "US: the per se vs. rule of reason split; naked horizontal restraints are "
    "per se, most else gets full effects analysis.",
    "SA §4(1)(b): a closed list of per se horizontal practices (price-fixing, "
    "market division, collusive tendering) — no efficiency defence at all.",
    "The economist's role disappears on liability for per se / object conduct "
    "and reappears only for remedy and damages. Knowing which regime you are "
    "in tells you whether your model matters.",
], footer=FT)

d.bullets("Public interest — the SA distinctive", [
    "SA merger review weighs competition AND public interest as a co-equal "
    "limb (§12A(3)).",
    "The statutory limbs: employment, SME participation, spread of ownership "
    "(esp. by historically disadvantaged persons), effect on a particular "
    "industrial sector or region, and national-industry export competitiveness.",
    "A merger can be cleared on pure competition grounds and still be "
    "conditioned or blocked on public interest (Walmart/Massmart conditions; "
    "Burger King/Grand Parade prohibition).",
    "This widens the evidence the economist must marshal — beyond price and "
    "shares to employment and ownership effects.",
], footer=FT)

d.bullets("Market inquiries — the SA power tool", [
    "A market inquiry is a forward-looking, industry-wide study with the power "
    "to impose remedies — not a litigated abuse finding.",
    "It suits fast-moving or structurally troubled markets where case-by-case "
    "litigation is too slow.",
    ("Three landmark SA inquiries:", 0),
    ("Grocery Retail — exclusive leases foreclosing entry by rivals and "
     "informal traders.", 1),
    ("Health Market Inquiry — concentrated funders and facilities; recommended "
     "a supply-side regulator.", 1),
    ("Online Intermediation Platforms (OIPMI) — ranking, self-preferencing, "
     "commissions on digital platforms.", 1),
    "Why it matters: SA reaches harms via inquiry + remedy where the US would "
    "litigate — a different toolkit for the same theories.",
], footer=FT)

d.bullets("Burden and standard of proof", [
    "Standard: competition matters are civil — proof on the balance of "
    "probabilities (not 'beyond reasonable doubt'), except SA criminalised "
    "cartel conduct for individuals (§73A).",
    "Burden shifts with structure: SA §7 thresholds move the burden; per se / "
    "object conduct removes the effects burden entirely.",
    "Prima facie then rebuttal: the agency makes out the elements; the firm "
    "raises efficiency / objective-justification defences.",
    "For the economist: know which element your number serves and who must "
    "prove it — that determines whether you are building the case or the "
    "rebuttal.",
], footer=FT)

# ============================================================ MODULE 1.2
d.section("Module 1.2 — Research design & the evidence triad",
          "From intake to remedy: where the economics enters.")

d.bullets("The evidence triad — the spine of the course", [
    "Every matter is built from three kinds of evidence; good work integrates "
    "all three.",
    ("Empirical — quantitative estimation (prices, shares, diversion, "
     "damages).", 0),
    ("Documentary — internal memos, board decks, emails ('hot docs'), "
     "discovery.", 0),
    ("Expert judgment — translating the first two into the legal standard.", 0),
    "The three corroborate each other: a screen flags conduct, a document "
    "explains it, the expert ties it to the statutory element.",
    "We return to this triad in every session. Of any claim, ask: which leg "
    "supports it?",
], footer=FT)

d.bullets("The investigation workflow: intake → remedy", [
    ("Intake — complaint, leniency application, or merger notification; "
     "triage 'hot docs' + quick analytics.", 0),
    ("Scoping — inventory data systems, prioritise custodians, run early "
     "screens (margins, shares/HHI, diversion).", 0),
    ("Analysis — test theories: market definition, unilateral/coordinated "
     "effects, DiD / IV / simulation, married to documents.", 0),
    ("Decision & remedy — statement of issues, then forward-looking remedy "
     "within institutional constraints.", 0),
    "At each hand-off: does the next dollar buy more data or better "
    "documents/testimony?",
], footer=FT)

d.two_col("Mapping economics onto the legal elements",
          "Economic question",
          ["Relevant market", "Market power / dominance", "Theory of harm",
           "Efficiencies / justification", "Remedy"],
          "Legal element it serves",
          ["Defines shares, the field of analysis",
           "An element of every abuse / §2 / Art. 102 case",
           "The causal mechanism the agency must prove",
           "The rebuttal / §4(1) or 101(3) defence",
           "Must be effective AND administrable by the Tribunal"],
          footer=FT)

d.bullets("How to read an expert report (1): question & data", [
    ("Research question. What exactly is being estimated, and how does it link "
     "to the legal element and to the prior literature? A report with no clear "
     "question is advocacy in a lab coat.", 0),
    ("The data. Where do they come from (collection process, selection)? "
     "Beware sample selection.", 0),
    ("Variables. Distinguish the outcome (dependent) variable from the "
     "explanatory variables — and ask whether the explanatory ones are "
     "themselves caused by the outcome.", 0),
    ("Unit of observation. Firm? store? transaction? market-week? The unit "
     "determines what variation identifies the effect and how to cluster "
     "standard errors.", 0),
], footer=FT)

d.bullets("How to read an expert report (2): the empirical strategy", [
    ("Ideal data vs. available data. What experiment would answer the "
     "question, and how far does the actual data fall short?", 0),
    ("Identification. What variation is being used to separate the causal "
     "effect from confounders? Name the source.", 0),
    ("Sources of exogenous variation. A policy change, a weather shock, a "
     "discontinuity, an instrument — something that moves the treatment but "
     "not the outcome directly.", 0),
    ("How much identification comes from the model? The more the answer leans "
     "on functional-form and distributional assumptions rather than on data "
     "variation, the more fragile it is — and the more you probe.", 0),
], footer=FT)

d.bullets("How to read an expert report (3): technique & conclusions", [
    ("The main equation. Write it down. What is the coefficient of interest, "
     "and in what units?", 0),
    ("Exogenous vs. endogenous regressors. Which right-hand-side variables are "
     "plausibly random, which are choices?", 0),
    ("What is in the error term? Anything correlated with the regressor and "
     "the outcome biases the estimate — name the omitted variables.", 0),
    ("Instruments & validity. Relevance (correlated with the endogenous "
     "variable) AND exclusion (affects the outcome only through it). Exclusion "
     "is an assumption, not a test.", 0),
    ("Conclusions & alternatives. State the most plausible alternative "
     "interpretation of the same result — then ask whether the report rules "
     "it out.", 0),
], footer=FT)

d.bullets("'Ideal data' thinking and the counterfactual", [
    "Every causal claim is a comparison to a counterfactual: what would the "
    "outcome have been but for the conduct/merger?",
    "The counterfactual is never observed — we estimate it.",
    "The gold standard for building it is random assignment: treatment and "
    "control differ only by chance, so differences in outcomes are caused by "
    "treatment.",
    "Most competition data is observational: firms and prices are not randomly "
    "assigned, so we must engineer a credible counterfactual from the "
    "variation we do have.",
    "The whole methods course is: how do we build a defensible counterfactual "
    "when we cannot randomise?",
], footer=FT)

d.bullets("The credibility revolution", [
    "A shift (1990s onward) from elaborate structural assumptions toward "
    "research designs that isolate exogenous variation.",
    ("RCTs — randomise treatment directly (rare in antitrust, common in "
     "policy).", 0),
    ("Natural experiments — nature/policy randomises for you. Mariel boatlift "
     "(1980): a sudden labour-supply shock to Miami used to estimate "
     "immigration's wage effect.", 0),
    ("Quasi-experiments — a discontinuity or staggered rollout approximates "
     "randomisation.", 0),
    "Leamer's critique: 'Let's take the con out of econometrics' — fragile "
    "results that flip with the specification. The fix is design, not "
    "post-hoc robustness patches: a good design survives reasonable "
    "specifications.",
], footer=FT)

d.table("Observational data structures → methods",
        ["Data structure", "Typical method", "What it controls"],
        [["Cross-section", "Multiple regression w/ controls", "Observed confounders only"],
         ["Time series", "Event study", "Pre/post around a date"],
         ["Panel (firm × time)", "Fixed effects; DiD", "Time-invariant unobservables + common shocks"],
         ["Panel + comparison", "Matching / PSM", "Observable selection"],
         ["Sharp threshold", "RDD", "Local randomisation at the cutoff"],
         ["Instrument available", "IV", "Endogeneity of the regressor"]],
        col_widths=[3.0, 4.3, 5.0],
        note="Map the data structure to the method BEFORE estimating. The "
             "design dictates the assumption you must defend.",
        footer=FT)

d.bullets("Threats to validity, by design", [
    ("RCT — check balance: are treatment and control similar on pre-treatment "
     "covariates? Attrition can re-introduce selection.", 0),
    ("IV — the exclusion restriction: the instrument must affect the outcome "
     "only through the endogenous variable. Untestable; argue it "
     "institutionally.", 0),
    ("DiD — parallel trends: absent treatment, treated and control would have "
     "moved together. Inspect pre-trends; worry about differential shocks.", 0),
    ("RDD — no bunching/manipulation at the cutoff (McCrary density test); the "
     "effect is local to the threshold, not global.", 0),
    "Naming the threat for your own design first is the mark of a credible "
    "report.",
], footer=FT)

d.two_col("Structural IO vs. reduced form",
          "Structural (BLP-style)",
          ["Estimate demand (elasticities, diversion) + a conduct model, then "
           "simulate the merger.",
           "Predicts effects of an event that hasn't happened.",
           "Heavy on assumptions: functional form, equilibrium, instruments "
           "for prices.",
           "Used when no clean experiment exists (most prospective mergers)."],
          "Reduced form (clean design)",
          ["e.g. Hastings (2004) gasoline: a vertical change used as a natural "
           "experiment on retail prices.",
           "Transparent, few assumptions, credible for the event observed.",
           "Limited external validity; can't simulate counterfactual mergers.",
           "Used when good exogenous variation exists."],
          lcolor=PURPLE, rcolor=GREEN, footer=FT)

d.bullets("Institutional details and the Scheffman best practice", [
    "Institutional details matter. Contracts, regulation, procurement rules, "
    "and how prices are actually set often determine the right model — and "
    "sometimes settle the question without econometrics.",
    "Scheffman (FTC) best practice: the most persuasive evidence is frequently "
    "descriptive quantitative — prices, shares, margins, shipments, bid data — "
    "clearly presented.",
    "Make assumptions least favourable to your own case. If the conclusion "
    "holds under conservative assumptions, it is robust; if it needs the "
    "favourable ones, the tribunal will notice.",
    "Fancy methods do not rescue a weak descriptive picture; they amplify a "
    "strong one.",
], footer=FT)

d.code_demo("Code as demo — the multi-jurisdiction timeline",
            "Book Ch. 1, figure 'antitrust-timeline'. Run live or show output.",
            ["library(ggplot2); source(\"program/R/helpers.R\")",
             "milestones <- tibble::tribble(",
             "  ~year, ~event,              ~type,     ~jurisdiction,",
             "  1998,  \"Competition Act 89\", \"Statute\", \"SA\",",
             "  2019,  \"SA Amendment Act\",   \"Statute\", \"SA\",",
             "  2023,  \"US Merger Guidelines\",\"Guidance\",\"US\")",
             "ggplot(milestones, aes(year, 0, colour = jurisdiction)) +",
             "  geom_point(size = 4) + theme_antitrust()"],
            "SA's 1998 Act drew on EU precedent; the 2023 US Guidelines moved "
            "toward EU-style structural presumptions — convergence over time.",
            footer=FT)

# ============================================================ MODULE 1.3
d.section("Module 1.3 — Market definition",
          "The market is not given; it is contested. It fixes the shares, the "
          "theory of harm, and the remedy.")

d.bullets("Why market definition comes first", [
    "The relevant market fixes the shares, the field for HHI, the dominance "
    "inference, and the set of constraints on the firm.",
    "It is contested, not given: defendants widen it (more competitors, lower "
    "shares); agencies narrow it (fewer, higher).",
    "Two dimensions, tested the same way: product (which products compete?) "
    "and geographic (where?).",
    "A wrong market definition can sink an otherwise sound theory of harm — "
    "get it right before you estimate effects.",
], footer=FT)

d.formula("The hypothetical monopolist test (SSNIP)",
          "Start with a candidate market. Could a hypothetical monopolist over "
          "just these products profitably impose a SSNIP — a Small but "
          "Significant Non-transitory Increase in Price (typically 5–10%)?",
          ["If YES → the candidate market IS a relevant market",
           "If NO  → widen the market and test again"],
          ["The test mechanises the question 'what constrains this firm?'.",
           "Iterate: keep adding the next-closest substitute until a SSNIP "
           "would be profitable.",
           "In zero-price digital markets, use SSNDQ — a Small but Significant "
           "Non-transitory Decrease in Quality (ad load, data extraction)."],
          footer=FT)

d.formula("Critical loss — the arithmetic",
          "A SSNIP is profitable if the sales actually lost are smaller than "
          "the most you could afford to lose:",
          ["Critical loss  CL = t / (t + m)",
           "t = SSNIP size,   m = gross margin"],
          ["Example: t = 5%, m = 40% → CL = 5/(5+40) = 11.1%.",
           "If ACTUAL loss < CL → SSNIP profitable → market is well "
           "defined (do NOT widen).",
           "If ACTUAL loss > CL → widen the candidate market.",
           "The two ingredients: an accounting margin and a demand estimate of "
           "the actual loss."],
          footer=FT)

d.bullets("The critical-loss fallacy", [
    "High margins give a LOW critical loss — which looks like it favours a "
    "narrow market.",
    "BUT high margins typically go with LOW actual loss too (a firm with "
    "pricing power faces inelastic demand).",
    "Citing only the low critical loss to claim a narrow market — without "
    "checking the actual loss — is the classic error (O'Brien–Wickelgren; "
    "Katz–Shapiro).",
    "The discipline: always compare actual loss to critical loss; never quote "
    "one in isolation.",
], footer=FT)

d.bullets("The Cellophane fallacy", [
    "From du Pont (cellophane): at the already-monopolised price, other "
    "products look like substitutes — but only because the price is already "
    "supra-competitive.",
    "Define the market at the COMPETITIVE price, not the prevailing one.",
    "Central wherever you start from an abuse / §8 / Art. 102 allegation, "
    "because the conduct under challenge has already moved the price.",
    "The mirror image of the SSNIP: SSNIP starts from a competitive price and "
    "pushes up; the Cellophane trap starts from a monopoly price and is fooled "
    "by the substitution it induced.",
], footer=FT)

d.bullets("Brown Shoe practical indicia", [
    "When the SSNIP arithmetic is data-starved, courts look to qualitative "
    "indicia (Brown Shoe, 1962):",
    ("Industry or public recognition of the market as separate.", 1),
    ("The product's peculiar characteristics and uses.", 1),
    ("Distinct customers and distinct prices.", 1),
    ("Sensitivity to price changes (cross-elasticity).", 1),
    ("Specialised vendors and distinct production facilities.", 1),
    "These corroborate (or undercut) the econometrics — the documentary leg of "
    "the triad applied to market definition.",
], footer=FT)

d.formula("Measuring concentration: HHI",
          "Once the market is defined, measure concentration. The "
          "Herfindahl–Hirschman Index is the sum of squared shares:",
          ["HHI = Σ (share_i)²        ΔHHI = 2 × s₁ × s₂"],
          ["Shares as percentages (so a monopoly = 10,000). The merger short-"
           "cut: ΔHHI from two merging firms = 2 × s₁ × s₂.",
           "2023 US Merger Guidelines structural presumption: post-merger "
           "HHI > 1,800 AND ΔHHI > 100 (or combined share ≥ 30% with "
           "ΔHHI > 100).",
           "The 2010 Guidelines' 1,500/2,500 bands still appear in older case "
           "law — know which standard a cited case used.",
           "HHI is a screen, not a verdict: it flags matters; it does not "
           "prove harm."],
          footer=FT)

d.code_demo("Code as demo — HHI in two lines",
            "Book helper calc_hhi_change(). Shares as decimals.",
            ["source(\"program/R/helpers.R\")",
             "shares <- data.frame(firm=c(\"A\",\"B\",\"C\",\"D\"),",
             "                     share=c(0.40,0.30,0.20,0.10))",
             "calc_hhi_change(shares, merging_firms = c(\"C\",\"D\"))",
             "#> pre_hhi   3000",
             "#> post_hhi  3400",
             "#> delta_hhi  400   # = 2 * 20 * 10"],
            "Pre 3,000; post 3,400; Δ 400. Both triggers met (>1,800 and "
            ">100) → structural presumption. This is your live warm-up.",
            footer=FT)

d.bullets("Deep dive: FTC v. Staples / Office Depot (1997)", [
    "The model market-definition case — the template for unilateral-effects-"
    "plus-econometrics in merger review.",
    "The office-superstore (OSS) format: one-stop shopping, 5,000–7,500 SKUs, "
    "deep discounts (30–70% off list).",
    "The industry consolidated from ~23 chains to 3: Staples, Office Depot, "
    "OfficeMax. The merger would have left two.",
    "The fight was entirely about the market: the FTC said 'office supplies "
    "sold through superstores'; the parties said 'all office-supply retailing' "
    "(Walmart, Best Buy, mail order) — which would have made the merger "
    "trivial.",
], accent=BLUE, footer=FT)

d.bullets("Staples (1): market by retail format", [
    "The relevant market was defined as 'consumable office supplies sold "
    "through office superstores' — by retail format, not by product.",
    "A pen is a pen wherever sold — but the competitive constraint on an OSS "
    "comes overwhelmingly from other OSS, not from Walmart or a corner "
    "stationer.",
    "The conceptual leap: markets can be drawn around a channel of "
    "distribution when that is where the competitive interaction lives.",
    "It reframed 'what is the product?' as 'what constrains the price the "
    "customer actually pays?'",
], accent=BLUE, footer=FT)

d.bullets("Staples (2): four pillars of evidence", [
    ("Distinct products/services — the one-stop superstore offering is a "
     "different shopping experience from mass merchants and mail order.", 0),
    ("Competitive recognition — internal documents labelled markets "
     "'competitive' (another OSS present) vs. 'non-competitive' (OSS-monopoly) "
     "and priced accordingly.", 0),
    ("Pricing constraints — non-OSS retailers (Walmart, Best Buy, warehouse "
     "clubs) did NOT discipline OSS prices.", 0),
    ("Econometric evidence — the hypothetical-monopolist regression predicted "
     "a merged firm could raise prices ~8.49%, exceeding the 5% SSNIP "
     "threshold (18 months of data, 400+ stores, 40+ cities).", 0),
], accent=BLUE, footer=FT)

d.bullets("Staples (3): the price-comparison smoking gun", [
    "Where Staples faced another OSS, prices were dramatically lower than "
    "where it had a local OSS monopoly — the firm's own data, from its own "
    "scanners.",
    "OSS-vs-OSS prices were nearly identical (Detroit basket: Staples $100, "
    "Office Depot $100.4, OfficeMax $102).",
    "A non-OSS like Best Buy ran ~18–19% higher on the same basket → it was "
    "NOT in the same market.",
    "This is the descriptive quantitative evidence Scheffman prizes: the "
    "parties' own prices, plainly arrayed, did most of the work.",
], accent=BLUE, footer=FT)

d.case_box("Staples (4): holding & legacy", "US",
           "Preliminary injunction granted; merger abandoned",
           ["Judge Hogan granted a preliminary injunction (D.D.C. 1997); the "
            "merger was abandoned.",
            "Memorable craft: 'store visits are worth a thousand affidavits' — "
            "get out of the spreadsheet and into the aisle.",
            "Precedent for combining unilateral-effects theory + econometric "
            "and internal-document evidence — later echoed in "
            "Oracle/PeopleSoft, Whole Foods/Wild Oats, T-Mobile/Sprint."],
           "It legitimised the modern merger toolkit — define by the "
           "constraint that actually binds, prove it with the parties' own "
           "data, and let documents corroborate the numbers.",
           footer=FT)

d.case_box("Tying it back to South Africa", "SA",
           "Same SSNIP logic, plus the public-interest lens",
           ["The same SSNIP / critical-loss logic travels — but SA adds the "
            "public-interest lens.",
            "In the Grocery Retail Market Inquiry, the issue was not price-"
            "fixing but long-term exclusive leases foreclosing entry by rivals "
            "and informal/township traders.",
            "Market definition met barriers-to-entry and the spread-of-"
            "participation limb in one matter."],
           "Market definition is where the public-interest story and the "
           "competition story first meet in SA practice.",
           footer=FT)

# ============================================================ MODULE 1.4
d.section("Module 1.4 — The IO toolkit",
          "Elasticities, margins, diversion, pass-through — the parameters "
          "every later method consumes.")

d.bullets("What is market power?", [
    ("Market power = the ability to profitably:", 0),
    ("raise price above marginal cost, or", 1),
    ("restrict output, or", 1),
    ("degrade quality / innovation (the digital-market form).", 1),
    "It is a matter of degree, not a switch — every firm has some; the "
    "question is how much and whether it is durable.",
    "Dominance / monopoly power is market power large and durable enough to "
    "clear the legal threshold (SA §7; EU AKZO; US §2).",
    "Everything in this module is a way to measure that gap or its sources.",
], footer=FT)

d.formula("The Lerner index",
          "Market power shows up in the gap between price and marginal cost. "
          "For a profit-maximising firm:",
          ["L = (P − MC) / P = − 1 / ε"],
          ["L is the Lerner index (the margin); ε is the firm's own-price "
           "elasticity of demand.",
           "Worked example: |ε| = 2 → L = 0.5 → price is double marginal cost. "
           "|ε| = 5 → L = 0.2.",
           "Inelastic demand (small |ε|) → high margin → market power.",
           "Caveat: a high margin alone is not proof of power — it can reflect "
           "fixed-cost recovery or quality. Pair it with other evidence."],
          footer=FT)

d.bullets("Measuring margins in practice", [
    "Price-cost margin (PCM): accounting proxy for the Lerner index from "
    "financial data — but accounting cost ≠ marginal cost.",
    "Tobin's Q: market value / replacement cost of assets; Q ≫ 1 hints at "
    "rents or intangibles, but is noisy and not market-specific.",
    "Production-function markups (De Loecker–Warzynski): μ = output elasticity "
    "/ cost share of a flexible input — estimable without observing marginal "
    "cost directly.",
    "Each measure trades availability against fidelity to the true marginal "
    "cost; triangulate, don't rely on one.",
], footer=FT)

d.bullets("The rise-of-markups debate", [
    "De Loecker–Eeckhout–Unger: estimated average US markups rose from ~21% "
    "over cost (1980) to ~61% (2016), concentrated in the right tail.",
    "A flashpoint: does it show rising market power, or something more benign?",
    ("Alternative explanations:", 0),
    ("Rising fixed/intangible costs (software, R&D, branding) → high markups "
     "over marginal cost but normal profits.", 1),
    ("Quality improvements and changing product mix.", 1),
    ("Globalisation and superstar-firm efficiency.", 1),
    ("Measurement: cost of goods sold vs. total cost changes the answer.", 1),
    "Lesson: a striking aggregate trend still needs a mechanism before it "
    "becomes a finding.",
], footer=FT)

d.bullets("Sources of market power", [
    "Scale economies — high fixed costs, declining average cost (utilities, "
    "networks).",
    "Product differentiation — brand, location, taste; softens price "
    "competition.",
    "Network effects — value rises with users (platforms, payment systems).",
    "Switching costs / lock-in — data, learning, contracts.",
    "Intellectual property — patents, copyrights, trade secrets.",
    "Geography & regulation — the only hospital in a region; licensing limits "
    "on entry.",
    "Data and strategic conduct — accumulated data as a barrier; exclusionary "
    "tactics that create power.",
], footer=FT)

d.two_col("Oligopoly: Cournot vs. Bertrand",
          "Cournot (quantity)",
          ["Firms choose output; price clears the market.",
           "Prices fall between monopoly and competitive as N rises.",
           "Margins ∝ HHI / elasticity — links structure to conduct.",
           "Fits homogeneous goods with capacity choices."],
          "Bertrand (price)",
          ["Firms choose price; lowest price wins.",
           "Bertrand paradox: with identical goods, two firms → price = MC.",
           "Differentiation breaks the paradox → positive margins.",
           "Fits branded consumer goods (most merger work)."],
          lcolor=BLUE, rcolor=ORANGE, footer=FT)

d.bullets("Concentration measures", [
    "CR4 / CRn — combined share of the top n firms; simple, but ignores the "
    "distribution among them.",
    "HHI — sum of squared shares; weights large firms more, so it captures "
    "both the number and the inequality of firms.",
    "Both are structural screens: high concentration raises the question, it "
    "doesn't answer it.",
    "They are inputs to (Cournot) conduct predictions, not substitutes for an "
    "effects analysis — and they depend entirely on the market definition "
    "(Module 1.3).",
], footer=FT)

d.bullets("The four parameters every later method consumes", [
    "Elasticity (ε) — how quantity responds to price; the foundation of "
    "demand and the Lerner index.",
    "Margin / Lerner (L) — the price–cost gap; sizes the incentive to raise "
    "price.",
    "Diversion ratio (D₁₂) — where lost sales go; the engine of unilateral "
    "effects (UPP/GUPPI, Day 3).",
    "Pass-through — how much of a cost change reaches price; converts "
    "overcharges and savings into price effects.",
    "Estimate pass-through in CHANGES, not levels — regressing one trending "
    "index on another (CPI on PPI in levels) is the spurious-regression trap.",
], footer=FT)

d.formula("Diversion and pass-through, defined",
          "Two of the four parameters get their own definitions:",
          ["D₁₂ = (sales gained by 2) / (sales lost by 1)",
           "Pass-through ρ = Δprice / Δcost   (estimate in changes)"],
          ["If 1 and 2 are owned by merging firms, sales 'lost' to 2 are "
           "recaptured → less reason to compete on price (Day 3).",
           "Diversion is estimated from switching data, win/loss records, "
           "surveys, or a demand model; it feeds UPP and GUPPI.",
           "Rule of thumb (linear demand): a merger's first-order price effect "
           "≈ pass-through × UPP (≈ UPP/2). Always state the assumption."],
          footer=FT)

d.bullets("Day 1 live-demo toolbox (book helpers)", [
    "calc_hhi_change(shares, merging_firms) — HHI, post-HHI, ΔHHI (pass a "
    "data.frame).",
    "run_logit_sim(products, merging_firms) — static logit merger simulation "
    "(we use it on Day 3).",
    "theme_antitrust() / scale_colour_antitrust() — consistent figures.",
    "fetch_fred() — pull a real concentration or price series (needs key).",
    "All live in program/R/helpers.R; each concept above is roughly one "
    "function call.",
], footer=FT)

# ============================================================ CLOSE
d.section("Close",
          "What you can now do — and the exercises that prove it.")

d.takeaways("Day 1 — what you should now be able to do", [
    "Map any conduct to §4 / §5 / §8 / §9 / §12 and to its US and EU homes; "
    "know who enforces and what they must prove.",
    "State the SA §7 dominance thresholds from memory and explain why the "
    "share does legal work (it shifts the burden).",
    "Read an expert report by its design: question, data, identification, "
    "technique, and the plausible alternative interpretation.",
    "Build a counterfactual — randomisation ideal, natural/quasi-experiments "
    "in practice; name the threat to validity for your own design.",
    "Run the hypothetical-monopolist test, compute critical loss, and avoid "
    "the Cellophane and critical-loss fallacies (Staples as the model case).",
    "Compute HHI / ΔHHI, apply the 2023 structural presumption, and read off "
    "the four IO parameters: elasticity, margin/Lerner, diversion, "
    "pass-through.",
], footer=FT)

d.exercise("Day 1 — exercises (worked answers in the key)", [
    "1.  HHI & the presumption: shares 40/30/20/10. Compute HHI; the two "
    "smallest merge — post-HHI, ΔHHI; does the 2023 presumption bite?",
    "2.  Critical loss: SSNIP t = 5%, margin m = 35%. Compute CL. If predicted "
    "actual loss is 9%, is the candidate market a relevant market?",
    "3.  Mapping memo: for an exclusive-dealing arrangement by a 48%-share "
    "firm, state the SA / US / EU statutory home and the burden each places "
    "on you.",
    "4.  SA public interest: give one example where §12A(3) changes a merger "
    "outcome that a pure consumer-welfare test would clear.",
    "5.  Optional R lab: read a real concentration series — a rising ratio is "
    "a flag, not a finding.",
], deliverable="Exercises 1–2 are checkable arithmetic; 3–5 are "
   "one-paragraph answers. Key provided.", footer=FT)

out = d.save("slides/day1_foundations.pptx")
print("saved", out, "slides:", len(d.prs.slides._sldIdLst))
