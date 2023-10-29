from pr_users import user

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
		