import pandas as pd 
import numpy as np 
print("pandas series with system defined index")
obj=pd.Series([4,2,3,-3])
print(obj)
print(type(obj))
print("series values")
print(obj.values)
print(obj.index)
print(obj[2])
obj=pd.Series([4,2,3,-3],index=['d','b','c','a'])
print(obj)
print(type(obj))
print(obj.values)
print(obj.index)
print(obj['c'])
print(obj[obj>0])
print(obj*2)
print(np.exp(obj))
print('b' in obj)
print('e'in obj)