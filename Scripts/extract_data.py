# import pandas as pd

# # Tell pandas to show ALL rows and columns, don't truncate
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)

# df_raw = pd.read_excel('Infosys.xlsx', sheet_name='Data Sheet', header=None)

# print(df_raw)



import pandas as pd

df_raw = pd.read_excel('Infosys.xlsx', sheet_name='Data Sheet', header=None)

pnl = df_raw.iloc[15:39]

pnl = pnl.dropna(how='all', subset=range(1,11))

pnl = pnl.set_index(0)

pnl = pnl.T

# Convert all the financial columns to actual numbers (they became 'object' type after transpose)
numeric_cols = ['Sales', 'Power and Fuel', 'Other Mfr. Exp', 'Employee Cost', 
                 'Selling and admin', 'Other Expenses', 'Other Income', 
                 'Depreciation', 'Interest', 'Profit before tax', 'Tax', 'Net profit']
for col in numeric_cols:
    pnl[col] = pd.to_numeric(pnl[col], errors='coerce')
 
pnl['Report Date'] = pd.to_datetime(pnl['Report Date'])
pnl['FY'] = pnl['Report Date'].dt.year.apply(lambda y: f'FY{str(y)[-2:]}')
pnl= pnl.drop(columns=['Report Date'])
pnl = pnl.set_index('FY').reset_index()

# Total operating expenses = sum of the 5 cost lines
cost_cols = ['Power and Fuel', 'Other Mfr. Exp', 'Employee Cost', 'Selling and admin', 'Other Expenses']
pnl['Total Expenses'] = pnl[cost_cols].sum(axis=1)

# Operating Profit and Operating Margin %
pnl['Operating Profit'] = pnl['Sales'] - pnl['Total Expenses']
pnl['OPM %'] = (pnl['Operating Profit'] / pnl['Sales'] * 100).round(2)

for col in cost_cols:
    pnl[f'{col} % of Sales'] = (pnl[col] / pnl['Sales'] * 100).round(2)
# Year-over-year Sales growth %
pnl['Sales YoY %'] = (pnl['Sales'].pct_change() * 100).round(2)
# Net Profit Margin %
pnl['Net Margin %'] = (pnl['Net profit'] / pnl['Sales'] * 100).round(2)

print(pnl[['FY', 'Sales', 'OPM %', 'Employee Cost % of Sales', 'Other Mfr. Exp % of Sales', 'Sales YoY %']])

# pnl.to_csv('infosys_annual_clean.csv', index=False)
# print("Saved to infosys_annual_clean.csv")