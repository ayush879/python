list1=[]
num=int(input("Enter a total number of Names "))
for i in range(1,num+1):
    data=input("Enter Name")
    list1.append(data)
length=[len(x) for x in list1]
for i in range(0,len(list1)):
    print(list1[i],end=" length is ")
    print(length[i])