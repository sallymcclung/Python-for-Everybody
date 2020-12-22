"""
Exercise 10.3: Write a program that reads a file and prints the letters
in decreasing order of frequency. Your program should convert all the
input to lower case and only count the letters a-z. Your program should
not count spaces, digits, punctuation, or anything other than the letters
a-z. Find text samples from several different languages and see how letter
frequency varies between languages. Compare your results with the tables at
https://wikipedia.org/wiki/Letter_frequencies.
"""

fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:",fname)
    quit()

alphabet = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]
mydict = dict()
for line in fhand:
    line = line.lower()
    for character in line:
        if character not in alphabet:
            continue
        mydict[character] = mydict.get(character, 0) + 1

lst = list()
for key, value in mydict.items():
    lst.append((value, key))

lst.sort(reverse=True)

for value, key in lst:
    print(key, value)
