# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

fname = input('Please input a file name')

try:
    fhandle = open(fname)
except:
    print('This file does not exist')
    exit()

count = 0
average = 0.00

for line in fhandle:
    if line.startswith('X-DSPAM-Confidence'):
        count += 1
        place = line.find(':') # to find where the colon is so we know the place of value
        value = float(line[place+1:].strip()) # 'line' should start at the next place where colon found, should be stripped of white spces then turned into float and stored as value
        average = average + value # First computing the sum as average in the loop
average = average / count # computing the real average now

print('Average spam confidence:', average)