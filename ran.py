import sys
randomlist=['a',0,2]
for entry in randomlist:
    try:
        print("the entry is",entry)
        r=1/int(entry)
        break
    except:
        print("oops!",sys.exc_info()[0],"occured.")
        print('next entry.')
        print()
print("the reciprocal of",entry,"is",r)

try:
    a=int(input("enter a positive integer:"))
    if a<=0:
        raise ValueError("that is not a postive number!")
except ValueError as ve:
    print(ve)

try:
    raise KeyboardInterrupt
finally:
    print('goodbye,world!')
