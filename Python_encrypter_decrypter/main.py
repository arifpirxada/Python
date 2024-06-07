from encrypt import encrypt
from decrypt import decrypt

print("Welcome! press 'en' to encrypt a file and 'de' to decrypt a file.")
choice = input()

if (choice == 'en'):
    encrypt()
elif(choice == 'de'):
    decrypt()
else:
    print(choice, " Invalid command!")
