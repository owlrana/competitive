#Retrieving the pages and treating them as file using urllib library (makes the work a lot easier)

import urllib.request, urllib.parse

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')

#Now we can do anything like we used to do in python to a file,,, store numbers in as dictionary... make lists... whatever
counts = dict()
for line in fhand:
    words = line.decode().split() #All we need to add is decode because it is coming from the network world where UTF-8 is the standard
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)