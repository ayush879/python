#20) Matches a string that has an 'a' followed by anything, ending in 'b'.
import re

string = input("Enter a string : ")
pattern = 'a.*?b$'
print(re.findall(pattern, string))
