import json
import getpass
import os

class TextColors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    RESET = '\033[0m'

class todo:

    # Functions
    # 1. authenticate
    # 2. list_tasks
    # 3. add_task
    # 4. delete_task_by_title
    # 5. delete_task_by_index
    # 6. restore_tasks
    # 7. help
    # 8. change_password
    # 9. ask

    def authenticate(self):
        with open("data/pass_setting.txt", "r") as pwset:
            if pwset.read() == '1':
                password = getpass.getpass("Password: ")

                with open("data/pass.txt", "r") as pw:
                    if password == pw.read():
                        print(TextColors.GREEN + "Access granted!\n" + TextColors.RESET)
                        self.ask()
                    else:
                        print(TextColors.RED + "Access denied!\n" + TextColors.RESET)
                        self.authenticate()
            else:
                self.ask()

    def list_tasks(self):
        with open("data/tasks.json", "r") as tasks:
            tks = json.load(tasks)
            
            i = 1
            for t in tks["tasks"]:
                print(TextColors.BLUE + f"{i}. " + TextColors.RESET + t)
                i += 1
            
            if i == 1:
                print(TextColors.RED + "No tasks found!" + TextColors.RESET)
    
    def add_task(self, title):
        with open("data/tasks.json", "r") as tasks:
            tks = json.load(tasks)
            tks["tasks"].append(title)
            with open("data/tasks.json", "w") as update_tks:
                json.dump(tks, update_tks)
                print(TextColors.GREEN + "Task added!" + TextColors.RESET)

    def delete_task_by_title(self, title):
        with open("data/tasks.json", "r") as tasks:
            tks = json.load(tasks)
            if title in tks["tasks"]:
                tks["tasks"].remove(title)
                with open("data/tasks.json", "w") as update_tks:
                    json.dump(tks, update_tks)
                    print(TextColors.GREEN + "Deletion successful!" + TextColors.RESET)
            else:
                print(f"Sorry! can't find task: '{title}'.")
                print(TextColors.RED + f"Sorry! can't find task: '{title}'." + TextColors.RESET)

    def delete_task_by_index(self, index):

        try:
            index = int(index)
        except ValueError:
            print(TextColors.RED + "Index is not a valid integer." + TextColors.RESET)
            return

        if index < 1:
            print(TextColors.RED + "Invalid index!" + TextColors.RESET)
            return
        
        with open("data/tasks.json", "r") as tasks:
            tks = json.load(tasks)
            if len(tks["tasks"]) >= index:
                tks["tasks"].remove(tks["tasks"][index - 1])
                with open("data/tasks.json", "w") as update_tks:
                    json.dump(tks, update_tks)
                    print(TextColors.GREEN + "Deletion successful!" + TextColors.RESET)
            else:
                print(TextColors.RED + "Invalid index!" + TextColors.RESET)

    def restore_tasks(self):
        with open("data/tasks.json", "w") as tasks:
            tasks.write('{"tasks": []}')
            print(TextColors.GREEN + "Restore successful!" + TextColors.RESET)
    
    def help(self):
        print(TextColors.BLUE + "show" + TextColors.RESET + " Lists all tasks.")
        print(TextColors.BLUE + "add [title]" + TextColors.RESET + " To add a task.")
        print(TextColors.BLUE + "del [index]" + TextColors.RESET + " Delete by index.")
        print(TextColors.BLUE + "delete [title]" + TextColors.RESET + " Delete by title.")
        print(TextColors.BLUE + "delal" + TextColors.RESET + " restore tasks.")
        print(TextColors.BLUE + "changepw" + TextColors.RESET + " change password.")
        print(TextColors.BLUE + "setpw [1/0]" + TextColors.RESET + " 1 - Always ask password; Press 0 - Never ask password")
        print(TextColors.BLUE + "exit" + TextColors.RESET + " To quit.\n")

    def change_password(self):
        prevPass =  getpass.getpass("Current password: ")
        with open("data/pass.txt", "r") as pw:
            if pw.read() == prevPass:
                newPass = getpass.getpass("New password: ")
                with open("data/pass.txt", "w") as pword:
                    pword.write(newPass)
                    print("Password changed!")
            else:
                print("Wrong password!")

    def password_setting(self, setting):
        if (setting == '1' or setting == '0'):
            with open("data/pass_setting.txt", "w") as pw:
                pw.write(setting)
                print(TextColors.GREEN + "Password setting changed!" + TextColors.RESET)
        else:
            print(TextColors.RED + "Invalid Choice" + TextColors.RESET)

    def ask(self):
        print("Press h for help.")

        while True:
            userPrompt = input("Write your prompt: ")
            print("\n")
            if userPrompt == "exit":
                break
            elif userPrompt == "h":
                self.help()
            elif userPrompt == "show":
                self.list_tasks()
            elif userPrompt[:4] == "del ":
                self.delete_task_by_index(userPrompt[4:])
            elif userPrompt[:7] == "delete ":
                self.delete_task_by_title(userPrompt[7:])
            elif userPrompt[:4] == "add ":
                self.add_task(userPrompt[4:])
            elif userPrompt == "changepw":
                self.change_password()
            elif userPrompt[:6] == "setpw ":
                self.password_setting(userPrompt[6:])
            elif userPrompt == "delal":
                self.restore_tasks()
            elif userPrompt == "cls":
                if os.name == 'posix':  # For Unix/Linux/Mac OS
                    os.system('clear')
                elif os.name == 'nt':  # For Windows
                    os.system('cls')
            else:
                print(TextColors.RED + f"Invalid command: {userPrompt}" + TextColors.RESET)