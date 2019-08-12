n = 1
count = 0
dec = 8
num=int(input("Enter the number of rows :"))
for i in range(0, num):
    for k in range(0, dec):
        print(end=" ")
    for j in range(0, i):
        count = count + 1
    n = count
    temp = n
    for j in range(0, i):
        print(n, end=" ")
        n = n - 1
    print()
    n = temp
    dec = dec - 2