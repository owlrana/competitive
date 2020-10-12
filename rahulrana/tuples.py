# Container where we can store diff values similar to lists but has differences from lists
# Tuples are immutable (cannot be modified at all, anything at all)
# Use tuples inspecial situations for data that is never going to change

coordinates = (4, 5, 6, 7) #This is now fixed it cannot be changed

print(coordinates)

print(coordinates[::-2])

try:
    coordinates[0] = 1
except:
    print("oops... cannot change tuples!")

