import pandas as pd 
import numpy as np 
df=pd.DataFrame([[2.0,1.0],[3.0,np.nan],[1.0,0.0]],columns=list('AB'))
print("CUMMULATIVE SUM")
print(df.cumsum())
print("CUMMULATIVE PRODUCT")
print(df.cumprod())
df=pd.DataFrame({"person":["john","myla",None,"john","myla"],
"Age":[24,np.nan,21.,33,26],"Dependents":[False,True,True,True,False]})
print(df)
print("COUNT")