import json
a=input("what is your favorite number: ")
file='numbers.json'
with open(file,'w') as f:
	json.dump(a,f)
	