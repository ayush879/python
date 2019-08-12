#9) Return the domain types with extensions of given email ids.
import re
str1=input("enter an email id:")
print(re.findall(r'@[\w].+',str1))

