matrix=[]
m=int(input("enter no of rows"))
n=int(input("enter no of cols"))
for i in range(1,m+1):
    row=[]
for j in range(1,n+1):
    data=input("Enter the data")
    row.append(data)
matrix.append(row)
for x in matrix:
    print(x,end="\t")