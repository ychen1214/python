class ComplexNumber:
    def __init__(self, r=0,i=0):
        self.real = r 
        self.imag = i

    def get_data(self):
        print(f'{self.real}+{self.imag}j')      
#Create a new ComplexNumber Object
num1 = ComplexNumber(2,3)        

#Call get_date() method
#Output: 2+3j
num1.get_data()

#Create anotehr ComplexNumber object
#and create a new attribute 'attr'
num2 = ComplexNumber(5)
num2.attr = 10 

#Output: (5, 0, 10)
print((num2.real, num2.imag, num2.attr))

#del num1.imag
#num1.get_data()