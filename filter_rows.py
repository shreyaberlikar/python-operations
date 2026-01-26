import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [22, 17, 25, 16]
}

df = pd.DataFrame(data)

filtered_df = df[df["age"] > 18]
print(filtered_df)


'''
output:
      name  age
0    Alice   22
2  Charlie   25
'''
