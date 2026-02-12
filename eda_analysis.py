import pandas as pd
import numpy as np

# Create sample dataset
data = {
    "Name": ["Shreya", "Amit", "Riya", "Rahul", "Sneha"],
    "Age": [20, 23, 22, 21, 24],
    "Salary": [30000, 40000, 35000, 37000, 50000],
    "Department": ["IT", "HR", "IT", "Finance", "IT"]
}

df = pd.DataFrame(data)

print("Dataset:\n")
print(df)

# -----------------------------
# 1. Basic Information
# -----------------------------
print("\nDataset Info:\n")
print(df.info())

# -----------------------------
# 2. Statistical Summary
# -----------------------------
print("\nStatistical Summary:\n")
print(df.describe())

# -----------------------------
# 3. Value Counts (Categorical)
# -----------------------------
print("\nDepartment Distribution:\n")
print(df["Department"].value_counts())

# -----------------------------
# 4. Correlation Matrix
# -----------------------------
print("\nCorrelation Matrix:\n")
print(df.corr(numeric_only=True))

# -----------------------------
# 5. Basic Insights
# -----------------------------
print("\nBasic Insights:")

print("Average Age:", df["Age"].mean())
print("Maximum Salary:", df["Salary"].max())
print("Department with most employees:",
      df["Department"].value_counts().idxmax())
