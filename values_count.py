import pandas as pd

data = {
    "Department":["IT","HR","IT","Finance","HR","IT"]
}

df = pd.DataFrame(data)

print(df["Department"].value_counts())
