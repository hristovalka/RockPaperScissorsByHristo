import random

user_choice = ""
computer_choice = ""
outcome = ""

while (user_choice != "rock" and user_choice != "paper" and user_choice != "scissors"):
    user_choice = input("Enter your choice (rock, paper, scissors): ")

computer_choice = ["rock", "paper", "scissors"][random.randint(0, 2)]

if (user_choice == computer_choice):
    outcome = "draw"
elif (user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "scissors" and computer_choice == "paper") or \
        (user_choice == "paper" and computer_choice == "rock"):
    outcome = "win"
else:
    outcome = "lose"

print(f"You chose {user_choice}. The computer chose {computer_choice}. The outcome is {outcome}.")
