import random
import sys


def gn(name="player"):
    game_count = 0
    player_wins = 0
    comp_wins = 0

    def play_gn():
        nonlocal name
        nonlocal player_wins
        nonlocal comp_wins

        player_choice = input(f"\n{name}, guess a number 1, 2, or 3\n")

        # Catch if player does not choose 1, 2 , or 3
        if player_choice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3")
            return play_gn()

        # You will want to turn the string value of the user's iput into an integer
        player = int(player_choice)

        # You will want to use the random class libarary to have the computer choose a random number bewteen 1-3
        comp_choice = random.choice("123")

        comp = int(comp_choice)

        def player_guesses(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal comp_wins

            if player == computer:
                player_wins += 1
                return (f"{name}, you guessed correctly!")
            else:
                comp_wins += 1

                return (f"{name}, you guessed incorrectly.")

        game_result = player_guesses(player, comp)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\n{name}'s winning percentage: {player_wins/game_count:.2%}%")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\nComputer's wins: {comp_wins}")

        print(f"\n{name} do you want to play again?")

        while True:
            play_again = input(
                "\nTo play again enter Y for yes and Q to quit\n")

            # if player enters capital or lowercase it won't matter bc this will catch that
            if play_again.lower() not in ["y", "q"]:
                continue
            else:
                break

        if play_again.lower() == "y":
            return play_gn()
        else:
            print(f"\nBye {name}! Thank you for playing.")
            sys.exit()

    return play_gn


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing this game."
    )

    args = parser.parse_args()

    guess_number = gn(args.name)
    guess_number()
