users = ["John", "David", "Sarah"]

data = ["John", 24, True]

emptyList = []

print("Dave" in emptyList)  # False

print(users[0])  # John
print(users[-1])  # Sarah
print(users[-2])  # David

print(users.index("Sarah"))  # 2

print(users[0:2])  # ["John", "David"]
print(users[1:])  # ["David", "Sarah"]
print(users[-3:-1])  # ["John", "David"]

print(len(data))  # 3

users.append("Mary")
print(users)  # ['John', 'David', 'Sarah', 'Mary']

users += ["Richard"]
print(users)  # ['John', 'David', 'Sarah', 'Mary', 'Richard']

users.extend(["Robert", "Jimmy"])
# ['John', 'David', 'Sarah', 'Mary', 'Richard', 'Robert', 'Jimmy']
print(users)

# users.extend(data)
# print(users) 'John', 'David', 'Sarah', 'Mary', 'Richard', 'Robert', 'Jimmy', 'John', 24, True]

# ['Bob', 'John', 'David', 'Sarah', 'Mary', 'Richard', 'Robert', 'Jimmy'] this will add "Bob" to the begining of the list bc we said 0 index
users.insert(0, "Bob")
print(users)

# ['Bob', 'John', 'Mike', 'Alex', 'David', 'Sarah', 'Mary', 'Richard', 'Robert', 'Jimmy'] this added mike and Alex to the second and third position
users[2:2] = ['Mike', 'Alex']
print(users)

users[1:3] = ["Bella", "Tim"]
# ['Bob', 'Bella', 'Tim', 'Alex', 'David', 'Sarah', 'Mary', 'Richard', 'Robert', 'Jimmy']
print(users)

# Removing Data

users.remove('Bob')
# ['Bella', 'Tim', 'Alex', 'David', 'Sarah', 'Mary', 'Richard', 'Robert', 'Jimmy'] removed "Bob"
print(users)

print(users.pop())  # removes Jimmy because pop() method removes the last item
print(users)

del users[0]  # Removed Bella since it was the first item
print(users)

# del data
data.clear()
print(data)  # Returns an empty list but doesnt delete it fully []

users[1:2] = ["dave"]
users.sort()
# ['Alex', 'David', 'Mary', 'Richard', 'Robert', 'Sarah', 'Tim'] sorts alphabetically
print(users)

# This allows for lower or uppercase to be ordered correctly in alphbetical order
users.sort(key=str.lower)
print(users)

nums = [3, 32, 78, 1, 5]
nums.reverse()
print(nums)  # Returns the reverse order [5, 1, 78, 32, 3]

# nums.sort(reverse=True)
# print(nums) # Returns in descending order [78, 32, 5, 3, 1]

# [78, 32, 5, 3, 1] This doesn't change the original list just sorts it!!!
print(sorted(nums, reverse=True))
print(nums)  # [5, 1, 78, 32, 3]

# Creating a variable name numscopy to create a copy of a list
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]  # Slicing the full list and copying it

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)  # [1, 3, 5, 32, 78] sorted list
print(nums)

print(type(nums))  # <class 'list'>

myList = list([1, "str", True])
print(myList)  # [1, 'str', True]

# Tuples

myTuple = tuple(("Yazmin", 24, True))

anotherTuple = (1, 2, 3, 4, 2, 2)

print(myTuple)  # ('Yazmin', 24, True)
print(type(myTuple))  # <class 'tuple'>
print(type(anotherTuple))  # <class 'tuple'>

# Cannot change/add/modify values in a Tuple must turn into list and make changes then turn back into Tuple
newList = list(myTuple)
newList.append("Doe")
newTuple = tuple(newList)
print(newTuple)

# Unpacking Tuple

# Using the * to get the range that is why two got both values of 2 and 3 when the Tuple was (1, 2, 3, 4)
(one, *two, hey) = anotherTuple
print(one)  # 1
print(two)  # [2, 3]
print(hey)  # 4

# Counting how many occurences are inside the Tuple is this case 2 is inside anotherTuple 3 times!
print(anotherTuple.count(2))
