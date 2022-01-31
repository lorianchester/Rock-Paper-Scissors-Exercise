


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
import random

options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)

print("Computer chose: ", computer_choice)

# DETERMINE THE WINNER

#scissors beats rock

if user_choice =="rock" and computer_choice == "scissors":
    winner = "Player One"

if computer_choice == "rock" and user_choice == "scissors":
    winner = "computer"

#paper beats rock
if user_choice == "paper" and computer_choice == "rock":
    winner = "Player One"

if computer_choice == "paper" and user_choice == "rock":
    winner = "computer"

#scissors beats paper
if user_choice == "scissors" and computer_choice == "paper":
    winner = "Player One"
if computer_choice == "scissors" and user_choice == "paper":
    winner = "computer"

#rock v rock, paper v paper, and scissors v paper result in a "tie"
if user_choice == "rock" and computer_choice == "rock":
    winner = "tie"
if user_choice == "paper" and computer_choice == "paper":
    winner = "tie"
if user_choice == "scissors" and computer_choice == "scissors":
    winner = "tie"

# FINAL RESULTS
if winner == "Player One":
    print("Player One wins!")
elif winner == "computer":
    print("Sorry! The computer won.")
else:
    print("It's a tie!")

print("Thanks for playing! Goodbye!")