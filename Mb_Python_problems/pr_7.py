'''Problem : Write a Python program to test whether a number is within 100 of 1000 or 2000.'''

num = int(input("Enter the number : "))
if num<100:
	print("The number is less than 100")
elif num<1000:
	print("The number is less than 1000")
elif num<2000:
	print("Number is less than 2000")
else:
	print("Number is more than 2000")