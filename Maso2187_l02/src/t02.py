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


temp_fahrenheit = int(input('Temperature (F): '))

"Convert to celsius"
temp_celsius = (temp_fahrenheit - FAHRENHEIT_FREEZING) * (5/9)
print('Temperature (C): ',temp_celsius)

