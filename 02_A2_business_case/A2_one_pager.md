# Executive One-Pager: GenAI Cost & ROI Analysis
**Project**: Kestrel Bank AI Transformation | **Module**: A2 Financial Business Case  
**Date**: November 2026 | **Author**: Techno-Consultant Engagement Team  

---

## Executive Recommendation
> **"A ₹86 lakh investment pays back in ~18 months, delivering a 3-Year Base NPV of ₹127.5 lakh and an 86% ROI — provided the pilot achieves $\ge 60\%$ agent adoption and reduces Ombudsman escalations by 15%. We recommend funding Phase 1 only and approving Phase 2 at Gate 2 based on measured pilot metrics."**

---

## The Four Core Consultant Takeaways

### 1. AI is Cheap Per Complaint; Agent Time is Not
* **The Math**: The model API cost across all three use cases (Triage, Reply Drafting, Policy RAG) averages **₹2.12 ($0.0241) per complaint**, compared to **~₹167 of agent handling cost** (25 minutes at ₹400/hour loaded cost).
* **The Insight**: AI efficiency delivers disproportionate operational leverage. Even tripling token prices changes NPV by less than ₹36 lakh.

### 2. This is a Regulatory & Customer Quality Case, NOT a Pure Cost-Cutting Case
* On **hard labor savings alone**, the project **does not pay back within 3 years** (NPV **-₹23.4 lakh**).
* Payback is achieved solely by reducing escalations to the **RBI Integrated Ombudsman** (avoiding administrative review costs and potential penalties up to ₹30 lakh under RB-IOS 2026).
* **Consulting Rule**: Present both **Hard Benefits** and **Full View** transparently to the CFO. A CFO will approve on hard savings plus strategic upside, but will distrust a model that claims 100% of saved minutes instantly convert to payroll cuts.

### 3. Agent Adoption is the Single Biggest Business Risk
* Sensitivity analysis reveals that **Adoption Rate** is the widest bar on the Tornado chart (swing of **₹174.1 lakh** in NPV).
* If adoption drops below **50%**, the investment fails to break even.
* **Strategic Implication**: The rollout budget and engineering effort must focus on **workflow integration, prompt usability, and change management**, not just model tuning.

### 4. Tokens Represent Only ~8% of 3-Year TCO
* Over 3 years, token costs represent only **8.2% (₹17.1 lakh)** of total expenditure (₹2.09 crore).
* Fixed run costs (internal engineering, MLOps, model risk reviews, hosting) and upfront build costs account for **>91%** of spend.
* **Strategic Implication**: Switching to cheaper open-source models moves the needle very little; maximizing agent utilization of existing models moves the needle massively.

---

## Scenario Comparison Table

| Metric | Worst Case (1) | Base Case (2) | Best Case (3) | Verification Target |
| :--- | :---: | :---: | :---: | :---: |
| **Model Cost per Complaint** | ₹2.12 | **₹2.12** | ₹2.12 | $\le ₹3.00$ |
| **Target Adoption** | 55% | **80%** | 90% | $\ge 60\%$ at Gate 2 |
| **Acceptance Rate** | 70% | **85%** | 92% | $\ge 80\%$ at Gate 2 |
| **Annual Hours Saved (Year 3)** | 27,227 hrs | **49,504 hrs** | 63,222 hrs | Operational buffer |
| **3-Year NPV (Hard Benefits Only)** | -₹123.3 lakh | **-₹23.4 lakh** | ₹75.6 lakh | Realised @ 50% |
| **3-Year NPV (Full View)** | **-₹68.0 lakh** | **₹127.5 lakh** | **₹324.6 lakh** | Hurdle @ 12% Disc |
| **Payback Period (Full View)** | Not within 3 yrs | **1.50 yrs (18 mos)** | **1.05 yrs (13 mos)** | $\le 24$ months target |
| **3-Year ROI (Full View)** | -27% | **86%** | **197%** | Net positive |
| **Token Share of 3-Year TCO** | 5.8% | **8.2%** | 9.1% | $< 12\%$ ceiling |

---

## Sensitivity & Risk Ranking (Tornado Summary)

```
                       Change in 3-Year NPV vs Base (₹ Lakh)
                          Downside (Red) | Upside (Green)
Adoption (50% → 95%)        [-116.1L] ===|================ [58.0L]    (Swing: ₹174.1L)
Cost/Escalation (₹2.5k → ₹8k) [-75.4L] ==|====================== [90.5L] (Swing: ₹165.9L)
Realisation (30% → 70%)       [-69.2L] ==|================= [69.2L]    (Swing: ₹138.4L)
Minutes Saved (0.6x → 1.3x)   [-69.2L] ==|============= [51.9L]        (Swing: ₹121.1L)
Agent Cost (₹300 → ₹500/hr)   [-43.2L] =|========== [43.2L]           (Swing: ₹86.4L)
Run Cost (1.5x → 0.75x)       [-48.0L] =|====== [24.0L]                (Swing: ₹72.0L)
Acceptance (65% → 95%)        [-40.7L] =|===== [20.3L]                 (Swing: ₹61.0L)
Token Price (3x → 0.5x)       [-28.5L] =|== [7.1L]                     (Swing: ₹35.6L)
```
*(Reference visual saved at `02_A2_business_case/tornado_chart.png`)*

---

## Interview Defense & Mental Math Drill

### Q1: "Estimate the monthly LLM cost for 2,000 users."
> **Formula**: $\text{Users} \times \text{Queries/Day} \times \text{Working Days} \times \text{Cost/Query}$  
> **Calculation**: $2,000 \times 10 \times 22 \times \$0.017 \approx \$7,480 \approx \$7,500\text{/month}$ ($\approx \mathbf{₹6.6\text{ lakh/month}}$ at ₹88/USD).  
> *Always state assumptions aloud: 10 queries/agent/day, 22 working days, Sonnet 5.5 cached rate.*

### Q2: "How would you reduce LLM inference costs by 40%?"
1. **Model Routing**: Route simple triage and extraction tasks to Claude Haiku 5.5 ($0.10/1M) instead of Sonnet ($2.00/1M).
2. **Aggressive Prompt Caching**: Cache common policy documents and system prompts to achieve 90% read discount ($0.10/1M).
3. **Batch Mode for Asynchronous Work**: Run nocturnal root-cause clustering and theme analysis at 50% discount via Batch API.
4. **Output Token Ceilings**: Constrain maximum completion tokens (every 100 output tokens avoided saves money).
5. **Drive Higher Adoption**: Fixed run costs and platform engineering dominate TCO; maximizing volume reduces unit overhead.
