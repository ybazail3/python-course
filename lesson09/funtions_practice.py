# Functions are reusable blocks of code

# start function with the def keyword followed by the name of your function and () paranthesis : colon
def hello_world():
    print("Hello World!")


# Calling the function
hello_world()

# Putting parameters in the function num1 and num2
# parametes never change
# This function is resusable


def sum(num1, num2):  # parameter
    print(num1 + num2)


# # Passing through arguments 2 and 5
# # arguments (args) can change
# sum(2, 5)  # args. this will print 7
# sum(3, 9)
# sum(4, 10)

def sum(num1=0, num2=0):  # parameter
    if (type(num1) is not int or type(num2) is not int):
        return 0
    return (num1 + num2)


total = sum(7, 2)
print(total)

# Creating a function named mulitple_items and passing in *args = non keyword arguments. We are usinf * because we aren't sure how many arguments will be passed through


def multiple_items(*args):
    print(args)
    print(type(args))  # This will return tuple


multiple_items("Yazmin", "John", " Sarah")

# ** = kwargs = keyword arguments


def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))


mult_named_items(first="Jane", last="Doe")  # this will reurn dicitonary

# *args and **kwargs / from geeks for geeks


def myFun(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)


# Now we can use both *args ,**kwargs
# to pass arguments to this function :
myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")
