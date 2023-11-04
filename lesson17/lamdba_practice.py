# lambda keyword syntax: lambda arguments : expression
from functools import reduce
def squared(num): return num * num  # squared = lambda num : num * num


print(squared(2))  # 4


def addTwo(num): return num + 2  # addTwo = lambda num : num +2


print(addTwo(12))  # 14


def sumTotal(a, b): return a + b  # sum = lambda a, b : a + b


print(sumTotal(2, 2))

###############################################################################

# How to use lambdas


def funcBuilder(x):
    return lambda num: num + x


addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))

###############################################################################

lambda num: num * num

numbers = [3, 12, 6, 89, 20, 42]

# Map is a built in function and it receives a function as an argument
squared_nums = map(lambda num: num * num, numbers)

print(list(squared_nums))


###############################################################################

# returning the odd numbers
lambda num: num % 2 != 0

# The filter function will only return True
odd_nums = filter(lambda num: num % 2 != 0, numbers)

print(list(odd_nums))

###############################################################################

# Reduce adds all number together

lambda acc, curr: acc + curr

numbers = [1, 2, 3, 4, 5, 1]

total = reduce(lambda acc, curr: acc + curr, numbers, 10)

print(total)

print(sum(numbers, 10))  # This is a simpler solution

# This will return the amount of characters in the list

names = ["Yazmin", "John", "Jane", "Melody", "Anna"]

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)

print(char_count)
