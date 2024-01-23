import random 

random_1=random.choice(1,90)
while True:
    force=input("enter to generate a number>>")
    try:
        if force:
            print(random_1)
        else:
            force=="quit"
            break
    except ValueError:
        if force=="quit":
            break