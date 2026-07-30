import pandas as pd

df1 = pd.DataFrame({"Name": ["A", "B"]})
df2 = pd.DataFrame({"Name": ["C", "D"]})

result = pd.concat([df1, df2], ignore_index=True)

print(result)
