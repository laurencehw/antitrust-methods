"""Day 3 — Mergers, remedies, IP, and litigation, closing with the
hospital-merger capstone. Maps to book chapters 6 (mergers),
8 (regulation/remedies), 11 (innovation/IP), 12 (litigation), 14 (capstone).
SA-forward, concept-first. Capstone numbers verified:
pre-HHI 2,202 / post 3,402 / dHHI 1,200; GUPPI_A 10.3%, GUPPI_B 19.6%."""

from deck_builder import Deck, BLUE, GREEN, ORANGE, RED, PURPLE, GREY, DARK

FT = "Day 3 · Mergers, remedies, IP & litigation"
d = Deck("Day 3 — Mergers, Remedies & Litigation",
         "Predicting effects, fixing harm, IP, and proving it in a tribunal")

# ============================================================ MODULE 3.1
d.section("Module 3.1 — Merger analysis and simulation",
          "Mergers are prospective: we predict effects that have not happened "
          "yet.")

d.bullets("The three theories of merger harm", [
    ("Unilateral effects.", 0),
    ("The merged firm raises price on its own because sales lost to a price "
     "rise are recaptured by the partner (diversion). No coordination needed.", 1),
    ("Coordinated effects.", 0),
    ("The merger makes tacit collusion among the remaining firms easier "
     "(fewer players, more symmetry, more transparency).", 1),
    ("Vertical / conglomerate effects.", 0),
    ("Input foreclosure, customer foreclosure, or leverage across products.", 1),
    "Plus the SA fourth question that can override all three: the "
    "public-interest test (§12A(3)).",
], footer=FT)

d.formula("Unilateral effects: UPP and GUPPI",
          "Screen the price pressure from diversion to the merging partner. "
          "For product A merging with B:",
          ["UPP_A = D_AB × (P_B − C_B) − E_A",
           "GUPPI_A = D_AB × M_B × (P_B / P_A)"],
          ["D_AB = diversion from A to B; (P_B − C_B) = the PARTNER's dollar "
           "margin; E_A = an efficiency credit. Use the partner's margin, not "
           "A's own.",
           "GUPPI expresses the same pressure as a percentage of A's price; "
           "M_B is the partner's percentage margin and (P_B/P_A) rescales.",
           "Rule of thumb: GUPPI above ~5% warrants a closer look. First-order "
           "price rise ≈ pass-through × UPP (≈ UPP/2)."],
          footer=FT)

d.code_demo("Code as demo — a logit merger simulation",
            "Book helper run_logit_sim(). Turns shares + margins + diversion "
            "into predicted price rises.",
            ["source(\"program/R/helpers.R\")",
             "products <- data.frame(",
             "  product=c(\"A\",\"B\",\"C\"), firm=c(\"A\",\"B\",\"C\"),",
             "  price=c(100,95,90), share=c(.4,.35,.25), mc=c(60,58,55))",
             "run_logit_sim(products, merging_firms=c(\"A\",\"B\"))",
             "#> pre/post price, % change, ownership matrix"],
            "Simulation needs a demand model and margins; GUPPI needs only "
            "diversion + margin. Screen with GUPPI, quantify with simulation.",
            footer=FT)

d.bullets("Efficiencies and entry — the rebuttal", [
    "Efficiencies can offset price pressure, but they must be "
    "merger-specific, verifiable, and passed through to consumers — the "
    "burden is on the merging parties.",
    "Marginal-cost savings discipline price; fixed-cost savings usually do "
    "not (they don't change the pricing incentive).",
    "Entry rebuts harm only if it is timely, likely, and sufficient.",
    "In SA, efficiencies and entry sit alongside — and can be outweighed "
    "by — the public-interest assessment.",
], footer=FT)

