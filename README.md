# 🐍 Python Data Cleaning Scripts

## 📘 Introduction to Python

Python is a high-level, interpreted, and beginner-friendly programming language. It is widely used in many domains such as data analysis, machine learning, web development, automation, and scientific computing.

Python is popular because:
- It has simple and readable syntax  
- It supports multiple programming paradigms  
- It has a large collection of libraries  
- It is platform independent  
- It has strong community support  

For data handling and analysis, Python commonly uses the **Pandas** library. Pandas allows us to work with structured data using DataFrames and provides powerful functions for data cleaning and preprocessing.

This repository demonstrates basic data cleaning operations using Python and Pandas.

---

## 📂 Scripts Description

### 1. `data_cleaning.py`

**Purpose:**  
This script performs basic data cleaning operations on a dataset (for example, energy consumption data).

**What this script does:**
- Loads a dataset into a Pandas DataFrame  
- Identifies missing (null) values  
- Removes or fills missing data  
- Displays the cleaned dataset  

**Use Case:**  
Used to prepare raw data for analysis or machine learning by handling incomplete or inconsistent values.

---

### 2. `filter_rows.py`

**Purpose:**  
This script filters rows in a DataFrame based on a condition.

**What this script does:**
- Creates or loads a DataFrame  
- Applies a filtering condition (example: students older than 18)  
- Displays only the filtered rows  

**Use Case:**  
Useful when you want to extract specific records from a large dataset based on logical conditions.

---

### 3. `normalization_basic.py`

**Purpose:**  
This script demonstrates basic data normalization using Pandas.

**What this script does:**
- Takes numerical data from a DataFrame  
- Applies Min-Max normalization  
- Scales values between 0 and 1  

**Use Case:**  
Normalization helps in machine learning and data analysis by:
- Reducing scale differences  
- Improving algorithm performance  

---

### 4. `select_columns.py`

**Purpose:**  
This script selects specific columns from a DataFrame.

**What this script does:**
- Loads or creates a DataFrame  
- Selects only required columns  
- Displays the selected column data  

**Use Case:**  
Helps reduce unnecessary data and focus only on important features.

---

## 🛠 Requirements

- Python 3.x  
- pandas  


