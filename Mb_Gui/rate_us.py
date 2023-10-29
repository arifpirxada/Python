from tkinter import*
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("900x1600")

def mes():
	msg=tmsg.askquestion("rate us!","Do you want to rate us?")
	if msg=="yes":
		val=tmsg.askretrycancel("rate us!","Sorry, something went wrong.")
		if val:
			tmsg.showinfo("rate us!","Sorry,Try again later...")
		else:
			print("wohooo")
					
	else:
		tmsg.showinfo("rate us!","Have a great day ahead!.")

l1=Label(root,text="",bg="grey",pady=210)
l1.pack(fill="x")

f1=Frame(root,bg="green",borderwidth=2,relief="sunken")
f1.pack(fill=X)
	
l3=Label(f1,text="",bg="green",pady=5)
l3.pack(fill="x")

message = Label(f1,text="rate us!",padx=30,borderwidth=6,relief="sunken")
message.pack()

l = Label(f1,text="select the number of stars",bg="orange",padx=25,borderwidth=6,relief="solid")
l.pack()

l5=Label(f1,text="",bg="green")
l5.pack(fill=X)

s = Scale(f1,from_=1,to_=10,orient="horizontal",bg="indigo",fg="white")
s.pack(fill=X)

b = Button(f1,text="rate",bg="yellow",fg="black",padx=18,pady=2,borderwidth=6,relief="sunken",command=mes)
b.pack()

l3=Label(f1,text="",bg="green",pady=5)
l3.pack(fill="x")

l2=Label(root,text="",bg="grey",pady=260)
l2.pack(fill="x")


root.mainloop()