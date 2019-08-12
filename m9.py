list1=[]
num=int(input("Enter a total number of Names "))
for i in range(1,num+1):
    data=input("Enter Name")
    list1.append(data)
first=[x[0] for x in list1]
last=[x[-1] for x in list1]
for i in range(0,len(list1)):
    print("\'",first[i], "\' is the first character of ",list1[i],
          " and \'",last[i],"\'is the last character of ",list1[i])


