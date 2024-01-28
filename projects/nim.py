#Exeptions


try:
    def divide(q,i):
    
        result=q/i
        return result
    
    divide(3,0)
except ZeroDivisionError:
    print("you cannot divide a nuber by zero!!")

