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
   using `STYLE.md`. Mechanical and high-impact. (~1–2 days)
2. **Mark or replace synthetic data.** Caption every synthetic figure now; replace
   the cartel and labor-HHI placeholders with real procurement / QCEW data. (the
   big substantive lift)
3. **De-duplicate chapter front pages.** One motivating intro, one tight goals
   list, no restatement. (~half a day, mechanical)
4. **Verify every case citation and statutory cite.** A methods book that gets
   *Ryan v. FTC* or a Guidelines section number wrong loses credibility fast. Spot
   a legal reader to read for cite accuracy.
5. **Strengthen end-of-chapter exercises** so each has at least one data-backed,
   checkable problem.
6. **Author voice consistency.** Decide on "we" vs. "I" once and apply it
   everywhere (the book currently uses editorial "we"; the preface now uses "I" for
   personal acknowledgments, which is the right split — just keep it deliberate).

Do 1, 3, and 4 and the book is a clean 8.5–9. Add 2 and 5 and it is a 9.5.
