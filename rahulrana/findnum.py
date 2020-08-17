import re

fhand = open('just-a-file.txt')

sum = 0

for line in fhand:
    number = re.findall('[0-9]+', line)
    number = int(number[0])
    sum += number

print(sum)