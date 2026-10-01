import pandas as pd

def get_opm_data(filename, company_name):
    df_raw = pd.read_excel(filename, sheet_name='Data Sheet', header=None)
    all_rows = df_raw.values.tolist()

    start = next(i for i, r in enumerate(all_rows) if r[0] == 'PROFIT & LOSS')
    end = next(i for i, r in enumerate(all_rows) if r[0] == 'Quarters')
    pnl_rows = {r[0]: r[1:11] for r in all_rows[start:end] if r[0]}

    years = pd.to_datetime(pd.Series(pnl_rows['Report Date'][:10])).dt.year
    fy_labels = [f'FY{str(y)[-2:]}' for y in years]

    sales = pd.to_numeric(pd.Series(pnl_rows['Sales'][:10]))

    cost_cols = ['Power and Fuel', 'Other Mfr. Exp', 'Employee Cost', 'Selling and admin', 'Other Expenses']
    total_expenses = sum(pd.to_numeric(pd.Series(pnl_rows[c][:10])).fillna(0) for c in cost_cols)

    opm = ((sales - total_expenses) / sales * 100).round(2)

    return pd.DataFrame({'FY': fy_labels, 'Company': company_name, 'OPM %': opm})

infosys_opm = get_opm_data('Infosys.xlsx', 'Infosys')
tcs_opm = get_opm_data('TCS.xlsx', 'TCS')
wipro_opm = get_opm_data('Wipro.xlsx', 'Wipro')

comparison = pd.concat([infosys_opm, tcs_opm, wipro_opm], ignore_index=True)
comparison.to_csv('sector_opm_comparison.csv', index=False)
print(comparison)