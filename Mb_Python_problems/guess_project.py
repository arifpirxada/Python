import random as rd
cum=rd.randint(1,6)

for i in range(1,51):
	
	guess=int(input("Guess the number: "))
	
	if guess==cum:
		print(f"You guessed it right in {i}! ")
		
	elif guess<cum:
		print("You are too low")
		
	elif guess>cum:
		print("You are too high")
		