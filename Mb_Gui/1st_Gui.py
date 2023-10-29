from tkinter import*
root=Tk()
root.geometry("644x344")
root.title("my gui")

def wow():
	with open('ggui.txt','w') as f:
		n=f.write("someone liked your gui")
		print(n)
		
l1=Label(text="my first",bg='black',fg='white',font=('Arial',45,'bold'),borderwidth=12,relief='sunken',pady=12,padx=56)
l1.pack()
a=Button(text="Like",command=wow)
a.pack(side='top')




root.mainloop()