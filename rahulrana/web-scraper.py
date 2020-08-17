#building a web scraper (Make sure you do not scrape Amazon or Flipkart, will hut your connectivity and in some cases lose access to your machine) [Beautiful Soup]
# www.crummy.com

import urllib.request, urllib.error, urllib.parse

from bs4 import BeautifulSoup #Need to have beautiful soup installed

url = input('Enter - ')
html = urllib.request.urlopen(ulr).read() #reads the whole page without a for loop or some other stuff
soup = BeautifulSoup(html, 'html.parser') #turns html into a soup object named 'soup' with the format html.parser (recommended for HTMLs)

#To retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))