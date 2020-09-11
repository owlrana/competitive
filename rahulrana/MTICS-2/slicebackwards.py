#Reverse a string with & without using arrays

##############################
# You can either do this thing where we slice
##############################
txt = input('Input a string: ')
newTxt = txt[::-1]
print(newTxt)

##############################
# or do this approach which is kind of traditional
##############################

length = int(len(txt))
print(length)
revTxt = ""
check = True

while check == True:
    revTxt = revTxt + txt[length - 1]
    length = length - 1
    if length == 0:
        check = False

print(revTxt)