def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return False
    else:
        return True
statement=input("Enter the statment ")
sequence=list(statement)
filtered = filter(fun, sequence)
print('The filtered statment is:',end=" ")
for s in filtered:
    print(s,end="")