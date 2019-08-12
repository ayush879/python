a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
c=int(input("enter 3rd number"))
def max(a,b,c):
	if a>b and a>c:
		print("a is greater:",a)
	elif b>c:
		print("b is greater:",b)
	else:
		print("c is greater:",c)
max(a,b,c)