"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roan Somers Mason
ID:      169072187
Email:   maso2187@mylaurier.ca
__updated__ = "2023-09-27"
-------------------------------------------------------
"""


# Imports

# Constants

dirt = float(input("Enter amount of dirt (m^3): "))
gravel = float(input("Enter amount of gravel (m^3): "))
sand = float(input("Enter amount of sand (m^3): "))

total = dirt + gravel + sand
print("Material   Cubic Metres")
print(f"Dirt       {dirt:5.1f}")
print(f"Gravel     {gravel:5.1f}")
print(f"Sand       {sand:5.1f}")
print(f"Total      {total:5.1f}")