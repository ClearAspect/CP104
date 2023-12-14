"""
-------------------------------------------------------
Testing for Task 7: line_lengths
-------------------------------------------------------
Author: Roan Mason
ID:     169072187
Email:  maso2187@mylaurier.ca
__updated__ = "2023-08-25"
-------------------------------------------------------
"""
# Imports

# your imports here
from t07_functions import line_lengths

# Your code here

fh_in = open("source.txt", "r", encoding="utf-8")
fh_short = open("source_short.txt", "w", encoding="utf-8")
fh_long = open("source_long.txt", "w", encoding="utf-8")

print(line_lengths(fh_in, fh_short, fh_long, 16))

fh_in.close()
fh_short.close()
fh_long.close()
