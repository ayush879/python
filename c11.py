def divisor(num):
	x=[]
	for i in range(1,num+1):
		if(num%i)==0:
			x.append(i)
	print("divisiors of",num,":",x)
	return x

def sum(num=[]):
	total=0
	length=len(num)
	for i in num:
		total+=i
	print("number of divisors:",length)
	print("divisors sum:",total)
	return

n=int(input("enter a number:"))
sum(divisor(n))