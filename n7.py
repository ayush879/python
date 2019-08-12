import numpy as np
a=np.array([[0,1,2],[3,4,5],[6,7,8]])
print(a)
print("first two columns of all rows",a[:3,:2])
print(a[:3,2])
print(a[2:])
print(a[1:,1])
print(a[1,:2])