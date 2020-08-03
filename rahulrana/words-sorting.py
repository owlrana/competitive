# 8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words 
# using the split() method. The program should build a list of words. For each word on each line check 
# to see if the word is already in the list and if not append it to the list. When the program completes, 
# sort and print the resulting words in alphabetical order.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt

fname = input("Enter file name: ")
fhandle = open(fname)

words_list = list()

for line in fhandle:
    for realwords in line.split():
        if not realwords in words_list:
            words_list.append(realwords)

words_list.sort()
print(words_list)