# Style Guide: Voice and the AI-Tic Sweep

This guide records the prose voice the book is being edited toward and the
specific patterns to remove. It exists so the remaining edits (body boxes,
"Looking ahead" sections) can be done consistently by anyone.

## The target voice

Anchored on the author's published empirical work (the foreclosure-contagion and
rural-apartheid papers), which is direct, declarative, and evidence-first. The
model paragraph sets up a problem in short sentences and then states what the
author does and finds, with magnitudes: *"Apartheid South Africa provides a good
setting in which to examine these issues. It was non-democratic. Its economy
remained dependent on agriculture for a long time."* And: *"I use subnational
variation in South Africa to test this mechanism. … I find that reductions in the
supply of foreign mine labor … increased mechanization on the mines and on farms
competing with mines for labor."*

Carry that into the book:

- **First person singular for analytical moves.** The author writes "I use," "I
  find," "I then show," not "we now turn to." For a co-written textbook the
  editorial "we" (author + reader) is acceptable, but keep it for genuinely shared
  steps and prefer plain statements and "you" for the reader. Reserve flourish-free
  "I" for authorial choices.
- **Lead with the claim, then support it.** Not "It is important to note that
  market definition shapes everything that follows" — just "Market definition fixes
  the market shares, the theory of harm, and the remedy."
- **Very short declaratives carry setup.** Three or four words is fine. "It was
  non-democratic." Let them sit next to longer explanatory sentences.
- **Concrete over abstract.** Name the document, the dataset, the date, the number.
  "between 1974 and 1976," "40% of all employment as late as 1958."
- **Hedge with ranges and conditions, not adverbs.** "between 0.5 and 0.7,"
  "suggestive evidence," "may have contributed" — not "arguably," "quite possibly."
- **Plain verbs.** "shows," "fixes," "rests on," "buys" — not "leverages,"
  "underpins," "powers," "unlocks."


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
