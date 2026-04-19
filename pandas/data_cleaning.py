#data cleaning
import numpy as np
import pandas as pd

data = {
    "Name" : ["Alice","Bob","charlie","David","Eve","Alice","charlie"],
    "Age":[25,30,21, np.nan, 12, np.nan, 21],
    "Department":["HR","IT","Finance","IT","HR","HR","Finance"],
    "Salary":[50000,60000,70000,65000,np.nan,50000,70000]
}

df = pd.DataFrame(data)
print(df)

# print(df.isnull().sum())

print(df.dropna(how= "all"))

# print(df)

age = df["Age"].fillna(df["Age"].mean())
salary = df['Salary'].fillna(df['Salary'].median())
print(age)
print(salary)

df['Name'] = df['Name'].str.lower().replace("charlie",'Rose').str.capitalize()
print(df)


df_dup = df[df.duplicated()]
print('Duplicated list : ',df_dup)


department_info = {
    'Department' : ['HR','IT','Finance'],
    'Location' : ['New York','San Francisco','Chicago'],
    'Manager' : ['Laura','Steve','Nina']
}
print(df)

df2 = pd.DataFrame(department_info)
print(df2)

# concate = pd.concat([df,df2])        #column
# concate = pd.concat([df,df2], axis=1)  #row
concate = pd.merge(df,df2,  on = 'Department')  #on department


print(concate)