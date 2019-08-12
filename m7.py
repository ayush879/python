list1=[]
for i in range(1,50):
    list1.append(i)
data=[a for a in [b for b in list1 if b%3!=0] if a%2!=0]
print(data)