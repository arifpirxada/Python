try:
	a=int(input('Enter first number: '))
	b=int(input('Enter second number: '))
except ValueError:
		print('please put integers only. ')
else:
	sum=a+b
	print(sum)