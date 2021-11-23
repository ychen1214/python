# Different types of tuples

# Empty tuple
my_tuple = ()
print(my_tuple)

# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

my_tuple = 3, 4.6, "dog"
print(my_tuple)

# tuple unpacking is also possible
a, b, c = my_tuple

# Accessing tuple elements using indexing
my_tuple = ("p", "e", "r", "m", "i", "t")

print(my_tuple[0])  # 'p'
print(my_tuple[5])  # 't'
# nested tuple
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
# nested index
print(n_tuple[0][3])  # 's'
print(n_tuple[1][1])  # 4

# Negative indexing for accessing tuple elements
my_tuple = ("p", "e", "r", "m", "i", "t")

# Output: 't'
print(my_tuple[-1])

# Output: 'p'
print(my_tuple[-6])

# Accessing tuple elements using slicing
my_tuple = ("p", "r", "o", "g", "r", "a", "m", "i", "z")

# elements 2nd to 4th
# Output: ('r', 'o', 'g')
print(my_tuple[1:4])

# elements beginning to 2nd
# Output: ('p', 'r')
print(my_tuple[:-7])

# elements 8th to end
# Output: ('i', 'z')
print(my_tuple[7:])

# elements beginning to end
# Output: ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
print(my_tuple[:])

my_tuple = (
    "a",
    "p",
    "p",
    "l",
    "e",
)

print(my_tuple.count("p"))  # Output: 2
print(my_tuple.index("l"))  # Output: 3

# Membership test in tuple
my_tuple = (
    "a",
    "p",
    "p",
    "l",
    "e",
)

# In operation
print("a" in my_tuple)
print("b" in my_tuple)

# Not in operation
print("g" not in my_tuple)

# Using a for loop to iterate through a tuple
for name in ("John", "Kate"):
    print("Hello", name)
