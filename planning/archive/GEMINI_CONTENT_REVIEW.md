# Gemini Content Review Summary
**Date:** 2026-01-01
**Reviewer:** Gemini (via Claude Code integration)

## Overview
Comprehensive content review of GitBook chapters identifying gaps, errors, and improvement opportunities.

---

## Chapter 03: Market Definition

### Critical Issues
- **Outdated Guidelines Reference:** Learning goals cite 2010 DOJ/FTC Guidelines; should be 2023
- **Missing Multi-sided Markets Methodology:** No workflow for platform market definition (Amex decision)

### Content Gaps
- SSNDQ operationalization (conjoint analysis)
- Supply-side substitution jurisdictional differences (EU vs US)
- Brown Shoe "practical indicia" cross-reference
- Aggregate Diversion Ratio explanation

### Enhancement Suggestions
- Add Cellophane Fallacy warning for monopoly cases
- Clarify Elzinga-Hogarty test naming
- Explain cointegration vs correlation distinction

---

## Chapter 06: Mergers

### CRITICAL CODE ERRORS
1. **UPP Formula Wrong:** `diversion * price * (1 - margin)` should be `diversion * price * margin`
2. **Logit Calibration Missing Price:** `alpha = 1/(margin * (1-share))` missing `price` in denominator
3. **Outdated HHI Thresholds:** Using 2010 thresholds (1,500/2,500); 2023 Guidelines use 1,800

### Content Gaps
- vUPP/EDM formulas and code (promised but not delivered)
- Killer acquisitions / innovation effects
- Labor market effects in merger review

### Enhancement Suggestions
- Add sensitivity matrix for UPP
- Connect simulation output to waterfall chart
- Note two-sided UPP for digital platforms

---

## Chapter 07: Monopolization

### Critical Issues
- **Missing Trinko:** Essential US case limiting essential facilities doctrine
- **Missing Amex:** Critical for platform market definition
- **Code Logic Error:** Price-cost test doesn't model retroactive rebate suction effect

### Content Gaps
- "Monopoly broth" / interrelated acts doctrine
- Behavioral vs structural remedy comparison
- EU recoupment distinction (AEC is about foreclosure, not recoupment)

### Enhancement Suggestions
- Integrate method box into narrative
- Add MES visualization
- Expand remedy section

---

## Chapter 09: Digital Markets

### Critical Issues
- **Duplicate Section:** "Southern African digital enforcement snapshots" appears twice
- **Visualization Mismatch:** Sankey diagram described as "bar chart"
- **Internal Notes Visible:** "(Roadmap 9.1)" etc. still in text

### Content Gaps
- Generative AI / LLMs as platform layer (critical for 2026)
- Privacy-competition interface (Privacy Sandbox, Apple ATT)
- Algorithmic pricing intermediaries (RealPage)

### Enhancement Suggestions
- Update citations to post-2023 outcomes
- Add ecosystem market definition concept
- Define "OIPMI" at first use

---

## Chapter 10: Labor Markets

### Critical Issues
- **Temporal Error:** FTC noncompete rule described as "proposed" (should be past tense for 2026)
- **Missing Labor Exemption:** No discussion of Clayton Act § 6 / why unions aren't cartels
- **HHI Code Warning Needed:** Denominator assumes complete market coverage

### Content Gaps
- 2023 Merger Guidelines labor market provisions
- Gig economy employee vs contractor tension
- Information exchange safety zones (DOJ/FTC withdrawal)
- Synthetic control method (mentioned but not explained)

### Enhancement Suggestions
- Clarify no-poach (horizontal) vs non-compete (vertical)
- Use log(wage) in models (standard practice)
- Remove "Roadmap" internal notes

---

## Chapter 11: Innovation & IP

### Critical Issues
- **Pie Chart vs Waterfall:** R code generates pie chart but text describes waterfall
- **Missing FTC v. Qualcomm:** Key SEP/licensing case

### Content Gaps
- Killer acquisitions theory
- Innovation/future markets definition
- Non-practicing entities (NPEs)
- Copyright in APIs (Google v. Oracle)
- Product hopping

### Enhancement Suggestions
- Replace pie chart with waterfall code
- Add "standard wars" context
- Mention essentiality over-declaration statistics

---

## Common Issues Across Chapters

### Code Quality
1. Several formulas have errors or don't match narrative
2. Hardcoded values instead of dynamic calculations
3. Missing connection between code output and visualizations

### Internal Artifacts
- "(Roadmap X.X)" references still visible
- "Visualizations and data sourcing" sections read as author notes

### Citation Consistency
- Some chapters use 2010 guidelines, others 2023
- Pandoc citation keys occasionally visible (though mostly fixed)

### Missing Cross-Chapter Links
- Market definition (Ch 3) not linked from merger chapter
- Labor chapter doesn't link to merger labor effects
- Remedies scattered rather than consolidated

---

## Priority Fixes

### Immediate (Code Errors)
1. Fix UPP formula in Chapter 06
2. Fix Logit alpha calibration in Chapter 06
3. Fix price-cost test code in Chapter 07
4. Replace royalty pie chart with waterfall in Chapter 11

### High Priority (Content)
1. Update all HHI thresholds to 2023 Guidelines (1,800)
2. Add Trinko to Chapter 07 essential facilities
3. Add labor exemption to Chapter 10
4. Update FTC noncompete status for 2026

### Medium Priority (Gaps)
1. Add vUPP/EDM code to Chapter 06
2. Add Generative AI section to Chapter 09
3. Add killer acquisitions to Chapter 11
4. Add synthetic control example to Chapter 10

### Cleanup
1. Remove all "(Roadmap X.X)" references
2. Remove duplicate SA snapshots section in Ch 09
3. Expand hint boxes into proper content
