#5
import re
str1="""MCA
department"""
print(re.findall(r'^\w\w',str1,re.MULTILINE))
