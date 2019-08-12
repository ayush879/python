import numpy as np 
arr=np.random.randn(5,4)
print(arr)
print("sum of all elements in array is",arr.sum())
print("mean of the array is",arr.mean())
print("sum of all elements in array with axis 0 is",arr.sum(axis=0))
print("mean of the array is with axis 0 is",arr.mean(axis=0))
print("sum of all elements in array with axis 1 is",arr.sum(axis=1))
print("mean of the array is with axis 1 is",arr.mean(axis=1))
arr=np.array([0,1,2,3,4,5,6,7])
print(arr)
print("the cummulative sum is",arr.cumsum())
print("the cummulative sum across axis 0 is",arr.cumsum(axis=0))


