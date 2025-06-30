import pandas as pd
from pathlib import Path

# File request.
input_path = input("Write name / path and name of file to be converted:").strip()
input_file = Path(input_path)

if not input_file.exists():
	print("File does not exist!")
	exit(1)

# Set output file name
output_file = input_file.parent / f"converted_{input_file.name}"

# Open excel file  which has column records.
sheets = pd.read_excel('test_data/spending_tracking_2025.xlsx', sheet_name = None, header=None)

# Transpose.
with pd.ExcelWriter(output_file) as writer:
	for sheet_name, df in sheets.items():
		df_t = df.transpose()
		df_t.to_excel(writer, sheet_name = sheet_name, index = False, header = False)

print(f"File is saved as {output_file}")
