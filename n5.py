import numpy as np 
arr=np.random.randn(6)
print(arr)
print("the sorted array is")
arr.sort()
print(arr)
arr=np.random.randn(5,3)
print(arr)
arr.sort()
print("the sorted array")
print(arr)
arr=np.array([[1,3,2,4],[6,2,4,1]])
print(arr)
arr.sort(axis=0)
print("the sorted array is")
print(arr)
arr=np.array([[1,3,2,4],[6,5,4,8]])
print(arr)
arr.sort(axis=1)
print("the sorted array is")
print(arr)
