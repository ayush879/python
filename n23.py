import numpy as np 
print("rand function is")
print(np.random.rand(3,2))
print("randn function is")
print(np.random.randn())
print(2.5*np.random.randn(2,4)+3)
print("randint function is")
print(np.random.randint(2,size=10))
print(np.random.randint(3,size=10))
print(np.random.randint(5,size=10))
print(np.random.randint(5,size=(2,4)))
print("random sample function is")
print(np.random.random_sample())
print(np.random.random_sample((5,)))
'''three-by-two array of random numbers from [-5,0)'''
print(5*np.random.random_sample((3,2))-5)