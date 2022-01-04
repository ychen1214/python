import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!", sys.exc_info()[0],"occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)        


#can have multiple except statements
#has a raise error clause
#has finally caluse