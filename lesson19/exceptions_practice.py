class NotCoolError(Exception):
    pass


x = 2


try:
    raise NotCoolError("This is not cool man")
    # print(x/0)
    # if not type(x) is str:
    #     raise TypeError("Only strings are allowed")
except NameError:
    print("Name error means something is undefined")
except ZeroDivisionError:
    print("Do not divide by zero")
except Exception as error:
    print(error)
else:
    print("No errors!")
finally:
    print("I'm going to print with or without an error")
