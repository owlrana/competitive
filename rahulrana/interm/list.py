# lists in python

# to make and print the whole list at a single time
mylist = ["banana", "cherry", "apple"]
print(mylist)

# to iterate through each item in the list
for i in mylist:
    print(i)

# to check if an element is present or not
if "banana" in mylist:
    print("yes")
else:
    print("no")

# adds element at the end of the list
mylist.append("lemon")
print(mylist)

# inserts element at specific position
mylist.insert(1, "blueberry")
print(mylist)

# removes the element if found
mylist.remove("lemon")

# removes the last element of a list
mylist.pop()

# clears the whole list
mylist.clear()