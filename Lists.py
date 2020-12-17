# Structures / Lists to organise and keep track of them

friends = list ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
print(friends)

# Accessing elements
print(friends[0])

# indexing from the back of the list using negative sign (-1,-2)
print(friends[-1])

# Grabbing elements after the first
print(friends[1:])

# Grabbing elements 1 to 4
print(friends[1:4])

# Modifying elements
friends[1] = "Mike"
print(friends[1])

# List FUnctions
lucky_numbers = [4,8,15,16,23,42]
friends = list ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
print(friends)

# Extend function - Add on one list to another list
friends.extend(lucky_numbers)

# Append Function - Add on to the list with another element
friends.append("Creed")

# Insert Function
friends.insert(1, "Kelly")
print(friends)

# Remove Function
friends.remove("Jim")

# Clear Function\
friends.clear()

# POP Function - Removed the last element in the list
friends.pop()

# Checking if a element is in the list
print(friends.index("Kevin"))

# Counting number of times the element appears in the list
print(friends.count("Jim"))

# Sorting in order - Alphabetical order
friends.sort()
print(friends)

# Reverse the order of the list
friends.reverse()

# Copying the list and making a duplicate
friends2 = friends.copy()