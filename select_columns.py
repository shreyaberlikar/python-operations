import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [22, 19, 25],
    "marks": [85, 90, 78]
}

df = pd.DataFrame(data)

selected_df = df[["name", "marks"]]
print(selected_df)

'''
Output :
      name  marks
0    Alice     85
1      Bob     90
2  Charlie     78

'''
