from cryptography.fernet import Fernet

def encrypt():
    key = Fernet.generate_key()

    with open("files/key.key", "wb") as keyFile:
        keyFile.write(key)

    file = input("Enter file location: ")

    with open(file, "rb") as curFile:
        content = curFile.read()
        encrypted_content = Fernet(key).encrypt(content)
        
        with open(file, "wb") as curFile:
            curFile.write(encrypted_content)
            print(file, "has been encrypted!")  
