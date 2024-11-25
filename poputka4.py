import pandas as pd
input_file = 'sales_september_october.csv'
output_file = 'sales_updated.csv'
try:
    df = pd.read_csv(input_file)
    print("")
    print(df)
except FileNotFoundError:
    print(f"'{input_file}'")
    exit()
df['Sales_November'] = [round(x * 1.1) for x in df['Sales_September']]
df['Sales_December'] = [round(x * 1.2) for x in df['Sales_October']]
print("")
print(df)
df.to_csv(output_file, index=False)
print(f"'{output_file}'.")
