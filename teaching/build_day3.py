"""Day 3 — Mergers, remedies, IP, and litigation, closing with the
hospital-merger capstone. Maps to book chapters 6 (mergers),
8 (regulation/remedies), 11 (innovation/IP), 12 (litigation), 14 (capstone).
SA-forward, concept-first. Capstone numbers verified:
pre-HHI 2,202 / post 3,402 / dHHI 1,200; GUPPI_A 10.3%, GUPPI_B 19.6%.

Kept in sync with slides/day3.qmd (same slides, same order). The .qmd is
authoritative; this builder mirrors it for the python-pptx output."""

from deck_builder import Deck, BLUE, GREEN, ORANGE, RED, PURPLE, GREY, DARK

FT = "Day 3 · Mergers, remedies, IP & litigation"
d = Deck("Day 3 — Mergers, Remedies & Litigation",
         "Predicting effects, fixing harm, IP, and proving it in a tribunal")

# ============================================================ MODULE 3.1
d.section("Module 3.1 — Merger analysis and simulation",
          "Mergers are prospective: we predict effects that have not happened "
          "yet.")

d.bullets("Mergers are prospective — the job is prediction", [
    "Conduct cases look backwards at what a firm did; merger review looks "
    "forward at what a combined firm will do — the evidence is largely "
    "predictive, not historical.",
    "Three economic theories of harm, plus — in SA — a fourth, non-competition "
    "question (public interest) that can override them.",
    "The agency carries an initial burden (a prima facie case); the parties "
    "then rebut with efficiencies, entry, or failing-firm arguments.",
    "Outputs are not just block / clear: the realistic menu is clear, "
    "condition (remedy), or prohibit.",
    "Screen cheap, quantify dear: GUPPI and diversion screens come first; full "
    "simulation only where the screen flags concern.",
], footer=FT)

d.bullets("The three theories of merger harm", [
    ("Unilateral effects.", 0),
    ("The merged firm raises price on its own because sales lost to a price "
     "rise are recaptured by the partner (diversion). No coordination needed.", 1),
    ("Coordinated effects.", 0),
    ("The merger makes tacit collusion among the remaining firms easier — "
     "fewer players, more symmetry/transparency, or removal of a maverick.", 1),
    ("Vertical / conglomerate effects.", 0),
    ("Input foreclosure, customer foreclosure, or leverage/bundling across "
     "products.", 1),
    "Plus the SA fourth question that can override all three: the "
    "public-interest test (§12A(3)) — employment, SMEs, spread of ownership.",
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
           "price rise ≈ pass-through × UPP (≈ UPP/2).",
           "The economics: a lost sale that returns to the family is no longer "
           "a cost of raising price — the merged firm internalises it."],
          footer=FT)

