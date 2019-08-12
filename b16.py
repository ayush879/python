num=int(input("Enter the number of rows :"))
count=0
sum=num
for i in range(1,num+1):
	print(count * ' ',end='')
	for j in range(num,i-1,-1):
		print(j,end=' ')
	print()
	count+=1
