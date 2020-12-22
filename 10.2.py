"""
Exercise 10.2: This program counts the distribution of the hour of the day for
each of the messages. You can pull the hour from the "From" line by finding the
time string and then splitting that string into parts using the colon character.
Once you have accumulated the counts for each hour, print out the counts, one
per line, sorted by hour as shown below.

python timeofday.py
Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
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
    if len(words) < 6 or words[0] != "From":
        continue
    hour = words[5].split(":")[0]
    mydict[hour] = mydict.get(hour,0) + 1

lst = sorted(mydict.items())
for key, value in lst:
    print(key, value)
