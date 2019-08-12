import matplotlib.pyplot as plt
import numpy as np
#plt.plot(x axis values ,y axis values)
#plt.plot([1,2,3],[3,5,1])
x=np.arange(0,10)
y=x^2
z=x^3
t=x^4
plt.style.use('dark_background')
plt.xlabel("time")
plt.ylabel("distance")
plt.plot(x,y,color="red")
plt.plot(x,z,color='black')
plt.plot(x,t,color='green')
plt.plot(x,y,'->')
#annotate
plt.annotate('second entry',xy=[2,1])
plt.annotate('third entry',xy=[4,6])
plt.legend(['race1','race2','race3'],loc=4)
plt.style.use('dark_background')
plt.savefig("mat.pdf")
plt.show()
