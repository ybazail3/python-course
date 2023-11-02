# Rock, Paper,  Scissors

import sys
import random
from enum import Enum

# Function rps is passing through a name argument


def rps(name="player_one"):
    # Creating local variables
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():

        # Added name since it is a global function
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):  # Syntax for this data is all caps
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        # Creating playerChoice object and asking the user a question where the user can then type in an input/value
        playerChoice = input(
            f"\n{name}, please enter... \n1 for Rock\n2 for Paper, or\n3 for Scissors:\n\n")

        if playerChoice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3.")
            return play_rps()

        # Creating an object named player and using the int() to turn playerChoice into an integer
        player = int(playerChoice)

        # Using the random class library to assign a random value of 1, 2, or 3 to object computerChoice
        computerChoice = random.choice("123")

        # Turning the string into an int data type with int()
        computer = int(computerChoice)

        # These line will print the player and computer choice using the format method
        print(f"\n{name}, you chose {
              str(RPS(player)).replace('RPS.', '').title()}.")
        print(
            f"Python chose {str(RPS(computer)).replace('RPS.', '').title()}.\n")

        # if statement to check if user chooses 1(rock) and comp chooses 3(scissors) user will and so on for the rest of the values

        def decide_winner(player, computer):
            # brining in outside variables to be modified
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins

            if player == 1 and computer == 3:
                # incrementing the player wins when the player in fact wins
                # Changed the player wins into format method to display the players name
                player_wins += 1
                return f"🎉  {name}, you win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"🎉  {name}, you win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"🎉  {name}, you win!"
            elif player == computer:
                return "😲 Tie game!"
            else:
                python_wins += 1
                return f"🐍 Python wins!\nSorry, {name}...😢"

        #
        game_result = decide_winner(player, computer)

        print(game_result)

        # Going to modify the variable game_count
        nonlocal game_count
        # incrementing the amount of games played
        game_count += 1

        # Printing the game count with variable game_count, player_wins, python_wins value and converting it into a string. using the format method {}
        print(f"\n Game count: {game_count}")
        print(f"\n {name}'s wins: {player_wins}")
        print(f"\n Python wins: {python_wins}")

        print(f"\n Play again, {name}?")
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
            sys.exit(f"Bye {name}! 👋")

    return play_rps


# This will only execute if we are in the rps7_practice.py file
if __name__ == "__main__":
    # Importing the argpase class library
    import argparse

    # Created a parser object passing through the argument method with a description
    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    # Add an argument that requires a name
    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )

    # Cretaing an args object and passing through the parse_args function
    args = parser.parse_args()

    # calling the function rps()
    # Using a closure
    # Passing through the arguments name so it is displayed in the terminal when it is called
    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()
