
#18) Matches a string that has an a followed by zero or more b's.
import re
string = input("Enter a string : ")
pattern = 'ab*?'
print(re.findall(pattern, string))