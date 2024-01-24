print("hello world")
print("Hello you?\n"+"how is your day going>> ")

while True:
    mood = input("yes or No: ")
    if mood.lower() == "yes":
        print("good, no need to be sad")
        break
    elif mood.lower() == "no":
        print("nobody cares, work harder!!")
        break
    else:
        print("Please enter 'yes' or 'no'")
