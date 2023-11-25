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
from functions import file_copy

# Constants

fh_1 = open("words.txt", "r", encoding="utf-8")
fh_2 = open("words_copy.txt", "w", encoding="utf-8")

file_copy(fh_1, fh_2)