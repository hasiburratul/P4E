"""
Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the
converted temperature.
"""

c = float(input('Enter Celcius Temperature:\n'))

#Fahrenheit=(Celsius * 9/5) + 32
f =  (c * 9/5) + 32

print('Temperature in Fahrenheit:',f)
