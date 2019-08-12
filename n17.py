import pandas as pd 
sdata={'banglore':5600000,'mysore':2400000,'manglore':3400000,'hassan':8989898}
obj=pd.Series(sdata)
print(obj)
print(type(obj))
cities=['chikmangalur','banglore','manglore','mysore']
obj=pd.Series(sdata,index=cities)
print(obj)