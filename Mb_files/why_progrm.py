l=[]
print('Enter q anytime to exit.')
while True:
	a=input('why you like programming?\n')
	if a!='q':
		l.append(a)
	if a=='q':
		print('Thanks for your responce!\nHave a nice day.')
		break
	
file='programming.txt'
with open(file,'a') as f:
	for item in l:
		h=item
		n=f.write(h)
	