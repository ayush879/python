num=int(input("Enter the number of rows :"))
for i in range(num,0,-1):
    for k in range(num,i,-1):
        print(" ",end="")
    for j in range(0,i):
        print("* ",end="")
    print("\r")