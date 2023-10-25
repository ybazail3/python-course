# Closures is a function having access to the scope of its parent
# function after the parent function has returned.
# This will include a nested function

def parent_function(person, coins):
    # coins = 3

    # "child function" local function
    def play_game():
        # Calling variable coins that is outside this function usinf keyword nonlocal to then modify the variable instead of cretaing a new one
        nonlocal coins
        coins -= 1

        # if statement
        if coins > 1:
            # str(coins) is making the value of coins into a string
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left.")
        else:
            print("\n" + person + " is out of coins.")

    # When we return play_game the closure is created
    return play_game


tommy = parent_function("Tommy", 3)
jenny = parent_function("Jenny", 5)

# calling tommy is essentially calling parent_function with a parameter of "Tommy" becasue that is the value assigned to the tommy variable
tommy()
tommy()

jenny()

tommy()
