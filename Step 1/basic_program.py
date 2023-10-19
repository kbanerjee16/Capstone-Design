#python program

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x*y

def divide(x, y):
    return x/y

x = int(input("Enter first number "))
y = int(input("Enter second number "))
calculation = False

while calculation == False:
    operation = input("Enter an operation: ")

    if operation == "+":
        print(add(x, y))
        calculation = True
    elif operation == "-":
        print(subtract(x, y))
        calculation = True
    elif operation == "*":
        print(multiply(x, y))
        calculation = True
    elif operation == "/":
        print(divide(x, y))
        calculation = True
    else:
        print("Operation unrecognizable, try again")

print("thank you for using this program")