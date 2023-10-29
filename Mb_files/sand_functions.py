class rest:
	def __init__(self,name,age,number_served):
		self.name=name
		self.age=age
		self.number_served=0
		
	def cust(self):
		print('the name of the customer is', self.name,'and age is',self.age)
	
	def open_rest(ing):
		print('restrount is open come in!')

	def set_served(self,number_served):
		self.number_served=number_served
		s=f"Served {number_served} number of customers "
		print(s)
		
	def increment(self,increase):
		inc=f"Now the number served is {self.number_served+increase}, Today's report."
		return inc
	
restaurant=rest('restaurant',43,56)
print(restaurant.number_served)
restaurant.number_served=70
print(restaurant.number_served)
restaurant.set_served(67)
incre=restaurant.increment(33)
print(incre)

class IceCreamStand(rest):
	def __init__(self,name,age,number_served,flavors):
		self.name=name
		self.age=age
		self.number_served=0
		self.flavors=flavors
		
	def display_flavors(self):
		print(f'Flavors are {self.flavors}')
		
icecreamstall=IceCreamStand('Icecreamstall',13,4,['sweet','choco','icy','salty'])
icecreamstall.display_flavors()



	