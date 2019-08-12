#19) Find sequences of lowercase letters joined with a underscore.
import re

string = input("Enter a string : ")
pattern = '^[a-z]+_[a-z]+$'
print(re.findall(pattern, string))