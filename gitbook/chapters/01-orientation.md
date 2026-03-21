# Orientation: Antitrust and Regulation {#sec-orientation}

Before diving into specific methods, we need to understand the institutional landscape where antitrust analysis occurs. This chapter provides that foundation. Economic analysis does not happen in a vacuum---it responds to legal standards, agency priorities, and procedural constraints that vary across jurisdictions. Understanding these institutions will help you frame your analyses to address the questions that actually matter in practice.

## Learning goals
This opening chapter orients you to the institutional settings where economists, researchers, and lawyers work side by side. By the end you should be able to articulate how competition authorities define their objectives, how they translate statutes or guidelines into investigative hypotheses, and how evidentiary burdens shift between agencies and courts. You will also learn how to map economic questions—market definition, market power, theory of harm, efficiencies, and remedy selection—onto the specific legal elements regulators must prove or rebut.

An equally important goal is judgment: when should you push for additional data work, and when is documentary, testimonial, or industry expertise the better marginal investment? Because this course serves practitioners in South Africa who often face multi-jurisdictional matters, we will continually compare US-led doctrines with approaches in the EU, UK, Asia, and regional African regulators. Expect a mix of narrative history, process walkthroughs, and applied examples from roughly 2005–2024.

## Core narrative
### Institutions and mandates

Modern antitrust work is anchored by a handful of institutions with overlapping mandates. In the United States, the Department of Justice (DOJ) Antitrust Division and the Federal Trade Commission (FTC) share merger and conduct jurisdiction, aided by state attorneys general and sector regulators such as the Federal Communications Commission or Surface Transportation Board.

Post-2000 history matters for understanding current doctrine. The Clinton-era Microsoft litigation cemented exclusionary conduct frameworks (*United States v. Microsoft*, 2001). The 2010 Horizontal Merger Guidelines (DOJ/FTC Horizontal Merger Guidelines, 2010) elevated unilateral effects analysis. Most recently, the 2023 Merger Guidelines (DOJ/FTC Merger Guidelines, 2023) re-centered structural presumptions and addressed platform dynamics head-on.

Across the Atlantic, the European Commission's Directorate-General for Competition (DG COMP) pairs investigations with inquisitorial decision making, while national authorities like the UK Competition and Markets Authority (CMA) play an increasingly global role—for example, blocking Microsoft/Activision until remedies evolved. Asian agencies—including Japan's JFTC, Korea's KFTC, and China's SAMR—have expanded resources to scrutinize digital markets and cross-border conduct.

For practitioners working in Southern Africa, the Competition Commission and Competition Tribunal are essential reference points. These bodies have expanded their focus to digital markets, food supply chains, and cartels affecting the Southern African Development Community (SADC). Understanding each body's statutory tests, procedural timelines, and evidentiary cultures is essential to crafting persuasive analyses.

{% hint style="success" %}
**Definition: Key Antitrust Concepts**

| Term | Definition |
|:-----|:-----------|
| **Market Power** | The ability to profitably raise prices above competitive levels or exclude competitors |
| **Relevant Market** | The product and geographic scope where competitive effects are assessed |
| **Theory of Harm** | The causal mechanism by which conduct is alleged to harm competition |
| **Efficiencies** | Cost savings or quality improvements that may offset anticompetitive effects |
| **Consumer Welfare** | The standard measuring harm to buyers (price, quality, choice, innovation) |
| **Public Interest** | Non-efficiency factors (employment, SMEs, ownership) considered in some jurisdictions |
{% endhint %}

### Comparative statute mapping

For multi-jurisdictional practitioners, the table below maps common conduct types to their statutory homes across the US, EU, and South Africa. Use this as a quick reference when translating theories of harm across legal frameworks.

