import pandas as pd

data = {
    "Name":["A","B","C","D"],
    "Marks":[45,92,76,34]
}

df = pd.DataFrame(data)

print(df[df["Marks"] >= 50])