d.case_box("Walmart / Massmart", "SA",
           "Cleared on competition grounds, fought on public interest",
           ["Walmart's acquisition of Massmart (2011, case 73/LM/Nov10) "
            "raised few horizontal competition concerns.",
            "The battle was public interest: effects on local suppliers and "
            "on jobs. Approved with conditions — a supplier-development fund, "
            "honouring existing labour agreements, and limits on "
            "merger-specific retrenchments (with some reinstatements).",
            "The conditions were litigated up to the CAC, which refined how "
            "public-interest conditions are framed and supervised."],
           "The canonical SA lesson: a merger can pass the competition test "
           "and still be reshaped — or saved — by public-interest conditions.",
           footer=FT)

d.case_box("Burger King (Grand Parade / ECP)", "SA",
           "Prohibited PURELY on a public-interest (ownership) ground",
           ["A foreign private-equity buyer sought to acquire the SA Burger "
            "King franchise from Grand Parade.",
            "The Commission prohibited it in 2021 because it cut shareholding "
            "by historically disadvantaged persons from a high level toward "
            "zero — the first SA merger blocked solely on the spread-of-"
            "ownership limb of public interest.",
            "It was later approved once the parties offered an employee/HDP "
            "ownership and worker commitment."],
           "Public interest is not a tie-breaker bolted onto competition "
           "analysis — in SA it can be the whole case.",
           footer=FT)

# ============================================================ MODULE 3.2
d.section("Module 3.2 — Remedies and regulation",
          "Finding harm is half the job. A remedy must be effective AND "
          "administrable.")

d.two_col("Structural vs. behavioural remedies",
          "Structural",
          ["Divestiture of a business / assets",
           "Clean break; little ongoing monitoring",
           "Preferred where feasible (US/EU default)",
           "Risk: divestiture package too weak to compete"],
          "Behavioural",
          ["Conduct rules: access, pricing, firewalls, non-discrimination",
           "Needs ongoing supervision",
           "Common in SA (public-interest conditions; Tribunal-supervised)",
           "Risk: gaming, monitoring burden, expiry"],
          footer=FT)

d.formula("Access pricing: ECPR and the revenue requirement",
          "When the remedy is access to a bottleneck (telecoms, rail, ports), "
          "you must set a price:",
          ["ECPR access price = direct cost + opportunity cost",
           "Revenue requirement = opex + depreciation + (return × rate base)"],
          ["ECPR (efficient component pricing rule) lets an efficient entrant "
           "in while compensating the incumbent — the benchmark in margin-"
           "squeeze remedies.",
           "Rate regulation builds the allowed revenue from costs plus a fair "
           "return on capital; the contested number is the allowed return.",
           "Benchmarking / yardstick: compare the regulated firm to "
           "comparable firms or regions to discipline its cost claims."],
          footer=FT)

d.case_box("Evanston Northwestern", "US",
           "The canonical BEHAVIOURAL hospital-merger remedy",
           ["A consummated hospital merger found to have raised prices.",
            "Rather than unwind it (structural), the FTC imposed a "
            "behavioural remedy: separate, independent negotiating teams for "
            "the two hospitals when bargaining with insurers.",
            "Shows the trade-off: an effective behavioural fix where "
            "divestiture of an integrated hospital was impractical — at the "
            "cost of ongoing supervision."],
           "When structural relief is impractical, a well-designed conduct "
           "remedy can restore the lost competition — if someone watches it.",
           footer=FT)

# ============================================================ MODULE 3.3
d.section("Module 3.3 — Innovation, IP, and antitrust",
          "Where the right to exclude (a patent) meets the duty not to "
          "exclude (competition law).")

d.formula("Standard-essential patents: hold-up and royalty stacking",
          "Once a standard is set, an SEP holder can hold up implementers; "
          "FRAND commitments are the check.",
          ["Cumulative royalty = Σ (royalty rate_i)"],
          ["Hold-up: threaten an injunction post-adoption to extract supra-"
           "FRAND rates. Hold-out: implementers delay/underpay.",
           "Royalty stacking: 10 SEP holders each asking 5% = 50% of the "
           "device price — manufacturing becomes unprofitable.",
           "Key law: Huawei v. ZTE (EU 2015 negotiation framework); Unwired "
           "Planet (UK 2017, courts will set a global FRAND rate)."],
          footer=FT)

