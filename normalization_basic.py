"""
File Name: normalization_basic.py
Description: This file demonstrates Normalization using Pandas in Python.
Normalization scales data values between 0 and 1 using Min-Max Scaling.
"""

import pandas as pd
import numpy as np

# -----------------------------
# 1. Create Sample DataFrame
# -----------------------------
data = {
    'Marks': [45, 60, 75, 90, 100],
    'Attendance': [65, 70, 80, 85, 95]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# ----------------------------------------
# 2. Min-Max Normalization using Formula
# ----------------------------------------
normalized_df = (df - df.min()) / (df.max() - df.min())

print("\nNormalized DataFrame (Min-Max Scaling):")
print(normalized_df)

# ------------------------------------------------
# 3. Normalization Column-wise (Manual Pandas)
# ------------------------------------------------
df['Marks_Normalized'] = (df['Marks'] - df['Marks'].min()) / (df['Marks'].max() - df['Marks'].min())
df['Attendance_Normalized'] = (
    (df['Attendance'] - df['Attendance'].min()) /
    (df['Attendance'].max() - df['Attendance'].min())
)

print("\nDataFrame with Normalized Columns:")
print(df)

# ----------------------------------------
# 4. Normalization using NumPy
# ----------------------------------------
numpy_normalized = (df[['Marks', 'Attendance']] - np.min(df[['Marks', 'Attendance']])) / \
                   (np.max(df[['Marks', 'Attendance']]) - np.min(df[['Marks', 'Attendance']]))

print("\nNormalized using NumPy:")
print(numpy_normalized)
