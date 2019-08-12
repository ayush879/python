def fun(variable):
    letters=['a','e','i','o','u']
    if (variable in letters):
        return True
    else:
        return False
str1=input("enter list element")
str2=list(str1)
filt1=filter(fun,str2)
for s in filt1:
    print(s)