def greet(name):
    """
    This function greets to the person passed in as a parameter
    """
    print("Hello, " + name + ". Good Morning!")

greet('Paul')

#doc string 
print(greet.__doc__)


def absolute_value(num):
    """
    This function returns the absolute value of the entered number
    """
    if num >= 0:
        return num
    else:
        return -num        

print(absolute_value(2))        
print(absolute_value(-4))        