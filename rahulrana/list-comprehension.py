#we can create a list of some iteration without using any loop

#normally we do this
h_letters = []

for letter in 'human':
    h_letters.append(letter)

print(h_letters)

#but by list comprehension
h_letters = [ letter for letters in 'human' ]
print(h_letters)