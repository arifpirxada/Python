import calendar
# Using calendar module !

year=int(input("Enter the year "))
month=int(input("Enter the month "))

frame=calendar.month(theyear=year,themonth=month,w=8,l=4)

print(frame)