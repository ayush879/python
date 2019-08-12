def prime(num):
    print("The prime numbers are : ")
    for i in range(2,num+1):
        k=0
        for j in range(2,i//2+1):
            if i%j==0:
                k=k+1
        if k<=0:
        	print(i,end=" ")
try:
	num=int(input("Enter the range : "))
except:
	print(sys.exc_info()[0],"occured")
else:
	prime(num)