import numpy as np 
arr=np.array([[0,1,2],[3,4,5],[6,7,8]])
print(arr)
print("the cummulative sum is")
print(arr.cumsum())
print("sum of all elements in array with axis 0 is",arr.cumsum(axis=0))
print("sum of all elements in array with axis 1 is",arr.cumsum(axis=1))
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
print("the cummulative product is")
print(arr.cumprod())
print("product of all elements in array with axis 0 is",arr.cumprod(axis=0))
print("product of all elements in array with axis 1 is",arr.cumprod(axis=1))
arr=np.array([[0,1,2],[3,4,5],[6,7,8]])
print(arr)
print("the standard deviation is")
print(arr.std())
print("the variation is")
print(arr.var())
print("the standard deviation across axis 0 is")
print(arr.std(axis=0))
print("the variation acorss axis 0 is")
print(arr.var(axis=0))
print("the standard deviation across axis 1 is")
print(arr.std(axis=1))
print("the variation acorss axis 1 is")
print(arr.var(axis=1))

