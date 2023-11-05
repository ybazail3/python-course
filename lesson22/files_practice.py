import os
# r = Read
# a = Append
# w = Write
# x = Create

# Read - error if it doesnt exist
# t for text files or b for binary

f = open("names.txt")
# print(f.read())
# print(f.read(6))

# print(f.readline())
# print(f.readline())

for line in f:
    print(line)

f.close()

try:
    f = open("names.txt")
    print(f.read())

except:
    print("The file you want to read doesnt't exist")
finally:
    f.close()

# Append - Creates the file if it doesn't exist

# f = open("names.txt", "a")
# f.write("\nJohny\n")
# f.close()

f = open("names.txt")
print(f.read())
f.close()

# Write (overwrite)
f = open("context.txt", "w")
f.write("I deleted all if the context")
f.close()

f = open("context.txt")
print(f.read())
f.close()

# Two ways to create a new file

# Opens a file for writing, creates the file if it does not exist
f = open("name_list.txt", "w")
f.close()

# Creates the specified file, btu returns an error if the file already exists
if not os.path.exists("yazmin.txt"):
    f = open("yazmin.txt", "x")
    f.close()

# Delete a file

# avoid an error if it does not exist
if os.path.exists("yazmin.txt"):
    os.remove("yazmin.txt")
else:
    print("The file you wish to delete does not exist")

# With keyword

with open("more_names.txt") as f:
    content = f.read()

with open("names.txt", "w") as f:
    f.write(content)
