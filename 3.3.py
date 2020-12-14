"""
Exercise 3.3: Write a program to prompt for a score between 0.0 and 1.0.
If the score is out of range, print and error message. If the score is
between 0.0 and 1.0, print a grade using the following table:

Score    Grade
>= 0.9   A
>= 0.8   B
>= 0.7   C
>= 0.6   D
 < 0.6   F

Enter score: 0.95
A

Enter score: perfect
Bad score

Enter score: 10.0
Bad score

Enter score: 0.75
C

Enter score: 0.5
F

Run the program repeatedly as shown above to test the various
different values for input.
"""

score = input("Enter score: ")
try:
    score = float(score)
except:
    print("Bad score")
    quit()

if score > 0.0 and score <= 1.0:
    if score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    else:
        print("F")
else:
    print("Bad score")
