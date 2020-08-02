#7.1 Write a program that prompts for a file name, then opens that file and reads through the file, 
# and print the contents of the file in upper case. Use the file words.txt to produce the output below.
#You can download the sample data at http://www.py4e.com/code3/words.txt

fname = input('Enter the name of the file you want to read:\n')

try:
    fhandle = open(fname)
except:
    print('You should have input a valid file name')
    quit()

for line in fhandle:
    fline = (line.upper()).rstrip()
    print(fline)