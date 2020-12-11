"""
Exercise 2.5: Write a program which prompts the user for a Celsius temperature, 
convert the temperature to Fahrenheit, and print out the converted temperature.
"""

celsius = input("Enter a Celsius temperature: ")
c = float(celsius)
f = (c * 9/5) + 32
print(f)
