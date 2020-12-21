"""
Exercise 9.4: Add code to the above program to figure out who has the most
messages in the file. After all the data has been read and the dictionary has
been created, look through the dictionary using a maximum and minimum loop
(see Chapter 5: Maximum and minimum loops) to find who has the most messages
and print how many messages the person has.

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195
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
    mydict[words[1]] = mydict.get(words[1],0) + 1

address = None
messages = None
for key, value in mydict.items():
    if messages is None or value > messages:
        address = key
        messages = value

print(address,messages)
