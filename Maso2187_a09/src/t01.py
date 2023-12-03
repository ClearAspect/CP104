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
from functions import file_top

# Constants

file_handle = open("students.txt", "r", encoding="utf-8")
file_top(file_handle, 5)

file_handle.close()
