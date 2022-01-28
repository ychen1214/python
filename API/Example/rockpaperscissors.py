""" Rock Paper Scissors
---------------------------------------
"""

import random
import os 
import re 

os.system('cls' if os.name =='nt' else 'clear')

while(1 < 2):
    print ("\n")
    print ("Rock, Paper, Scissors - Shoot!")
    userChoice = input("Choose your weapon [R]ock, [P]aper, or [S]cissors: ")
    if not re.match("[srp]",userChoice.lower()):
        print("Please choose a letter:")
        print("[R]ock, [S]cissors or [P]aper.")
        continue 
    print("You chose: " + userChoice)    
    choices = ['R','P','S']
    oppChoice = random.choice(choices)
    print("I chose: " + oppChoice)
    if oppChoice == str.upper(userChoice):
        print("Tie! ")
    elif oppChoice == "R" and userChoice.upper == "P":     
        print("Wrecked!")
    elif oppChoice == "S" and userChoice.upper == "P":
        print("Cutted!")
    elif oppChoice == "P" and userChoice.upper == "R":
        print("Smacked!")
    else:
        print("Winnable!")        

