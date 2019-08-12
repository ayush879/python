num=int(input("Enter the number of rows :"))
for i,j in zip(range( 1,num+1),reversed(range(0,num))):
	print(j*' ',i*str(i)," ", end="")
	print("")
num=int(input("Enter the number of rows :"))
count=num
for i in range(1,num+1):
	print(count * ' ',end='')
	for j in reversed(range(1,i+1)):
		print(j,end='')
	print()
	count-=1