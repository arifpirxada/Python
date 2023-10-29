file=' goa.txt'
try:
	with open(file) as f:
		n=f.read()
		print(n)
except FileNotFoundError:
	print('file nhi mil rahi bhai!')