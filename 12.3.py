"""
Exercise 12.3: Use urllib to replicate the previous exercise of (1) retrieving
the document from a URL, (2) displaying up to 3000 characters, and (3) counting
the overall number of characters in the document. Don't worry about the headers
for this exercise, simply show the first 3000 characters of the document contents.
"""

import urllib.request, urllib.parse, urllib.error

while True:
    URL = input('Enter the URL: ')
    parts = URL.split('/')
    first = parts[0]
    if first == 'http:':
        host = parts[2]
        document = ''
        for i in parts[3:]:
            document = document + '/' + i
        break
    elif first.startswith('www.'):
        host = parts[0]
        document = ''
        for i in parts[1:]:
            document = document + '/' + i
        break
    else:
        print('Invalid URL input')
        continue

try:
    fhand = urllib.request.urlopen(URL)
except:
    print('Invalid URL')
    quit()

alldata = ''
for line in fhand:
    data = line.decode()
    alldata = alldata + data
limit = alldata[:3000]
print(limit)
