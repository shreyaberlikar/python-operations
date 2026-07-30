import pandas as pd

df = pd.DataFrame({
    "name":["A","B"],
    "marks":[90,80]
})

df.rename(columns={"name":"Student_Name",
                   "marks":"Score"},
          inplace=True)

print(df)
