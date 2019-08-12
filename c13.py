def combination(n, m):
    if m==0 or m==n:
        return 1
    return combination(n-1,m-1)+combination(n-1,m)

def pascals_triangle(num):
    print("Pascal's tiangle : ")
    for i in range( num):
        result=""
        for j in range(i+1):
            result=result+str(combination(i,j))+"\t"
        print(result)

pascals_triangle(int(input("Enter the number of rows : ")))
