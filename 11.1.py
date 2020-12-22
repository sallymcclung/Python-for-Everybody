"""
Exercise 11.1: Write a simple program to simulate the operation of the grep command
on Unix. Ask the user to enter a regular expression and count the number of lines
that matched the regular expression:

$ python grep.py
Enter a regular expression: ^Author
mbox.txt had 1798 lines that matched ^Author

$python grep.py
Enter a regular expression: ^X
mbox.txt had 14368 lines that matched ^X

$python grep.py
Enter a regular expression: java$
mbox.txt had 4175 lines that matched java$

=============== A Special Note ===============
Using line.rstrip() removes the whitespace at the end of each line, so when we use
this, it increases our matches for 'java$' from 4175 lines to 4218 lines. If you
comment out 'line = line.rstrip()', this eliminates the extra matches because any
'java' at the end of a line that includes trailing whitespace will no longer be
included in the matches.
"""

import re

fname = input('Enter the file name: ')
fhand = open(fname)
regex = input('Enter a regular expression: ')

linecount = 0
for line in fhand:
    # Comment this line out only when attempting to match the results from the third sample execution
    line = line.rstrip()
    if re.search(regex, line):
        linecount = linecount + 1

print(fname,'had',linecount,'lines that matched',regex)
