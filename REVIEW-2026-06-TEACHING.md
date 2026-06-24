# Review for Teaching Use: *Antitrust Methods: Research and Practice*

Reviewed 24 June 2026, in the course of building a 9-hour practitioner short
course (three 3-hour days) for South African competition-law masters students.
This is a **third** review with a deliberately different lens from the two on
file. `REVIEW.md` scored prose, structure, and pedagogy (8.5 after the voice
pass). `REVIEW-2026-06-AUDIT.md` scored *reliability* — formulas, case
outcomes, citations, build (6, with a long error catalog and a status addendum
recording fixes applied on this branch). Neither asked the question this one
does: **can you teach directly from this book, and what does a South African
classroom need that the manuscript does not yet give it?**

I did not re-run the full fact audit. Where I spot-checked audit items against
the current text, I note the result below — including one the prior audit got
wrong.

## Headline

The book is **very close to a turnkey teaching text** and is, to my knowledge,
the only methods book that carries US / EU / South Africa as co-equal
jurisdictions with runnable code. For a South African practitioner audience it
is better positioned than anything else in print. The gaps that remain for
classroom use are not about content depth — that is there — but about three
things: (1) **executable reproducibility** (the single biggest open item from
the audit is still open), (2) **a few teaching scaffolds** the book gestures at
but does not supply, and (3) **SA-specific framing** that is present but
unevenly foregrounded relative to the US/EU material.

---

## What makes it strong to teach from

- **The evidence triad is a genuine spine.** Empirical / documentary / expert
  judgment is how matters are actually built, and it gives every session the
  same three-part close. Students remember a frame they meet six times.
- **Every chapter ends with a "Data exercise (checkable)" with a worked answer.**
  This is the single most useful teaching feature in the book. The audit
  recomputed all eleven and found them arithmetically correct; I rebuilt the
  course exercises directly on top of them. They are short, self-contained, and
  markable — exactly what a practitioner cohort needs.
- **The box system (Method / Case / Qualitative / Debate) is slide-ready.** Each
  box is roughly one slide of content. The course decks are in large part a
  re-sequencing of these boxes.
- **The reusable R helpers** (`calc_hhi_change`, `run_logit_sim`,
  `plot_waterfall`, `plot_tornado`, `theme_antitrust`) make live "code as demo"
  segments cheap: one function call per concept, consistent styling.
- **Currency has largely landed.** Spot-checking the chapters the audit flagged
  as stale, the 2024–2026 record is now present: *US v. Google* search liability
  (2024) and remedies (Sept 2025), Google ad-tech liability (2025), DMA
  non-compliance fines (Apple €500M / Meta €200M, Apr 2025), *Jindal* and
  *DaVita* acquittals, and the *Ryan v. FTC* noncompete-rule endgame. A 2026
  cohort will not catch the chapters reading like 2023.

---

## What a classroom still needs (teaching-readiness gaps)

These are ordered by how much they hurt in a live session.

### 1. A fresh clone cannot render — so a student cannot reproduce a figure
This is audit item §H-55, and the status addendum confirms it is **still open**:
no `_freeze/` cache is committed, `data/` ships only a README, and R/Quarto were
unavailable in the editing sandbox, so the corrected chunks have never been
executed. For a *reading* it is survivable. For a *course* it is the gating
item: the book's whole pitch is "every figure regenerates from code," and the
first thing a curious student does is clone and render — and it fails. **Highest
priority for teaching use.** Render once locally with keys set, eyeball the
figures the audit touched (waterfalls, Q-learning, event studies, Lorenz curve,
margin squeeze), and commit `_freeze/` plus the processed `data/derived`
aggregates the chapters read.

### 2. The capstone is the best exercise in the book but only half-executable
The hospital-merger capstone (Ch. 14) supplies a clean dataset and has fully
worked answers for Steps 2–4 (HHI/ΔHHI, diversion, GUPPI). Steps 5–7
(Nash-in-Nash bargaining, retrospective DiD, the recommendation memo) reference
data that is never supplied and have no checkable answer, so a student hits a
wall mid-workflow and cannot tell whether they are missing something. For the
course I supplied a small insurer/bargaining table and a jurisdiction-explicit
memo rubric so the capstone runs end to end; the book should fold the same in.

### 3. "Code as demo" needs a no-data fallback path the slides can rely on
Several teachable chunks read files that the repo does not ship (and that a
classroom will not have keys for). The guards added in the build pass mean these
degrade to a printed message rather than erroring — good — but a printed "data
not available" is not a teachable figure. Either commit the small synthetic
fallback CSVs the guards expect, or ship the `_freeze/` so the cached figure
displays. The course decks therefore show the *code and the expected output*
rather than depending on a live render; the book could do the same in a margin.

