#6 Return consecutive two characters available at start of word boundary.
import re
str1=input("enter a string:").split(" ")

for i in str1:
    print(re.findall('^[a-zA-Z][a-zA-Z]',i))