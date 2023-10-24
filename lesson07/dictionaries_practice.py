# Dictionaris are used to store values in key : value pairs looks similar to JSON
band = {
    "vocals": "Plant",
    "guitar": "Page"
}

# Using dict() to create a dictionary
band2 = dict(vocals="Plant", guitar="Page")

# Both will print {'vocals': 'Plant', 'guitar': 'Page'}
print(band)
print(band2)

print(type(band))  # <class 'dict'>
print(len(band))  # 2 for two key a: value pairs

# Access items
# Will get the values aligned with the keys
print(band["vocals"])
print(band["guitar"])

# List all keys
print(band.keys())  # dict_keys(['vocals', 'guitar'])

# List all values
print(band.values())  # dict_values(['Plant', 'Page'])

# List of key/valu pairs as a Tuple
print(band.items())  # dict_items([('vocals', 'Plant'), ('guitar', 'Page')])

# Verify if a key ixists in a dictionary
# Using the "in" keyword to check if keys/values are in the dict
print("guitar" in band)  # True
print("triangle" in band)  # False

# Change values
band["vocals"] = " Coverdale"
band.update({"bass": "JPJ"})
print(band)  # {'vocals': ' Coverdale', 'guitar': 'Page', 'bass': 'JPJ'}

# Remove items
print(band.pop("bass"))  # JPJ pop only returns the value that is removed
print(band)  # {'vocals': ' Coverdale', 'guitar': 'Page'}

band["drums"] = "Bonham"
print(band)

# this wll return a Tuple and popitem() will remove the last item
print(band.popitem())  # ('drums', 'Bonham')
print(band)  # {'vocals': ' Coverdale', 'guitar': 'Page'}

# Delete and Clear
band["drums"] = "Bonham"
del band["drums"]  # deletes band dict
print(band)

# The clear method will return and empty dict
band2.clear()
print(band2)

del band2  # will delete band2

# Copy Dictionaries

# Creates a reference
# Do not create a copy like this
# band2 = band
# print("Bady copy!")
# print(band2)
# print(band)

# band2["drums"] = "Yazmin"
# print(band)

# Do this instead!!!
band2 = band.copy()
band2["drums"] = "Yazmin"
print(band)  # {'vocals': ' Coverdale', 'guitar': 'Page'}
print(band2)  # {'vocals': ' Coverdale', 'guitar': 'Page', 'drums': 'Yazmin'}

# Or use the dict() constructor function
band3 = dict(band)
print("Good copy!")
print(band3)  # {'vocals': ' Coverdale', 'guitar': 'Page'}

# Nested dictionaries

mbr1 = {
    "name": "Plant",
    "instrument": "vocals"
}
mbr2 = {
    "name": "Page",
    "instrument": "guitar"
}
band = {
    "mbr1": mbr1,
    "mbr2": mbr2
}
# {'mbr1': {'name': 'Plant', 'instrument': 'vocals'}, 'mbr2': {'name': 'Page', 'instrument': 'guitar'}}
print(band)
print(band["mbr1"]["name"])  # Plant

# Sets

nums = {1, 2, 3, 4}

nums2 = set((1, 2, 3, 4))

print(nums)  # {1, 2, 3, 4}
print(nums2)  # {1, 2, 3, 4}
print(type(nums))  # <class 'set'>
print(type(nums2))  # <class 'set'>

# no duplicates allows in sets
nums = {1, 2, 3, 4}
print(nums)

# True is a duplicate of 1, False is duplicate of zero
nums = {1, True, 2, False, 3, 4, 0}
# {False, 1, 2, 3, 4}} False came before 0 that is why it is listed first
print(nums)

# Using "in" keyword
# Check if value is in the set
print(2 in nums)  # True

# But you cannot refer to an element in the set with an idez position or a key

# Add a new element to a set
nums.add(8)
print(nums)  # {False, 1, 2, 3, 4, 8}

# Add elements from one set to another
moreNums = {5, 6, 7}
nums.update(moreNums)
print(nums)  # {False, 1, 2, 3, 4, 5, 6, 7, 8}

# Can use update() with Lists, Tuples and Dictionaries too

# Merge two sets to create a new set
one = {1, 2, 3}
two = {5, 6, 7}

myNewSet = one.union(two)
print(myNewSet)

# Keep only the duplicate values of the two sets
# Changing the first set "one"
one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)  # {2, 3}

# Keep everything except the duplicates
# Changing the first set "one"
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)  # {1, 4}
