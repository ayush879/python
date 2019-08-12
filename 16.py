#16) Split with multiple delimiters.
import re
str1 = 'The quick brown\nfox jumps*over the lazy dog.'
print(re.split('; |, |\*|\n',str1))