#17) Replaces the substring with the pattern and counts how many times it has done the same.
import re

string = input("Enter a string : ")
string_replace = input("Enter a replace string : ")
pattern = input("enter the pattern")
print(re.sub(pattern, string_replace, string))
