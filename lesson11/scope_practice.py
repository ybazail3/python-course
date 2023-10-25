# Scope

name = "John"

# passing firstname as a parameter


def greeting(firstname):
    color = "purple"
    print(color)
    print(firstname)


# using "Jane" as an argument
greeting("Jane")
# print(color) # color is only aailable in the function greeting since is is a local variable if i try to run this i will get aan error

# Can call a global function inside a local function


def another():
    greeting("John")


another()

# In this case greeting function is local because it is inside another() function
# Don't pollute the global scope


def another():
    color = "blue"

    def greeting(name):
        print(color)
        print(name)

    greeting("John")


another()

# modify the assignemt of a variable inside of a function

count = 1


def another():
    color = "blue"
    global count  # use the global keyword first before modifying count
    count += 1  # Ex: count += 2 - this will not work because you're making a new variable and it has no value
    print(count)

    def greeting(name):
        nonlocal color  # use the nonlocal keword to reassign the value of color instead of making a new variable
        color = "red"
        print(color)
        print(name)

    greeting("John")


another()
