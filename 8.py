#8) Return the domain types of given email ids.
import re
str1=input("enter an email id:")
print(re.findall('@',str1))
