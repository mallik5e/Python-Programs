import calendar
y=int(input("enter the year : "))
print("*****CALENDER******")
cal=calendar.TextCalendar(calendar.MONDAY)
i=1
while i<=12:
    cal.prmonth(y,i)
    i+=1