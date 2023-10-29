''' Problem 6 : Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum. '''

first_num = int(input("Enter the first number "))
second_num = int(input("Enter the second number "))
third_num = int(input("Enter the third number "))

if first_num==second_num==third_num:
	summ=first_num+second_num+third_num
	sum=summ+summ+summ
	print(sum)
	
else:
	print(first_num+second_num+third_num)
	