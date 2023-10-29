it=[]
while True:
	a=input('Enter the name: ')
	if a!='exit':
		print('welcome '+a)
		it.append(a)
	elif a=='exit':
		break

file='greet.txt'
with open(file,'a') as f:
	for item in it:
		n=item+' has visited your programme\n'
		w=f.write(n)