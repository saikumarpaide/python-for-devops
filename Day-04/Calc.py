num1 = int(input("Imput First Number :-    "))
num2 = int(input("Input Second Number :-   "))

def addition(num1, num2):
    return num1 + num2



def substraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def module(num1, num2):
    return num1 % num2


print("Addition = "+str(addition(num1, num2)))
print("Substraction = "+str(substraction(num1, num2)))
print("Multiplication = "+str(multiplication(num1, num2)))
print("Module = " +str(module(num1,num2)))