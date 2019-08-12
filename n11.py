import pandas  as pd 
data=[['alex',10],['bob',12],['clark',13]]
df=pd.DataFrame(data,columns=['name','age'])
print(df)
data=[['alex',10],['bob',12],['clark',13]]
df=pd.DataFrame(data,columns=['name','age'],dtype=float)
print(df)