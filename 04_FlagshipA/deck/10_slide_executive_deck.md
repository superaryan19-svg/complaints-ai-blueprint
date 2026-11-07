# Flagship A: 10-Slide Executive Presentation Deck
**Client**: Kestrel Bank | **Audience**: Executive Steering Committee & Board | **Week**: 11  
**Format**: Action-Titled Slides for an 8-Minute Executive Pitch  

---

### Slide 1: Title & Executive Summary
> **Action Title: AI can cut complaint handling effort by about a quarter, if we start with the process.**

* **The Core Findings**:
  1. Six complaint categories drive 81% of volume; knowledge fragmentation across 4 systems causes ~50% of handle time.
  2. Six operational quick wins resolve immediate SLA drift with zero technology licensing cost.
  3. A targeted AI copilot delivers an 18-month payback and ₹127.5L NPV—justified by avoiding RBI Ombudsman penalties.
* **The Strategic Ask**:
  * Approve **₹18 lakh** for Phase 1 single-team pilot deployment (Cards). Full Phase 2 rollout (₹68L) to be decided at **Gate 2** based on measured pilot telemetry.
* *Labels: All financial figures sourced from verified A2 model; assumptions cataloged in register.*

---

### Slide 2: Problem Concentration (A1 Diagnostic)
> **Action Title: A handful of issue types and one root cause drive most complaints.**

* **Visual Element**: High-resolution Pareto distribution chart (`outputs/pareto_issues.png`).
* **Key Supporting Takeaways**:
  * 6 of 11 issues account for **81.4% of total complaints**, led by Fees/Interest (23.9%) and Statement Disputes (18.6%).
  * **30.6% of closed cases conclude with customer relief**, proving high initial operational error rates.
  * Median intake routing lag is **0.0 days**; delay does not occur at intake, but during policy lookup.
* *Footnote: Stand-in CFPB data (N=23,046); 40,000 monthly volume scaled for Kestrel Bank [AS-01].*

---

### Slide 3: Immediate Operational Improvements (Non-AI Fixes)
> **Action Title: Six fixes need no AI and should start now.**

* **Visual Element**: 6-Fix Action Matrix with operational owners and turnaround timelines.
* **Key Supporting Takeaways**:
  * **1-Day Auto-Acknowledgement**: Reassures customers and satisfies RB-IOS norms (Contact Center).
  * **Standard CRM Categories**: Cuts ticket misrouting from 20% to $<8\%$ (CRM Ops).
  * **₹1,500 Discretionary Agent Authority**: Eliminates 4–6 day supervisor queue for routine fee disputes (Finance).
  * **Single Knowledge Custodian**: Consolidates 4 intranet stores under the Principal Nodal Officer.
  * **Automated Day-25 Warning Alert**: Prevents complaints from drifting past the 30-day Ombudsman cliff.
* *Footnote: Zero software procurement required; immediate 10–15% SLA turnaround improvement.*

---

### Slide 4: Operational Voice of the Frontline (Discovery)
> **Action Title: Agents lose most time searching for policy and rewriting replies.**

* **Visual Element**: Pain-Point Register (P1 to P5) mapped against frontline interview quotes.
* **Key Supporting Takeaways**:
  * *"I spend 15 minutes checking four portals just to verify if an annual card fee waiver applies."*
  * *"When tickets are misrouted, they bounce between Cards and Digital for three days before anyone reads them."*
  * Frontline agents spend **~10 minutes rewriting standard circular text** for routine card responses.
* *Footnote: Validated through 5 operational stakeholder interviews; baseline AHT calibrated at 25 min [AS-02].*

---

### Slide 5: Future-State Operating Model (To-Be BPMN)
> **Action Title: AI should assist agents at three points, with a human approving every reply.**

* **Visual Element**: To-Be Process Swimlane Diagram with step tags (`H`, `R`, `AI`).
* **Key Supporting Takeaways**:
  * **Manual touchpoints cut by 36%** (from 11 down to 7 human steps).
  * Automated rules (`[R]`) enforce 1-day acknowledgements and 30-day SLA timers.
  * AI inference (`[AI]`) deployed for **Triage**, **Policy RAG**, and **Drafting**.
  * **Zero Autonomous Agents (`[AG] = 0`)**: Every outgoing reply requires human agent verification.
* *Footnote: Strictly complies with RBI FREE-AI guidelines preserving human operational accountability.*

---

