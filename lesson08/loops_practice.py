# A while loop will execute a block of code while a condition is True
value = 1
# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1  # incrementing everytime its going through the loop


# while value <= 10:
#     value += 1  # incrementing everytime its going through the loop
#     if value == 5:
#         continue
#     print(value)
# else:
#     print("value is now equal to " + str(value))

names = ["John", "Jane", "Tim"]
# for x in names:
#     print(x)  # John , Jane, Tim

# for x in "Mississippi":
#     print(x) # Will print each individual letter


# for x in names:
#     if x == "Jane":
#         break # this stops the iteration
#     print(x) # Only prints John

# continue stops the current iteration and moves on to the next
# for x in names:
#     if x == "Jane":
#         continue
#     print(x) # Only prints John and Tim

# Ranges
# for x in range(4):
#     print(x) # 0, 1, 2 ,3

# for x in range(2, 4):  # start at 2 and ends at 4
#     print(x) # 2 and 3

for x in range(0, 100, 5):  # start at 0 and counts to 100 in 5 increments
    print(x)  # 0, 5, 10 ,15 and so on
else:
    print("Glad that's over!")

# Nested Loops

names = ["John", "Jane", "Tim"]
actions = ["codes", "eats", "sleeps"]
#  # This for loop has another nested for loop that iterates through all names and actions. In the print function a senetence is concantenated as name first and action second
# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")
#         '''John codes.
# John eats.
# John sleeps.
# Jane codes.
# Jane eats.
# Jane sleeps.
# Tim codes.
# Tim eats.
# Tim sleeps.'''

for action in actions:
    for name in names:
        print(name + " " + action + ".")
'''John codes.
Jane codes.
Tim codes.
John eats.
Jane eats.
Tim eats.
John sleeps.
Jane sleeps.
Tim sleeps.'''
