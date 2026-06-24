"""Day 2 — Conduct: cartels, abuse of dominance, labour, digital.
Maps to book chapters 5 (cartels), 7 (monopolization), 10 (labour),
9 (digital). SA-forward, concept-first. Corrected facts per the audit:
Sasol excessive-pricing finding SET ASIDE by CAC (2015); Media24 finding
overturned by CAC (2019); Intel rebates/AEC finding annulled; Microsoft
tying VACATED (liability was s2 maintenance); Jindal acquitted on Sherman
counts; DaVita acquitted (2022)."""

from deck_builder import Deck, BLUE, GREEN, ORANGE, RED, PURPLE, GREY, DARK

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
    "Per se / by-object: no need to prove market power or effects — the "
    "agreement itself is the violation. The economics shifts from 'is there "
    "harm?' to 'screening' and 'damages'.",
    "The hard part is proof of the agreement. Leniency programmes turn "
    "insiders into witnesses; economics corroborates the documentary record.",
    "Economist's two jobs: (1) screens that flag suspicious behaviour, "
    "(2) quantifying the overcharge for damages.",
], footer=FT)

d.bullets("Cartel screens — what to compute before you have a confession", [
    ("Variance / structural-break screens.", 0),
    ("Cartels stabilise prices, then prices jump when the cartel breaks. "
     "Bai–Perron and CUSUM tests date the breaks; a sharp drop in price "
     "variance during the suspected period is a flag.", 1),
    ("Bid-rotation / market-allocation screens.", 0),
    ("In procurement: who wins in turn, suspiciously similar losing bids, "
     "bid spreads that are too tight. Needs bid-LEVEL data (every bid), not "
     "just who won.", 1),
    ("Margin / parallel-pricing screens.", 0),
    ("Co-moving prices across rivals beyond what common costs explain.", 1),
    "A screen is an investigative aid, never proof — it survives "
    "cross-examination only when tied to documents and testimony.",
], footer=FT)

d.formula("Quantifying the overcharge (before/after method)",
          "Compare cartel-period prices to a competitive benchmark, then "
          "convert to damages:",
          ["Overcharge $ = (P_cartel − P_benchmark) × volume",
           "Damages = pass-through × overcharge rate × commerce"],
          ["Benchmark from a clean 'before'/'after' window (validate with a "
           "structural-break test) or a yardstick market.",
           "Pass-through matters when buyers are intermediaries who passed the "
           "overcharge downstream (Day 1 trap: estimate in changes).",
           "US: treble damages (×3). SA: follow-on civil claims after a "
           "Tribunal finding."],
          footer=FT)

d.bullets("Standing & the passing-on defence — know the split", [
    ("United States.", 0),
    ("Illinois Brick: only DIRECT purchasers may claim federal damages. "
     "Hanover Shoe: a defendant may NOT reduce damages by arguing the direct "
     "purchaser passed the overcharge on. (Many states differ — Illinois "
     "Brick repealers.)", 1),
    ("EU and South Africa.", 0),
    ("The passing-on defence IS available, and indirect purchasers can in "
     "principle claim — so quantifying pass-through is central, not barred.", 1),
    "This is the first thing a litigator looks for in a damages dispute — "
    "get the jurisdiction's rule right before you model.",
], footer=FT)

d.case_box("The bread cartel", "SA",
           "Leniency + documents + pricing analysis, with real victims",
           ["Premier Foods applied for leniency; implicated Tiger Brands, "
            "Pioneer and others in fixing the price of bread (2007).",
            "Documentary and testimonial evidence established the agreement; "
            "pricing analysis quantified the overcharge on a staple food.",
            "Pioneer paid penalties and made price commitments; the matter "
            "anchored SA follow-on damages and the public salience of cartels "
            "(Children's Resource Centre class action)."],
           "The template SA cartel matter: leniency cracks it open, economics "
           "sizes the harm, and the harm lands on poor households.",
           footer=FT)

d.case_box("The construction 'fast-track' settlement", "SA",
           "Bid rigging across an industry, resolved by settlement",
           ["The Commission's fast-track process (settled 2013) covered bid "
            "rigging on major projects, including 2010 World Cup stadiums.",
            "15 firms settled for penalties totalling about R1.46 billion.",
            "Shows the bid-rotation screen logic at industry scale and the use "
            "of a settlement mechanism to resolve many linked bids at once."],
           "When rigging is industry-wide, a structured settlement can do what "
           "case-by-case prosecution cannot.",
           footer=FT)

