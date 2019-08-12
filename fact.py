def cal_fact(x):
    if x==1:
        return 1
    else:
        return(x*cal_fact(x-1))
num=None
while(num!=-1):
    num=int(input("enter a number:"))
    if(num<0):
        print("factorial not possible")
        break
    print("the factorial of",num,"is",cal_fact(num))
