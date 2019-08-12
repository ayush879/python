num=int(input("Enter the number of rows : "))
val = 65
for i in range(0, num):
    for j in range(0, i+1):
        ch = chr(val)
        print(ch, end=" ")
        val = val + 1
    print()
num=int(input("Enter the number of rows :"))
n = 65
for i in range(0, num):
    for j in range(0, i+1):
        ch = chr(n)num=int(input("Enter the number of rows :"))
for i in range(0, num):
    for j in range(num, i, -1):
        print("* ", end="")
    print()
    
        print(ch, end=" ")
    n = n + 1
    print()