d.code_demo("Code as demo — a before/after overcharge",
            "Book Ch. 5. Structural break dates the cartel; the gap is the "
            "overcharge.",
            ["# prices: cartel window vs clean benchmark window",
             "p_cartel    <- mean(price[period == \"cartel\"])",
             "p_benchmark <- mean(price[period == \"after\"])",
             "overcharge_rate <- (p_cartel - p_benchmark) / p_benchmark",
             "damages_single  <- overcharge_rate * commerce",
             "damages_treble  <- 3 * damages_single   # US only"],
            "Validate the benchmark window with a Bai–Perron break test before "
            "you trust the gap.",
            footer=FT)

# ============================================================ MODULE 2.2
d.section("Module 2.2 — Abuse of dominance",
          "§8 / Art. 102 / Sherman §2. First dominance, then the abuse, then "
          "(sometimes) the justification.")

d.bullets("The structure of an abuse case", [
    "Step 1 — Dominance. SA: the §7 thresholds (Day 1). EU: ~40%+ with "
    "barriers, AKZO presumption at 50%. US §2: monopoly power, ~70%+.",
    "Step 2 — Abusive conduct. Exclusionary (foreclosing rivals) or "
    "exploitative (excessive pricing — live in SA/EU, largely not in the US).",
    "Step 3 — Effects & justification. Anticompetitive effect vs. objective "
    "justification / efficiency; in SA, §8 distinguishes per se-type and "
    "rule-of-reason abuses.",
    "The economist supplies the foreclosure measure, the cost benchmark, or "
    "the price-vs-competitive-level comparison.",
], footer=FT)

d.formula("Predatory pricing: the as-efficient-competitor logic",
          "Pricing below cost to exclude, expecting to recoup later. Two legs:",
          ["Leg 1: Price < cost benchmark (AVC / AAC / LRAIC)",
           "Leg 2 (US): recoupment must be plausible (Brooke Group)"],
          ["EU AKZO presumptions: below AVC presumed predatory; between AVC "
           "and ATC predatory if part of an exclusion plan.",
           "US Brooke Group adds a recoupment screen — no recoupment, no "
           "claim. SA looks to cost benchmarks without a strict recoupment "
           "gate.",
           "The AEC ('as-efficient competitor') test: would a rival as "
           "efficient as the dominant firm survive these prices?"],
          footer=FT)

d.formula("Margin squeeze (vertically integrated dominant firm)",
          "A firm dominant in an input squeezes downstream rivals who must buy "
          "that input from it:",
          ["Squeeze if:  P_retail − P_wholesale < downstream cost",
           "i.e. the firm's own retail arm couldn't profit at its own "
           "wholesale price"],
          ["This is the AEC test applied to a two-level structure.",
           "Classic in telecoms (access to the local loop). SA: the Telkom "
           "matters on wholesale broadband access.",
           "ECPR (efficient component pricing rule) is the benchmark for what "
           "the access price should be — we return to it on Day 3 (remedies)."],
          footer=FT)

d.bullets("Exclusion: dealing, tying, and refusal to supply", [
    ("Exclusive dealing / loyalty rebates.", 0),
    ("Foreclose rivals' access to customers or distribution; assessed on the "
     "share of the market foreclosed and the AEC test for rebates.", 1),
    ("Tying / bundling.", 0),
    ("Leverage power in one product to a second.", 1),
    ("Refusal to deal / essential facilities.", 0),
    ("Narrow in the US after Trinko; recognised in the EU (Bronner / IMS "
     "Health conditions: indispensability, elimination of competition, no "
     "objective justification); SA uses §8 refusal-to-supply / essential-"
     "facility provisions more readily than US law.", 1),
], footer=FT)

d.case_box("Sasol — excessive pricing", "SA",
           "Tribunal found excessive pricing; the CAC SET IT ASIDE (2015)",
           ["Sasol Chemical Industries was found by the Tribunal to have "
            "charged excessive prices for polymers (propylene/polypropylene) "
            "to local converters.",
            "On appeal the Competition Appeal Court SET ASIDE the finding "
            "(2015), faulting the economic value / cost benchmark used.",
            "Excessive pricing (§8(1)(a)) requires a price that bears no "
            "reasonable relation to economic value — notoriously hard to prove."],
           "Excessive-pricing cases turn on the value benchmark, and SA "
           "appellate courts have set findings aside on exactly that point. "
           "Teach it as good law on the TEST, not as a standing liability.",
           footer=FT)

