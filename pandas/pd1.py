import numpy as np
import pandas as pd

#data frames
data = {
    "Name" : ["Alice","Bob","Charlie","David","Eve","Alice","charlie"],
    "Age":[25,30,35, np.nan, 1, np.nan, 2],
    "Department":["HR","IT","Finance","IT","HR","HR","Manager"],
    "Salary":[50000,60000,70000,65000,np.nan,50000,20000]
}

# print(data)

df = pd.DataFrame(data)
print(df)

print(df.head(2))
print(df.tail(2))

# print(df("age"))

print(df.loc[1:3,["Age","Department"]])

age = df["Age"]
print(age)

print(df.shape)
print(df.info())
print(df.describe())

#broadcasting
df["Salary"] = df["Salary"] + 5000
print(df["Salary"])

#Rename
df.rename (columns= {"Department":"Dept"}, inplace=True)
print(df)

print(df["Dept"].value_counts())
print(df["Dept"].unique())

