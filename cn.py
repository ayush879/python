class com_nu:
    def __init__(self,r=0,i=0):
        self.real=r
        self.imag=i
    def getData(self):
        print("{0}+{1}j".format(self.real,self.imag))
n=int(input("enter the number:"))
m=int(input("enter the number:"))
c=com_nu(n,m)
c.getData()