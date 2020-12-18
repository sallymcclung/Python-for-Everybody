"""
Exercise 7.2: Write a program to prompt for a file name, and then read
through the file and look for lines of the form:

X-DSPAM-Confidence: 0.8475

When you encounter a line that starts with 'X-DSPAM-Confidence:' pull apart
the line to extract the floating-point number on the line. Count these lines
and then compute the total of the spam confidence values from these lines.
When you reach the end of the file, print out the average spam confidence.

Enter the file name: mbox.txt
Average spam confidence: 0.894128046745

Enter the file name: mbox-short.txt
Average spam confidence: 0.750718518519

Test your file on the mbox.txt and the mbox-short.txt files.

=============== A Special Note ===============
There is a notable difference between the results in the exercise examples
from the book, and the results of my code. The average spam confidence
results from the examples in the book have been rounded to the 12th decimal
place, while my code gives you 16 decimal places. I chose to ignore this
discrepancy, as the instructions do not indicate we should perform rounding.
"""

fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:",fname)
    quit()

count = 0
sum = 0
average = 0
for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
        colonpos = line.find(":")
        num = float(line[colonpos + 1:].strip())
        count = count + 1
        sum = sum + num
average = sum / count

print("Average spam confidence:",average)
