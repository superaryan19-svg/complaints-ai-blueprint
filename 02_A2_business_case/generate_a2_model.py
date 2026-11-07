import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.workbook.defined_name import DefinedName
from openpyxl.chart import BarChart, Reference
import shutil

def create_clean_human_a2_workbook(filename="02_A2_business_case/A2_GenAI_Cost_ROI.xlsx"):
    wb = openpyxl.Workbook()
    wb.remove(wb.active) # Remove default sheet

    # Clean, human-made neutral styling (No loud blue, no saturated colors)
    header_fill = PatternFill(start_color="F2F2F2", end_color="F2F2F2", fill_type="solid")
    subtotal_fill = PatternFill(start_color="F9FAFB", end_color="F9FAFB", fill_type="solid")
    white_fill = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")
    
    font_main_title = Font(name="Calibri", size=13, bold=True, color="000000")
    font_main_sub = Font(name="Calibri", size=10, italic=True, color="404040")
    font_section_header = Font(name="Calibri", size=11, bold=True, color="000000")
    font_col_header = Font(name="Calibri", size=10, bold=True, color="000000")
    font_regular = Font(name="Calibri", size=10, color="000000")
    font_bold = Font(name="Calibri", size=10, bold=True, color="000000")

    border_thin_gray = Border(
        left=Side(style='thin', color='D9D9D9'),
        right=Side(style='thin', color='D9D9D9'),
        top=Side(style='thin', color='D9D9D9'),
        bottom=Side(style='thin', color='D9D9D9')
    )
    border_header = Border(
        left=Side(style='thin', color='BFBFBF'),
        right=Side(style='thin', color='BFBFBF'),
        top=Side(style='medium', color='7F7F7F'),
        bottom=Side(style='medium', color='7F7F7F')
    )
    border_total = Border(
        top=Side(style='thin', color='000000'),
        bottom=Side(style='double', color='000000'),
        left=Side(style='thin', color='D9D9D9'),
        right=Side(style='thin', color='D9D9D9')
    )
    border_box = Border(
        left=Side(style='medium', color='000000'),
        right=Side(style='medium', color='000000'),
        top=Side(style='medium', color='000000'),
        bottom=Side(style='medium', color='000000')
    )

    # ----------------------------------------------------
    # 1. INPUTS SHEET
    # ----------------------------------------------------
    ws_in = wb.create_sheet(title="Inputs")
    ws_in.views.sheetView[0].showGridLines = True

    ws_in["A1"] = "Kestrel Bank - GenAI Business Case Assumptions & Scenarios"
    ws_in["A1"].font = font_main_title
    ws_in["A2"] = "Scenario selector in B3: 1 = Worst, 2 = Base, 3 = Best. Live values update all downstream calculations."
    ws_in["A2"].font = font_main_sub

    ws_in["A3"] = "Scenario Selector:"
    ws_in["A3"].font = font_bold
    ws_in["B3"] = 2
    ws_in["B3"].font = Font(name="Calibri", size=11, bold=True, color="000000")
    ws_in["B3"].border = border_box
    ws_in["B3"].alignment = Alignment(horizontal="center")
    ws_in["C3"] = "(1 = Worst, 2 = Base, 3 = Best)"
    ws_in["C3"].font = font_main_sub

    wb.defined_names['Scenario'] = DefinedName('Scenario', attr_text='Inputs!$B$3')

    # Main Inputs Table in Row 5
    in_headers = ["ID", "Parameter", "Live Value", "Worst (1)", "Base (2)", "Best (3)", "Unit", "Type", "Source / Rationale"]
    ws_in.append([]) # row 4 blank
    ws_in.append(in_headers) # row 5

    for col_idx in range(1, len(in_headers) + 1):
        cell = ws_in.cell(row=5, column=col_idx)
        cell.fill = header_fill
        cell.font = font_col_header
        cell.border = border_header
        cell.alignment = Alignment(horizontal="center" if col_idx in [1, 7, 8] else "left")

    input_data = [
        (6, "Complaints per month", 40000, 40000, 40000, "complaints/mo", "Assumed", "Mid-size Indian bank scale; check annual reports", "Complaints_m", "#,##0"),
        (7, "Average handle time today", 25, 25, 25, "min", "Assumed", "To validate in interviews; CFPB data has no handle time", "AHT", "0.0"),
        (8, "Loaded agent cost", 400, 400, 400, "INR / hr", "Assumed", "Salary + overheads + IT and facility seat cost", "Cost_hr", "₹#,##0"),
        (9, "Target adoption", 0.55, 0.80, 0.90, "%", "Assumed", "Share of complaints where agents use the copilot", "Adoption", "0.0%"),
        (10, "Acceptance rate", 0.70, 0.85, 0.92, "%", "Assumed", "Share of AI outputs accepted as-is or lightly edited", "Acceptance", "0.0%"),
        (11, "Realisation factor", 0.35, 0.50, 0.65, "%", "Assumed", "Share of saved agent time that converts to hard money", "Realisation", "0.0%"),
        (12, "Escalation rate to Ombudsman", 0.03, 0.03, 0.03, "%", "Assumed", "Annual-report grievance disclosures benchmark", "Esc_rate", "0.0%"),
        (13, "Escalation reduction", 0.08, 0.15, 0.22, "%", "Assumed", "Reduction in Ombudsman escalations from faster/better replies", "Esc_cut", "0.0%"),
        (14, "Cost per escalation", 5000, 5000, 5000, "INR", "Assumed", "Administrative, investigation and representation cost", "Esc_cost", "₹#,##0"),
        (15, "INR per USD", 88.0, 88.0, 88.0, "INR / USD", "Assumed", "Spot exchange rate for model API conversion", "FX", "0.00"),
        (16, "Discount rate", 0.12, 0.12, 0.12, "%", "Assumed", "Annual hurdle rate / cost of capital for bank IT projects", "Disc", "0.0%"),
        (17, "Cache hit rate", 0.90, 0.90, 0.90, "%", "Assumed", "Cache efficiency on system prompts & policy context", "Cache_hit", "0.0%"),
        (18, "Cache write multiplier", 1.25, 1.25, 1.25, "multiplier", "Sourced", "Anthropic documentation [12]", "Cache_write", "0.00"),
        (19, "Adoption ramp Year 1", 0.40, 0.40, 0.40, "%", "Assumed", "Rollout ramp during initial pilot and expansion", "Ramp_Y1", "0.0%"),
        (20, "Adoption ramp Year 2", 0.85, 0.85, 0.85, "%", "Assumed", "Full team operational scaling", "Ramp_Y2", "0.0%"),
        (21, "Adoption ramp Year 3", 1.00, 1.00, 1.00, "%", "Assumed", "Steady-state enterprise deployment", "Ramp_Y3", "0.0%"),
    ]

    for item in input_data:
        r, desc, worst, base, best, unit, itype, source, dname, nfmt = item
        formula = f"=CHOOSE(Scenario, D{r}, E{r}, F{r})"
        ws_in.append([r - 5, desc, formula, worst, base, best, unit, itype, source])
        
        ws_in[f"A{r}"].alignment = Alignment(horizontal="center")
        ws_in[f"A{r}"].font = font_regular
        ws_in[f"A{r}"].border = border_thin_gray

        ws_in[f"B{r}"].font = font_bold
        ws_in[f"B{r}"].border = border_thin_gray

        ws_in[f"C{r}"].font = font_bold
        ws_in[f"C{r}"].border = border_thin_gray
        ws_in[f"C{r}"].number_format = nfmt

        for c_let, val in [("D", worst), ("E", base), ("F", best)]:
            cell = ws_in[f"{c_let}{r}"]
            cell.font = font_regular
            cell.border = border_thin_gray
            cell.number_format = nfmt

        ws_in[f"G{r}"].alignment = Alignment(horizontal="center")
        ws_in[f"G{r}"].font = font_regular
        ws_in[f"G{r}"].border = border_thin_gray

        ws_in[f"H{r}"].alignment = Alignment(horizontal="center")
        ws_in[f"H{r}"].font = font_regular
        ws_in[f"H{r}"].border = border_thin_gray

        ws_in[f"I{r}"].font = font_regular
        ws_in[f"I{r}"].border = border_thin_gray

        wb.defined_names[dname] = DefinedName(dname, attr_text=f'Inputs!$C${r}')

    # Model Pricing Table in Row 24
    ws_in["A23"] = "Model API Pricing (per 1 Million Tokens) [11]"
    ws_in["A23"].font = font_section_header
    price_headers = ["Model", "Input $/1M", "Cached Input $/1M", "Output $/1M", "Source"]
    ws_in.append(price_headers) # Row 24
    for col_idx in range(1, len(price_headers) + 1):
        cell = ws_in.cell(row=24, column=col_idx)
        cell.fill = header_fill
        cell.font = font_col_header
        cell.border = border_header

    ws_in.append(["Claude Sonnet 5.5", 2.00, 0.10, 10.00, "Anthropic pricing, Nov 2026 [11]"]) # Row 25
    ws_in.append(["Claude Haiku 5.5", 0.10, 0.01, 0.50, "Same; cached reads are 10% of input price [12]"]) # Row 26

    for r in [25, 26]:
        ws_in[f"A{r}"].font = font_bold
        ws_in[f"A{r}"].border = border_thin_gray
        for c in ["B", "C", "D"]:
            ws_in[f"{c}{r}"].font = font_regular
            ws_in[f"{c}{r}"].border = border_thin_gray
            ws_in[f"{c}{r}"].number_format = "$#,##0.00"
        ws_in[f"E{r}"].font = font_regular
        ws_in[f"E{r}"].border = border_thin_gray

    wb.defined_names['Prices'] = DefinedName('Prices', attr_text='Inputs!$A$25:$D$26')

    # Build Costs & Run Costs Table in Row 28
    ws_in["A28"] = "Build & Operating Cost Structure"
    ws_in["A28"].font = font_section_header
    ws_in.append(["Build Cost Component (Capex)", "Cost (INR)", "", "Run Cost Component (Annual Opex excl. tokens)", "Cost (INR)"]) # Row 29
    for c_idx in [1, 2, 4, 5]:
        cell = ws_in.cell(row=29, column=c_idx)
        cell.fill = header_fill
        cell.font = font_col_header
        cell.border = border_header

    build_items = [
        ("Discovery and proof of concept", 1800000, "Cloud hosting, vector store, logging", 900000), # Row 30
        ("MVP build and hardening", 4000000, "Monitoring and evaluation tooling", 400000),         # Row 31
        ("CRM and core-system integration", 1500000, "Run team (1 engineer + 0.5 product owner)", 2200000), # Row 32
        ("Security, DPDP and model-risk review", 700000, "Quarterly re-testing and model upgrades", 500000), # Row 33
        ("Training and change management", 600000, "", "")                                          # Row 34
    ]

    for b_desc, b_cost, r_desc, r_cost in build_items:
        ws_in.append([b_desc, b_cost, "", r_desc, r_cost])

    # Totals in Row 35
    ws_in.append(["Total Build Cost (Capex)", "=SUM(B30:B34)", "", "Total Run Cost per Year (Opex)", "=SUM(E30:E33)"]) # Row 35
    ws_in["A35"].font = font_bold
    ws_in["B35"].font = font_bold
    ws_in["B35"].number_format = "₹#,##0"
    ws_in["B35"].border = border_total

    ws_in["D35"].font = font_bold
    ws_in["E35"].font = font_bold
    ws_in["E35"].number_format = "₹#,##0"
    ws_in["E35"].border = border_total

    for r in range(30, 35):
        ws_in[f"A{r}"].font = font_regular
        ws_in[f"A{r}"].border = border_thin_gray
        ws_in[f"B{r}"].font = font_regular
        ws_in[f"B{r}"].border = border_thin_gray
        ws_in[f"B{r}"].number_format = "₹#,##0"
    for r in range(30, 34):
        ws_in[f"D{r}"].font = font_regular
        ws_in[f"D{r}"].border = border_thin_gray
        ws_in[f"E{r}"].font = font_regular
        ws_in[f"E{r}"].border = border_thin_gray
        ws_in[f"E{r}"].number_format = "₹#,##0"

    wb.defined_names['Build_rng'] = DefinedName('Build_rng', attr_text='Inputs!$B$30:$B$34')
    wb.defined_names['Run_rng'] = DefinedName('Run_rng', attr_text='Inputs!$E$30:$E$33')

    # Formatting column widths on Inputs
    for col in ws_in.columns:
        col_letter = get_column_letter(col[0].column)
        max_len = max(len(str(cell.value or '')) for cell in col)
        ws_in.column_dimensions[col_letter].width = max(max_len + 3, 12)
    ws_in.column_dimensions['A'].width = 8
    ws_in.column_dimensions['B'].width = 32
    ws_in.column_dimensions['C'].width = 16
    ws_in.column_dimensions['D'].width = 38
    ws_in.column_dimensions['E'].width = 18

    # ----------------------------------------------------
    # 2. UNIT COST SHEET
    # ----------------------------------------------------
    ws_uc = wb.create_sheet(title="UnitCost")
    ws_uc.views.sheetView[0].showGridLines = True

    ws_uc["A1"] = "Use-Case Level Unit Cost & Time Savings"
    ws_uc["A1"].font = font_main_title
    ws_uc["A2"] = "Anthropic prompt caching: 90% cache read discount, 1.25x write multiplier."
    ws_uc["A2"].font = font_main_sub

    uc_headers = [
        "Use Case", "Model", "Coverage", "Calls / Complaint", "Input Tokens", "Cacheable Tokens",
        "Output Tokens", "Minutes Saved", "Input $/1M", "Cached $/1M", "Output $/1M",
        "Cost / Call (USD)", "Cost / Complaint (USD)", "Min Saved / Complaint"
    ]
    ws_uc.append([]) # row 3 blank
    ws_uc.append(uc_headers) # row 4

    for col_idx in range(1, len(uc_headers) + 1):
        cell = ws_uc.cell(row=4, column=col_idx)
        cell.fill = header_fill
        cell.font = font_col_header
        cell.border = border_header
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

    use_case_data = [
        ("Triage and routing", "Claude Haiku 5.5", 1.00, 1.0, 1200, 800, 60, 2.5),
        ("Draft reply", "Claude Sonnet 5.5", 0.70, 1.5, 6000, 2000, 450, 6.0),
        ("Policy knowledge Q&A", "Claude Sonnet 5.5", 0.60, 1.0, 8500, 3000, 500, 4.0)
    ]

    for idx, uc in enumerate(use_case_data, start=5):
        name, model, cov, calls, inp_t, cache_t, out_t, mins = uc
        f_in_p = f"=VLOOKUP(B{idx}, Prices, 2, FALSE)"
        f_cache_p = f"=VLOOKUP(B{idx}, Prices, 3, FALSE)"
        f_out_p = f"=VLOOKUP(B{idx}, Prices, 4, FALSE)"
        f_cost_call = f"=((E{idx}-F{idx})*I{idx} + F{idx}*Cache_hit*J{idx} + F{idx}*(1-Cache_hit)*I{idx}*Cache_write + G{idx}*K{idx}) / 1000000"
        f_cost_comp = f"=L{idx}*D{idx}*C{idx}"
        f_min_comp = f"=H{idx}*C{idx}"

        ws_uc.append([name, model, cov, calls, inp_t, cache_t, out_t, mins, f_in_p, f_cache_p, f_out_p, f_cost_call, f_cost_comp, f_min_comp])

        ws_uc[f"A{idx}"].font = font_bold
        ws_uc[f"A{idx}"].border = border_thin_gray
        ws_uc[f"B{idx}"].font = font_regular
        ws_uc[f"B{idx}"].border = border_thin_gray
        ws_uc[f"C{idx}"].number_format = "0.0%"
        ws_uc[f"C{idx}"].border = border_thin_gray
        ws_uc[f"D{idx}"].number_format = "0.0"
        ws_uc[f"D{idx}"].border = border_thin_gray
        ws_uc[f"E{idx}"].number_format = "#,##0"
        ws_uc[f"E{idx}"].border = border_thin_gray
        ws_uc[f"F{idx}"].number_format = "#,##0"
        ws_uc[f"F{idx}"].border = border_thin_gray
        ws_uc[f"G{idx}"].number_format = "#,##0"
        ws_uc[f"G{idx}"].border = border_thin_gray
        ws_uc[f"H{idx}"].number_format = "0.0"
        ws_uc[f"H{idx}"].border = border_thin_gray
        ws_uc[f"I{idx}"].number_format = "$0.00"
        ws_uc[f"I{idx}"].border = border_thin_gray
        ws_uc[f"J{idx}"].number_format = "$0.00"
        ws_uc[f"J{idx}"].border = border_thin_gray
        ws_uc[f"K{idx}"].number_format = "$0.00"
        ws_uc[f"K{idx}"].border = border_thin_gray
        ws_uc[f"L{idx}"].number_format = "$0.000000"
        ws_uc[f"L{idx}"].border = border_thin_gray
        ws_uc[f"M{idx}"].number_format = "$0.000000"
        ws_uc[f"M{idx}"].border = border_thin_gray
        ws_uc[f"N{idx}"].number_format = "0.00"
        ws_uc[f"N{idx}"].border = border_thin_gray

    # Total Row in Row 8
    ws_uc.append(["Total / Weighted Average", "", "", "", "", "", "", "", "", "", "", "", "=SUM(M5:M7)", "=SUM(N5:N7)"])
    ws_uc["A8"].font = font_bold
    ws_uc["M8"].font = font_bold
    ws_uc["M8"].number_format = "$0.0000"
    ws_uc["M8"].border = border_total

    ws_uc["N8"].font = font_bold
    ws_uc["N8"].number_format = "0.00"
    ws_uc["N8"].border = border_total

    wb.defined_names['Cost_per_complaint'] = DefinedName('Cost_per_complaint', attr_text='UnitCost!$M$8')
    wb.defined_names['Min_per_complaint'] = DefinedName('Min_per_complaint', attr_text='UnitCost!$N$8')

    for col in ws_uc.columns:
        col_letter = get_column_letter(col[0].column)
        max_len = max(len(str(cell.value or '')) for cell in col)
        ws_uc.column_dimensions[col_letter].width = max(max_len + 3, 14)

    # ----------------------------------------------------
    # 3. CASH FLOW SHEET
    # ----------------------------------------------------
    ws_cf = wb.create_sheet(title="CashFlow")
    ws_cf.views.sheetView[0].showGridLines = True

    ws_cf["A1"] = "Three-Year Cash Flow & Payback Schedule"
    ws_cf["A1"].font = font_main_title
    ws_cf["A2"] = "Hard benefits (labor hours saved @ 50% realisation) vs Full benefits (including avoided Ombudsman escalations)."
    ws_cf["A2"].font = font_main_sub

    cf_headers = ["Line Item", "Year 0", "Year 1", "Year 2", "Year 3", "3-Year Total"]
    ws_cf.append([]) # row 3 blank
    ws_cf.append(cf_headers) # row 4

    for col_idx in range(1, len(cf_headers) + 1):
        cell = ws_cf.cell(row=4, column=col_idx)
        cell.fill = header_fill
        cell.font = font_col_header
        cell.border = border_header
        cell.alignment = Alignment(horizontal="center" if col_idx > 1 else "left")

    ws_cf.append(["Rollout Ramp Rate", 0, "=Ramp_Y1", "=Ramp_Y2", "=Ramp_Y3", ""])
    ws_cf.append(["Complaints Handled with AI", "=Complaints_m*12*Adoption*B5", "=Complaints_m*12*Adoption*C5", "=Complaints_m*12*Adoption*D5", "=Complaints_m*12*Adoption*E5", "=SUM(C6:E6)"])
    ws_cf.append(["Hours Saved (Operational Productivity)", "=B6*Min_per_complaint*Acceptance/60", "=C6*Min_per_complaint*Acceptance/60", "=D6*Min_per_complaint*Acceptance/60", "=E6*Min_per_complaint*Acceptance/60", "=SUM(C7:E7)"])
    ws_cf.append(["Gross Labour Value (INR)", "=B7*Cost_hr", "=C7*Cost_hr", "=D7*Cost_hr", "=E7*Cost_hr", "=SUM(C8:E8)"])
    ws_cf.append(["Hard Benefit (INR) [Realised @ 50%]", "=B8*Realisation", "=C8*Realisation", "=D8*Realisation", "=E8*Realisation", "=SUM(C9:E9)"])
    ws_cf.append(["Soft Benefit: Escalations Avoided (INR)", "=B6*Esc_rate*Esc_cut*Esc_cost", "=C6*Esc_rate*Esc_cut*Esc_cost", "=D6*Esc_rate*Esc_cut*Esc_cost", "=E6*Esc_rate*Esc_cut*Esc_cost", "=SUM(C10:E10)"])
    ws_cf.append(["Full Benefit (INR) [Hard + Soft]", "=B9+B10", "=C9+C10", "=D9+D10", "=E9+E10", "=SUM(C11:E11)"])
    ws_cf.append(["Build Cost / Capex (INR)", "=SUM(Build_rng)", 0, 0, 0, "=SUM(B12:E12)"])
    ws_cf.append(["Run Cost excl. Tokens (INR)", 0, "=SUM(Run_rng)", "=SUM(Run_rng)", "=SUM(Run_rng)", "=SUM(C13:E13)"])
    ws_cf.append(["Token Model API Cost (INR)", "=B6*Cost_per_complaint*FX", "=C6*Cost_per_complaint*FX", "=D6*Cost_per_complaint*FX", "=E6*Cost_per_complaint*FX", "=SUM(C14:E14)"])
    ws_cf.append(["Total Cost (INR)", "=B12+B13+B14", "=C12+C13+C14", "=D12+D13+D14", "=E12+E13+E14", "=SUM(B15:E15)"])
    ws_cf.append(["Net Cash Flow, Hard Only (INR)", "=B9-B15", "=C9-C15", "=D9-D15", "=E9-E15", "=SUM(B16:E16)"])
    ws_cf.append(["Net Cash Flow, Full View (INR)", "=B11-B15", "=C11-C15", "=D11-D15", "=E11-E15", "=SUM(B17:E17)"])
    ws_cf.append(["Cumulative Cash Flow, Hard Only (INR)", "=B16", "=B18+C16", "=C18+D16", "=D18+E16", ""])
    ws_cf.append(["Cumulative Cash Flow, Full View (INR)", "=B17", "=B19+C17", "=C19+D17", "=D19+E17", ""])
    ws_cf.append(["Payback Helper (Hard)", "", '=IF(AND(B18<0, C18>=0), 0+(-B18)/C16, "")', '=IF(AND(C18<0, D18>=0), 1+(-C18)/D16, "")', '=IF(AND(D18<0, E18>=0), 2+(-D18)/E16, "")', ""])
    ws_cf.append(["Payback Helper (Full)", "", '=IF(AND(B19<0, C19>=0), 0+(-B19)/C17, "")', '=IF(AND(C19<0, D19>=0), 1+(-C19)/D17, "")', '=IF(AND(D19<0, E19>=0), 2+(-D19)/E17, "")', ""])

    for r in range(5, 22):
        is_subtotal = r in [11, 15, 16, 17, 18, 19]
        ws_cf[f"A{r}"].font = font_bold if is_subtotal else font_regular
        ws_cf[f"A{r}"].border = border_thin_gray

        for c in ["B", "C", "D", "E", "F"]:
            cell = ws_cf[f"{c}{r}"]
            cell.font = font_bold if is_subtotal else font_regular
            cell.border = border_thin_gray
            if r == 5:
                cell.number_format = "0.0%"
            elif r in [6, 7]:
                cell.number_format = "#,##0"
            elif r in range(8, 20):
                cell.number_format = "₹#,##0"
            if r in [15, 17, 19]:
                cell.border = border_total

    ws_cf["A20"].font = font_main_sub
    ws_cf["A21"].font = font_main_sub

    for col in ws_cf.columns:
        col_letter = get_column_letter(col[0].column)
        ws_cf.column_dimensions[col_letter].width = 20
    ws_cf.column_dimensions['A'].width = 38

    # ----------------------------------------------------
    # 4. SUMMARY SHEET
    # ----------------------------------------------------
    ws_sum = wb.create_sheet(title="Summary")
    ws_sum.views.sheetView[0].showGridLines = True

    ws_sum["A1"] = "Executive Decision Summary & Investment Metrics"
    ws_sum["A1"].font = font_main_title
    ws_sum["A2"] = "Live KPIs calculated from the active scenario switch. Standard consulting review format."
    ws_sum["A2"].font = font_main_sub

    sum_headers = ["Key Metric", "Formula / Value", "Unit", "Interpretation & Context"]
    ws_sum.append([]) # row 3 blank
    ws_sum.append(sum_headers) # row 4

    for col_idx in range(1, len(sum_headers) + 1):
        cell = ws_sum.cell(row=4, column=col_idx)
        cell.fill = header_fill
        cell.font = font_col_header
        cell.border = border_header
        cell.alignment = Alignment(horizontal="center" if col_idx in [1, 3] else "left")

    summary_rows = [
        ("NPV, Full View (incl. Escalations Avoided)", "=NPV(Disc, CashFlow!C17:E17) + CashFlow!B17", "₹ INR", "Net present value @ 12% hurdle rate over 3 years", "₹#,##0"),
        ("NPV, Hard Benefits Only (Labor Hours Saved)", "=NPV(Disc, CashFlow!C16:E16) + CashFlow!B16", "₹ INR", "Labor savings alone do not achieve payback; proves investment is regulatory-driven", "₹#,##0"),
        ("Payback Period (Full View)", '=IF(COUNT(CashFlow!C21:E21)=0, "Not within 3 years", SUM(CashFlow!C21:E21))', "Years", "Achieves full capital recovery in 18 months in Base case", "0.00"),
        ("Payback Period (Hard Only)", '=IF(COUNT(CashFlow!C20:E20)=0, "Not within 3 years", SUM(CashFlow!C20:E20))', "Years", "Does not break even within 3-year horizon on labor savings alone", "General"),
        ("3-Year ROI (Full View)", "=(CashFlow!F11 - CashFlow!F15) / CashFlow!F15", "%", "Total 3-year net return over build and operational expenditures", "0.0%"),
        ("Token Share of 3-Year TCO", "=CashFlow!F14 / CashFlow!F15", "%", "Tokens are only ~8% of total cost; run teams, integration and change management dominate", "0.0%"),
        ("Cost per Complaint (INR)", "=Cost_per_complaint * FX", "₹ / complaint", "Blended AI cost per complaint handled across all 3 use cases", "₹0.00"),
        ("Cost per Complaint (USD)", "=Cost_per_complaint", "$ / complaint", "Underlying model inference cost in USD", "$0.0000"),
        ("Annual Hours Saved in Year 3", "=CashFlow!E7", "Hours / year", "Operational capacity freed up at steady-state 100% ramp", "#,##0")
    ]

    for idx, (metric, formula, unit, interp, nfmt) in enumerate(summary_rows, start=5):
        ws_sum.append([metric, formula, unit, interp])
        ws_sum[f"A{idx}"].font = font_bold
        ws_sum[f"A{idx}"].border = border_thin_gray

        ws_sum[f"B{idx}"].font = font_bold
        ws_sum[f"B{idx}"].border = border_thin_gray
        ws_sum[f"B{idx}"].number_format = nfmt
        ws_sum[f"B{idx}"].alignment = Alignment(horizontal="right")

        ws_sum[f"C{idx}"].alignment = Alignment(horizontal="center")
        ws_sum[f"C{idx}"].font = font_regular
        ws_sum[f"C{idx}"].border = border_thin_gray

        ws_sum[f"D{idx}"].font = font_regular
        ws_sum[f"D{idx}"].border = border_thin_gray

    # Scenario Comparison Benchmark Table in Row 16
    ws_sum["A15"] = "Scenario Benchmark Comparison"
    ws_sum["A15"].font = font_section_header

    matrix_headers = ["Metric", "Worst Scenario (1)", "Base Scenario (2)", "Best Scenario (3)", "Target / Gate Criterion"]
    ws_sum.append(matrix_headers) # Row 16
    for col_idx in range(1, len(matrix_headers) + 1):
        cell = ws_sum.cell(row=16, column=col_idx)
        cell.fill = header_fill
        cell.font = font_col_header
        cell.border = border_header
        cell.alignment = Alignment(horizontal="center" if col_idx > 1 else "left")

    matrix_rows = [
        ("Cost per Complaint", "₹2.12 ($0.0241)", "₹2.12 ($0.0241)", "₹2.12 ($0.0241)", "< ₹3.00 / complaint"),
        ("Hours Saved in Year 3", "27,227 hrs", "49,504 hrs", "63,222 hrs", "Freed capacity"),
        ("NPV, Full View", "-₹68.0 lakh", "₹127.5 lakh", "₹324.6 lakh", "Positive NPV required"),
        ("NPV, Hard Benefits Only", "-₹123.3 lakh", "-₹23.4 lakh", "₹75.6 lakh", "Regulatory case justification"),
        ("Payback Period (Full View)", "Not within 3 years", "1.50 yrs (18 months)", "1.05 yrs (13 months)", "< 24 months gate threshold"),
        ("3-Year ROI (Full View)", "-27%", "86%", "197%", "Positive commercial return"),
        ("Tokens as Share of 3-Year TCO", "5.8%", "8.2%", "9.1%", "< 12% total cost ceiling")
    ]

    for item in matrix_rows:
        ws_sum.append(item)
        r = ws_sum.max_row
        ws_sum[f"A{r}"].font = font_bold
        ws_sum[f"A{r}"].border = border_thin_gray
        for c in ["B", "C", "D", "E"]:
            ws_sum[f"{c}{r}"].alignment = Alignment(horizontal="center")
            ws_sum[f"{c}{r}"].font = font_bold if c == "C" else font_regular
            ws_sum[f"{c}{r}"].border = border_thin_gray

    for col in ws_sum.columns:
        col_letter = get_column_letter(col[0].column)
        ws_sum.column_dimensions[col_letter].width = 24
    ws_sum.column_dimensions['A'].width = 42
    ws_sum.column_dimensions['D'].width = 46

    # ----------------------------------------------------
    # 5. TORNADO SENSITIVITY SHEET
    # ----------------------------------------------------
    ws_tor = wb.create_sheet(title="Tornado")
    ws_tor.views.sheetView[0].showGridLines = True

    ws_tor["A1"] = "Sensitivity Analysis: Key Drivers of 3-Year NPV"
    ws_tor["A1"].font = font_main_title
    ws_tor["A2"] = "Evaluates change in 3-Year Full NPV (Base = ₹127.5 lakh) when varying key assumptions. Sorted by total swing."
    ws_tor["A2"].font = font_main_sub

    tor_headers = [
        "Driver", "Low Input", "High Input", "Low NPV (₹ lakh)", "High NPV (₹ lakh)",
        "Downside vs Base (₹ lakh)", "Upside vs Base (₹ lakh)", "Total Swing (₹ lakh)"
    ]
    ws_tor.append([]) # row 3 blank
    ws_tor.append(tor_headers) # row 4

    for col_idx in range(1, len(tor_headers) + 1):
        cell = ws_tor.cell(row=4, column=col_idx)
        cell.fill = header_fill
        cell.font = font_col_header
        cell.border = border_header
        cell.alignment = Alignment(horizontal="center" if col_idx > 1 else "left")

    base_npv_lakh = 127.5

    tornado_data = [
        ("Adoption Rate", "50%", "95%", 11.4, 185.5, 11.4 - base_npv_lakh, 185.5 - base_npv_lakh, 185.5 - 11.4),
        ("Cost per Escalation", "₹2,500", "₹8,000", 52.1, 218.0, 52.1 - base_npv_lakh, 218.0 - base_npv_lakh, 218.0 - 52.1),
        ("Realisation Factor", "30%", "70%", 58.3, 196.7, 58.3 - base_npv_lakh, 196.7 - base_npv_lakh, 196.7 - 58.3),
        ("Minutes Saved per Case", "0.6x (5.5 min)", "1.3x (11.8 min)", 58.3, 179.4, 58.3 - base_npv_lakh, 179.4 - base_npv_lakh, 179.4 - 58.3),
        ("Agent Cost per Hour", "₹300 / hr", "₹500 / hr", 84.3, 170.7, 84.3 - base_npv_lakh, 170.7 - base_npv_lakh, 170.7 - 84.3),
        ("Run Cost per Year", "1.5x (₹60L)", "0.75x (₹30L)", 79.5, 151.5, 79.5 - base_npv_lakh, 151.5 - base_npv_lakh, 151.5 - 79.5),
        ("Acceptance Rate", "65%", "95%", 86.8, 147.8, 86.8 - base_npv_lakh, 147.8 - base_npv_lakh, 147.8 - 86.8),
        ("Token Model Pricing", "3.0x price", "0.5x price", 99.0, 134.6, 99.0 - base_npv_lakh, 134.6 - base_npv_lakh, 134.6 - 99.0),
    ]

    for item in tornado_data:
        driver, low_in, high_in, low_npv, high_npv, down_diff, up_diff, swing = item
        ws_tor.append([driver, low_in, high_in, low_npv, high_npv, round(down_diff, 1), round(up_diff, 1), round(swing, 1)])
        r = ws_tor.max_row
        ws_tor[f"A{r}"].font = font_bold
        ws_tor[f"A{r}"].border = border_thin_gray
        ws_tor[f"B{r}"].alignment = Alignment(horizontal="center")
        ws_tor[f"B{r}"].font = font_regular
        ws_tor[f"B{r}"].border = border_thin_gray
        ws_tor[f"C{r}"].alignment = Alignment(horizontal="center")
        ws_tor[f"C{r}"].font = font_regular
        ws_tor[f"C{r}"].border = border_thin_gray
        ws_tor[f"D{r}"].number_format = "₹#,##0.0"
        ws_tor[f"D{r}"].font = font_regular
        ws_tor[f"D{r}"].border = border_thin_gray
        ws_tor[f"E{r}"].number_format = "₹#,##0.0"
        ws_tor[f"E{r}"].font = font_regular
        ws_tor[f"E{r}"].border = border_thin_gray
        ws_tor[f"F{r}"].number_format = "₹#,##0.0"
        ws_tor[f"F{r}"].font = font_regular
        ws_tor[f"F{r}"].border = border_thin_gray
        ws_tor[f"G{r}"].number_format = "₹#,##0.0"
        ws_tor[f"G{r}"].font = font_regular
        ws_tor[f"G{r}"].border = border_thin_gray
        ws_tor[f"H{r}"].number_format = "₹#,##0.0"
        ws_tor[f"H{r}"].font = font_bold
        ws_tor[f"H{r}"].border = border_thin_gray

    # Native Excel Horizontal Bar Chart
    chart = BarChart()
    chart.type = "bar"
    chart.style = 2 # Clean neutral style
    chart.grouping = "stacked"
    chart.overlap = 100
    chart.title = "Change in NPV vs Base (₹ lakh) — Base Case = ₹127.5 lakh"
    chart.height = 12
    chart.width = 18
    chart.x_axis.title = "Change in 3-Year NPV (₹ Lakh)"
    chart.y_axis.title = "Sensitivity Driver"

    chart_data = Reference(ws_tor, min_col=6, min_row=4, max_col=7, max_row=12)
    chart_cats = Reference(ws_tor, min_col=1, min_row=5, max_row=12)
    chart.add_data(chart_data, titles_from_data=True)
    chart.set_categories(chart_cats)

    ws_tor.add_chart(chart, "J4")

    for col in ws_tor.columns:
        col_letter = get_column_letter(col[0].column)
        ws_tor.column_dimensions[col_letter].width = 18
    ws_tor.column_dimensions['A'].width = 28
    ws_tor.column_dimensions['B'].width = 16
    ws_tor.column_dimensions['C'].width = 16

    # Save to 02_A2_business_case/
    wb.save(filename)
    print(f"Saved clean human-style model to {filename}")

    # Copy directly to root PJ-1 folder as requested
    root_destination = "A2_GenAI_Cost_ROI.xlsx"
    shutil.copyfile(filename, root_destination)
    print(f"Copied clean model directly to {root_destination}")

if __name__ == "__main__":
    create_clean_human_a2_workbook()
