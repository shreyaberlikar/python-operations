import pandas as pd
import numpy as np

# Create sample dataset
data = {
    "Name": ["Shreya", "Amit", "Riya", "Rahul", "Sneha"],
    "Age": [20, np.nan, 22, 21, np.nan],
    "Salary": [30000, 40000, np.nan, 35000, 50000],
    "Department": ["IT", "HR", None, "Finance", "IT"]
}

df = pd.DataFrame(data)

print("Original DataFrame:\n")
print(df)

# -----------------------------
# 1. Check Missing Values
# -----------------------------
print("\nMissing Values Count:\n")
print(df.isnull().sum())

# -----------------------------
# 2. Drop Rows with Missing Values
# -----------------------------
df_drop = df.dropna()
print("\nDataFrame After Dropping Missing Values:\n")
print(df_drop)

# -----------------------------
# 3. Fill Missing Values (Mean Imputation)
# -----------------------------
df_mean = df.copy()
df_mean["Age"].fillna(df_mean["Age"].mean(), inplace=True)
df_mean["Salary"].fillna(df_mean["Salary"].mean(), inplace=True)

print("\nAfter Filling Missing Values with Mean:\n")
print(df_mean)

# -----------------------------
# 4. Fill Missing Values (Mode for Categorical)
# -----------------------------
df_mode = df.copy()
df_mode["Department"].fillna(df_mode["Department"].mode()[0], inplace=True)

print("\nAfter Filling Department with Mode:\n")
print(df_mode)

# -----------------------------
# 5. Fill with Custom Value
# -----------------------------
df_custom = df.fillna("Not Available")

print("\nAfter Filling All Missing Values with Custom Value:\n")
print(df_custom)
