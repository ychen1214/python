import timeit

def getExecutionTime():
    t = timeit.Timer("sayHello()", "from __main__ import sayHello")
    return t.timeit(2)

def sayHello():
    print("Hello")

print(getExecutionTime())