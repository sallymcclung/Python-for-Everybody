"""
Exercise 9.1: Download a copy of the file www.py4e.com/code3/words.txt

Write a program that reads the words in words.txt and stores them as keys
in a dictionary. It doesn't matter what the values are. Then you can use
the in operator as a fast way to check whether a string is in the dictionary.
"""

fhand = open("words.txt")

mydict = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in mydict:
            mydict[word] = 1
        else:
            mydict[word] = mydict[word] + 1

while True:
    checkword = input("Enter the word to be checked for: ")
    if checkword == "done" or checkword == "Done":
        break
    if checkword in mydict:
        print("True")
    else:
        print("False")
