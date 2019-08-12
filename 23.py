#23) Separate and print the numbers of a given string.
import re
str1 = input("Enter a string : ")
pattern = '\d+'
print(re.findall(pattern, str1))