# Using libraries that does all the socket work and makes web pages look more like a file
# These require BeautifulSoup to be downloaded, which can be done from: https://pypi.python.org/pypi/beautifulsoup4
# or can be locally installed through https://www.py4e.com/code3/bs4.zip and extracted into the local folder
#updating existing lib

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