d.case_box("Media24 — exclusionary (predatory) pricing", "SA",
           "Tribunal finding (2015) later overturned by the CAC (2019)",
           ["Media24's Forum community newspaper was alleged to have priced to "
            "drive out the rival Gold–Net News in Welkom, then closed Forum.",
            "The Tribunal found abuse in 2015 on a recoupment-flavoured "
            "theory; on appeal the CAC overturned the finding in 2019.",
            "The litigation refined the SA cost benchmark for predation "
            "(average avoidable cost vs. average total cost)."],
           "A second SA appellate reversal — when teaching SA abuse cases, "
           "carry the appellate history, because the audience will know it.",
           footer=FT)

d.bullets("Comparative note: the AEC framework is contested abroad", [
    "EU Intel: the original 2009 rebates decision and its AEC analysis were "
    "annulled (General Court 2022, affirmed CJEU Oct 2024). Do NOT cite "
    "'the AEC framework established in Intel' as settled — it was unwound.",
    "US Microsoft (2001): the D.C. Circuit VACATED the tying ruling; the "
    "liability that stood was §2 monopoly maintenance. Cite it for "
    "maintenance, not tying.",
    "Lesson for the expert: exclusion tests (AEC, foreclosure shares) are "
    "live and jurisdiction-specific. Anchor your method in the forum's "
    "current law, not a famous old headline.",
], footer=FT)

# ============================================================ MODULE 2.3
d.section("Module 2.3 — Antitrust and labour markets",
          "Buyer power over workers: monopsony is the mirror image of "
          "monopoly.")

d.formula("Monopsony and the wage markdown",
          "A dominant employer faces an upward-sloping labour supply curve, so "
          "it holds wages below the value workers add:",
          ["wage / MRPL = η / (1 + η)",
           "η = firm-level labour-supply elasticity"],
          ["MRPL = marginal revenue product of labour (what the worker adds).",
           "η = 2 → wage = 2/3 of MRPL → a 33% markdown. As η → ∞ "
           "(competitive), wage → MRPL.",
           "A firm can be tiny in its product market yet dominant as a BUYER "
           "of local labour — e.g. the only large hospital in a rural "
           "commuting zone."],
          footer=FT)

d.formula("Labour-market concentration (labour HHI)",
          "Define the market as occupation × commuting zone, then apply the "
          "same HHI:",
          ["Labour HHI = Σ (employment share_i)²"],
          ["2023 Merger & labour guidelines use the 1,800 concentration "
           "threshold (the 2010 figure was 2,500).",
           "Many US local labour markets exceed 3,000 — highly concentrated "
           "(Azar–Marinescu–Steinbaum).",
           "Same arithmetic as product-market HHI; the work is defining the "
           "geography (commute) and the occupation."],
          footer=FT)

d.bullets("The conduct: no-poach, wage-fixing, non-competes", [
    "No-poach agreements between employers (incl. across franchisees) — the "
    "US DOJ treats naked no-poach and wage-fixing as per se criminal, like "
    "price-fixing.",
    "Non-competes bind workers post-employment; ~18% of US workers; they "
    "reduce mobility and shave wages. The FTC's 2024 ban was set aside in "
    "court (Ryan v. FTC, 2024) and the FTC dropped the appeal (2025) — back "
    "to case-by-case enforcement.",
    "US enforcement reality check: Jindal (physical therapists) — jury "
    "ACQUITTED on the Sherman counts; DaVita (no-poach) — defendants "
    "ACQUITTED (2022). Hard to win criminally, but the cases reshaped "
    "compliance.",
    "SA hook: the Healthcare Market Inquiry documented a small number of "
    "hospital groups (>80% of beds) — a structural monopsony over nurses and "
    "clinical labour in many regions.",
], footer=FT)

d.code_demo("Code as demo — labour HHI and the markdown",
            "Book Ch. 10. Same helper as product markets.",
            ["shares <- c(50, 30, 20)             # hiring shares, %",
             "hhi <- sum(shares^2)                # 3800  -> concentrated",
             "eta <- 2                            # labour-supply elasticity",
             "markdown <- 1 - eta/(1+eta)         # 0.333 -> 33% below MRPL"],
            "HHI 3,800 (> 1,800) and a 33% markdown: concentration and the "
            "wage gap tell the same story.",
            footer=FT)

# ============================================================ MODULE 2.4
d.section("Module 2.4 — Digital markets and platforms",
          "Multi-sided, data-rich, fast-moving. New measurement problems, "
          "familiar theories of harm.")

