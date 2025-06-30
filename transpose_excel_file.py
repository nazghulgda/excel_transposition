import pandas as pd

# Open excel file  whch has column records.
df = pd.read_excel('test_data/spending_tracking_2025.xlsx', header=None)

# Transpose.
df = df.transpose()

# Save excel file with row records.
df.to_excel('test_data/converted_file.xlsx', index = False, header = False)
