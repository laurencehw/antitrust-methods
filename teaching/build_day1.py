"""Day 1 — Foundations: institutions, evidence, markets, and power.
Maps to book chapters 1 (orientation), 2 (research design),
3 (market definition), 4 (IO toolkit). SA-forward, concept-first."""

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
], footer=FT)

d.bullets("South Africa: the institutions", [
    "Competition Act 89 of 1998 (as amended, incl. 2019 Amendment Act).",
    ("Competition Commission — investigates, screens mergers, refers cases.", 0),
    ("Competition Tribunal — adjudicates (Pretoria); decides large mergers and "
     "prohibited-practice referrals.", 0),
    ("Competition Appeal Court (CAC) — hears appeals; several headline economic "
     "findings have been set aside on appeal.", 0),
    "Distinctive features: a statutory public-interest test in merger review, "
    "and market inquiries as a standing tool (Grocery Retail, Healthcare, "
    "Online Intermediation Platforms).",
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
          ["US: 'monopoly power', in practice inferred above ~70% share.",
           "EU: 'dominance', in practice from ~40% with entry barriers; "
           "rebuttable presumption at 50% (AKZO).",
           "Why it matters: in SA the share number does legal work directly — "
           "the economist's market-share estimate can decide the burden."],
          footer=FT)

d.bullets("The same conduct, three regimes", [
    "Object vs. effects: EU Art. 101 treats 'object' restrictions as "
    "presumptively restrictive (101(3) exemption still formally available); "
    "US separates per se from rule of reason; SA §4(1)(b) lists per se "
    "horizontal practices.",
    "Public interest: SA uniquely weighs employment, SME participation, "
    "spread of ownership (incl. by historically disadvantaged persons) in "
    "merger review — a merger can be cleared on competition grounds and still "
    "conditioned, or blocked, on public interest.",
    "Private enforcement: US allows treble damages; SA/EU frameworks are "
    "narrower (SA: follow-on civil claims after a Tribunal finding).",
    "Practitioner habit: map the same theory of harm to each regime's "
    "statutory test early, and build a separate legal-economic narrative for "
    "each forum.",
], footer=FT)

# ============================================================ MODULE 1.2
d.section("Module 1.2 — Research design & the evidence triad",
          "From intake to remedy: where the economics enters.")

d.bullets("The evidence triad — the spine of the whole course", [
    "Every matter is built from three kinds of evidence, and good work "
    "integrates all three rather than over-relying on one.",
    ("Empirical — quantitative estimation (prices, shares, diversion, "
     "damages).", 0),
    ("Documentary — internal memos, board decks, emails ('hot docs'), "
     "discovery.", 0),
    ("Expert judgment — translating the first two into the legal standard the "
     "tribunal must apply.", 0),
    "We will return to this triad in every session. By Day 3 you should "
    "instinctively ask of any claim: which leg of the triad supports it?",
], footer=FT)

d.bullets("The investigation workflow: intake → remedy", [
    ("Intake — complaint, leniency application, or merger notification; "
     "triage 'hot docs' and quick descriptive analytics.", 0),
    ("Scoping — inventory data systems, prioritise custodians, run early "
     "screens (margins, shares/HHI, diversion) before costly data work.", 0),
    ("Analysis — test theories: market definition, unilateral/coordinated "
     "effects, DiD / IV / simulation, married to documents.", 0),
    ("Decision & remedy — statement of issues, then forward-looking remedy "
     "design within institutional constraints.", 0),
    "At each hand-off, ask the marginal-return question: does the next dollar "
    "buy more data work, or better documentary / testimonial evidence?",
], footer=FT)

d.two_col("Mapping economics onto the legal elements",
          "Economic question",
          ["Relevant market", "Market power / dominance", "Theory of harm",
           "Efficiencies / pro-competitive justification", "Remedy"],
          "Legal element it serves",
          ["Defines shares, the field of analysis",
           "An element of every abuse / §2 / Art. 102 case",
           "The causal mechanism the agency must prove",
           "The rebuttal / §4(1) or 101(3) defence",
           "Must be effective AND administrable by the Tribunal"],
          footer=FT)

d.code_demo("Code as demo — the multi-jurisdiction timeline",
            "Book Ch. 1, figure 'antitrust-timeline'. Run live or show output.",
            ["library(ggplot2); source(\"program/R/helpers.R\")",
             "milestones <- tribble(",
             "  ~year, ~event,              ~type,     ~jurisdiction,",
             "  1998,  \"Competition Act 89\", \"Statute\", \"SA\",",
             "  2019,  \"SA Amendment Act\",   \"Statute\", \"SA\",",
             "  2023,  \"US Merger Guidelines\",\"Guidance\",\"US\", ...)",
             "ggplot(milestones, aes(year, y, colour = jurisdiction)) + ...",
             "  theme_antitrust()"],
            "SA's 1998 Act drew on EU precedent; the 2023 US Guidelines moved "
            "toward EU-style structural presumptions — convergence over time.",
            footer=FT)

# ============================================================ MODULE 1.3
d.section("Module 1.3 — Market definition",
          "The market is not given; it is contested. It fixes the shares, the "
          "theory of harm, and the remedy.")

d.formula("The hypothetical monopolist test (SSNIP)",
          "Start with a candidate market. Ask: could a hypothetical "
          "monopolist over just these products profitably impose a SSNIP — a "
          "Small but Significant Non-transitory Increase in Price (typically "
          "5–10%)?",
          ["If YES → the candidate market IS a relevant market",
           "If NO  → widen the market and test again"],
          ["The test mechanises the question 'what constrains this firm?'.",
           "In zero-price digital markets, use SSNDQ — a Small but Significant "
           "Non-transitory Decrease in Quality (ad load, data extraction).",
           "Geographic and product dimensions are tested the same way."],
          footer=FT)

d.formula("Critical loss analysis — and the fallacy to avoid",
          "A SSNIP is profitable if the sales actually lost are smaller than "
          "the most you could afford to lose:",
          ["Critical loss  CL = t / (t + m)",
           "t = SSNIP size,   m = gross margin"],
          ["Example: t = 5%, m = 40% → CL = 5/(5+40) = 11.1%.",
           "If ACTUAL loss < CL → SSNIP profitable → market is well "
           "defined (do NOT widen).",
           "If ACTUAL loss > CL → SSNIP unprofitable → widen the "
           "candidate market.",
           "THE FALLACY: high margins give a LOW critical loss — but high "
           "margins often go with LOW actual loss too. Citing only the low "
           "critical loss to claim a narrow market is the classic error "
           "(O'Brien–Wickelgren; Katz–Shapiro)."],
          footer=FT)

d.bullets("Two traps the tribunal will test you on", [
    ("The Cellophane fallacy.", 0),
    ("At the prevailing (already-monopolised) price, other products look like "
     "substitutes — but only because the price is already supra-competitive. "
     "Define the market at the COMPETITIVE price, not the current one. Central "
     "wherever you start from an abuse/§8/Art. 102 allegation.", 1),
    ("Brown Shoe practical indicia.", 0),
    ("Beyond the SSNIP arithmetic, courts look at peculiar uses, distinct "
     "customers, distinct prices, specialised vendors, industry recognition. "
     "Useful when the data are thin.", 1),
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
           "law — know which standard a cited case used."],
          footer=FT)

d.code_demo("Code as demo — HHI in two lines",
            "Book helper calc_hhi_change(). Shares as decimals.",
            ["source(\"program/R/helpers.R\")",
             "shares <- c(A=0.40, B=0.30, C=0.20, D=0.10)",
             "calc_hhi_change(shares, merging_firms = c(\"C\",\"D\"))",
             "#> pre_hhi   3000",
             "#> post_hhi  3400",
             "#> delta_hhi  400   # = 2 * 20 * 10"],
            "Pre 3,000; post 3,400; Δ 400. Both triggers met (>1,800 and "
            ">100) → structural presumption. This is your live warm-up.",
            footer=FT)

d.case_box("Grocery Retail Market Inquiry", "SA",
           "Market definition + concentration in everyday retail",
           ["Inquiry into national supermarket chains (Shoprite, Pick n Pay, "
            "Spar, Woolworths) and the long-term exclusive lease agreements in "
            "shopping centres.",
            "Exclusivity clauses foreclosed entry by rivals and informal "
            "traders — a market-definition and barriers-to-entry question, not "
            "a price-fixing one.",
            "Illustrates SSNIP/critical-loss reasoning and the public-interest "
            "lens (SME and township-trader participation) in one matter."],
           "Market definition is where the public-interest story and the "
           "competition story first meet in SA practice.",
           footer=FT)

# ============================================================ MODULE 1.4
d.section("Module 1.4 — The IO toolkit",
          "Elasticities, margins, diversion, pass-through — the parameters "
          "every later method consumes.")

d.formula("Elasticity and the Lerner index",
          "Market power shows up in the gap between price and marginal cost. "
          "For a profit-maximising firm:",
          ["L = (P − MC) / P = − 1 / ε"],
          ["L is the Lerner index (the margin); ε is the firm's own-price "
           "elasticity of demand.",
           "Inelastic demand (small |ε|) → high margin → market "
           "power. This links a measurable margin to an elasticity.",
           "Caveat: a high margin alone is not proof of power — it can reflect "
           "fixed-cost recovery or quality. Pair it with the other evidence."],
          footer=FT)

d.formula("Diversion ratios — the engine of unilateral-effects analysis",
          "When product 1's price rises, where do its lost sales go? The "
          "diversion ratio to product 2:",
          ["D₁₂ = (sales gained by 2) / (sales lost by 1)"],
          ["If 1 and 2 are owned by merging firms, sales 'lost' to 2 are "
           "recaptured — so the merged firm has less reason to compete on "
           "price. That is the unilateral-effects mechanism (Day 3).",
           "Estimated from switching data, win/loss data, surveys, or a demand "
           "model. It feeds UPP and GUPPI directly.",
           "Aggregate diversion (sum to all merging products) gauges overall "
           "recapture."],
          footer=FT)

d.bullets("Pass-through — and a trap to avoid", [
    "Pass-through = how much of a cost change reaches price. It converts an "
    "overcharge or merger cost-saving into a price effect, and it is central "
    "to cartel damages (Day 2) and efficiencies (Day 3).",
    ("Estimate in changes / log-differences with lags — NOT on price/cost "
     "index LEVELS.", 0),
    ("Regressing one trending index on another (e.g. CPI on PPI in levels) is "
     "the spurious-regression trap: you get a tight fit that means nothing. "
     "First-difference, then estimate.", 1),
    "Rule of thumb under linear demand: a merger's first-order price effect "
    "≈ pass-through × UPP (≈ UPP/2). State the assumption.",
], footer=FT)

d.bullets("Day 1 live-demo toolbox (book helpers)", [
    "calc_hhi_change(shares, merging_firms) — HHI, post-HHI, ΔHHI.",
    "run_logit_sim(products, merging_firms) — static logit merger simulation "
    "(we use it on Day 3).",
    "theme_antitrust() / scale_colour_antitrust() — consistent figures.",
    "fetch_fred() — pull a real concentration or price series (needs key).",
    "All live in program/R/helpers.R; each concept above is roughly one "
    "function call.",
], footer=FT)

# ============================================================ CLOSE
d.takeaways("Day 1 — what you should now be able to do", [
    "Name the SA institutions and statutory tests, and map any conduct to §4 / "
    "§5 / §8 / §9 / §12 and to its US and EU homes.",
    "State the SA §7 dominance thresholds from memory and explain why the "
    "share estimate does legal work.",
    "Run the hypothetical-monopolist test, compute critical loss, and avoid "
    "both the Cellophane and the critical-loss fallacies.",
    "Compute HHI and ΔHHI and apply the 2023 structural presumption.",
    "Read off the four IO parameters — elasticity, margin/Lerner, diversion, "
    "pass-through — that every later method consumes.",
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
], deliverable="Exercises 1–2 are checkable arithmetic; 3–4 are "
   "one-paragraph answers. Key provided.", footer=FT)

out = d.save("slides/day1_foundations.pptx")
print("saved", out, "slides:", len(d.prs.slides._sldIdLst))
