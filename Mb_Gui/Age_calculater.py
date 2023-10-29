import datetime as dt
from tkinter import*
root=Tk()
root.geometry("900x1600")
	
def like():
	pass
	
f1=Frame(root,bg="green",padx=260,pady=15)
f1.pack()

l1=Label(f1,text="Age calculater")
l1.pack()

f2=Frame(root,bg='yellow',padx=1)
f2.pack(anchor='nw')

b1=Button(f2,text="Like",padx=330,bg='blue',fg='yellow',borderwidth=6,command=like)
b1.pack(anchor='nw')

f3=Frame(root,bg="yellow",padx=1)
f3.pack(anchor='ne')

b2=Button(f3,text="Exit",padx=330,bg='red',borderwidth=6,command=exit)
b2.pack(anchor='nw')

photo=PhotoImage(file="20220601_085617.png")

l2=Label(image=photo,borderwidth=15,relief='raised',bg='green')
l2.pack(anchor='n')

name=Label(root,text='Name',padx=23)
name.pack(anchor='n')


nameval=StringVar()
dayval=StringVar()
monthval=StringVar()
yearval=StringVar()

nameentry=Entry(root,textvariable=nameval)
nameentry.pack(anchor='n')

day=Label(root,text='day')
day.pack(anchor='n')

dayentry=Entry(root,textvariable=dayval)
dayentry.pack(anchor='n')

month=Label(root,text='month')
month.pack(anchor='n')

monthentry=Entry(root,textvariable=monthval)
monthentry.pack(anchor='n')

year=Label(root,text='year')
year.pack(anchor='n')

yearentry=Entry(root,textvariable=yearval)
yearentry.pack(anchor='n')

l_=Label(root,text='')
l_.pack()

def final():
	name=nameentry.get()
	bd=man(name,dt.date(int(yearentry.get()),int(monthentry.get()),int(dayentry.get())))
	
	area=Text(master=root,height=3,width=40,bg="yellow",borderwidth=3,relief='raised')
	area.pack(anchor='n')
	message="Hey {bd}!. You are {age} years old! and you have spent {days} on this planet.".format(bd=name,age=bd.age(),days=bd.days())
	area.insert(END,message)
	
b3=Button(root,text='Calculate Age',bg='green',fg='yellow',command=final)
b3.pack(anchor='n')

class man():
	
	def __init__(self,name,birth):
		self.name=name
		self.birth=birth
		
	def age(self):
		today=dt.date.today()
		age=today.year-self.birth.year
		return age
	
	def days(self):
		today=dt.date.today()
		days=today-self.birth
		d=str(days)
		if ', 0:00:00' in d:
			e=d.replace(", 0:00:00","")
			return e

#f_=Frame(root,bg='grey',padx=74,pady=15)
#f_.pack(side='bottom',anchor='s')
#l__=Label(f_,text="For more visit OnlyAaru's youtube channel")
#l__.pack()



root.mainloop()