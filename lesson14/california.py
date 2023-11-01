# Importing choice function from random class libarary
from random import choice

# Creating variables
capital = "Sacramento"

bird = "California quail"

flower = "California poppy"

song = "I Love You California"

# Created a function names random_fun_facts that is a list of California fun facts


def random_fun_fact():
    fun_facts = [
        "The Hollywood Bowl is the largest outdoor amphitheater in the United States. When it opened in 1922, it was merely a simple wooden platform with a canvas top!",
        "Wondering what the name of the world's largest tree is? It's General Sherman, and it lives in Sequoia National Park! At nearly 275 feet tall and a circumference of 102 feet, it's certainly a large tree!",
        "In 1964, San Francisco's cable cars were named the first moving National Historic Landmark. The San Francisco cable cars are the only ones still operating in a U.S city.",
        "California is the birthplace of the internet. In 1969, the first ARPANET message was sent from a UCLA site."
    ]

    # Creating the index object and randomly choosing 0-4 with choice function
    index = choice("0123")

    # Printing fun_facts list and turning the value into an integer
    print(fun_facts[int(index)])


print(__name__)

# This will only run __name__ is equal to __main__ then it will run random_fun_fact function. This should usually always be equal to main since we are talking about this file.
if __name__ == "__main__":
    random_fun_fact()
