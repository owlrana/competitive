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
# and moves other elements ahead
mylist.insert(1, "blueberry")
print(mylist)

# removes the element if found
mylist.remove("lemon")

# removes the last element of a list
mylist.pop()

# clears the whole list
mylist.clear()

# reverses the order of the list
mylist.reverse()

# sorts original list in asc ord
mylist.sort()

# does not affect the older list
new_list = sorted(mylist)

# create new list with the same elements multiple times
mynewlist = [0] * 5 

# can merge two lists, concatenate
newlists = mylist + mynewlist

# list slicing, from 1 till 5 (not including 5) in 1 step forward
listone = [1, 2, 3, 4, 5, 6, 7, 8. 9, 0]
a = listone[1:5]

# same as before but steps change into every second from last
listone = [1, 2, 3, 4, 5, 6, 7, 8. 9, 0]
a = listone[1:5:-2]

# copying a list
list_org = ["banana", "cherry", "apple"]
list_cpy = list_org
# but if we change the cpy, it will also change original list
# because from "=" assignment both lists are assigned to the
# same location in memory
# so use copy method

list_cpy = list_org.copy()
# or
list_cpy = list(list_org)
# or
list_cpy = list_org[:]

# LIST COMPREHENSION
# create new list from existing list easily
list_a = [1, 2, 3, 4, 5, 6, 7]
list_b = [i*i for i in list_a]
# created a list with all elements squared