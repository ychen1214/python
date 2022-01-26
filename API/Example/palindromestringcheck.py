# A Palindrome is a string that is the same read forward or backward

# Program to check if a string is a palindrome or not

my_str  = 'aIbohPhoBiA'

# make it suitable for caseless comparison
my_str = my_str.casefold()

#reverse teh string
rev_str = reversed(my_str)

#check if the string is equal to its reverse
if list(my_str) == list(rev_str):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome")    