| Conduct Type | United States | European Union | South Africa |
|:-------------|:--------------|:---------------|:-------------|
| **Cartels / Horizontal agreements** | Sherman Act §1 (15 U.S.C. §1) | TFEU Article 101 | Competition Act 89/1998, §4 |
| **Monopolization / Abuse of dominance** | Sherman Act §2 (15 U.S.C. §2) | TFEU Article 102 | Competition Act 89/1998, §8 |
| **Vertical restraints** | Sherman Act §1; Rule of reason | TFEU Art. 101 + VBER | Competition Act §4(1)(b), §5 |
| **Mergers (horizontal)** | Clayton Act §7 (15 U.S.C. §18) | EUMR (Reg. 139/2004) | Competition Act §12, §12A |
| **Mergers (vertical/conglomerate)** | Clayton Act §7 | EUMR Art. 2 | Competition Act §12A |
| **Price discrimination** | Robinson-Patman Act | Art. 102(c) (dominant firms) | §9 (price discrimination by dominant firm) |
| **Unfair trade practices** | FTC Act §5 (15 U.S.C. §45) | Unfair Commercial Practices Dir. | Consumer Protection Act 68/2008 |

**Key differences to note:**

- **Standards**: US uses "monopoly power" (typically >70% share); EU/SA use "dominance" (typically >40-50% share with barriers).
- **Effects vs. object**: EU Art. 101 distinguishes "object" restrictions (per se illegal) from "effects" analysis; US separates per se from rule of reason.
- **Public interest**: South Africa uniquely incorporates public interest factors (employment, SME participation, ownership) in merger review under §12A(3) (SA Competition Act, 1998).
- **Private enforcement**: US allows treble damages; EU/SA have more limited private action frameworks.

{% hint style="info" %}
**Practitioner tip**

When advising on multi-jurisdictional matters, map the same conduct to each regime's statutory test early. A practice that survives US rule-of-reason analysis may still violate EU "object" restrictions or trigger South African public-interest review. Build separate legal-economic narratives for each forum.
{% endhint %}

### Workflow from intake to remedies

Having mapped these institutions and their statutory frameworks, practitioners must translate regulatory mandates into operational workflows. The section below outlines the typical arc from case intake through remedy selection, highlighting key decision points where economic analysis informs legal strategy.

{% hint style="info" %}
**Investigation Workflow Overview**

```
INTAKE                 SCOPING                ANALYSIS               DECISION
   |                      |                      |                      |
   v                      v                      v                      v
+--------------+    +--------------+    +--------------+    +--------------+
| Complaint /  |    | Data         |    | Market       |    | Statement    |
| Leniency /   |--->| inventory &  |--->| definition & |--->| of Issues /  |
| Notification |    | custodians   |    | effects      |    | White Paper  |
+--------------+    +--------------+    +--------------+    +--------------+
       |                  |                   |                    |
       v                  v                   v                    v
  "Hot docs"         Preservation        Econometric          Remedies
  triage             protocols           + qualitative        discussion
                          |                   |
                          v                   v
                    +--------------+    +--------------+
                    | Quick        |    | Test         |
                    | screens:     |    | theories:    |
                    | - Shares/HHI |    | - DiD / IV   |
                    | - Entry data |    | - Simulation |
                    | - Margins    |    | - Documents  |
                    +--------------+    +--------------+
```
**Key decision points:** At each transition, evaluate whether additional data work or qualitative evidence offers the better marginal return given deadlines and burden of proof.
{% endhint %}

Regardless of jurisdiction, investigations follow a recognizable arc. Matters typically begin with a complaint, leniency application, or merger notification. Case teams triage with “hot docs” and quick descriptive analytics, draft a plan that allocates legal and economic workstreams, and establish preservation plus data-request protocols. The second phase is scoping: enumerating data systems, prioritizing custodians, negotiating production formats, and deciding whether to run early econometric screens—such as price-cost margins or diversion ratios—before collecting more costly qualitative evidence. In phase three the team synthesizes theory and evidence into statements of issues, white papers, or ultimately pleadings and testimony. Finally, remedies discussions integrate forward-looking modeling with institutional constraints: can the Competition Tribunal in Pretoria supervise behavioral commitments as effectively as US courts, or is divestiture the only reliable fix? Always document these choices so that tribunals (and future teams) can reconstruct the evidentiary chain.

