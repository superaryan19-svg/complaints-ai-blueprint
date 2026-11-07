# AI Transformation Blueprint for Complaint Operations (Kestrel Bank)
> **Category A Techno-Consultant Portfolio Deliverable**  
> *Targeting Management Consulting & Big 4 GenAI / Business Analytics Engagements*

---

## 1. Executive Summary
This repository contains the end-to-end consulting deliverables for **Kestrel Bank** (a fictional mid-sized Indian private-sector bank), answering the core mandate:  
> *"Where should Kestrel Bank use AI in complaint handling, what will it return, and how do we roll it out safely?"*

The engagement addresses rising customer complaint volumes (~40,000/month across 120 agents) and mitigating compliance risks under the **Reserve Bank – Integrated Ombudsman Scheme (RB-IOS 2026)** and the **Digital Personal Data Protection Act (DPDP Act & Rules)**. Rather than prematurely deploying unconstrained autonomous agents, this project applies a rigorous Lean Six Sigma DMAIC diagnostic, token-level financial engineering, Power BI value tracking, and an enterprise governance blueprint.

---

## 2. Five Key Findings
1. **Knowledge & Process, Not People**: The primary driver of handle time delay is disparate knowledge storage across four unintegrated systems. Process and ownership fixes must precede AI implementation.
2. **Non-AI Fixes First**: 6 operational fixes (CRM categorization, SLA auto-acknowledgements, Day-25 escalation alerts) resolve major bottlenecks with zero software licensing costs.
3. **The Business Case is Regulatory & Quality-Driven**: On pure labor hours saved, the investment does not achieve 3-year payback (NPV -₹23.4 lakh). When factoring in avoided RBI Ombudsman escalations and penalties, the project delivers a **Base NPV of ₹127.5 lakh** with an **18-month payback**.
4. **Adoption Outweighs Model Costs**: Token costs represent only **~8% of the 3-year Total Cost of Ownership (TCO)**. Sensitivity analysis shows agent adoption is the single largest determinant of ROI.
5. **Human-in-the-Loop is Mandatory**: Under RBI FREE-AI guidelines, autonomous customer replies are rejected. AI is deployed solely as an internal agent assistant for triage, policy RAG, and drafting, with mandatory human verification.

---

## 3. Repository Architecture

```
complaints-ai-blueprint/
├── 00_admin/
│   ├── client_brief.md                 # Context, constraints, and mandate
│   ├── assumptions_register.xlsx       # Labeled assumptions (Measured, Sourced, Assumed)
│   ├── sources.md                      # Citations (RBI, DPDP, CFPB, Anthropic pricing)
│   └── timeline.md                     # 12-week delivery schedule
├── 01_A1_diagnostic/                   # Supporting Project A1 (DMAIC & EDA)
│   ├── data/
│   │   ├── raw/                        # CFPB raw download archive
│   │   └── clean/                      # Filtered banking dataset
│   ├── notebooks/                      # Data pipeline & NLP scripts
│   └── outputs/                        # Pareto charts, Fishbone, SIPOC, KPIs
├── 02_A2_business_case/                # Supporting Project A2 (Financial Model)
│   ├── A2_GenAI_Cost_ROI.xlsx          # 3-year cash flow, scenario switch, tornado analysis
│   └── A2_one_pager.pdf                # Executive financial summary
├── 03_A3_dashboard/                    # Supporting Project A3 (Power BI & Telemetry)
│   ├── ai_event_log.csv                # 90-day simulated telemetry (64,600 events)
│   ├── baseline_targets.csv            # Pre-AI benchmarks vs targets
│   └── A3_AI_Value.pbix                # Star-schema Power BI dashboard (4 persona pages)
├── 04_FlagshipA/                       # Master Flagship Consulting Deliverables
│   ├── discovery/                      # Stakeholder map, interview notes, pain-points
│   ├── process/                        # As-Is & To-Be BPMN with HITL tags
│   ├── requirements/                   # AI-aware BRD, User Stories, RTM
│   ├── governance/                     # DPDP / RBI FREE-AI control map, Risk Register, RACI
│   ├── roadmap/                        # 12-month phased roadmap with 3 stage gates
│   └── deck/                           # 10-slide action-titled executive deck
└── README.md
```

---

## 4. How to Reproduce

### Prerequisites
* Python 3.10+ (tested on Python 3.11)
* Python packages: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `openpyxl`
* Microsoft Excel (Desktop edition for Data Tables & What-If analysis)
* Microsoft Power BI Desktop

```bash
# Clone the repository
git clone <your-repo-url>
cd complaints-ai-blueprint

# Install Python dependencies
pip install pandas numpy matplotlib seaborn scikit-learn openpyxl
```

### Execution Sequence
1. **Assumptions Register**: Run `python 00_admin/generate_assumptions_register.py`.
2. **A1 Diagnostic**: Execute notebooks/scripts in `01_A1_diagnostic/notebooks/` to process complaint data and generate Pareto charts.
3. **A2 Business Case**: Open `02_A2_business_case/A2_GenAI_Cost_ROI.xlsx` to review the financial engine and tornado sensitivity.
4. **A3 Dashboard Data**: Run `python 03_A3_dashboard/a3_simulate_ai_log.py` to generate simulated telemetry logs and open `A3_AI_Value.pbix`.

---

## 5. Methodological & Legal Disclosures
* **Fictional Entity**: Kestrel Bank is a fictional institution designed for demonstration purposes.
* **Public Stand-In Data**: US Consumer Financial Protection Bureau (CFPB) data serves as a proxy for complaint distributions, taxonomy, and linguistic sentiment.
* **Assumption Labeling**: In line with Big 4 consulting best practices, all figures are categorized as **Measured**, **Sourced**, or **Assumed** in the [Assumptions Register](00_admin/assumptions_register.xlsx).
* **Regulatory Compliance**: Summaries of DPDP Rules 2025 and RBI guidelines inform system design and do not constitute formal legal advice.
