import numpy as np 
xarr=np.array([1.1,1.2,1.3,1.4,1.5])
yarr=np.array([2.1,2.2,2.3,2.4,2.5])
cond=np.array([True,False,True,True,False])
result=np.where(cond,xarr,yarr)
'''take the value from xarr whenever the corresponding value in cond is True and value from yarr whenever it is false'''
print(result)
print(type(result))
arr=np.random.randn(4,4)
print(arr)
res=np.where(arr>0,2,-2)
print(res)
res=np.where(arr>0,arr,-2)
print(res)