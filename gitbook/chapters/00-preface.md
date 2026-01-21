# Preface and How to Use This Book {.unnumbered}

This book bridges the gap between academic research and the practical realities of antitrust work. Whether you are a graduate student preparing for a career in competition policy, an economist moving into antitrust consulting, or a practitioner seeking to strengthen your methodological toolkit, this text aims to provide the conceptual foundations, empirical techniques, and practical judgment you need to contribute effectively to antitrust analysis.

## Who this book is for

The primary audience includes upper-level undergraduates and early graduate students in economics, law, and public policy who want to understand how antitrust analysis actually works in practice. The book also serves practitioners---economists at consulting firms, agency staff, and lawyers working with economic experts---who need a reference for modern empirical methods and their application to competition cases.

We assume familiarity with intermediate microeconomics and basic econometrics (regression, hypothesis testing, panel data). Where more advanced techniques appear, we provide intuition and references to deeper treatments. The goal is not to make you a specialist in any single method, but to give you the vocabulary and judgment to work effectively across the range of issues that arise in antitrust matters.

## The evidence triad

A central organizing principle of this book is what we call the *evidence triad*: the integration of empirical analysis, documentary evidence, and expert judgment. Modern antitrust work rarely succeeds on any single dimension alone.

**Empirical analysis** provides quantitative rigor through estimation and statistical inference. Throughout this book, code boxes demonstrate how to implement key techniques using R, with all figures designed to be reproduced locally. We emphasize transparency in assumptions, diagnostics for identification, and clear communication of uncertainty.

**Documentary evidence** grounds quantitative findings in real-world context. Case boxes throughout each chapter illustrate how agencies, courts, and parties have used (or misused) particular methods. We draw on discovery documents, public filings, and reported decisions to show how evidence fits together in actual matters.

**Expert judgment** ties analysis to legal and economic standards. Method boxes flag common pitfalls, highlight where professional judgment is required, and note areas of ongoing debate in the field. We discuss survey design, qualitative interviews, and the translation of technical findings for legal audiences.

## How to navigate this book

The chapters are designed to build on each other, but each can also stand alone as a reference for a particular topic. Here are several ways to approach the material:

**For classroom use:** Work through chapters sequentially, starting with the orientation to antitrust institutions (Chapter 1) and research design (Chapter 2). The core analytical chapters on market definition (Chapter 3), industrial organization tools (Chapter 4), and specific practice areas (cartels, mergers, monopolization) follow logically. End with the specialized chapters on digital markets, labor, and innovation that apply these methods to emerging areas.

**For practitioners:** Use the book as a reference. Each chapter opens with learning goals and core topics, making it easy to locate relevant material. The empirical appendix (Chapter 13) provides reusable code templates and diagnostic tools that can be adapted to specific matters.

**For self-study:** Begin by skimming the case boxes to see how methods are applied in practice, then work through the technical material. Every code chunk is designed to run with the accompanying data files, so you can experiment with the techniques yourself.

{% hint style="success" %}
**Using the code examples**

All R code in this book is designed to be fully reproducible. Data files are stored in `data/raw/` and `data/derived/`, with API keys managed through `.Renviron`. Render the entire book with `quarto render`, or work through individual chapters interactively. We recommend using `renv` to lock package versions, ensuring consistency for teaching and for litigation work where reproducibility is essential.
{% endhint %}

## Structure of each chapter

Most chapters follow a consistent structure:

- **Learning goals** articulate what you should understand after completing the chapter.
- **Core topics** provide a roadmap of the material covered.
- **Method boxes** explain key empirical techniques, including their assumptions and limitations.
- **Case boxes** illustrate how methods have been applied in real antitrust matters.
- **Code chunks** demonstrate implementation with reproducible examples.
- **Qualitative evidence sections** discuss documentary sources and interview protocols.
- **Looking ahead sections** preview how the current chapter connects to subsequent material.

This structure reflects our conviction that good antitrust work requires moving fluidly between theory, empirics, and institutional context.

## Jurisdictional scope

The primary focus is United States antitrust law and practice, including the Department of Justice Antitrust Division, the Federal Trade Commission, and federal courts. However, antitrust is increasingly a global discipline. Throughout the book, we note where European Union, United Kingdom, and other jurisdictions diverge in their standards, burdens of proof, or analytical approaches.

When a claim depends on jurisdictional context, we flag it explicitly. Readers outside the US should find the methods broadly applicable while remaining attentive to local legal frameworks.

## Acknowledgments and how to contribute

This book grew out of teaching materials developed at NYU Wagner and consulting experience across a range of competition matters. We are grateful to the students and colleagues who provided feedback on earlier drafts.

The book is designed as a living document. If you find errors, have suggestions for additional case examples, or develop useful code extensions, please contribute through the book's repository. Our goal is to keep the methods current as the field evolves.

## Looking ahead

The next chapter provides an orientation to antitrust institutions, legal standards, and the professional landscape. We then turn to research design principles before diving into the substantive methods that form the core of antitrust economic analysis. Welcome to the practice of antitrust methods.
