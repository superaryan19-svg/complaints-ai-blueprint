# Sourced References & Citations

**Checked**: 7 November 2026  
**Project**: Complaints AI Transformation Blueprint (Kestrel Bank)

---

### Regulatory & Industry Benchmark Sources
* **[1] Consumer Financial Protection Bureau (CFPB)**: *Consumer Complaint Database*.  
  [https://www.consumerfinance.gov/data-research/consumer-complaints/](https://www.consumerfinance.gov/data-research/consumer-complaints/)
* **[2] CFPB Newsroom**: *The CFPB to cease discretionary publication of complaint narratives and visualizations* (August 2026).  
  [https://www.consumerfinance.gov/about-us/newsroom/the-cfpb-to-cease-discretionary-publication-of-complaint-narratives-and-visualizations/](https://www.consumerfinance.gov/about-us/newsroom/the-cfpb-to-cease-discretionary-publication-of-complaint-narratives-and-visualizations/)
* **[3] CFPB FOIA Reading Room**: *CFPB Consumer Complaint Database Narratives Archive* (Dec 2011 – 14 Aug 2026).  
  [https://www.consumerfinance.gov/foia-requests/foia-electronic-reading-room/cfpb-consumer-complaint-database-narratives-archive/](https://www.consumerfinance.gov/foia-requests/foia-electronic-reading-room/cfpb-consumer-complaint-database-narratives-archive/)
* **[4] CFPB Field Reference**: *Field Reference Guide for the Complaint Database*.  
  [https://cfpb.github.io/api/ccdb/fields.html](https://cfpb.github.io/api/ccdb/fields.html)
* **[5] Reserve Bank of India**: *Reserve Bank – Integrated Ombudsman Scheme, 2026 (RB-IOS 2026)* (In force from 1 July 2026).  
  [https://website.rbi.org.in/documents/d/rbi/reserve-bank-integrated-ombudsman-scheme-2026-160126](https://website.rbi.org.in/documents/d/rbi/reserve-bank-integrated-ombudsman-scheme-2026-160126)
* **[6] IDFC FIRST Bank Regulatory Disclosure**: *Salient Features: The Reserve Bank – Integrated Ombudsman Scheme, 2026* (30-day resolution timeline, 90-day filing window, ₹30 lakh consequential loss compensation limit).
* **[7] Reserve Bank of India**: *Report of the Committee to Develop a Framework for Responsible and Ethical Enablement of Artificial Intelligence (FREE-AI) in the Financial Sector* (August 2025).  
  [https://website.rbi.org.in/ur/web/rbi/-/press-releases/report-of-the-committee-to-develop-a-framework-for-responsible-and-ethical-enablement-of-artificial-intelligence-free-ai-in-the-financial-sector](https://website.rbi.org.in/ur/web/rbi/-/press-releases/report-of-the-committee-to-develop-a-framework-for-responsible-and-ethical-enablement-of-artificial-intelligence-free-ai-in-the-financial-sector)
* **[8] Chambers & Partners / Legal Commentary**: *RBI Committee Report on Responsible AI in the Financial Sector (FREE-AI Framework)*.
* **[9] Ministry of Electronics and Information Technology (MeitY) / Legal Analysis**: *Digital Personal Data Protection (DPDP) Rules 2025 – Phased Rollout & Compliance Milestones* (Notified 13 November 2025; operational enforcement through May 2027).
* **[10] DPDP Rules 2025 Statutory Provisions**: *Section on Security Safeguards and 72-Hour Mandatory Data Breach Reporting to the Data Protection Board of India (DPBI)*.

### Vendor & Commercial Pricing Benchmarks
* **[11] Anthropic Model Pricing**: *Claude 3.5 / 5.5 Sonnet & Haiku Pricing Schedule* (as of November 2026):
  * **Claude Haiku 5.5**: \$0.10 / 1M input tokens, \$0.01 / 1M cached input, \$0.50 / 1M output tokens.
  * **Claude Sonnet 5.5**: \$2.00 / 1M input tokens, \$0.10 / 1M cached input, \$10.00 / 1M output tokens.  
  [https://platform.claude.com/docs/en/about-claude/pricing](https://platform.claude.com/docs/en/about-claude/pricing)
* **[12] Anthropic Engineering Docs**: *Prompt Caching Architecture & Write Multipliers (1.25x write premium; 90% read discount)*.  
  [https://platform.claude.com/docs/en/build-with-claude/prompt-caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
* **[13] Microsoft Fabric / Power BI Documentation**: *Publish to Web Licensing & Security Guidelines*.

---

### Data Caveats & Disclosures
1. **No Resolution Date in Stand-in Data**: The CFPB dataset tracks `Date received` and `Date sent to company` with a timely response flag, but does not capture the date the grievance was resolved. Handling time (25 min) and 30-day resolution rates (88%) are assumptions validated through operational interviews.
2. **US Dataset for Indian Client**: Stand-in data models the distribution of issues, linguistic narratives, and relief outcomes, not volume or cost.
3. **Redacted Public Records**: Customer narratives mask private sensitive data as `XXXX`.
