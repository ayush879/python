n=int(input("enter the value of n"))
n/=2
n=int(n)
for x in range(1,n+2) :
	for y in range(1,x+1):
		print(" *",end="")
	print()
for x in range(n,-1,-1) :
	for y in range(x-1,-1,-1):
		print(" *",end="")
	print()
