import cmath
#Python Program to calculate the square root

#Note: change this value for a different result
num = 8

# To take the input from the user
#num = float(input('Enter a number: '))

num_sqrt = cmath.sqrt(num)
print('The square root of %0.3f is %0.3f'%(num, num_sqrt.real))

