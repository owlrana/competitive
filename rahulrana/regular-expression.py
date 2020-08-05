# to extract the floating point values using regular expressions
import re

name = input('Please input the file you want to open')
if name == '':
    name = 'mbox-short.txt'
fhandle = open(name)

numlist = list() #to store the list of floating points
for line in fhandle:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line) # extract lines that START WITH 'X-DSPAM....: ' then RETURN ONLY a floating number that is present one or more times in line
    if len(stuff) !=1:  continue #the re.findall() returns a list, if the list has more then 1 floating point values then it is kinda garbage as we dont know what it picked up. Disregard it.
    num = float(stuff[0])
    numlist.append(num)

print(numlist)
print('Maximum is: ', ax(numlist))