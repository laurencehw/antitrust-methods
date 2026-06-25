# Day 3 — Mergers, Remedies, IP & Litigation: Exercises & Answer Key

**Course:** Antitrust Methods for Practitioners (South Africa) ·
**Day 3:** Merger simulation, remedies, IP, expert evidence, capstone ·
**Book chapters:** 6, 8, 11, 12, 14

---

## A. Unilateral effects — GUPPI [checkable]

Products A and B belong to merging firms. Diversion from A to B is
**D_AB = 0.30**. B's price is **P_B = 100** with a **40%** margin; A's price is
**P_A = 120**.

1. Compute GUPPI_A.
2. Does it clear the ~5% screen?

> **Answer.**
> 1. GUPPI_A = D_AB × M_B × (P_B / P_A) = 0.30 × 0.40 × (100/120)
>    = 0.30 × 0.40 × 0.8333 = **0.10 = 10%**.
> 2. **Yes** — 10% is well above the ~5% screen, so unilateral effects warrant
>    closer analysis (e.g. a full merger simulation).

---

## B. Royalty stacking [checkable]

A handset maker must license SEPs from **8 holders**, each demanding a **2%**
royalty on the device price. The target product margin is **15%**.

1. Compute the cumulative royalty.
2. Is the product viable on the 15% margin? What is the policy point?

> **Answer.**
> 1. Cumulative royalty = 8 × 2% = **16%**.
> 2. **No** — a 16% royalty stack exceeds the 15% margin, so the device is
>    unprofitable to make. This is the **royalty-stacking** problem FRAND
>    commitments exist to contain: each holder's "reasonable" rate is fine
>    alone, but they stack to an unviable total.

---

## C. Pay-for-delay damages [checkable]

A brand drug sells at **$100**; the generic would sell at **$20**. Annual volume
is **1,000,000** units. A reverse-payment settlement delays generic entry by
**2 years**.

1. Estimate the consumer harm from delay.
2. Which legal test governs the settlement, and what is the key signal of
   anticompetitive intent?

> **Answer.**
> 1. Harm ≈ (P_brand − P_generic) × volume × delay = ($100 − $20) × 1,000,000 ×
>    2 = **$160 million**.
> 2. ***FTC v. Actavis* (US 2013): rule of reason** (no "scope of the patent"
>    shield). The key signal is a **large, unexplained reverse payment** from
>    brand to generic — its size proxies for the value of the avoided
>    competition.

---

## D. Expert evidence — significance and damages [checkable]

A common-impact regression returns a coefficient of **2.5** percentage points
with a standard error of **0.5**. Affected commerce is **$200 million** at a
**15%** overcharge.

1. Compute the t-statistic and test at the 1% level.
2. Compute single and trebled damages.

> **Answer.**
> 1. t = 2.5 / 0.5 = **5.0**. The two-sided 1% critical value ≈ 2.58, so t = 5.0
>    is **significant at the 1% level** — supports common impact across the
>    class.
> 2. Single = 0.15 × $200m = **$30 million**; trebled = 3 × $30m =
>    **$90 million** (US). In SA, recovery would be actual damages (≈ $30m),
>    no multiplier.

---

## E. Remedy design [discussion]

A consummated hospital merger is found to have raised prices, but divestiture of
the integrated hospital is impractical.

1. Propose a remedy and justify structural vs. behavioural.
2. State the main risk of your choice and how an SA tribunal would manage it.

> **Model answer.**
> 1. A **behavioural** remedy — e.g. **separate, independent negotiating teams**
>    for the two hospitals when contracting with insurers (cf. *Evanston
>    Northwestern*, the canonical behavioural hospital remedy). Structural
>    relief is impractical once an integrated hospital cannot be cleanly
>    unwound.
> 2. **Risk:** behavioural remedies require **ongoing supervision** and can be
>    gamed. An SA tribunal would attach **monitoring/reporting conditions** and
>    a compliance trustee, consistent with its practice of supervising
>    behavioural and public-interest conditions over time.

---

## F. Capstone — hospital merger, end to end

**Data.** Six hospitals, discharge volumes (= shares, total 100,000):
A 30,000 (30%), B 20,000 (20%), C 25,000 (25%), D 15,000 (15%), E 6,000 (6%),
F 4,000 (4%). Prices/margins: A $12,000 / 40%; B $11,000 / 35%.
Diversion: A→B = 0.32, A→C = 0.30, B→A = 0.45. **A and B propose to merge.**

