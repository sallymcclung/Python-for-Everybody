"""
Exercise 13.1.online: In this assignment you will write a Python program somewhat
similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL
using urllib and then parse and extract the comment counts from the XML data,
compute the sum of the numbers in the file.
"""

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')

try:
    fhand = urllib.request.urlopen(url)
except:
    print('Invalid URL')
    quit()

data = fhand.read().decode()

tree = ET.fromstring(data)
comments = tree.findall('comments/comment')
print('Comment count:',len(comments))

sum = 0
for i in comments:
    count = int(i.find('count').text)
    sum = sum + count
print('Sum:',sum)
