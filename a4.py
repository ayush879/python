var=input("enter a variable")
if var.isnumeric():
	print("you have entered a number")
elif var.isalpha():
	if var.isupper():
		print("you have entered string in upper case")
	else:
		print("you have entered string in lower case")
else:
		print("you have entered something else")
