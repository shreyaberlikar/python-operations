import pandas as pd

data = {
    "department": ["IT", "IT", "HR", "HR"],
    "salary": [50000, 60000, 40000, 45000]
}

df = pd.DataFrame(data)

grouped_df = df.groupby("department")["salary"].mean()
print(grouped_df)

'''
Output:
department
HR    42500.0
IT    55000.0
Name: salary, dtype: float64
'''
