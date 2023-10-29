'''Problem 9: Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2.'''

string = input("Enter the string: ")
if len(string)>1:
	first_two = string[0]+string[1]
	n = 6
	for i in range(n):
		print(first_two)
else:
	print(string)