**Tasks.**
1. Define the relevant market (narrative; use critical-loss reasoning).
2. Compute HHI, post-merger HHI, ΔHHI. [checkable]
3. Compare the supplied (patient-flow) diversion A→B with share-proportional
   diversion. [checkable]
4. Compute GUPPI_A and GUPPI_B. [checkable]
5. Explain (qualitatively) how the merger shifts bargaining leverage with
   insurers (Nash-in-Nash).
6. Pre-commit a retrospective DiD design to test the effect after the fact.
7. Write a 2–3 page recommendation memo under ONE jurisdiction's standard.

> **Worked answers (steps 2–4).**
>
> **2. Concentration.**
> - Pre-HHI = 30² + 20² + 25² + 15² + 6² + 4²
>   = 900 + 400 + 625 + 225 + 36 + 16 = **2,202**.
> - Merged A+B = 50%. Post-HHI = 50² + 25² + 15² + 6² + 4²
>   = 2,500 + 625 + 225 + 36 + 16 = **3,402**.
> - ΔHHI = 3,402 − 2,202 = **1,200** (shortcut: 2 × 30 × 20 = 1,200).
> - Post-HHI 3,402 > 1,800 and ΔHHI 1,200 > 100 ⇒ **structural presumption**
>   (triggered under either the 2023 or the 2010 thresholds).
>
> **3. Diversion.**
> - Share-proportional diversion A→B (diversion in proportion to B's share of
>   the non-A market) = 20 / (100 − 30) = 20/70 = **0.286**.
> - Supplied patient-flow A→B = **0.32** > 0.286 ⇒ A and B are **closer
>   substitutes** than shares alone imply — strengthens the unilateral-effects
>   concern.
>
> **4. GUPPI.**
> - GUPPI_A = D_AB × M_B × (P_B/P_A) = 0.32 × 0.35 × (11,000/12,000)
>   = 0.32 × 0.35 × 0.9167 = **0.103 = 10.3%**.
> - GUPPI_B = D_BA × M_A × (P_A/P_B) = 0.45 × 0.40 × (12,000/11,000)
>   = 0.45 × 0.40 × 1.0909 = **0.196 = 19.6%**.
> - Both exceed the ~5% screen; B's pressure is larger because A is the bigger,
>   higher-margin recapture target.
>
> **5–7 (rubric).**
> - **Step 5:** the merger raises A's and B's *disagreement payoff* in insurer
>   negotiations (dropping either from a network is now less costly to the
>   merged system), shifting bargaining leverage toward higher negotiated
>   rates — the mechanism the GUPPIs proxy.
> - **Step 6:** a panel DiD with hospital and time fixed effects, treated =
>   merging hospitals, with **event-time leads/lags** to check pre-trends;
>   pre-commit the specification and the control group *before* seeing
>   post-merger prices.
> - **Step 7 (graded on tie-out, not a single answer):** state the test —
>   **US Clayton §7** (substantial lessening of competition; the presumption
>   shifts the burden to the parties), **EU SIEC**, or **SA §12/§12A** plus the
>   **§12A(3) public-interest** assessment. A defensible recommendation is
>   *prohibit or condition*: the structural presumption is triggered, both
>   GUPPIs are high, and diversion shows close substitution; efficiencies/entry
>   would have to be substantial, merger-specific, and verifiable to rebut.
>
> *R checks:* `calc_hhi_change(data.frame(firm=c("A","B","C","D","E","F"), share=c(.30,.20,.25,.15,.06,.04)), merging_firms=c("A","B"))`
> for step 2; `run_logit_sim()` to extend step 4 into a full simulation.

---

### Grading guide for the memo (step 7)

| Dimension | What earns full marks |
|---|---|
| Computation | HHI/ΔHHI and both GUPPIs correct, arithmetic shown |
| Market definition | Critical-loss reasoning, not just an assertion |
| Theory of harm | Unilateral effects named and tied to diversion/GUPPI |
| Rebuttal | One efficiency or entry argument engaged honestly |
| Legal framing | Correct test for the chosen forum; SA answers address §12A(3) |
| Uncertainty | States what would change the conclusion (a confidence interval, not a point) |
