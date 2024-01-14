import random
while True:

    choices=["rock","paper","scissors"]

    computer_choice=random.choice(choices)
    player_choice=None
    while player_choice not in choices:
        player_choice=input("rock,paper,scissors  ").lower()

    if computer_choice==player_choice:
        print(f"computer ::{computer_choice}")
        print(f" your choice::{player_choice}")
        print("its a tie nigga!!")
    elif computer_choice=="rock" and player_choice=="paper":
        print(f"computer ::{computer_choice}")
        print(f"your choice::{player_choice}")
        print("you win nigga ")
    elif computer_choice=="paper" and player_choice=="rock":
        print(f"computer ::{computer_choice}")
        print(f"your choice::{player_choice}")
        print("you loose nigga ")
    elif computer_choice=="scissors" and player_choice=="paper":
        print(f"computer ::{computer_choice}")
        print(f"your choice::{player_choice}")
        print("you lose my guy!!")
    elif player_choice=="scissors" and computer_choice=="paper":    
        print(f"computer ::{computer_choice}\n")
        print(f"your choice::{player_choice}\n")
        print("you win")
    elif computer_choice=="rock" and player_choice=="paper":
        print(f"computer::{computer_choice}")     
        print(f"your choice is:: {player_choice}")
        print("you win my guy!!")
    elif player_choice=="rock" and computer_choice=="paper":
        print(f"computer ::{computer_choice}")
        print(f"your choice::{player_choice}")
        print("you lose mada faka")
    play_again=(input("Do you want to play again? (yes) or (no)"))
    if play_again != "yes":
        break

print("good bye nigga")
            

