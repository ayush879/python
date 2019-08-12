#13) Return the words that start with a vowel.
import re
str1=input("enter a string:")
pattern='^[aeiouAEIOU]'
for i in str1:
    print(re.findall(pattern,i))
