'''Problem 8: Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.'''

num =int(input("Enter the number: "))
if num%2==0:
	print("The number is even")
elif num%2!=0:
	print("The number is odd")