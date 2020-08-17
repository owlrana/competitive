#Practice file to check code while taking lectures and notes. Code available for the last lecture and last check only.

import urllib.request, urllib.parse
fhand = urllib.request.urlopen('http://data.pr43.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())