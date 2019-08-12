def my_gen():
    n=1
    print("this is printed first")
    yield n
    n+=1
    print("this is printed second")
    yield n
    n+=1
    print("this is printed last")
    yield n
a=my_gen()
print(next(a))
n=1
print(next(a))
print(next(a))
print(next(a))
