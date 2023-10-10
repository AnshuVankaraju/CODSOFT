def addition(num1,num2):
    return num1+num2
def subtraction(num1,num2):
    return num1-num2
def multiplication(num1,num2):
    return num1*num2
def division(num1,num2):
    return num1%num2

print("Please the option\n"
      "1.Addition\n"
      "2.Subtraction\n"
      "3.Multiplication\n"
      "4.Division\n")
x=eval(input("Select the operations from 1,2,3,4\n"))
num1=eval(input("Enter the first number "))
num2=eval(input("Enter the second number "))
if x==1:
    print(f"The sum of {num1} and {num2} is {num1+num2}.")
elif x==2:
    print(f"The subtraction of {num1} and {num2} is {num1-num2}.")
elif x==3:
    print(f"The multiplication of {num1} and {num2} is {num1*num2}.")
elif x==4:
    print(f"The division of {num1} and {num2} is {num1%num2}.")
else:
    print("Invalid selection")

