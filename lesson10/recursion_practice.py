# recursion happens when a function is called within itself
# recursion is a mathmatical concept
# Russian nesting doll

# Creating a function and passing one as a parameter
def add_one(num):

    # If statement if the num is greater than or equal to 9
    if (num >= 9):
        # Return num incrementing
        return num + 1

    # creating an object named total and assigning num + 1 as the value then printing total
    total = num + 1
    print(total)

    # Asking the function to return itself and pass in total as an argument
    # The return keyword allows us to get the value of this recursive function
    return add_one(total)


# Calling the function and passing 0 as an argument
# add_one(0) Only returns 1-9

mynewtotal = add_one(0)
print(mynewtotal)  # return 1-10
