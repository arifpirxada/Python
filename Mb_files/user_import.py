from pr_users import user,Admin,Privileges

raja=Admin('Ra','ja','Nepal',7)
raja.privileges.add_privileges(['can go anywhere','can do anything','can kill anyone'])
raja.privileges.show_privileges()