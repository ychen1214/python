import datetime
from datetime import time 

datetime_object = datetime.datetime.now()
print(datetime_object)

date_object = datetime.date.today()
print(date_object)

print(dir(datetime))

d = datetime.date(2019,4,13)
print(d)

today = datetime.date.today()

print("Current date=", today)

timestamp = datetime.date.fromtimestamp(1326244364)
print("Date=", timestamp)

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)


# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)

# time(hour, minute and second)
b = time(11, 34, 56)
print("b =", b)

# time(hour, minute and second)
c = time(hour = 11, minute = 34, second = 56)
print("c =", c)

# time(hour, minute, second, microsecond)
d = time(11, 34, 56, 234566)
print("d =", d)

a = time(11, 34, 56)

print("hour =", a.hour)
print("minute =", a.minute)
print("second =", a.second)
print("microsecond =", a.microsecond)


'''
    %Y - year [0001,..., 2018, 2019,..., 9999]
    %m - month [01, 02, ..., 11, 12]
    %d - day [01, 02, ..., 30, 31]
    %H - hour [00, 01, ..., 22, 23
    %M - minute [00, 01, ..., 58, 59]
    %S - second [00, 01, ..., 58, 59]
'''


# current date and time
now = datetime.datetime.now()


t = now.strftime("%H:%M:%S")
print("time:", t)

s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", s1)

s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("s2:", s2)


date_string = "21 June, 2018"
print("date_string =", date_string)

date_object = datetime.datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)