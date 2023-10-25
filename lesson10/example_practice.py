# While loops and how they evaluate True and falso conditions
value = "y"
count = 0


while value:
    count += 1
    print(count)
    # if count is equal to 5 then breal else: move on to the next block of code
    if (count == 5):
        break
    else:
        # since 0 is equal to False the value = 0 will just end the while loop and go back to the begining
        value = 0
        continue
