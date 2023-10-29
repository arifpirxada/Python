a=input('Enter your name: ')
lis=' '
filename='writen.txt'
with open(filename,'a') as f:
	lis+=a+'\n'
	w=f.write(lis)
	
