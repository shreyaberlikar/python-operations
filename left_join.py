import pandas as pd

student = pd.DataFrame({
    "ID": [1,2,3],
    "Name": ["A","B","C"]
})

marks = pd.DataFrame({
    "ID":[1,2],
    "Marks":[90,80]
})

print(student.merge(marks,on="ID",how="left"))
