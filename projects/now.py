import random

# Generate a random number between 10 and 100
guess_comp = random.randint(10, 100)

print("Welcome to my guessing game!\n")
print("Put down 'quit' in order to quit the game.")
print("Enter a number between 10 and 100.")

while True:
    user_input = input("What is your guess: ")

    # Check if the user wants to quit
    if user_input.lower() == 'quit':
        print("Thanks for playing. Goodbye!")
        break

    try:
        # Convert the user input to an integer
        guess = int(user_input)

        if guess == guess_comp:
            print("Congratulations! You guessed the correct number.")
            break
        elif guess_comp-guess>1 or 0:
            print("A little bit more!")
        elif guess-guess_comp>1 or 0:
            print("Less, less!")
        else:
            print("Your guess is not in the correct range.")

    except ValueError:
        print("Please enter a valid number or 'quit'.")
