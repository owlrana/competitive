# this program makes use of the google maps api and is consumer centric

import urllib.request, urllib.parse, urllib.error
import json

servicourl = 'http://maps.googleapis.com/maps/api/geocode/json?' #gives us the json file for api use

while True:
    address = input('Enter Location: ')
    if len(address) < 1: break

    url = servicourl + urllib.parse.urlencode({'address': address }) #gives back and concatenates the servicourl with given address
    # address spaces need to be turned to + and commans into % and other stuff that is done by this urrlib.parse.urlencode

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('=== Failure to Retreive ===')
    print(data)
    continue

lat = js["results"][0]["geometry"]["location"]["lat"]
lng = js["results"][0]["geometry"]["location"]["lng"]
print('lat', lat, 'lng', lng)
location = js['results'][0]['formatted_address']
print(location)