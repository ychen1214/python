#https://www.programiz.com/python-programming/examples/pyramid-patterns

rows = 5

for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print("\n")        




k = 0

for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")
   
    while k!=(2*i-1):
        print("* ", end="")
        k += 1
   
    k = 0
    print()    