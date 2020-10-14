# Replace a letter from one to another
# we are replacing all vowels to something a user inserts
def translate(phrase,  user_replacer):
    translation = ""
    #vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for letter in phrase:
        if letter.lower() not in "aeiou": #vowels:    
            translation += letter
        else:
            translation += user_replacer

    return translation

user_string = input("Please enter a string you want to remove vowels from: ")
user_replacer = input("Please enter the char you want to insert instead: ")
print(translate(user_string, user_replacer))