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

flyers = int(input("Number of flyers: "))
delivery_people = int(input("Number of delivery people: "))

flyers_per_person = flyers // delivery_people
leftover_flyers = flyers % delivery_people

print(f"Flyers per delivery person: {flyers_per_person}")
print(f"Flyers left over: {leftover_flyers}")