d.bullets("Pay-for-delay and killer acquisitions", [
    ("Reverse-payment ('pay-for-delay') settlements.", 0),
    ("A brand pays a generic to stay out. FTC v. Actavis (US 2013): no 'scope "
     "of the patent' shield — rule of reason, and a large unexplained payment "
     "is itself evidence of anticompetitive intent.", 1),
    ("Killer acquisitions.", 0),
    ("An incumbent buys a nascent rival to shut its pipeline, not for "
     "synergies (Cunningham et al. 2021 estimate ~5–7% of pharma deals). "
     "Test: compare project discontinuation rates, acquired vs. independent.", 1),
    "Watch the appellate record: FTC v. Qualcomm reversed (9th Cir. 2021); "
    "the EU Qualcomm exclusivity fine (€997m) annulled (GC 2022). Cite "
    "outcomes, not headlines.",
], footer=FT)

d.case_box("ARV / pharmaceutical access", "SA",
           "IP, access to medicines, and competition law together",
           ["SA competition complaints over antiretroviral pricing pushed "
            "originators toward voluntary licences expanding generic supply.",
            "Method mix: medicine price data, the patent landscape, and "
            "SAHPRA registration timelines to estimate the harm from delayed "
            "generic entry.",
            "Sits at the intersection of §8 abuse, IP rights, and a pressing "
            "public-health interest."],
           "In SA the IP-vs-competition question is not abstract — it has been "
           "about access to life-saving medicines.",
           footer=FT)

# ============================================================ MODULE 3.4
d.section("Module 3.4 — Litigation practice and expert evidence",
          "Where the evidence triad meets cross-examination.")

d.bullets("Getting expert evidence admitted and believed", [
    ("US — the Daubert gate.", 0),
    ("Four factors: testability/falsifiability, known error rate, peer "
     "review, general acceptance. Build the report to satisfy each.", 1),
    ("Class certification.", 0),
    ("Wal-Mart v. Dukes (commonality: a common question that drives the "
     "answer); Comcast v. Behrend (the damages model must match the theory of "
     "liability and be common to the class).", 1),
    ("South Africa & UK/Australia — concurrent expert evidence ('hot "
     "tubbing').", 0),
    ("Experts are sworn together and answer in turn; a joint statement lists "
     "agreement and disagreement before the hearing. The SA Tribunal's "
     "flexible procedure favours this over rigid Daubert gatekeeping.", 1),
], footer=FT)

d.bullets("Three damages models — and how to defend them", [
    "Before/after: compare the violation period to a clean benchmark window "
    "(validate the break).",
    "Yardstick: compare the affected market to an unaffected comparator "
    "market.",
    "Difference-in-differences: compare changes over time, treated vs. "
    "untreated — the workhorse, with clustered SEs (or randomisation "
    "inference for few clusters).",
    "Reproducibility IS advocacy: a clean /data /scripts /reports bundle with "
    "a lockfile is both scientific best practice and your defence under "
    "cross-examination — run the sensitivity analysis BEFORE opposing counsel "
    "does.",
], footer=FT)

d.formula("Significance and treble damages — the checkable close",
          "The two numbers an expert is asked for on the stand:",
          ["t = coefficient / standard error",
           "US exposure = 3 × (overcharge rate × commerce)"],
          ["t = 2.5 / 0.5 = 5.0 → beyond the 1% critical value (~2.58) → "
           "common impact is statistically significant.",
           "Commerce $200m at a 15% overcharge → $30m single → $90m trebled "
           "(US). In SA, follow-on civil damages without the multiplier.",
           "Always pair the point estimate with its uncertainty — the "
           "tribunal is buying the confidence interval, not just the number."],
          footer=FT)

# ============================================================ CAPSTONE
d.section("Capstone — a hospital merger, end to end",
          "Hospitals A and B propose to merge. Work the evidence triad to a "
          "recommendation.")

