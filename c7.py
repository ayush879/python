def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
try:
	a=int(input("Enter first number:"))
	b=int(input("Enter second number:"))
except:
	print(sys.exc_info()[0],"occured")
print("GCD of", a ,"and",b,": ",gcd(a,b))