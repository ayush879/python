import numpy as np 
n,p=10,.5
s=np.random.binomial(n,p,1000)
print(s)
sum=sum(np.random.binomial(9,0.1,20000)==0)/20000.
print(sum)
print("chisquare")
print(np.random.chisquare(2,4))
shape,scale=2.,2. 
s=np.random.gamma(shape,scale,1000)
print("gamma distribution")
print(s)
mu,sigma=0,0.1
s=np.random.normal(mu,sigma,1000)
print("normal distribution")
print(s)
print("uniform distribution")
s=np.random.uniform(-1,0,1000)
print(s)
print(np.all(s>=-1))
print(np.all(s<0))