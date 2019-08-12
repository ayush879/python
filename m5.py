statment=input("Enter the statment ")
sequence=list(statment)
upper=[s.lower() for s in sequence]
print('The upper case list is:',end=" ")
print(upper)