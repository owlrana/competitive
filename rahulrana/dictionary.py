# Dictionaries in Python
# Program to convert 3 Letter month name to full eg, Jan --> January

monthConversions = {
    "Jan" : "January", # Key : Value pair
    "Feb" : "Februar",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    9 : "September",
    "Oct" : "October",
    12.0 : "November",
    "Dec" : "December",
    #"Dec" : "Hello" ,....Dictionaries cannot be with duplicate keys
    # You can also put numbers as keys, not just strings but ints as well
}

print(monthConversions)
print(monthConversions[9])

print(monthConversions.get("Dec")) # You can have default values if key is not mapped in dictionary
print(monthConversions.get("Luv", "DEFAULT VALUE"))
