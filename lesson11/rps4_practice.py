# Rock, Paper,  Scissors using local and global scope

import sys
import random
from enum import Enum

# Creating a global variable
game_count = 0


def play_rps():

    class RPS(Enum):  # Syntax for this data is all caps
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    # Creating playerChoice object and asking the user a question where the user can then type in an input/value
    playerChoice = input(
        "\nEnter...\n1 for Rock\n2 for Paper, or\n3 for Scissors:\n\n")

    if playerChoice not in ["1", "2", "3"]:
        print("Please enter 1, 2, or 3.")
        return play_rps()

    # Creating an object named player and using the int() to turn playerChoice into an integer
    player = int(playerChoice)

    # Using the random class library to assign a random value of 1, 2, or 3 to object computerChoice
    computerChoice = random.choice("123")

    # Turning the string into an int data type with int()
    computer = int(computerChoice)

    # These line will print the player and computer choice
    print("\nYou chose " + str(RPS(player)).replace("RPS.", "") + ".")
    print("Python chose " + str(RPS(computer)).replace("RPS.", "") + ".\n")

    # if statement to check if user chooses 1(rock) and comp chooses 3(scissors) user will and so on for the rest of the values
    def decide_winner(player, computer):
        if player == 1 and computer == 3:
            return "🎉 You win!"
        elif player == 2 and computer == 1:
            return "🎉 You win!"
        elif player == 3 and computer == 2:
            return "🎉 You win!"
        elif player == computer:
            return "😲 Tie game!"
        else:
            return "🐍 Python wins!"

    #
    game_result = decide_winner(player, computer)

    print(game_result)

    # Going to modify the variable game_count
    global game_count
    # incrementing the amount of games played
    game_count += 1

    # Printing the game count with variable game_count value and converting it into a string
    print("\n Game count: " + str(game_count))

    print("\n Play again?")
    # Creating an object names play_again and asking the user if they want to keep playing Y for yes and Q for quit
    while True:
        play_again = input("\nPlay again?\nY for Yes or\nQ to Quit\n\n")
        # turning user input to lowercase and if the value is not q or y go back to the top of the while loop
        if play_again.lower() not in ["y", "q"]:
            continue
        else:
            break

    # Changing to users input into lowercase
    # if statment to say if y is chosen continue the game if q is chosen change the value of play_again to false, print thx for playing
    if play_again.lower() == "y":
        return play_rps()
    else:
        print("\n🎉🎉🎉🎉")
        print("Thank you for playing!\n")
        # This will exit you fully out of the game
        sys.exit("Bye! 👋")


play_rps()
