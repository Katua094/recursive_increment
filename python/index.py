def product(a,b):
    result=(a*b)
    return result

def add(x,y):
    result_1=(x+y)
    return result_1

def both(result,result_1):
    result_2= (result/result_1)
    print(f"your result is :{result_2}\n\n")


while True:
    a= int(input("input your first numerator::"))
    b= int(input("input yor second nimerator:: "))
    x= int(input("onput your first denomenator:: "))
    y= int(input ("input your second denomenator:: "))

    result = product(a, b)
    result_1 = add(x, y)
    both(result, result_1)


    product(a,b)
    add(x,y)
    both(result,result_1)
    quit=input("do you want to quit?: (yes) or(no)").lower()

    if quit =="yes":
        break
    else:
        continue
    
    