d.bullets("What makes platforms different (and what doesn't)", [
    "Multi-sided: value depends on the other side (buyers/sellers, "
    "users/advertisers, riders/drivers); network effects and switching costs "
    "feed market power.",
    "Zero price on one side breaks the SSNIP — use SSNDQ (quality decrease: "
    "ad load, data extraction) and watch the OTHER side's price.",
    "But the theories of harm are old friends: self-preferencing (a form of "
    "leverage/discrimination), exclusion via defaults, tying, refusal to "
    "interoperate.",
    "Defaults move behaviour even when switching is nominally free — the "
    "central empirical fact of the search cases.",
], footer=FT)

d.formula("Measuring self-preferencing and default effects",
          "Two workhorse measurements:",
          ["Ranking harm:  Δclicks = (CTR_top − CTR_demoted) × queries",
           "Default effect: event-study / DiD around a choice-screen change"],
          ["Top organic result captures ~25–35% of clicks; demotion to "
           "position ~4 is a large traffic loss even at equal quality.",
           "Self-preferencing test: regress rank (or visibility) on quality "
           "AND an own-product dummy — the dummy is the favouritism.",
           "Defaults: a DiD around the introduction of a choice screen "
           "isolates how much share moves when the default is removed."],
          footer=FT)

d.bullets("The enforcement record is now 2024–2026 — keep it current", [
    "US v. Google (search): liability Aug 2024; remedies Sept 2025 — "
    "default-exclusivity bans and data-sharing, NO Chrome divestiture.",
    "US v. Google (ad tech): §2 liability 2025 (publisher ad server + "
    "exchange).",
    "EU: Google Shopping affirmed (CJEU 2024); DMA non-compliance fines — "
    "Apple €500M, Meta €200M (Apr 2025); ex ante gatekeeper rules vs. the US "
    "case-by-case model.",
    "Epic v. Apple: 2025 contempt ruling barred Apple's 27% off-app "
    "surcharge and anti-steering 'scare screens'.",
], footer=FT)

d.case_box("Online Intermediation Platforms Market Inquiry (OIPMI)", "SA",
           "Self-preferencing and platform dependence, SA-style remedies",
           ["Final report (2023) covered e-commerce (Takealot marketplace "
            "ranking vs. its own retail arm), food delivery (commissions "
            "~25–30%), online travel, and Google's >90% search share.",
            "Remedies pointed at fair-ranking reporting, anti-steering relief "
            "for restaurants, and data/visibility transparency.",
            "A market-inquiry remedy package, not a litigated abuse finding — "
            "the SA tool of choice for fast-moving digital markets."],
           "SA reaches platform harms through market inquiries with "
           "forward-looking remedies, in parallel with the EU's ex ante DMA — "
           "both contrast with US case-by-case litigation.",
           footer=FT)

# ============================================================ CLOSE
d.takeaways("Day 2 — what you should now be able to do", [
    "Lay out a cartel case: per se status, a screen to run, and a before/after "
    "overcharge — and state whether passing-on is available in the forum.",
    "Structure an abuse case (dominance → conduct → justification) and apply "
    "the AEC test to predation and margin squeeze.",
    "Carry the SA appellate history: Sasol set aside (2015), Media24 "
    "overturned (2019), and treat Intel's AEC analysis as unwound.",
    "Compute a labour HHI and a wage markdown, and explain how a firm can be "
    "small in product but dominant in labour.",
    "Apply old theories of harm to platforms with SSNDQ and ranking/default "
    "measurement, and place SA market inquiries against the EU DMA and US "
    "litigation.",
], footer=FT)

d.exercise("Day 2 — exercises (worked answers in the key)", [
    "1.  Overcharge & damages: commerce R200m, overcharge rate 15%. Single "
    "damages? US treble exposure? Why might the SA number differ?",
    "2.  Wage markdown: three employers with hiring shares 50/30/20. Compute "
    "the labour HHI. With η = 2, what is the markdown vs. MRPL?",
    "3.  Ranking harm: CTR 35% at position 1, 8% at position 4; a rival is "
    "demoted 1→4 on 1,000,000 queries. Lost clicks?",
    "4.  Abuse strategy: a vertically integrated SA telco is accused of margin "
    "squeeze. State the test, the two prices you need, and one objective "
    "justification the firm might raise.",
], deliverable="Exercises 1–3 are checkable arithmetic; 4 is a "
   "one-paragraph strategy note. Key provided.", footer=FT)

out = d.save("slides/day2_conduct.pptx")
print("saved", out, "slides:", len(d.prs.slides._sldIdLst))
