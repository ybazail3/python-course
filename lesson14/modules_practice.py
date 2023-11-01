# Importing class library (module) math
from math import pi
import sys
# Creating an alias for a module
import random as rdm
from enum import Enum
import california
from rps7 import rock_paper_scissors

print(pi)  # 3.141592653589793


for item in dir(rdm):
    print(item)  # this will print everything in that module

print(california.capital)
california.random_fun_fact()


# Every module has a name value
print(__name__)  # modules_practice.py named module is __main__

print(california.__name__)  # california is the name of the module

# We are importing the class library/module that we created  and calling it here the game will also run in this file.
rock_paper_scissors()
