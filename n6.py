import numpy as np
dtype=[('name','S10'),('height',float),('age',int)]
values=[('arthur',1.8,41),('lancelot',1.9,38),('galahad',1.7,38)]
a=np.array(values,dtype=dtype)
print(a)
print("sorted based on height")
print(np.sort(a,order='height'))
print("sorted based on age and if age is equal then based on height")
print(np.sort(a,order=['age','height']))
arr=np.arange(16).reshape((2,2,4))
print(arr)
print(arr.swapaxes(1,2))