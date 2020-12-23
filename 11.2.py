"""
Exercise 11.2: Write a program to look for lines of the form:

New Revision: 39772

Extract the number from each of the lines using a regular expression and the
findall() method. Compute the average of the numbers and print out the average
as an integer.

Enter file: mbox.txt
38549

Enter file: mbox-short.txt
39756
"""

import re

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print("File cannot be opened:",fname)
    quit()

total = 0
count = 0
for line in fhand:
    line = line.rstrip()
    rev = re.findall('^New Revision: ([0-9.]+)',line)
    if len(rev) == 0:
        continue
    for num in rev:
        num = float(num)
        total = total + num
        count = count + 1

average = int(total / count)
print(average)
