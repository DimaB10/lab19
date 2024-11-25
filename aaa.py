import pandas as pd
with open('input.txt', 'r', encoding='utf-8') as file:
    data = file.readlines()
data = [line.strip() for line in data]
unique_data = list(set(data))
series = pd.Series(unique_data)
with open('result.txt', 'w', encoding='utf-8') as result_file:
    result_file.write(series.to_string(index=False))
print("'result.txt'")
