# Flagship A: Executive Case Study
**Engagement**: AI Transformation Blueprint for Banking Complaint Operations  
**Client**: Kestrel Bank (Fictional Mid-Size Indian Commercial Bank)  
**Author**: Techno-Consultant Strategy Team | **Date**: November 2026  

---

## 1. Context (60 Words)
Kestrel Bank is a mid-sized Indian private-sector commercial bank handling ~40,000 retail complaints monthly across 120 agents in four business units (Cards, CASA, Digital Banking, Branch Escalations). Acting as external techno-consultants, we evaluated whether Generative AI could accelerate grievance resolution and mitigate regulatory exposure under the Reserve Bank – Integrated Ombudsman Scheme (RB-IOS 2026). Public CFPB data served as an empirical structural stand-in.

---

## 2. Problem Statement & SCQ (60 Words)
Surging digital adoption increased complaint volumes while agent capacity remained constrained. Grievance handling suffered from severe information fragmentation across four disconnected intranet repositories, causing ~12% of complaints to drift past the 30-day statutory threshold. This exposed the bank to regulatory penalties, mandatory audits, and RBI Ombudsman compensation awards up to ₹30 lakh per case.

---

## 3. Engagement Approach (150 Words)
We applied a hypothesis-driven management consulting approach structured in seven disciplined phases:
1. **Lean Six Sigma DMAIC Diagnostic (A1)**: Filtered 24-month banking complaints using Python (`pandas`), calculated baseline KPIs, constructed a Pareto distribution of top issues, sampled 100 complaint narratives for qualitative NLP audit, and conducted 5 Whys root-cause analysis.
2. **Operational Discovery**: Mapped stakeholder priorities and conducted structured 30-minute operational interviews to construct a prioritized pain-point register (P1–P5).
3. **Process Redesign**: Engineered an AI-aware To-Be BPMN workflow incorporating strict Human-in-the-Loop (HITL) checkpoints.
4. **Use-Case Prioritization**: Evaluated candidate automations against the "Decision Ladder", filtering out high-risk ideas.
5. **Financial Business Case (A2)**: Modeled a 3-year cash flow in Microsoft Excel integrating Anthropic prompt caching mechanics, labor realization factors (50%), and 8-driver tornado sensitivity.
6. **Regulatory Governance**: Structured compliance controls for the DPDP Act 2025/2027 and RBI FREE-AI framework.
7. **Value Telemetry (A3)**: Designed a Star-Schema Power BI dashboard across 4 leadership personas.

---

## 4. Key Findings (150 Words)
* **Finding 1 (Measured)**: **Concentration & Avoidable Errors**: 6 of 11 issue categories account for **81.4% of complaints**, led by Fees/Interest (23.9%) and Statement Disputes (18.6%). Crucially, **30.6% of closed cases end with customer relief**, indicating that a large portion of complaints stem from internal operational defects rather than customer misunderstandings.
* **Finding 2 (Measured & Assumed)**: **Knowledge Fragmentation is the Root Bottleneck**: Median intake routing lag is **0.0 days**, proving intake is not the delay. Instead, agents lose **12–15 minutes per case** searching across 4 siloed policy repositories.
* **Finding 3 (Modeled)**: **The Business Case is Regulatory-Driven**: At ₹2.12 model cost per complaint, the ₹86 lakh investment achieves an **18-month payback and ₹127.5 lakh NPV (86% ROI)** in the Base Case. However, on labor savings alone, it fails to break even (NPV -₹23.4 lakh). Adoption is the #1 financial driver, while token prices represent only **8.2% of 3-year TCO**.

---

## 5. Strategic Recommendations (100 Words)
* **What to Do**: Deploy six non-AI operational fixes immediately (1-day auto-acknowledgements, standardized CRM categories, ₹1,500 agent refund authority, Day-25 alerting). Concurrently deploy an internal AI Copilot for **Intelligent Triage** (`Claude Haiku 5.5`) and **Policy Knowledge RAG** (`Claude Sonnet 5.5`).
* **What NOT to Do**: **Never deploy autonomous customer replies without human sign-off** (rejected due to regulatory risk), and **never automate compensation decisions**.
* **The Gated Plan**: Fund Phase 1 pilot on Cards (₹18L capex). Gate 2 approval for 4-team expansion requires $\ge 80\%$ acceptance, $\le 15\%$ override, and zero PII leaks.

---

## 6. Expected Impact & Limitations (80 Words)
* **Projected Outcomes**: AHT reduced from 25 to 19 minutes; 30-day resolution rate elevated from 88% to $\ge 95\%$; 49,504 agent hours saved annually by Year 3; RBI Ombudsman escalations reduced by 15%.
* **Analytical Limitations**: The public stand-in dataset lacks exact resolution timestamps; handling times (25 min) and escalation volumes (3%) are calibrated assumptions. Next operational phase requires validating these baselines during the 90-day Cards pilot.

---

## 7. 90-Second Interview Defense (STAR Format)
* **Situation**: *"Kestrel Bank was facing surging retail complaints, with 12% drifting past the 30-day RBI Ombudsman statutory threshold, risking penalties up to ₹30 lakh."*
* **Task**: *"I was brought in to determine where AI should and should not be deployed, quantify the commercial ROI, and build a safe, compliant rollout blueprint."*
* **Action**: *"Using Lean Six Sigma and Python, I diagnosed that the root cause was policy knowledge fragmentation across four portals, not agent negligence. I first established six non-AI operational fixes. Then, using the Decision Ladder, I prioritized an internal agent copilot for Triage and Policy RAG, while explicitly rejecting unreviewed auto-replies. I modeled the 3-year financial case in Excel, proving an 18-month payback that was highly sensitive to adoption but largely unaffected by token prices, and designed a Power BI value telemetry framework."*
* **Result**: *"Delivered a stage-gated 12-month blueprint with an ₹86 lakh build cost, ₹127.5 lakh NPV, and 86% ROI, governed by DPDP and RBI FREE-AI compliance controls."*
