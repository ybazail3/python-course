import sys
import random
from enum import Enum


class RPS(Enum):  # Syntax for this data is all caps
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


# While True or in the game have the user input a value to start
play_again = True

while play_again:

    # Creating playerChoice object and asking the user a question where the user can then type in an input/value
    playerChoice = input(
        "\nEnter...\n1 for Rock\n2 for Paper, or\n3 for Scissors:\n\n")

    # Creating an object named player and using the int() to turn playerChoice into an integer
    player = int(playerChoice)

    # if player is less than 1 or higher than 3 return "Please enter 1, 2, 3."
    if player < 1 or player > 3:
        sys.exit("Please enter 1, 2, or 3.")

    # Using the random class library to assign a random value of 1, 2, or 3 to object computerChoice
    computerChoice = random.choice("123")

    # Turning the string into an int data type with int()
    computer = int(computerChoice)

    # These line will print the player and computer choice
    print("\nYou chose " + str(RPS(player)).replace("RPS.", "") + ".")
    print("Python chose " + str(RPS(computer)).replace("RPS.", "") + ".\n")

    # if statement to check if user chooses 1(rock) and comp chooses 3(scissors) user will and so on for the rest of the values
    if player == 1 and computer == 3:
        print("You win 🎉!")
        # Can have as many elif statements elif = else if
    elif player == 2 and computer == 1:
        print("You win 🎉!")
    elif player == 3 and computer == 2:
        print("You win 🎉!")
    elif player == computer:
        print("Tied game! 😱")
        # Can only have one else statement else is meant to catch the last ...
    else:
        print("Python wins 🐍!")

    # Creating an object names play_again and asking the user if they want to keep playing Y for yes and Q for quit
    play_again = input("\nPlay again?\nY for Y or\nQ to Quit\n\n")

    # Changing to users input into lowercase
    # if statment to say if y is chosen continue the game if q is chosen change the value of play_again to false, print thx for playing
    if play_again.lower() == "y":
        continue
    else:
        print("\n🎉🎉🎉🎉")
        print("Thank you for playing!\n")
        play_again = False  # break would work as well
# This will exit you fully out of the game
sys.exit("Bye! 👋")
