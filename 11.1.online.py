"""
Exercise 11.1.online: In this assignment you will read through and parse a
file with text and numbers. You will extract all the numbers in the file and
compute the sum of the numbers. The file contains much of the text from the
introduction of the textbook except that random numbers are inserted throughout
the text.
"""

import re

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print("File cannot be opened:",fname)
    quit()

total = 0
for line in fhand:
    line = line.rstrip()
    rev = re.findall('([0-9]*\.[0-9]+|[0-9]+)',line)
    if len(rev) == 0:
        continue
    for num in rev:
        num = float(num)
        total = total + num

print(total)
