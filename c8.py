def recur_sum(num):
	if num<=1:
		return num
	else:
		return num+recur_sum(num-1)
num=int(input("enter a number"))
print("sum of numbers",recur_sum(num))