def add(x,y):
    result=x+y
    return result


def sutract(x,y):
    result = x-y
    return result
def divide(x,y):
    if y==0:
        print("number cant be divided by zero")
    else:
        result=x/y
    return result
def multiply(x,y):
    result=x*y
    return result

operation={
    "add":add(),
    "subtract":sutract(),
    "divide":divide(),
    "multiply":multiply()
}



def main():
    while True:
        user_input=input("what operation do you want ?").lower()
        x=input("put down the first number>>")
        y=input("putdown your second number>>")
