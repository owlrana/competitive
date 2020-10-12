# Function is  acollection of code that performs a specific task
# They are used so that we don't need to repeat things again and again
# Very core concept of programming in python

def printerz(user_string): # "user_string" is a parameter that is "passed" into the function
    print(user_string)

a_string = input("Please enter any string to get it printed!\n")

# You need to execute the function only then it will perform, it's called "calling"
print(printerz(a_string)) # output of this is None because we didn't return anything
# in the function, so by default it takes it as None type

# *****************************
# RETURN statement in functions:

def cube(num):
    return num*num*num
    print("This statement is never going to run dawg \_('')_/")

number = input("Please enter a number you want to get the cube of:\n")
print(cube(int(number)))

