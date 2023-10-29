class user:
	def __init__(self,first_name,last_name,address,login_attempts):
		self.first_name=first_name
		self.last_name=last_name
		self.address=address
		self.login_attempts=login_attempts
	
	def describe(self):
		print('users first name is',self.first_name,'.last name is',self.last_name, '\nand address is:',self.address)
		
	def greet(self):
		print('Hello',self.first_name+' '+self.last_name)
		
	def increment_login_attempts(self):
		self.login_attempts=self.login_attempts+1
		print(self.login_attempts)
		
	def reset_login_attempts(self):
		self.login_attempts=self.login_attempts-self.login_attempts
		print(self.login_attempts)
		
shazam=user('shazam','hero','america',1)
shazam.describe()
shazam.greet()

akshay=user('akshay','kumar','India',0)
akshay.increment_login_attempts()
akshay.increment_login_attempts()
akshay.increment_login_attempts()

akshay.reset_login_attempts()
akshay.increment_login_attempts()

class Admin(user):
	def __init__(self,first_name,last_name,address,login_attempts):
		#self.first_name=first_name
#		self.last_name=last_name
#		self.address=address
#		self.login_attempts=login_attempts
		super().__init__(first_name,last_name,address,login_attempts)
		self.privileges=Privileges()
		self.add_privileges=Privileges()
class Privileges():
	def __init__(self,privileges=[]):
		self.privileges=privileges

	def show_privileges(self):
		print(f'Privileges are listed below:\n {self.privileges}')
	def add_privileges(self,values):
		self.privileges=self.privileges+values
		
		
		
#admin=Admin('ad','min','India',0,['Can add post','Can delete post','Can ban user','Can invite user'])
#admin.privileges.show_privileges()

Harry=Admin('Ha','rry','India','India')
Harry.privileges.add_privileges(['can add user','can ban user','can edit settings'])
Harry.privileges.show_privileges()