### Scoping data needs early
Practitioners treat data, documents, and interviews as complements rather than substitutes. Intake meetings should generate inventories of transactional databases, billing systems, CRM extracts, internal forecasts, board presentations, and benchmark studies. The task is to identify what can be measured quickly (e.g., monthly price series, bidding outcomes, churn metrics) and what requires longitudinal assembly (e.g., claims-level healthcare data or network telemetry). Teams should simultaneously plan qualitative work: establish search terms for electronically stored information (ESI), design interview protocols, and identify third parties—customers, suppliers, former employees—whose perspectives sharpen or rebut economic priors. Missing this early sequencing is costly; see the Competition Commission South Africa’s review of Netcare/Community Hospital Group, where late-stage data disputes shortened the time available for substantive modeling.

### Illustrative vignette: Search dominance diagnostics
The 2020–2023 DOJ challenge to Google Search (*United States v. Google (Search)*, 2023) illustrates how process and substance intertwine. Economists combined browser default share calculations, auction revenue data, and margin analyses with interview testimony from handset makers and browser developers. Those fact narratives clarified why certain regression designs mattered (e.g., estimating counterfactual query volume absent default contracts). Compare that to the Competition Commission South Africa's investigation into digital platforms and app stores (SA OIPMI Final Report, 2023), where documentary evidence about self-preferencing and ad-tech fee structures filled gaps in transaction data. The lesson: quantitative rigor carries the day only when tied to institutional detail about distribution agreements, switching costs, and remedy administrability.

{% hint style="info" %}
**Method box: Integrating empirics here**

Early-stage screening rarely needs sophisticated econometrics. Build dashboards that pull together market shares, HHI trends, entry/exit indicators, and switching matrices from customer-level data. Combine transactional datasets with public sources (e.g., SEC filings, the FTC’s merger statistics, Stats SA tariff books) to benchmark plausible margins. When data are thin, like in new fintech or biotech markets pivot, quickly to qualitative or expert evidence rather than forcing underpowered regressions. Document these decisions in a running technical memo so litigators can later explain why the team prioritized one technique over another.
{% endhint %}

{% hint style="info" %}
**Qualitative evidence**

Treat qualitative work as disciplined research, not anecdote hunting. Begin with an interview guide that connects each theory of harm to specific questions, and pair every interview with contemporaneous notes plus sourcing metadata (custodian, date, privilege status). For document review, align search strings with economic hypotheses—for example, pairing “capacity discipline” with “shutdown” when probing fertilizer cartel allegations in the US Midwest and South Africa's Sasol case (*Competition Commission v. Sasol*, 2014). Create chronologies that marry documentary excerpts with data milestones; these become invaluable when explaining to a tribunal why a particular conduct pattern aligns with measured price changes or customer churn.
{% endhint %}

{% hint style="info" %}
**Case box: Quick tour**

Recent matters illustrate the diversity of evidentiary mixes. The *US v. Microsoft* (*United States v. Microsoft*, 2001) legacy is still instructive for tying and exclusion, but newer platform cases—*US v. Google Search* (*United States v. Google (Search)*, 2023) and the FTC's Meta/Within suit—highlight how product design data and third-party developer testimony reinforce each other. Airline collaborations such as DOJ v. American Airlines/JetBlue (NEA) show how scheduling data, revenue management simulations, and traveler surveys combine to test unilateral and coordinated effects. Global cartel work remains vibrant: the EU Trucks cartel decisions, the KFTC’s memory chip probes, and South Africa’s construction and bread cartels each turned on leniency statements corroborated by bidding records and cost analyses. Labor markets are now front-page antitrust: US wage-fixing cases in healthcare and the 2023 consent orders in the poultry industry relied on HR databases and interview evidence from recruiters.
{% endhint %}

