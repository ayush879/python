import pandas as pd 
print("data frames from dictionary of series")
d={'one':pd.Series([1,2,3],index=['a','b','c']),'two':pd.Series([1,2,3,4]
,index=['a','b','c','d'])} 
df=pd.DataFrame(d)
print(df)
d={'one':pd.Series([1,2,3],index=['a','b','c']),'two':pd.Series([1,2,3,4]
,index=['a','b','c','d'])} 
df=pd.DataFrame(d)
print(df['one'])
d={'one':pd.Series([1,2,3],index=['a','b','c']),'two':pd.Series([1,2,3,4]
,index=['a','b','c','d'])} 
df=pd.DataFrame(d)
print("adding new column by passing as series:")
df['three']=pd.Series([10,20,30],index=['a','b','c'])
print(df)
df['four']=df['one']+df['three']
print(df)