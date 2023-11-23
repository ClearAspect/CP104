"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roan Somers Mason
ID:      169072187
Email:   maso2187@mylaurier.ca
__updated__ = "2023-11-20"
-------------------------------------------------------
"""
# Imports
from functions import append_max_num

# Constants

fh = open("numbers.txt", "r+", encoding="utf-8")
print(append_max_num(fh))
