import pandas as pd
import numpy as np
s=pd.Series(["a","b","c","a"],dtype="category")
print(s)
#pd.Categorical
cat=pd.Categorical(['a','b','c','a','b','c','a','a','d'])
print(cat)
cat=pd.Categorical(['a','b','c','a','b','c','d'],['c','b','a'])
print(cat)
cat=pd.Categorical(['a','b','c','a','b','c','d'],['c','b','a'],ordered=True)
print(cat)
cat=pd.Categorical(['a','b','c','a','b','c','d'],['a','b','c'],ordered=True)
print(cat)
#.describe
cat=pd.Categorical(['a','b','c','a','b','c','d'],['a','b','c'],ordered=True)
print(cat.describe)
cat=pd.Categorical(['a','b','c','a','b','c','d'],['a','b','c'],ordered=True)
print(cat.categories)
cat=pd.Categorical(['a','b','c','a','b','c','d'],['a','b','c'],ordered=True)
print(cat.ordered)
print(cat.ordered)
s=pd.Series(["a","b","c","a"],dtype="category")
s.cat.categories=["Group %s" % g for g in s.cat.categories ]
print(s.cat.categories)
print()
s=pd.Series(["a","b","c","a"],dtype="category")
print(s)
print("after removal")
print(s.cat.remove_categories("a"))
print(s.cat.remove_categories('a'))
print(s)
#series/dataframe.reindex(index,method,fill_value,limit,tolerance,level,copy)
obj=pd.Series([4.5,6.7,-1.2,3.4],index=['d','a','b','c'])
print(obj)
obj1=obj.reindex(['a','b','c','d','e'])
print(obj1)
print()
obj2=pd.Series(['blue','green','yellow'],index=[0,2,4])
print(obj2)
print(obj2.reindex(range(6),method='ffill'))
obj2=pd.Series(['blue','green','yellow'],index=[0,2,4])
print(obj2)
print(obj2.reindex(range(6),method='bfill'))
obj2=pd.Series(['blue','green','yellow'],index=[0,2,4])
print(obj2)
print(obj2.reindex(range(6),method='nearest'))
obj2=pd.Series(['blue','green','yellow'],index=[0,3,7])
print(obj2)
print(obj2.reindex(range(9),method='nearest'))
print()
df=pd.DataFrame(np.arange(9).reshape((3,3)),index=['a','c','d'],columns=['banglore','mysore','manglore'])
print(df)
df1=df.reindex(['a','b','c','d'],fill_value=12)
print(df1)
df1=df.reindex(['a','b','c','d'])
print(df1)
print(df)
cities=['banglore','manglore','mysore']
print(df.reindex(columns=cities))
print()
s=pd.Series(['tom','william rick','john','albert',np.nan,'1234','stevesmith'])
print(s)
print("lower case is \n",s.str.lower())
print("lower case is \n",s.str.upper())
print("lower case values contained in \n",s.str.islower())
print("upper case values contained in \n",s.str.isupper())
print("numeric values contained in \n",s.str.isnumeric())
print("length is \n",s.str.len())