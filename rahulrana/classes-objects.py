# About python classes and objects
# Extremely useful, will make the program more organised and
# more powerful

# We have a lot of data types but not all of the data is not 
# represented by the available data types, what we can do with
# classes and objects is that we can create our own data type

# class is another data type that we want to use

# Let's say I want to represent a student as a data type

class Student:
    
    #initialise a function to know what a stud is in the program
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

# object is an actual student, class is just like a template