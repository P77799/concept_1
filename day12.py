#input from user
#input from computer
#Result print
#cases
#if rock and rock then draw
#if rock and paper then paper win etc etc

import random

item_list = ["Rock", "Paper", "Scissors"]

user_choice = input("Enter your move = Rock, Paper or Scissors: ").capitalize()
computer_choice = random.choice(item_list)

print(f"user_choice = {user_choice}\ncomputer_choice = {computer_choice}")

if user_choice == computer_choice:
    print("Match Draw")
elif user_choice == "Rock":
    if computer_choice == "Paper":
        print("Paper wins")
    else:
        print("Rock wins")
elif user_choice == "Paper":
    if computer_choice == "Scissors":
        print("Scissors wins")
    else:
        print("Paper wins")
elif user_choice == "Scissors":
    if computer_choice == "Rock":
        print("Rock wins")
    else:
        print("Scissors wins")
else:
    print("Invalid move! Please choose Rock, Paper or Scissors.")