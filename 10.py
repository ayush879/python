#10) Return the domain of given email ids.
import re
str1=input("enter an email id:")
print(re.findall('\.[\w].+',str1))