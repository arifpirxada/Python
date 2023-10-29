#1st pr
with open('inPython.txt') as f:
	n=f.read()
	print(n+'\n')
	
#2nd pr
with open('inPython.txt') as l:
	for line in l:
		print(line.rstrip())

#3rd pr
print(' ')
with open('inPython.txt') as t:
	contents=t.readlines()
for line in contents:
		print(line.rstrip())
		
	