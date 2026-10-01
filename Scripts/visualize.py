import pandas as pd
import matplotlib.pyplot as plt

pnl = pd.read_csv('infosys_annual_clean.csv')

# # Create a figure with two y-axes: one for Sales (bars), one for OPM% (line)
# fig, ax1 = plt.subplots(figsize=(10, 6))

# # Bar chart for Sales on the left axis
# ax1.bar(pnl['FY'], pnl['Sales'], color='steelblue', alpha=0.7, label='Sales (Rs Cr)')
# ax1.set_xlabel('Financial Year')
# ax1.set_ylabel('Sales (Rs Cr)', color='steelblue')

# # # Create a second y-axis sharing the same x-axis, for OPM%
# ax2 = ax1.twinx()
# ax2.plot(pnl['FY'], pnl['OPM %'], color='red', marker='o', linewidth=2, label='OPM %')
# ax2.set_ylabel('Operating Margin %', color='red')

# plt.title('Infosys: Revenue Growth vs Operating Margin (FY17-FY26)')
# fig.tight_layout()
# plt.savefig('chart1_sales_vs_margin.png', dpi=150)
# plt.show()


# # --- Chart 2: Which cost is actually driving the margin decline ---
# fig2, ax = plt.subplots(figsize=(10, 6))

# ax.plot(pnl['FY'], pnl['Employee Cost % of Sales'], marker='o', linewidth=2, 
#          color='green', label='Employee Cost % of Sales')
# ax.plot(pnl['FY'], pnl['Other Mfr. Exp % of Sales'], marker='s', linewidth=2, 
#          color='red', label='Other Mfr. Exp % of Sales (subcontractor/technical costs)')

# ax.set_xlabel('Financial Year')
# ax.set_ylabel('% of Sales')
# ax.set_title('The Real Driver: Subcontractor Cost, Not Employee Cost')
# ax.legend()
# ax.grid(alpha=0.3)

# fig2.tight_layout()
# plt.savefig('chart2_cost_driver.png', dpi=150)
# plt.show()

# # --- Chart 3: Full cost structure as % of Sales, stacked ---
fig3, ax3 = plt.subplots(figsize=(10, 6))

cost_pct_cols = [
     'Employee Cost % of Sales',
     'Other Mfr. Exp % of Sales', 
     'Selling and admin % of Sales',
     'Other Expenses % of Sales',
     'Power and Fuel % of Sales'
]
labels = ['Employee Cost', 'Other Mfr./Subcontractor', 'Selling & Admin', 'Other Expenses', 'Power & Fuel']

ax3.stackplot(pnl['FY'], [pnl[col] for col in cost_pct_cols], labels=labels, alpha=0.85)

ax3.set_xlabel('Financial Year')
ax3.set_ylabel('% of Sales')
ax3.set_title('Infosys: Full Cost Structure as % of Sales (FY17-FY26)')
ax3.legend(loc='upper left', fontsize=9)

fig3.tight_layout()
plt.savefig('chart3_cost_structure.png', dpi=150)
plt.show()