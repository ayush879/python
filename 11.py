#11) Return the date from a given string.
import re
str1 = input("Enter a date : ")
pattern = '[0-9]{2}[-|\/]{1}[0-9]{2}[-|\/]{1}[0-9]{4}'
print(re.findall(pattern, str1))
