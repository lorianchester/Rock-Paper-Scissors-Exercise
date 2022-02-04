


#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#

def determine_winner(choice_1, choice_2):
    #determines the winning choice between two valid choices from selectable options:
    #returns the winning choice (e.g. "paper") or none if there is a tie.
    
    #scissors beats rock
    if choice_1.lower() == "rock" and choice_2.lower() == "scissors":
        result = "rock"

    elif choice_2.lower() == "rock" and choice_1.lower() == "scissors":
        result = "rock"
   
    #paper beats rock
    elif choice_1.lower() == "paper" and choice_2.lower()== "rock":
        result = "paper"

    elif choice_2.lower() == "paper" and choice_1.lower() == "rock":
        result = "paper"

    #scissors beats paper
    elif choice_1.lower() == "scissors" and choice_2.lower() == "paper":
        result = "scissors"

    elif choice_2.lower() == "scissors" and choice_1.lower() == "paper":
        result = "scissors"

    #rock v rock, paper v paper, and scissors v paper result in a "tie"
    else:
        result = None
    
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
    print(player_name, "chose:", user_choice.lower())

    # COMPUTER CHOICE
    from random import choice

    options = ["rock", "paper", "scissors"]

    computer_choice = choice(options)

    #print computer choice
    print("Computer chose:", computer_choice)

    # DETERMINE THE WINNER
    #invoke the determine_winner function to return the winning choice
    result = determine_winner(user_choice, computer_choice)

    #determine which player had the winning choice
    if result == None:
        winner = "It's a tie!"
    elif result == user_choice:
        winner = player_name + " wins!"
    else:
        winner = "Sorry! The computer won."


    # FINAL RESULTS
    print("-----------------")

    print(winner)

    print("-----------------")

    print("Thanks for playing! Goodbye!")