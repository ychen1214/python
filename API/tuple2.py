import sys
from operator import itemgetter  
# sample Tuples
Tuple1 = ("A", 1, "B", 2, "C", 3)
Tuple2 = ("Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu")
Tuple3 = ((1, "Lion"), ( 2, "Tiger"), (3, "Fox"), (4, "Wolf"))
  
# print the sizes of sample Tuples
print("Size of Tuple1: " + str(sys.getsizeof(Tuple1)) + "bytes")
print("Size of Tuple2: " + str(sys.getsizeof(Tuple2)) + "bytes")
print("Size of Tuple3: " + str(sys.getsizeof(Tuple3)) + "bytes")


# print the sizes of sample Tuples
print("Size of Tuple1: " + str(Tuple1.__sizeof__()) + "bytes")
print("Size of Tuple2: " + str(Tuple2.__sizeof__()) + "bytes")
print("Size of Tuple3: " + str(Tuple3.__sizeof__()) + "bytes")



# Python3 code to demonstrate working of
# Sort tuple list by Nth element of tuple
# using sort() + lambda

# initializing list
test_list = [(4, 5, 1), (6, 1, 5), (7, 4, 2), (6, 2, 4)]

# printing original list
print("The original list is : " + str(test_list))

# index according to which sort to perform
N = 2

# Sort tuple list by Nth element of tuple
# using sort() + lambda
#test_list.sort(key = lambda x: x[N])
test_list.sort(key = itemgetter(N)) #https://docs.python.org/3/library/operator.html

# printing result
print("List after sorting tuple by Nth index sort : " + str(test_list))
