"""
Exercise 13.2.online: In this assignment you will write a Python program similar
to json2.py. The program will prompt for a URL, read the json data from that URL
using urllib and then parse and extract the comment counts from the json data,
compute the sum of the numbers in the file and enter the sum below.
"""

import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')

try:
    connection = urllib.request.urlopen(url)
except:
    print('Invalid URL')
    quit()

data = connection.read().decode()

try:
    js = json.loads(data)
except:
    js = None
    print('JSON Loading Error')
print(json.dumps(js, indent=4))

comments = 0
sum = 0
for i in js['comments']:
    comments = comments + 1
    count = int(i['count'])
    sum = sum + count
print('Comment count:',comments)
print('Sum:',sum)
