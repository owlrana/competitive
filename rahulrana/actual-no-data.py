#to find the sum of all the numbers that appear in the file actula-no-data (the answer is 475674 with 98 numbers)

import re

name = input('Please input the file you want to open')
if name == '':
    name = 'actual-no-data.txt'
fhandle = open(name)

numlist = list() #to store the list of floating points
for line in fhandle:
    line = line.rstrip()
    stuff = re.findall('\S*?([0-9]+)\S*?', line) # extract lines that START WITH 'X-DSPAM....: ' then RETURN ONLY a floating number that is present one or more times in line
    numlist.extend(stuff)

#print(numlist)

sum = 0
count = 0
for integer in numlist:
    try:
        integer = int(integer)
        sum += integer
        count += 1
    except:
        print(integer)
print(sum)
print(count)