file='find_the.txt'
with open(file,'r') as f:
	n=f.read()
	q=n.lower().count('lower')
	print(q)
	