### Slide 6: Use-Case Prioritization Matrix (Decision Ladder)
> **Action Title: Two use cases are ready now; two should not be done at all.**

* **Visual Element**: Value vs. Feasibility Matrix with 9 evaluated use cases.
* **Key Supporting Takeaways**:
  * **Do First (Phase 1)**: Triage & Routing (Score 26) and Policy RAG Q&A (Score 24).
  * **Plan Carefully (Phase 2)**: Guided Reply Drafting (Score 22; high value, requires approval guardrails).
  * **Quick Wins**: Escalation Summaries (Score 24) and Batch Theme Mining (Score 23).
  * **Explicit Rejections**: Auto-sending unreviewed replies (Score 17) and AI compensation awards (Score 14).
* *Footnote: Scored across 6 criteria (Financial, Regulatory, Data, Technical, Risk, Adoption).*

---

### Slide 7: Commercial Business Case & Sensitivity (A2 Financials)
> **Action Title: The base case pays back in 18 months, but only if escalations fall.**

* **Visual Element**: Summary Financial Table + 8-Driver Tornado Sensitivity Chart (`tornado_chart.png`).
* **Key Supporting Takeaways**:
  * **3-Year Base NPV is ₹127.5 lakh** (86% ROI) with an **18-month payback period**.
  * On labor savings alone, project does not break even (NPV -₹23.4L); savings come from avoiding RBI fines.
  * **Adoption is the #1 Risk**: Below 50% adoption, the project fails to break even.
  * **Tokens are only ~8% of 3-Year TCO**: Fixed platform engineering and change management dominate.
* *Footnote: 12% discount rate applied; cash flows discounted at 50% realization factor [AS-09].*

---

### Slide 8: Regulatory & Compliance Architecture (Governance)
> **Action Title: The design meets DPDP, FREE-AI and RB-IOS requirements from day one.**

* **Visual Element**: Statutory Control Architecture Map.
* **Key Supporting Takeaways**:
  * **DPDP Compliance**: Client-side PII scrubbing redacts PAN, Account #, and Aadhaar prior to model calls.
  * **72-Hour Breach Runbook**: Encrypted logging, India data residency, and tested DPBI notification protocols.
  * **FREE-AI Alignment**: Registered in Central AI Inventory with explicit risk tiering and model risk cards.
  * **RB-IOS Safeguard**: Automated Day-25 warning alerts ensure compliance before the 30-day statutory clock expires.
* *Footnote: Legal and compliance sign-off mandatory prior to Gate 1 pilot launch.*

---

### Slide 9: Phased Implementation & Stage Gates (Roadmap)
> **Action Title: Three gates let the bank stop or scale based on evidence.**

* **Visual Element**: 12-Month Roadmap Gantt Chart with 3 Decision Milestones.
* **Key Supporting Takeaways**:
  * **Phase 0 (M1–M2)**: Non-AI quick wins; knowledge consolidation; evaluation set design.
  * **Gate 1 (M2)**: Pilot Go/No-Go ($\ge 90\%$ triage test accuracy, privacy audit complete).
  * **Phase 1 (M3–M5)**: Single-team pilot on Cards (30 agents).
  * **Gate 2 (M5)**: Expand to 4 teams + Add drafting ($\ge 80\%$ acceptance, $\le 15\%$ override, 0 PII leaks).
  * **Phase 2–3 (M6–M12)**: Enterprise scale to 120 agents; narrow internal agentic automation.
* *Footnote: Change management stream embedded throughout: 8 champions, 2-hr training, weekly huddles.*

---

### Slide 10: Value Tracking & Next Steps (A3 Telemetry)
> **Action Title: We will know it is working within 90 days.**

* **Visual Element**: Mockup of A3 Telemetry Dashboard with CFO, COO, CRO, and Sponsor views.
* **Key Supporting Takeaways**:
  * Live monitoring across 4 persona pages: Cost per run (₹0.70), Acceptance (89.7%), Overrides (10.3%).
  * Clear early warning triggers: Sustained override rates $>15\%$ automatically pause model scaling.
* **Immediate Recommended Actions (Next 30 Days)**:
  1. Approve Phase 0 non-AI quick wins (CRM categories and 1-day auto-acknowledgements).
  2. Authorize ₹18 lakh discovery & pilot build budget for Cards team deployment.
  3. Appoint Principal Nodal Officer as chair of the AI Steering Committee.
* *Footnote: Deliverable suite includes full Python scripts, Excel model, Power BI telemetry, and BRD.*
