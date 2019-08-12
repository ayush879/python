#22) Extract year, month and date from a an url.
import re

string = input("Enter an url : ")
pattern = '/(\d{4})/(\d{1,2})/(\d{1,2})/'
print(re.findall(pattern, string))