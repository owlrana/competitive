# cannot be changed after creation

mytuple = ("max", 28, "Boston")
# or
mytuple1 = "max", 28, "Boston" # parenthisis are option

# this is not a tuple of 1 elements
mytuple2 = ("max") # this is recognised as a string
# this is a tuple of 1 element
mytuple3 = ("max",)

#Tuple can also be created from an existing list using an
# inbuilt function called tuple
mytuple4 = tuple(["Max", 28, "Boston"])

# gives the first item in the tuple
item = mytuple[0]
print(item)