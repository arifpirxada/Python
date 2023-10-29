from tkinter import*
root=Tk()
root.geometry("900x1600")
root.title("Only Calculater")

def get(event):
	global scval
	text=event.widget.cget("text")
	k=(scval.get()+text)
	if text=="×":
		text=text.replace("×","*")
	elif text=="÷":
		text=text.replace("÷","/")
	if text=="=":
		if scval.get().isdigit():
			cc=int(scval.get())
		else:
			cc=eval(sc.get())
		scval.set(cc)
		sc.update()
	elif text=="Clear":
		pass
	elif text=="Del":
		scval.set("")
		sc.update()
	elif text=="Undo":
		scval.set(k)
		sc.update()	
	else:
		scval.set(k)
		sc.update()

l=Label(root,text="Calculater",bg="orange")
l.pack(fill=X)

scval=StringVar()
scval.set("")
sc=Entry(root,textvariable=scval,font=("lucida 30 bold"),borderwidth=4,relief="sunken")
sc.pack()

f=Frame(root,bg="violet",padx=10,pady=10)
f.pack(anchor=W)
			
b=Button(f,text="9",padx=50,pady=60,font=("lucida 10 bold"))
b.bind("<Button-1>",get)
b.pack(side=LEFT,padx=15,pady=10)

b=Button(f,text="8",padx=50,pady=60,font=("lucida 10 bold"))
b.bind("<Button-1>",get)
b.pack(side=LEFT,padx=15,pady=10)

b=Button(f,text="7",padx=50,pady=60,font=("lucida 10 bold"))
b.bind("<Button-1>",get)
b.pack(side=LEFT,padx=15,pady=10)

b=Button(f,text="Clear",padx=40,pady=60,font=("lucida 10 bold"),bg="yellow")
b.bind("<Button-1>",get)
b.pack(side=LEFT,padx=15,pady=10)

f=Frame(root,bg="violet",padx=10,pady=10)
f.pack(anchor=W)

b=Button(f,text="6",padx=50,pady=60,font=("lucida 10 bold"))
b.bind("<Button-1>",get)
b.pack(side=LEFT,padx=15,pady=10)

b=Button(f,text="5",padx=50,pady=60,font=("lucida 10 bold"))
b.bind("<Button-1>",get)
b.pack(side=LEFT,padx=15,pady=10)

b=Button(f,text="4",padx=50,pady=60,font=("lucida 10 bold"))
b.bind("<Button-1>",get)
b.pack(side=LEFT,padx=15,pady=10)

b=Button(f,text="+",padx=64,pady=38,font=("lucida 20 bold"))
b.bind("<Button-1>",get)
b.pack(side=LEFT,padx=15,pady=10)

f=Frame(root,bg="violet",padx=10,pady=10)
f.pack(anchor=W)

b=Button(f,text="3",padx=50,pady=60,font=("lucida 10 bold"))
b.bind("<Button-1>",get)
b.pack(side=LEFT,padx=15,pady=10)

b=Button(f,text="2",padx=50,pady=60,font=("lucida 10 bold"))
b.bind("<Button-1>",get)
b.pack(side=LEFT,padx=15,pady=10)

b=Button(f,text="1",padx=50,pady=60,font=("lucida 10 bold"))
b.bind("<Button-1>",get)
b.pack(side=LEFT,padx=15,pady=10)

b=Button(f,text="-",padx=66,pady=20,font=("lucida 25 bold"))
b.bind("<Button-1>",get)
b.pack(side=LEFT,padx=15,pady=10)

f=Frame(root,bg="violet",padx=10,pady=10)
f.pack(anchor=W)

b=Button(f,text="0",padx=50,pady=60,font=("lucida 10 bold"))
b.bind("<Button-1>",get)
b.pack(side=LEFT,padx=15,pady=10)

b=Button(f,text="%",padx=50,pady=60,font=("lucida 10 bold"))
b.bind("<Button-1>",get)
b.pack(side=LEFT,padx=15,pady=10)

b=Button(f,text="=",padx=46,pady=60,font=("lucida 10 bold"))
b.bind("<Button-1>",get)
b.pack(side=LEFT,padx=15,pady=10)

b=Button(f,text="×",padx=60,pady=26,font=("lucida 25 bold"))
b.bind("<Button-1>",get)
b.pack(side=LEFT,padx=15,pady=10)

f=Frame(root,bg="violet",padx=10,pady=10)
f.pack(anchor=W)

b=Button(f,text="Del",padx=35,pady=60,font=("lucida 10 bold"),bg="red")
b.bind("<Button-1>",get)
b.pack(side=LEFT,padx=15,pady=10)

b=Button(f,text="Undo",padx=21,pady=60,font=("lucida 10 bold"),bg="green")
b.bind("<Button-1>",get)
b.pack(side=LEFT,padx=15,pady=10)

b=Button(f,text=".",padx=51,pady=60,font=("lucida 10 bold"))
b.bind("<Button-1>",get)
b.pack(side=LEFT,padx=15,pady=10)

b=Button(f,text="÷",padx=57.3,pady=26,font=("lucida 25 bold"))
b.bind("<Button-1>",get)
b.pack(side=LEFT,padx=15,pady=10)








				



root.mainloop()