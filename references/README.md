# Bibliography Guide for Antitrust Methods Book

## Overview

This directory contains the comprehensive bibliography for "Antitrust Methods: Research and Practice." The bibliography has been significantly expanded to provide robust academic and legal support for all chapters.

## File Structure

- **`references.bib`**: Main BibTeX bibliography file with 150+ entries
- **`csl-placeholder.txt`**: Placeholder for citation style files (if needed)

## Bibliography Organization

The bibliography is organized by topic for easy navigation and maintenance:

### 1. Foundational Texts and Treatises
- Classic antitrust texts (Areeda & Hovenkamp, Motta, Tirole)
- Policy frameworks (Baker, Salop)

### 2. Research Methods and Econometrics
- Causal inference (Angrist & Pischke, Cunningham)
- Difference-in-differences methods (Callaway & Sant'Anna)
- Synthetic control methods (Abadie et al.)

### 3. Market Definition
- Critical loss analysis (Katz & Shapiro)
- UPP and alternatives to market definition (Farrell & Shapiro)

### 4. Cartels and Collusion
- Cartel detection methods (Harrington, Abrantes-Metz)
- Bid rigging (Porter & Zona, Conley & Decarolis)
- OECD guidance documents

### 5. Merger Analysis
- Retrospective studies (Ashenfelter & Hosken, Miller & Weinberg)
- Merger simulation (Nevo, Berry-Levinsohn-Pakes)
- UPP/GUPPI (Farrell & Shapiro, Jaffe & Weyl)

### 6. Monopolization and Exclusion
- Theoretical foundations (Whinston, Salop & Scheffman)
- Predatory pricing (Areeda & Turner)
- Vertical foreclosure (Ordover et al.)

### 7. Digital Markets and Platforms
- Two-sided market theory (Rochet & Tirole, Armstrong)
- Platform competition (Evans & Schmalensee, Hagiu & Wright)
- Empirical evidence on self-preferencing (Luca et al., Edelman & Lai)

### 8. Labor Markets and Monopsony
- Labor market concentration (Azar et al., Benmelech et al.)
- Monopsony theory (Manning, Ashenfelter et al.)
- No-poach agreements (Krueger & Ashenfelter)

### 9. Innovation and Intellectual Property
- Patent holdup and SEPs (Shapiro, Lemley & Shapiro)
- Pay-for-delay (Edlin & Hemphill, Hemphill & Sampat)
- Generic entry (Scott Morton)

### 10. Litigation and Expert Testimony
- Expert testimony standards (Rubinfeld, Baker & Rubinfeld)
- Federal Judicial Center Reference Manual

### 11. Case Law
- **US Cases**: Microsoft, Brooke Group, Actavis, Qualcomm, Google, Epic v. Apple
- **EU Cases**: United Brands, AKZO, Intel, Deutsche Telekom, Google Shopping/Android
- **UK Cases**: Unwired Planet, Optis v. Apple

### 12. Agency Guidelines
- **US**: DOJ/FTC Merger Guidelines (2010, 2023), HR Guidance, Noncompete Rule
- **EU**: Horizontal Merger Guidelines, Market Definition Notice, Article 102 Guidance, DMA
- **UK**: CMA Merger Assessment Guidelines
- **South Africa**: Competition Act, OIPMI Report, key enforcement decisions

### 13. Data Sources
- BLS QCEW, Census LEHD (labor markets)
- PatentsView, FDA Orange Book (innovation)
- FRED (economic data)

## How to Use Citations

### Basic Citation Syntax

In your Quarto/RMarkdown text, use:

```markdown
Single citation: [@author_year]
Multiple citations: [@author1_year; @author2_year]
In-text citation: @author_year argues that...
```

### Examples from the Book

**Monopolization chapter:**
```markdown
The foundational economic framework was established by @areeda_turner_1975.
For economic analysis of exclusive dealing, see @whinston_2006 and 
@ordover_saloner_salop_1990 on vertical foreclosure.
```

**Digital markets chapter:**
```markdown
For two-sided market theory, see @rochet_tirole_2003 and @armstrong_2006.
```

**Labor markets chapter:**
```markdown
For empirical evidence on labor market concentration, see 
@azar_marinescu_steinbaum_2020 and @benmelech_bergman_kim_2020.
```

## Adding New References

When adding new references to `references.bib`:

1. **Follow the existing format** for consistency
2. **Use descriptive citation keys**: `author_year` or `agency_document_year`
3. **Add keywords** to help organize and search
4. **Include full citation information**: volume, pages, DOI/URL where available

### Template for Academic Article

```bibtex
@article{author_year,
  author = {Last, First and Last, First},
  title = {Article Title},
  journal = {Journal Name},
  year = {2024},
  volume = {10},
  number = {2},
  pages = {100--150},
  keywords = {topic1, topic2}
}
```

### Template for Case Law

```bibtex
@misc{jurisdiction_case_year,
  title = {Case Name},
  author = {{Court Name}},
  year = {2024},
  note = {Citation (e.g., 123 F.3d 456)},
  keywords = {jurisdiction, topic}
}
```

### Template for Agency Guidelines

```bibtex
@misc{agency_document_year,
  title = {Document Title},
  author = {{Agency Name}},
  year = {2024},
  note = {Document number or reference},
  url = {https://...},
  keywords = {jurisdiction, topic}
}
```

## Citation Coverage by Chapter

### Current Status

✅ **Well-cited chapters:**
- Chapter 5: Cartels (Harrington, Porter & Zona, OECD)
- Chapter 6: Mergers (Ashenfelter & Hosken, Nevo, Farrell & Shapiro)
- Chapter 7: Monopolization (Whinston, Areeda & Turner, case law)
- Chapter 9: Digital Markets (Rochet & Tirole, Armstrong, case law)
- Chapter 10: Labor Markets (Azar et al., Manning, Krueger & Ashenfelter)
- Chapter 11: Innovation (Shapiro, Lemley & Shapiro, Actavis)
- Chapter 12: Litigation (Rubinfeld, FJC Reference Manual)
- Chapter 13: Empirical Appendix (Angrist & Pischke, Cunningham, Callaway & Sant'Anna)

### Chapters Needing More Citations

The following chapters could benefit from additional citations as you develop them:

- **Chapter 1: Orientation** - Add foundational policy texts
- **Chapter 2: Research Design** - Already has good methods citations
- **Chapter 3: Market Definition** - Add Katz & Shapiro, Davis & Garcés
- **Chapter 4: IO Toolkit** - Add Tirole, Motta
- **Chapter 8: Regulation & Remedies** - Add regulatory economics literature

## Bibliography Compilation

The bibliography is automatically compiled by Quarto when you build the book. The configuration in `_quarto.yml` specifies:

```yaml
bibliography: references/references.bib
```

### Generating a Standalone Bibliography

To generate a standalone bibliography document:

```bash
quarto render references/references.bib --to html
```

Or create a simple Quarto document:

```markdown
---
title: "Bibliography"
bibliography: references.bib
nocite: '@*'
---

# Complete Bibliography
```

## Citation Style

The default citation style is Chicago author-date. To change the citation style:

1. Download a CSL file from https://github.com/citation-style-language/styles
2. Save it to the `references/` directory
3. Add to `_quarto.yml`:

```yaml
csl: references/your-style.csl
```

Common styles for legal/academic work:
- `chicago-author-date.csl` (current default)
- `bluebook-law-review.csl` (legal citations)
- `apa.csl` (social sciences)

## Maintenance

### Regular Tasks

1. **Check for duplicate entries** - Search for duplicate citation keys
2. **Validate BibTeX syntax** - Use a BibTeX validator
3. **Update URLs** - Check that agency guideline URLs are current
4. **Add new cases** - Update with recent enforcement actions

### Quality Checks

Before publishing, run these checks:

```bash
# Check for undefined citations in chapters
grep -r "@[a-z_]*" chapters/*.qmd | grep -v "^#"

# Check for duplicate BibTeX keys
grep "^@" references/references.bib | sort | uniq -d
```

## Resources

### Finding Citations

- **Academic papers**: Google Scholar, SSRN, NBER
- **Case law**: Justia, CourtListener, EUR-Lex, SAFLII
- **Agency documents**: Official agency websites (DOJ, FTC, EC, CMA, CCSA)
- **OECD reports**: https://www.oecd.org/competition/

### BibTeX Tools

- **JabRef**: Cross-platform BibTeX editor
- **Zotero**: Reference manager with BibTeX export
- **Google Scholar**: "Cite" button provides BibTeX
- **doi2bib**: Convert DOI to BibTeX (https://www.doi2bib.org/)

## Contact

For questions about the bibliography or to suggest additions, please contact the book author or submit an issue to the project repository.

---

*Last updated: November 2024*
