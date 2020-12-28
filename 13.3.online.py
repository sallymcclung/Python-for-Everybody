"""
Exercise 13.3.online: In this assignment you will write a Python program somewhat similar
to geojson.py. The program will prompt for a locatation, contact a web service and retrieve
json for the web service and parse that data, and retrieve the first place_id from the json.
A place id is a textual identifier that uniquely identifies a place as within Google Maps.
To complete this assignment, you should use this API endpoint that has a static subset of
the Google data:

http://py4e-data.dr-chuck.net/json?

This API uses the same parameter (address) as the Google API. This API has no rate limit,
and if you visit the site with no parameters, you get 'No address' response. To call the API,
you need to include a key= parameter and provide the address that you are requesting as the
address= parameter that is properly URL encoded using the urllib.parse.urlencode() function.
Make sure to check that your code is using the API endpoint as shown above. You will get
different results from the geojson and json endpoints, so make sure you are using the same
one as the autograder.
"""

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    placeid = js['results'][0]['place_id']
    print('Place ID:',placeid)
