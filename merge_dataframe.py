import pandas as pd

student = pd.DataFrame({
    "ID": [1,2,3],
    "Name": ["A","B","C"]
})

marks = pd.DataFrame({
    "ID":[1,2,3],
    "Marks":[90,85,95]
})

result = pd.merge(student, marks, on="ID")

print(result)
