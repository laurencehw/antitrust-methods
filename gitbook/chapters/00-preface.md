# Preface and How to Use This Book {.unnumbered}

Antitrust work sits between two worlds that rarely talk to each other: the academic literature on industrial organization and the day-to-day reality of building a case. This book tries to connect them. It is for the graduate student headed into competition policy, the economist moving into antitrust consulting, and the practitioner who wants a current reference on empirical methods and how courts and agencies actually use them.

## Who this book is for

The core readers are upper-level undergraduates and early graduate students in economics, law, and public policy who want to see how antitrust analysis works once it leaves the seminar room. The book also serves practitioners---economists at consulting firms, agency staff, and the lawyers who work with them---who need a desk reference for modern methods and their application.

We assume intermediate microeconomics and basic econometrics: regression, hypothesis testing, panel data. Where the material runs ahead of that, we give the intuition and point to fuller treatments. The aim is not to make you a specialist in any one method but to give you the vocabulary and the judgment to work across the range of questions that come up in a matter.

## The evidence triad

The book is organized around a simple claim: good antitrust analysis rests on three kinds of evidence at once, and weakness in any one shows. We call this the *evidence triad*.

**Empirical analysis** supplies the quantitative side---estimation, inference, and the discipline of stating assumptions and uncertainty plainly. Code boxes throughout show how to implement each technique in R, and every figure can be reproduced locally.

**Documentary evidence** supplies context. Case boxes show how agencies, courts, and parties have used---and misused---a given method, drawing on discovery documents, public filings, and reported decisions.

**Expert judgment** ties the analysis to legal and economic standards. Method boxes flag the common mistakes, mark where judgment has to do the work, and note where the field still disagrees.

A point estimate of overcharge persuades when it lines up with the internal pricing memos; a merger simulation gains weight when customers describe the same switching costs it assumes. The triad is not a theory. It is a description of how the cases that win are actually built.

## How to navigate this book

The chapters build on each other, but each also stands alone as a reference.

**For classroom use:** Work straight through. Start with the orientation to antitrust institutions ([Chapter 1](chapters/01-orientation.md)) and research design ([Chapter 2](chapters/02-research-design.md)), then the analytical core---market definition ([Chapter 3](chapters/03-market-definition.md)), the IO toolkit ([Chapter 4](chapters/04-io-toolkit.md)), and the practice areas (cartels, mergers, monopolization). The later chapters on digital markets, labor, and innovation apply those methods to harder, newer terrain.

**For practitioners:** Use it as a reference. Each chapter opens with its goals and a roadmap, so the relevant section is easy to find. The empirical appendix ([Empirical Appendix](chapters/13-empirical-appendix.md)) collects reusable code templates and diagnostics.

**For self-study:** Skim the case boxes first to see the methods in use, then work the technical material. Every code chunk runs against the supplied data, so you can change assumptions and see what moves.

{% hint style="success" %}
**Using the code examples**

All R code here is meant to run. Data live in `data/raw/` and `data/derived/`, and API keys in `.Renviron`. Render the whole book with `quarto render`, or work a chapter at a time. Use `renv` to lock package versions---it keeps results stable for teaching, and it matters in litigation, where another expert has to reproduce what you did.
{% endhint %}

## Structure of each chapter

Most chapters share a layout:

- **Learning goals** state what you should be able to do afterward.
- **Core topics** map the ground covered.
- **Method boxes** work through a technique, its assumptions, and its limits.
- **Case boxes** show the method in a real matter.
- **Code chunks** implement it on data you can run.
- **Qualitative evidence sections** cover documentary sources and interview protocols.
- **Looking ahead** connects the chapter to what follows.

## Jurisdictional scope

Most antitrust texts are written from inside one legal system and treat the others as appendices. This one carries three throughout: the United States, the European Union, and South Africa. The reason is practical, not encyclopedic. These three regimes solve the same problems in different ways, and watching a method bend as it crosses borders teaches you something about the method itself.

The US system---two federal agencies (the DOJ Antitrust Division and the FTC), enforcement through the federal courts, and the deepest body of case law and econometric practice anywhere---is the doctrinal and technical anchor. The EU---a single Commission (DG COMP), administrative decision-making, and an effects-based approach worked out over two decades of merger and abuse-of-dominance cases---offers the clearest treatment of how to trade competitive harm against efficiencies, and the most developed framework for regulating digital markets. South Africa---the Competition Commission and Tribunal, the public-interest mandate written into the Competition Act of 1998---shows how competition policy can take on employment, ownership, and small-business participation alongside the usual consumer-welfare questions, which is why it has become a template for other emerging-economy regimes.

Where a method behaves differently across the three, we say so. Where a case from one jurisdiction illuminates a method that travels, we use it. Where the data environment differs---US microdata, EU case-team data rooms, South African market inquiries---we show how to adapt. A reader working in just one system will find the methods apply directly; a reader working across borders will need the comparison.

## Acknowledgments and how to contribute

This book came out of teaching at NYU Wagner and consulting across a range of competition matters. I am grateful to the students and colleagues who read earlier drafts and pushed back on them.

It is meant to stay current. If you find an error, have a case worth adding, or write a useful code extension, send it through the book's repository.

## Looking ahead

The next chapter sets the stage: the institutions, the legal standards, and the working landscape antitrust economists operate in. From there we move to research design, and then into the methods that make up the bulk of the book.
