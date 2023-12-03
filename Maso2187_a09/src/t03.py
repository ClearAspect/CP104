"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roan Somers Mason
ID:      169072187
Email:   maso2187@mylaurier.ca
__updated__ = "2023-12-02"
-------------------------------------------------------
"""


# Imports
from functions import file_statistics

# Constants

file_handle = open("addresses.txt", "r", encoding="utf-8")

print(file_statistics(file_handle))

file_handle.close()
