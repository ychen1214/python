from collections import namedtuple

Car = namedtuple('Car','color mileage')

my_car = Car('red',3912.4)

print(my_car.color)
print(my_car.mileage)
print(my_car)