d.table("Capstone data (supplied)",
        ["Hospital", "Discharges", "Share", "Price", "Margin"],
        [["A", "30,000", "30%", "$12,000", "40%"],
         ["B", "20,000", "20%", "$11,000", "35%"],
         ["C", "25,000", "25%", "—", "—"],
         ["D", "15,000", "15%", "—", "—"],
         ["E", "6,000", "6%", "—", "—"],
         ["F", "4,000", "4%", "—", "—"]],
        col_widths=[2.4, 2.6, 2.4, 2.4, 2.5],
        note="Diversion: A→B = 0.32, A→C = 0.30, B→A = 0.45. "
             "Total discharges = 100,000. A and B propose to merge.",
        footer=FT)

d.bullets("Capstone — the seven steps", [
    ("1. Market definition — patient-flow / critical-loss reasoning for the "
     "geographic market.", 0),
    ("2. Concentration — HHI, post-merger HHI, ΔHHI.", 0),
    ("3. Diversion — patient-flow ratios vs. share-proportional diversion.", 0),
    ("4. Unilateral effects — GUPPI for A and for B.", 0),
    ("5. Bargaining — Nash-in-Nash: how the merger shifts the disagreement "
     "payoff in insurer negotiations (qualitative here).", 0),
    ("6. Retrospective design — pre-commit a DiD with leads/lags to test the "
     "effect after the fact.", 0),
    ("7. Recommendation — translate to the legal standard (US Clayton §7 / EU "
     "SIEC / SA §12 + §12A(3)) and recommend clear / condition / prohibit.", 0),
], footer=FT)

d.formula("Capstone — the checkable answers (steps 2–4)",
          "These three steps have exact answers; bring them to the memo.",
          ["HHI: pre 2,202 → post 3,402,  ΔHHI = 1,200",
           "GUPPI_A = 0.32 × 0.35 × (11/12) = 10.3%",
           "GUPPI_B = 0.45 × 0.40 × (12/11) = 19.6%"],
          ["ΔHHI = 2 × 30 × 20 = 1,200; post-HHI well above 1,800 → "
           "structural presumption (under either guidelines vintage).",
           "Both GUPPIs exceed the ~5% screen; B's is larger because A is the "
           "bigger, higher-margin recapture target.",
           "Step 7 has no single right answer — it is graded on whether the "
           "numbers are tied correctly to the chosen legal standard."],
          footer=FT)

# ============================================================ CLOSE
d.takeaways("Course close — the habits to keep", [
    "Institutions first: know the forum's test before you pick a method.",
    "The evidence triad: never rest a conclusion on one leg — empirics, "
    "documents, and judgment together.",
    "Screen cheap, quantify dear: GUPPI before simulation, a variance screen "
    "before a full damages model.",
    "Cite outcomes, not headlines: carry the SA and EU appellate history "
    "(Sasol, Media24, Intel, Qualcomm).",
    "In South Africa, public interest can be the whole case — and a remedy is "
    "only as good as the body that can supervise it.",
], footer=FT)

d.exercise("Capstone deliverable", [
    "Write a 2–3 page recommendation memo on the A/B hospital merger.",
    ("Required computations: HHI / ΔHHI, both GUPPIs (show the arithmetic).", 1),
    ("Required reasoning: define the market, classify the unilateral-effects "
     "concern, and address one efficiency or entry rebuttal.", 1),
    ("Required framing: choose ONE jurisdiction (US / EU / SA), state its "
     "legal test, and recommend clear / condition / prohibit — for SA, address "
     "§12A(3) public interest explicitly.", 1),
], deliverable="A tribunal-ready memo: numbers correct, tied to the legal "
   "standard, uncertainty acknowledged. Model answer in the key.", footer=FT)

out = d.save("slides/day3_mergers_remedies_litigation.pptx")
print("saved", out, "slides:", len(d.prs.slides._sldIdLst))
