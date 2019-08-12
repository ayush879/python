import numpy as np 
import pandas as pd 
s=pd.Series(np.random.randn(10))
print("series",s)
print("min is",s.agg('min'))
print("max is ",s.agg('max'))
print("mean is",s.agg('mean'))
print("median is",s.agg('median'))
print("sum is",s.agg('sum'))
print("product is",s.agg('prod'))
print("standard deviation is",s.agg('std'))
print("variance is",s.agg('var'))