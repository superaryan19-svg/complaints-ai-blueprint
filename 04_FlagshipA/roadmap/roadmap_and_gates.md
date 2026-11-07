# Flagship A: 12-Month Phased Roadmap with Stage Gates
**Client**: Kestrel Bank | **Project**: Enterprise AI Transformation Blueprint | **Week**: 11  
**Module**: 04_FlagshipA/roadmap/roadmap_and_gates.md  

---

## 1. Phased 12-Month Implementation Timeline

```mermaid
gantt
    title Kestrel Bank AI Transformation Implementation Roadmap
    dateFormat  YYYY-MM
    axisFormat  %b %Y

    section Phase 0 (Quick Wins)
    Deploy 6 Non-AI Operational Fixes       :done, p0_1, 2026-01, 2026-02
    Centralize Knowledge Base & Categories  :done, p0_2, 2026-01, 2026-02
    Gate 1 Review (Pilot Readiness)         :milestone, g1, 2026-02-28, 0d

    section Phase 1 (Single Team Pilot)
    Deploy Triage & Policy RAG (Cards Team) :active, p1_1, 2026-03, 2026-05
    Pilot Telemetry & A3 Dashboard Tracking :active, p1_2, 2026-03, 2026-05
    Gate 2 Review (Scale & Add Drafting)    :milestone, g2, 2026-05-31, 0d

    section Phase 2 (Four-Team Expansion)
    Rollout Guided Drafting (HITL)          :p2_1, 2026-06, 2026-08
    Scale to CASA, Digital & Branch Teams   :p2_2, 2026-06, 2026-08
    Gate 3 Review (Enterprise Scale)        :milestone, g3, 2026-08-31, 0d

    section Phase 3 (Full Scale & Agentic)
    Full Enterprise Operations (120 Agents) :p3_1, 2026-09, 2026-12
    Internal Agentic Document Aggregation   :p3_2, 2026-10, 2026-12
```

---

## 2. Formal Stage-Gate Decision Criteria

Every gate represents a binding **Go / No-Go decision** governed by pre-agreed quantitative criteria:

| Stage Gate | Scheduled Date | Core Investment Decision | Mandatory "Go" Criteria (All Must Pass) |
| :---: | :---: | :--- | :--- |
| **Gate 1** | **Month 2** | **Approve Single-Team Pilot Go-Live** (Cards, 30 agents) | 1. Six Phase 0 non-AI fixes deployed and verified in CRM.<br>2. Information Security and DPDP privacy review signed off.<br>3. Central AI Registry entry approved by Risk Committee.<br>4. Evaluation test sets validated ($\ge 90\%$ triage, $\ge 85\%$ RAG).<br>5. Pilot team baseline handling time captured (25 min). |
| **Gate 2** | **Month 5** | **Approve 4-Team Expansion (120 agents) & Enable Reply Drafting** | 1. Agent Acceptance Rate $\ge 80.0\%$ over pilot.<br>2. Agent Override Rate $\le 15.0\%$.<br>3. **Zero unmasked PII leakage incidents**.<br>4. $\ge 60.0\%$ of pilot agents active weekly.<br>5. Ombudsman escalations trending downward vs. baseline.<br>6. Financial business case re-run with live pilot telemetry. |
| **Gate 3** | **Month 9** | **Approve Enterprise Steady-State & Narrow Agentic Steps** | 1. Gate 2 performance sustained for 3 consecutive months.<br>2. Measured financial payback confirmed $\le 24$ months.<br>3. Compliance and Legal sign-off on any proposed automation.<br>4. Unit cost confirmed $\le ₹3.00$ per complaint handled. |

---

## 3. Dedicated Change Management & Training Program
> *"The tornado analysis proved that Agent Adoption is the single largest determinant of project ROI. Change management is therefore treated as a primary engineering stream, not an afterthought."*

* **Frontline AI Champion Network**: Identify two respected senior agents in each of the four business units to serve as dedicated floor champions during initial rollout.
* **Role-Specific Training Program**: 2-hour interactive workshop covering prompt phrasing, reading citations, evaluating draft accuracy, and logging overrides.
* **Weekly 15-Minute Operational Huddles**: Weekly feedback sessions between frontline champions and the AI Product Owner to review rejected drafts and eliminate prompt friction.
* **Empowering Strategic Framing**: Reinforce in all executive and town-hall communications that **the AI Copilot eliminates administrative searching and typing; it does not replace banking professionals**.
