def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False
    
statement=input("Enter the elements of a list ")
sequence=list(statement)
filtered = filter(fun, sequence)
print('The filtered vowels are:',end=" ")
for s in filtered:
    print(s,end=" ")
