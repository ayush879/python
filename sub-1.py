import numpy as np
arr = np.array([0,1,2,3,4,5,6,7,8,9,10,11])
arr[arr%2==1] = -1
print(arr)