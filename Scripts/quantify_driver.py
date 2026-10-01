import pandas as pd

pnl = pd.read_csv('infosys_annual_clean.csv')

# Compare peak margin year (FY21) to latest year (FY26)
fy21 = pnl[pnl['FY'] == 'FY21'].iloc[0]
fy26 = pnl[pnl['FY'] == 'FY26'].iloc[0]

# Total OPM% decline
opm_decline = fy21['OPM %'] - fy26['OPM %']
print(f"Total OPM decline (FY21 to FY26): {opm_decline:.2f} percentage points")

# Change in each cost line's % of Sales
cost_pct_cols = ['Employee Cost % of Sales', 'Other Mfr. Exp % of Sales', 
                  'Selling and admin % of Sales', 'Other Expenses % of Sales', 
                  'Power and Fuel % of Sales']

for col in cost_pct_cols:
    change = fy26[col] - fy21[col]
    print(f"{col}: changed by {change:+.2f} points")

# What % of the total decline does Other Mfr. Exp explain?
other_mfr_change = fy26['Other Mfr. Exp % of Sales'] - fy21['Other Mfr. Exp % of Sales']
contribution_pct = (other_mfr_change / opm_decline) * 100
print(f"\nOther Mfr. Exp alone explains {contribution_pct:.0f}% of the total OPM decline")