"""
Exercise 12.2.online: Write a program that expands on urllinks.py. The program will use
urllib to read the HTML from the data files below, extract the href= values from the
anchor tags, scan for a tag that is in a particular position relative to the first name
in the list, follow that link and repeat the process a number of times and report the last
name you find.
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ')
count = int(input('Enter count - '))
position = int(input('Enter position - '))-1
html = urllib.request.urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')
sequence = list()

for i in range(count):
    link = tags[position].get('href', None)
    sequence.append(tags[position].contents[0])
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')

print(sequence[-1])
