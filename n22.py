import numpy as np 
'''solve the system of equations 3*x0+x1=9 and x0+2*x1=8'''
a=np.array([[3,1],[1,2]])
b=np.array([9,8])
x=np.linalg.solve(a,b)
print(a,b,x)
print("dot product of 3 and 4 is",np.dot(3,4))
print("dot product of complex number is",np.dot([2j,3j],[2j,3j]))
a=[[1,0],[0,1]]
b=[[4,1],[2,2]]
print(a,b,np.dot(a,b))
a=np.arange(3*4*5*6).reshape((3,4,5,6))
b=np.arange(3*4*5*6)[::-1].reshape((5,4,6,3))
print(a,b,np.dot(a,b)[2,3,2,1,2,2])
s=sum(a[2,3,2,:]*b[1,2,:,2])
print(s)
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
print(np.trace(arr))
