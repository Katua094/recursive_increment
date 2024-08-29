import random

def guess_the_number():
    print("Welcome to Guess the Number Game!")
    print("I am thinking of a number between 1 and 100.")

    # Randomly generate a number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            # Ask the player for their guess
            player_guess = int(input("Enter your guess: "))
            attempts += 1

            # Check if the guess is correct
            if player_guess < number_to_guess:
                print("Too low! Try again.")
            elif player_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()
