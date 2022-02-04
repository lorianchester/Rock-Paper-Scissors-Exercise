


#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#

def determine_winner(user_choice, computer_choice):
    #determines the winning choice between two valid choices from selectable options:
    #returns the winning choice (e.g. "paper") or none if there is a tie.
    
    #scissors beats rock
    if user_choice.lower() == "rock" and computer_choice == "scissors":
        result = "You wins!"

    elif computer_choice == "rock" and user_choice.lower() == "scissors":
        result = "Sorry! The computer won."
   
    #paper beats rock
    elif user_choice.lower() == "paper" and computer_choice == "rock":
        result = "You win!"

    elif computer_choice == "paper" and user_choice.lower() == "rock":
        result = "Sorry! The computer won."

    #scissors beats paper
    elif user_choice.lower() == "scissors" and computer_choice == "paper":
        result = "You win!"

    elif computer_choice == "scissors" and user_choice.lower() == "paper":
        result = "Sorry! The computer won."

    #rock v rock, paper v paper, and scissors v paper result in a "tie"
    else:
        result = "It's a tie!"
    
    return result

if __name__ == "__main__":
    
    #allow user to change their name
    import os

    player_name = os.getenv("PLAYER_NAME", default="Player One")

    #greet player with dashes for formatting
    print("-----------------")

    print("Welcome", player_name, "to my Rock-Paper-Scissors game!")

    # ASK FOR USER INPUT
    print("-----------------")

    user_choice = input("Please choose one of: 'rock', 'paper', 'scissors': ")

    # VALIDATIONS
    if user_choice.lower() != "rock" and user_choice.lower() != "paper" and user_choice.lower() != "scissors":
        print("Sorry! You must choose 'rock', 'paper', or 'scissors'.")
        exit()

    #print user choice    
    print(player_name, "chose:", user_choice)

    # COMPUTER CHOICE
    from random import choice

    options = ["rock", "paper", "scissors"]

    computer_choice = choice(options)

    #print computer choice
    print("Computer chose:", computer_choice)

    # DETERMINE THE WINNER
    #invoke the determine_winner function
    result = determine_winner(user_choice, computer_choice)

    # FINAL RESULTS
    print("-----------------")

    print(result)

    print("-----------------")

    print("Thanks for playing! Goodbye!")