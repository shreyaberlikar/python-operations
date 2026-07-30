import pandas as pd
import numpy as np

data = {
    "Name": ["A", "B", "C", "D"],
    "Marks": [90, np.nan, 75, np.nan]
}

df = pd.DataFrame(data)

print("Original Data")
print(df)

print("\nMissing Values")
print(df.isnull())

print("\nFill Missing with Average")
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
print(df)
