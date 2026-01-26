import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie"],
    "salary": [40000, 60000, 50000]
}

df = pd.DataFrame(data)

sorted_df = df.sort_values(by="salary")
print(sorted_df)

'''
Output
      name  salary
0    Alice   40000
2  Charlie   50000
1      Bob   60000

'''
