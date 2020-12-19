"""
Exercise 8.1: Write a function called chop that takes a list and modifies it,
removing the first and last elements, and returns None. Then write a function
called middle that takes a list and returns a new list that contains all but
the first and last elements.
"""

# Takes a list and modifies it, removing the first and last elements, returning None
# Does not create a new list
def chop(lst):
    del lst[0]
    del lst[-1]

# Takes a list and returns a new list that contains all but the first and last elements
def mid(lst):
    middle = lst[1:-1]
    return middle

lst_1 = ["a", "b", "c", "d", "e"]
lst_2 = ["a", "b", "c", "d", "e"]

choplst = chop(lst_1)
print(lst_1)           # Should be ['b', 'c', 'd']
print(choplst)         # Should be None

midlst = mid(lst_2)
print(lst_2)           # Should be ['a', 'b', 'c', 'd', 'e']
print(midlst)          # Should be ['b', 'c', 'd']
