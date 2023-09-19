"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roan Somers Mason
ID:      169072187
Email:   maso2187@mylaurier.ca
__updated__ = "2023-09-13"
-------------------------------------------------------
"""
# Imports

# Constants
FAHRENHEIT_FREEZING = 32



temp_celsius = int(input('Temperature (C): '))

"""Convert to fahrenheit"""
temp_fahrenheit = (9/5)*temp_celsius+FAHRENHEIT_FREEZING
print('Temperature (F): ',temp_fahrenheit)

