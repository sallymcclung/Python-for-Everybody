"""
Exercise 3.2: Rewrite your pay program using try and except so that your program
handles non-numeric input gracefully by printing a message and exiting the program.
The following shows two executions of the program:

Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input

Enter Hours: forty
Error, please enter numeric input
"""

hrs = input("Enter Hours: ")
try:
    h = float(hrs)
except:
    print("Error, please enter numeric input")
    quit()

rate = input("Enter Rate: ")
try:
    r = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

if h > 40.0:
    reg = 40 * r
    ot = (h - 40.0) * (r * 1.5)
    pay = reg + ot
else:
    pay = h * r

print("Pay:",pay)
