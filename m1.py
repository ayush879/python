import math
num=(lambda n:math.sqrt(n))
print(num(9))
n=lambda x,y,z,p:x+y*z/p
print(n(12,23,34,21))
list1=list((1,3,5,9,8,12))
list2=list(filter(lambda x:(x%3==0),list1))
print(list2)
my_list=['hello', '', '', 'people', '', '!']
list1=list(filter(None,my_list))
print(list1)
names = ['Alpha', 'Bravo', 'jackson', 'jaguar', 'jadu', 'Foxtrot']
first_letters = ['j']
output_names = [name for name in names if (name[0] in first_letters)]
print(output_names)
from functools import reduce
nums = [10, 20, 30,]
nums_product = reduce( (lambda x, y: x * y), nums)
print("Product of the numbers : ",nums_product)
