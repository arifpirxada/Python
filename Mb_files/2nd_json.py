import json

file='numbers.json'
with open(file) as f:
	numbers=json.load(f)
	
print("I know your favorite number! it's",numbers)