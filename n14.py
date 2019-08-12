import pandas as pd 
print("data frame eith column deletion")
d={'one':pd.Series([1,2,3],index=['a','b','c']),
'two':pd.Series([1,2,3,4],index=['a','b','c','d']),
'three':pd.Series([10,20,30],index=['a','b','c'])}
df=pd.DataFrame(d)
print("our datagram is:")
print(df)
print("deleting the first column using del function:")
del df['one']
print(df)
print("deletinganother column using pop function:")
df.pop('two')
print(df)
d={'one':pd.Series([1,2,3],index=['a','b','c']),
'two':pd.Series([1,2,3,4],index=['a','b','c','d'])}
df=pd.DataFrame(d)
print(df.loc['b'])
df=pd.DataFrame(df)
print(df.iloc[2])
print("sliced rows")
df=pd.DataFrame(d)
print(df[2:4])

