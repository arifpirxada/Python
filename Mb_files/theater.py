your_age="Enter your age: "
oh=""

while oh!=50: # this will loop your age 49 times
	oh=int(input(your_age))
	
	if oh<=3:
		print('you can watch the movie for free!')
	elif oh>3 and oh<12:
		print("you will have to pay 10$")
	elif oh>12:
		print("you ticket's cost is 15$")
	
	