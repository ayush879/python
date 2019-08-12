import numpy as np 
import pandas as pd 
print("reindexing series")
obj=pd.Series([4.5,6.7,-1.2,3.4],index=['d','a','b','c'])
print(obj)
obj1=obj.reindex(['a','b','c','d','e'])
print(obj1)

obj2=pd.Series(['blue','green','yellow'],index=[0,2,4])
print(obj2)
print(obj2.reindex(range(6),method='ffill'))
obj2=pd.Series(['blue','green','yellow'],index=[0,3,7])
print(obj2)
print(obj2.reindex(range(9),method='nearest'))
print("reindexing dataframe")
df=pd.DataFrame(np.arange(9).reshape((3,3)),index=['a','c','d'],columns=['banglore','mysore','manglore'])
print(df)
df1=df.reindex(['a','b','c','d'],fill_value=2)
print(df1)
cities=['banglore','manglore','mysore']
print(df.reindex(columns=cities))