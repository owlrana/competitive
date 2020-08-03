#8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 
# 'From ' like the following line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out the second word in the line 
# (i.e. the entire address of the person who sent the message). Then print out a count at the end.
#Hint: make sure not to include the lines that start with 'From:'.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt

fname = input("Enter file name: ")
if len(fname) < 2 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
email_list = list()

for lines in fh:
    if lines.startswith('From'):
        email = lines.split()
        if email[1] in email_list: 
            continue
        else:
            email_list.append(email[1])
            print(email[1])
        count += 1
    email = None
print("There were", count, "lines in the file with From as the first word")
