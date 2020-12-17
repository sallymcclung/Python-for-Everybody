"""
Exercise 6.1: Write a while loop that starts at the last character in the string
and works its way backwards to the first character in the string, printing each
letter on a separate line, except backwards.
"""

string = input("Enter a string: ")
index = len(string) - 1
while index >= 0:
    letter = string[index]
    print(letter)
    index = index - 1
