# ================================
# SEABORN PRACTICE DATASET
# ================================

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Name": ["A","B","C","D","E","F","G","H","I","J","K","L"],
    "Age": [22,25,30,35,28,40,30,29,27,32,26,38],
    "Dept": ["IT","HR","IT","Sales","HR","IT","Sales","IT","HR","Sales","HR","IT"],
    "Salary": [20000,25000,30000,29000,28000,35000,40000,22000,27000,32000,26000,37000],
    "Experience": [1,3,5,7,2,10,8,4,2,6,3,9],
    "Gender": ["M","F","M","F","F","M","M","F","F","M","F","M"]
}

df = pd.DataFrame(data)

# ================================
# Q1: DISTRIBUTION + HIST + KDE
# ================================
# Plot Salary distribution using seaborn
# Include:
# - histogram
# - KDE curve
# - proper title

# sns.histplot(df['Salary'], kde=True)
# plt.title("Salary Distribution with KDE")
# plt.xlabel("Salary")
# plt.ylabel("Frequency")
# plt.show()


# ================================
# Q2: BARPLOT + GROUP ANALYSIS
# ================================
# Create barplot:
# - X = Dept
# - Y = Salary (average)
# - Show confidence interval (default)
# - Add title

# sns.barplot(x="Dept", y="Salary", data=df)

# plt.title("Average Salary by Department")
# plt.xlabel("Department")
# plt.ylabel("Average Salary")
# plt.show()

# ================================
# Q3: SCATTER + HUE (RELATIONSHIP)
# ================================
# Create scatter plot:
# - X = Age
# - Y = Salary
# - Color by Dept (hue)
# - Add title

# sns.scatterplot(x="Age", y="Salary", hue="Dept", data=df)

# plt.title("Age vs Salary by Department")
# plt.xlabel("Age")
# plt.ylabel("Salary")
# plt.show()

# ================================
# Q4: BOXPLOT (OUTLIERS + SPREAD)
# ================================
# Create boxplot:
# - X = Dept
# - Y = Salary
# - Show distribution + outliers
# - Add title

# sns.boxplot(x="Dept", y="Salary", data=df)

# plt.title("Salary Distribution by Department")
# plt.xlabel("Department")
# plt.ylabel("Salary")
# plt.show()

# ================================
# Q5: HEATMAP + CORRELATION
# ================================
# Create correlation matrix
# Plot heatmap:
# - show values (annot=True)
# - use any color palette
# - add title

# corr = df[["Age", "Salary", "Experience"]].corr()

# sns.heatmap(corr, annot=True)

# plt.title("Correlation Heatmap")
# plt.show()


# ================================
# BONUS (VERY IMPORTANT)
# ================================
# Create pairplot:
# - include Age, Salary, Experience
# - color by Gender

sns.pairplot(df[["Age", "Salary", "Experience", "Gender"]], hue="Gender")

plt.show()