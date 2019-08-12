for n in range(10,30):
	n1=n
	total=0
	while(n>0):
	    num=n%10
	    total=total+num
	    n=n//10
	if(total%2==0):
		print(n1,"")