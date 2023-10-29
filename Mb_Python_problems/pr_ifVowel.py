'''Problem: Write a Python program to test whether a passed letter is a vowel or not.'''

letter = input("Enter the letter please: \n").lower()

if "a" in letter:
	print(f"The letter {letter} is vowel")
	
elif "e" in letter:
	print(f"The given letter {letter} is vowel")
	
elif "i" in letter:
	print(f"The given letter {letter} is vowel")
	
elif "o" in letter:
	print(f"The given letter {letter} is vowel")
	
elif "u" in letter:
	print(f"The given letter {letter} is vowel")
	
else:
	print(f"The given letter {letter} is not a vowel")