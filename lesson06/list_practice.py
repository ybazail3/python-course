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
