# converting strings into upper lower, check etc

test_string = "Rahul Rana is idiot"

print(test_string.capitalize())
print(test_string.lower())
print(test_string.isupper())
print(len(test_string))
print(test_string.join("1"))

print(test_string[0])
try:
    print(test_string.index("idiot"))
except:
    print('')

print(test_string.replace("Rahul Rana", "Vibhor Kumar"))

