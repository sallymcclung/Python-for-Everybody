"""
Exercise 12.1.online: In this assignment you will write a Python program to use
urllib to read the HTML from the data files below, and parse the data, extracting
numbers and compute the sum of the numbers in the file.
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

total = 0
tags = soup('span')
for tag in tags:
    content = int(tag.contents[0])
    total = total + content
print(total)
