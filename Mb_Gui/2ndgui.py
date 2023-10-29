from tkinter import*
root=Tk()
root.geometry("644x344")

def getvals():
	print(userentry.get())
	print(passentry.get())
def exitt():
	exit()

l1=Label(text="Welcome",bg="black",fg="white",padx=256,pady=80,borderwidth=55,relief="sunken",font=('Arial',8,'bold'))
l1.grid()
f1=Frame(root,bg="blue",borderwidth=10,padx="200")
f1.grid()

l2=Label(f1,text='Please give your details',font=('Arial',8,'bold'))
l2.grid(row=0,column=1)

user=Label(root,text="Name")
user.grid(row=2,column=0)


uservalue=StringVar()
passvalue=StringVar()

userentry=Entry(root,textvariable=uservalue)


userentry.grid()
password=Label(root,text="password")
password.grid(row=9,column=0)
passentry=Entry(root,textvariable=passvalue)
passentry.grid(row=10)

l4=Label(root,text="")
l4.grid(row=15)

b1=Button(root,text="Submit",bg='green',fg='white',command=getvals())
b1.grid()

l2=Label(root,text="")
l2.grid(row=21)

wel="IQ pvt.limited"
l3=Label(root,text=wel,bg="yellow",fg="black",padx=275,pady=555,borderwidth=3,relief='sunken',font=('Cursive',8,'bold'))
l3.grid()

b2=Button(root,text='Exit',bg="red",command=exitt)
b2.grid(row=18)


root.mainloop()