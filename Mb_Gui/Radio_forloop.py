from tkinter import*
root=Tk()
root.geometry("900x1600")

v=IntVar()
#b=Radiobutton(root,text="male",variable=v,value=1)
#b.pack()
#b1=Radiobutton(root,text="female",variable=v,value=2)
#b1.pack()
#b2=Radiobutton(root,text="both",variable=v,value=3)
#b2.pack()

for i in range(3):
	t="male"
	tt=t.replace("male","female")
	ttt="both"
	if i==0:
		t=t
	elif i==1:
		t=tt
	elif i==2:
		t=ttt	
	b=Radiobutton(root,text=t,variable=v,value=1+i)
	b.pack(anchor="w")



root.mainloop()