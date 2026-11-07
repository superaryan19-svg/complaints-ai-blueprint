# A1 Improve & Control: Non-AI Fixes, AI Mapping & Control Plan
**Project**: Kestrel Bank Complaint Process Diagnostic | **Week**: 3  

---

## 1. The Six Operational Fixes That Require NO AI
> **Consultant Rule**: Recommending process and policy fixes before suggesting AI demonstrates professional maturity. Big 4 interviewers look for this first.

| Fix # | Non-AI Operational Fix | Root Cause Addressed | Implementation Effort | Accountable Owner | Expected Operational Impact |
| :---: | :--- | :--- | :---: | :--- | :--- |
| **1** | **Mandatory 1-Day Auto-Acknowledgement Rule** | Absence of formal intake SLA communication. | **Low** (1 week) | Contact Centre Ops | Eliminates repeat follow-ups; assures compliance with RB-IOS norms. |
| **2** | **Standardize CRM Complaint Categories** | Inconsistent manual categorization in CRM. | **Low** (2 weeks) | CRM Platform Team | Replaces free text with top Pareto categories; cuts misrouting by 40%. |
| **3** | **Clear Refund Approval Authorization Matrix** | Minor fee reversals (< ₹1,500) trapped in supervisor queue. | **Low** (immediate) | Operations + Finance | Grants Level-1 agents pre-approved waiver limits; removes 3–5 days wait. |
| **4** | **Designate Single Complaint Knowledge Owner** | Knowledge scattered across 4 silos; zero accountability. | **Medium** (3 weeks) | Principal Nodal Officer | Establishes monthly policy-to-script review; unifies internal guidance. |
| **5** | **Automated "Day-25 Alert" for Open Complaints** | Complaints silently drifting beyond the 30-day RBI threshold. | **Low** (3 days) | CRM Systems Team | Daily escalation digest to department heads for cases at Day 25. |
| **6** | **Product & Operational Bug Remediation** | Recurring account closure maintenance charges. | **Medium** (4 weeks) | Card & CASA Product Owners | Prevents the root issue driving high-relief complaints (31.8% relief rate). |

---

## 2. Where AI Genuinely Adds Value (Opportunity Mapping)

AI is only mapped to steps where rules cannot solve the complexity:

| As-Is Step | Operational Bottleneck | Proposed AI Capability | Form of AI Applied | Evidence & Justification |
| :--- | :--- | :--- | :--- | :--- |
| **Classify & Route** | Misrouting; tickets bouncing between teams. | **Intelligent Triage & Routing** | Small Language Model (`Claude Haiku 5.5`) | 36% of narrative tags cite routing friction; low-cost classification. |
| **Investigate Policy** | 12–15 min spent searching 4 disconnected portals. | **Policy Knowledge Q&A with Citations (RAG)** | Large Language Model (`Claude Sonnet 5.5`) | 51% of narrative tags need knowledge retrieval; reduces AHT by 4.0 min. |
| **Draft Reply** | Writing repetitive letters from blank screen. | **AI-Assisted Reply Drafting (HITL)** | Large Language Model (`Claude Sonnet 5.5`) | Generates structured draft with regulatory clauses for agent approval. |
| **Supervisor Escalation**| Supervisors read lengthy multi-week case logs. | **Case Summary Synthesis** | Large Language Model (`Claude Sonnet 5.5`) | Condensed 3-bullet history saves 5–7 min per supervisor escalation. |

---

## 3. The Lean Six Sigma Control Plan

To prevent backsliding and maintain performance gains:

| Tracked KPI | Metric Definition | Target | Review Frequency | Accountable Owner | Operational Response if Off-Target |
| :--- | :--- | :---: | :---: | :--- | :--- |
| **Resolution $\le$ 30 Days** | Closed complaints resolved within 30 days $\div$ Total closed | **$\ge 95.0\%$** | Weekly | Head of Operations | Daily review of Day-25 warning list by team leads. |
| **Acknowledgement $\le$ 1 Day** | Acknowledged in $\le 1$ working day $\div$ Total received | **$\ge 98.0\%$** | Daily | CRM Operations Lead | Audit auto-responder gateway logs and API availability. |
| **Complaint Reopen Rate** | Reopened within 30 days $\div$ Total closed | **$< 5.0\%$** | Monthly | Quality Assurance Lead | Sample 20 reopened cases weekly for root-cause quality audits. |
| **RBI Ombudsman Escalations**| Complaints escalating to Ombudsman $\div$ Total volume | **$\le 2.55\%$** | Monthly | Principal Nodal Officer | Mandatory root-cause investigation for every Ombudsman notice. |
| **AI Suggestion Override Rate** | AI drafts/classifications rejected by agents $\div$ Total runs | **$\le 15.0\%$** | Weekly | AI Product Owner | Flag for prompt/knowledge base drift review if $>15\%$ for 2 weeks. |

---

## 4. Phase A1 Quality Checklist

- [x] Problem statement and project charter formulated with baseline data.
- [x] SIPOC process diagram and Critical-to-Quality (CTQ) tree completed.
- [x] Python data pipeline executed (`a1_step1_load.py` and `a1_step2_clean_kpis.py`).
- [x] `baseline_kpis.csv`, `relief_by_issue.csv`, and Pareto chart (`pareto_issues.png`) generated.
- [x] 100 complaint narratives sampled and tagged (`root_cause` and `ai_could_help`).
- [x] Fishbone diagram and 5 Whys root-cause analysis completed.
- [x] As-Is swimlane process map documented with `[H]` / `[R]` / `[AI]` tags.
- [x] Catalog of 6 Non-AI operational quick wins formulated with named owners.
- [x] AI opportunity map and ongoing Lean Six Sigma Control Plan established.
