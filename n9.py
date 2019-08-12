import pandas as pd
data={'city':['banglore','banglore','banglore','manglore','manglore','manglore'],
'year':[1991,2001,2011,1991,2001,2011],
'population':[4839162,6537124,9621551,1656165,1897730,2345678]}
frame=pd.DataFrame(data)
print("data frame from dictionary")
print(frame)
print("data frame with headers")
print(frame.head())
print("data frame with specific columns")
print(pd.DataFrame(data,columns=['year','city','population']))