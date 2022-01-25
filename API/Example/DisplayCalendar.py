# Program to display calendar of the given month and year

#importing calendar module
import calendar 

yy = 2014 #year
mm = 11 #month

#To  take the month and year input fromt he user
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))

#dispaly the calendar
print(calendar.month(yy,mm))