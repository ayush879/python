#PRINT all text that start with a
import re
list=["ayush","vijay","kalyan","amit","aqib"]
for ele in list:
    print(re.match("a",ele))