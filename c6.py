def pangram(str):
    str=str.lower()
    str=str.replace(" ","")
    alphabets="abcdefghijklmnopqrstuvwxyz"
    flag=True
    for char in alphabets:
        if char in str:
            True
        else:
            flag=False
    if flag:
        print("The given string contains all 26 alphabets")
    else:
        print("The given string does not contain all 26 alphabets")
    return

pangram(input("Enter a string : "))
