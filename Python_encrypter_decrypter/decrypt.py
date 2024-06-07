from cryptography.fernet import Fernet

def decrypt():
    with open("files/key.key", "rb") as keyFile:
        key = keyFile.read()

    file = input("Enter file location: ")

    with open(file, "rb") as curFile:
        content = curFile.read()
        decrypted_content = Fernet(key).decrypt(content)
        
        with open(file, "wb") as curFile:
            curFile.write(decrypted_content)
            print(file, "has been decrypted!")