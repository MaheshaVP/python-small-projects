#Pandas 

import pandas as pd
import numpy as np


s = pd.Series([10,20,30,40,50])
print(s)
print(s.dtype)

print(s.index)
print(s.values)
s.name = "Numbers"

print(s.iloc[2])

print(s[0:2])

index = ['a','b','c','d','e']

s.index = index

print(s)
print(s['b':'d'])

#logical operators

sand = s[(s>10) & (s<40)]
print(sand)

#modifying
s['d'] = 100

print(f"value of d is",s['d'])

ser = pd.Series(['a',np.nan,1,np.nan,2])
ser.notnull().sum()
print(ser)








