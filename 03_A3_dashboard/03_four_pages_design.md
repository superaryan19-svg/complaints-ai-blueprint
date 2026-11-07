# A3 Dashboard Page Layouts & Storytelling Specifications
**Project**: Kestrel Bank AI Value Dashboard | **Module**: A3 Power BI Visual Engineering  

---

## Executive Design Rules
* **Question-Based Titles**: Every page title answers a specific executive question (e.g., *"Is it safe?"*), giving each report page a single, focused objective.
* **4-Card Top Banner**: Top 4 KPI cards answer *"How are we doing?"*; central chart answers *"Which way is it trending?"*; side breakdown answers *"Where is the variance?"*.
* **Synced Slicers**: Date range (`DimDate[Date]`), Business Unit (`DimTeam[team]`), and Use Case (`DimUseCase[use_case]`) synced across all 4 pages.

---

## Page 1: Executive View (CFO)
* **Audience**: Chief Financial Officer & Investment Steering Committee
* **Core Question**: *"Is this paying for itself?"*
* **Top KPI Cards**:
  1. `[AI Cost INR]` (₹45,017)
  2. `[Realised Value INR]` (₹6.74 lakh)
  3. `[Net Value INR]` (₹6.29 lakh)
  4. `[Cost per Run INR]` (₹0.70)
* **Central Visual**: Line chart of `[Cumulative Net Value INR]` by `DimDate[Date]`.
* **Side Visual**: Clustered bar chart of `[AI Cost INR]` broken down by `DimUseCase[use_case]`.
* **Mandatory Footnote Box**:  
  > *"Note: Net value reflects direct model usage vs. realized labor capacity. It excludes upfront build Capex (₹86L) and annual fixed platform Run costs (₹40L), which are fully amortized in the A2 Business Case."*

---

## Page 2: Operations View (COO)
* **Audience**: Chief Operating Officer & Contact Center Operations Head
* **Core Question**: *"Is it making the team faster?"*
* **Top KPI Cards**:
  1. `[Hours Saved]` (3,370 hrs)
  2. `[Runs per Day]` (718 runs/day)
  3. `[Acceptance Rate]` (89.7%)
  4. `[Human Escalation Rate]` (6.0%)
* **Central Visual**: Stacked column chart of `[Hours Saved]` by `DimDate[Week Start]`.
* **Side Visual**: Horizontal bar chart of `[Acceptance Rate]` by `DimTeam[team]` with an 80% reference target line.
* **Benchmark Target Callout**: Average Handle Time (AHT) trending down from **25.0 min baseline $\rightarrow$ 19.0 min target**.

---

## Page 3: Risk & Governance View (CRO)
* **Audience**: Chief Risk Officer, Compliance & Data Protection Officer (DPO)
* **Core Question**: *"Is it safe and compliant?"*
* **Top KPI Cards**:
  1. `[Override Rate]` (10.3%)
  2. `[Guardrail Flag Rate]` (3.4%)
  3. `[PII Blocks]` (944 incidents)
  4. `[Human Escalation Rate]` (6.0%)
* **Central Visual**: Line chart of `[Override Rate]` by `DimDate[Week Start]` with an explicit **15% Threshold Risk Line**.
* **Side Visual**: Matrix heatmap: `FactAIEvents[guardrail_flag]` $\times$ `DimUseCase[use_case]`.
* **Risk Guidance Note**:  
  > *"Override rate tracks agent rejections. Any sustained breach above 15% for two consecutive weeks automatically triggers prompt and knowledge-base re-audit."*

---

## Page 4: Project Sponsor View (Customer Service Head)
* **Audience**: Head of Customer Service & Change Management Leads
* **Core Question**: *"Are agents actually adopting the copilot?"*
* **Top KPI Cards**:
  1. `[Active Agents]` (120 agents)
  2. `[Adoption %]` (100% of pilot cohort)
  3. `[Runs per Agent]` (538 runs)
  4. `[Teams Live]` (4 teams)
* **Central Visual**: Line chart of `[Active Agents]` by `DimDate[Week Start]` showing the ramp curve from 52 to 120 agents.
* **Side Visual**: 100% stacked bar chart of `[AI Runs]` by `DimTeam[team]` segmented by `DimUseCase[use_case]`.

---

## Interview Defense Concept: "Deflection Rate"
> **Question**: *"How did you calculate deflection rate in this dashboard?"*  
> **Consultant Answer**:  
> *"Deflection rate is defined as contacts fully resolved via customer self-service divided by total inbound contacts. In Kestrel Bank's Phase 1 and 2, the AI tool is an **internal agent copilot**, not a customer-facing chatbot. Therefore, zero complaints are deflected—100% still reach a human agent. Deflection will only apply in Phase 3 if automated self-service tier-0 resolution is introduced."*
