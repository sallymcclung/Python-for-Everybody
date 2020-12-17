"""
Exercise 6.3: Encapsulate this code in a function named count, and generalize
it so that it accepts the string and the letter as arguments.
"""

def counter(word, letter):
    count = 0
    for char in word:
        if char == letter:
            count = count + 1
    return count

word = input("Enter a word: ")
letter = input("Enter a letter: ")

result = counter(word, letter)
print(result)
