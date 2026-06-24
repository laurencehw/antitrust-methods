# Day 2 — Conduct: Exercises & Answer Key

**Course:** Antitrust Methods for Practitioners (South Africa) ·
**Day 2:** Cartels, abuse of dominance, labour markets, digital platforms ·
**Book chapters:** 5, 7, 10, 9

---

## A. Cartel overcharge and damages [checkable]

A cartel affected **R200 million** of commerce. The estimated overcharge rate is
**15%**.

1. Compute single damages.
2. Compute the US treble-damages exposure for the equivalent conduct.
3. Why might the recoverable South African figure differ from the US number?

> **Answer.**
> 1. Single damages = 0.15 × R200m = **R30 million**.
> 2. Treble = 3 × R30m = **R90 million** (US private actions).
> 3. **No multiplier in SA** — follow-on civil claims recover *actual* damages
>    (≈ R30m, plus interest), not treble. Also, the **passing-on defence is
>    available in SA/EU**, so a direct purchaser's recovery may be reduced to
>    the extent the overcharge was passed downstream (the US bars that defence
>    under *Hanover Shoe*, but limits standing to direct purchasers under
>    *Illinois Brick*).

---

## B. Labour monopsony [checkable]

A local labour market has three employers with hiring shares **50, 30, 20**
(percent). The firm-level labour-supply elasticity is **η = 2**.

1. Compute the labour HHI. Is the market concentrated under the 2023 threshold?
2. Compute the wage as a fraction of the marginal revenue product of labour
   (MRPL), and the implied markdown.

> **Answer.**
> 1. HHI = 50² + 30² + 20² = 2,500 + 900 + 400 = **3,800** — well above the
>    **1,800** threshold, so **highly concentrated**.
> 2. wage / MRPL = η/(1+η) = 2/3 = **0.667**, i.e. the wage is **33% below**
>    MRPL (a 33% markdown). Both numbers tell the same story: concentrated
>    buyer side, suppressed wages.

---

## C. Digital ranking harm [checkable]

A search platform demotes a rival from **position 1 (CTR 35%)** to **position 4
(CTR 8%)** on **1,000,000** queries.

1. Compute the lost clicks.
2. One sentence: what must you control for before attributing the loss to
   self-preferencing rather than quality?

> **Answer.**
> 1. Lost clicks = (0.35 − 0.08) × 1,000,000 = **270,000 clicks**.
> 2. Control for **quality/relevance** — regress rank (or visibility) on a
>    quality measure *and* an own-product dummy; the favouritism is the
>    coefficient on the dummy, holding quality fixed.

---

## D. Abuse strategy — margin squeeze [discussion]

A vertically integrated South African telecommunications firm, dominant in
wholesale access, is accused of a margin squeeze against downstream ISPs.

1. State the test.
2. Name the two prices you must obtain.
3. Give one objective justification the firm might raise.

> **Model answer.**
> 1. **Test (AEC applied to two levels):** an abuse exists if
>    `P_retail − P_wholesale < downstream incremental cost` — i.e. the firm's
>    own retail arm could not profitably operate at the wholesale (access)
>    price it charges rivals.
> 2. The **wholesale/access price** charged to downstream rivals and the firm's
>    own **retail price** (plus the downstream incremental cost of providing
>    the retail service).
> 3. Justifications might include: genuine cost differences (the rivals are
>    less efficient, not foreclosed), a meeting-competition response, or that
>    the spread reflects a legitimate efficiency. The benchmark access price is
>    often framed via the **ECPR** (Day 3).

---

## E. Case-law currency check [discussion]

For each, state the *current* status and the one-line teaching point.

1. Sasol (SA, excessive pricing).
2. Media24 (SA, predation).
3. Intel (EU, rebates / AEC).
4. *Jindal* and *DaVita* (US, labour).

> **Answer.**
> 1. **Sasol:** Tribunal's excessive-pricing finding **set aside by the CAC
>    (2015)** on the value benchmark. Teach as good law on the *test*, not as
>    standing liability.
> 2. **Media24:** Tribunal abuse finding (2015) **overturned by the CAC
>    (2019)**; refined the AAC-vs-ATC cost benchmark for predation.
> 3. **Intel:** the 2009 rebates decision and its AEC analysis were
>    **annulled** (GC 2022, affirmed CJEU Oct 2024) — do not cite "the AEC
>    framework established in *Intel*" as settled.
> 4. **Jindal:** jury **acquitted** on the Sherman Act counts (physical
>    therapists); **DaVita:** defendants **acquitted** (2022). Criminal labour
>    cases are hard to win, but reshaped compliance.

---

## F. Optional R lab — cartel before/after

```r
# synthetic illustration: cartel vs clean benchmark window
p_cartel    <- mean(price[period == "cartel"])
p_after     <- mean(price[period == "after"])
overcharge  <- (p_cartel - p_after) / p_after
damages     <- overcharge * commerce
# validate the benchmark window first:
# strucchange::breakpoints(price ~ 1) to date the structural break
```

> **Discussion.** The overcharge is only as good as the benchmark window. A
> Bai–Perron / `strucchange` break test should confirm the "after" window is
> genuinely post-cartel before you trust the gap.
