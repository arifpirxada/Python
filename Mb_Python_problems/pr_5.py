''' Problem 5 : Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.'''

num = int(input("Enter the number "))
if num<17 or num==17:
	diff = 17-num
	print("  ",diff)
elif num>17:
	diff = 17-num
	double = diff+diff
	print("  ",double)