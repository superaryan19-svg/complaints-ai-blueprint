# A1 Project Charter & Define Phase (Lean Six Sigma DMAIC)
**Client**: Kestrel Bank | **Engagement**: Complaint Process Diagnostic | **Week**: 1  

---

## 1. Problem Statement
> "Kestrel Bank handles approximately 40,000 complaints a month [AS-01]. An estimated 12% are not resolved within the 30-day statutory window after which customers may escalate to the Reserve Bank of India (RBI) Integrated Ombudsman [assumption], and roughly 3% are escalated [AS-04]. In the public banking stand-in data, 6 of 11 issue types account for over 80% of complaint volume, and 30.6% of complaints conclude with customer relief (monetary or non-monetary), indicating that a substantial share of grievances have merit and are avoidable. The objective of this diagnostic is to uncover operational root causes and prioritize high-impact fixes that require zero new technology before evaluating AI assistance."

---

## 2. Project Charter

| Charter Field | Operational Specification |
| :--- | :--- |
| **Problem Statement** | Stated above. Excessive resolution lag and avoidable escalations to the RBI Ombudsman. |
| **Business Case** | Under the **Reserve Bank – Integrated Ombudsman Scheme, 2026 (RB-IOS 2026)**, failure to resolve within 30 days triggers regulatory intervention and potential consequential loss awards up to ₹30 lakh. |
| **Goal Statement (SMART)**| Increase the 30-day complaint resolution rate from **88.0% to $\ge 95.0\%$** and decrease Ombudsman escalations from **3.0% to $\le 2.55\%$** within 12 months. |
| **In Scope** | Retail customer complaints across Credit Cards, Savings & Current Accounts, and Digital Banking; all intake channels (Web, Mobile App, Branch, Call Center). |
| **Out of Scope** | Core banking modernization, direct fraud loss investigations, collection recovery legal disputes. |
| **Key Stakeholders** | Head of Customer Service (Executive Sponsor), Principal Nodal Officer (Compliance Owner), Frontline Team Leads, IT Architecture Lead. |
| **Timeline** | 3 Weeks: **Define** (Wk 1) $\rightarrow$ **Measure & Analyse** (Wk 2) $\rightarrow$ **Improve & Control** (Wk 3). |

---

## 3. High-Level Process Map: SIPOC

```
Suppliers  ───►  Inputs  ───►  High-Level Process (7 Steps)  ───►  Outputs  ───►  Customers
```

| Element | Specification |
| :--- | :--- |
| **Suppliers** | Retail Customers, Branch Officers, Call Centre Agents, RBI CMS (Complaint Management System) Portal. |
| **Inputs** | Unstructured complaint narrative, submission channel, customer product/account ID, transaction records, internal policy circulars. |
| **Process Steps** | **1.** Receive and Log $\rightarrow$ **2.** Acknowledge Receipt $\rightarrow$ **3.** Classify & Route to Specialized Team $\rightarrow$ **4.** Investigate Records & Policy $\rightarrow$ **5.** Decide Outcome & Approval $\rightarrow$ **6.** Issue Reply & Close in CRM $\rightarrow$ **7.** Root-Cause Learning & MIS. |
| **Outputs** | Formal response communication (email/letter), account adjustment/monetary refund, CRM audit closure record, executive MIS reporting. |
| **Customers** | Aggrieved Customer, Principal Nodal Officer, Compliance & Legal, RBI Ombudsman Office. |

---

## 4. Voice of the Customer (VoC) to Critical-to-Quality (CTQ) Tree

```
Customer Need (VoC)           Quality Driver          CTQ Metric                         Target        Measurable in Data?
"Fix it quickly"          ──► Speed              ──► % resolved within 30 days           ≥ 95.0%       Proxy: Timely response flag
"Tell me you got it"      ──► Communication      ──► % acknowledged in 1 working day     ≥ 98.0%       Intake routing lag (days)
"Don't make me repeat"    ──► Operational Effort ──► First-Contact Resolution (FCR) %    ≥ 70.0%       Interview / Re-route log
"Give me a fair outcome"  ──► Fairness & Quality ──► Reopen rate (<5%) & Relief rate    Reopen <5%    Relief rate: Yes (30.6%)
```
