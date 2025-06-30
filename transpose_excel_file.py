import pandas as pd

# Open excel file  whch has column records.
sheets = pd.read_excel('test_data/spending_tracking_2025.xlsx', sheet_name = None, header=None)

# Transpose.
with pd.ExcelWriter('test_data/converted_file.xlsx') as writer:
	for sheet_name, df in sheets.items():
		df_t = df.transpose()
		df_t.to_excel(writer, sheet_name = sheet_name, index = False, header = False)

