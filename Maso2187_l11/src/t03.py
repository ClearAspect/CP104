"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roan Somers Mason
ID:      169072187
Email:   maso2187@mylaurier.ca
__updated__ = "2023-11-30"
-------------------------------------------------------
"""
# Imports
from functions import generate_matrix_num, print_matrix_num

# Constants

matrix = generate_matrix_num(3, 4, -10, 10, "float")
print_matrix_num(matrix, "float")

print("\n")

matrix = generate_matrix_num(3, 4, -10, 10, "int")
print_matrix_num(matrix, "int")
