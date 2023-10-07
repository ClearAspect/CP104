"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roan Somers Mason
ID:      169072187
Email:   maso2187@mylaurier.ca
__updated__ = "2023-10-06"
-------------------------------------------------------
"""


# Imports

# Constants

date = int(input("Enter a date in the format YYYYMMDD: "))

year = date // 10000
month = (date // 100) % 100
day = date % 100

print(f"The reformatted date: {year}/{month}/{day}")
