# Importing the module argparse from Python
import argparse

# 
def hello(name, lang):
    greetings = {
        "English": "Hello",
        "Spanish": "Hola",
        "German": "Hallo",
    }
    msg = f"{greetings[lang]} {name}!"
    print(msg)

if __name__ == "__main__":
    print

    # Creating an object named parser and calling argumentparser method from the arparse module
    parser = argparse.ArgumentParser(
        description="Provides a personal greeting."
    )

    # Adding an argument that ist must contatin a name
    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="the name of the person to greet."
    )

    parser.add_argument(
        "-l", "--lang", metavar = "language",
        required = True, choices = ["English", "Spanish", "German"],
        help = "the langauage of tej greeting."
    )

    args = parser.parse_args()

    hello(args.name, args.lang)

    # # Creating an object name msg that has a string using the format method to collect the name from the argument
    # msg = f"Hello {args.name}!"

    # # Printing msg
    # print(msg)
