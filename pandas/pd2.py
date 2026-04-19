#pandas
import pandas as pd


print(pd.__version__)

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

cardata = pd.DataFrame(mydataset)
print(cardata)

#series
a = [1, 8, 7, 2]
myvar = pd.Series(a)
print(myvar)
print(myvar[1])
#create labels

myvar = pd.Series(a, index=['w','x','y','z'])
print(myvar)
print(myvar['z'])

#data frames
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data)
print(df)
print(df.loc[0])
print(df.loc[[0,1]])

df = pd.DataFrame(data, index=['day1','day2','day3'])
print(df)