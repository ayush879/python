import numpy as np 
array=np.array(['alpha','beta','gama','alpha','omega','pi','alpha','beta','delta'])
print(array)
print(array[array=='alpha'])
data=np.random.randn(9,4)
print(data)
print(data[array=='alpha'])
print(data[array=='alpha',2:])
print(data[array=='alpha',1:])
print(data[~(array=='alpha')])
c=array=='beta'
print(type(c))
print(data[c])
print(data[~c])
print(data[array!='alpha'])
c=(array=='alpha') | (array=='gama')
print(data[c])
print(type(c))