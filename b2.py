num=int(input("Enter the number of rows:"))
n = 2 * num
for i in range(0, num):
    for j in range(0, n):
        print(end=" ")
    n = n - 2
    for j in range(0, i+1):
        print("* ", end="")
    print()
