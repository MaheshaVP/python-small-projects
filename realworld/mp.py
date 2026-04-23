# ================================
# MATPLOTLIB PRACTICE QUESTIONS
# ================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ----------------
# DATASET
# ----------------
data = {
    "Name": ["A","B","C","D","E","F","G","H","I","J"],
    "Age": [22, 25, 30, 35, 28, 40, 30, 29, 27, 32],
    "Dept": ["IT","HR","IT","Sales","HR","IT","Sales","IT","HR","Sales"],
    "Salary": [20000, 25000, 30000, 29000, 28000, 35000, 40000, 22000, 27000, 32000],
    "Experience": [1, 3, 5, 7, 2, 10, 8, 4, 2, 6]
}

df = pd.DataFrame(data)

# ================================
# LEVEL 1: BASIC PLOTS
# ================================

# 1. Create a line plot:
#    X = Age, Y = Salary

# plt.plot(df['Age'],df['Salary'],data=df)
# plt.title('Age vs Salary')
# plt.xlabel('Age')
# plt.ylabel('Salary')
# plt.show()

# 2. Create a bar chart:
#    Average salary by department

# avg_salary = df.groupby("Dept")["Salary"].mean()
# plt.bar(avg_salary.index,avg_salary.values)
# plt.title("Average salary by department")
# plt.xlabel('Department')
# plt.ylabel('Salary')
# plt.show()

# 3. Create a histogram:
#    Salary distribution

# plt.hist(df["Salary"],bins=5)
# plt.title("Salary distribution")
# plt.xlabel('salary')
# plt.ylabel('freequency')
# plt.show()

# 4. Create a scatter plot:
#    Age vs Salary

# plt.scatter(df['Age'],df['Salary'])
# plt.title("Age vs Salary")
# plt.xlabel("Age")
# plt.ylabel("Salary")
# plt.show()

# 5. Create a pie chart:
#    Count of employees in each department

# dept_count = df['Dept'].value_counts()
# plt.pie(dept_count.values,labels=dept_count.index,autopct="%1.1f")
# plt.title("Department Distribution")
# plt.show()


# ================================
# LEVEL 2: CUSTOMIZATION
# ================================

# 6. Add:
#    - Title
#    - X label
#    - Y label
#    to any one plot

# plt.plot(df["Age"], df["Salary"], marker='o')

# plt.title("Age vs Salary")
# plt.xlabel("Age")
# plt.ylabel("Salary")

# plt.show()

# 7. Scatter plot with colors:
#    IT → yellow
#    HR → blue
#    Sales → green

# color_map = {
#     "IT": "yellow",
#     "HR": "blue",
#     "Sales": "green"
# }
# colors = df["Dept"].map(color_map).fillna("gray")
# plt.scatter(df["Age"], df["Salary"], c=colors)

# plt.title("Age vs Salary by Department")
# plt.xlabel("Age")
# plt.ylabel("Salary")
# plt.show()

# 8. Add legend to scatter plot

# for dept, color in color_map.items():
#     subset = df[df["Dept"] == dept]
#     plt.scatter(subset["Age"], subset["Salary"], c=color, label=dept)

# plt.title("Age vs Salary by Department")
# plt.xlabel("Age")
# plt.ylabel("Salary")

# plt.legend()
# plt.show()


# ================================
# LEVEL 3: MULTIPLE PLOTS
# ================================

# 9. Create 2 plots in one figure (side by side):
#    - Bar chart
#    - Histogram

# fig, ax = plt.subplots(1, 2, figsize=(10,5))

# # Bar chart (Avg Salary by Dept)
# avg_salary = df.groupby("Dept")["Salary"].mean()
# ax[0].bar(avg_salary.index, avg_salary.values)
# ax[0].set_title("Avg Salary by Dept")

# # Histogram (Salary Distribution)
# ax[1].hist(df["Salary"], bins=5)
# ax[1].set_title("Salary Distribution")

# plt.tight_layout()
# plt.show()

# 10. Create 3 subplots:
#     - Line plot
#     - Scatter plot
#     - Histogram

# fig, ax = plt.subplots(1, 3, figsize=(15,5))

# # Line plot
# ax[0].plot(df["Age"], df["Salary"], marker='o')
# ax[0].set_title("Age vs Salary (Line)")

# # Scatter plot
# ax[1].scatter(df["Age"], df["Salary"])
# ax[1].set_title("Age vs Salary (Scatter)")

# # Histogram
# ax[2].hist(df["Salary"], bins=5)
# ax[2].set_title("Salary Distribution")

# plt.tight_layout()
# plt.show()

# ================================
# LEVEL 4: ADVANCED
# ================================

# 11. Sort data by Salary and plot line chart
# df_sorted = df.sort_values(by="Salary")

# plt.plot(df_sorted["Age"], df_sorted["Salary"], marker='o')
# plt.title("Salary Trend (Sorted)")
# plt.xlabel("Age")
# plt.ylabel("Salary")
# plt.show()

# 12. Highlight highest salary point in scatter plot
# max_salary = df["Salary"].max()

# plt.scatter(df["Age"], df["Salary"])

# # highlight max
# highlight = df[df["Salary"] == max_salary]
# plt.scatter(highlight["Age"], highlight["Salary"], marker='o', label="Highest Salary")

# plt.legend()
# plt.title("Highest Salary Highlight")
# plt.show()

# 13. Bar chart:
#     Total salary by department

# total_salary = df.groupby("Dept")["Salary"].sum()

# plt.bar(total_salary.index, total_salary.values)
# plt.title("Total Salary by Dept")
# plt.xlabel("Dept")
# plt.ylabel("Total Salary")
# plt.show()

# 14. Scatter plot:
#     Experience vs Salary

# plt.scatter(df["Experience"], df["Salary"])
# plt.title("Experience vs Salary")
# plt.xlabel("Experience")
# plt.ylabel("Salary")
# plt.show()

# 15. Salary distribution per department
#     (multiple histograms or grouping)

# for dept in df["Dept"].unique():
#     subset = df[df["Dept"] == dept]
#     plt.hist(subset["Salary"], bins=5, label=dept, alpha=0.5)

# plt.legend()
# plt.title("Salary Distribution by Dept")
# plt.show()


# ================================
# FINAL TASK
# ================================

# 16. Create a dashboard-style figure:
#     Combine 3 plots:
#     - Salary distribution
#     - Dept vs Avg Salary
#     - Age vs Salary

fig, ax = plt.subplots(1, 3, figsize=(15,5))

# Salary distribution
ax[0].hist(df["Salary"], bins=5)
ax[0].set_title("Salary Distribution")

# Avg salary by Dept
avg_salary = df.groupby("Dept")["Salary"].mean()
ax[1].bar(avg_salary.index, avg_salary.values)
ax[1].set_title("Avg Salary by Dept")

# Age vs Salary
ax[2].scatter(df["Age"], df["Salary"])
ax[2].set_title("Age vs Salary")

plt.tight_layout()
plt.show()

# ================================
# END
# ================================