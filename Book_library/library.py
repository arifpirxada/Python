import json

class library:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Welcome {self.name}!\n")

    def listLib(self):
        with open("data/data.json", "r") as bks:
            dt = json.load(bks)
            for i in dt["books"]:
                print(i)
    
    def addBk(self):
        inputBk = input("Write book name: ")
        with open("data/data.json", "r") as bks:
            dt = json.load(bks)
            dt["books"].append(inputBk)
            with open("data/data.json", "w") as updateBks:
                json.dump(dt, updateBks)

    def getBk(self):
        bkName = input("Write book name: ")
        with open("data/data.json", "r") as bks:
            dt = json.load(bks)
            if bkName in dt["books"]:
                dt["books"].remove(bkName)
                with open("data/data.json", "w") as updateBks:
                    json.dump(dt, updateBks)
                    print(f"Congratulations! You now own the book: {bkName}. Please return the book after 30 days or you will have to pay a high price. Thank you!")
            else:
                print(f"Sorry the book, {bkName} is currently unavailable. Please come later!")

    def help(self):
        print("show - Lists all available books.")
        print("get - To get a book.")
        print("return - To return a book.")
        print("q - To quit.\n")

    def ask(self):
        while True:
            print("Press h for help.")
            userPrompt = input("Write your prompt: ")
            print("\n")
            if userPrompt == "q":
                break
            elif userPrompt == "h":
                self.help()
            elif userPrompt == "show":
                self.listLib()
            elif userPrompt == "get":
                self.getBk()
            elif userPrompt == "return":
                self.addBk()
            else:
                print(f"There is no command like {userPrompt}")