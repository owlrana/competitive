#Retrieving the pages and treating them as file using urllib library (makes the work a lot easier)

import urllib.request, urllib.parse

fhand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/known_by_Fikret.html')

#Now we can do anything like we used to do in python to a file,,, store numbers in as dictionary... make lists... whatever
for line in fhand:
    print(line)