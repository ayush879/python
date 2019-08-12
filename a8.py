a=[]
sum1=sum2=0
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
even=[]
odd=[]
for j in a:
    if(j%2==0):
        even.append(j)
        sum1+=j;
    else:
        odd.append(j)
        sum2+=j;
print("The even list",even)
print("sum of even no:",sum1)
print("The odd list",odd)
print("sum of odd no:",sum2)

