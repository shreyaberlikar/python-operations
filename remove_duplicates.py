import pandas as pd

data = {
    "Name": ["A", "B", "A", "C", "B"],
    "Age": [20, 21, 20, 22, 21]
}

df = pd.DataFrame(data)

print("Before")
print(df)

print("\nAfter Removing Duplicates")
print(df.drop_duplicates())
