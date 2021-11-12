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

def greet(name, msg="Good Morning!"):
    """
    This function greets to 
    the person with the
    provided message.

    If the message is not provided,
    it defaults to "Good Morning!"
    """
    print("Hello", name + ', ' + msg)


greet("Kate")
greet("Bruce","how do you do?")
#doc string 
print(greet.__doc__)


def greet2(*names):
    """
    This function greets all the person in the names tuple
    """
    #names is a tuple with arguments
    for name in names:
        print("Hello", name)
greet2("Monica","Luke","Steve","John")        
