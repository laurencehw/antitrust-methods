# Editorial Review: *Antitrust Methods: Research and Practice*

Reviewed June 2026. This is a working review of the manuscript as a whole, with a
score, the case for it, and a concrete path to a 9.5. A companion file,
`STYLE.md`, records the voice the prose should be edited toward and the
machine-checkable tics to remove.

## Score: 7.5 / 10 (as reviewed) → ~8.5 after the voice pass already applied

A genuinely strong manuscript with a clear, defensible structure and an unusual
amount of runnable code. It is held back from the top of the range by three
things: a pervasive "AI voice" in the framing prose, some structural redundancy,
and a reliance on synthetic data in several chapters that undercuts the
reproducibility the book sells. None of these is hard to fix. The substance is
there.

## What the book gets right

- **The organizing idea earns its place.** The evidence triad (empirical /
  documentary / expert judgment) is not a gimmick; it is a fair description of how
  cases are actually built, and it gives every chapter the same spine.
- **Code-forward and reproducible by design.** Figures regenerate from R, data
  are cached, keys live in `.Renviron`. For a methods text this is the right call
  and it is followed through.
- **The three-jurisdiction frame is a real differentiator.** US / EU / South
  Africa, carried throughout rather than bolted on, is rare and valuable —
  especially the South African public-interest material, which most texts ignore.
- **Coverage is current.** 2023 Merger Guidelines, staggered DiD (Callaway–Sant'Anna,
  Sun–Abraham), labor monopsony, DMA, algorithmic pricing. The "what to read next"
  section is well chosen.
- **Method/Case/Qualitative/Debate boxes** are a good pedagogical device and are
  used consistently.

## What holds it back (and how to fix it)

### 1. AI voice in the framing prose — *partly fixed in this pass*
The front matter, every chapter opener, and the closing chapter were written in a
recognizable register: throat-clearing openers ("Before diving into…", "does not
happen in a vacuum"), self-congratulation ("the aspect that most distinguishes it
from competing texts"), rule-of-three flourishes, and breathless closings ("would
seem like science fiction… That is as it should be"). This is the single biggest
drag on perceived quality because it sits in the highest-visibility positions.

Already rewritten in this pass: `index.qmd`, `00-preface`, `01-orientation`
(opener), `02`, `03`, `04`, `05`, `07`, `08`, `10` (openers), and the entire
prose of `14-closing`. Remaining: the body Method/Case boxes and the
"Looking ahead" sections in most chapters. `STYLE.md` lists the exact patterns and
a grep sweep to finish the job.

### 2. Structural redundancy
Most chapters say the same thing three times in the first page: the intro
paragraph, then "Learning goals," then "Core topics" all restate "this chapter
synthesizes the tools from earlier chapters." Chapter 6 is the clearest case
(lines 3–19). Fix: let the intro motivate, let Learning goals be a tight bulleted
"you will be able to…", and cut the "Core topics" restatement or fold it into the
first real section.

### 3. Synthetic data undercuts the reproducibility claim
Per `CLAUDE.md`, cartel bid data, labor-market HHI, platform usage, and
patent/FDA data are still synthetic placeholders. The book promises figures that
"regenerate from code" against real data; where the data are fabricated, say so in
the figure caption (a one-line "Synthetic data for illustration" note) and
prioritize replacing them. A reader who discovers an unmarked synthetic figure
discounts the rest. This is the highest-value substantive item for credibility.

### 4. Jurisdictional scope was inconsistent — *fixed in this pass*
`index.qmd` described the book as "US focus with comparative notes for
EU/UK/Japan/China," while the preface and closing claimed a co-equal US/EU/SA
design, and `01-orientation` framed it as a course for South African
practitioners. These are now reconciled on the US/EU/SA framing with UK/Asia as
notes. Worth a final read-through to confirm nothing downstream still says
"course."

### 5. Exercises and worked examples are uneven
The best (the hospital-merger capstone in `14-closing`) are excellent. Many
chapter-end exercises are generic ("compile a table of the 5 most recent
challenges"). To reach 9.5, every chapter should end with at least one exercise
that runs against a specific supplied dataset and has a checkable answer.

## Path to 9.5 — priority order

1. **Finish the voice pass** through the body boxes and "Looking ahead" sections,
   using `STYLE.md`. — **DONE.** Front matter rewritten by hand; body swept across
   all 13 content chapters (integrity-verified: no citation, statute, case, number,
   or code touched).
2. **Mark or replace synthetic data.** — **Captioning DONE** (13 figures now carry
   "Synthetic data for illustration only"). **Replacement DEFERRED** by author's
   choice: the build environment has no outbound network or API keys, so real data
   cannot be pulled here. When run locally with `FRED_API_KEY`/`BLS_KEY`, the
   pipeline in `program/scripts/` supplies real series; the open item is wiring the
   cartel-bid and labor-HHI chunks to a real source (BLS QCEW open CSVs; an open
   procurement bid set) with the synthetic path as a clearly-labeled fallback.
3. **De-duplicate chapter front pages.** — **DONE** for the clear offenders (ch.6
   intro/goals/core-topics; ch.3 opener/goals/"why it matters"; ch.7 opener vs. a
   duplicate "Introduction").
4. **Verify every case citation and statutory cite.** A methods book that gets
   *Ryan v. FTC* or a Guidelines section number wrong loses credibility fast.
   — **OPEN** (needs a human legal reader).
5. **Strengthen end-of-chapter exercises** so each has at least one data-backed,
   checkable problem. — **DONE.** Chapters 1–12 each gained a "Data exercise
   (checkable)" with inline numbers and a collapsible worked answer (HHI/delta-HHI,
   DiD, critical loss, logit diversion, overcharge and treble damages, GUPPI, margin
   squeeze, revenue requirement, self-preferencing traffic loss, labor HHI +
   markdown, royalty stacking + pay-for-delay, t-stat + damages).
6. **Author voice consistency.** Decide on "we" vs. "I" once and apply it
   everywhere (the book currently uses editorial "we"; the preface now uses "I" for
   personal acknowledgments, which is the right split — just keep it deliberate).

Remaining for a clean 9.5: item 4 (a legal-cite read-through), the data-source
wiring half of item 2, and item 6. The stylistic and structural work is complete.
