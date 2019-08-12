#14) Return the words that start with a consotant.
import re
str1=input("enter a string:")
pattern='[^aeiouAYUSH]+'
for i in str1:
    print(re.findall(pattern,i))
