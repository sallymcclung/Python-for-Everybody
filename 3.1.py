"""
Exercise 3.1: Rewrite your pay computation to give the employee 1.5
times the hourly rate for hours worked above 40 hours.

Enter Hours: 45
Enter Rate: 10
Pay: 475.0
"""

hrs = input("Enter Hours: ")
h = float(hrs)
rate = input("Enter Rate: ")
r = float(rate)

if h > 40.0:
    reg = 40 * r
    ot = (h - 40.0) * (r * 1.5)
    pay = reg + ot
else:
    pay = h * r

print("Pay:",pay)
