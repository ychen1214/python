#Program to find the sum of all numbers stored in a list

#List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

#variable to store the sum
sum = 0

#iterate over the list
for val in numbers:
    sum = sum+val

print("The sum is", sum)    

print(range(10))
print(list(range(2,8)))
print(list(range(2,20,3)))

#Program to iterate through a list of using indexing

genre = ['pop','rock','jazz']

#iterate over the list using index
for i in range(len(genre)): #Len(genre) gets the list length / range gets range of items in list
    print("I like",genre[i])

#print(range(len(genre)))

for i in genre:    
    print("I like", i)    


#for else
#
digits = [0, 1, 5]    
for i in digits:
    print(i)
else:
    print("No items left.")    

#for else break
student_name = 'James'    
marks ={'James':90, 'Jules':55, 'Arthur': 77}
for student in marks:
    if student == student_name:
        print(marks[student])
        break
else:
    print('No entry with that name found.')            