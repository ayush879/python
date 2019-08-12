def reversnum(num):
    temp=num
    rev=0
    while(num>0):
        rem=num%10
        rev=rev*10+rem
        num=num//10
    if temp==rev:
        print(temp," is a palindrome.")
    else:
        print(temp," is not a palindrome.")
    return 
def reversestr(str):
    rstr=""
    for i in range(1,len(str)+1):
        rstr=rstr+str[-i]
    if rstr==str:
        print(str," is a palindrome.")
    else:
        print(str," is not a palindrome.")
    return 

def palindrome(x):
    if isinstance(x,int):
        reversenum(x)
    else:
        reversestr(x)        
    return 

palindrome(input("Enter an input to check if it is palindrome or not : "))        
