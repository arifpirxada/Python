from send_email import send_email

# Authenticate user

with open("data/sender.txt", "r") as sndr:
    sender = sndr.read()
    if sender == '0':
        sender = input("Sender's email: " + "\033[93m")
        with open("data/sender.txt", "w") as s:
            s.write(sender)
            print("\033[0m" + "Email has been saved!")

with open("data/app_password.txt", "r") as pw:
    password = pw.read()
    if password == '0':
        password = input("Sender's app password: " + "\033[93m")
        with open("data/app_password.txt", "w") as p:
            p.write(password)
            print("\033[0m" + "Password has been saved!")


subject = input("Email subject: " + "\033[93m")
print("\033[0m")
body = input("Email Body: " + "\033[93m")
print("\033[0m")

recipientsInput = input("Enter recipients seperated by ',' with no space: ")
recipients = recipientsInput.split(",")

send_email(subject, body, sender, recipients, password)