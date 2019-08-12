#12) Return the year of the date from a given string.
import re
string = input("Enter a date : ")
pattern = '.*([1-3][0-9]{3})'
print(re.findall(pattern, string))
