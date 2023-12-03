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
from functions import line_numbering

# Constants

file_handle = open("wilde.txt", "r")
file_handle2 = open("wilde_numbered.txt", "w")
line_numbering(file_handle, file_handle2)
