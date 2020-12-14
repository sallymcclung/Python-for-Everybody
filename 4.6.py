"""
Exercise 4.6: Rewrite your pay computation with time-and-a-half for overtime
and create a function called computepay which takes two parameters
(hours and rate).

Enter Hours: 45
Enter Rate: 10
Pay: 475.0
"""

def computepay(h, r):

    if h > 40.0:
        reg = 40.0 * r
        ot = (h - 40.0) * (r * 1.5)
        pay = reg + ot
        return pay
    else:
        pay = h * r
        return pay

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

pay = computepay(h, r)

print("Pay:",pay)
