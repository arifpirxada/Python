'''Problem: Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.'''

a = int(input("Enter: "))
b = int(input("Enter: "))
c = int(input("Enter: "))

if a!=b and a!=c and b!=c:
	sum =a + b + c
	print(sum)
elif a==b or a==c or b==c:
	print(0)