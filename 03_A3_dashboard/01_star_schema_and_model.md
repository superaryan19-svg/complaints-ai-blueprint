# A3 Power BI Data Model: Star Schema & Ingestion Guide
**Project**: Kestrel Bank AI Value Dashboard | **Module**: A3 Telemetry & Telemetry Architecture  
**Deliverable**: Star-Schema Architecture & Power Query Transformation Pipeline  

---

## 1. Dimensional Architecture (Star Schema)

```
        ┌──────────────────┐
        │     DimDate      │
        │──────────────────│
        │ Date (PK)        │
        │ Month            │
        │ Week Start       │
        └────────┬─────────┘
                 │ 1
                 │
                 │ *
┌────────────────┴──────────────┐         1 ┌──────────────────┐
│         FactAIEvents          ├───────────┤     DimTeam      │
│───────────────────────────────│           │──────────────────│
│ event_id (PK)                 │           │ team (PK)        │
│ date (FK)                     │           └──────────────────┘
│ team (FK)                     │
│ use_case (FK)                 │         1 ┌──────────────────┐
│ agent_id                      ├───────────┤    DimUseCase    │
│ input_tokens, output_tokens   │           │──────────────────│
│ cost_usd, minutes_saved       │           │ use_case (PK)    │
│ latency_ms, agent_outcome     │           └──────────────────┘
│ guardrail_flag, escalated     │
└───────────────────────────────┘
```

---

## 2. Power Query Data Transformation Steps

### Step 1: Ingest Fact Table
1. Open **Power BI Desktop** $\rightarrow$ **Get data** $\rightarrow$ **Text/CSV** $\rightarrow$ select `ai_event_log.csv` (located in root `PJ-1/` or `03_A3_dashboard/`).
2. Click **Transform Data**.
3. Rename query to `FactAIEvents`.
4. Ensure explicit data types:
   * `event_id`: Text
   * `timestamp`: Date/Time
   * `date`: Date
   * `agent_id`: Text
   * `team`: Text
   * `use_case`: Text
   * `model`: Text
   * `input_tokens`, `cached_tokens`, `output_tokens`: Whole Number (`Int64`)
   * `cost_usd`: Decimal Number (`Double`)
   * `latency_ms`: Whole Number (`Int64`)
   * `agent_outcome`: Text (`Accepted`, `Edited`, `Rejected`)
   * `minutes_saved`: Decimal Number (`Double`)
   * `guardrail_flag`: Text (`No flag`, `PII blocked`, `Low confidence`, `Off-policy`)
   * `escalated_to_human`: Text (`Yes`, `No`)

### Step 2: Ingest Targets Table
1. Select **New Source** $\rightarrow$ **Text/CSV** $\rightarrow$ `baseline_targets.csv`.
2. Rename query to `Targets`.
3. Set `metric` to Text, `baseline` and `target` to Decimal Number.

### Step 3: Create Conformed Dimensions
1. Right-click `FactAIEvents` in the Queries pane $\rightarrow$ click **Reference**.
2. Select only the `team` column $\rightarrow$ right-click $\rightarrow$ **Remove Other Columns**.
3. Click **Remove Rows** $\rightarrow$ **Remove Duplicates**.
4. Rename query to `DimTeam`.
5. Repeat for Use Case:
   * Right-click `FactAIEvents` $\rightarrow$ **Reference**.
   * Keep only `use_case` column $\rightarrow$ **Remove Duplicates**.
   * Rename query to `DimUseCase`.
6. Click **Close & Apply**.

---

## 3. Date Dimension DAX Definition

In Power BI Desktop, navigate to **Modeling** $\rightarrow$ **New Table** and paste:

```dax
DimDate = 
ADDCOLUMNS (
    CALENDAR ( DATE ( 2026, 1, 1 ), DATE ( 2026, 4, 30 ) ),
    "Month", FORMAT ( [Date], "YYYY-MM" ),
    "Week Start", [Date] - WEEKDAY ( [Date], 2 ) + 1 -- Monday of each week
)
```

> **Configuration**: Select `DimDate` $\rightarrow$ Table Tools $\rightarrow$ **Mark as date table** $\rightarrow$ select `Date` column.

---

## 4. Relationship Configuration

In the **Model View**, establish the following relationships:

| From Dimension (1 side) | To Fact Table (* side) | Cardinality | Cross Filter Direction |
| :--- | :--- | :---: | :---: |
| `DimDate[Date]` | `FactAIEvents[date]` | One-to-Many (`1:*`) | Single |
| `DimTeam[team]` | `FactAIEvents[team]` | One-to-Many (`1:*`) | Single |
| `DimUseCase[use_case]` | `FactAIEvents[use_case]` | One-to-Many (`1:*`) | Single |
| `Targets` | *(No relationship)* | Disconnected | — |

*Best Practice: Right-click `date`, `team`, and `use_case` columns inside `FactAIEvents` and select **Hide in Report View**. This prevents report builders from accidentally slicing by unindexed fact columns.*
