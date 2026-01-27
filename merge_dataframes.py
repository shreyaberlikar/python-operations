import pandas as pd

data1 = {
    "id": [1, 2, 3],
    "name": ["Alice", "Bob", "Charlie"]
}

data2 = {
    "id": [1, 2, 3],
    "marks": [85, 90, 78]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

merged_df = pd.merge(df1, df2, on="id")
print(merged_df)
