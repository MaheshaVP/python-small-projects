# ================================
# PANDAS PRACTICE QUESTIONS
# ================================

import pandas as pd
import numpy as np

# ----------------
# DATASET
# ----------------
data = {
    "Name": ["A","B","C","D","E","F","G","H","I","J"],
    "Age": [22, 25, np.nan, 35, 28, 40, 30, np.nan, 27, 32],
    "Dept": ["IT","HR","IT","Sales","HR","IT","Sales","IT","HR","Sales"],
    "Salary": [20000, 25000, 30000, None, 28000, 35000, 40000, 22000, None, 32000],
    "Experience": [1, 3, 5, 7, 2, 10, 8, 4, 2, 6],
    "Gender": ["M","F","M","F","F","M","M","F","F","M"]
}

df = pd.DataFrame(data)

# ================================
# LEVEL 1: BASICS
# ================================

# 1. Display first 5 rows
print(df.head())

# 2. Display last 3 rows
print(df.tail(3))

# 3. Check dataset info
print(df.info())

# 4. Check summary statistics
print(df.describe())

# 5. Select "Name" column
print(df['Name'])

# 6. Select multiple columns: Name, Salary
print(df[['Name','Salary']])


# ================================
# LEVEL 2: DATA CLEANING
# ================================

# 7. Check missing values
print(df.isna().sum())

# 8. Fill missing Age with mean
df['Age'] = df["Age"].fillna(df["Age"].mean())
print(df["Age"])

# 9. Fill missing Salary with median
df['Salary'] = df['Salary'].fillna(df["Salary"].median())
print(df["Salary"])

# 10. Drop rows where Salary is missing
print(df.dropna(subset=['Salary']))

# 11. Convert Age to integer
df["Age"] = df["Age"].astype(int)

# ================================
# LEVEL 3: FILTERING & SORTING
# ================================

# 12. Employees with Salary > 30000
print(df[df["Salary"] > 30000])

# 13. Employees from IT department
print(df[df['Dept'] == 'IT'])

# 14. Employees Age between 25 and 35
print(df[(df["Age"]>=25) & (df["Age"]<=35)])

# 15. Sort by Salary descending
print(df.sort_values(by='Salary', ascending=False))

# 16. Sort by Dept and Salary
print(df.sort_values(by=['Dept','Salary']))


# ================================
# LEVEL 4: GROUPBY & AGGREGATION
# ================================

# 17. Average salary by Dept
print(df.groupby('Dept')['Salary'].mean())

# 18. Count employees per Dept
print(df.groupby('Dept')['Name'].count())

# 19. Max salary per Dept
print(df.groupby('Dept')['Salary'].max())

# 20. Multiple aggregation (mean, max, min)
print(df.groupby('Dept')['Salary'].agg(['mean','max','min']))


# ================================
# LEVEL 5: APPLY & MAP
# ================================

# 21. Create Bonus column (10% Salary)
df["Bonus"] = df["Salary"] * 0.10
print(df["Bonus"])

# 22. Convert Gender:
#     M → Male
#     F → Female
df['Gender'] = df['Gender'].map({'M':"Male",'F':'Female'})
print(df['Gender'])

# 23. Create Experience Level:
#     <3 → Junior
#     3–6 → Mid
#     >6 → Senior

def exp_level(x):
    if x < 3:
        return "Junior"
    elif 3 <= x <= 6:
        return "Mid"
    else:
        return "Senior"
    
df['exp_level'] = df['Experience'].apply(exp_level)
print(df['exp_level'])

# ================================
# LEVEL 6: MERGE & JOIN
# ================================

df2 = pd.DataFrame({
    "Dept": ["IT","HR","Sales"],
    "Location": ["Bangalore","Delhi","Mumbai"]
})

# 24. Merge df and df2 on Dept
merged_df = pd.merge(df,df2, on='Dept')
print(merged_df)

# 25. Perform left join
left_merged_df = pd.merge(df,df2, on='Dept',how='left')
print(left_merged_df)

# ================================
# LEVEL 7: PIVOT TABLE
# ================================

# 26. Average Salary by Dept
print(pd.pivot_table(df, values='Salary', index='Dept', aggfunc='mean'))

# 27. Dept vs Gender → average salary
print(pd.pivot_table(df, values='Salary', index='Dept', columns='Gender', aggfunc='mean'))


# ================================
# LEVEL 8: ADVANCED
# ================================

# 28. Find correlation matrix
print(df.corr(numeric_only=True))

# 29. Rename all columns to lowercase
df.columns = df.columns.str.lower()
print(df.columns)

# 30. Drop duplicate rows
df = df.drop_duplicates()
print(df)

# ================================
# LEVEL 9: FILE HANDLING
# ================================

# 31. Save dataframe to CSV
df.to_csv('output.csv',index=False)

# 32. Read CSV file back
df_new = pd.read_csv('output.csv')
print(df_new)



# ================================
# FINAL REAL-WORLD CHALLENGE
# ================================

df.columns = df.columns.str.capitalize()

# 33. Handle missing values (Age & Salary)
df['Age'] = df["Age"].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(df["Salary"].median())

# 34. Create Salary after 10% hike (use NumPy)
df['Salary'] = df["Salary"] * 1.10

# 35. Categorize Salary:
#     <25000 → Low
#     25000–35000 → Medium
#     >35000 → High
df['salary_catogory'] = np.where(
    df['Salary'] < 25000, 'Low',
    np.where(df['Salary'] <= 35000,'Medium','High')
)
print(df)


# 36. Find highest paid department
print(df.groupby("Dept")["Salary"].mean().sort_values(ascending=False))


# 37. Average salary by gender
print(df.groupby('Gender')['Salary'].mean())

# 39. Correlation between Age, Salary, Experience
print(df[["Age", "Salary", "Experience"]].corr())

# 40. Top 3 highest salary employees
print(df.sort_values(by="Salary", ascending=False).head(3))

# 41. Save final cleaned dataset
df.to_csv("final_cleaned_data.csv", index=False)