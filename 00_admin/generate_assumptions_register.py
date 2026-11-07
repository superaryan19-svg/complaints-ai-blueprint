import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Assumptions_Register"

# Ensure grid lines are visible
ws.views.sheetView[0].showGridLines = True

# Title block
ws["A1"] = "Kestrel Bank — AI Transformation Blueprint"
ws["A1"].font = Font(name="Calibri", size=14, bold=True, color="1F497D")
ws["A2"] = "Master Assumptions Register (Category A Techno-Consultant Deliverable)"
ws["A2"].font = Font(name="Calibri", size=10, italic=True, color="595959")

# Table headers
headers = ["ID", "Assumption Description", "Value", "Type", "Reason / Source / Citation", "Used In", "Confidence Level"]
ws.append([]) # row 3 blank
ws.append(headers) # row 4

header_fill = PatternFill(start_color="1F497D", end_color="1F497D", fill_type="solid")
header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")

thin_border = Border(
    left=Side(style='thin', color='D9D9D9'),
    right=Side(style='thin', color='D9D9D9'),
    top=Side(style='thin', color='D9D9D9'),
    bottom=Side(style='thin', color='D9D9D9')
)

for col_idx in range(1, len(headers) + 1):
    cell = ws.cell(row=4, column=col_idx)
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = Alignment(horizontal="center" if col_idx in [1, 4, 6, 7] else "left", vertical="center")

data = [
    ("AS-01", "Complaints per month", "40,000", "Assumed", "Mid-size bank scale; benchmarked against Indian private bank annual reports", "A2, A3", "Medium"),
    ("AS-02", "Average handle time today", "25 min", "Assumed", "To validate in operational interviews; CFPB data lacks handle time", "A2", "Low"),
    ("AS-03", "Loaded agent cost", "₹400 / hour", "Assumed", "Salary + overheads + facility and IT seat cost", "A2, A3", "Medium"),
    ("AS-04", "Escalation rate to Ombudsman", "3.0%", "Assumed", "Complaints escalating beyond 30 days to RBI Integrated Ombudsman", "A2", "Low"),
    ("AS-05", "Claude Sonnet 5.5 price", "$2 in / $10 out / 1M", "Sourced", "Anthropic pricing schedule, November 2026 [11]", "A2", "High"),
    ("AS-06", "Claude Haiku 5.5 price", "$0.10 in / $0.50 out / 1M", "Sourced", "Anthropic pricing schedule, November 2026 [11]", "A2", "High"),
    ("AS-07", "Target adoption (Base)", "80%", "Assumed", "Percentage of agents actively utilizing AI suggestions daily", "A2, A3", "Medium"),
    ("AS-08", "Acceptance rate (Base)", "85%", "Assumed", "Proportion of AI outputs accepted as-is or lightly edited", "A2, A3", "Medium"),
    ("AS-09", "Realisation factor (Base)", "50%", "Assumed", "Share of saved agent time converted into bottom-line financial gains", "A2, A3", "Medium"),
    ("AS-10", "Escalation reduction (Base)", "15%", "Assumed", "Decline in Ombudsman escalations due to improved turnaround & quality", "A2", "Low"),
    ("AS-11", "Cost per escalation", "₹5,000", "Assumed", "Administrative and investigation effort per Ombudsman filing", "A2", "Low"),
    ("AS-12", "INR per USD (FX)", "88.0", "Assumed", "Exchange rate applied for USD token pricing to INR conversions", "A2, A3", "High"),
    ("AS-13", "Discount rate", "12.0%", "Assumed", "Cost of capital / hurdle rate for bank IT investments", "A2", "High"),
    ("AS-14", "Prompt cache hit rate", "90%", "Assumed", "Cache efficiency on repeated system instructions & policy docs", "A2, A3", "High"),
    ("AS-15", "Prompt cache write multiplier", "1.25x", "Sourced", "Anthropic Prompt Caching documentation [12]", "A2", "High"),
    ("AS-16", "Pilot agent cohort", "120 agents", "Assumed", "30 agents across 4 teams: Cards, Savings, Digital, Branch Esc.", "A2, A3", "Medium"),
]

for row_idx, row_data in enumerate(data, start=5):
    ws.append(row_data)
    fill_color = "F9FAFB" if row_idx % 2 == 0 else "FFFFFF"
    row_fill = PatternFill(start_color=fill_color, end_color=fill_color, fill_type="solid")
    
    for col_idx in range(1, len(row_data) + 1):
        cell = ws.cell(row=row_idx, column=col_idx)
        cell.font = Font(name="Calibri", size=10)
        cell.fill = row_fill
        cell.border = thin_border
        cell.alignment = Alignment(
            horizontal="center" if col_idx in [1, 4, 6, 7] else "left",
            vertical="center"
        )
        # Highlight Type
        if col_idx == 4:
            if cell.value == "Sourced":
                cell.font = Font(name="Calibri", size=10, bold=True, color="006100")
            elif cell.value == "Assumed":
                cell.font = Font(name="Calibri", size=10, bold=True, color="9C6500")

# Adjust column widths
for col in ws.columns:
    max_len = max(len(str(cell.value or '')) for cell in col)
    col_letter = get_column_letter(col[0].column)
    ws.column_dimensions[col_letter].width = max(max_len + 4, 12)

ws.column_dimensions['A'].width = 10
ws.column_dimensions['B'].width = 30
ws.column_dimensions['C'].width = 18
ws.column_dimensions['D'].width = 14
ws.column_dimensions['E'].width = 50
ws.column_dimensions['F'].width = 12
ws.column_dimensions['G'].width = 18

wb.save("00_admin/assumptions_register.xlsx")
print("Saved 00_admin/assumptions_register.xlsx successfully!")
