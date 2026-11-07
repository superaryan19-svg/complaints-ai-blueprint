import matplotlib.pyplot as plt
import numpy as np

def generate_tornado():
    drivers = [
        "Adoption (50% → 95%)",
        "Cost per escalation (₹2,500 → ₹8,000)",
        "Realisation factor (30% → 70%)",
        "Minutes saved (×0.6 → ×1.3)",
        "Agent cost per hour (₹300 → ₹500)",
        "Run cost (×0.75 → ×1.5)",
        "Acceptance rate (65% → 95%)",
        "Token prices (×0.5 → ×3)"
    ]

    # Change in NPV vs Base (Base NPV = 127.5 lakh)
    # Downside diff = Low NPV - 127.5 (negative)
    # Upside diff = High NPV - 127.5 (positive)
    # For Run cost & Token prices, lower cost is upside, higher cost is downside
    low_npv = [11.4, 52.1, 58.3, 58.3, 84.3, 79.5, 86.8, 99.0]
    high_npv = [185.5, 218.0, 196.7, 179.4, 170.7, 151.5, 147.8, 134.6]
    base_npv = 127.5

    downside_diff = [l - base_npv for l in low_npv]
    upside_diff = [h - base_npv for h in high_npv]

    # Reverse so largest swing appears at top
    drivers.reverse()
    downside_diff.reverse()
    upside_diff.reverse()
    low_npv.reverse()
    high_npv.reverse()

    y_pos = np.arange(len(drivers))

    fig, ax = plt.subplots(figsize=(12, 6.5), dpi=300)

    # Plot bars
    bars_down = ax.barh(y_pos, downside_diff, align='center', color='#e65c00', alpha=0.9, height=0.55, label='Downside Impact')
    bars_up = ax.barh(y_pos, upside_diff, align='center', color='#2e7d32', alpha=0.9, height=0.55, label='Upside Impact')

    # Baseline vertical line at 0
    ax.axvline(0, color='black', linewidth=1.2, linestyle='--')

    # Formatting axes
    ax.set_yticks(y_pos)
    ax.set_yticklabels(drivers, fontsize=10, fontweight='medium')
    ax.set_xlabel('Change in 3-Year NPV vs Base Case (₹ Lakh) [Base NPV = ₹127.5 Lakh]', fontsize=11, labelpad=10, fontweight='bold')
    ax.set_title('GenAI Financial Sensitivity: Tornado Analysis on 3-Year NPV (₹ Lakh)', fontsize=13, fontweight='bold', pad=15)

    # Add data labels
    for i, (d, u, l_val, h_val) in enumerate(zip(downside_diff, upside_diff, low_npv, high_npv)):
        # Label downside
        ax.text(d - 3, i, f"₹{l_val:.1f}L", va='center', ha='right', fontsize=8.5, fontweight='bold', color='#b30000')
        # Label upside
        ax.text(u + 3, i, f"₹{h_val:.1f}L", va='center', ha='left', fontsize=8.5, fontweight='bold', color='#006400')

    ax.set_xlim(-140, 110)
    ax.grid(axis='x', linestyle=':', alpha=0.6)
    ax.legend(loc='lower right', frameon=True, facecolor='#f8f9fa', edgecolor='none')

    # Annotation box
    ax.text(0.02, 0.05, 
            "Key Consultant Insight:\n• Adoption & Avoided Escalations swing NPV most (~₹170L+ swing).\n• Token pricing swings NPV least (<₹36L swing).\n• Token cost is not the critical business risk.", 
            transform=ax.transAxes, fontsize=9, bbox=dict(boxstyle="round,pad=0.6", facecolor="#fff9e6", edgecolor="#ffd166"))

    plt.tight_layout()
    output_path = "02_A2_business_case/tornado_chart.png"
    plt.savefig(output_path)
    plt.close()
    print(f"Tornado chart successfully saved to {output_path}")

if __name__ == "__main__":
    generate_tornado()
