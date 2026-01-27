import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob"],
    "age": [22, 24]
})

df.to_csv("students.csv", index=False)

new_df = pd.read_csv("students.csv")
print(new_df)

'''
Output:
    name  age
0  Alice   22
1    Bob   24
'''
