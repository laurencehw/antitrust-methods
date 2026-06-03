# Style Guide: Voice and the AI-Tic Sweep

This guide records the prose voice the book is being edited toward and the
specific patterns to remove. It exists so the remaining edits (body boxes,
"Looking ahead" sections) can be done consistently by anyone.

## The target voice

Anchored on the author's published empirical work, which is direct, declarative,
and evidence-first. The model sentence states a claim and a magnitude and stops:
"a completed foreclosure causes between 0.5 and 0.7 additional filings within
0.1 miles." Carry that into the book:

- **Lead with the claim, then support it.** Not "It is important to note that
  market definition shapes everything that follows" — just "Market definition
  fixes the market shares, the theory of harm, and the remedy."
- **Concrete over abstract.** Name the document, the dataset, the number. Prefer
  "the internal pricing memo" to "documentary context."
- **Hedge with ranges and conditions, not adverbs.** "between 0.5 and 0.7," "when
  the panel is rich," not "arguably," "quite possibly," "it could be argued."
- **Short declarative sentences carry the load.** Use a long sentence when the
  logic needs it, not for rhythm.
- **Plain verbs.** "shows," "fixes," "rests on," "buys" — not "leverages,"
  "underpins," "powers," "unlocks."
- **One voice for the author.** Editorial "we" for the book's argument; "I" only
  for genuinely personal statements (acknowledgments). Decide once, keep it.

## Patterns to remove (the sweep)

Run these and edit every hit that is prose (skip tables, code, captions):

```bash
# 1. Throat-clearing and clichéd openers
grep -rinE "before (diving|we dive)|in a vacuum|it is (important|worth) (to )?not(e|ing)|at its core|in essence|ultimately,|the bottom line" chapters/

# 2. Self-congratulation about the book
grep -rinE "for its own sake|not an exercise in|that most distinguishes|defining feature|powerful|seamless|robust framework" chapters/

# 3. The "not just X, but Y" / "not A but B" flourish
grep -rinE "not just .* but|not merely|not only .* but also|is not a .* but" chapters/

# 4. Inflated adjectives
grep -rinE "\b(crucial|essential|vital|pivotal|critical) " chapters/

# 5. Formulaic chapter bridges (vary, don't delete the signpost entirely)
grep -rinE "the (previous|preceding) chapter|with that (foundation|in place)|we now turn to" chapters/

# 6. Breathless / promissory closings
grep -rinE "science fiction|that is as it should be|served its purpose|stay current|standing still|smoking gun" chapters/

# 7. Rule-of-three triads (read for three parallel items joined for rhythm)
#    No clean regex — read each "Looking ahead" and box closer by eye.
```

## Editing rules of thumb

- **Em-dashes:** keep for genuine interruptions; do not use three sets in a
  paragraph. Many here can become commas or periods.
- **A bridge once is fine; a bridge every chapter is a tell.** Vary how each
  chapter connects back — a question, a contrast, a concrete scenario — rather
  than "The previous chapter examined X. This chapter turns to Y."
- **Cut the meta-narration.** "This is the workflow the book has been building
  toward" tells the reader what to feel. Show the workflow; drop the line.
- **Triads:** when you find three parallel clauses, ask whether all three earn
  their place. Usually one is filler. Keep two, or replace with one specific
  example.

## Already done (reference for the rest)

`index.qmd`, `00-preface`, `14-closing` (full prose), and the openers of
`01`, `02`, `03`, `04`, `05`, `07`, `08`, `10`. Use these as the model when
editing the remaining chapters.
