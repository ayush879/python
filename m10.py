my_list=[]
n=int(input("Enter a total number of Names "))
for i in range(1,n+1):
    data=input("Enter Name" )
    my_list.append(data)
length=[len(x) for x in my_list]
for i in range(0,len(my_list)):
    for j in range(1,length[i]+1):
        print(my_list[i][-j],end=" ")
