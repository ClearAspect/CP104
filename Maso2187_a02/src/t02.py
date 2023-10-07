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


number = int(input("Enter a positive digit number: "))

digit_1 = number % 10
digit_2 = (number // 10) % 10

difference = digit_2 - digit_1

print(f"The difference of the digits of {number} is {difference}")
