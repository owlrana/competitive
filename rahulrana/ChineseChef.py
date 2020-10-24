# for chef.py
# we want to give chinese chef all functionalitiies of Cheff
# + some additional stuff
# but we dont want to copy paste the function from Cheff into here
# instead we can use the inheritance feature

from Cheff import Chef

class ChineseChef(Chef):

    # overwriting the Cheff functionality be redefining
    def make_special_dish(self):
        print("Chinese Chef can make special dishes, yes. LOL.")
    
    def make_fried_rice(self):
        print("The chef makes fried rice")