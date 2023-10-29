''' Problem 4 : Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days'''

from datetime import date

first_date = date(2014, 7, 2)
second_date = date(2014, 7, 11)
days = second_date-first_date
da = str(days)

if ", 0:00:00" in da:
	day = da.replace(", 0:00:00","")
	print(day)


	
