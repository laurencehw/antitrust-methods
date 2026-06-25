# Day 1 — Foundations: Exercises & Answer Key

**Course:** Antitrust Methods for Practitioners (South Africa) ·
**Day 1:** Institutions, evidence, market definition, market power ·
**Book chapters:** 1–4

Each exercise is marked **[checkable]** (one right number) or **[discussion]**
(graded on reasoning). Worked answers follow each block. Computations need only
a calculator; the R one-liners are optional and use the book's helpers.

---

## A. Warm-up — concentration [checkable]

A market has four firms with shares **40, 30, 20, 10** (percent).

1. Compute the HHI.
2. The two smallest firms (20% and 10%) propose to merge. Compute the
   post-merger HHI and the change (ΔHHI).
3. Under the 2023 US Merger Guidelines (structural presumption at post-merger
   HHI > 1,800 **and** ΔHHI > 100), is the presumption triggered?

> **Answer.**
> 1. HHI = 40² + 30² + 20² + 10² = 1,600 + 900 + 400 + 100 = **3,000**.
> 2. Merged firm = 30%. Post-HHI = 40² + 30² + 30² = 1,600 + 900 + 900 =
>    **3,400**. ΔHHI = 3,400 − 3,000 = **400** (shortcut: 2 × 20 × 10 = 400).
> 3. **Yes** — 3,400 > 1,800 and 400 > 100, so the structural presumption
>    applies.
>
> *R check:* `calc_hhi_change(data.frame(firm=c("A","B","C","D"), share=c(.40,.30,.20,.10)), merging_firms = c("C","D"))`.

---

## B. Critical loss [checkable]

You are testing whether a candidate market is a relevant antitrust market. The
SSNIP is **t = 5%** and the gross margin is **m = 35%**. A demand study predicts
that a 5% price rise would actually lose **9%** of unit sales.

1. Compute the critical loss.
2. Is the candidate market a relevant market, or should you widen it?
3. One sentence: state the *critical-loss fallacy* and why it matters here.

> **Answer.**
> 1. CL = t / (t + m) = 5 / (5 + 35) = 5/40 = **12.5%**.
> 2. Actual loss (9%) < critical loss (12.5%) ⇒ the SSNIP is **profitable** ⇒
>    the candidate market **IS a relevant market** — do **not** widen it.
> 3. *Fallacy:* high margins give a *low* critical loss (which seems to favour
>    a narrow market), but high margins typically come with *low actual loss*
>    too. Quoting only the low critical loss to argue for a narrow market
>    ignores that the actual loss is also low — you must compare the two.

---

## C. Cross-jurisdiction mapping memo [discussion]

A firm with a **48% share** uses exclusive-dealing contracts that tie up most
distributors. For **South Africa, the US, and the EU**, state (a) the statutory
home of the theory of harm, and (b) the burden it puts on you as the economist.

> **Model answer.**
> - **South Africa.** Vertical restraint under **§5**, and abuse of dominance
>   under **§8(1)(d)** because at 48% the firm is **presumed dominant** (≥ 45%,
>   §7). You must show the exclusivity forecloses rivals / harms competition;
>   the firm may raise a technological-efficiency or pro-competitive gain
>   defence.
> - **United States.** **Sherman §1** (and possibly §2). **Rule of reason:**
>   you must show *substantial foreclosure* of the relevant market and net
>   anticompetitive effect — exclusive dealing is not per se unlawful.
> - **EU.** **Article 102** (a 48% share with entry barriers is likely
>   dominant; AKZO presumption bites at 50%). Apply the **as-efficient-
>   competitor** framing to any rebate/exclusivity; the firm may offer an
>   objective justification.
> - *Cross-cutting point:* the same contracts can pass US rule-of-reason and
>   still infringe EU/SA dominance rules — build a separate narrative per forum.

---

## D. South African public interest [discussion]

Give one concrete example where the §12A(3) public-interest test changes a
merger outcome that a pure consumer-welfare standard would clear. Name the
public-interest limb engaged.

> **Model answer.**
> A competitively benign acquisition (no SSNIP concern, low ΔHHI) in which a
> foreign buyer eliminates a high level of ownership by **historically
> disadvantaged persons** — engaging the **spread-of-ownership** limb — can be
> conditioned or prohibited under §12A(3) even though consumer-welfare analysis
> would clear it (cf. the Burger King / Grand Parade prohibition). Equally, a
> merger threatening large **employment** losses can attract conditions
> (Walmart/Massmart: supplier-development fund and retrenchment limits) that a
> consumer-welfare test would not require.

---

## E. Optional R lab — read a real concentration series

If you have R and a FRED key, reproduce the Chapter 1 bank-concentration figure
and describe the 2008 break.

```r
source("program/R/helpers.R")
conc <- readr::read_csv("data/raw/fred_bank_conc_5.csv") |>
  dplyr::mutate(date = as.Date(date))
ggplot2::ggplot(conc, ggplot2::aes(date, value)) +
  ggplot2::geom_line(colour = "#0072B2", linewidth = 1) +
  theme_antitrust()
```

> **What to observe.** Five-bank asset concentration steps up around the 2008
> crisis (failures and crisis-era acquisitions). Discussion point: a rising
> *concentration ratio* is a flag, not a finding — it does not by itself define
> a market or prove power.
