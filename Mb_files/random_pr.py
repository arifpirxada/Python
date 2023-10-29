from random import randint

class Die():

	def __init__(self,sides=6):
		self.sides=sides
		
	def roll_die(self):
		return randint(1,self.sides)
		
	#def lop(self,rangge):
#		for i in range(rangge):
#			n=self.roll_die()
#			result.append(n)

		
do=Die()
result=[]
for i in range(10):
	n=do.roll_die()
	result.append(n)
print(result)

did=Die(sides=10)
result=[]
for i in range(10):
	n=did.roll_die()
	result.append(n)
print(result)

done=Die()
result=[]
for i in range(10):
	n=done.roll_die()
	result.append(n)
print(result)
