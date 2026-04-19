#data cleaning

import pandas as pd

data = pd.read_csv('data.csv')
df = data.dropna()

df = data.fillna(130)

print(df.to_string())

print(data.head(10))
# print(data.tail(10))


mean = data['Calories'].mean()
print(mean)

median = data['Pulse'].median()
print(median)

# print(data.to_string())


print(data.duplicated().to_string())

print(data.drop_duplicates(inplace=True))

print(data.to_string())