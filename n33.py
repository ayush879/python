import pandas as pd 
import numpy as np 
d={'name':['Alisa','Bobby','jodha','jack','raghu','Cathrine','Alisa','Bobby',
'kumar','Alisa','Alex','Cathrine'],
'Age':[26,24,23,22,23,24,26,24,22,23,24,24],
'Score':[85,63,55,74,31,77,85,63,42,62,89,77]}
df=pd.DataFrame(d,columns=['name','Age','Score'])
print(df)
print("MINIMUM")
print(df.min())
print("MINIMUM AGE")
print(df['Age'].min())
print("MINIMUM NAME ")
print(df['name'].min())
print("MAXIMUM")
print(df.max())
print("MAXIMUM AGE")
print(df['Age'].max())
print("MINIMUM NAME ")
print(df['name'].max())