# Importing all the modules and function we will be using
from guess_number_practice import gn
from rps import rps
import sys


def arcade(name="player_one"):
    in_arcade = False

    while True:
        if in_arcade == True:
            print(f"\n{name} welcome back to the arcade menu")

        user_choice = input(
            f"\n{name}, choose a game:\n\n1 = Rock Paper Scissors\n\n2 = Guess my number\n\nx = exit\n\n")

        if user_choice not in ["1", "2", "x"]:
            print(f"\n{name} please choose 1, 2, or x")
            return arcade(name)

        in_arcade = True

        if user_choice == "1":
            rock_paper_scissors = rps(name)
            rock_paper_scissors()
        elif user_choice == "2":
            guess_number = gn(name)
            guess_number()
        else:
            print(f"\nBye {name}!")
            sys.exit()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="This will allow the user to choose between two games."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()

    print(f"\n{args.name}, welcome to the arcade!")

    arcade(args.name)