### 4. SA framing is present but not consistently foregrounded
The South African material is the book's differentiator, but in several chapters
it arrives last (after the US and EU treatment) and in a shorter register. For
an SA cohort the natural order is reversed: start from the Competition Act and
the Tribunal/CAC, then use the US/EU material as comparison. The course decks do
this; the book need not, but a one-paragraph "South African anchor" at the head
of each conduct chapter would serve SA readers better than the current
US-first-SA-last default.

### 5. A few SA specifics still want a local legal read-through
Audit item C (SA case outcomes and numbers) was substantially fixed on this
branch, but the addendum keeps a **human SA practitioner read-through open** —
specifically the Grocery Retail and Healthcare Market Inquiry specifics, SA
docket numbers, and the softened inquiry summaries. For a course taught *to* SA
practitioners this is non-optional: the audience will know the case numbers. I
have flagged the specific items the decks rely on (Sasol CAC set-aside 2015,
Media24 CAC reversal 2019, Walmart/Massmart `/LM/` docket, dominance thresholds
in §7) so they can be confirmed before teaching.

---

## Fresh observations (not in the prior reviews)

- **The glossary's labor-supply-elasticity entry is fine — do not "fix" it.**
  A reading flagged "elasticities below 2–3 indicate meaningful monopsony power"
  as backwards. It is not. It is consistent with the book's own Ch. 10 worked
  example (firm-level elasticity η = 2 ⇒ markdown = η/(1+η) = 2/3, i.e. wage 33%
  below marginal revenue product) and with a defensible reading of the empirical
  literature on *residual firm-level* labor supply. The entry already says "at
  the firm level." Leave it. (Noting it here because it is the kind of plausible
  "correction" that would introduce an error.)
- **HHI threshold discipline held.** Spot-checks of the 2023 thresholds
  (1,800 / Δ100) in market definition, mergers, and the Ch. 1 exercise are
  internally consistent; the audit's book-wide 1,500/2,500-vs-1,800
  contradiction (§F) appears resolved in the chapters I checked.
- **The "Enhanced Visualizations" back-halves (Chs. 9–11) still read as
  exported notebooks** in places ("Key insights:", "How to use this analysis:").
  The audit flagged this (§J-69); it is cosmetic but it is the one place the
  voice pass did not fully reach, and it is visible if you project those slides.
  I did not lift content from those sections into the decks for that reason.
- **Pedagogically, the book under-uses its own best device.** The checkable
  exercises are excellent but sit at the *end* of each chapter. In class the
  arithmetic should come *during* the concept, not after it. The decks
  interleave a one-line computation into each method slide; the book could seed
  a "compute this now" margin note at each formula.

---

## Recommendations, in priority order

1. **Render locally and commit `_freeze/` + the `data/derived` aggregates.**
   This is the one change that turns "a book about reproducible analysis" into
   "a reproducible book," and it unblocks every live demo. (Audit §H — still
   open.)
2. **Complete the capstone** (supply the bargaining table and a
   jurisdiction-explicit memo rubric; the course version can be lifted back in).
3. **SA legal read-through** of the inquiry specifics and docket numbers, by an
   SA practitioner, before the book is taught to SA practitioners. (Audit
   addendum item 3 — still open.)
4. **Add a one-paragraph "South African anchor"** at the head of each conduct
   chapter for SA readers; keep the comparative US/EU material where it is.
5. **Seed the checkable arithmetic into the body** at each formula, not only at
   chapter end.
6. **Finish the cosmetic voice sweep** of the Chs. 9–11 "Enhanced
   Visualizations" sections. (Audit §J — still open.)

Items 1–3 are what stand between this manuscript and a course a colleague could
pick up and teach from a clean clone. Everything else is polish on an already
strong, genuinely distinctive book.

---

## Companion deliverable

This review accompanies a full set of course materials in `teaching/`:

- `teaching/slides/` — three PowerPoint decks (`day1`–`day3`), SA-forward,
  concept-first with "code as demo" segments.
- `teaching/exercises/` — exercise sets and worked answer keys for each day,
  plus an end-of-course capstone (the completed hospital-merger workflow).
- `teaching/README.md` — the course map: how the three days map onto the book's
  chapters, timings, and which R helpers each live demo uses.

The materials are built so the decks stand alone (no render required to
present), while every live-demo segment points back to a specific chapter and
helper function in the book for instructors who want to run the code.
