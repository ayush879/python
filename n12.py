import pandas as pd 
print("data frames from a list of dictionary")
data=[{'a':1,'b':2},{'a':5,'b':10,'c':20}]
df=pd.DataFrame(data)
print(df)
data=[{'a':1,'b':2},{'a':5,'b':10,'c':20}]
df1=pd.DataFrame(data,index=['first','second'],columns=['a','b'])
df2=pd.DataFrame(data,index=['first','second'],columns=['a','b'])
print(df1)
print(df2)
