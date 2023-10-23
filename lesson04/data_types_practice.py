import math  # Imports go at the top of the file

# String data type

# Literal assignment of values
first = "Yazmin"
last = "lname"


# print(type(first))
# ^prints <class 'str'.
# print(type(first) == str)
# ^prints True
# print(isinstance(first, str))
# ^prints True

# Constructor function
# pizza = str("Pepperoni")
# print(type(pizza))
# ^prints <class 'str'.
# print(type(pizza) == str)
# ^prints True
# print(isinstance(pizza, str))
# ^prints True

# Concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# Casting a number to a string
decade = str(2000)
print(type(decade))
print(decade)

statement = "I like R&B music from " + decade + "s."
print(statement)

# Mulitiple lines
multiline = """

I was just checking in.
                        All good?

"""
print(multiline)

# Escaping special characters
# \' = allows you to use ', \t = tab, \n = newline, \\ = allows you to use a backslash
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located'
print(sentence)

# String Methods
print(first)
print(first.lower())  # Turns string into lowercase
print(first.upper())  # Turns string into uppercase
print(first)

# Will return everything to poper case capatilizing ever first letter of a word
print(multiline.title())
print(multiline.replace("good", "ok"))  # replacing good with ok
print(multiline)

print(len(multiline))
multiline += "                            "
multiline = "                             " + multiline
print(len(multiline))

print(len(multiline.strip()))  # 57
print(len(multiline.lstrip()))  # 87
print(len(multiline.rstrip()))  # 88

# Build a menu
title = "menu".upper()
print(title.center(20, "="))  # ========MENU========
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

print("")

# String index values
print(first[1])  # indexes start at 0
print(first[-1])  # negative indexing starts at -1
print(first[1:-1])  # When providing a range the last index will not be listed
# When you leave the range empty it will return the rest of the string on either side
print(first[1:])

# Some methods return boolean data
print(first.startswith("Y"))  # Return True
print(first.endswith("n"))  # Return True
print(first.endswith("B"))  # Return False

# Boolean Data Type
myvalue = True
x = bool(False)
print(type(x))  # <class 'bool'>
print(isinstance(myvalue, bool))  # True

# integer type
price = 100
best_price = int(80)
print(type(price))  # <class 'int>
print(isinstance(price, int))  # True

# float type
gpa = 3.28
y = float(1.14)
print(type(gpa))  # <class 'float'>
print(isinstance(y, float))  # True

# complex type
comp_value = 5 + 3j
print(type(comp_value))  # <class 'complex'>
print(comp_value.real)  # 5.0
print(comp_value.imag)  # 3.0

# Built-in Fnctions for number

print(abs(gpa))  # 3.28
print(abs(gpa * -1))  # 3.28

print(round(gpa))  # 3

print(round(gpa, 1))  # 3.3 rounds to nearest decimal place

print(math.pi)  # 3.141592653589793
print(math.sqrt(64))  # 8.0
print(math.ceil(gpa))  # 4 rounds up
print(math.floor(gpa))  # 3 rounds down

# Casting a string to a number
zipcode = "11111"
zip_value = int(zipcode)
print(type(zip_value))  # <class 'int'>

# Error if you attempt to cast incorrect data
# zip_value = int("Seattle") =  Invalid literal
