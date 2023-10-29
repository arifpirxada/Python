'''Problem: Write a Python program to add two objects if both objects are an integer type. '''

obj_one = 6
obj_2nd = 74
obj_list = [obj_one,obj_2nd]

a = obj_list[0]
b = obj_list[1]

if a==str(a) and b==str(b):
	print(a,b)
elif a==str(a) and b==int(b):
	print(a,b)
elif a==int(a) and b==str(b):
	print(a,b)
elif a==int(a) and b==int(b):
	print(a+b)
