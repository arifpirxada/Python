'''Problem: Write a Python program to check whether a specified value is contained in a group of values.'''

value = int(input("Enter the value "))
group = [6,9,52,3]
if value in group:
	print(f"Yes,the value {value} is present in the group")
elif value not in group:
	print(f"No,the value {value} is not present in the group")