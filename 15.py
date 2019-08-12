#15) Validating a phone number.
import re
str1 = input("Enter a phone number : ")
pattern = '\+?\d[\d -]{8,12}\d'
print(re.findall(pattern, str1))
