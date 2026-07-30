import pandas as pd

data = {
    "Name":["A","B","C"],
    "Marks":[88,95,75]
}

df = pd.DataFrame(data)

print(df.sort_values(by="Marks", ascending=False))
