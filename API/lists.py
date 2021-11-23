# a list of programming languages
# ['Python','C++','Javascript']

# list of integers
my_list = [1, 2, 3]

# empty list
my_list = []

# list with mixed data types
my_list = [1, "Hello", 3.4]

# nested list
my_list = ["mouse", [8, 4, 5], ["a"]]

my_list = ["p", "r", "o", "b", "e"]

# first item
print(my_list[0])  # p

# third item
print(my_list[2])  # o

# fifth item
print(my_list[4])  # e

# Nested List
n_list = ["Happy", [2, 0, 1, 5]]

# Nested indexing
print(n_list[0][1])

print(n_list[1][3])


# Negative indexing in lists
my_list = ["p", "r", "o", "b", "e"]

# last item
print(my_list[-1])

# fifth last item
print(my_list[-5])


# List slicing in Python

my_list = ["p", "r", "o", "g", "r", "a", "m", "i", "z"]

# elements from index 2 to index 4
print(my_list[2:5])

# elements from index 5 to end
print(my_list[5:])

# elements beginning to end
print(my_list[:])


# Correcting mistake values in a list
odd = [2, 4, 6, 8]

# change the 1st item
odd[0] = 1

print(odd)

# change 2nd to 4th items
odd[1:4] = [3, 5, 7]

print(odd)

# Appending and Extending lists in Python
odd = [1, 3, 5]

odd.append(7)

print(odd)

odd.extend([9, 11, 13])

print(odd)


# Concatenating and repeating lists
odd = [1, 3, 5]

print(odd + [9, 7, 5])
# * repeats a list by the multiplier
print(["re"] * 3)

# Demonstration of list insert() method
odd = [1, 9]
odd.insert(1, 3)

print(odd)

odd[2:2] = [5, 7]

print(odd)
# Deleting list items
my_list = ["p", "r", "o", "b", "l", "e", "m"]

# delete one item
del my_list[2]

print(my_list)

# delete multiple items
del my_list[1:5]

print(my_list)

# delete the entire list
del my_list

# Error: List not defined
# print(my_list)
my_list = ["p", "r", "o", "b", "l", "e", "m"]
my_list.remove("p")

# Output: ['r', 'o', 'b', 'l', 'e', 'm']
print(my_list)

# Output: 'o'
print(my_list.pop(1))

# Output: ['r', 'b', 'l', 'e', 'm']
print(my_list)

# Output: 'm'
print(my_list.pop())

# Output: ['r', 'b', 'l', 'e']
print(my_list)

my_list.clear()

# Output: []
print(my_list)


my_list = ["p", "r", "o", "b", "l", "e", "m"]

# Output: True
print("p" in my_list)

# Output: False
print("a" in my_list)

# Output: True
print("c" not in my_list)


for fruit in ["apple", "banana", "mango"]:
    print("I like", fruit)

# this is list Comprehenstion
pow2 = [2 ** x for x in range(10)]
print(pow2)

# same as above code
pow2 = []
for x in range(10):
    pow2.append(2 ** x)

print(pow2)


pow2 = [2 ** x for x in range(10) if x > 5]
print(pow2)
