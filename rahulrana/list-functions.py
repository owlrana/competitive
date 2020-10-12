# Functions in lists in python

lucky_numbers = [4, 18, 315, 16, 253, 42, 87, ]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

print(friends)

# lists are very important so there are a lot of in built functions for lists
# to extend the elements of a list with another lists' contents
friends.extend(lucky_numbers)
print(friends)

friends.append("End")
print(friends)

friends.insert(1, "Kelly")
print(friends)

friends.remove("Kevin")
friends.remove("Karen")
print(friends)

friends.pop()
print(friends)

friends.clear()
print(friends)

friends.insert(1, "Rahul")
friends.index("Rahul")
print(friends)

print(friends.count("Rahul"))
friends.append("Rahul")
print(friends.count("Rahul"))

lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy()
print(friends2)
