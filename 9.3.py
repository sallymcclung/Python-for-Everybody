"""
Exercise 9.3: Write a program to read through a mail log, build a histogram
using a dictionary to count how many messages have come from each email address,
and print the dictionary.

Enter file name: mbox-short.txt
{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3, 'cwen@iupui.edu': 5,
'antranig@caret.cam.ac.uk': 1, 'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1, 'zqian@umich.edu': 4,
'stephen.marquard@uct.ac.za': 2, 'ray@media.berkeley.edu': 1}
"""

fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:",fname)
    quit()

mydict = dict()
for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != "From":
        continue
    if words[1] not in mydict:
        mydict[words[1]] = 1
    else:
        mydict[words[1]] = mydict[words[1]] + 1

print(mydict)
