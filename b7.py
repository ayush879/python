num=int(input("Enter the number of rows :"))
for i in range(0, num):
    for j in range(num, i, -1):
        print("* ", end="")
    print()