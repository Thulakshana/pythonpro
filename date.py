import datetime
birth=datetime.date(2012,4,12)
print(birth)


today=datetime.date.today() #ada dawasa gannawa 
print(today)

print(birth.strftime('%A,%B %d,%Y'))

age=today-birth 
print(age)

print(today.isoweekday()) #ada dawase index eka 

#*************************************************************************************************
#time 
t=datetime.time(9,30,45,10000) 
print(t.hour) #time eka display karanwa

#***************************************************************************************************
#date time ekata pennanawa 
tt=datetime.datetime.today()
print(tt)

#***************************************************************************************************
t_date=datetime.timedelta(days=20)
print(t-t_date)