d.formula("Diversion ratios — where the lost sales go",
          "Diversion is the direction and strength of competition between two "
          "products — the most load-bearing number in unilateral-effects work.",
          ["D₁₂ = (sales gained by 2) / (sales lost by 1 when P₁ rises)"],
          ["Sources: switching/win-loss data, customer surveys (the "
           "'second-choice' question), a demand model, or — weakest — "
           "share-proportional diversion (D ≈ s_B / (1 − s_A)).",
           "Patient-flow / catchment / second-choice data usually beat "
           "share-proportional; supplied diversion above the proportional "
           "benchmark means the parties are CLOSER rivals than shares imply.",
           "Aggregate diversion (sum to all merging products) gauges total "
           "recapture and overall upward pricing pressure."],
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

d.bullets("Coordinated effects — the maverick and the conditions", [
    "Maverick-firm theory: harm often comes from the merger removing or "
    "absorbing a maverick — the disruptive price-cutter that destabilises "
    "tacit coordination.",
    ("Facilitating factors (the checklist): transparency of prices/terms, "
     "product homogeneity, symmetric firms and costs, stable demand, and high "
     "entry barriers.", 0),
    "A workable tacit scheme needs three things: reach a common understanding, "
    "detect deviation, and punish it credibly.",
    "Evidence: count the firms, measure symmetry, look for price-announcement "
    "or information-exchange practices, and ask whether the target IS the "
    "maverick.",
    "Coordinated-effects theories are harder to prove than unilateral ones — "
    "courts want a plausible mechanism, not just 'few firms'.",
], footer=FT)

d.bullets("The merger review process — burden and outcomes", [
    ("Notification: turnover/asset thresholds trigger mandatory filing (SA: "
     "large/intermediate mergers; US: HSR; EU: EUMR turnover tests).", 0),
    ("Second phase: a 'second request' (US) / Phase II (EU) / referral to the "
     "Tribunal (SA large mergers) — deeper analysis on the flagged theory.", 0),
    ("Burden: the agency makes a prima facie case (often via the structural "
     "presumption); the parties then rebut.", 0),
    ("Standard: US Clayton §7 'substantially lessen competition'; EU SIEC; SA "
     "§12A + the §12A(3) public-interest overlay.", 0),
    ("Outcome menu: clear unconditionally / clear with conditions (structural "
     "or behavioural) / prohibit.", 0),
], footer=FT)

d.bullets("Efficiencies and entry — the rebuttal", [
    "Efficiencies can offset price pressure, but must be merger-specific, "
    "verifiable, and passed through to consumers — burden on the parties.",
    "Marginal-cost savings discipline price; fixed-cost savings usually do "
    "not (they don't change the pricing incentive).",
    "Entry rebuts harm only if it is timely, likely, and sufficient to deter "
    "or counteract the price rise.",
    "The failing-firm defence is narrow: the firm must be failing, with no "
    "less-anticompetitive buyer and assets otherwise exiting.",
    "In SA, efficiencies and entry sit alongside — and can be outweighed "
    "by — the public-interest assessment.",
], footer=FT)

d.case_box("Staples / Office Depot — the econometric model", "US",
           "An econometric price regression carried the day",
           ["The FTC's challenge rested on a large-scale price regression: "
            "~400+ stores × ~18 months, regressing prices on the number of "
            "office-superstore competitors in each local market.",
            "Result: prices were materially higher where Staples faced no "
            "superstore rival — the model predicted roughly an ~8.49% price "
            "increase going from three superstore firms to one (monopoly).",
            "An event study on the merger announcement / FTC challenge dates "
            "corroborated the direction: stock moves were consistent with the "
            "market expecting the merger to raise prices.",
            "The court enjoined the merger — an early, influential win for "
            "an econometric model on unilateral effects."],
           "A transparent, replicable price regression on real transaction "
           "data can beat a market-definition argument — example-led merger "
           "economics at its strongest.",
           footer=FT)

d.case_box("Walmart / Massmart", "SA",
           "Cleared on competition grounds, fought on public interest",
           ["Walmart's acquisition of Massmart (2011, case 73/LM/Nov10) "
            "raised few horizontal competition concerns.",
            "The battle was public interest: effects on local suppliers and "
            "on jobs. Approved with conditions — a supplier-development fund, "
            "honouring existing labour agreements, and limits on "
            "merger-specific retrenchments (with some reinstatements).",
            "The conditions were litigated up to the CAC, which refined how "
            "public-interest conditions are framed and supervised over time."],
           "A merger can pass the competition test and still be reshaped — or "
           "saved — by public-interest conditions.",
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
d.section("Module 3.2 — Merger retrospectives and natural experiments",
          "Predicting effects is half the job; checking the predictions is "
          "how the system learns.")

d.bullets("Why look back at cleared mergers", [
    "Merger review is prediction; retrospectives check the predictions "
    "against what actually happened — the only feedback loop the system has.",
    "The point is institutional learning: were the price forecasts right, "
    "were efficiencies realised, did remedies work?",
    "Methods: difference-in-differences, event studies, synthetic controls, "
    "and re-estimated structural models on post-merger data.",
    "The credible designs lean on a clean control — an unaffected product, "
    "region, or comparable transaction that did not experience the merger.",
    "Retrospectives are also a litigation asset: an expert who pre-commits a "
    "retrospective design looks far more credible than one who reverse-"
    "engineers a result.",
], footer=FT)

d.bullets("What the retrospective literature finds", [
    "Efficiency claims are often overstated and frequently not passed through "
    "to consumers — the rebuttal that wins approval often does not "
    "materialise.",
    "Behavioural remedies often underperform structural ones — conduct rules "
    "get gamed, monitoring lapses, and the fix expires.",
    "Some cleared mergers raised prices — evidence that enforcement was, in "
    "places, too lenient at the margin.",
    "The asymmetry: blocked mergers can't be studied counterfactually, so the "
    "literature is built mostly from cleared deals — a selection caveat.",
    "Practitioner upshot: discount unverified efficiency promises and favour "
    "structural relief where it is feasible.",
], footer=FT)

d.bullets("Natural experiments in competition policy", [
    "Deregulation episodes are policy's natural experiments: airline "
    "deregulation (1978), the AT&T breakup (1984), banking-branching "
    "liberalisation, and electricity restructuring.",
    "Antitrust-law changes also serve: the US corporate leniency program "
    "(1993) revision sharply changed cartel-detection incentives — a clean "
    "before/after.",
    "Each gives a sharp, often discontinuous change in the competitive "
    "environment that is plausibly exogenous to the firms studied.",
    "Design discipline: identify treated and control groups, check pre-"
    "trends, and worry about confounding shocks that coincide with the date.",
    "These episodes are the empirical backbone of much of what we know about "
    "how concentration maps to prices.",
], footer=FT)

d.case_box("Liebersohn (2017) — banking", "US",
           "A regulatory HHI threshold as a natural experiment",
           ["Setting: US merger rules require divestiture where a merger pushes "
            "a market's HHI up by ≥ 200 to above 1,800 — a sharp, rule-based "
            "threshold.",
            "Design: difference-in-differences comparing markets just inside "
            "vs. just outside a 500-point band around the 1,800 cutoff — "
            "similar in everything but whether the rule bound.",
            "Result: where the rule forced more competition, banks did more "
            "lending to larger, safer borrowers — concentration had been "
            "constraining credit supply.",
            "Clean-design check: no bunching of mergers just below the cutoff "
            "— firms were not gaming the threshold."],
           "A regulatory threshold is a gift to the empiricist — it "
           "manufactures the discontinuity a credible causal design needs.",
           footer=FT)

d.case_box("Whirlpool / Maytag — appliances", "US",
           "A scanner-data post-merger retrospective",
           ["Post-merger evaluation using scanner (point-of-sale) data across "
            "appliance categories after the Whirlpool–Maytag combination.",
            "Design: use freezers as a control category (little affected by the "
            "merger) against the treated categories to net out common shocks.",
            "Finding: prices for dishwashers and dryers rose post-merger, while "
            "the control category did not move the same way — consistent with "
            "exercised market power.",
            "A model retrospective: real transaction data, a defensible "
            "control, and a transparent before/after anyone can replicate."],
           "Ex-post evidence like this is exactly what should discipline the "
           "next appliance-merger prediction.",
           footer=FT)

# ============================================================ MODULE 3.3
d.section("Module 3.3 — Remedies and regulation",
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

d.bullets("Remedy design principles", [
    "A remedy must be effective (it actually cures the identified harm) AND "
    "administrable (the Tribunal can monitor and enforce it).",
    "Match the remedy to the theory of harm: structural for horizontal "
    "overlap; access/firewall conduct rules for vertical foreclosure.",
    "Prefer remedies with clear, measurable compliance triggers over open-"
    "ended 'behave well' obligations.",
    "Build in monitoring: reporting duties, a compliance trustee/monitor, and "
    "a sunset or review date.",
    "Recall the retrospective lesson — behavioural remedies underperform — so "
    "use them where structure is impractical, and supervise hard.",
], footer=FT)

d.formula("Access pricing: ECPR and the revenue requirement",
          "When the remedy is access to a bottleneck (telecoms, rail, ports), "
          "you must set a price:",
          ["ECPR access price = direct cost + opportunity cost",
           "Revenue requirement = opex + depreciation + (return × rate base)"],
          ["ECPR (efficient component pricing rule) lets an efficient entrant "
           "in while compensating the incumbent — the benchmark in margin-"
           "squeeze remedies.",
           "Rate regulation builds allowed revenue from costs plus a fair "
           "return on capital; the contested number is the allowed return.",
           "Rate base = the regulated asset value on which the return is "
           "earned; gold-plating it is the classic incumbent strategy.",
           "Benchmarking / yardstick: compare the regulated firm to "
           "comparable firms or regions to discipline its cost claims."],
          footer=FT)

d.bullets("Benchmarking and yardstick regulation", [
    "Yardstick regulation ties a firm's allowed prices/costs to the "
    "performance of comparators, breaking the regulator's information "
    "dependence on the firm.",
    "Works best with many comparable units (regional utilities, water boards, "
    "port terminals) facing similar conditions.",
    "Methods range from simple peer ratio benchmarks to frontier techniques "
    "(DEA, stochastic frontier analysis) that estimate an efficient cost "
    "frontier.",
    "The trap: comparators must be genuinely comparable — adjust for scale, "
    "density, and input prices or the firm will (rightly) attack the "
    "benchmark.",
    "In SA, sector regulators (energy, ports/rail, telecoms) increasingly lean "
    "on benchmarking to test cost claims.",
], footer=FT)

d.case_box("Evanston Northwestern", "US",
           "The canonical BEHAVIOURAL hospital-merger remedy",
           ["A consummated hospital merger found to have raised prices.",
            "Rather than unwind it (structural), the FTC imposed a "
            "behavioural remedy: separate, independent negotiating teams for "
            "the two hospitals when bargaining with insurers.",
            "An effective conduct fix where divestiture of an integrated "
            "hospital was impractical — at the cost of ongoing supervision."],
           "When structural relief is impractical, a well-designed conduct "
           "remedy can restore the lost competition — if someone watches it.",
           footer=FT)

d.bullets("Tying it to SA — Tribunal-supervised conditions", [
    "Behavioural and public-interest conditions are the SA norm, not the "
    "exception — the Tribunal routinely supervises conditions over years.",
    "Typical machinery: reporting obligations, a compliance monitor/trustee, "
    "defined remedies for breach, and periodic review by the Tribunal.",
    "The CAC's refinements (Walmart/Massmart) shape how conditions are "
    "drafted so they are enforceable, not aspirational.",
    "The design lesson and the SA institutional reality coincide: a remedy is "
    "only as good as the body that can supervise it.",
], footer=FT)

# ============================================================ MODULE 3.4
d.section("Module 3.4 — Innovation, IP, and antitrust",
          "Where the right to exclude (a patent) meets the duty not to "
          "exclude (competition law).")

d.formula("SEPs and FRAND: hold-up vs hold-out",
          "Once a standard is set, an SEP holder can hold up implementers; "
          "FRAND commitments are the check.",
          ["Cumulative royalty = Σ (royalty rate_i)"],
          ["Hold-up: threaten an injunction post-adoption to extract supra-"
           "FRAND rates. Hold-out: implementers delay/underpay, free-riding "
           "on the standard.",
           "FRAND (fair, reasonable, non-discriminatory) is the licensing "
           "promise made to the standard body — the legal hinge of SEP "
           "disputes.",
           "Huawei v. ZTE (EU 2015): a negotiation framework — the SEP holder "
           "must offer FRAND terms before seeking an injunction; the "
           "implementer must respond in good faith.",
           "Unwired Planet (UK 2017): courts will set a global FRAND rate, "
           "not just a national one — a major jurisdictional escalation."],
          footer=FT)

d.formula("Royalty stacking — the arithmetic",
          "The problem: many SEP holders each charging a 'reasonable' rate "
          "that stacks to an unviable total.",
          ["Cumulative royalty = Σ (royalty rate_i)"],
          ["Worked figure: 10 holders × 5% each = 50% of the device price in "
           "royalties — manufacturing becomes unprofitable on any normal "
           "margin.",
           "Each individual demand can look defensible; the aggregate is what "
           "kills the product. FRAND and the ND limb exist to contain the "
           "stack.",
           "Remedy logic: aggregate royalty caps, top-down rate-setting from a "
           "total reasonable royalty, and patent-pool licensing."],
          footer=FT)

d.bullets("Pay-for-delay — FTC v. Actavis", [
    ("Reverse-payment ('pay-for-delay') settlements.", 0),
    ("A brand pays a generic to stay out of the market — the brand keeps the "
     "monopoly, both split the rents.", 1),
    ("FTC v. Actavis (US 2013).", 0),
    ("No 'scope of the patent' shield — even within the patent's nominal "
     "scope, a reverse payment is judged under the rule of reason.", 1),
    "The key signal: a large, unexplained reverse payment is itself evidence "
    "of anticompetitive intent — its size proxies the value of the avoided "
    "competition.",
    "Damages logic: harm ≈ (P_brand − P_generic) × volume × delay — the "
    "consumer overcharge from postponed generic entry.",
], footer=FT)

d.bullets("Killer acquisitions", [
    "Killer acquisition: an incumbent buys a nascent rival to shut its "
    "pipeline, not for synergies — pre-emptive elimination of future "
    "competition.",
    "Cunningham, Ederer & Ma (2021) estimate roughly 5–7% of pharma deals are "
    "killer acquisitions — small in count, large in lost innovation.",
    "The test: compare project discontinuation rates, acquired vs. "
    "independent — acquired overlapping projects are dropped more often.",
    "The enforcement gap: many such deals fall below notification thresholds "
    "(the target has little revenue) — hence share-of-supply and call-in "
    "powers.",
    "Live in digital and pharma policy debates (the 'string of nascent-rival "
    "acquisitions' theory in platform cases).",
], footer=FT)

d.bullets("Appellate caution — Qualcomm, both sides", [
    "FTC v. Qualcomm: the district court found liability, but the 9th Circuit "
    "REVERSED (2021) — no duty to deal, and the licensing practices were not "
    "shown to harm competition under §2. Cite the reversal, not the headline.",
    "EU: the Commission's €997m exclusivity-payment fine on Qualcomm was "
    "ANNULLED by the General Court (2022) on procedural and substantive "
    "grounds.",
    "Lesson: the most-cited 'abuse' stories were undone on appeal in both "
    "jurisdictions — carry the outcome, not the press release.",
    "This is the IP-and-dominance counterpart to the recurring habit: cite "
    "outcomes, not headlines (Sasol, Media24, Intel, Qualcomm).",
], footer=FT)

d.case_box("ARV / antiretroviral access", "SA",
           "IP, access to medicines, and competition law together",
           ["SA competition complaints over antiretroviral pricing pushed "
            "originators toward voluntary licences expanding generic supply.",
            "Method mix: medicine price data, the patent landscape, and "
            "SAHPRA registration timelines to estimate the harm from delayed "
            "generic entry.",
            "Sits at the intersection of §8 abuse, IP rights, and a pressing "
            "public-health interest — excessive-pricing and refusal-to-licence "
            "theories under SA dominance law."],
           "In SA the IP-vs-competition question has been about access to "
           "life-saving medicines, not abstract royalty rates.",
           footer=FT)

# ============================================================ MODULE 3.5
d.section("Module 3.5 — Research integrity and credibility",
          "How much should you believe any number — including your own?")

d.bullets("The research-credibility crisis", [
    "A wave of evidence shows much published empirical work does not "
    "replicate — directly threatening expert testimony built on it.",
    ("Four interacting culprits:", 0),
    ("Publication bias (only significant results get out), specification "
     "searching (p-hacking), low statistical power, and outright replication "
     "failures.", 1),
    "For an expert this is not academic hygiene — it is cross-examination "
    "risk: opposing counsel will probe every degree of freedom you took.",
    "The defence is transparency: pre-commit the design, disclose the "
    "specification space, and make the work reproducible end to end.",
    "This module is the methodological conscience of the course — it governs "
    "how much to believe any number.",
], footer=FT)

d.formula("The Ioannidis PPV model",
          "Why most published 'findings' in a hot, low-powered field can be "
          "false — the positive predictive value of a significant result:",
          ["PPV = (1 − β) R / [ (1 − β) R + α ]"],
          ["PPV = probability a 'significant' finding is true. β = "
           "false-negative rate (so 1 − β = power); R = prior odds the "
           "hypothesis is true; α = significance level.",
           "Good practice — high power, plausible prior — and an ideal field "
           "can hit ~89% true positives.",
           "A hot field — many teams testing long-shots, low power — and PPV "
           "can collapse toward ~20%: most 'discoveries' are false.",
           "Reading: one significant result from a low-powered study in a hot "
           "literature is weak evidence, statistics notwithstanding."],
          footer=FT)

d.bullets("Publication bias and the file drawer", [
    "The file-drawer problem: null results sit unpublished in drawers; "
    "significant results get out — so the published literature over-"
    "represents positives.",
    "Consequence: published effect sizes are inflated, because only the "
    "larger, 'significant' estimates clear the journal filter.",
    "Diagnostic: the funnel plot — effect size vs. precision; symmetry "
    "suggests no bias, a missing corner (small null studies) signals it.",
    "Tools: trim-and-fill, p-curve, and (best) pre-registration so the result "
    "exists regardless of significance.",
    "For experts: a literature that looks unanimous may be an artefact of the "
    "filter — weight it accordingly.",
], footer=FT)

d.formula("Multiple testing — the garden of forking paths",
          "Run enough tests and a 'significant' result is guaranteed by "
          "chance. With n independent tests at level α:",
          ["P(≥1 false positive) = 1 − (1 − α)ⁿ"],
          ["At α = 0.05: 10 tests → ~40% chance of at least one false "
           "positive; 20 tests → ~64%.",
           "The garden of forking paths: even without formal multiple testing, "
           "flexible choices (controls, subsamples, transformations) "
           "implicitly search the space.",
           "Corrections: Bonferroni (divide α by n — conservative), Holm, or "
           "FDR control for many tests.",
           "The real fix: a pre-analysis plan that fixes hypotheses and "
           "specifications before seeing outcomes. 'How many specifications "
           "did you run?' is a deadly cross-exam question."],
          footer=FT)

d.bullets("The replication crisis in economics", [
    "Replication efforts in economics find roughly half of studies fail to "
    "reproduce the original result — comparable to the psychology numbers.",
    "Causes mirror the rest of the module: small samples, researcher degrees "
    "of freedom, weak data, and selective reporting.",
    "Distinguish reproducibility (same data + code → same numbers) from "
    "replicability (new data → same finding) — experts owe at least the "
    "first.",
    "Journals' response: mandatory data-and-code archives and replication "
    "packages — increasingly expected of expert reports too.",
    "Advocacy lesson: build your analysis so a hostile third party can re-run "
    "it and get your numbers — the strongest credibility signal there is.",
], footer=FT)

d.bullets("The FTC's nine characteristics of useful analysis", [
    "A practical checklist for credible econometric work: (1) addresses a "
    "relevant issue; (2) consistent with economic theory; (3) reflects "
    "institutional facts; (4) uses appropriate data; (5) uses suitable "
    "techniques;",
    "(6) realistic about its limits; (7) tests robustness; (8) is replicable; "
    "(9) communicates clearly to a non-technical decision-maker.",
    ("The most common deficiencies in practice:", 0),
    ("Institutional disconnect (the model ignores how the industry actually "
     "works), data-quality problems, and poor communication.", 1),
    "Use it as a self-audit before filing — and as a cross-examination map of "
    "the OTHER side's report.",
    "It rhymes with the rest of the module: relevance, robustness, and "
    "replicability are the recurring themes.",
], footer=FT)

d.bullets("Pre-analysis plans and open science", [
    "Pre-analysis plans (PAPs): register hypotheses, specifications, and the "
    "analysis path before seeing the data — the antidote to forking paths and "
    "p-hacking.",
    "Open data and code: post the cleaning and analysis scripts (GitHub) and "
    "the data (Dataverse) so the result is independently checkable.",
    "Registration: clinical-trial-style registries (AEA RCT Registry, OSF) "
    "timestamp the design and deter selective reporting.",
    "A reproducible lockfile (renv / pinned packages) means the analysis runs "
    "identically years later — when the matter is finally heard.",
    "These practices are migrating from journals into agency and tribunal "
    "expectations of expert work.",
], footer=FT)

d.bullets("Reproducibility IS advocacy", [
    "A clean /data /scripts /reports bundle with a lockfile is not just good "
    "science — it is your cross-examination defence.",
    "If the whole pipeline runs from raw data to final exhibit with one "
    "command, you answer 'did you cherry-pick?' with a demonstration, not a "
    "denial.",
    "Run the sensitivity analysis BEFORE opposing counsel does — disclose the "
    "specifications that don't change the answer, and explain the ones that "
    "do.",
    "A reproducible report lets you update fast when new data arrives mid-"
    "matter — re-run, don't rebuild.",
    "The single highest-leverage habit in expert work: make your conclusion "
    "mechanically reproducible from the inputs.",
], footer=FT)

# ============================================================ MODULE 3.6
d.section("Module 3.6 — Litigation practice and expert evidence",
          "Where the evidence triad meets cross-examination.")

d.bullets("Getting expert evidence admitted — Daubert", [
    ("US — the Daubert gate.", 0),
    ("The judge is a gatekeeper; four (non-exclusive) factors: testability/"
     "falsifiability, known/potential error rate, peer review/publication, and "
     "general acceptance in the field.", 1),
    "Build the report to satisfy each: state the method's error properties, "
    "cite the peer-reviewed basis, and use accepted techniques.",
    "Kumho Tire extended Daubert beyond 'scientific' to all expert testimony, "
    "including economics.",
    "The gate excludes ipse dixit — 'trust me, I'm an expert' — so every step "
    "from data to conclusion must be defensible on its own.",
    "Contrast with the more flexible weight-not-admissibility approach of the "
    "SA Tribunal and UK/Australian courts.",
], footer=FT)

d.bullets("Class certification — Dukes and Comcast", [
    ("Wal-Mart v. Dukes (2011).", 0),
    ("Commonality requires a common QUESTION whose answer drives the "
     "resolution of the class's claims — not just a shared characteristic.", 1),
    ("Comcast v. Behrend (2013).", 0),
    ("The damages model must match the theory of liability and be capable of "
     "measurement on a class-wide basis.", 1),
    "For experts: a common-impact regression must show the violation affected "
    "the class in common, and the damages methodology must be common — not a "
    "patchwork of individual inquiries.",
    "A mismatch between liability theory and damages model is now a "
    "certification-killer — align them from the start.",
], footer=FT)

d.bullets("SA & concurrent expert evidence ('hot-tubbing')", [
    "Concurrent expert evidence ('hot-tubbing', from Australia, used in the "
    "UK and SA): opposing experts are sworn together and questioned side by "
    "side.",
    "Before the hearing they file a joint statement itemising points of "
    "agreement and disagreement — narrowing the real dispute for the "
    "tribunal.",
    "The SA Tribunal's flexible procedure favours this over a rigid Daubert-"
    "style admissibility gate: weight, not exclusion, and direct expert-to-"
    "expert testing.",
    "Advantage: the tribunal hears the genuine disagreement in real time, not "
    "filtered through advocates — and experts are disciplined by a peer in the "
    "box.",
    "Prepare differently: you must be able to defend every choice live, "
    "against a knowledgeable opponent, on the record.",
], footer=FT)

d.bullets("Three damages models — and how to defend them", [
    "Before/after: compare the violation period to a clean benchmark window "
    "for the same market — validate that the break is the violation, not a "
    "shock.",
    "Yardstick: compare the affected market to an unaffected comparator "
    "market — defend the comparability of the yardstick.",
    "Difference-in-differences: changes over time, treated vs. untreated — "
    "the workhorse, with clustered SEs (or randomisation inference for few "
    "clusters).",
    "Each needs an explicit counterfactual ('but-for' world); the fight is "
    "always over which benchmark is clean.",
    "Pair the point estimate with its confidence interval — the tribunal is "
    "buying the uncertainty, not just the number.",
], footer=FT)

d.bullets("The expert report — structure walkthrough", [
    "Real reports follow a stable spine (cf. Farber in Moussouris v. "
    "Microsoft; Card in the Harvard admissions case):",
    ("Qualifications → Assignment → Executive summary → Institutional "
     "background & data → Methodology & variable selection → Analyses → "
     "Damages → Rebuttal.", 0),
    "Variable selection is where reports live or die: avoid 'tainted' "
    "controls — variables that are themselves products of the challenged "
    "conduct (don't control away your own effect).",
    "The executive summary must be readable by a generalist judge; the "
    "methodology must be replicable by a hostile economist — write to both.",
    "The rebuttal section pre-empts the other side: address the obvious "
    "robustness attacks before they are made.",
], footer=FT)

d.formula("Significance and treble damages — the checkable close",
          "The two numbers an expert is asked for on the stand:",
          ["t = coefficient / standard error",
           "US exposure = 3 × (overcharge rate × commerce)"],
          ["t = 2.5 / 0.5 = 5.0 → beyond the 1% critical value (~2.58) → "
           "common impact is statistically significant.",
           "Commerce $200m at a 15% overcharge → $30m single → $90m trebled "
           "(US, automatic treble for Sherman Act violations).",
           "In SA, follow-on civil damages recover actual loss (≈ single) "
           "WITHOUT the US multiplier — same overcharge, very different "
           "exposure by forum.",
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
           "Share-proportional diversion A→B = 20/70 = 0.286 < supplied 0.32 → "
           "A and B are CLOSER substitutes than shares imply."],
          footer=FT)

d.code_demo("Capstone — verify the HHI in R",
            "Book helper calc_hhi_change(). Merging firms passed by NAME.",
            ["source(\"program/R/helpers.R\")",
             "hosp <- data.frame(",
             "  firm  = c(\"A\",\"B\",\"C\",\"D\",\"E\",\"F\"),",
             "  share = c(.30,.20,.25,.15,.06,.04))",
             "calc_hhi_change(hosp, merging_firms = c(\"A\",\"B\"))",
             "#> pre_hhi 2202 ; post_hhi 3402 ; delta_hhi 1200"],
            "The helper reproduces the hand arithmetic exactly — pre 2,202, "
            "post 3,402, Δ 1,200. Always tie the code back to the checkable "
            "number.",
            footer=FT)

d.exercise("Capstone deliverable — the memo", [
    "Write a 2–3 page recommendation memo on the A/B hospital merger.",
    ("Required computations: HHI / ΔHHI, both GUPPIs (show the arithmetic).", 1),
    ("Required reasoning: define the market, classify the unilateral-effects "
     "concern, and address one efficiency or entry rebuttal.", 1),
    ("Required framing: choose ONE jurisdiction (US / EU / SA), state its "
     "legal test, and recommend clear / condition / prohibit — for SA, address "
     "§12A(3) public interest explicitly.", 1),
], deliverable="A tribunal-ready memo: numbers correct, tied to the legal "
   "standard, uncertainty acknowledged. Model answer in the key.", footer=FT)

# ============================================================ CLOSE
d.takeaways("Course close — the habits to keep", [
    "Institutions first: know the forum's test before you pick a method.",
    "The evidence triad: never rest a conclusion on one leg — empirics, "
    "documents, and judgment together.",
    "Screen cheap, quantify dear: GUPPI before simulation, a variance screen "
    "before a full damages model.",
    "Cite outcomes, not headlines: carry the SA and EU appellate history "
    "(Sasol, Media24, Intel, Qualcomm).",
    "Reproducibility is advocacy — a one-command pipeline from raw data to "
    "exhibit is your best cross-examination defence.",
    "In South Africa, public interest can be the whole case — and a remedy is "
    "only as good as the body that can supervise it.",
], footer=FT)

out = d.save("slides/day3_mergers_remedies_litigation.pptx")
print("saved", out, "slides:", len(d.prs.slides._sldIdLst))
