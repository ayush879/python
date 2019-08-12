list1=[]
list2=[]
num=int(input("Enter a total number of element"))
for i in range(1,num+1):
    data=input("Enter data for key :")
    list1.append(data)
for i in range(1,num+1):
    data=input("Enter data for value :")
    list2.append(data)
listdict=dict(zip(list1,list2))
print(list1)
print(list2)
print(listdict)