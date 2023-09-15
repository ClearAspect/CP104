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
LARGE_COST = 75
SMALL_COST = 50

num_large_dogs = int(input('Number of large dogs groomed: '))
num_small_dogs = int(input('Number of small dogs groomed: '))

total_income = (num_large_dogs * LARGE_COST) + (num_small_dogs * SMALL_COST)
print(f'Total earned for the day: ${total_income:d}')