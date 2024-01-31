# Car game, my guy
print("Hello! Drive, stop, or quit\n")

while True:
    game = input("Your game, bro: ").lower()

    if game == "drive":
        print("The car is driving!!\n")
    elif game == "stop":
        print("The car has stopped\n")
    elif game == "quit":
        break
    else:
        print("Invalid input. Please enter 'drive', 'stop', or 'quit'.\n")
