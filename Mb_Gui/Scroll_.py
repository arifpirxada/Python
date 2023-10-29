import random
from tkinter import*
root=Tk()
root.geometry("900x1600")

def add():
	b=random.randint(1,100)
	a=list.insert(END,b)
	return a
	
scroll=Scrollbar(root)
scroll.pack(side=RIGHT,fill=Y)
list=Listbox(root,yscrollcommand=scroll.set)
list.pack()
list.insert(END,"Who am i ")
scroll.config(command=list.yview)

Button(root,text="add",command=add).pack()



root.mainloop()