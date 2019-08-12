#21) Matches a word containing 'z', not start or end of the word.
import re

str1 = input("Enter a string : ").split(" ")
pattern = '\Bz\B'
for i in str1:
    print(re.findall(pattern, i))