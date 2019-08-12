my_list=[]
num=int(input("Enter a total number of Names "))
for i in range(1,num+1):
    data=input("Enter Name")
    my_list.append(data)
vowel=['a','e,','i','o','u','A','E','I','O','U']
name=[my_name for my_name in my_list if my_name[0] in vowel]
print(name)