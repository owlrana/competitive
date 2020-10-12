# for loops in python, special loop to loop though different arrays, letters, etc
# #ForLoopsAreAwesome

for letter in "Rahul Rana":
    print(letter, end = "")

print("")

friends = ["Michael", "Jim", "Dwight"]
for elements in friends:
    print(elements)

for i in range(10, 1, -2):
    print(i)

for index in range(len(friends)):
    if index == 0:
        print("This is the first iteration!")
    else:
        print(friends[index])

