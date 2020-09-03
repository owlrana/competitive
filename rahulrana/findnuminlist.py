#Program to find a number in the list

print('Please enter the number you want to find in the list')
findnum = int(input())

listofnum = [1,2,3,4,5,6,7,8,9,10]

place = 0
syn = None
#for item in listofnum:
#place = place + 1
if findnum in listofnum:
    for items in listofnum:
        place = place + 1
        if items == findnum:
            if items == 1:
                syn = 'st'
            elif items == 2:
                syn = 'nd'
            elif items == 3:
                syn = 'rd'
            else:
                syn = 'th'
            
            print('The number is found at', place, end = '')
            print(syn, 'place')
else:
    print('The number could not be found, sorry!')