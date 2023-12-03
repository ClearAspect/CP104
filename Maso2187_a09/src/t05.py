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
from functions import student_stats

# Constants

file_handle = open("students.txt", "r", encoding="utf-8")
print(student_stats(file_handle))