{% hint style="info" %}
**Comparative note**

While the US emphasizes adversarial hearings and judicial precedent, DG COMP and the CMA operate administrative processes where agencies both investigate and decide. This affects research timing: EU cases often allow broader use of compelled internal data but require detailed written submissions early, whereas South African proceedings feature public-interest considerations that demand additional qualitative evidence (jobs, ownership, regional development). Asian agencies have diverse discovery rules—SAMR can request granular consumer data with little advance notice—so plan modular analyses that adapt as production obligations change. Throughout the book, sidebar notes will flag where legal standards (dominance vs. monopoly), burdens of proof, or remedy preferences diverge.
{% endhint %}

## Exercises

1. **Conceptual.** Compare how the same conduct (e.g., exclusive dealing) would be analyzed under US Sherman Act §1, EU Article 101, and SA Competition Act §4. What differences in burden of proof and legal standard would affect your research design?

2. **Conceptual.** A client brings you a potential merger notification. Draft a one-page scoping memo identifying: (a) the likely relevant markets, (b) data sources you would request, (c) which jurisdiction's timeline is most binding, and (d) whether the evidence triad suggests prioritizing quantitative, qualitative, or documentary evidence first.

3. **Case discussion.** Read the comparative statute table. Identify one conduct type where the US and EU approaches diverge most sharply. How would this divergence affect an economist advising a multi-jurisdictional client?

4. **Conceptual.** What is the significance of South Africa's public-interest test for antitrust analysis? Give an example of how it might change the outcome of a merger review compared to a pure consumer-welfare standard.

5. **Data/research.** Using publicly available data from agency websites (DOJ, FTC, EC, SA Competition Commission), compile a table of the 5 most recent merger challenges in each jurisdiction. What patterns do you observe in terms of industries targeted, theories of harm, and remedies imposed?

## Looking ahead

Orientation work is only useful if it flows directly into research design. In **Chapter 02**, we translate the institutional map above into concrete analytical workplans—building case chronology templates, sketching data inventories, and establishing the evidence-integration frameworks that will structure every subsequent chapter.

**Before proceeding, prepare:**

1. **Case chronology template**: Build a timeline that can accommodate both US and SADC procedural milestones.
2. **Data inventory**: Sketch which datasets span US, EU, and SADC sources (e.g., FRED for HHI, Stats SA for market shares).
3. **Flagship dataset**: Identify at least one dataset (claims-level healthcare data, national tender records) that will power the quantitative chapters.

Keep a running list of figures—HHI trends, entry timelines, platform governance maps—that we will revisit throughout the book. This ensures the narrative remains visually anchored and cumulative, with each chapter building on artifacts from previous ones.

## Visualizations

### Agency and case timeline
This timeline pairs statutory milestones with landmark enforcement actions so readers can anchor later quantitative work in institutional change. We include US, EU, and South African milestones to reflect the multi-jurisdictional focus of this book.

![Antitrust Milestones: US, EU, and South Africa](../images/antitrust-timeline-1.png)

{% hint style="info" %}
**Timeline interpretation**

The timeline shows convergence in competition enforcement approaches: South Africa's 1998 Competition Act (SA Competition Act, 1998) drew heavily on EU precedent, while the 2023 US Merger Guidelines (DOJ/FTC Merger Guidelines, 2023) moved closer to EU-style structural presumptions. Note how major cases (Microsoft (*United States v. Microsoft*, 2001), Google (*United States v. Google (Search)*, 2023); (*Google Shopping*, 2017)) often span jurisdictions with related but distinct theories of harm.
{% endhint %}

### HHI trend example
Track concentration trends using FRED data as a baseline for cross-jurisdictional comparisons.

![US Bank Concentration (HHI)](../images/us-bank-hhi-1.png)

