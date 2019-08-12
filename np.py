import numpy as np
a=np.array([1,2,3])
print(a)
print(type(a))

a=np.array([1,2,3],dtype=complex)
print(a)
print(type(a))

a=np.array(['a','b','c'])
print(a)
print(type(a))

a=np.array([(1,2,3),(4,5,6)])
print(a)

a=np.array([1,2,3,4,5],ndmin=3)
print(a)

a=np.array([1,0,3],dtype=bool)
print(a)

a=np.array([1,0,3],dtype='object')
print(a)

a=np.array([1,2.4,'a'],dtype='object')
print(a)
type(a)

#asanyarray
#arange
#zeros,zeros_like
#empty,empty_like
#full,full_like
#eye,identity
#ones,ones_like

a=np.asanyarray([1,2,3])
print(a)
print(type(a))

a=np.arange(1,10,2)
print(a)
print(type(a))

a=np.ones((2,3))
print(a)
print(type(a))

a=np.ones_like((2,3))
print(a)
print(type(a))

a=np.zeros((2,3))
print(a)
print(type(a))

a=np.zeros_like((2,3))
print(a)
print(type(a))

a=np.eye(2)
print(a)
print(type(a))
a=np.identity(2)
print(a)
print(type(a))

a=np.empty(2)
print(a)
print(type(a))
a=np.empty([2,2])
print(a)
print(type(a))

a=np.full(2,10)
print(a)
print(type(a))
l=[(1,2,3),(1,2,3)]
a=np.full_like(l,10)
print(a)
print(type(a))

#shape 
 #<array_name>.shape
 #Data type
  #<array_name>.dtype
  #size
   #<array_name>.size
   #number of dimensions
   #<array_name>.ndim

a=np.array([1,2,3,4,5])
print(a.shape)
print(a.dtype)
print(a.size)
print(a.ndim)

a=np.array([1,0,3],dtype=bool)
print(a)
print(a.shape)
print(a.dtype)
print(a.size)
print(a.ndim)


a=np.array([1,0,3],dtype='object')
print(a)
print(a.shape)
print(a.dtype)
print(a.size)
print(a.ndim)

#array_name[index]
#array_name[starting_pos,ending_pos]
#array_array_name[:]

a=np.arange(8)
print(a[3])
print(a[2:4])
#print(a[2,4])
print(a[:])

#array_name[row_index][col_index]
#array_name[row_index,col_index]
#array_name[slice_num:slice_num]
#array_name[:2]
#print(a[1,:2])
#array_name[:2,2]
a=np.array([(0,1,2),(3,4,5),(6,7,8)])
print(a[1,:2])
print(a[1,2])