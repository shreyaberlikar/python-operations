import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create sample dataset
data = {
    "Name": ["Shreya", "Amit", "Riya", "Rahul", "Sneha"],
    "Age": [20, 23, 22, 21, 24],
    "Salary": [30000, 40000, 35000, 37000, 50000],
    "Department": ["IT", "HR", "IT", "Finance", "IT"]
}

df = pd.DataFrame(data)

# Set seaborn style
sns.set(style="whitegrid")

# -----------------------------
# 1. Bar Chart (Department Count)
# -----------------------------
plt.figure()
df["Department"].value_counts().plot(kind="bar")
plt.title("Department Distribution")
plt.xlabel("Department")
plt.ylabel("Count")
plt.show()

# -----------------------------
# 2. Histogram (Salary)
# -----------------------------
plt.figure()
plt.hist(df["Salary"])
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

# -----------------------------
# 3. Boxplot (Salary)
# -----------------------------
plt.figure()
sns.boxplot(y=df["Salary"])
plt.title("Salary Boxplot")
plt.show()

# -----------------------------
# 4. Heatmap (Correlation)
# -----------------------------
plt.figure()
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True)
plt.title("Correlation Heatmap")
plt.show()
