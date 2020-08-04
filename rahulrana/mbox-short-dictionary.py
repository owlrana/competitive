# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 
#'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's 
# mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using 
# a maximum loop to find the most prolific committer.

fname = input('Enter the name of file you want to open')
if fname == '':
    fname = "mbox-short.txt" #make sure a valid name is entered when I speed through
fhandle = open(fname)

email = dict()

for lines in fhandle:
    if lines.startswith('From') and not lines.startswith('From:'):
        requiredline = lines.split()
        reqemail = requiredline[1]
        email[reqemail] = email.get(reqemail, 0) + 1

highest = 0
highestemail = None
for key in email:
    if email[key] > highest:
        highest = email[key]
        highestemail = key

print(highestemail, highest)