def add(x, y):
    result = x + y
    return result

def subtract(x, y):
    result = x - y
    return result

def divide(x, y):
    if y == 0:
        print("Number can't be divided by zero")
    else:
        result = x / y
    return result

def multiply(x, y):
    result = x * y
    return result

operations = {
    "add": add,
    "subtract": subtract,
    "divide": divide,
    "multiply": multiply
}

def main():
    while True:
        user_input = input("What operation do you want? (add, subtract, divide, multiply, quit)").lower()

        if user_input == "quit":
            break

        if user_input in operations:
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))

            result = operations[user_input](x, y)
            print(f"Result: {result}")

        else:
            print("Invalid operation. Please choose add, subtract, divide, multiply, or quit.")

if __name__ == "__main__":
    main()








        
