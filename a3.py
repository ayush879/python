fruits=list(input("enter no of fruits"))
len(fruits)
if len(fruits)>4:
	fruits.append("guava")
	print("EXCELLENT")
	if "banana" in fruits:
        fruits.replace("mango","orange")
        print("GOOD")
	if "apple" in fruits:
		fruits.remove(1)
		print("AVERAGE")
	else:
		print("BAD")
