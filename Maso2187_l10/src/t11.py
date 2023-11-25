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
from functions import find_longest

# Constants

fh = open("words.txt", "r+", encoding="utf-8")
print(find_longest(fh))