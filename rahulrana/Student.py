# in reference to Classes-Objects.py in this same folder

class Student:
    
    # initialise a function to know what a stud is in the program
    # basically this is assigning evey useful detail to our model
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    # this is a function of Student class, it is usually used to
    # give back info, change info and all
    def on_honour_roll(self): # self needs to be passed eveytime first
        if self.gpa >= 3.5:
            return True
        else:
            return False

    # this can be used as object.on_honour_roll() to get info