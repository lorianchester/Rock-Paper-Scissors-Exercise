


#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#


print("Welcome 'Player One' to my Rock-Paper-Scissors game!")

# ASK FOR USER INPUT
user_choice = input("Please choose one of: 'rock', 'paper', 'scissors': ")
user_choice.lower()

# VALIDATIONS
if user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
    print("Sorry! You must choose 'rock', 'paper', or 'scissors'.")
    exit()

print("User chose: ", user_choice)

# COMPUTER CHOICE
from random import choice

options = ["rock", "paper", "scissors"]

computer_choice = choice(options)

print("Computer chose: ", computer_choice)

# DETERMINE THE WINNER

#scissors beats rock

if user_choice == "rock" and computer_choice == "scissors":
    result = "Player One wins!"

elif computer_choice == "rock" and user_choice == "scissors":
    result = "Sorry! The computer won."

#paper beats rock
elif user_choice == "paper" and computer_choice == "rock":
    result = "Player One wins!"

elif computer_choice == "paper" and user_choice == "rock":
    result = "Sorry! The computer won."

#scissors beats paper
elif user_choice == "scissors" and computer_choice == "paper":
    result = "Player One wins!"

elif computer_choice == "scissors" and user_choice == "paper":
    result = "Sorry! The computer won."

#rock v rock, paper v paper, and scissors v paper result in a "tie"
else:
    result = "It's a tie!"

# FINAL RESULTS
print(result)

print("Thanks for playing! Goodbye!")