"""
Exercise 5.2: Write another program that prompts for a list of numbers as
above and at the end prints out both the maximum and minimum of numbers
instead of the average.
"""

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" or num == "Done" :
        break
    try:
        fnum = float(num)
    except:
        print("Invalid input")
        continue

    if largest is None or largest < fnum:
        largest = fnum

    if smallest is None or smallest > fnum:
        smallest = fnum

print("Maximum is:",largest)
print("Minimum is:",smallest)
