num=int(input("Enter the number of rows : "))
for i in range(0, num):
    n=1
    for j in range(0, i+1):
        print(n, end=" ")
        n = n + 1
    print()