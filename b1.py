num=int(input("enter no. of rows:"))
n = 1
for i in range(0, 9):
    for j in range(0, i+1):
    	print(n, end=" ")
    n = n + 1
    print()