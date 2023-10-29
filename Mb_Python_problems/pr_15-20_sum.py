'''Problem: Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.'''

num_one = int(input("Enter: "))
num_two = int(input("Enter: "))

if num_one+num_two>15 and num_one+num_two<20:
	print(20)
elif num_one+num_two<15 or num_one+num_two>20:
	sum = num_one+num_two
	print(sum)