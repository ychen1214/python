import random

def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

uppercaseletter1 = chr(random.randint(65,90))
uppercaseletter2 = chr(random.randint(65,90))
lowercaseletter1 = chr(random.randint(97,122))
lowercaseletter2 = chr(random.randint(97,122))
number1 = chr(random.randint(48,57))
specialchar = chr(random.randint(58,64))


password = uppercaseletter1 + uppercaseletter2 + lowercaseletter1 + lowercaseletter2 + specialchar + number1
password = shuffle(password)
print(password)