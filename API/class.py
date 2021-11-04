class Person:
    "This is a person class"
    age = 10
    def greet(self):
        print('Hello')

#Output: 10
print(Person.age)

#Output: <function Person.greet>
print(Person.greet)

#Output: "This is a person class"
print(Person.__doc__)

# create a new object of Person class
harry = Person()

# Output: <function Person.greet>
print(harry.greet)

# Calling object's greet() method
# Output: Hello
harry.greet()