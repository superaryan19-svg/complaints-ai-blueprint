# A1 As-Is Process Map & Lean Waste Analysis
**Project**: Kestrel Bank Complaint Process Diagnostic | **Week**: 3  

---

## 1. As-Is Operational Swimlane Map

Every step is classified by execution mechanism:
* **[H]**: Manual Human Effort
* **[R]**: Automated Rule / Deterministic Workflow
* **[AI]**: AI Inference Call
* **[AG]**: Autonomous AI Agent (Unused in As-Is)

```mermaid
sequenceDiagram
    autonumber
    actor C as Customer
    participant CRM as Channels & CRM
    actor A as Complaint Agent
    actor S as Supervisor / QA
    actor T as Product / Back-Office Team

    C->>CRM: Submits complaint via App / Web / Branch [H]
    CRM->>CRM: Logs ticket; no SLA acknowledgement sent [H]
    CRM->>A: Unclassified queue assignment (often wrong team) [H]
    Note over A: Waste: Manual triage & re-routing (2-3 days lost)
    A->>T: Re-routes misassigned ticket [H]
    T->>A: Reassigns back to correct desk [H]
    Note over A: Waste: Searching 4 separate intranet systems (12-15 min)
    A->>A: Searches policy circulars across 4 systems [H]
    A->>A: Manually crafts reply letter from blank template [H]
    alt Refund exceeds discretionary limit
        A->>S: Submits escalation ticket for refund approval [H]
        Note over S: Waste: Waiting queue for supervisor review (4-6 days)
        S->>A: Approves or rejects refund [H]
    end
    A->>CRM: Enters resolution notes & closes case [H]
    CRM->>C: Dispatches resolution email / letter [H]
    Note over C,CRM: Waste: Case reopened if resolution is generic or unaddressed
```

---

## 2. As-Is Step Inventory & Tagging

| Step # | Process Step Description | Lane / Role | Tag | Duration (Est.) | Lean Waste Category |
| :---: | :--- | :--- | :---: | :---: | :--- |
| **1** | Customer files grievance through channel | Customer | **[H]** | 10–15 min | — |
| **2** | Ticket created without instant category validation | Channels / CRM | **[H]** | 0.5–1 day | **Waiting** (No auto-acknowledgement) |
| **3** | Initial manual sorting and routing | Intake Queue | **[H]** | 1–2 days | **Extra Hand-off / Rework** (Misrouting) |
| **4** | Misrouted ticket returned to central intake | Complaint Agent | **[H]** | 1 day | **Rework & Delay** |
| **5** | Agent reviews customer history and files | Complaint Agent | **[H]** | 5 min | **Data Re-entry / Context switching** |
| **6** | Agent searches four siloed portals for policy | Complaint Agent | **[H]** | **12–15 min** | **Motion / Searching for Information** |
| **7** | Agent drafts formal response from scratch | Complaint Agent | **[H]** | 8–10 min | **Overprocessing** |
| **8** | Supervisor approval queue for minor refunds | Supervisor / QA | **[H]** | 3–5 days | **Waiting / Bottleneck** |
| **9** | Final dispatch and manual closure update | Complaint Agent | **[H]** | 3 min | **Manual Processing** |

> **Summary Tag Count**: **11 Human [H] | 1 Rule [R] | 0 AI | 0 Autonomous Agents [AG]**  
> *Observation: In the As-Is process, 92% of operational steps rely entirely on manual human touchpoints, creating compounded waiting queues.*

---

## 3. Lean Waste (Muda) Audit

1. **Waiting (Lag Waste)**:
   * Tickets sit idle in queues during manual routing and supervisor approval hand-offs, burning 8–12 days of the 30-day statutory clock.
2. **Overprocessing (Drafting Waste)**:
   * Frontline agents rewrite standardized regulatory clauses from scratch for routine card and fee inquiries.
3. **Motion / Search (Knowledge Waste)**:
   * Searching across 4 disconnected intranet portals for applicable RBI circulars accounts for ~50% of active handling time (AHT).
4. **Defects & Rework (Misrouting Waste)**:
   * Approximately 1 in 5 complaints is routed to the wrong specialist desk initially, triggering re-assignment loops.
