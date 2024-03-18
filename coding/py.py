def add(x, y):
    result = x + y
    return result

def divide(x, y):
    result = x / y
    return result

def multiply(x, y):
    result = x * y
    return result

def subtract(x, y):
    result = x - y
    return result

while True:
    operation = input("What do you want to do? Type 'add', 'divide', 'multiply', 'subtract', or 'quit' to exit: ")

    if operation == "quit":
        break
    elif operation == "add":
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        print(f"Your answer is {add(x, y)}\n")
    elif operation == "divide":
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        print(f"Your answer is {divide(x, y)}\n")
    elif operation == "multiply":
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        print(f"Your answer is {multiply(x, y)}\n")
    elif operation == "subtract":
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        print(f"Your answer is {subtract(x, y)}\n")
    else:
        print("Invalid input\n")
